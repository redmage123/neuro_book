# Active Context

## Current Focus
- Chapter 4 (Circuits, Networks, and Coordinated Behavior) drafted with companion; both volumes aligned through Chapter 4
- Next: Chapter 5 (Plasticity and Memory: How Experience Becomes Structure), as announced at the end of Chapter 4

## Recent Changes
- 2026-10-16: all chapters, companions and front matter restyled to one house style and rebuilt from markdown sources (docs/build.py, docs/style/reference.docx); old descriptor-suffixed files removed; Chapter 0 figures made local (four dead Commons links replaced: Na/K pump and Hooke cork from Commons, bond types and macromolecules drawn)
- Added Chapter 3: Neuromodulation to main book
- 2026-10-16: Chapter 3 PDF regenerated from the Word doc with headless LibreOffice (`soffice --headless --convert-to pdf`)
- 2026-10-16: Chapter 2 Student Notes and Labs moved from docs/book into docs/companion/Chapter2
- 2026-10-16: Chapter 3 Student Notes and Labs written (notes + Labs 3.1-3.5) into docs/companion/Chapter3, with a reference table of the four neuromodulatory systems (source nuclei, targets, context, timescale)
- 2026-10-16: Chapter 1 companion expanded from a 2-page outline to full Student Notes + Labs 1.1-1.5
- 2026-10-16: Chapter 4 written (markdown source + docx + PDF in docs/book/*/Chapter4; figures in Word/Chapter4/images, drawn ones regenerable with make_figures.py). Companion Chapter 4 (notes + Labs 4.1-4.6) added.
- Configured MCP servers for research assistance (semantic-scholar, pubmed, arxiv, cite-assist)

## Next Steps
1. Draft Chapter 5: Plasticity and Memory (Chapter 4 points to it for hippocampal synaptic change)
2. Add Chapter 4 terms to the front-matter glossary: circuit motif, feedforward/feedback/lateral inhibition, disinhibition, recurrent excitation, excitation-inhibition balance, central pattern generator, half-center oscillator, canonical microcircuit, cortical column, basal ganglia, striatum, cerebellum, Purkinje cell, climbing fiber, pattern separation, pattern completion, oscillation (theta/alpha/beta/gamma), small-world network, hub, connectome
3. Decide whether the Contents list in the front matter (original 20-chapter plan) should be updated to the chapters as actually written (0 Foundations, 3 Neuromodulation, 4 Circuits, 5 Plasticity and Memory)

## Active Decisions
- Companion volume creation prioritized after each main chapter? (TBD)
- Chapter 5 scope: LTP/LTD, STDP, structural plasticity, consolidation, systems memory (TBD)

## Current Blockers
- None identified

## Session Notes
- MCP servers configured: zotero, semantic-scholar, pubmed, arxiv, pandoc, mermaid, cite-assist, filesystem
- latex MCP removed (failed to initialize)
