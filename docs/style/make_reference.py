#!/usr/bin/env python3
"""Build the house-style pandoc reference.docx from pandoc's default reference document."""
import subprocess, sys
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("reference.docx")
base = out.with_name("ref-default.docx")
subprocess.run(["pandoc", "-o", str(base), "--print-default-data-file", "reference.docx"], check=True)
doc = Document(str(base))
BODY, HEAD = "Cambria", "Calibri"
BLUE, DARK, BLACK = RGBColor(0x1F, 0x4E, 0x79), RGBColor(0x40, 0x40, 0x40), RGBColor(0, 0, 0)
byid = {s.style_id: s for s in doc.styles}

def st(sid):
    return byid[sid]

def setfont(s, name, size, bold=None, italic=None, color=None):
    f = s.font; f.name = name; f.size = Pt(size)
    rpr = s.element.get_or_add_rPr(); rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = rpr.makeelement(qn("w:rFonts"), {}); rpr.insert(0, rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), name)
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        rf.attrib.pop(qn(a), None)
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    if color is not None: f.color.rgb = color
    f.all_caps = False; f.small_caps = False

def para(s, before=None, after=None, line=None, align=None, left=None, right=None, keep=None, first=None):
    pf = s.paragraph_format
    if before is not None: pf.space_before = Pt(before)
    if after is not None: pf.space_after = Pt(after)
    if line is not None: pf.line_spacing = line
    if align is not None: pf.alignment = align
    if left is not None: pf.left_indent = Inches(left)
    if right is not None: pf.right_indent = Inches(right)
    if keep is not None: pf.keep_with_next = keep
    if first is not None: pf.first_line_indent = Inches(first)

setfont(st("Normal"), BODY, 11, color=BLACK); para(st("Normal"), before=0, after=8, line=1.15)
for sid in ("BodyText", "FirstParagraph"):
    setfont(st(sid), BODY, 11, color=BLACK); para(st(sid), before=0, after=8, line=1.15, left=0, first=0)
setfont(st("Compact"), BODY, 11, color=BLACK); para(st("Compact"), before=0, after=2, line=1.15)
setfont(st("Title"), HEAD, 26, bold=True, italic=False, color=BLUE); para(st("Title"), before=0, after=2, align=WD_ALIGN_PARAGRAPH.LEFT)
setfont(st("Subtitle"), HEAD, 15, bold=False, italic=False, color=DARK); para(st("Subtitle"), before=0, after=18, align=WD_ALIGN_PARAGRAPH.LEFT)
setfont(st("Heading1"), HEAD, 15, bold=True, italic=False, color=BLUE); para(st("Heading1"), before=18, after=6, keep=True)
setfont(st("Heading2"), HEAD, 13, bold=True, italic=False, color=BLUE); para(st("Heading2"), before=14, after=4, keep=True)
setfont(st("Heading3"), HEAD, 11.5, bold=True, italic=False, color=DARK); para(st("Heading3"), before=10, after=2, keep=True)
setfont(st("Heading4"), HEAD, 11, bold=True, italic=True, color=DARK); para(st("Heading4"), before=8, after=2, keep=True)
for sid in ("ImageCaption", "Caption", "TableCaption"):
    setfont(st(sid), BODY, 9.5, bold=False, italic=True, color=DARK); para(st(sid), before=4, after=14, align=WD_ALIGN_PARAGRAPH.CENTER)
setfont(st("BlockText"), BODY, 11, bold=False, italic=True, color=DARK); para(st("BlockText"), before=4, after=10, left=0.5, right=0.5)
setfont(st("DefinitionTerm"), BODY, 11, bold=True, color=BLACK); para(st("DefinitionTerm"), before=8, after=0)
setfont(st("Definition"), BODY, 11, color=BLACK); para(st("Definition"), before=0, after=6, left=0.3)
para(st("Figure"), align=WD_ALIGN_PARAGRAPH.CENTER, before=8, after=0)
para(st("CaptionedFigure"), align=WD_ALIGN_PARAGRAPH.CENTER, before=8, after=0)
setfont(st("VerbatimChar"), "Consolas", 9.5)
for sec in doc.sections:
    sec.page_width = Inches(8.5); sec.page_height = Inches(11)
    sec.left_margin = sec.right_margin = sec.top_margin = sec.bottom_margin = Inches(1)
doc.save(str(out)); base.unlink()
print("wrote", out)
