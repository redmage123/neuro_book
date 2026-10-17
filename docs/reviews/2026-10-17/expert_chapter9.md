# Expert review: Chapter 9, Habits, Skills, and Automaticity: How Practice Turns Choices into Routines

File: `docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md`

Reviewer role: motor learning, basal ganglia, cerebellum, habits, skill, computational RL. Reviewed the source, `make_figures.py` and all seven figures.

## Overall assessment

Technical accuracy score: **4 / 5**

A strong chapter with the structure a specialist would choose: adaptation versus skill, chunking and task-bracketing, the dorsomedial-to-dorsolateral shift, cortical tutoring, structural plasticity, offline gains, automaticity, practice scheduling, and songbird exploration. Contested areas are handled well (sleep and micro-offline gains, deliberate practice, cortex versus striatum, Berlot's fMRI re-evaluation, Hogarth on addiction). It builds on Chapter 8 without repeating it, and most attributions and numbers are right.

The problems: three factual misdescriptions (Wymbs et al., Kerr and Booth, the scope of the two-state model); a few overstated claims (variability predicting learning, no interference between skills, instance theory "assuming nothing else"); two figures that do not show what the text says (9.1, 9.4); and smaller slips. None undermines the argument.

## Major (factually wrong, must fix)

- **Line 48: the two-state model does not explain savings in general.** "Maurice Smith, Ali Ghazizadeh, and Shadmehr explained both [savings and spontaneous recovery] with a model of two processes..."
  - **What is wrong**: The linear two-state model explains spontaneous recovery and some savings after brief counter-perturbation, but not savings after a full washout, which is what the text describes (Zarahn et al.). Much of savings reflects recall of an explicit aiming strategy.
  - **Fix**: "...explained spontaneous recovery, and some forms of savings, with a model of two processes... Savings after a perturbation has been fully washed out is not explained by this model, and appears to depend partly on remembering an explicit aiming strategy."
  - **Cite**: Zarahn, E., Weston, G. D., Liang, J., Mazzoni, P., & Krakauer, J. W. (2008). Explaining savings for visuomotor adaptation: Linear time-invariant state-space models are not sufficient. *Journal of Neurophysiology*, 100(5), 2537–2548 (verified). Haith, A. M., Huberdeau, D. M., & Krakauer, J. W. (2015). The influence of movement preparation time on the expression of visuomotor learning and savings. *Journal of Neuroscience*, 35(13), 5109–5117 (verified).

- **Line 60: Wymbs et al. studied 3 days of training, not weeks.** "...how strongly a person's sequence was chunked over weeks of practice tracked activity in the sensorimotor putamen."
  - **What is wrong**: Wymbs et al. (2012) collected data over 3 days of training. The putamen correlated specifically with chunk *concatenation*, and a left frontoparietal network correlated with segmentation.
  - **Fix**: "...found that, over three days of training, activity in the sensorimotor putamen rose with how strongly the elements of a sequence were joined into chunks, while frontoparietal cortex was more active when a sequence was broken into chunks."

- **Line 122: Kerr and Booth is misdescribed.** The text implies twelve weeks of varied or specific practice.
  - **What is wrong**: All 64 children took a 12-week physical education program; the specific/varied manipulation was practice throws given just before the pretest and posttest. Groups did not differ at pretest; the varied group was better at posttest. Throws were made without vision, with knowledge of results.
  - **Fix**: "Robert Kerr and Bernard Booth tested children of 8 and 12 throwing beanbags, without vision, at a target on the floor, before and after a twelve-week physical education program. Before each test, one group warmed up at the test distance and the other only at a nearer and a farther target. At the end of the program, the group that had never thrown at the test distance was the more accurate at it."
  - **Also**: Attribute the "rule" to Schmidt's schema theory (Schmidt, R. A. (1975). *Psychological Review*, 82(4), 225–260; not verified here); varied-practice benefits are more consistent in children than adults.

## Moderate (misleading, overstated, or figure problems)

- **Line 72: check the Yin et al. (2009) lesion description.** "Lesions of the dorsomedial striatum impaired early learning but not the performance of mice already trained."
  - **What is wrong**: As I recall, the lesions were made before training: DMS-lesioned mice were impaired early and caught up, DLS lesions impaired both phases. "Mice already trained" implies post-training lesions. Check against the paper's Figure 1.
  - **Fix**: "...impaired the early sessions, but the lesioned mice caught up later."
  - **Also**: The abstract specifies that the late potentiation in DLS was in striatopallidal (indirect-pathway) neurons. That detail is worth a clause.

- **Line 106: instance theory needs more than the text admits.** "...instance theory predicts the power law of practice without assuming anything else."
  - **What is wrong**: Logan's derivation is exact only for independent Weibull retrieval times, approximate otherwise, and with the procedure in the race early practice departs from a power function, as Figure 9.5A shows.
  - **Fix**: "...so, under simple assumptions about retrieval times, instance theory predicts the power law of practice. It also predicts something less obvious that was confirmed: the variability of response times shrinks at the same rate as their mean."

- **Line 126: the variability result has failed to replicate.** Wu et al. (2014) is presented as settled.
  - **What is wrong**: He et al. (2016) found that baseline variability did not predict the speed of error-based learning, and other groups have reported mixed results.
  - **Fix**: Add "though later studies have not consistently found the same relation for error-based learning."
  - **Cite**: He, K., Liang, Y., Abdollahi, F., Fisher Bittmann, M., Kording, K., & Wei, K. (2016). The statistical determinants of the speed of motor learning. *PLoS Computational Biology*, 12(9), e1005023 (verified).

- **Line 160: motor memories do interfere.** "Skills in the brain accumulate without erasing one another."
  - **What is wrong**: Opposing adaptations learned in close succession interfere, and the chapter's own spontaneous-recovery paradigm depends on it.
  - **Fix**: "Skills in the brain largely accumulate without erasing one another, although two conflicting adaptations learned close together do interfere."
  - **Cite**: Brashers-Krug, T., Shadmehr, R., & Bizzi, E. (1996). Consolidation in human motor memory. *Nature*, 382, 252–255 (verified).

- **Figure 9.4 and line 148: the figure lacks the ventral striatum and the pallidum.** Line 148 says control shifts "from ventral to dorsal striatum along the spiral of Figure 9.4".
  - **What is wrong**: The figure has no ventral striatum; the "spiral" is only a label over separate dopamine arrows; and striatum → thalamus omits the output nuclei (GPi/SNr) central to Chapter 4.
  - **Fix**: Add a ventral striatum (limbic) box at the left. Draw the spiral as striatum → dopamine neurons → next striatal region. Label the striatum-to-thalamus arrow "via pallidum/SNr".
  - **Also**: "Dorsomedial (caudate)" and "dorsolateral (putamen)" are rodent/primate approximations. In primates the associative territory also includes the anterior putamen, and the sensorimotor territory is the posterolateral putamen. Say "mainly caudate" and "posterior putamen".

- **Figure 9.1: the curve never reaches the floor, and the numbers are implausible.**
  - **What is wrong**: Text (line 14) and caption say improvement stops near the machine's limit, but at 16 million cigars the curve (about 0.6 s) is still nearly twice the floor (0.35 s). Panel A squeezes all the early fall into a vertical line at x ≈ 0, and a 35-fold speed-up to 0.35 s per cigar is implausible.
  - **Fix**: Use arbitrary units or a realistic floor, choose parameters so the curve visibly meets the floor, and plot panel A over a range that shows the early fall.

## Minor

- **Lines 12 and 16: Chapter 8 does not end with the devaluation rats**; they are in "Goals and Habits", and "the same economy" is in "Thinking Is Costly". Use "Near its end, Chapter 8 described...". "A failure of flexibility" also undersells Chapter 8, which treats habit as a sensible policy.
- **Line 32: the sentence is garbled.** "Anyone can trace a difficult path slowly or quickly and badly" should read "slowly and well, or quickly and badly."
- **Line 36**: amnesic patients learned normally early but fall behind with longer training, and some later studies found impairment. Add "at least early in training."
- **Line 64: Jog et al. did not test devaluation.** "As the behavior became habitual" is an inference. Smith and Graybiel (2013, already cited) linked bracketing to insensitivity to devaluation.
- **Line 116: the closing sentence goes too far.** "The amount does not explain who becomes expert" should be "The amount alone does not explain...". Macnamara's figures show that practice explains a real, if modest, share of the variance.
- **Line 128: Tumer and Brainard used Bengalese finches.** The paragraph opens with zebra finches, so name the species.
- **Line 154: implicit chain of thought is a research direction.** "Language models are now trained in the same way..." should read "Researchers have begun training language models...". It is not standard practice.
- **Line 158: OpenAI's hand did not solve the cube.** It learned the manipulation; the sequence of face turns came from a conventional solver. Say "learned to manipulate a Rubik's cube through a solution supplied by a standard solver."
- **Figure 9.2 and line 48: "no error feedback" is inaccurate.** In Smith et al. these were error-clamp trials: the error was held at zero, not hidden. Use "error-clamp trials (error held at zero)".
- **Figure 9.5**: the code uses a constant procedure time, so the caption should say "fixed time", not "fixed mean time"; panel A needs y ticks (0.2, 0.5, 1).
- **Figure 9.6**: Shea and Morgan measured total time (reaction plus movement time), not "movement time"; and the random-practice advantage was largest in a random-order retention test, so say which context the dots show.
- **Omissions a specialist would expect** (one or two sentences each would suffice):
  - **Taxonomy of motor learning**: use-dependent learning and reward-based human motor learning, alongside error-based and strategic learning. One example: cerebellar patients can learn from reward when they cannot learn from sensory error (Therrien, A. S., Wolpert, D. M., & Bastian, A. J. (2016). *Brain*, 139(1), 101–114, verified).
  - **Dopamine in sensorimotor striatum for habits**: Faure, A., Haberland, U., Condé, F., & El Massioui, N. (2005). Lesion to the nigrostriatal dopamine system disrupts stimulus-response habit formation. *Journal of Neuroscience*, 25(11), 2771–2780 (verified).
  - **Direct and indirect pathways in sequence parsing and concatenation**: Jin, X., Tecuapetla, F., & Costa, R. M. (2014). *Nature Neuroscience*, 17(3), 423–430 (verified).

## Cross-references

All "Chapter N" references were checked against the chapters:
All Chapter 3 to 8 references point to content those chapters contain (Ch. 4 climbing fibers and basal ganglia selection; Ch. 5 H.M., procedural memory, sleep, waking replay, catastrophic interference; Ch. 6 forward models and prisms; Ch. 8 TMS, explore/exploit, striatal subregions, speed-accuracy, de Wit, compulsivity). The only inaccuracy is the "Chapter 8 ended" phrasing.

## What I verified

- **Against abstracts**: Yin et al. 2009; Jin & Costa 2010; Poldrack et al. 2005; Wymbs et al. 2012; Tumer & Brainard 2007; Dhawale et al. 2021; Wu et al. 2014; Gadagkar et al. 2016; Knowlton et al. 1996; Smith et al. 2012; Kerr & Booth 1978; Gupta & Rickard 2022; Pan & Rickard 2015 ("may still protect" is fair); Zarahn et al. 2008.
- **From the literature, consistent with the text**: the adaptation studies (Shadmehr & Mussa-Ivaldi; Martin et al.; Tseng; Mazzoni & Krakauer; Taylor; Morehead); Ericsson, Chase & Faloon (230 h, 7 to 79); the striatal recording and anatomy work (Jog; Barnes; Martiros; Thorn; Lehéricy; Haber); the cortex and spine studies (Kawai; Wolff; Nudo; Karni; Pascual-Leone; Elbert; Draganski; Xu; Yang; Hayashi-Takagi; Peters; Berlot); Walker et al. (about 20 percent); Bönstrup; Buch; Macnamara et al. (12 percent); Wood et al. (43 percent); Lally et al. (18 to 254 days, median 66); Neal et al.; Gillan et al. 2011.
- **Figures**: the two-state simulation (9.2) and the instance race (9.5) are correctly computed, the song circuit (9.7) is anatomically correct, and task-bracketing (9.3) is a fair caricature.

## What would be needed for 5 / 5

1. Correct the three Major items.
2. Hedge the variability, interference and instance-theory claims.
3. Check the Yin et al. lesion wording against the paper.
4. Redraw Figure 9.4 with the ventral striatum, the spiral and the output nuclei.
5. Redraw Figure 9.1 so the curve visibly meets the floor with plausible units.
6. Add two or three sentences on use-dependent and reward-based human motor learning and on dopamine's role in sensorimotor striatum.
