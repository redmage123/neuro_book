# Audit: cross-chapter repetition, epigraphs, mechanical style

Book: *How the Brain Learns* (`/home/bbrelin/neuro_book`, read-only). Line numbers are those of the chapter `.md` files as they stand (the numbering `body.py` prints). Every "Current" quotation below was verified by script to occur exactly once on the cited line. Word counts are whitespace tokens. Footnote markers in replaced text are kept unless stated.

Convention: "home" is the occurrence that keeps the full telling; other occurrences become short callbacks.

## Summary of words saved

| Chapter | Body words | Proposed cuts (repetition + redundancy) | Saved | % | Further author's-call trims (unique material, listed per chapter) |
|---|---|---|---|---|---|
| 7 | 7380 | 7 | 94 | 1.3% | up to 282 more |
| 8 | 7373 | 7 | 184 | 2.5% | up to 333 more |
| 9 | 7740 | 9 | 112 | 1.4% | up to 279 more |
| 10 | 7780 | 8 | 169 | 2.2% | up to 318 more |
| 11 | 7611 | 11 | 223 | 2.9% | up to 102 more |
| 12 | 7293 | 8 | 231 | 3.2% | up to 480 more |
| 13 | 7720 | 6 | 124 | 1.6% | up to 279 more |
| 14 | 7003 | 10 | 203 | 2.9% | up to 362 more |

Honest bottom line: repetition and redundancy alone yield roughly 1.3 to 3.2 percent per chapter in Chapters 7 to 14. Chapters 7, 9, and 13 are mostly original material, with few retellings. To reach the 5 to 10 percent target, the author would have to drop some unique material. The "Author's call" list under each chapter names self-contained passages that could go without breaking the flow. Each of those would remove the only statement of its facts, so they are offered for decision, not proposed as cuts.

Body word counts include title block, epigraph, and figure captions, as `body.py` prints them.

# A. Cross-chapter repetition and within-chapter redundancy

## A1. Chapters 7 to 14 (priority)

### Chapter 7 (`docs/book/Word/Chapter7/How_the_Brain_Learns_Chapter_7_Emotion_and_the_Body.md`)

Body words: 7380.

- **Thesis restated (emotion = body estimate that sets priorities)** (within-chapter). `docs/book/Word/Chapter7/How_the_Brain_Learns_Chapter_7_Emotion_and_the_Body.md:78`. Saves **27** words.
  - Current: "And every position agrees on the part this chapter needs: emotional states carry an estimate of how things stand for the body, and the estimate sets priorities."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Restates the thesis of line 16 and the Central Lesson (line 188).

- **Reward prediction error (home: Ch3 lines 50-66)** (cross-chapter). `docs/book/Word/Chapter7/How_the_Brain_Learns_Chapter_7_Emotion_and_the_Body.md:86`. Saves **9** words.
  - Current: "The reward prediction error that a large population of dopamine neurons signals, described in Chapter 3, is computed against outcomes whose value depends on the state of the body. A drop of juice"
  - Replace with: "The reward prediction error of Chapter 3 is computed against outcomes whose value depends on the state of the body: a drop of juice"
  - Note: The 'large population of dopamine neurons' hedge is stated in full in Ch3 line 64; callbacks need not repeat it.

- **Fear returns after extinction (stated in line 110)** (within-chapter). `docs/book/Word/Chapter7/How_the_Brain_Learns_Chapter_7_Emotion_and_the_Body.md:112`. Saves **6** words.
  - Current: "rather than erasing it, which is why the fear can return and why, as Chapter 5 noted,"
  - Replace with: "rather than erasing it, which is why, as Chapter 5 noted,"
  - Note: Line 110 already says extinction 'shares extinction's weakness: the fear can come back.'

- **Disorders as errors of estimation (stated in line 136)** (within-chapter). `docs/book/Word/Chapter7/How_the_Brain_Learns_Chapter_7_Emotion_and_the_Body.md:140`. Saves **17** words.
  - Current: "The evidence for these hypotheses is largely correlational. What they offer is a common language: if feeling is an estimate, disorders of feeling are errors of estimation, and treatments with good evidence behind them, such as exposure therapy and the reappraisal practiced in cognitive behavioral therapy, can be read as ways of correcting them."
  - Replace with: "The evidence for these hypotheses is largely correlational, but treatments with good evidence behind them, such as exposure therapy and the reappraisal practiced in cognitive behavioral therapy, can be read as ways of correcting errors of estimation."
  - Note: Line 136 opens the section with the same if-emotion-is-an-estimate argument.

- **Figure 7.1 described twice (text and caption)** (within-chapter). `docs/book/Word/Chapter7/How_the_Brain_Learns_Chapter_7_Emotion_and_the_Body.md:34`. Saves **9** words.
  - Current: "Figure 7.1 shows the difference prediction makes. A purely reactive controller lets glucose swing far from its set point before the correction catches up. A controller that releases insulin on the cue that a meal is coming acts before the disturbance arrives and keeps the swing small."
  - Replace with: "Figure 7.1 shows the difference prediction makes: a controller that releases insulin on the cue that a meal is coming acts before the disturbance arrives, while a purely reactive one lets glucose swing far from its set point."
  - Note: The caption gives the same contrast in full.

- **Sickness behavior: priorities point made twice** (within-chapter). `docs/book/Word/Chapter7/How_the_Brain_Learns_Chapter_7_Emotion_and_the_Body.md:54`. Saves **13** words.
  - Current: "Body signals do not only report a state; they reset the animal's priorities."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Hart's sentence immediately before already says the brain redirects energy 'by changing what feels worth doing'.

- **Opening: same point made three ways** (within-chapter). `docs/book/Word/Chapter7/How_the_Brain_Learns_Chapter_7_Emotion_and_the_Body.md:12`. Saves **13** words.
  - Current: "A model of the world is not yet a reason to do anything."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: The next two sentences ('Perception answers ... It does not answer ...') make the point.

**Chapter 7 total from proposed cuts: 94 words (1.3%).**

Author's call. These passages are unique, so cutting one removes its facts and orphans its footnotes:

- `docs/book/Word/Chapter7/How_the_Brain_Learns_Chapter_7_Emotion_and_the_Body.md:70`: Dutton and Aron's bridge study, 53 words, beginning "On the Capilano suspension bridge in Vancouver, 70 meters above ...". Orphans [^34].
- `docs/book/Word/Chapter7/How_the_Brain_Learns_Chapter_7_Emotion_and_the_Body.md:102`: BNST and sustained anxiety, 40 words, beginning "Nor does it work alone. A brief, cued fear depends ...". Orphans [^53].
- `docs/book/Word/Chapter7/How_the_Brain_Learns_Chapter_7_Emotion_and_the_Body.md:124`: Hand-holding in the scanner, 32 words, beginning "Its response in the moment also depends on company: women ...". Orphans [^66].
- `docs/book/Word/Chapter7/How_the_Brain_Learns_Chapter_7_Emotion_and_the_Body.md:152`: Flashbulb memories paragraph (Brown and Kulik, Challenger, 9/11), 157 words, beginning "The enhancement strengthens the conviction of memory more than its ...". Orphans [^86], [^87], [^88].

### Chapter 8 (`docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md`)

Body words: 7373.

- **Roadmap paragraph (duplicates Figure 8.1, section heads, and Central Lesson)** (within-chapter). `docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md:16`. Saves **82** words.
  - Current: "The argument of this chapter is that the brain meets these problems with a small set of mechanisms that can be described precisely and have been recorded in neurons. It accumulates evidence until it is sure enough, where "enough" is set by the cost of waiting and the cost of being wrong. It represents the value of options on a scale that lets unlike things be compared, and it bends that scale in ways that look irrational in the laboratory and often make sense in the world. It balances using what it knows against finding out more. And it runs more than one decision system at once, a deliberate one that plans from a model of the world and a fast one that repeats what has worked. Every one of these mechanisms is tuned by learning: the values, the bounds, the rate of exploration, and the balance between planning and habit are all set by outcomes. Figure 8.1 lays out the pieces, and the sections that follow take them in turn."
  - Replace with: "The argument of this chapter is that the brain meets these problems with a small set of mechanisms that have been recorded in neurons: it accumulates evidence until it is sure enough, values unlike options on one scale that it bends in ways that look irrational in the laboratory and often make sense in the world, balances using what it knows against finding out more, and runs a deliberate planner beside a fast habit system. Every one of them is tuned by outcomes. Figure 8.1 lays out the pieces."
  - Note: Each clause is restated at the head of its own section and again in the Central Lesson (line 166).

- **Deep brain stimulation explained (home: Ch3 line 120)** (cross-chapter). `docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md:40`. Saves **6** words.
  - Current: "treated by deep brain stimulation, in which an implanted electrode delivers continuous pulses to the subthalamic nucleus, the relay"
  - Replace with: "treated by deep brain stimulation of the subthalamic nucleus (Chapter 3), the relay"
  - Note: Ch3 line 120 describes the hardware and the procedure in full.

- **Reward prediction error restated (home: Ch3 lines 50-66)** (cross-chapter). `docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md:68`. Saves **22** words.
  - Current: "Values are not given; they are learned from outcomes, and the learning rule is the one Chapter 3 described. A large population of midbrain dopamine neurons signals the difference between the reward received and the reward predicted, and the error adjusts"
  - Replace with: "Values are not given; they are learned from outcomes by the reward prediction error of Chapter 3, which adjusts"
  - Note: Footnote [^29] stays at the end of the sentence.

- **Iowa patients and Fellows and Farah (home: Ch7 line 168)** (cross-chapter). `docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md:70`. Saves **23** words.
  - Current: "Chapter 7 left the Iowa patients with a problem of exactly this kind: the bad decks pay well at first and turn bad later, and Lesley Fellows and Martha Farah found that the patients' difficulty was largely explained by a failure to reverse what they had learned.[^32] The reason is now visible. The patients learned"
  - Replace with: "The Iowa patients of Chapter 7, whose difficulty Lesley Fellows and Martha Farah traced to a failure to reverse what they had learned, had a problem of exactly this kind.[^32] They learned"
  - Note: Ch7 line 168 already explains that the bad decks pay well first and that the deficit is one of reversal. Footnote [^32] kept.

- **Accumulation-to-bound summary repeated in AI section** (within-chapter). `docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md:154`. Saves **22** words.
  - Current: "The brain spends time in proportion to difficulty, stops when it is sure enough, and raises the bound when errors are expensive."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Restates lines 38-42 and the Central Lesson.

- **Biases as protections (stated at line 134)** (within-chapter). `docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md:162`. Saves **11** words.
  - Current: "Fifth, the biases are not simply errors to remove. A system designed to maximize expected value in every choice will be exploited by any environment that is adversarial, nonstationary, or poorly described by its probabilities. Loss aversion, ambiguity aversion, and a preference for reliable options are protections as well as distortions, and an artificial agent that must act in the world may need versions of them."
  - Replace with: "Fifth, the biases are not simply errors to remove. For the reasons given in the section on the cost of thinking, loss aversion, ambiguity aversion, and a preference for reliable options are protections as well as distortions, and an artificial agent that must act in an adversarial or changing world may need versions of them."
  - Note: Line 134 makes the same argument ('policies of a machine that must decide quickly ... in a world that is uncertain, changing, and sometimes adversarial').

- **Wald test: 'Bayesian inference ... one sample at a time' plus eye-movement aside** (within-chapter). `docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md:32`. Saves **18** words.
  - Current: "Chapter 6's eye movements are decisions of the same kind, each a choice of where to sample next."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Optional. Ch6 line 128 already calls a saccade 'a decision about where evidence is most needed'.

**Chapter 8 total from proposed cuts: 184 words (2.5%).**

Author's call. These passages are unique, so cutting one removes its facts and orphans its footnotes:

- `docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md:42`: Collapsing bounds and urgency, 69 words, beginning "When the difficulty of the evidence varies from trial to ...". Orphans [^11], [^12].
- `docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md:64`: Divisive normalization of value, 121 words, beginning "The scale may also be relative. Kenway Louie, Glimcher, and ...". Orphans [^26], [^27], [^28].
- `docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md:102`: Marshmallow trust studies (keep the final sentence), 67 words, beginning "Celeste Kidd, Holly Palmeri, and Richard Aslin found, in 28 ...". Orphans [^57], [^58].
- `docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md:142`: Henrich's 15 societies, 76 words, beginning "Joseph Henrich and colleagues ran the game in 15 small-scale ...". Orphans [^86].

Dependency: if the Ch8:42 passage goes, nothing else refers to collapsing bounds. Ch8:142 can go alone; Ch8:140 still closes the ultimatum-game thread.

### Chapter 9 (`docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md`)

Body words: 7740.

- **Roadmap says 'three things' but lists four; repeats Central Lesson** (within-chapter). `docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md:18`. Saves **35** words.
  - Current: "The argument of this chapter is that practice does three things, in different circuits, each of which can be described in terms the earlier chapters have introduced. It recalibrates movements that have drifted out of true, through the cerebellum's error-driven learning of Chapter 4. It binds separate actions into units and hands their control from circuits that deliberate to circuits that execute, through the basal ganglia and the dopamine signal of Chapter 3. The same dopamine signal grades the small variations that practice produces and keeps the ones that work. And practice changes the structure of the cortex, building and then protecting a few new connections."
  - Replace with: "The argument of this chapter is that practice works in several circuits, each described in terms the earlier chapters introduced: the cerebellum recalibrates movements that have drifted (Chapter 4); the basal ganglia and the dopamine signal of Chapter 3 bind actions into units, hand their control from circuits that deliberate to circuits that execute, and keep the variations that work; and the cortex builds and then protects a few new connections."
  - Note: Also fixes a factual slip: 'three things' followed by four. The same four items recur in the Central Lesson (line 168).

- **Diminishing returns stated twice** (within-chapter). `docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md:22`. Saves **13** words.
  - Current: "The tenth hour helps less than the first, but the thousandth still helps."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Same point as the previous sentence and as line 14 ('Practice does not stop working when a skill feels finished') and line 26.

- **Devalued-lever rat retold (line 12)** (within-chapter). `docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md:32`. Saves **12** words.
  - Current: "its signature is insensitivity to devaluation: the habitual rat keeps pressing when the food is no longer wanted."
  - Replace with: "its signature is insensitivity to devaluation."
  - Note: The rat is described at line 12, again at 140, 158, and 168.

- **H.M. mirror tracing (home: Ch5 line 156)** (cross-chapter). `docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md:34`. Saves **9** words.
  - Current: "Chapter 5 described the patient H.M. learning to trace a star in a mirror while denying each day that he had seen the task before; Suzanne Corkin found that he also improved over days at keeping a stylus on a moving target.[^8]"
  - Replace with: "Chapter 5's patient H.M., who learned mirror tracing while denying each day that he had seen the task, also improved over days, Suzanne Corkin found, at keeping a stylus on a moving target.[^8]"
  - Note: Already a callback; this only tightens it. Footnote [^8] kept.

- **Goal-directed vs habitual striatum (home: Ch8 line 122)** (cross-chapter). `docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md:70`. Saves **15** words.
  - Current: "Chapter 8 described two kinds of control, goal-directed actions that depend on the dorsomedial striatum and its prefrontal inputs and habits that depend on the dorsolateral striatum. Practice moves an action from the first to the second, and the shift has now been watched as it happens."
  - Replace with: "Practice moves an action from the goal-directed control of the dorsomedial striatum to the habitual control of the dorsolateral striatum (Chapter 8), and the shift has now been watched as it happens."
  - Note: Ch8 line 122 gives the anatomy and the lesion evidence.

- **Explore-exploit dilemma redefined (home: Ch8 lines 106-110)** (cross-chapter). `docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md:86`. Saves **14** words.
  - Current: "Chapter 8 described the dilemma between exploiting the best known option and exploring to find a better one; for a movement, exploration means"
  - Replace with: "For a movement, the exploration of Chapter 8 means"

- **Arbitration and the pianist (home of the pianist image is here; Ch10 line 144 and Ch11 line 120 repeat it)** (cross-chapter). `docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md:164`. Saves **1** words.
  - Current: "Chapter 8 described arbitration between planning and habit; practice adds a twist, because a routine runs only while a supervisor permits it, as the infralimbic experiments show."
  - Replace with: "Practice adds a twist to Chapter 8's arbitration between planning and habit: a routine runs only while a supervisor permits it, as the infralimbic experiments show."
  - Note: Tightening only.

- **Adaptation defined twice in consecutive sentences** (within-chapter). `docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md:50`. Saves **8** words.
  - Current: "Adaptation, however learned, is recalibration of something that already works. It returns a person"
  - Replace with: "Adaptation, however learned, returns a person"
  - Note: Line 38 already calls adaptation recalibration.

- **Habitual rat invoked again** (within-chapter). `docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md:158`. Saves **5** words.
  - Current: "reproduces the search's answers in the situations it was trained on, and like the habitual rat it does not consult the outcome."
  - Replace with: "reproduces the search's answers in the situations it was trained on and does not consult the outcome."
  - Note: 'brittle in the way habits are' in the previous sentence already makes the comparison.

**Chapter 9 total from proposed cuts: 112 words (1.4%).**

Author's call. These passages are unique, so cutting one removes its facts and orphans its footnotes:

- `docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md:58`: Ericsson, Chase, and Faloon's digit-span runner, 80 words, beginning "K. Anders Ericsson, Chase, and Steve Faloon took an undergraduate ...". Orphans [^24].
- `docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md:146`: Leon Fleisher anecdote, 110 words, beginning "Practice itself can go wrong. In 1964 the American pianist ...". Orphans [^85].
- `docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md:148`: Musician's dystonia and Byl's monkeys, 89 words, beginning "About one in 100 professional musicians develops musician's dystonia, a ...". Orphans [^86], [^87].

Dependency: Ch9:146 and Ch9:148 together make the 'Practice itself can go wrong' paragraph pair. Cut both, or keep 148 and open it with 'Practice itself can go wrong.'

### Chapter 10 (`docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md`)

Body words: 7780.

- **Hubel and Wiesel to Fukushima's neocognitron (home: Ch6 line 54)** (cross-chapter). `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md:26`. Saves **33** words.
  - Current: "The architecture of modern vision systems came from Chapter 6. David Hubel and Torsten Wiesel had found that neurons in visual cortex respond to oriented edges and that cells further along respond to the same edge over a wider area. Kunihiko Fukushima built that hierarchy into a network in 1980, alternating layers that detect features with layers that pool them, and called it the neocognitron.[^5]"
  - Replace with: "The architecture of modern vision systems came from Chapter 6: Kunihiko Fukushima's neocognitron of 1980 built Hubel and Wiesel's hierarchy of edge detectors into a network of alternating feature-detecting and pooling layers.[^5]"
  - Note: Ch6 line 54 tells the same history ('stacked alternating layers of feature detectors and pooling units in explicit imitation of Hubel and Wiesel's simple and complex cells'). Footnote [^5] kept.

- **Error-driven learning recap of Chapters 3, 5, 6** (cross-chapter). `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md:52`. Saves **24** words.
  - Current: "Chapter 3 showed that dopamine broadcasts such an error about reward, Chapter 5 that synapses change according to the timing of activity and a third factor that signals whether the change should count, and Chapter 6 that perception can be described as the continual correction of predictions by sensory error. In every case learning is driven by error and aimed at prediction."
  - Replace with: "Dopamine broadcasts such an error about reward (Chapter 3), synapses change by timing and a third factor (Chapter 5), and perception corrects its predictions by sensory error (Chapter 6): learning is driven by error and aimed at prediction."
  - Note: Pure recap; Chapter 12 line 14 and Figure 12.1 recap the same list again.

- **Catastrophic interference and complementary learning systems (home: Ch5 line 116; also Ch1 line 56)** (cross-chapter). `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md:88`. Saves **10** words.
  - Current: "The obstacle is the one Michael McCloskey and Neal Cohen found in 1989 and Chapter 5 described: a network trained on a second set of associations loses the first.[^39]"
  - Replace with: "The obstacle is the catastrophic interference that Michael McCloskey and Neal Cohen found in 1989 (Chapters 1 and 5).[^39]"
  - Note: Also corrects the cross-reference: McCloskey and Cohen are named in Ch1 line 56, not in Ch5.

- **Complementary learning systems restated (home: Ch5 line 116)** (cross-chapter). `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md:88`. Saves **21** words.
  - Current: "The brain's answer, on the complementary learning systems theory of Chapter 5, is to keep a fast learner, the hippocampus, that stores episodes at once and replays them into a slow one, the cortex, interleaved with what it already knows.[^40]"
  - Replace with: "The brain's answer is the complementary learning systems of Chapter 5, a fast hippocampal learner replaying into slow cortex.[^40]"
  - Note: Fourth full statement of the theory in the book (Ch1:56, Ch5:116, Ch10:88; later Ch12:112, Ch13:132). Footnote [^40] kept.

- **Pianist and the wrong note (home: Ch9 line 164)** (cross-chapter). `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md:144`. Saves **15** words.
  - Current: "A pianist plays automatically until a wrong note, and the wrong note is the signal."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Ch9 line 164 has the image; Ch11 line 120 uses it a third time.

- **Sorting of differences restated (lines 18, 150, 154 and Central Lesson 172)** (within-chapter). `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md:156`. Saves **16** words.
  - Current: "Sorted this way, the differences named at the start of this chapter fall on both sides. Learning all its life without forgetting, and an honest estimate of what it knows, are solutions to problems that every system meets once it is put to use, and machines lack them to their cost."
  - Replace with: "Sorted this way, the differences named at the start of this chapter fall on both sides. Lifelong learning without forgetting, and an honest estimate of what it knows, are solutions machines lack to their cost."
  - Note: Tightening; line 150 has just said these are 'problems that a learning system meets when it leaves the laboratory'.

- **Plasticity maintained (rhetorical close)** (within-chapter). `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md:94`. Saves **19** words.
  - Current: "Plasticity in the brain is not a phase but a maintained state, and it is maintained at a cost."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Optional. The point is made by the preceding sentence; Ch5 line 144 makes the 'cost' point.

- **Feedback alignment, bursts, predictive coding (homes: Ch3 line 74, Ch6 line 162)** (cross-chapter). `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md:100`. Saves **31** words.
  - Current: "The two most developed answers were met in Chapters 3 and 6. Chapter 3 showed that a backward pathway with random, fixed weights can be enough, because the forward weights come to align with it, and that bursts arriving at the apical dendrites of pyramidal neurons could carry an error apart from the cell's main output.[^46] Chapter 6 showed that a network built to correct its own predictions, as cortex may be, can compute nearly the same weight changes that backpropagation does, using only plasticity local to each synapse.[^47]"
  - Replace with: "The two most developed answers were met in Chapters 3 and 6: a backward pathway with random, fixed weights, to which the forward weights come to align, with bursts at the apical dendrites carrying the error;[^46] and a network that corrects its own predictions, which can compute nearly the same weight changes as backpropagation using only local plasticity.[^47]"
  - Note: Both footnotes kept.

**Chapter 10 total from proposed cuts: 169 words (2.2%).**

Author's call. These passages are unique, so cutting one removes its facts and orphans its footnotes:

- `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md:46`: Grid cells in trained networks, 116 words, beginning "Even the brain's map of space has appeared unbidden. Andrea ...". Orphans [^19], [^20].
- `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md:64`: Recht and Engstrom fresh-test-set study, 87 words, beginning "Benjamin Recht and his colleagues built a fresh test set ...". Orphans [^27], [^28].
- `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md:166`: Innateness and Piantadosi, 115 words, beginning "Third, machine learning has reopened an old argument about how ...". Orphans [^80], [^81].

Dependency: Ch10:166 is the 'Third' item of a numbered list, so renumber if it goes. Check Figure 10.7 (ledger) for rows that point to removed passages.

### Chapter 11 (`docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md`)

Body words: 7611.

- **Roadmap list of eight borrowings (duplicates section heads and Figure 11.4)** (within-chapter). `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md:16`. Saves **60** words.
  - Current: "This chapter takes the borrowable solutions one at a time: learning for a lifetime without forgetting, a memory that learns while it is used, signals that decide when and how fast to learn, learning by local rules on frugal hardware, values that cannot be redefined, knowing when to stop and think, a curriculum that grows with the learner, and the use of recordings from brains to train machines. For each, the questions are what the brain does, what has been built in its image, how well the copy works, and what is still missing."
  - Replace with: "This chapter takes the borrowable solutions one at a time, asking of each what the brain does, what has been built in its image, how well the copy works, and what is still missing."
  - Note: The section headings name the eight borrowings, and the Central Lesson (line 152) lists them again.

- **Small network losing a list (home: Ch10 line 88, Figure 10.5)** (cross-chapter). `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md:32`. Saves **29** words.
  - Current: "Chapter 10 showed a small network losing one list of associations when trained on another, and recovering it when a few old items were replayed. Replay is the obvious remedy, one that machine learning found for itself and has used for more than 30 years, but it has a cost the brain does not pay in the same way: storing old examples."
  - Replace with: "Replay, the remedy Chapter 10 demonstrated and one that machine learning has used for more than 30 years, has a cost the brain does not pay in the same way: storing old examples."

- **Pattern completion defined twice (line 50)** (within-chapter). `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md:54`. Saves **11** words.
  - Current: "Chapter 5 described recall as pattern completion, in which a fragment of a memory settles into the whole. John Hopfield"
  - Replace with: "Chapter 5 described recall as pattern completion. John Hopfield"
  - Note: Line 50 has just said 'a fragment of the experience can reactivate the whole'; the Hopfield sentence that follows says it again.

- **Behrens volatility experiment (first told: Ch8 line 110)** (cross-chapter). `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md:66`. Saves **23** words.
  - Current: "Timothy Behrens and his colleagues had people choose, over hundreds of trials, between a blue and a green option, one of which paid off more often. For long stretches the better option stayed the same; in other stretches it switched every few dozen trials. People learned faster in the volatile stretches and more slowly in the stable ones, weighting each new outcome as an ideal learner would, and activity in the anterior cingulate cortex tracked how volatile the world had become.[^34] The brain sets its own learning rate, moment by moment."
  - Replace with: "Chapter 8 introduced Timothy Behrens's evidence that the brain sets its own learning rate. Choosing over hundreds of trials between a blue and a green option, one of which paid off more often, people learned faster in stretches where the better option switched every few dozen trials than where it stayed the same, as an ideal learner would, and activity in the anterior cingulate cortex tracked the volatility.[^34]"
  - Note: Keeps every fact (blue/green, few dozen trials, ACC) and footnote [^34]. If adopted, Ch12 line 80 should cite Chapter 8 (see Ch12 entry).

- **Neuromodulator roles and Doya (home: Ch3 lines 104-108 and 130; also Ch7 line 180)** (cross-chapter). `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md:68`. Saves **23** words.
  - Current: "Chapter 3 described a brain whose neuromodulators do ask: acetylcholine shifts the balance toward taking in new information, norepinephrine signals that the world has changed, and dopamine says what was better or worse than expected. Kenji Doya's proposal, met in Chapter 3, maps the four main neuromodulators onto the settings a learning machine needs.[^36]"
  - Replace with: "Chapter 3 described a brain whose neuromodulators do ask, and Kenji Doya's proposal, met in Chapters 3 and 7, maps the four of them onto the settings a learning machine needs.[^36]"
  - Note: Third statement of Doya's mapping and fourth listing of the modulators' roles. Footnote [^36] kept.

- **Fixed learning-rate schedule (stated at line 68)** (within-chapter). `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md:72`. Saves **16** words.
  - Current: "A learning-rate schedule fixed in advance has no way to know that the world has changed."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Line 68: 'nothing in the schedule asks whether the world has just changed'.

- **Eligibility trace callback doubled** (cross-chapter). `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md:90`. Saves **11** words.
  - Current: "This is the three-factor rule of Chapter 3, rederived from the mathematics of gradient descent, with the eligibility trace that Chapter 3 described at real synapses and a broadcast signal in place of the neuromodulator."
  - Replace with: "This is the three-factor rule of Chapter 3, rederived from the mathematics of gradient descent, with a broadcast signal in place of the neuromodulator."
  - Note: The eligibility trace is named in the previous sentence.

- **Homeostatic reinforcement learning definition (first: Ch7 line 176)** (cross-chapter). `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md:104`. Saves **-1** words.
  - Current: "Chapter 7 described the brain's alternative, in Mehdi Keramati and Boris Gutkin's homeostatic reinforcement learning. Reward is not a number delivered from outside but the reduction"
  - Replace with: "Chapter 7 described the brain's alternative, Mehdi Keramati and Boris Gutkin's homeostatic reinforcement learning, in which reward is not a number delivered from outside but the reduction"
  - Note: Small tightening; Ch11 is the better home because it carries Figure 11.7.

- **Complementary-learning confirmation restated (Ch10 line 88, Ch11 lines 32-34)** (within-chapter). `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md:146`. Saves **17** words.
  - Current: "Complementary learning systems theory predicted that a single network trained in sequence would forget, and that interleaving would prevent it; machines confirmed both, and Chapter 10's simulation repeats the confirmation in a few lines of code."
  - Replace with: "Machines confirmed complementary learning systems theory's prediction that a network trained in sequence forgets and that interleaving prevents it."

- **Building as a test of theory (stated at line 144)** (within-chapter). `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md:148`. Saves **20** words.
  - Current: "Building the brain's remaining solutions is also how neuroscience will find out whether its theories of the brain are right."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Line 144: 'A theory of how the brain learns is incomplete until something built on it learns'.

- **Pianist and the wrong note (home: Ch9 line 164)** (cross-chapter). `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md:120`. Saves **14** words.
  - Current: ", as the pianist of Chapter 9 hears the wrong note before thinking about it."
  - Replace with: "."
  - Note: Optional; third use of the image.

**Chapter 11 total from proposed cuts: 223 words (2.9%).**

Author's call. These passages are unique, so cutting one removes its facts and orphans its footnotes:

- `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md:60`: Transformer place and grid cells, 50 words, beginning "James Whittington, Joseph Warren, and Timothy Behrens showed that a ...". Orphans [^32].
- `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md:138`: Other brain-data training studies, 52 words, beginning "Other groups have made networks' internal representations resemble those of ...". Orphans [^75].

### Chapter 12 (`docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md`)

Body words: 7293.

- **Recap of prediction in Chapters 3-9 (duplicates Figure 12.1; stale count)** (cross-chapter). `docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md:14`. Saves **59** words.
  - Current: "The previous eleven chapters met prediction everywhere. Dopamine neurons signaled the difference between the reward that arrived and the reward that was predicted (Chapter 3). The hippocampus replayed sequences and laid down expectations of where the animal would go next (Chapters 5 and 10). Sensory cortex sent predictions down and errors up (Chapter 6). The brain regulated the body by anticipating its needs (Chapter 7), weighed choices by their predicted outcomes and its confidence in them (Chapter 8), and moved by comparing the predicted consequences of each movement with the real ones (Chapter 9). Figure 12.1 collects these."
  - Replace with: "The previous chapters met prediction everywhere: in dopamine neurons (Chapter 3), hippocampal replay (Chapters 5 and 10), sensory cortex (Chapter 6), the regulation of the body (Chapter 7), choice (Chapter 8), and movement (Chapter 9). Figure 12.1 collects these."
  - Note: Figure 12.1 gives what each system predicts and its error signal. Also removes the 'eleven' count (there are twelve chapters before this one, counting Chapter 0).

- **Reactive vs predictive controller (home: Ch7 line 34, Figure 7.1)** (cross-chapter). `docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md:36`. Saves **27** words.
  - Current: "A controller that waits for an error to appear corrects it late and overshoots. A controller that predicts the disturbance can cancel it as it arrives, and Peter Sterling,"
  - Replace with: "Peter Sterling,"
  - Note: Footnote [^9] sentence kept.

- **Two kinds of prediction error (home: Ch6 line 64; also Ch3 line 64)** (cross-chapter). `docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md:72`. Saves **37** words.
  - Current: "Chapter 6 was careful to distinguish the dopamine neuron's error, a single number broadcast widely that says whether things went better or worse than expected, from the errors of sensory cortex, a whole pattern of mismatches feature by feature that never leaves the sensory hierarchy. The cerebellum's error arrives on climbing fibers, one to each Purkinje cell, and says which movement went wrong. They differ in their anatomy, their speed, and their meaning."
  - Replace with: "Chapter 6 distinguished the dopamine neuron's scalar error about value from the feature-by-feature errors of sensory cortex, and the cerebellum's error arrives on climbing fibers, one to each Purkinje cell, and says which movement went wrong."
  - Note: Third full statement of the distinction; the last sentence also repeats line 68.

- **Behrens and Yu-Dayan (homes: Ch8 line 110, Ch3 line 104)** (cross-chapter). `docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md:80`. Saves **22** words.
  - Current: "As Chapter 11 described with Behrens's blue and green options, people adjust their learning rate to the volatility of the world, and the neuromodulatory account of Chapter 3, Angela Yu and Peter Dayan's, has acetylcholine report the expected uncertainty of a noisy but stable world and norepinephrine the unexpected uncertainty of one that has changed.[^31]"
  - Replace with: "People adjust their learning rate to the volatility of the world (Chapters 8 and 11), and on Angela Yu and Peter Dayan's account (Chapter 3) acetylcholine reports expected uncertainty and norepinephrine unexpected uncertainty.[^31]"
  - Note: Yu and Dayan's account is stated in Ch3:104, Ch6:102, here, and Ch13:136. Footnote [^31] kept.

- **Savings caveat (home: Ch9 line 44)** (cross-chapter). `docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md:106`. Saves **17** words.
  - Current: "; Chapter 9 described both and noted that savings after an adaptation has been fully washed out seems to need something more.[^40]"
  - Replace with: "; Chapter 9 described both.[^40]"
  - Note: The caveat is stated in Ch9 line 44.

- **Fast and slow learners (home: Ch5 line 116)** (cross-chapter). `docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md:112`. Saves **38** words.
  - Current: "The timescales also answer a problem that Chapters 5 and 10 raised, the balance between learning and remembering. A system with only a fast learner would forget everything it knew whenever the world changed; one with only a slow learner could not keep up. Layering fast processes on slow ones lets the brain follow the moment without losing what is reliably true, which is what Chapter 10's catastrophically forgetting network could not do."
  - Replace with: "The timescales also answer the problem of Chapters 5 and 10, the balance between learning and remembering: layering fast processes on slow ones lets the brain follow the moment without losing what is reliably true."
  - Note: Fifth statement of the fast/slow argument.

- **Kinds of error listed again (line 72)** (within-chapter). `docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md:156`. Saves **20** words.
  - Current: "Fourth, the brain learns from many errors at once, of different kinds: a single number about reward broadcast widely, a pattern of errors in each sensory area, a movement error delivered to each Purkinje cell."
  - Replace with: "Fourth, the brain learns from many errors at once, of the different kinds described above."

- **What prediction leaves out (line 144; repeated again in Ch13 line 14)** (within-chapter). `docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md:158`. Saves **11** words.
  - Current: "What prediction leaves unexplained, why the brain is built as it is, depends on the constraints under which it evolved, and those are the subject of Chapter 13."
  - Replace with: "The constraints under which the brain evolved, which prediction leaves unexplained, are the subject of Chapter 13."

**Chapter 12 total from proposed cuts: 231 words (3.2%).**

Author's call. These passages are unique, so cutting one removes its facts and orphans its footnotes:

- `docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md:26`: Flash-lag effect, 63 words, beginning "One sign that the brain compensates is the flash-lag effect: ...". Orphans [^3].
- `docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md:108`: Slow-speed prior and fog driving, 171 words, beginning "Even long-held priors can be revised. People assume, other things ...". Orphans [^41], [^42], [^43].
- `docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md:128`: Isomura cultured neurons, 121 words, beginning "The principle has had direct tests, with results that show ...". Orphans [^54].
- `docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md:130`: Kagan's Pong-playing cultures, 125 words, beginning "Brett Kagan and his colleagues connected cultures of mouse or ...". Orphans [^55], [^56].

Dependency: Ch12:110 opens 'Chapter 6's light from above ... makes the same point', which refers back to line 108. If 108 goes, open 110 with 'Long-held priors can be revised: Chapter 6's light from above ...'. Ch12:128 and Ch12:130 form a pair: 130's closing sentence ('Both studies ...') needs rewording if only one goes.

### Chapter 13 (`docs/book/Word/Chapter13/How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md`)

Body words: 7720.

- **Recap of the book and of Ch12's closing questions** (cross-chapter). `docs/book/Word/Chapter13/How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md:14`. Saves **31** words.
  - Current: "The earlier chapters have described what the brain does: how its cells signal, how chemicals reset its circuits, how it learns, perceives, feels, decides, and practices, and, in Chapter 12, how much of that activity can be read as prediction. Chapter 12 closed with questions prediction cannot answer:"
  - Replace with: "The earlier chapters described what the brain does, and Chapter 12 closed with questions prediction cannot answer:"
  - Note: Ch12 lines 144 and 158 have just asked these questions; the list of earlier topics recurs in Ch15 line 16.

- **Synaptic failures (home: Ch1 line 80; repeated Ch2 line 58)** (cross-chapter). `docs/book/Word/Chapter13/How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md:30`. Saves **14** words.
  - Current: "The argument extends to the synaptic failures that Chapter 1 described, in which more than half of the impulses arriving at a hippocampal synapse release nothing."
  - Replace with: "The argument extends to the synaptic failures of Chapters 1 and 2."
  - Note: Third statement of Allen and Stevens's figure.

- **Complementary learning systems (home: Ch5 line 116)** (cross-chapter). `docs/book/Word/Chapter13/How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md:132`. Saves **28** words.
  - Current: "The constraint here is statistical rather than physical: a single network that learns fast enough to capture one experience will overwrite what it already knew, so two learners working at different rates are the economical answer."
  - Replace with: "Here the constraint is statistical rather than physical."
  - Note: Sixth statement of the fast/slow argument.

- **'Moves along fronts' stated twice** (within-chapter). `docs/book/Word/Chapter13/How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md:136`. Saves **25** words.
  - Current: "A fixed design must choose one compromise for every situation. A design that can move along its fronts can choose a different compromise for each."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: The paragraph opens with the same point ('it moves along them as conditions change'), and line 158 and the Central Lesson repeat it.

- **Wiring-cost hierarchy: closing restatement** (within-chapter). `docs/book/Word/Chapter13/How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md:72`. Saves **19** words.
  - Current: "But a brain that pays for every axon is pushed toward the arrangement of areas the earlier chapters described."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Optional; restates the paragraph's first sentence.

- **Pareto front re-defined** (within-chapter). `docs/book/Word/Chapter13/How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md:128`. Saves **7** words.
  - Current: "sits on a trade-off that no amount of engineering could remove, because improving one side worsens the other."
  - Replace with: "sits on a trade-off that no amount of engineering could remove."
  - Note: Line 76 defines the front in these terms.

**Chapter 13 total from proposed cuts: 124 words (1.6%).**

Author's call. These passages are unique, so cutting one removes its facts and orphans its footnotes:

- `docs/book/Word/Chapter13/How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md:94`: Obstetric dilemma, 152 words, beginning "Size also meets the constraint of birth. The traditional view, ...". Orphans [^40], [^41].
- `docs/book/Word/Chapter13/How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md:96`: Elephantnose fish and Megaphragma, 127 words, beginning "At the extremes, the constraints are stark. The elephantnose fish, ...". Orphans [^42], [^43].

Dependency: check Figures 13.1 and 13.7 for rows that cite birth or the elephantnose fish before cutting Ch13:94 or Ch13:96.

### Chapter 14 (`docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md`)

Body words: 7003.

- **Bridge sentence repeated from Ch13 line 160** (cross-chapter). `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md:20`. Saves **21** words.
  - Current: "Chapter 13 ended by noting that these constraints do not disappear when the brain is put to work in classrooms, in offices, and in front of screens. This chapter asks what they imply."
  - Replace with: "This chapter asks what those constraints imply for classrooms, offices, and screens."
  - Note: Ch13 line 160 says the same sentence almost word for word.

- **Forgetting curve recap (home: Ch5 line 140) and factual mismatch** (cross-chapter). `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md:40`. Saves **2** words.
  - Current: "Chapter 5 described the forgetting curve and three things that slow it, retrieval, spacing, and sleep, and Chapter 9"
  - Replace with: "Chapter 5 described the forgetting curve and how spaced retrieval and sleep slow it, and Chapter 9"
  - Note: Ch5's three things are retrieval (helped by spacing), sleep, and emotional significance; the current wording misstates them.

- **Sleep consolidation recap (home: Ch5 lines 118-126)** (cross-chapter). `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md:66`. Saves **11** words.
  - Current: "Chapter 5 described how sleep consolidates what was learned during the day, replaying it and moving it from the hippocampus toward the cortex."
  - Replace with: "Chapter 5 described how sleep consolidates what was learned during the day."

- **Self-control summary restating lines 86-88** (within-chapter). `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md:90`. Saves **27** words.
  - Current: "The evidence supports a narrower conclusion. Sustained demanding work over many hours does shift people toward easier and quicker options, but the dramatic short-term effects once attributed to depleted willpower are not reliable. Breaks,"
  - Replace with: "The evidence supports a narrower conclusion. Breaks,"
  - Note: Both halves of the deleted sentence are the findings of lines 86 and 88.

- **Bastani and Kestin results restated (lines 112-120)** (within-chapter). `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md:144`. Saves **24** words.
  - Current: "Bastani's unrestricted chatbot raised scores in practice and lowered them on the exam; Kestin's tutor, which guided students through each step, did the opposite."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Also removes an inaccuracy: Kestin's study did not compare practice with exam scores, so 'did the opposite' overstates it.

- **Bainbridge's last irony restated (quoted at line 104)** (within-chapter). `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md:146`. Saves **18** words.
  - Current: "Second, automation should leave its users practiced. Bainbridge's last irony was that the most reliable systems need the most training for the people who must take over when they fail. Aviation"
  - Replace with: "Second, automation should leave its users practiced, as Bainbridge's last irony warns. Aviation"

- **Bridge to Ch15 repeats Ch15 line 16** (cross-chapter). `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md:152`. Saves **31** words.
  - Current: "The book has now described the brain's cells and circuits, its strategies, the constraints that shaped them, and what follows for the way people live. What remains is to put these pieces together into one model of how the brain learns, and that is the task of Chapter 15."
  - Replace with: "Putting these pieces together into one model of how the brain learns is the task of Chapter 15."
  - Note: Ch15 line 16 lists the same parts. The old wording ('What remains') also reads as if Chapter 15 were the last chapter.

- **Recap of Chapters 3, 9, 13 before the Instagram study** (within-chapter). `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md:124`. Saves **32** words.
  - Current: "Chapter 3 described how dopamine neurons teach the brain which actions pay off, and Chapter 9 how repeated rewarded actions become habits cued by context. Chapter 13 described supernormal stimuli, objects that trigger an instinct more strongly than anything in the world it evolved in. All three ideas have been applied,"
  - Replace with: "Dopamine teaching (Chapter 3), habits cued by context (Chapter 9), and supernormal stimuli (Chapter 13) have all been applied,"
  - Note: Optional tightening.

- **Prediction-error analogy** (cross-chapter). `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md:48`. Saves **15** words.
  - Current: ", much as Chapter 12's prediction errors drive learning hardest when expectation and outcome differ"
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Optional; the analogy is repeated at line 58 ('the answer arrives as a prediction error').

- **Bruer's point restated** (within-chapter). `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md:22`. Saves **22** words.
  - Current: "A fact about synapses does not become a lesson plan without passing through experiments on how people actually learn and work, and the evidence that matters most in this chapter is of that kind."
  - Replace with: "The evidence that matters most in this chapter is of that kind."
  - Note: The preceding sentence (Bruer's 'stop in between, in the psychology of how people learn') already says it.

**Chapter 14 total from proposed cuts: 203 words (2.9%).**

Author's call. These passages are unique, so cutting one removes its facts and orphans its footnotes:

- `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md:34`: Left-brained / right-brained, 47 words, beginning "The popular idea that people are "left-brained" or "right-brained" fared ...". Orphans [^11].
- `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md:62`: Ramirez and Beilock expressive writing, 93 words, beginning "Another brief intervention shows how hard such effects are to ...". Orphans [^23], [^24].
- `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md:70`: Tablet light and melatonin, 130 words, beginning "Light is one of the things that pushes bedtime later. ...". Orphans [^28].
- `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md:118`: Kosmyna EEG preprint, 92 words, beginning "Measures of the brain itself are only beginning. Nataliya Kosmyna, ...". Orphans [^55].

Dependency: Figure 14.7 (ledger of evidence) may list learning styles, expressive writing, left/right brain, or screens at night. Remove the matching row if a passage goes.

## A2. Other chapters (secondary, same rules)

### Chapter 0 (`docs/book/Word/Chapter0/How_the_Brain_Learns_Chapter_0_Foundations.md`)

- **Hodgkin and Huxley 1952 model (fuller telling: Ch1 line 40)** (cross-chapter). `docs/book/Word/Chapter0/How_the_Brain_Learns_Chapter_0_Foundations.md:78`. Saves **20** words.
  - Current: "Their model explained in quantitative detail how the opening and closing of sodium and potassium channels generate the electrical impulse."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: The next sentence (Figure 0.7) shows exactly this; Ch1 line 40 and Ch2 line 96 explain it again.

**Chapter 0 total: 20 words.**

### Chapter 1 (`docs/book/Word/Chapter1/How_the_Brain_Learns_Chapter_1_What_the_Brain_Is.md`)

- **No global objective but local errors (home: Ch3 line 84; also Ch3 line 134, Ch6 line 110)** (cross-chapter). `docs/book/Word/Chapter1/How_the_Brain_Learns_Chapter_1_What_the_Brain_Is.md:86`. Saves **54** words.
  - Current: "Nor is it true that the brain optimizes nothing. There is no single global objective that the whole brain minimizes by gradient descent, as an artificial network minimizes its loss, but many of its circuits are well described as minimizing a local error or cost: the reward prediction error carried by a large population of dopamine neurons in Chapter 3, the sensory prediction error of Chapter 6, and the near-optimal combination of cues that Chapter 6 also describes."
  - Replace with: "Nor does the brain optimize nothing: Chapters 3 and 6 show circuits that minimize a local error or cost, though no single global objective."
  - Note: Four statements of the same point in Chapters 1, 3 (twice), and 6.

**Chapter 1 total: 54 words.**

### Chapter 2 (`docs/book/Word/Chapter2/How_the_Brain_Learns_Chapter_2_Neurons.md`)

- **Golgi stain (first told: Ch1 line 92)** (cross-chapter). `docs/book/Word/Chapter2/How_the_Brain_Learns_Chapter_2_Neurons.md:14`. Saves **12** words.
  - Current: "with Camillo Golgi's silver method, which blackens only about one cell in a hundred and leaves the rest invisible, and drew"
  - Replace with: "with Camillo Golgi's silver method (Chapter 1) and drew"
  - Note: Ch1 line 92 gives the one-in-a-hundred fact and the discrete-cells conclusion.

- **Attwell and Laughlin energy budget (home: Ch1 line 46)** (cross-chapter). `docs/book/Word/Chapter2/How_the_Brain_Learns_Chapter_2_Neurons.md:24`. Saves **15** words.
  - Current: "David Attwell and Simon Laughlin estimated that in the gray matter of the rodent brain, the tissue that holds cell bodies and synapses, most of the energy budget goes to pumping back the ions that signaling lets through.[^4]"
  - Replace with: "By Attwell and Laughlin's estimate in Chapter 1, most of the energy budget goes to pumping back the ions that signaling lets through.[^4]"
  - Note: Ch2 line 126 cites the same budget a second time.

- **Same point in two consecutive sentences** (within-chapter). `docs/book/Word/Chapter2/How_the_Brain_Learns_Chapter_2_Neurons.md:98`. Saves **9** words.
  - Current: "Nothing travels the length of the axon except causation."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Previous sentence: 'No particle travels the length of the axon; what travels is a pattern of channel openings'.

- **Thorpe's animal-detection experiment (home: Ch1 line 30)** (cross-chapter). `docs/book/Word/Chapter2/How_the_Brain_Learns_Chapter_2_Neurons.md:112`. Saves **13** words.
  - Current: "Simon Thorpe and his colleagues flashed photographs for twenty milliseconds and asked people to respond only if the picture contained an animal; brain signals distinguishing the two kinds of trial appeared about 150 milliseconds after the flash.[^38]"
  - Replace with: "In Simon Thorpe's experiment of Chapter 1, brain signals distinguishing photographs with and without an animal appeared about 150 milliseconds after a twenty-millisecond flash.[^38]"
  - Note: Ch6 line 54 cites the same result a third time.

- **Sterling and Laughlin near-optimal design (home: Ch1 line 86)** (cross-chapter). `docs/book/Word/Chapter2/How_the_Brain_Learns_Chapter_2_Neurons.md:130`. Saves **13** words.
  - Current: "Peter Sterling and Simon Laughlin argue that, under these constraints, neural design is close to efficient: neurons send information at the lowest rate that will serve, use the cheapest signal that will carry it, and fire sparsely because every spike is paid for.[^44]"
  - Replace with: "Peter Sterling and Simon Laughlin argue, as Chapter 1 noted, that under these constraints neural design is close to efficient, with neurons firing sparsely because every spike is paid for.[^44]"
  - Note: Near-verbatim repeat of Ch1 line 86.

**Chapter 2 total: 62 words.**

### Chapter 3 (`docs/book/Word/Chapter3/How_the_Brain_Learns_Chapter_3_Neuromodulation.md`)

- **Two kinds of prediction error (home: Ch6 line 64)** (cross-chapter). `docs/book/Word/Chapter3/How_the_Brain_Learns_Chapter_3_Neuromodulation.md:64`. Saves **36** words.
  - Current: "Second, the error in question is a single number about value, about how much better or worse things went than expected. Chapter 6 introduces a different prediction error, the difference between what the senses deliver and what the cortex expected them to deliver, which is high-dimensional and about content rather than value. The two share a name and a logic, but they are different signals."
  - Replace with: "Second, the error in question is a single number about value; Chapter 6 introduces a different, high-dimensional prediction error about sensory content, and the two should not be confused."
  - Note: Ch6 line 64 states the contrast in full.

- **Local objectives restated (line 84)** (within-chapter). `docs/book/Word/Chapter3/How_the_Brain_Learns_Chapter_3_Neuromodulation.md:134`. Saves **15** words.
  - Current: "No loss function is handed to the brain. It has many local errors, the temporal-difference error among them, and it reduces them under"
  - Replace with: "The brain reduces its many local errors under"
  - Note: Footnote [^48] kept.

**Chapter 3 total: 51 words.**

### Chapter 4 (`docs/book/Word/Chapter4/How_the_Brain_Learns_Chapter_4_Circuits.md`)

- **'Energy will become the binding constraint' motif (also Ch1:102, Ch10:112, Ch11:94)** (cross-chapter). `docs/book/Word/Chapter4/How_the_Brain_Learns_Chapter_4_Circuits.md:170`. Saves **15** words.
  - Current: "As energy becomes the binding constraint on large models, the brain's economies are worth studying."
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Optional; Ch10 line 112 is the home of this argument.

**Chapter 4 total: 15 words.**

### Chapter 6 (`docs/book/Word/Chapter6/How_the_Brain_Learns_Chapter_6_Perception_as_Inference.md`)

- **Sense in which the brain optimizes (home: Ch3 line 84)** (cross-chapter). `docs/book/Word/Chapter6/How_the_Brain_Learns_Chapter_6_Perception_as_Inference.md:110`. Saves **34** words.
  - Current: "This is also the sense, and the only sense, in which this book says that the brain optimizes. Chapter 3 argued that there is no single global objective trained by gradient descent; what there is, here and in the dopamine error of that chapter, is a circuit that behaves as if it were minimizing a well-defined local cost, in this case the variance of its estimate."
  - Replace with: "This is the local sense, argued in Chapter 3, in which the brain optimizes: a circuit behaves as if it were minimizing a well-defined local cost, here the variance of its estimate."

- **Ch1 slogan quoted a second time (also Ch4 line 82)** (cross-chapter). `docs/book/Word/Chapter6/How_the_Brain_Learns_Chapter_6_Perception_as_Inference.md:118`. Saves **16** words.
  - Current: "Chapter 1 put it in one sentence: "The brain generates behavior, and the world corrects it.""
  - Replace with: (delete; text before and after joins cleanly)
  - Note: Optional; Ch4 line 82 already quotes the slogan.

- **Hubel and Wiesel monocular deprivation (home: Ch1 line 62)** (cross-chapter). `docs/book/Word/Chapter6/How_the_Brain_Learns_Chapter_6_Perception_as_Inference.md:136`. Saves **31** words.
  - Current: "The window was discovered by Hubel and Wiesel in the 1960s. A kitten with one eye closed for a few weeks early in life loses, permanently, the cortical representation of that eye; the same closure in an adult does nothing.[^45] The period during which experience can reorganize the visual cortex is called the critical period, and it"
  - Replace with: "The window is the one Hubel and Wiesel found in kittens with one eye closed (Chapter 1).[^45] This critical period (the sensitive period of Chapter 1)"
  - Note: Ch1 line 62 tells the experiment in full. Also reconciles 'critical' (Ch6) with 'sensitive' (Ch1, Ch13, Ch14).

**Chapter 6 total: 81 words.**

## A3. Index of repeated items (every occurrence, with the home)

Approximate word counts are for the passage devoted to the item at that line. "Cut" means a proposal in A1 or A2 above. "Keep" means the occurrence is already a short callback or adds new material.

1. **Catastrophic interference and complementary learning systems (McCloskey and Cohen; McClelland, McNaughton, and O'Reilly).** Home: **Ch5:116** (~140). Others: Ch1:56 (~110; the only place McCloskey and Cohen are named, so keep as the preview), Ch1:106 (~50, keep), Ch3:22 (~45, stability-plasticity, keep), Ch5:162 (~60, keep), Ch5:168 (~75, replay convergence, keep), Ch9:162 (~15, keep), Ch10:88 (~150 with Figure 10.5, cut x2), Ch11:32 (~55, cut), Ch11:146 (~40, cut), Ch12:112 (~70, cut), Ch13:132 (~70, cut), Ch15:22 and Ch15:40 (synthesis recap, keep), Ch16:90 (~60, diagnostic, keep). This is the most retold idea in the book: six full statements before the cuts.
2. **Schultz's dopamine neurons and the reward prediction error.** Home: **Ch3:48-66** (~700). Others: Ch1:86 (~25, cut in A2), Ch4:108 (~30, keep), Ch6:64 (~40, keep), Ch7:86 (~45, cut), Ch8:68 (~50, cut), Ch9:92 (~20, keep), Ch10:30 (~30, keep), Ch12:14 (~20, cut), Ch15:22, 24, 60 (recap, keep). The hedge "a large population of (midbrain) dopamine neurons" recurs as a formula at Ch1:86, Ch4:108, Ch6:64, Ch7:86, and Ch8:68. Ch3:64 states it once with its justification, so callbacks can drop it.
3. **Two kinds of prediction error (value scalar vs sensory pattern).** Home: **Ch6:64** (~100). Others: Ch3:64 (~60, cut in A2), Ch12:72 (~75, cut), Ch12:156 (~35, cut).
4. **Eligibility trace and the three-factor rule.** Home: **Ch3:86-98** (~500). Others: Ch4:114 (~20, keep), Ch5:90-92 (~150, molecular form, complementary, keep), Ch7:150 (~35, keep), Ch11:90 (~60, trim), Ch11:146 (~35, keep), Ch15:38 (~70, recap with the Yagishita numbers, deliberate), Ch16:54-62 (~350, diagnostic, keep).
5. **"No global objective, only local errors."** Home: **Ch3:84** (~130). Others: Ch1:86 (~70, cut in A2), Ch3:134 (~50, trim), Ch6:110 (~60, cut).
6. **Hubel and Wiesel.** Home for monocular deprivation: **Ch1:62** (~200). Others: Ch6:54 (~45, home for the neocognitron link), Ch6:136 (~110, cut), Ch6:138 (~10, keep), Ch10:26 (~70, cut), Ch11:26 (~35, keep, needed for the argument), Ch15:22 and Ch15:44 (recap). Terminology clash: Ch6:136 says "critical period", while Ch1:62, Ch13:122, and Ch14:134 say "sensitive period". The A2 cut reconciles them.
7. **Hodgkin and Huxley.** Ch0:78 (~170, with Figure 0.7), **Ch1:40** (~170, home for the "membrane's physics" argument), Ch2:94-96 (~200, home for the mechanism), Ch13:46 (~40, data for Figure 13.3, keep), Ch15:22 (recap). Ch0 and Ch1 both tell the 1952 model in full. A2 trims Ch0 by one sentence. Further trimming of Ch0 is possible if Figure 0.7 stays.
8. **Hebb's rule; Bliss and Lømo.** Hebb home: **Ch5** (epigraph, 20, 34). Bliss and Lømo are named only in **Ch2:116** (~75); Ch5:54 gives the 1973 date without names. Others: Ch0:98 (~20), Ch10:22 (~15), Ch15:22 (recap, which cites "(Chapter 5)" for Bliss and Lømo; change to "(Chapters 2 and 5)").
9. **H.M.** Home: **Ch5:114 and Ch5:156**. Other: Ch9:34 (~40, callback, tightened). No further retellings.
10. **The brain's 20 watts and the energy budget.** Home: **Ch1:46** (~200). Others: Ch1:86, 102, 114 (keep), Ch2:24 (~35, cut in A2), Ch2:126 (~70, keep: the only place the 15 percent figure appears), Ch10:18, Ch10:106-112 (~250, home for the brain-vs-GPT energy comparison), Ch10:172, Ch13:24 (~10, keep). Related motif, "energy will become the binding constraint on AI", appears four times: Ch1:102, Ch4:170 (cut in A2), Ch10:112 (home), and Ch11:94.
11. **Phineas Gage.** Only Ch7:158. Not repeated.
12. **Pavlov.** Ch7:94 (fear conditioning) and Ch8:128 (the Pavlovian controller) are different uses. Not repeated.
13. **Predictive coding.** Home: **Ch6:58-76**. Others: Ch7:58 (~25, keep), Ch10:100 (~35, trim), Ch12:32 (new retinal origin, keep), Ch12:126 (evaluation, keep), Ch15:118 (recap).
14. **Thorpe's 150 ms animal detection.** Home: **Ch1:30** (~75). Others: Ch2:112 (~50, cut in A2), Ch6:54 (~25, keep).
15. **Allen and Stevens's synaptic failures.** Home: **Ch1:80**. Others: Ch2:58 (~30, keep), Ch13:30 (~25, cut).
16. **Sterling and Laughlin, near-optimal design.** Home: **Ch1:86** (~55). Other: Ch2:130 (~45, a near-verbatim repeat, cut in A2). Sterling's allostasis: home Ch7:32, callback Ch12:36 (fine).
17. **Golgi's stain blackening one cell in a hundred.** Home: **Ch1:92**. Others: Ch2:14 (~25, cut in A2), Ch4:86 (Nissl vs Golgi, keep).
18. **Doya's four neuromodulators as metaparameters.** Home: **Ch3:130** (~45). Others: Ch7:180 (~45; the only place giving the modulator-by-modulator mapping, keep), Ch11:68 (~55, cut).
19. **Yu and Dayan (acetylcholine for expected uncertainty, norepinephrine for unexpected).** Home: **Ch3:104**. Others: Ch6:102 (~40, keep), Ch12:80 (~45, cut), Ch13:136 (~40, keep; it carries footnote [^55]).
20. **Behrens's volatility experiment.** First told at **Ch8:110** (~50). Ch11:66 (~90) retells it with more detail, and Ch12:80 cites Ch11 for it. A1 tightens Ch11 and points it back to Ch8, and Ch12 cites both.
21. **Iowa gambling task; Fellows and Farah.** Home: **Ch7:162-170**. Others: Ch8:12 (~50, bridge, keep), Ch8:70 (~75, cut), Ch8:140 (~20, keep), Ch8:166 (~35, Central Lesson, keep).
22. **Devaluation (Adams and Dickinson) and the lever-pressing rat.** Home: **Ch8:118**. The rat is invoked again at Ch9:12, 32 (cut), 140, 158 (cut), and 168, and at Ch15:42.
23. **Goal-directed vs habitual striatum.** Home: **Ch8:122**. Other: Ch9:70 (~40, trim).
24. **Explore-exploit.** Home: **Ch8:106-110**. Other: Ch9:86 (~25, trim).
25. **The pianist and the wrong note.** Home: **Ch9:164**. Others: Ch10:144 (cut), Ch11:120 (cut).
26. **AlphaGo.** Home: **Ch8:160**. Ch9:156, Ch10:116, and Ch10:138 add new material (AlphaGo Zero, Lee Sedol), so keep them.
27. **Elastic weight consolidation.** Home: **Ch9:162**. Callbacks at Ch10:92, Ch11:36, and Ch16:46. Ch16:46 says "that Chapter 11 described"; better "Chapters 9 and 11".
28. **Experience replay (1992) as a convergence.** Home: **Ch5:168**. Callbacks at Ch1:106, Ch10:88, and Ch11:28 are fine.
29. **Mixture of experts.** Home: **Ch10:112**. Callbacks at Ch11:96, Ch13:152, and Ch15:136 are fine.
30. **Homeostatic reinforcement learning (Keramati and Gutkin).** Ch7:176 (~45) and **Ch11:104** (home, with Figure 11.7). Ch11 is tightened.
31. **Reward hacking.** Home: **Ch7:178**. Callbacks at Ch8:148 and Ch11:100 are fine.
32. **Cannon, Ashby, and homeostasis.** Ch1:68 (~70, preview) and **Ch7:20** (home). Ch12:120 and Ch15:20 are fine.
33. **Simon's satisficing; Gigerenzer.** Ch1:74 (~80) and **Ch8:132** (home, ~140). Gigerenzer and Brighton (Ch1) and Gigerenzer and Goldstein (Ch8) make the same "simple rules match complex models" claim. No cut proposed, because both sentences carry footnotes. If Ch1 is trimmed later, this is the place.
34. **Helmholtz's unconscious inference.** Ch1:70 (preview), **Ch6:18** (home), Ch15:20 (recap). Fine.
35. **"The brain generates behavior, and the world corrects it."** Stated at Ch1:68 and quoted again at Ch4:82 and Ch6:118 (optional cut in A2).
36. **"Fear is easily learned and rarely unlearned, only suppressed."** Ch5:154 and Ch7:112, verbatim. Ch7 credits Ch5, so this is acceptable.
37. **Place cells defined.** Ch4:138 (home), Ch5:122, and Ch12:56 each re-define them in a clause. Acceptable.
38. **Degeneracy.** Home: **Ch1:84**. Ch13:82 and Ch15:106 re-define it in a clause. Acceptable.
39. **"What not to copy" (slow, imprecise, cannot be reset).** Ch1:110 (~85, preview) and **Ch10:154** (home). No cut proposed.
40. **Bridge sentences duplicated across chapter boundaries.** Ch12:144 and Ch12:158 vs Ch13:14 (cut), Ch13:160 vs Ch14:20 (cut), Ch14:152 vs Ch15:16 (cut).

# B. Duplicated epigraphs and opening anecdotes

1. **Chapter 2 and Chapter 3 share the Cajal "butterflies of the soul" epigraph** (`Chapter2/...md:6`, `Chapter3/...md:6`). This is a true duplicate, and the two copies also differ:
   - Ch2: "brightly coloured butterflies ... may some day—who knows?—clarify"
   - Ch3: "brightly colored butterflies ... may some day (who knows?) clarify"

   Ch2:14 explicitly glosses the quotation ("the hope in the epigraph above"), so Chapter 2 should keep it. Chapter 3 needs a new epigraph; I am not proposing one, because quotations should not be supplied unverified. Whichever chapter keeps it should match the source translation (Craigie's 1937 English edition) in spelling and punctuation. The quotation keeps its original spelling, so "coloured" stays if that is what the translation prints.
2. **Chapter 15 epigraph = the frontispiece** (`Chapter15/...md:6`; `Frontispiece/How_the_Brain_Learns_Front_Matter.md:8`), Cajal's "sculptor of his own brain". This is deliberate, as stated. Ch15:144 and Ch16:118 ("Cajal's sculptor") call back to it, which is also deliberate. The frontispiece attribution has no source while Ch15 gives the full source; that is fine.
3. **No other duplicated epigraphs.** The other 14 epigraphs are distinct: Schrödinger, Dickinson, Sherrington, Hebb, Helmholtz, James, Pascal, Whitehead, Turing, Feynman, Craik, Dobzhansky, Plato, and Box.
4. **No duplicated opening anecdotes.** Several epigraphs or openings are deliberately picked up again later. These are callbacks, not repeats:
   - Ch5's Hebb epigraph is quoted at Ch5:20.
   - Ch0's Schrödinger is picked up at Ch0:30 and Ch0:76.
   - Ch7's James epigraph is picked up at Ch7:62, which retells James's bear argument from the same 1884 essay.
   - Ch8's Pascal is picked up at Ch8:20.
   - Ch9's Whitehead is extended at Ch9:16.
   - Ch11's Feynman is picked up at Ch11:144 and Ch16:14.
   - Ch12's Craik is both the epigraph and the opening anecdote (Ch12:12), then recapped at Ch15:20.
   - Ch14's Plato *Phaedrus* epigraph is followed by a retelling of the Theuth story with a second quotation at Ch14:94.
   - Ch15's opening (the Jonas and Kording microprocessor) is reprised at Ch15:144 and Ch16:118.
   - Ch14's opening (Kuhl's infants) is picked up at Ch15:50, Ch16:64, and Ch14:156.

   The only near-overlap of openings is Helmholtz. Ch1:70 introduces unconscious inference in about 50 words, and Ch6 then opens on it (epigraph plus Ch6:18). This is acceptable as preview and home.

**B count: 1 problem duplicate (Ch2/Ch3, with inconsistent renderings), 1 deliberate duplicate (Ch15 = frontispiece), 0 duplicated opening anecdotes.**

# C. Mechanical house-style violations

Search method: all 17 bodies scanned by script for the following, with each hit reviewed by hand.

- "—", "–", and "---".
- British spellings: -our, -ise/-yse, -re, programme, grey, travell-/modell-/labell-, whilst, amongst, learnt, judgement, ageing, defence, and similar.
- Numerals 1 to 10 standing alone in prose. Hits were excluded when they were measurements with units, chapter, figure, or layer numbers, dates, ranges, equations, or model names.
- Stale or time-anchored phrasing.

**Violations to fix (6):**

1. `Chapter7/...md:106`: "while only 3 of 12 healthy volunteers did." Change to "while only three of 12 healthy volunteers did."
2. `Chapter11/...md:50`: "gave a model a database of 2 trillion tokens". Change to "two trillion tokens". House usage elsewhere is "two million", "three billion", "one to seven billion".
3. `Chapter16/...md:28`: "for roughly 2 million in all". Change to "for roughly two million in all", matching Ch16:16 ("about two million"), the Figure 16.1 caption, and Ch16:60.
4. `Chapter12/...md:14`: "The previous eleven chapters met prediction everywhere." This is a stale count: Chapters 0 to 11 make twelve. The A1 cut replaces it with "The previous chapters".
5. `Chapter14/...md:152`: "The book has now described ... What remains is to put these pieces together ... the task of Chapter 15." This is last-chapter phrasing, but Chapter 16 follows. The A1 cut fixes it.
6. `Chapter10/...md:172`: "Seventy-six years later the machines learn". This is anchored to 2026 (Turing, 1950) and will read as stale in a later printing. Change to "Three-quarters of a century later".

**Content slip found while scanning (fixed by an A1 cut):** `Chapter9/...md:18` says "practice does three things" and then lists four.

**Inside quotations (no change required, listed for the editor):**

- `Chapter2/...md:6` has em dashes ("some day—who knows?—") and "coloured" inside the Cajal quotation, and `Chapter3/...md:6` renders the same quotation differently. Reconcile both copies against the source (see B1).
- `Chapter10/...md:6`: "programme" in the Turing quotation. Original spelling, keep.
- `Chapter15/...md:94`: "millimetre" in the Crick quotation. Original spelling, keep.

**Convention note (not counted):** every chapter's epigraph attribution line (line 8 in Chapters 0 to 16, and Frontispiece line 10) is written "> --- Name", which Pandoc renders as an em dash. This is uniform and outside body prose. If the no-em-dash rule is meant to cover epigraph attributions too, change all 18 at once.

**Clean:**

- No British spellings outside quotations.
- No em dashes or "---" in body prose.
- No other numerals one to ten in prose.

**C count: 6 violations to fix (plus 1 content slip handled in A), 3 in-quotation items for reconciliation, 1 convention note.**

# D. Cross-reference accuracy issues noticed during the audit

Several of these are fixed by the A cuts as noted.

- `Chapter10/...md:88`: credits McCloskey and Cohen to "Chapter 5", but they are named only in Ch1:56 (fixed by A1).
- `Chapter14/...md:40`: says Ch5's three things that slow forgetting are "retrieval, spacing, and sleep". Ch5:140 gives retrieval (helped by spacing), sleep, and emotional significance (fixed by A1).
- `Chapter14/...md:144`: says "Kestin's tutor ... did the opposite" of Bastani's chatbot, but Kestin measured learning immediately after two lessons, not practice vs exam (fixed by A1).
- `Chapter12/...md:80`: cites Chapter 11 for Behrens, but Behrens is first told in Ch8:110 (fixed by A1).
- `Chapter15/...md:22`: "(Chapter 5)" for Bliss and Lømo should read "(Chapters 2 and 5)".
- `Chapter16/...md:46`: "elastic weight consolidation that Chapter 11 described" should read "that Chapters 9 and 11 described".
- `Chapter6/...md:136`: "critical period" vs "sensitive period" elsewhere (fixed by A2).
