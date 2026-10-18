# Expert review: Chapter 12, The Brain as a Predictive, Adaptive System: Is There One Principle Beneath the Mechanisms?

File: `docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md`

Reviewer role: computational neuroscience and machine learning (predictive coding, efficient coding, RL, Bayesian models, the free-energy literature). I reviewed the source, `make_figures.py`, and all seven figures. I re-ran the computed Figures 12.2 to 12.5 and checked every callback against the Chapter 1 to 11 files.

## Overall assessment

Technical accuracy score: **4.5 / 5**

This is a well-built synthesis chapter. Its thesis is the right one for a careful book: prediction and adaptation are the brain's most general *strategy*, implemented by many mechanisms, and the one-equation version is weakly supported. It is argued with good evidence:
- the retina and the fly (Srinivasan, Laughlin and Dubs; Laughlin; Brenner and Fairhall);
- the successor representation;
- Keller's mismatch responses;
- the N400;
- Kalman/Nassar adaptive learning rates;
- the HGF clinical studies;
- Körding's multi-timescale adaptation;
- a free-energy section that quotes Friston's own non-falsifiability statement and cites the main critiques (Andrews, Gershman, Bruineberg, Aitchison and Lengyel, Walsh, Westerberg) and the cell-culture tests.

The descriptions I checked against abstracts are accurate:
- Duhamel et al. 1992 ("nearly all parietal neurons respond..." is in the abstract);
- Zimmerman et al. 2016;
- Mehta et al. 1997;
- Attinger et al. 2017;
- Nassar 2010 and 2012;
- Lawson et al. 2017;
- the Westerberg preprint (global oddballs only in higher-order cortex, no subtractive mechanism);
- Isomura et al. 2023;
- Kagan et al. 2022 ("within five minutes");
- the Balci et al. critique.

All four computed figures reproduce the numbers in the text.

There is no Major error. Six Moderate issues:
- One clinical study is misdescribed (the Powers et al. fMRI result).
- The free-energy section is unfair to the proponents in one place (epistemic value is not "added") and too generous in another (Isomura's test does not compare against alternatives).
- Körding's model is said to explain savings, which Chapter 9 corrected.
- The light-from-above passage largely repeats Chapter 6.
- The N400's status as evidence of *prediction* is contested.

At about 5,400 words the chapter is short. I suggest where 1,000 to 1,500 words of substance would strengthen it, mostly by giving each side of the "one principle?" question its best evidence.

## Major (factually wrong, must fix)

None.

## Moderate (overstated, contested, misleading, or repetitive)

- **Line 78: the Powers et al. imaging result is misdescribed.** "...and in brain scans the conditioned hallucinations activated the same region of auditory cortex as real tones did."
  - **What is wrong**: Powers, Mathys and Corlett (2017) reported that conditioned hallucinations engaged a network including the anterior insula, inferior frontal gyrus, anterior cingulate, superior temporal cortex and caudate. That network overlapped with regions implicated in *clinical* hallucinations in a meta-analysis, and the HGF prior-weighting parameter correlated with activity in insula and superior temporal cortex. The paper does not report a comparison with the region activated by real tones.
  - **Fix**: "...and in brain scans the conditioned hallucinations engaged a network, including auditory cortex and the insula, that overlaps with the regions active when patients hallucinate."

- **Line 116: in active inference, exploration is not simply "added".** "Active inference can include such a term, and its proponents have done so; the point is that it has to be added."
  - **What is wrong**: This is unfair to the proponents. In active inference, policies are chosen by minimizing *expected* free energy, which decomposes into pragmatic value (reaching preferred outcomes) and epistemic value (expected information gain). The drive to resolve uncertainty falls out of that quantity rather than being bolted on. The serious criticism is different: expected free energy is not derived from the free-energy principle itself and has to be postulated.
  - **Fix**: "In active inference, a drive to resolve uncertainty appears as an 'epistemic' part of the quantity the agent minimizes when it plans, the free energy it expects in the future. Critics have pointed out that this expected free energy is not derived from the principle but chosen for its consequences, so the exploration is, in effect, assumed rather than explained."
  - **Cite**:
    - Friston, K., Rigoli, F., Ognibene, D., Mathys, C., Fitzgerald, T., & Pezzulo, G. (2015). Active inference and epistemic value. *Cognitive Neuroscience*, 6(4), 187–214. https://doi.org/10.1080/17588928.2015.1020053 (from memory, not re-verified this round).
    - Millidge, B., Tschantz, A., & Buckley, C. L. (2021). Whence the expected free energy? *Neural Computation*, 33(2), 447–482. https://doi.org/10.1162/neco_a_01354 (from memory, not re-verified this round).

- **Line 108: the Isomura test does not discriminate the principle from simpler accounts.** "...a free-energy model fitted to the first ten sessions predicted how their responses and connections would change over the remaining ninety."
  - **What is wrong**: The description is accurate. But a specialist will note that blind source separation by cultured networks is also what Hebbian or ICA-type learning rules predict. Indeed Isomura and Friston's own earlier work showed that a canonical neural network's dynamics can be read as free-energy minimization. So the result shows that the framework *can* describe the cultures, not that it outperforms alternatives. The paragraph's closing sentence partly covers this. A clause would make the fairness explicit in both directions.
  - **Fix**: Add after the Isomura sentence: "The same separation is predicted by simpler learning rules of the Hebbian kind, which the free-energy model can be read as restating; the study shows that the principle can describe what the neurons did, not that a rival account could not."

- **Line 90: Körding's model is credited with explaining savings, which Chapter 9 corrected.** "They showed that such a learner reproduces savings ... and spontaneous recovery ... both of which Chapter 9 described."
  - **What is wrong**: Chapter 9 (line 44) now says that multi-timescale models explain spontaneous recovery and "part of savings", and that savings after full washout depends on remembering an aiming strategy (Zarahn et al. 2008; Haith et al. 2015). Line 90 restates the stronger claim.
  - **Fix**: "They showed that such a learner reproduces spontaneous recovery, the return of an old adaptation after a new one fades, and some forms of savings, the faster relearning of an adaptation met before; both were described in Chapter 9, which noted that savings after an adaptation has been fully washed out seems to need something more."

- **Line 92: the light-from-above passage repeats Chapter 6.** The prior, the bump/dent demonstration, Adams et al. 2004 and Hershberger's chicks are all in Chapter 6 (lines 42 to 44 and 134, including Figure 6.3).
  - **What is wrong**: The new material is only the 26° leftward bias and Vallortigara's chicks. Re-telling Adams and Hershberger costs about 120 words that the chapter needs for substance.
  - **Fix**: Compress to: "The light-from-above prior of Chapter 6, which training can shift and which chicks reared under light from below still hold, is a prior of this kind. Even its details are oddly specific: the assumed light is not overhead but about 26 degrees to the left, a bias no one has explained.[^32] Chicks hatched in darkness..." Then keep the Vallortigara sentence and the closing line.
  - **Also**: Check the handedness clause ("in right- and left-handed people alike") against Mamassian and Goutcher (2001). Sun and Perona (1998) reported a weaker leftward bias in left-handers. Drop the clause if the cited paper does not test handedness.

- **Line 58: the N400 as "the first sign of prediction" is contested.** "The N400 was the first sign of that prediction..."
  - **What is wrong**: That the N400 scales with cloze probability is uncontroversial. Whether it reflects *pre-activation* of the upcoming word (prediction) or the ease of integrating it once it arrives has been argued for decades. A large multi-lab replication (Nieuwland et al., 2018) failed to replicate the best-known evidence for pre-activation of specific words, the article-based effect of DeLong et al. (2005), though it found that nouns showed the expected cloze effect.
  - **Fix**: "...even when both are perfectly sensible. Whether that reflects a word predicted before it arrives or one more easily fitted in after it does has been argued over for decades, but the brain's sensitivity to how expected each word is was the first sign of the prediction that Chapter 10 described..."
  - **Cite**: Nieuwland, M. S., Politzer-Ahles, S., Heyselaar, E., Segaert, K., Darley, E., Kazanina, N., ... Huettig, F. (2018). Large-scale replication study reveals a limit on probabilistic prediction in language comprehension. *eLife*, 7, e33468. https://doi.org/10.7554/eLife.33468 (from memory, not re-verified this round).

## Minor

- **Line 9 (Craik).** Sources differ on the date: the *Nature* obituary notice gives 7 May 1945, while Wikipedia and others give 8 May. "Struck on 7 May, died the next day" reconciles them. Confirm this against Zangwill (1980), which footnote 1 cites. The cycling accident on King's Parade is widely reported; I could not verify it online this round.
- **Line 14.** "The hippocampus replayed sequences and laid down expectations of where the animal would go next (Chapter 5)." Chapter 5 described replay; the forward route sequences (Pfeiffer and Foster) are in Chapter 10. Use "(Chapters 5 and 10)".
- **Line 52.** "Chapter 5 described place cells": Chapter 4 introduced them, and Chapter 5 (line 122) refers back to "the hippocampal neurons of Chapter 4". Use "Chapter 4".
- **Line 66.** "The delta rule of Chapter 3": Chapter 3's body describes TD learning and mentions Rescorla-Wagner only in footnote 16, never naming the delta rule. Use "the error-correcting rule behind Chapter 3's temporal-difference learning".
- **Line 86.** "Synaptic scaling, which Chapter 2 described": it is Chapter 5 (line 84, "Keeping the Whole Neuron Stable").
- **Line 68.** The Yu and Dayan sentence repeats Chapter 3 (line 104) nearly word for word. Use "the neuromodulatory account of Chapter 3, in which acetylcholine reports expected uncertainty and norepinephrine unexpected uncertainty".
- **Line 98.** "Variational free energy, which is a measurable upper bound on surprise" is not right. Free energy is *computable by the system* from its sensations and its own model, while surprise is not. That is the point of the bound, and it is not "measurable" by an experimenter. Use "a quantity the system can compute, which is an upper bound on surprise..."
- **Line 106.** For balance, set the Westerberg preprint beside the chapter's own Keller result: sensorimotor mismatch responses *are* found in mouse V1 (line 56), while passive sequence oddballs are not. One sentence would note that the evidence depends on the kind of prediction being violated. The PubMed record shows the preprint was last revised in September 2025; check before press whether it has been published.
- **Line 126.** "A language model predicts text it has no part in producing" is slightly overstated. During generation a model conditions on its own outputs, and reinforcement-learning post-training learns from the consequences of its own text. Use "A language model is trained mostly to predict text it had no part in producing".
- **Line 68 and Figure 12.5.** The adaptive learner in the code is given the true hazard rate and noise level. Say so in the caption: "...a learner that knows how often the mean jumps and how noisy the observations are". Also, "23 for the best of the fixed rates shown" is in fact close to the best fixed rate of any value: my grid search gave 23.1 at rates 0.5 to 0.6. You can therefore say "the best fixed rate".

## Figures

- **Figure 12.2**: The re-run gives a variance ratio of 5.3, matching "about five times smaller". A 1/f power spectrum along a line is the right 1-D statistic for natural images.
- **Figure 12.3**: The re-run gives 3.32 bits for the matched curve against 2.32 for the linear one, exactly as stated.
- **Figure 12.4**: The successor-representation computation is correct. Fields are symmetric under a random walk and extend backward under rightward running, as Mehta et al. observed.
- **Figure 12.5**: The re-run over 100 seeds gives RMS errors of 35.8, 23.1 and 20.3, matching the caption. The model is Nassar et al.'s approximately Bayesian delta rule (simplified relative-uncertainty update), which is acceptable.
- **Figure 12.6**: The "sensory adaptation" bar ends at about 10 s. The text (line 44) describes rate adaptation lasting about a minute and power-law adaptation over longer periods, so extend the bar to several minutes.
- **Figure 12.1**: The rows match the chapters. The hippocampus "error signal" ("mismatch with the expected sequence") is the most speculative cell. "Successor-representation prediction error (proposed)" would be more honest.
- **Figure 12.7**: Correct as a schematic.

## Cross-references checked

These are accurate:
- Chapter 1: Ashby.
- Chapter 3: dopamine RPE; norepinephrine and acetylcholine (Yu and Dayan).
- Chapter 6: predictive coding; dopamine and sensory errors distinguished (line 64); precision; illusions and aftereffects; the clinical accounts.
- Chapter 7: cephalic insulin; AgRP neurons quieted by the sight of food (Knight's laboratory).
- Chapter 8: confidence; accumulation.
- Chapter 9: fast and slow motor processes.
- Chapter 10: language models and the language network; the forgetting network; DreamerV3.
- Chapter 11: Behrens; curiosity as learning progress.

These are inaccurate:
- Chapter 2 for synaptic scaling (it is Chapter 5).
- Chapter 5 for place cells (Chapter 4) and for forward expectations (Chapter 10).
- The "delta rule" of Chapter 3.
- Savings, which overstates Chapter 9.

Chapter 6 overlap: the light-from-above material repeats Chapter 6. The omission and MMN themes are *not* repeated; Keller's mismatch work is new. The clinical section adds new primary studies (Powers, Lawson) to Chapter 6's reviews. These two are good extensions, not repetition.

## Length: where substance should be added (about 1,000 to 1,500 words)

The chapter's question is whether there is one principle. It currently gives the free-energy side and its critics, but not the strongest evidence *for* prediction as a general strategy beyond the cases already in the book, nor the main critique of the *Bayesian* half of the claim. In order of value:

1. **Efficient against predictive coding, and the retina's predictive information** (about 300 words, in "Matching the World's Statistics"). These are two distinct normative ideas that the chapter runs together. Palmer et al. (2015) showed that a retinal population carries nearly the maximum possible information about the *future* of a moving stimulus. That is the most direct evidence that early sensory coding is predictive in the strong sense. Chalk, Marre and Tkačik (2018) unify efficient, predictive and sparse coding as limits of one objective. This would also give the chapter's thesis ("one strategy, many implementations") a formal grounding.
   - Palmer, S. E., Marre, O., Berry, M. J., & Bialek, W. (2015). Predictive information in a sensory population. *Proceedings of the National Academy of Sciences*, 112(22), 6908–6913. https://doi.org/10.1073/pnas.1506855112 (from memory, not re-verified this round).
   - Chalk, M., Marre, O., & Tkačik, G. (2018). Toward a unified theory of efficient, predictive, and sparse coding. *Proceedings of the National Academy of Sciences*, 115(1), 186–191. https://doi.org/10.1073/pnas.1711114115 (from memory, not re-verified this round).
2. **The case against "optimal" learning** (about 250 words, after line 72). The Kalman/Nassar story presents the brain as near-optimal. The standard critique is that Bayesian models are flexible enough to fit almost anything post hoc, which parallels the free-energy critique at line 106. Bowers and Davis (2012) is the reference a specialist expects, and it gives the chapter a consistent standard for both halves of the claim.
   - Bowers, J. S., & Davis, C. J. (2012). Bayesian just-so stories in psychology and neuroscience. *Psychological Bulletin*, 138(3), 389–414. https://doi.org/10.1037/a0026450 (from memory, not re-verified this round).
3. **Prediction errors drive learning in infants** (about 200 words, in "Prediction at Every Level" or "Adaptation on Every Timescale"). Stahl and Feigenson (2015) showed that 11-month-olds learn more about, and explore, objects that violated their expectations. This is direct developmental evidence that surprise gates learning, and it ties Chapter 11's curriculum section to this chapter's thesis.
   - Stahl, A. E., & Feigenson, L. (2015). Observing the unexpected enhances infants' learning and exploration. *Science*, 348(6230), 91–94. https://doi.org/10.1126/science.aaa3799 (from memory, not re-verified this round).
4. **Human evidence for the successor representation** (about 150 words, after line 52). Momennejad et al. (2017) showed that people's re-planning after changes is better fitted by a successor-representation learner than by purely model-free or model-based ones, with a characteristic failure on transition changes. This strengthens a section that currently rests on rat place fields and one model.
   - Momennejad, I., Russek, E. M., Cheong, J. H., Botvinick, M. M., Daw, N. D., & Gershman, S. J. (2017). The successor representation in human reinforcement learning. *Nature Human Behaviour*, 1(9), 680–692. https://doi.org/10.1038/s41562-017-0180-8 (from memory, not re-verified this round).
5. **Active inference's epistemic value, fairly stated** (about 150 words; see Moderate, line 116), and the Isomura caveat (about 50 words).

## What I verified

- **Against abstracts or full records**:
  - Duhamel et al. 1992 (PubMed abstract: "nearly all parietal neurons respond").
  - Kagan et al. 2022 ("apparent learning within five minutes").
  - Isomura et al. 2023.
  - Westerberg et al., preprint (bioRxiv, revised September 2025).
  - Lawson et al. 2017 (reduced surprise linked to symptom severity).
  - Powers et al. 2017 (regions; see Moderate).
  - The Craik date sources.
- **From the literature, consistent with the text**:
  - Schmolesky et al. 1998; Nijhawan 1994.
  - Srinivasan et al. 1982; Rao and Ballard 1999.
  - Zimmerman et al. 2016; Sterling 2012.
  - Laughlin 1981; Barlow 1961; Brenner et al. 2000; Fairhall et al. 2001; Wark et al. 2007.
  - Addams 1834.
  - Mehta et al. 1997; Stachenfeld et al. 2017.
  - Keller et al. 2012; Attinger et al. 2017.
  - Kutas and Hillyard 1980; Kutas and Federmeier 2011.
  - Kalman 1960; Nassar 2010 and 2012; Yu and Dayan 2005; Mathys 2011.
  - Lamb and Pugh; Turrigiano 1998; Hensch 2005; Körding et al. 2007.
  - Vallortigara et al. 2005.
  - Friston 2006 and 2010; Friston, Thornton and Clark 2012; the Friston interview (2018); Andrews 2021; Gershman 2019; Bruineberg et al. 2022; Aitchison and Lengyel 2017; Walsh et al. 2020.
  - Balci et al. 2023; Cisek 2019; LeCun 2022; Sutton 1992.
- **Simulations**: I re-ran Figures 12.2 to 12.5. Their numbers are given above.

## What would make it a 5

1. Correct the Powers et al. imaging description (line 78).
2. State active inference's epistemic value fairly, and add the Isomura caveat (lines 108 and 116).
3. Align the savings claim with Chapter 9 (line 90), and hedge the N400's interpretation (line 58).
4. Compress the light-from-above passage to a callback (line 92), and fix the five callback slips.
5. Use the recovered space, and the remaining length budget, for items 1 to 4 under "Length", especially the retina's predictive information and the Bayesian just-so critique. These give each side of the chapter's central question its strongest evidence.
