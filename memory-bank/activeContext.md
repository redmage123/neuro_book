# Active Context

## Current Focus
- Chapters 0-5 drafted with companions; both volumes aligned through Chapter 5
- Next: Chapter 6 (Perception as Inference: How the Brain Sees What It Expects), as announced at the end of Chapter 5

## Recent Changes
- 2026-10-16: Chapter 5 (Plasticity and Memory) written with companion (Labs 5.1-5.7: Hebb runaway/Oja, calcium control, STDP on a chain, sliding threshold, catastrophic interference vs interleaving, forgetting and spacing, concept map); figures via book/Word/Chapter5/make_figures.py
- 2026-10-16: all chapters, companions and front matter restyled to one house style and rebuilt from markdown sources (docs/build.py, docs/style/reference.docx); old descriptor-suffixed files removed; Chapter 0 figures made local (four dead Commons links replaced: Na/K pump and Hooke cork from Commons, bond types and macromolecules drawn)
- Added Chapter 3: Neuromodulation to main book
- 2026-10-16: Chapter 3 PDF regenerated from the Word doc with headless LibreOffice (`soffice --headless --convert-to pdf`)
- 2026-10-16: Chapter 2 Student Notes and Labs moved from docs/book into docs/companion/Chapter2
- 2026-10-16: Chapter 3 Student Notes and Labs written (notes + Labs 3.1-3.5) into docs/companion/Chapter3, with a reference table of the four neuromodulatory systems (source nuclei, targets, context, timescale)
- 2026-10-16: Chapter 1 companion expanded from a 2-page outline to full Student Notes + Labs 1.1-1.5
- 2026-10-16: Chapter 4 written (markdown source + docx + PDF in docs/book/*/Chapter4; figures in Word/Chapter4/images, drawn ones regenerable with make_figures.py). Companion Chapter 4 (notes + Labs 4.1-4.6) added.
- Configured MCP servers for research assistance (semantic-scholar, pubmed, arxiv, cite-assist)

## Next Steps
1. Draft Chapter 6: Perception as Inference (predictive processing, Bayesian priors, illusions, attention as precision; links to Ch4 rhythms/routing and Ch5 priors as learned structure)
2. Add Chapter 4 and 5 terms to the front-matter glossary (Ch5: LTP, LTD, NMDA receptor, STDP, eligibility trace, synaptic tagging, engram, consolidation, reconsolidation, synaptic scaling, sliding threshold, complementary learning systems, sharp-wave ripple, catastrophic interference) and Chapter 4 terms: circuit motif, feedforward/feedback/lateral inhibition, disinhibition, recurrent excitation, excitation-inhibition balance, central pattern generator, half-center oscillator, canonical microcircuit, cortical column, basal ganglia, striatum, cerebellum, Purkinje cell, climbing fiber, pattern separation, pattern completion, oscillation (theta/alpha/beta/gamma), small-world network, hub, connectome
3. Decide whether the Contents list in the front matter (original 20-chapter plan) should be updated to the chapters as actually written (0 Foundations, 3 Neuromodulation, 4 Circuits, 5 Plasticity and Memory)

## Active Decisions
- Companion volume creation prioritized after each main chapter? (TBD)
- Chapter 6 scope: perception as inference; predictive coding; priors from Ch5 memory; attention; illusions as evidence (TBD)

## Current Blockers
- None identified

## Session Notes
- MCP servers configured: zotero, semantic-scholar, pubmed, arxiv, pandoc, mermaid, cite-assist, filesystem
- latex MCP removed (failed to initialize)
