# Expert review, round 3: Chapter 10, What Artificial Intelligence Gets Right and Wrong

File: `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md` (revised)

Reviewer role: computational neuroscience and machine learning (deep learning, RL, LLMs, NeuroAI). This round is a read-only review of every passage changed since round 2, the footnote apparatus, the new and amended citations, and the regenerated Figure 10.5.

## Overall assessment

Technical accuracy score: **5 / 5** (round 1: 4; round 2: 4.5)

Both round 2 Moderate findings are fixed, and both now match their sources.

- **BabyLM (line 78, footnote 35).** The text now says the best small-data models did as well as some models trained on trillions of words, on tests that are mostly grammaticality judgments. That matches the Findings paper's abstract, which says the winning LTG-BERT submissions "outperformed models trained on trillions of words". The narrowness caveat keeps it honest.
- **Kar et al. 2019 (line 42, footnote 15).** The text now says feedforward networks predicted the late IT responses poorly, that deeper networks predicted them better, and that the authors read this as recurrence doing what extra layers do. That matches the abstract.

The optional round 2 items are also done and correct:
- **Dohare (line 92).** "No better than a network with no hidden layers at all" matches the paper's linear-network baseline.
- **Sorscher et al. 2023 (footnote 20).** Added for "others have argued that the needed choices are principled". I confirmed the details through CrossRef: *Neuron*, 111(1), 121–137 (article pages 121–137.e13).
- **AlphaGo (line 144).** "Noticed its mistake only eight moves later" is consistent with line 138 and with Hassabis's statement: the mistake was at move 79 and the realization came around move 87.
- **Sousa et al. 2025.** CrossRef confirms *Nature*, 642(8068), 691–699.
- **Linsley et al. 2023.** Pages 28873–28891 are now given (verified in round 2).
- **BabyLM.** The pages (1–34) and the DOI are now given (verified).
- **Piantadosi.** The Zenodo DOI 10.5281/zenodo.12665933 resolves to "Modern language models refute Chomsky's approach to language", by Steven T. Piantadosi, Language Science Press (Berlin), 2024. The chapter is Chapter 15 of Gibson and Poliak's tribute volume. I could not confirm the page range 353–414 from the record.
- **Figure 10.2.** The caption now says the horizontal axis is schematic, because the two studies used different benchmarks.
- **Figure 10.5.** The legend now sits in the empty region of panel A, between passes 25 and 90 at 45 to 55 percent, and touches no curve.

The literary edits introduced no technical errors:
- **Line 28.** The reordered backpropagation sentence keeps the attribution right: the method came from mathematics and control, and Rumelhart, Hinton and Williams in 1986 demonstrated that it learns hidden representations.
- **Line 102.** The Song et al. description is unchanged in substance.
- **Line 140.** "Training can blunt a model's sense of its own reliability" is a fair reading of the GPT-4 calibration result, and it is more careful than the round 2 wording.
- **Line 144.** "Yue Wang and colleagues" is correct for the underthinking paper (arXiv:2501.18585).

## Major (factually wrong, must fix)

None.

## Moderate (overstated, contested, or misleading)

None.

## Minor (optional, does not affect the score)

- **Footnote 80 and reference list, Piantadosi.** The page range 353–414 is not confirmed by the Zenodo record. Before typesetting, check it against the volume's open-access PDF (langsci-press.org/catalog/book/434).
- **Line 144.** "AlphaGo at move 78 had no such trigger and noticed its mistake only eight moves later." A reader who has just read "move 78" may count from 78 rather than from AlphaGo's mistake at 79. The arithmetic is right either way within rounding, since Hassabis said "around move 87". If you want it exact, use "...noticed its own mistake, made at move 79, only around move 87".

## What I verified this round

- **Footnotes.**
  - There are 81 markers in the body, numbered monotonically from 1 to 81.
  - Every marker has a definition, and there are no unused definitions.
  - Spot checks show each footnote attached to the right sentence: 10 (Dabney and Sousa), 14 (Linsley), 15 (Kar), 20 (Schaeffer and Sorscher), 35 (BabyLM, line 78), 43 (Dohare), 50 (Song), 74 (GPT-4 report), 75 (Chen and Wang), 80 (Piantadosi), 81 (BabyLM, line 162).
- **CrossRef.** Sorscher et al. 2023 and Sousa et al. 2025 (volume, issue and pages).
- **Zenodo.** The Piantadosi DOI (title, author, publisher).
- **Revised passages.** The BabyLM and Kar wording was checked against the abstracts retrieved in round 2.
- **Figures.** Figure 10.5 was regenerated with an unchanged simulation; the line 88 numbers still hold from the round 2 re-run. Figure 10.2's caption now matches its schematic x-axis.
- **Cross-references.** The callbacks to Chapters 1, 3, 5, 6, 7, 8 and 9 are unchanged since round 2 and still accurate.

## What would be needed for 5 / 5

Nothing further. The chapter meets the bar. The two Minor items are a citation check before typesetting and an optional clarity edit; neither is a correction.
