"""Shared helper: insert pandoc footnotes into a chapter markdown file and append a
'References and Attribution' section built from the same citation table.

Usage from a per-chapter script:
    from footnote_lib import apply
    apply(path, REFS, NOTES, epigraph_source="...")

REFS:  {key: "Full citation (author-date style)"}
NOTES: list of (anchor, [ref keys], optional note text). The marker [^n] is inserted
       immediately after the first (and only) occurrence of `anchor`. The footnote text is
       the full citation(s) joined by "; " with the note (if any) appended after a period.
The existing '# Figure Credits' section is converted into '## Figure Attribution' under
'# References and Attribution', followed by '## Epigraph' (if given) and '## References'
(every cited work, alphabetical).
"""
import re
from pathlib import Path


def apply(path, refs, notes, epigraph_source=None, figure_attribution=None):
    path = Path(path); text = path.read_text()
    assert "[^" not in text, f"{path.name} already has footnotes"
    used = []
    defs = []
    for i, item in enumerate(notes, 1):
        anchor, keys, *rest = item
        note = rest[0] if rest else None
        n = text.count(anchor)
        assert n == 1, f"anchor occurs {n} times: {anchor!r}"
        for k in keys:
            assert k in refs, f"unknown ref key {k}"
            if k not in used:
                used.append(k)
        body = "; ".join(refs[k].rstrip(".") for k in keys) + ("." if keys else "")
        if note:
            body = (body + " " + note) if body else note
        text = text.replace(anchor, anchor + f"[^{i}]", 1)
        defs.append(f"[^{i}]: {body}")
    # convert Figure Credits
    m = re.search(r"^# Figure Credits\n", text, re.M)
    if m:
        head, credits = text[: m.start()], text[m.end():].strip()
    else:
        assert figure_attribution, "no '# Figure Credits' section and no figure_attribution given"
        head, credits = text, figure_attribution.strip()
    out = head.rstrip() + "\n\n# References and Attribution\n\n## Figure Attribution\n\n" + credits + "\n"
    if epigraph_source:
        out += "\n## Epigraph\n\n" + epigraph_source.strip() + "\n"
    out += "\n## References\n\n"
    out += "\n\n".join(refs[k] for k in sorted(used, key=lambda k: refs[k].lower())) + "\n"
    out += "\n" + "\n\n".join(defs) + "\n"
    path.write_text(out)
    print(f"{path.name}: {len(defs)} footnotes, {len(used)} references")
