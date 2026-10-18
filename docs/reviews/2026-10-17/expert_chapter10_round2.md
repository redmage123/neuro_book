# Expert review, round 2: Chapter 10, What Artificial Intelligence Gets Right and Wrong

File: `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md` (revised)

Reviewer role: computational neuroscience and machine learning (deep learning, RL, LLMs, NeuroAI). This round I re-read the whole revised chapter, verified every newly introduced claim and citation against sources, re-ran the Figure 10.5 simulation, viewed the regenerated figures, and re-checked the new callbacks against Chapters 1, 3, 8 and 9.

## Overall assessment

Technical accuracy score: **4.5 / 5** (round 1: 4)

### Round 1 findings now fixed
All three round 1 Major findings are fixed and correct:
- **Line 16, Marr.** It now calls back to Chapter 1, line 34, which does give Marr's three-way distinction, and it says "borrow that discipline loosely".
- **Line 74, infant findings.** Johnson et al. (1991) is right: preferential tracking of face-like patterns in the first hour of life. Object permanence is now dated to 4 to 5 months, after Baillargeon et al. (1985), with the debate noted.
- **Line 88, the simulation.** I re-ran `interference()` for 20 seeds. List A is 53.8 percent after 3 passes, 5.0 percent after 20 and 0.8 percent after 35. List B is 47 percent at pass 20 and reaches 95 percent at about pass 45. "Half within a few passes, nearly all within about 20, well before it has finished learning the second" is exact.

The Moderate fixes are also accurate:
- **Callbacks.** The Chapter 6 adversarial callback (line 14), the Chapter 3 Crick and apical-burst callback (line 100; Chapter 3, line 74 has both), the Chapter 6 predictive-coding callback, and Pfeiffer and Foster replacing the Chapter 5 route claim (line 130).
- **History.** TD history via Rescorla-Wagner and Sutton and Barto (1981) (line 30). Backpropagation history (lines 22 and 28). Dabney softened, plus Sousa et al. (2025).
- **Representations and robustness.** Linsley et al. (2023) in the text and Figure 10.2. Next-token prediction against hierarchical predictive coding, plus post-training (line 54). Recht qualified by Engstrom (line 64).
- **Credit assignment.** Whittington and Bogacz, Bartunov, and Song et al.
- **Energy.** Patterson et al. (2022) for the three-fifths inference share, and 700 W marked as dated.
- **Reasoning.** The o1 PlanBench update.
- **Metacognition.** The GPT-4 calibration evidence, with human overconfidence acknowledged.
- **Line 158.** "Until the mid-2010s ... largely by hand".

### New material checked
I verified the new material against sources:
- **Kar et al. (2019): mostly right.** The paper found "hundreds" of challenge images, with identity emerging about 30 ms later in IT.
- **Varley et al. (2005): exact.** Three men; "The man killed the lion"; 90 − [(3 + 17) × 3] appears in the paper.
- **AlphaGo game 4: right.** Move 78 at 1 in 10,000 (DeepMind). Hassabis's "mistake was on move 79 ... realisation on around move 87" (quoted by NPR and others).
- **Chen et al. (2024): right.** QwQ-32B-Preview generated 13 solutions to "2 + 3".
- **Wang et al. (2025): fairly characterized.** Underthinking means abandoning promising lines of thought too soon.
- **Piantadosi.** The chapter is Chapter 15 of Gibson and Poliak (2024), Language Science Press.

### What remains
- **Line 78, BabyLM.** One new claim contradicts its source, and I suggested the wording in round 1, so this is partly my error.
- **Line 42, Kar et al.** One new claim slightly misstates what the paper reports.
- Small citation and figure items.

## Major (factually wrong, must fix)

None.

## Moderate (overstated, contested, or misleading)

- **Line 78: BabyLM is stated backwards relative to the Findings paper.** "...such models learn much of English grammar but still fall short of models trained on trillions."
  - **What is wrong**: The Findings abstract (Warstadt et al., 2023) reports the opposite headline: the winning submissions, built on the LTG-BERT architecture, "outperformed models trained on trillions of words" on the challenge's evaluation suite. That suite is mostly grammaticality judgments (BLiMP) plus a few fine-tuned understanding tasks. The fair reading is that small-data models can match large ones on these narrow tests. It is not that they still fall short. I suggested the round 1 wording without checking it against the abstract; this corrects it.
  - **Fix**: "A related line of work, the BabyLM Challenge, trains language models on 100 million words or fewer, roughly what a child hears by early adolescence. On the challenge's tests, most of them judgments of whether sentences are grammatical, the best such models did as well as some models trained on trillions of words, which suggests that much of what the giant datasets buy is not grammar."
  - **Also**: Line 162 ("how well a model does on a child's budget of words") remains correct and now reads as the payoff of line 78.

- **Line 42: Kar et al. compared deeper and shallower feedforward networks, not recurrent and feedforward ones.** "...and networks with recurrent connections predicted the late responses better than feedforward ones."
  - **What is wrong**: The abstract reports that the late IT responses were poorly predicted by the feedforward networks, and that *deeper* CNNs predicted them better. The authors interpret extra depth as functionally standing in for recurrent processing. The paper does not report a recurrent-against-feedforward comparison as its finding. The rest of the paragraph (hundreds of challenge images, about 30 ms later, present even in passive viewing) is accurate.
  - **Fix**: "...as if a second pass had been needed. Feedforward networks predicted those late responses poorly, and deeper networks predicted them better, which the authors read as a sign that the brain was using recurrent processing to do what extra layers do."

## Minor

- **Line 92, Dohare et al.** "...no better than a shallow network" understates the paper's point. On Continual ImageNet the deep network's accuracy fell to, then below, that of a *linear* network. Use "no better than a network with no hidden layers at all".
- **Line 46.** "...others have argued that the needed choices are principled" has no citation. Add Sorscher, B., Mel, G. C., Ocko, S. A., Giocomo, L. M., & Ganguli, S. (2023). A unified theory for the computational and mechanistic origins of grid cells. *Neuron*, 111(1), 121–137. https://doi.org/10.1016/j.neuron.2022.10.003 (from memory, not verified this round). Alternatively, drop the clause.
- **Line 140.** "AlphaGo at move 78 had no such trigger" is slightly unfair. Hassabis clarified that AlphaGo's value network stayed near 70 percent after move 79 and dropped sharply only at move 87. The program did eventually register the surprise, nine moves late. Use "AlphaGo at move 78 had no such trigger, and noticed its mistake only eight moves later".
- **Footnotes and references.**
  - Footnotes 36 and 82 (BabyLM) lack pages and DOI, and have a stray space before the period. Use "(pp. 1–34). https://doi.org/10.18653/v1/2023.conll-babylm.1" (verified).
  - Footnote 15 (Linsley) lacks pages: 28873–28891 (verified).
  - Footnote 11 (Sousa et al., 2025): volume 642 and issue 8068 are verified via DOI 10.1038/s41586-025-09089-6. I could not confirm pages 691–699, so check them against the publisher's page.
  - Footnote 81 (Piantadosi): Chapter 15 of Gibson and Poliak (2024) is verified. I could not confirm pages 353–414, so check them against the open-access PDF.
- **Line 30.** Optional: the Rescorla-Wagner rule is formally the Widrow-Hoff (1960) delta rule, an engineering rule. A clause ("a rule engineers had already written down as the delta rule") would make the "psychology to engineering" arrow honestly two-headed. This is not required.

## Figures

- **Figure 10.1**: The Rescorla-Wagner→Sutton and Hebb→Rosenblatt arrows are correct, and the y-label "neuroscience and psychology" fixes the category problem.
- **Figure 10.2**: The falling "later, more accurate networks" points convey Linsley et al. (2023), and the caption and attribution say the figure is illustrative. A pedantic note, optional: Yamins's x-axis was categorization on his own image set, while Linsley's was ImageNet accuracy, so a single x-axis is a schematic simplification. Adding "on each study's own benchmark" to the caption would cover it.
- **Figure 10.3**: The switch to dots on a log axis is an improvement, and the values are unchanged and correct.
- **Figure 10.5**: The caption now states the all-ten-outputs criterion and the random replay draw. The code is unchanged and still matches the text. In panel A the relocated legend's right edge now touches the list-A curve where it falls at pass 100. Shift the legend left or down into the empty region at passes 30 to 90 and 20 to 60 percent.
- **Figure 10.7**: The two new rows, "feedback loops in perception" and "deciding when to deliberate", both partly shared, match lines 42 and 140. The caption's note on "error-driven learning" resolves my round 1 concern. Line 146 now names only the red rows, so text and figure agree.
- **Docstrings** now match the chapter's numbering.

## Cross-references checked this round

- **Chapter 1, line 34.** Marr's three-way distinction is there (line 16 is now accurate).
- **Chapter 3, line 74.** Crick 1989, random feedback, and apical-dendrite bursts are all there (lines 98 to 100 are now accurate).
- **Chapter 6.** The predictive-coding approximation of backpropagation and the adversarial nuance are there (lines 14 and 100).
- **Chapter 8, AI section.** Step-by-step reasoning is described as a step toward accumulation to a bound (line 128).
- **Chapter 9.** The power law is disputed, citing Heathcote et al. 2000 (line 56). The handover question at the end of Chapter 9 is answered at line 140.

## What I verified this round

- **Against primary sources or abstracts**:
  - Kar et al. 2019: challenge images, about 30 ms, deeper CNNs.
  - Varley et al. 2005, full text: three men, the reversible-sentence example, the bracket example.
  - Johnson et al. 1991: first hour of life.
  - Baillargeon et al. 1985: five-month-olds; Bogartz et al. 2000 critique.
  - BabyLM Findings, abstract: "outperformed models trained on trillions of words".
  - Chen et al. 2024: 13 solutions to "2 + 3".
  - Hassabis on moves 79 and 87 (as quoted by NPR and others) and DeepMind's 1 in 10,000 for move 78.
  - Piantadosi chapter in the Gibson and Poliak contents.
  - Sousa et al. 2025: DOI, volume, issue.
  - Valmeekam et al. 2024: Tables 1 and 2.
  - Patterson et al. 2022: the ⅗ inference sentence.
- **Simulation**: I re-ran it with 20 seeds. The numbers above match line 88 and the caption.

## What would make it a 5

1. Correct line 78 (BabyLM) to match the Findings paper.
2. Correct line 42 (Kar et al.) to "deeper networks", not "recurrent networks".
3. Optional and quick: line 92 "linear network"; the citation for line 46; the AlphaGo nuance at line 140; the footnote pages and DOIs; the Figure 10.5 legend position.

With items 1 and 2 done, the chapter meets the bar.
