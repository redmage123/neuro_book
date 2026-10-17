# Active Context

## Current Focus
- Chapters 0-6 drafted with companions; both volumes aligned through Chapter 6
- Next: Chapter 7 (Emotion and the Body: How Internal States Tell the Brain What Matters), as announced at the end of Chapter 6

## Recent Changes
- 2026-10-17: every main chapter (0-6) given footnoted citations and a "References and Attribution" section (figure attribution, epigraph source, alphabetical references): Ch0 43 notes/48 refs, Ch1 18/27, Ch2 21/32, Ch3 30/55, Ch4 46/79, Ch5 56/124, Ch6 58/83. Footnote styles added to reference.docx. Three text corrections: Galvani "around 1780" (published 1791), Ch4 duplicate epigraph line removed, Ch5 LTD history (cerebellum 1982, hippocampus 1992).
- 2026-10-16: Chapter 6 (Perception as Inference) written with companion (Labs 6.1-6.7: Bayes by hand, precision-weighted cue combination, prediction error on a chain, hollow-mask odds, efference copy cases, learning a prior with a surprise rule, concept map); figures via book/Word/Chapter6/make_figures.py; Figure 6.6 is Adelson's checker-shadow (CC BY-SA 4.0)
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
1. Draft Chapter 7: Emotion and the Body (interoception as inference, homeostasis and allostasis, amygdala/insula/hypothalamus, neuromodulators of Ch3 as the chemistry of emotion, decision-making link)
2. Add Chapter 4, 5 and 6 terms to the front-matter glossary (Ch6: inverse problem, prior, likelihood, posterior, precision, predictive coding, prediction error, repetition suppression, mismatch negativity, receptive field, ventral stream, critical period, efference copy, forward model, cue combination; Ch5: LTP, LTD, NMDA receptor, STDP, eligibility trace, synaptic tagging, engram, consolidation, reconsolidation, synaptic scaling, sliding threshold, complementary learning systems, sharp-wave ripple, catastrophic interference) and Chapter 4 terms: circuit motif, feedforward/feedback/lateral inhibition, disinhibition, recurrent excitation, excitation-inhibition balance, central pattern generator, half-center oscillator, canonical microcircuit, cortical column, basal ganglia, striatum, cerebellum, Purkinje cell, climbing fiber, pattern separation, pattern completion, oscillation (theta/alpha/beta/gamma), small-world network, hub, connectome
3. Decide whether the Contents list in the front matter (original 20-chapter plan) should be updated to the chapters as actually written (0 Foundations, 3 Neuromodulation, 4 Circuits, 5 Plasticity and Memory)

## Active Decisions
- Companion volume creation prioritized after each main chapter? (TBD)
- Chapter 7 scope: emotion as regulation; interoception; body-to-brain signalling; how emotion sets priorities for learning and decision (TBD)

## Current Blockers
- Figure rights (found while attributing, needs the author's decision): Ch1 Fig 1.2 (midsagittal MRI, source file unknown); Ch2 Fig 2.2 carries a Healthline watermark (copyrighted; replace), Figs 2.3 and 2.7 are the same OpenStax image, Figs 2.1/2.4/2.5/2.6/2.8/2.9/2.10 unknown provenance (2.4, 2.9, 2.10 low-res journal figures); Ch3 all ten figures of unidentified origin, Fig 3.7 carries a "Current Opinion in Neurobiology" imprint, 3.5/3.8 look like figures from Miconi et al. 2019 / reward-modulated STDP papers. Options: redraw with make_figures.py in the house palette, or source Commons/CC images.
- Ch3 epigraph ("unexplored continents") attributed to Cajal but primary source not verified.

## Session Notes
- MCP servers configured: zotero, semantic-scholar, pubmed, arxiv, pandoc, mermaid, cite-assist, filesystem
- latex MCP removed (failed to initialize)
