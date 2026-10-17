### Organizational Principles
- The **main book** and the **companion volume** are kept separate but parallel.
- PDF and Word outputs are maintained independently for each publication.
- Each chapter and front-matter component has its own directory.
- The structure mirrors the logical structure of the books, not build tooling.

This layout supports:
- Independent review of individual chapters
- Publisher workflows requiring Word documents
- Stable, print-ready PDF artifacts
- Incremental updates without rebuilding the entire project

---

## Design Philosophy

This project follows several explicit principles:

- **Mechanism over metaphor**  
  Explanations are grounded in physical and biological processes wherever possible.

- **Cumulative structure**  
  Chapters are designed to be read sequentially; later material depends on earlier concepts.

- **Respect for levels of explanation**  
  Molecular, cellular, circuit, and cognitive explanations are distinguished and not conflated.

- **Technical respect for the reader**  
  The reader is assumed to be intelligent and technically literate, but not trained in neuroscience.

- **Biological realism**  
  Noise, energy constraints, slow adaptation, and imperfect components are treated as central features, not inconveniences.

---

## Companion Volume: Student Notes and Laboratory Exercises

The companion volume is designed to support active learning and operational understanding. It provides:

- Mechanism-focused chapter summaries
- Annotated diagrams
- Conceptual exercises
- Computational and modeling tasks aligned with each chapter of the main book

The companion volume is **not a simplified version of the text**. It is a complementary artifact intended to make the mechanisms concrete through repetition, manipulation, and modeling.

---

## Formats and Publishing Workflow

Every document has one source of truth: a markdown file stored next to its Word output
(`docs/book/Word/<part>/*.md`, `docs/companion/ChapterN/Word/*.md`). Word and PDF are build
products:

```bash
python3 docs/build.py              # rebuild every .docx and .pdf
python3 docs/build.py Chapter3     # only the documents whose path contains "Chapter3"
python3 docs/build.py --docx       # skip the PDF step
```

- **Word (.docx)** is produced by pandoc from the markdown using the shared style
  `docs/style/reference.docx` (regenerate it with `docs/style/make_reference.py`).
  It is the format for copy-editing and publisher workflows.
- **PDF** is exported from the Word file with headless LibreOffice. It is the print-ready and
  review-ready artifact.

The house style (Letter page, Cambria body, Calibri headings, numbered figure captions, epigraphs
as block quotes) is documented in `memory-bank/systemPatterns.md`. Every chapter cites its sources
with footnotes (pandoc `[^n]` markers, rendered as Word footnotes) and ends with a
"References and Attribution" section: figure attribution, epigraph source, and an alphabetical
reference list of every work cited. Do not edit the .docx or .pdf
files by hand; edit the markdown and rebuild.

Requirements: `pandoc`, LibreOffice (`soffice`), Python 3 with `python-docx` (only for
regenerating the reference document) and `matplotlib` (only for redrawing the figures of Chapters 2 to 7).
