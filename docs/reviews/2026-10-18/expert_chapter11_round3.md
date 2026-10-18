# Expert review, round 3: Chapter 11, Integrating Brain Mechanisms into AI Models

File: `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md` (revised)

Reviewer role: computational neuroscience and machine learning (deep learning, RL, LLMs, NeuroAI). This round is a read-only review of the passages changed since round 2 and of the footnote apparatus.

## Overall assessment

Technical accuracy score: **5 / 5** (round 1: 4; round 2: 4.5)

The round 2 Moderate item is fixed, and the text now matches Dapello et al. (2020), Table 1 and §4.3.

- **VOneNet (line 134, footnote 74).** The paragraph now says:
  - **White-box attacks:** resistance rose from 16 to 51 percent (ResNet50 16.4% against VOneResNet50 51.1%).
  - **Clean images:** the cost was about four points of accuracy (75.6% against 71.7%).
  - **Ordinary corruptions:** the gain was small (38.8% against 40.0%).
  - **Source of the protection:** much of it came from the copied trial-to-trial noise acting together with the filters. That matches the paper's ablation, which found the stochasticity interacting supralinearly with the filter bank.
  - **Front-end parameters:** they are "fixed to match what recordings of monkey V1 have measured". That accurately describes parameters drawn from published V1 distributions, with Poisson-like noise.
- **"A narrow copy" (line 134).** The new sentence reconciles VOneNet with the thesis correctly. It is a copy of a mechanism, but of one stage, built from measurements, inside a conventionally trained network. That is consistent with Figure 11.1, where the VOneBlock sits in "borrow the data" rather than "copy the mechanism".
- **Line 138.** The text now restricts its claim to "the second version of the approach, in which a network is trained toward recordings". That is accurate: VOneNet fixes a front end, while Li et al. (2019) and Safarani et al. (2021) train toward neural data. The point that the network "discovers the mechanism for itself" applies only to the latter.
- **Line 28.** "Invented by a computer scientist in 1992" is precise.
- **Central Lesson (line 150).** It no longer calls replay and attention borrowings. "Where engineers found replay and attention for themselves, they arrived at the brain's principle, not its parts" is consistent with lines 28 and 56 to 60 and with Chapters 5 and 10. "The borrowing that has worked best" (convolution) agrees with the vision-transformer qualification at line 26.

The literary splits and cuts introduced no technical changes.

## Major (factually wrong, must fix)

None.

## Moderate (overstated, contested, or misleading)

None.

## Minor (optional, does not affect the score)

- **Line 134.** "A standard network that resisted 16 percent of the attacks" compresses the paper's measure, which is mean top-1 accuracy under white-box attacks of several strengths. Strictly, "kept its answer correct on 16 percent of attacked images" is more exact. The current wording is acceptable for a general reader.

## What I verified this round

- **Footnotes.** There are 75 markers, numbered monotonically. Every marker has a definition, and there are no unused definitions.
- **Revised passages.** The revised VOneNet passage was checked against Dapello et al. 2020: Table 1, §4.3 and the VOneBlock methods, read in full in round 2.
- **Cross-references.** The convergence wording at lines 28 and 150 is consistent with Chapter 5 (line 168) and Chapter 10 (line 88).
- **Figures and simulations.** Both are unchanged since round 2, so the round 1 re-runs of Figures 11.2 and 11.3 still hold.

## What would be needed for 5 / 5

Nothing further. The chapter meets the bar.
