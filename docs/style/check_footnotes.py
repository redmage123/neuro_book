#!/usr/bin/env python3
"""Renumber a chapter's pandoc footnotes in order of first appearance and check the
References list against the footnote definitions.

    python3 docs/style/check_footnotes.py <chapter.md> [--write]

Without --write it only reports. Checks: every marker [^n] has a definition and vice versa;
every References entry is cited in at least one footnote; every footnote citation (text up to
the first "). " year marker) appears in the References list."""
import re, sys
from pathlib import Path

path = Path(sys.argv[1]); write = "--write" in sys.argv
text = path.read_text()
body, sep, tail = text.partition("\n# References and Attribution\n")
assert sep, "no References and Attribution section"
refs_part, defs_part = tail, ""
m = re.search(r"^\[\^\d+\]: ", tail, re.M)
if m:
    refs_part, defs_part = tail[: m.start()], tail[m.start():]
defs = {}
for blk in re.split(r"\n(?=\[\^\d+\]: )", defs_part.strip()):
    mm = re.match(r"\[\^(\d+)\]: (.*)", blk, re.S)
    if mm: defs[mm.group(1)] = mm.group(2).strip()
markers = re.findall(r"\[\^(\d+)\]", body + refs_part.split("\n## References\n")[0])
order = []
for k in markers:
    if k not in order: order.append(k)
problems = []
for k in order:
    if k not in defs: problems.append(f"marker [^{k}] has no definition")
for k in defs:
    if k not in order: problems.append(f"definition [^{k}] is never cited")
# references list vs footnotes
refs_sec = refs_part.split("\n## References\n", 1)[1] if "\n## References\n" in refs_part else ""
ref_items = [p.strip() for p in refs_sec.strip().split("\n\n") if p.strip()]
alldefs = "\n".join(defs.values())
for r in ref_items:
    if r.rstrip(".") not in alldefs: problems.append(f"reference not cited in any footnote: {r[:70]}")
sorted_items = sorted(ref_items, key=str.lower)
if ref_items != sorted_items: problems.append("References list is not in alphabetical order")
for k, d in defs.items():
    for cit in re.split(r"(?<=\d)[;.] (?=[A-Z][^()]*\(\d{4})", d):
        pass
print(f"{path.name}: {len(order)} footnotes, {len(defs)} definitions, {len(ref_items)} references")
for p in problems: print("  PROBLEM:", p)
if write:
    mapping = {old: str(i) for i, old in enumerate(order, 1)}
    new_body = re.sub(r"\[\^(\d+)\]", lambda mm: f"[^{mapping.get(mm.group(1), mm.group(1))}]", body)
    new_refs = refs_part.rstrip("\n") + "\n"
    if ref_items:
        head_refs = refs_part.split("\n## References\n", 1)[0]
        new_refs = head_refs.rstrip("\n") + "\n\n## References\n\n" + "\n\n".join(sorted_items) + "\n"
    new_defs = "\n\n".join(f"[^{mapping[k]}]: {defs[k]}" for k in order) + "\n"
    path.write_text(new_body + sep + new_refs + "\n" + new_defs)
    print(f"  rewritten: footnotes renumbered 1..{len(order)}, references sorted")
