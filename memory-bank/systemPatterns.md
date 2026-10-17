# System Patterns

## Document Organization
```
docs/
├── book/           # Main textbook
│   ├── Word/       # Publisher/editorial workflow
│   │   ├── Frontispiece/
│   │   ├── Chapter1/
│   │   ├── Chapter2/
│   │   ├── Chapter3/
│   │   ├── Chapter4/   # + images/, make_figures.py, .md source
│   │   └── Chapter5/   # same layout
│   └── pdf/        # Print-ready, review-ready
│       ├── frontispiece/
│       ├── Chapter1/
│       ├── Chapter2/
│       ├── Chapter3/
│       ├── Chapter4/
│       └── Chapter5/
└── companion/      # Student notes & labs
    ├── Chapter1/
    ├── Chapter2/
    ├── Chapter3/
    ├── Chapter4/
    └── Chapter5/
        ├── Word/
        └── pdf/
```

## House Style and Build (since 2026-10-16)
- Single source of truth per document: a markdown file next to the Word output
  (docs/book/Word/<part>/How_the_Brain_Learns_<...>.md, docs/companion/ChapterN/Word/..._Student_Notes_and_Labs.md).
- `python3 docs/build.py [filter] [--docx]` rebuilds every .docx (pandoc) and .pdf (LibreOffice headless)
  from the markdown with the shared style `docs/style/reference.docx` (regenerate with docs/style/make_reference.py).
- Style: Letter, 1 in margins; body Cambria 11 pt / 1.15; Title Calibri 26 bold blue (#1F4E79); Subtitle Calibri 15 grey;
  Heading 1 Calibri 15 bold blue (chapter sections); Heading 2 13 bold blue; Heading 3 11.5 bold grey; Heading 4 11 bold italic;
  figure captions Cambria 9.5 italic centered; epigraphs as blockquotes (Block Text, italic, indented).
- Markdown conventions: YAML title/subtitle; epigraph as a blockquote; main-chapter sections are `#`;
  companions use `#` for Student Notes / Labs, `##` for sections, `###` for lab parts; companions are built with
  hard line breaks (one line = one line); figures are `![Figure N.M. caption](images/file)` alone in a paragraph;
  images live in `images/` beside the source. Figure numbering is N.M in every chapter.
- Citations (since 2026-10-17): every main chapter uses pandoc footnotes `[^n]` placed after the sentence making the
  claim (definitions at the end of the file). Footnote text = full author-date citation(s), joined by "; ", plus an
  optional note. Each chapter ends with `# References and Attribution` containing `## Figure Attribution` (the former
  Figure Credits), `## Epigraph` (source edition) and `## References` (every cited work, alphabetical). Word footnotes
  are styled Footnote Text (Cambria 9) / Footnote Reference (superscript) in reference.docx. Rule: cite only works
  verified to exist; omit volume/pages rather than guess. Companions carry no footnotes (they cite the chapter). Helper for a new chapter: docs/style/footnote_lib.py
  (apply(path, REFS, NOTES, epigraph_source, figure_attribution) inserts markers at exact anchor sentences and appends the section).
- Do not edit the .docx/.pdf by hand; edit the .md and rebuild.

## Naming Conventions
- Main book: `How_the_Brain_Learns_Chapter_N_<ShortTitle>.{md,docx,pdf}` (Chapter_0_Foundations, Chapter_1_What_the_Brain_Is, Chapter_2_Neurons, Chapter_3_Neuromodulation, Chapter_4_Circuits, Chapter_5_Plasticity_and_Memory, Chapter_6_Perception_as_Inference); front matter `How_the_Brain_Learns_Front_Matter`
- Companion: `How_the_Brain_Learns_Chapter_N_Student_Notes_and_Labs.{docx,pdf}`
- No version or descriptor suffixes any more (git history holds earlier versions)

## Writing Patterns
1. **Chapter structure**: Cumulative — each builds on previous
2. **Explanation levels**: Molecular → Cellular → Circuit → Cognitive (kept distinct)
3. **Constraints first**: Introduce biological limitations before describing solutions
4. **No hand-waving**: Every mechanism explained physically

## Editorial Workflow
1. Draft in Word for collaboration
2. Generate PDF for review and archival
3. Chapters reviewed independently
4. Style sheet compliance checked before finalization

## Key Technical Decisions
- Parallel Word/PDF outputs (not derived from single source)
- Chapter-per-directory structure
- No build tooling dependency — manual artifact management
- Companion volume is complementary, not simplified
