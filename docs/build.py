#!/usr/bin/env python3
"""Build every Word and PDF document of the book from its markdown source with one shared style.

    python3 docs/build.py            # build everything
    python3 docs/build.py Chapter3   # build only sources whose path contains "Chapter3"
    python3 docs/build.py --docx     # skip the PDF step

Sources: every *.md under docs/book/Word/<part>/ (front matter, chapters, back matter),
         docs/companion/Chapter*/Word/ and docs/companion/AnswerKey/Word/.
The whole book as one document is built by docs/build_book.py.
Outputs: the .docx next to the source; the PDF in the matching pdf/ folder
         (docs/book/pdf/<part>/ or docs/companion/ChapterN/pdf/).
Style:   docs/style/reference.docx (regenerate with docs/style/make_reference.py).
Needs:   pandoc, LibreOffice (soffice) for the PDF step.
"""
import os, subprocess, sys, tempfile
from pathlib import Path

DOCS = Path(__file__).resolve().parent
REF = DOCS / "style" / "reference.docx"


def sources():
    yield from sorted((DOCS / "book" / "Word").glob("*/*.md"))
    yield from sorted((DOCS / "companion").glob("Chapter*/Word/*.md"))
    yield from sorted((DOCS / "companion").glob("AnswerKey/Word/*.md"))


def pdf_dir(src: Path) -> Path:
    if src.is_relative_to(DOCS / "book"):
        return DOCS / "book" / "pdf" / src.parent.name
    return src.parent.parent / "pdf"


def build(src: Path, want_pdf: bool) -> None:
    docx = src.with_suffix(".docx")
    fmt = "markdown+hard_line_breaks+pipe_tables" if "companion" in src.parts else "markdown"
    subprocess.run(["pandoc", str(src), "-f", fmt, "-t", "docx", f"--reference-doc={REF}",
                    f"--resource-path={src.parent}", "-o", str(docx)], check=True)
    print("docx ", docx.relative_to(DOCS))
    if not want_pdf:
        return
    out = pdf_dir(src); out.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, HOME=tempfile.mkdtemp(prefix="lo-"))  # private profile: no clash with a running LibreOffice
    subprocess.run(["soffice", "--headless", "--norestore", "--convert-to", "pdf", "--outdir", str(out), str(docx)],
                   check=True, env=env, capture_output=True)
    print("pdf  ", (out / docx.with_suffix(".pdf").name).relative_to(DOCS))


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    want_pdf = "--docx" not in sys.argv
    if not REF.exists():
        sys.exit(f"missing {REF}; run docs/style/make_reference.py")
    for src in sources():
        if args and not any(a in str(src) for a in args):
            continue
        build(src, want_pdf)
