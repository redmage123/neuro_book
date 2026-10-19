#!/usr/bin/env python3
"""Build the whole book as one document: Word, PDF and EPUB, with a paged Contents,
a consolidated Bibliography and a page-referenced Index.

    python3 docs/build_book.py            # docx + pdf + epub
    python3 docs/build_book.py --no-epub

Sources: the front matter, Chapters 0-16 and the glossary under docs/book/Word/.
Outputs: docs/book/full/How_the_Brain_Learns.{md,docx,pdf,epub}
Style:   docs/style/reference_book.docx (regenerate with docs/style/make_book_reference.py).
Needs:   pandoc, LibreOffice (soffice), pdftotext.

The PDF is built three times. Pass 1 lays out the book with placeholder page numbers;
the Contents is then filled from where each heading landed in the PDF. Pass 2 confirms
the layout and supplies the pages for the Index, which pass 3 appends at the end (so it
cannot move anything before it). Contents lines end in a tab and a number and never wrap, so filling in the
numbers cannot move anything; the final pass checks that they still match.
"""
import os, re, subprocess, sys, tempfile
from pathlib import Path
from xml.sax.saxutils import escape

DOCS = Path(__file__).resolve().parent
WORD = DOCS / "book" / "Word"
OUT = DOCS / "book" / "full"
REF = DOCS / "style" / "reference_book.docx"
NAME = "How_the_Brain_Learns"

PARTS = [
    ("Part I", "Foundations", [0, 1, 2]),
    ("Part II", "The Machinery of Learning", [3, 4, 5]),
    ("Part III", "Mind and Behavior", [6, 7, 8, 9]),
    ("Part IV", "Brains and Machines", [10, 11]),
    ("Part V", "Synthesis", [12, 13, 14, 15]),
    ("Part VI", "A Case Study", [16]),
]
PAGEBREAK = '```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n'


def one(pattern):
    found = sorted(WORD.glob(pattern))
    assert len(found) == 1, (pattern, found)
    return found[0]


def split_yaml(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    meta = dict(re.findall(r'^(\w+): "(.*)"$', m.group(1), re.M))
    return meta, text[m.end():]


def sections(body):
    """Split markdown into (heading, text) pairs at level-1 headings."""
    parts = re.split(r"(?m)^(# .*)$", body)
    out = [("", parts[0])]
    for i in range(1, len(parts), 2):
        out.append((parts[i][2:].strip(), parts[i + 1]))
    return out


def norm(ref):
    return re.sub(r"[^a-z0-9]", "", ref.lower().replace("*", ""))


def chapter(n, bib):
    meta, body = split_yaml(one(f"Chapter{n}/*.md").read_text())
    folder = one(f"Chapter{n}/*.md").parent
    body = body.replace("](images/", f"]({folder}/images/")
    body = re.sub(r"\[\^(\d+)\]", rf"[^c{n}_\1]", body)
    main, sep, tail = body.partition("\n# References and Attribution\n")
    assert sep, n
    m = re.search(r"^\[\^c\d+_\d+\]: ", tail, re.M)
    notes, defs = (tail[: m.start()], tail[m.start():]) if m else (tail, "")
    notes, _, refs = notes.partition("\n## References\n")
    for item in (p.strip() for p in refs.strip().split("\n\n")):
        if item:
            bib.setdefault(norm(item)[:80], item)
    main = re.sub(r"(?m)^(#+) ", r"#\1 ", main)            # chapter sections become level 2
    notes = re.sub(r"(?m)^## ", "### ", notes)
    head = f"# Chapter {n}\n\n::: {{custom-style=\"Subtitle\"}}\n{meta['subtitle']}\n:::\n"
    sources = f"\n## Figure and Epigraph Sources\n{notes}\n" if notes.strip() else ""
    return PAGEBREAK + head + main + sources + "\n" + defs + "\n"


def toc_xml(entries, pages):
    """Contents as Word paragraphs with a dotted right tab to the page number."""
    xml = []
    for kind, label in entries:
        page = pages.get(label, "000")
        indent = '<w:ind w:left="360"/>' if kind == "chapter" else ""
        bold = "<w:rPr><w:b/></w:rPr>" if kind == "part" else ""
        before = '<w:spacing w:before="160" w:after="40"/>' if kind == "part" else '<w:spacing w:before="0" w:after="40"/>'
        xml.append(
            f'<w:p><w:pPr><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9350"/></w:tabs>{before}{indent}</w:pPr>'
            f'<w:r>{bold}<w:t xml:space="preserve">{escape(label)}</w:t></w:r>'
            f'<w:r>{bold}<w:tab/><w:t>{page}</w:t></w:r></w:p>')
    return "```{=openxml}\n" + "\n".join(xml) + "\n```\n"


def assemble(pages, index_md, for_epub=False):
    meta, front = split_yaml(one("Frontispiece/*.md").read_text())
    front = front.replace("](images/", f"]({WORD / 'Frontispiece'}/images/")
    glossary = split_yaml(one("BackMatter/*Glossary*.md").read_text())[1]
    bib, chapters, entries = {}, [], []
    for sec, _ in sections(front)[1:]:
        if sec not in ("Contents",):
            entries.append(("front", sec))
    for part, title, nums in PARTS:
        label = f"{part}: {title}"
        entries.append(("part", label))
        chapters.append(PAGEBREAK + f"# {label}\n")
        for n in nums:
            sub = split_yaml(one(f"Chapter{n}/*.md").read_text())[0]["subtitle"]
            entries.append(("chapter", f"Chapter {n}  {sub.split(': ')[0]}"))
            chapters.append(chapter(n, bib))
    entries += [("back", "Glossary"), ("back", "Bibliography")]
    if index_md is not None:
        entries.append(("back", "Index"))
    out = [f'---\ntitle: "{meta["title"]}"\nsubtitle: "{meta["subtitle"]}"\nauthor: "Braun Brelin"\n---\n']
    for sec, text in sections(front):
        if sec == "":
            out.append(text)
        elif sec == "Contents":
            if not for_epub:
                out.append(PAGEBREAK + "# Contents\n\n" + toc_xml(entries, pages))
        else:
            out.append(PAGEBREAK + f"# {sec}\n{text}")
    out += chapters
    out.append(PAGEBREAK + glossary.strip() + "\n")
    items = sorted(bib.values(), key=lambda s: norm(s))
    out.append(PAGEBREAK + "# Bibliography\n\n" + "\n\n".join(items) + "\n")
    if index_md is not None and not for_epub:
        out.append(PAGEBREAK + "# Index\n\n" + index_md)
    return "\n".join(out), entries


def render(md_text, stem, tmp):
    md = tmp / f"{stem}.md"; md.write_text(md_text)
    docx = tmp / f"{stem}.docx"
    subprocess.run(["pandoc", str(md), "-f", "markdown", "-t", "docx", f"--reference-doc={REF}", "-o", str(docx)], check=True)
    env = dict(os.environ, HOME=tempfile.mkdtemp(prefix="lo-"))
    subprocess.run(["soffice", "--headless", "--norestore", "--convert-to", "pdf", "--outdir", str(tmp), str(docx)],
                   check=True, env=env, capture_output=True)
    pdf = docx.with_suffix(".pdf")
    text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], check=True, capture_output=True, text=True).stdout
    return md, docx, pdf, text.split("\f")


def locate(entries, page_texts):
    """Page number (1-based) of each Contents entry: the first page, after the previous
    entry's page, with a line consisting of exactly that heading."""
    pages, start = {}, 1
    for kind, label in entries:
        target = label.split("  ")[0] if kind == "chapter" else label
        for i in range(start, len(page_texts)):
            if any(line.strip() == target for line in page_texts[i].splitlines()):
                pages[label] = str(i + 1)
                start = i
                break
        else:
            sys.exit(f"could not find the page of {label!r}")
    return pages


def build_index(page_texts, pages):
    first = int(pages[next(k for k in pages if k.startswith("Chapter 0"))])
    last = int(pages["Glossary"]) - 1
    flat = {p: re.sub(r"\s+", " ", page_texts[p - 1]) for p in range(first, last + 1)}
    glossary = split_yaml(one("BackMatter/*Glossary*.md").read_text())[1]
    terms = re.findall(r"(?m)^([^\s:#][^\n]*)\n\n:   ", glossary)
    lines = []
    for term in sorted(terms, key=str.lower):
        base = re.sub(r"\s*\(.*?\)", "", term).strip()
        abbr = re.findall(r"\(([A-Z][A-Za-z0-9-]+)\)", term)
        word = re.compile(r"(?<![A-Za-z])" + re.escape(base) + r"(?:e?s)?(?![A-Za-z])", re.I)
        # abbreviations match case-sensitively, so "LTP" does not hit inside ordinary words
        short = [re.compile(r"(?<![A-Za-z])" + re.escape(a) + r"s?(?![A-Za-z])") for a in abbr]
        hits = [p for p, t in flat.items() if word.search(t) or any(s.search(t) for s in short)]
        if not hits:
            continue
        ranges, run = [], [hits[0], hits[0]]
        for p in hits[1:]:
            if p == run[1] + 1:
                run[1] = p
            else:
                ranges.append(run); run = [p, p]
        ranges.append(run)
        shown = [f"{a}–{b}" if b > a else f"{a}" for a, b in ranges]
        more = ", and throughout" if len(shown) > 15 else ""
        lines.append(f"{term}, {', '.join(shown[:15])}{more}")
    return "\n\n".join(lines) + "\n"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="book-"))
    md, entries = assemble({}, None)
    *_, texts = render(md, "pass1", tmp)
    pages = locate([e for e in entries], texts)
    md, entries = assemble(pages, "")                    # reserve the Index entry in the Contents
    *_, texts = render(md, "pass2", tmp)
    pages2 = locate(entries, texts)                      # pass 2 already has an (empty) Index page
    if any(pages2[k] != pages.get(k, pages2[k]) for k in pages2 if k != "Index"):
        print("note: layout moved between passes; using pass-2 pages")
    index_md = build_index(texts, pages2)
    md, entries = assemble(pages2, index_md)
    md_path, docx, pdf, texts = render(md, NAME, tmp)
    final = locate(entries, texts)
    bad = [k for k in final if final[k] != pages2[k]]
    if bad:
        sys.exit(f"Contents page numbers do not match the final layout: {[(k, pages2[k], final[k]) for k in bad]}")
    for f in (md_path, docx, pdf):
        os.replace(f, OUT / f.name)
        print("wrote", (OUT / f.name).relative_to(DOCS))
    if "--no-epub" not in sys.argv:
        epub_md, _ = assemble(pages2, None, for_epub=True)
        src = tmp / "epub.md"; src.write_text(epub_md)
        cover = WORD / "Frontispiece" / "images" / "cajal_portrait.png"
        subprocess.run(["pandoc", str(src), "-f", "markdown", "-t", "epub3", "--toc", "--toc-depth=1",
                        "--split-level=1", f"--epub-cover-image={cover}", "-o", str(OUT / f"{NAME}.epub")], check=True)
        print("wrote", (OUT / f"{NAME}.epub").relative_to(DOCS))
    print(f"{len(texts) - 1} pages")


if __name__ == "__main__":
    main()
