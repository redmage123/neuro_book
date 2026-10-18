# Expert review, round 2: Chapter 11, Integrating Brain Mechanisms into AI Models

File: `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md` (revised)

Reviewer role: computational neuroscience and machine learning (deep learning, RL, LLMs, NeuroAI). This round I re-read the whole revised chapter and verified each new claim and citation against its source. That includes the full text of Dapello et al. (2020): its methods and Table 1. I also viewed the regenerated figures and checked the footnote apparatus.

## Overall assessment

Technical accuracy score: **4.5 / 5** (round 1: 4)

### The round 1 Major is fixed
The chapter now separates borrowings from convergences everywhere:
- the thesis (line 18);
- Copying and Borrowing (line 28): replay in 1992 before hippocampal replay was recorded, TD from conditioning, and attention;
- line 34 ("one that machine learning found for itself");
- the Central Lesson (line 148);
- Figure 11.1, which has a new "not borrowed: convergences" band.

This now agrees with Chapter 5 (line 168) and Chapter 10 (line 88), and the thesis is more defensible for it.

### The round 1 Moderate items are fixed and accurate
- **Vision transformers (line 26, Dosovitskiy 2021).** This is the right test of the flagship borrowing, and the conclusion ("advantage shows mainly when data are scarce") is fair.
- **Forgetting and continued training (line 46).** It now says retrieval, plus continued training on mixed data, "replay at enormous scale". Footnote 19 gives the DeepSeek-V3.1-Base figure of about 840B tokens, which matches the model card (630B + 209B).
- **Curriculum (line 124).** Shifting data mixtures and a final anneal on the cleanest data, citing Llama 3.
- **Titans (line 62).** Tempered to "one of the most developed attempts", with Behrouz named.
- **Hopfield (line 56).** The fairness sentence is in. "Begins to fail at about 12 and recalls fewer than half by 17" matches my re-run (89% at 12, 43–47% at 17). "Fewer if recall must be exact" correctly qualifies 0.14N.
- **Adam (line 68).** Correctly described as per-parameter adaptation from gradient consistency.
- **KL penalty (line 108, Ouyang 2022).** Correctly characterized.
- **Callbacks, all now accurate.**
  - "takes up the solutions Chapter 10 listed" (line 30).
  - "a memory wiped when the conversation ends" (line 54).
  - Pattern completion in Chapter 5, with Hopfield as the modeler (line 56).
  - The settle-then-learn rule of Song and Bogacz (line 94).
  - Wright et al. trained with backprop, with "others trying" in-physics learning (line 94).
- **Figure numbering.** It is now in order of citation. The memory map is Figure 11.4 at line 74, and Figures 11.5 to 11.7 follow. The Figure 11.7 caption ("once the meal would carry the store past the set point") matches the code. The Figure 11.3 legend no longer sits on a curve. The docstrings match.

### New material verified
- **Behrens et al. 2007 (line 66).** The blue/green choice, a stable block against blocks that switched every few dozen trials, faster learning when volatile, and the ACC tracking volatility are all consistent with the paper.
- **Logan and Crump 2010 (line 118).** Accurate. Fingers slowed after corrected errors and not after inserted ones, while typists took credit for corrections and accepted blame for insertions. *Science*, 330(6004), 683–686, verified.
- **Hala Point (line 86).** "More than a billion simulated neurons on less than three kilowatts" is consistent with 1.15B neurons and a 2,600 W maximum.
- **The Chapter 8 compression (line 116).** It now cites Kepecs and Botvinick in one sentence and drops the duplicate detail. This is good.

### What remains
One new Moderate item, in the rebuilt Borrowing the Data section: the VOneNet results are described more favorably than Table 1 of the paper supports.

## Major (factually wrong, must fix)

None.

## Moderate (overstated, contested, or misleading)

- **Line 132: the VOneNet numbers are overstated in two places.** "...scored 18 percent higher than the same networks without the front end on a combined measure of robustness to such attacks and to common corruptions, and their accuracy on clean images barely changed."
  - **What is wrong**: Dapello et al. (2020), Table 1, for ResNet50 against VOneResNet50 (mean of 3 seeds):

    | Measure | ResNet50 | VOneResNet50 |
    |---|---|---|
    | Perturbation mean | 27.6% | 45.6% |
    | White-box attacks | 16.4% | 51.1% |
    | Common corruptions | 38.8% | 40.0% |
    | Clean accuracy | 75.6% | 71.7% |

    Three corrections follow:
    - The "18%" is 18 *percentage points* on the perturbation mean, a relative gain of about 65 percent. "18 percent higher" reads as a relative gain and so understates the gain.
    - Almost all of the gain is in white-box adversarial robustness. The gain on common corruptions is only about one point. The paper itself calls it "more moderate", in the noise, blur and digital categories. The sentence, and the line before it about "noise, blur, or fog", imply broad robustness to corruption.
    - Clean accuracy fell by about four points. The paper's wording is "largely intact", not "barely changed".

    The paper also reports that the V1-like stochasticity accounts for much of the white-box robustness, interacting supralinearly with the filters. That is consistent with "the robustness came with the copy", since the noise is part of the copy, and worth a clause.
  - **Fix**: "The resulting networks, called VOneNets, withstood attacks of this kind far better: a standard network that resisted 16 percent of the attacks resisted 51 percent with the front end, and it lost about four points of accuracy on clean images. Against ordinary corruptions such as noise and blur the gain was small. Much of the protection came from the front end's copy of the neurons' trial-to-trial noise, acting together with its filters."
  - **Also**: In the same paragraph, "whose filters, simple and complex cells, and trial-to-trial noise were all set from recordings rather than learned" is slightly too literal. The filter parameters were *sampled from distributions measured in monkey V1* (preferred orientation, spatial frequency and so on, from published studies). The noise was Poisson-like, with variance equal to the mean as in V1. It was not set from new recordings. Use "...were all fixed to match what recordings of monkey V1 have measured, rather than learned".

## Minor

- **Line 126.** "...development orders it and the child chooses it" is fine. Note that Sheybani et al. tested developmental order only. Choice by curiosity is supported by the chapter's general argument, not by that study. The sentence already separates the two, so this is optional.
- **Figure 11.1.** "Homeostatic reward" and "learned plasticity" sit in the borrowed-principle box. That is consistent with the text, and the record line "most others in research systems" is honest. No change needed.
- **Line 28.** "Experience replay was invented by an engineer" is slightly loose, since Long-Ji Lin was a computer-science doctoral student. "By a computer scientist" is more precise. This is optional.

## Figures

- **Figure 11.1**: The new convergence band is correct and clearly labeled ("invented by engineers or psychologists, recognized in the brain afterward").
- **Figure 11.2**: The code is unchanged. The round 1 re-run still holds (83.3% for gating plus protection; no protection and protection alone coincide).
- **Figure 11.3**: The legend now sits in the empty right-hand region, and the code is unchanged.
- **Figure 11.4 (memory map)**: The replay row now reads "retraining on mixed old and new data; replay in research systems", consistent with line 46.
- **Figures 11.5 to 11.7**: They are unchanged apart from numbering and the corrected Figure 11.7 caption.

## Cross-references checked this round

- **Chapter 5, line 168, and Chapter 10, line 88.** Replay is a convergence; the text and Figure 11.1 now agree.
- **Chapter 5, lines 104 and 114.** Pattern completion and the hippocampal index.
- **Chapter 10, lines 54/84 and 102.** The context window, and the settle-then-learn rule.
- **Chapter 3.** Doya, acetylcholine and norepinephrine, the learned modulatory gating, and eligibility traces.
- **Chapter 8.** Confidence and conflict, now compressed with the citations kept.
- **Chapter 9.** The pianist.

All are accurate.

## What I verified this round

- **Footnotes.** There are 75 markers, numbered monotonically. Every marker has a definition, and there are no unused definitions.
- **New citations.** Dosovitskiy et al. 2021; Kingma and Ba 2015; the DeepSeek-V3.1-Base model card (token counts verified); Grattafiori et al. 2024 (annealing); Ouyang et al. 2022; Logan and Crump 2010 (verified); Dapello et al. 2020 (methods and Table 1 read in full).
- **Simulations.** The code for Figures 11.2 and 11.3 is unchanged since my round 1 re-run, and the text's numbers match it.

## What would make it a 5

1. Correct line 132's description of the VOneNet results: percentage points; mainly adversarial robustness with a small gain on corruptions; about four points lost on clean images; and stochasticity's role.

With that done, the chapter meets the bar.
