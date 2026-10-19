# Terminology consistency audit: How the Brain Learns

Scope: chapter bodies Ch0 to Ch16 (text above "# References and Attribution"), companions Ch1 to Ch16, and the front-matter glossary.
Line numbers are file line numbers as printed by `body.py N`. "chN:L" = `docs/book/Word/ChapterN/*.md` line L; "coN:L" = `docs/companion/ChapterN/Word/*.md` line L; "FM:L" = `docs/book/Word/Frontispiece/How_the_Brain_Learns_Front_Matter.md` line L.
All replacement text uses American spelling and no em dashes.

Severity: **A** = a reader would get a contradictory definition; **B** = same thing named two ways, or a wrong cross-reference that sends the reader to the wrong chapter; **C** = used before it is defined, or a small wording drift.

Total: 24 issues (A: 5, B: 11, C: 8).

---

## A. Conflicting definitions

### A1. Three-factor rule: does the third factor gate the change, or only whether it is kept? (most serious)

- ch3:94: "A synapse changes only when three things coincide within the lifetime of the trace: the presynaptic neuron was active, the postsynaptic neuron fired, and a neuromodulatory signal arrived."
- ch3:90: "If a neuromodulatory signal arrives while that state persists, the synapse changes; if not, the state fades and nothing lasting happens." (this one is fine: it says "lasting")
- ch3:32 (same chapter): "Synaptic plasticity ... can be induced by presynaptic and postsynaptic activity alone ... What neuromodulators do is gate and scale much of that plasticity ... and decide whether it is consolidated."
- ch5:90: "Chapter 3 described the three-factor learning rule: a synapse changes when it was recently active, when its neuron fired, and when a neuromodulatory signal arrives ... the first two alone can induce potentiation and depression. What the third factor decides is whether, how strongly, and for how long the change is kept"
- ch15:38 and ch16:54: "whether the change is kept depends on a third factor" / "a broadcast signal ... decides whether the change is kept."

Conflict: ch3:94 says no change at all without the third factor; ch3:32, ch5:90, ch15:38 and ch16:54 say activity alone induces change and the third factor decides whether it lasts (and its size and sign). ch5:90 even restates the ch3:94 version in its first sentence and contradicts it in its second.

Canonical: the ch3:32 / ch15:38 version (activity induces; the third factor decides whether, how strongly, and in which direction the change is kept).

Replacements:
- ch3:94: "A synapse changes only when three things coincide within the lifetime of the trace:" -> "A change that lasts requires three things to coincide within the lifetime of the trace:"
- ch5:90: "Chapter 3 described the three-factor learning rule: a synapse changes when it was recently active, when its neuron fired, and when a neuromodulatory signal arrives saying that something significant happened." -> "Chapter 3 described the three-factor learning rule: a synapse changes lastingly when it was recently active, when its neuron fired, and when a neuromodulatory signal arrives saying that something significant happened."
- co5:60: same edit ("a synapse changes" -> "a synapse changes lastingly"). co3:87 to co3:91 already carries the caveat and needs no change.

### A2. Eligibility trace equated with synaptic tagging, at a hundredfold different timescale

- ch3:90: "Eligibility traces in the brain, then, last seconds to minutes"; ch3:94: "decays with a time constant of seconds"; ch16:54: "the change is held for a second or so in an eligibility trace".
- ch3:98: "synaptic tagging and capture, the molecular form of the trace, in which a tag set at a synapse lets it collect proteins ... up to an hour or two later."
- ch5:92: "Early LTP sets a tag at the synapse, a transient biochemical mark lasting an hour or two ... This is synaptic tagging and capture, and it is the eligibility trace of Chapter 3 seen at the level of molecules."
- co3:91 "Chapter 5 describes its molecular form, synaptic tagging and capture."; co5:62 "This is synaptic tagging and capture: Chapter 3's eligibility trace at the level of molecules."

Conflict: the book defines the eligibility trace as lasting seconds to minutes (Yagishita 0.3 to 2 s; Brzosko about 1 min), then twice calls the one-to-two-hour synaptic tag "the" trace. A reader cannot hold both. The tag is a slower relative of the trace, not its molecular identity.

Canonical: eligibility trace = seconds to minutes (Ch3); synaptic tag = an analogous mark lasting one to two hours (Ch5).

Replacements:
- ch3:98: "synaptic tagging and capture, the molecular form of the trace, in which" -> "synaptic tagging and capture, a slower relative of the trace, in which"
- ch5:92: "This is synaptic tagging and capture, and it is the eligibility trace of Chapter 3 seen at the level of molecules." -> "This is synaptic tagging and capture, a slower, molecular relative of Chapter 3's eligibility trace that works over hours rather than seconds."
- co3:91: "Chapter 5 describes its molecular form, synaptic tagging and capture." -> "Chapter 5 describes a slower relative, synaptic tagging and capture, which works over hours."
- co5:62: "Chapter 3's eligibility trace at the level of molecules." -> "a slower, hour-scale relative of Chapter 3's eligibility trace."
- ch16:54: "the change is held for a second or so in an eligibility trace" -> "the change is held for seconds to minutes in an eligibility trace"

### A3. Glossary "Learning" and "Memory" disagree with Chapters 1 and 5

- FM:141 Learning: "A lasting physical change in neural structure or function that alters future behavior as a result of experience."
- FM:145 Memory: "The capacity of a system to behave differently because of past experience."
- ch1:68: "learning is the process by which the controller changes its own organization"; ch1:70: "Learning is the mechanism by which the control system adapts. Memory is the persistence of those adaptations."
- ch5:14: "Memory is not something the brain has. It is something the brain's tissue has become."; ch15:40: "Memory is not one system but several".

Conflict: the glossary makes learning the product (the physical change) and memory a capacity; Ch1 makes learning the process and memory the persistence of its products; Ch5 makes memory the altered tissue itself, which is what the glossary calls learning.

Canonical: Ch1 (learning = process; memory = what persists), with Ch5's physical framing.

Replacements:
- FM:141: "A lasting physical change in neural structure or function that alters future behavior as a result of experience." -> "The process by which experience produces lasting physical changes in neural structure or function that alter future behavior."
- FM:145: "The capacity of a system to behave differently because of past experience." -> "The persistence of the changes that learning makes, and the capacity they give a system to behave differently because of past experience. In the brain it is held in altered tissue, not as stored records, and it is divided among several systems."

### A4. Who sets the learning rate: acetylcholine (Ch3, Ch7) or norepinephrine (Ch12, Ch13, Ch15)?

- ch3:130: Doya's four quantities "the error signal, the learning rate, the exploration rate, and the discount" (mapping not given).
- ch7:180: "Kenji Doya proposed that the neuromodulators of Chapter 3 set exactly these metaparameters, with dopamine carrying the prediction error, serotonin the time horizon, norepinephrine the balance between exploring and exploiting, and acetylcholine the learning rate."
- ch12:80: Yu and Dayan: "acetylcholine report the expected uncertainty ... and norepinephrine the unexpected uncertainty"; ch13:136: "Norepinephrine raises the learning rate when the world has changed, as Chapter 12 described"; ch15:58: "Norepinephrine rises with the surprise ... raising the learning rate".

Conflict: Ch7 assigns the learning rate to acetylcholine with no caveat; Ch13 and Ch15 state as fact that norepinephrine raises it. The two theories are reconcilable, but the book never says so.

Canonical: the later synthesis (norepinephrine signals that the world has changed and raises the learning rate; acetylcholine signals known noise and shifts weight toward incoming evidence), with Doya presented as an earlier proposal.

Replacement (ch7:180, after the Doya sentence ending "...and acetylcholine the learning rate.[^104]"): insert "Later work, described in Chapter 12, divides the learning rate between them: norepinephrine raises it when the world has changed, and acetylcholine weights incoming evidence when the world is noisy but stable."

### A5. "Attention" defined as precision (Ch6) versus as a capacity budget (Ch14), and the companion hardens the Ch6 version

- ch6:98: "The proposal that follows from predictive coding is that this is what attention is: the gain applied to prediction errors" (hedged as a proposal).
- co6:113: "Attention is precision: gain on errors, implemented by biased competition, gamma synchrony, and acetylcholine." (unhedged); co6:15 lists "treating attention as a spotlight that selects" as a misconception.
- ch14:74: "Attention is the means by which that capacity is allotted"; ch14:72 heading "Attention Is a Budget"; ch15:58 "The limited budget of attention described in Chapter 14".

Conflict: the companion calls the selection-and-capacity view a misconception, and Ch14 then teaches it. The two views are compatible (gain on evidence; a limited capacity to apply it), but nothing links them.

Canonical: attention = the weighting of signals by their expected reliability or relevance, drawing on a limited capacity.

Replacements:
- co6:113: "- Attention is precision: gain on errors" -> "- On the predictive coding proposal, attention is precision: gain on errors"
- co6:15: "3) treating attention as a spotlight that selects, rather than a gain that weights evidence by its reliability." -> "3) treating attention only as a spotlight that selects, rather than also as a gain that weights evidence by its reliability."
- ch14:74: "Attention is the means by which that capacity is allotted," -> "Attention, which Chapter 6 described as the weighting of evidence by its reliability, is also the means by which that capacity is allotted,"

---

## B. One thing named two ways, or a cross-reference that points to the wrong chapter

### B1. Sensitive period (Ch1) versus critical period (Ch6), for the same kitten experiment

- ch1:62: "Experience during a sensitive period, a window of early life in which a circuit is unusually open to being shaped" (Wiesel and Hubel kittens); ch13:122 and ch14:134: "the sensitive periods of Chapter 1"; co1:65, co13:254, co15:26 ("Hubel and Wiesel's sensitive period").
- ch6:136: "The period during which experience can reorganize the visual cortex is called the critical period" (same experiment, introduced as if new); ch12:102 "critical periods"; co6:88, co6:116, co12:60.

Canonical: keep both terms but relate them. "Sensitive period" is the general term; "critical period" is the strict, closing form.

Replacement, ch6:136: "is called the critical period, and it closes," -> "is called the critical period, the strict form of the sensitive periods that Chapter 1 introduced, and it closes,"

### B2. Norepinephrine versus noradrenaline; epinephrine versus adrenaline

- ch2:134: "substances such as dopamine, acetylcholine, and noradrenaline"; co2:117 same. Everywhere else (Ch3 onward, about 25 uses) the book says "norepinephrine".
- ch7:70, 118, 120, 140, 146 (x2): "adrenaline"; co7:51 notes "Adrenaline, which American physiologists call epinephrine"; co7:54, 88, 97, 98, 286, 322.

Canonical (American usage, matching "norepinephrine"): norepinephrine and epinephrine.

Replacements:
- ch2:134 and co2:117: "noradrenaline" -> "norepinephrine"
- ch7:70 first use: "injected volunteers with adrenaline," -> "injected volunteers with epinephrine (adrenaline),"; later ch7 uses: "adrenaline" -> "epinephrine". co7:51: "(Adrenaline, which American physiologists call epinephrine, is a close relative of Chapter 3's norepinephrine.)" -> "(Epinephrine, also called adrenaline, is a close relative of Chapter 3's norepinephrine.)"; other co7 uses "adrenaline" -> "epinephrine".
- If the author prefers to keep "adrenaline" for the hormone as more familiar, the minimum is the ch2/co2 fix plus an "(epinephrine)" gloss at ch7:70.

### B3. "Reward prediction error" versus "dopamine prediction error" / "dopamine error"

- Canonical in ch3:54, ch3:56, ch4:108, ch7:86, ch9:92, co3, co6:44, co8:52: "reward prediction error".
- Variants: ch8:124 "through the dopamine prediction error of Chapter 3"; ch6:110 "the dopamine error of that chapter"; co6:77 "the dopamine error of Chapter 3"; co13:254 and co15:68 "dopamine prediction errors".

Replacements: ch8:124 "the dopamine prediction error of Chapter 3" -> "the reward prediction error of Chapter 3"; ch6:110 "the dopamine error of that chapter" -> "the reward prediction error of that chapter"; co6:77 "the dopamine error of Chapter 3" -> "the reward prediction error of Chapter 3"; co13:254 and co15:68 "dopamine prediction errors" -> "reward prediction errors".

### B4. "Predictive processing" used once, undefined, as though it were a synonym of predictive coding

- ch12:126: "found much of it compatible with predictive processing but rarely decisive against alternatives." This is the only use in any chapter body. The same paragraph and Ch6 use "predictive coding"; co12:66 uses "predictive processing philosophy (Clark 2013; Hohwy 2013)" for something broader.

Replacement, ch12:126: "compatible with predictive processing but" -> "compatible with predictive coding and its relatives, often grouped as predictive processing, but"

### B5. Two meanings of "free energy" (Ch0 thermodynamic, Ch12 variational)

- ch0:30 to ch0:34: free energy = "the portion of energy that is available to do work" (thermodynamic).
- ch12:116: "minimizing variational free energy, a quantity it can compute from its sensations and its own model"; ch15:132: "the minimization of free energy"; ch1:72: "Karl Friston's free-energy principle".

Conflict: a reader who learned "free energy" in Ch0 will take Ch12 to mean the same quantity. The Ch12 quantity is informational.

Replacement, ch12:116: "minimizing variational free energy, a quantity it can compute from its sensations and its own model and one that sets an upper bound on surprise," -> "minimizing variational free energy, an information-theoretic quantity distinct from the thermodynamic free energy of Chapter 0, which it can compute from its sensations and its own model and which sets an upper bound on surprise,"

### B6. Homeostatic plasticity (Ch1) versus synaptic scaling (Ch5), never linked, with different timescales

- ch1:82: "neurons monitor their own average activity over hours and days and scale their synapses ... a mechanism Gina Turrigiano and Sacha Nelson called homeostatic plasticity"; co1:94.
- ch5:84: "This synaptic scaling is slow, taking a day or two"; ch12:102 "over a day or two"; co5:55 "if firing stays too high for hours". Ch5 never uses "homeostatic plasticity".

Canonical: homeostatic plasticity = the family (synaptic scaling, the sliding threshold, homeostatic inhibitory plasticity); synaptic scaling = the multiplicative member, acting over a day or two.

Replacement, ch5:84: "This synaptic scaling is slow, taking a day or two," -> "This synaptic scaling, the form of homeostatic plasticity that Chapter 1 introduced, is slow, taking a day or two,"; ch1:82: "over hours and days" -> "over a day or more" (optional, for timescale agreement).

### B7. Complementary learning systems: named in Ch1 and Ch10, but in Ch5 only in a figure caption

- ch10:88: "on the complementary learning systems theory of Chapter 5"; ch11:146; co1:59, co5:243.
- ch5:116 (the defining paragraph): "The theory that explains why the brain would bother with two systems was set out in 1995 by McClelland, McNaughton, and O'Reilly" with no name. The name appears only in the ch5:112 caption.

Replacement, ch5:116: "The theory that explains why the brain would bother with two systems was set out in 1995" -> "The theory that explains why the brain would bother with two systems, called complementary learning systems, was set out in 1995"

### B8. Elastic weight consolidation attributed to Chapter 11 instead of Chapter 9

- Introduced at ch9:162. ch10:92 and ch11:36 both say "Chapter 9 described elastic weight consolidation".
- ch16:46: "a method called elastic weight consolidation that Chapter 11 described".

Replacement, ch16:46: "that Chapter 11 described" -> "that Chapters 9 and 11 described"

### B9. Yu and Dayan's uncertainty account attributed to Chapter 3

- ch12:80: "the neuromodulatory account of Chapter 3, Angela Yu and Peter Dayan's". The account is not in the Ch3 body. It is introduced at ch6:102 ("One influential account assigns acetylcholine to expected uncertainty ...") and appears in the Ch3 companion only (co3:104, co3:117).

Replacement, ch12:80: "the neuromodulatory account of Chapter 3, Angela Yu and Peter Dayan's," -> "the neuromodulatory account of Chapter 6, Angela Yu and Peter Dayan's,". Optionally also add Yu and Dayan to the ch3:104 to ch3:108 section, so that co3:104 has a chapter source (see D1).

### B10. "Circuits of choice" cited to Chapters 6, 9, and 12, leaving out Chapter 8

- ch15:58: "Each failure is a prediction error, in sensory cortex, in the cerebellum, and in the circuits of choice (Chapters 6, 9, and 12)." Choice and its prediction errors are Chapter 8 (with Chapter 3).

Replacement: "(Chapters 6, 9, and 12)" -> "(Chapters 6, 8, 9, and 12)"

### B11. Helmholtz's inference credited only to Chapter 12

- ch15:24: "Helmholtz's inference became the predictions of Chapter 12". Helmholtz's unconscious inference is the organizing idea of Chapter 6 (ch6:60 "a direct implementation of Helmholtz's idea"), and Chapter 1 introduces it (ch1:70).

Replacement: "became the predictions of Chapter 12" -> "became the inference of Chapter 6 and the predictions of Chapter 12"

---

## C. Used before it is defined, or small drift

### C1. Early LTP: "lasting an hour or two" versus "takes minutes"

- ch5:62: "Early LTP, lasting an hour or two, uses proteins already present"; ch5:92 "a transient biochemical mark lasting an hour or two"; co5:45.
- ch5:160: "Early LTP takes minutes; late LTP takes hours and new protein"; co5:103 "Minutes for early LTP".
- ch15:60: "the early phase of long-term potentiation holds those changes for the next few hours".

Replacements: ch5:160 "Early LTP takes minutes;" -> "Early LTP forms in minutes and lasts an hour or two;"; co5:103 "Minutes for early LTP," -> "Minutes to form early LTP, which lasts an hour or two;"; ch15:60 "for the next few hours" -> "for the next hour or two".

### C2. "Precision" has an everyday sense (Ch1, Ch13) and a technical sense (Ch6) that the chapter never states

- Everyday sense (exactness): ch1:32, ch1:72 "When precision conflicts with speed ... precision often loses", ch13:164.
- Technical sense: ch6:34 "leans toward whichever of the two is more precise", ch6:36 "set by relative precision", ch6:96 heading "Attention as Precision". The formal definition is only in the companion (co6:144 "Precision is 1/s².").

Replacement, ch6:36: "The optimal weighting is set by relative precision," -> "The optimal weighting is set by relative precision, the inverse of a distribution's spread (the narrower the curve, the more precise),"

### C3. Representation: the glossary is narrower than the book's usage

- FM:161: "An explanatory description summarizing regularities in neural activity, not a physical stored object."
- Usage: ch5:116 "distributed representations" (of a network); ch10:16 "match in representation, organizing information inside it as the brain does"; ch11:34 "a reactivation of the patterns that represented the experience"; ch11:50 the hippocampus "stores a pointer to the cortical patterns that represented it"; ch12:60 "successor representation".

The book uses "representation" for the pattern of activity or connection strength that carries information about something. The glossary's anti-reification point is fine, but its wording excludes this usage.

Replacement, FM:161: -> "A pattern of neural activity or connection strength that varies systematically with something in the world, the body, or the brain's own state, so that it can be described as standing for it. In this book the word describes what activity carries, not a stored copy that is looked up."

### C4. Plasticity defined three ways

- FM:153: "Biological mechanisms that enable learning by changing synaptic strength, excitability, or structure."
- ch1:48: "plasticity, the capacity of neurons and synapses to change their structure and strength with use".
- ch3:32: "Synaptic plasticity, the lasting change in the strength of a connection".

These are mechanism, capacity, and the change itself. They are compatible, but a glossary should pick one. Canonical: the capacity (Ch1), with the mechanisms as how it is realized.

Replacements: FM:153 -> "The capacity of neurons and synapses to change their strength, excitability, or structure with use, and the mechanisms that make those changes."; ch3:32 "Synaptic plasticity, the lasting change in the strength of a connection," -> "Synaptic plasticity, the capacity of a connection to change its strength lastingly,"

### C5. Neuromodulators "do not carry information" versus a quantitative reward prediction error

- ch3:16: "a small number of cell groups whose job is not to carry information but to change how everything else handles it."
- ch3:56: the reward prediction error is "quantitative rather than merely present or absent"; ch3:28 and co3:25 put it more carefully: "does not carry detailed sensory content".

Replacement, ch3:16: "whose job is not to carry information but to change" -> "whose job is not to carry detailed content but to change"

### C6. Two kinds of "levels": the front matter's levels of organization versus Marr's levels of analysis

- FM:85 to FM:99 "A Note on Levels of Explanation": molecular, cellular, circuit, and behavioral levels (scale of organization).
- ch1:34: "David Marr's distinction between what a system computes, the procedure it uses, and the hardware ... is the standard way of keeping those levels apart"; ch10:16 refers back to it.

The two are different axes, both called "levels".

Replacement, ch1:34: "is the standard way of keeping those levels apart," -> "is the standard way of keeping those levels of analysis apart (a different axis from the levels of biological organization in the front matter),"

### C7. Terms used before their defining chapter without a gloss

- ch3:36 "project to the striatum and the prefrontal cortex": "striatum" is first explained at ch4:104 ("the striatum, the input stage"). Replacement: "project to the striatum" -> "project to the striatum, the input stage of the basal ganglia described in Chapter 4,"
- ch3:108 "Low acetylcholine, as during slow-wave sleep": defined at ch5:120. Replacement: "as during slow-wave sleep," -> "as during slow-wave sleep, the deep stage of sleep that Chapter 5 describes,"
- ch4:42 "the basis of working memory and of pattern completion": working memory is defined at ch5:154; pattern completion at ch4:122 later in the same chapter. Replacement: "which is the basis of working memory and of pattern completion" -> "which is the basis of working memory, the holding of information in mind for seconds, and of pattern completion, described below"
- ch1:86 "minimizes by gradient descent": defined only implicitly at ch3:72. Replacement: "minimizes by gradient descent," -> "minimizes by gradient descent (adjusting every weight a small step in the direction that most reduces the error),"
- ch3:32 "decide whether it is consolidated": consolidation is defined at ch5:110. Acceptable as is, because ch3:108 points to Ch5. No change required.

### C8. Companion statements with no source in their chapter (definition drift)

- co3:104: "In Yu and Dayan's account, norepinephrine reports unexpected uncertainty ... and acetylcholine reports expected uncertainty". Not in the Ch3 body (see B9). Either add a sentence to ch3:104 to ch3:108, or change co3:104 to "In Yu and Dayan's account (Chapter 6), ...".
- co6:246: "The forward model is learned by the cerebellum (Chapter 4)." Ch4 never uses "forward model" (first used at ch6:142, "the cerebellar forward model"). Replacement: "(Chapter 4)" -> "(Chapters 4 and 6)".
- co15:26: "Hubel and Wiesel's sensitive period". Fine after B1; leave as is.

---

## Related non-terminology inconsistencies noticed (for the fact-check pass)

- Synapse counts: ch1:28 "on the order of a hundred trillion synapses" (whole brain); ch4:16 "in the neocortex alone, roughly 150 trillion"; ch13:118 "the human neocortex alone holds about 164 trillion". The whole-brain figure is smaller than either neocortex figure. Suggest ch1:28 "on the order of a hundred trillion" -> "well over a hundred trillion", and choosing one neocortical figure (ch4:16 and ch13:118).
- British word: ch15:58 "a lorry behind" -> "a truck behind" (American usage rule).
- Front matter uses "---" (em dash) at FM:87 and FM:91.

---

## Canonical definitions (seed for the glossary)

Each entry follows the book's dominant usage, with the chapter where the term is introduced.

1. **Action potential (spike, impulse)** (Ch2; previewed Ch0): A brief, all-or-none electrical pulse that starts near the beginning of the axon when the membrane voltage crosses threshold, and travels along the axon to the neuron's synapses. Its timing and pattern carry the signal; its size does not.
2. **Synapse** (Ch1, Ch2): The junction at which one neuron influences another, usually by releasing neurotransmitter across a gap about 20 nanometers wide.
3. **Neurotransmitter** (Ch2): A chemical released from a presynaptic terminal that acts on receptors of a target cell. Fast transmitters such as glutamate and GABA act point to point within milliseconds.
4. **Neuromodulator** (Ch2, Ch3): A chemical (chiefly dopamine, norepinephrine, serotonin, or acetylcholine), released widely by small groups of neurons, often by volume transmission. It does not carry detailed content; it changes how circuits respond and whether, how strongly, and in which direction their synapses change.
5. **Volume transmission** (Ch3): Release of a signaling molecule into the extracellular space, where it diffuses to receptors on many cells at once, in contrast to point-to-point synaptic transmission.
6. **Plasticity** (Ch1, Ch2): The capacity of neurons and synapses to change their strength, excitability, or structure with use, and the mechanisms that make those changes.
7. **Long-term potentiation and depression (LTP, LTD)** (Ch2, Ch5): Activity-induced lasting increases (LTP) or decreases (LTD) in synaptic strength. Early LTP forms in minutes and lasts an hour or two using existing proteins; late LTP requires new protein synthesis.
8. **Hebbian plasticity** (Ch2, Ch5): Change in a synapse driven by coordinated activity on its two sides ("cells that fire together wire together"). It can be induced by activity alone.
9. **Spike-timing-dependent plasticity (STDP)** (Ch5): A Hebbian rule in which a presynaptic spike a few to a few tens of milliseconds before the postsynaptic spike strengthens the synapse, and the reverse order weakens it.
10. **Eligibility trace** (Ch3): A transient, decaying mark left at a recently active synapse, lasting seconds to minutes, during which a neuromodulatory signal can turn the activity into a lasting change.
11. **Three-factor learning rule** (Ch3; developed Ch5): The book's central learning rule. Activity on the two sides of a synapse (factors one and two) induces a change and sets an eligibility trace, and a broadcast neuromodulatory signal (the third factor) decides whether, how strongly, and in which direction the change is kept.
12. **Synaptic tagging and capture** (Ch5): A molecular mechanism in which early LTP sets a tag lasting an hour or two, and the tagged synapse captures newly made proteins that make the change lasting. It is a slower relative of the eligibility trace.
13. **Reward prediction error** (Ch3): The difference between the reward received (plus the value now expected) and the reward that was predicted. It is carried as a scalar by a large population of midbrain dopamine neurons and corresponds to the temporal-difference error.
14. **Temporal-difference learning** (Ch3): Sutton's algorithm for learning to predict future reward from the difference between successive predictions. Its error term matches the firing of dopamine neurons.
15. **Credit assignment** (Ch3): The problem of deciding which synapses or actions were responsible for an outcome, especially when the outcome is delayed.
16. **Sensory prediction error** (Ch6): The high-dimensional difference between what a level of the sensory hierarchy receives and what the level above predicted. It concerns content, not value, and must not be confused with the reward prediction error.
17. **Prior, likelihood, posterior** (Ch6): In Bayesian inference, the prior is what is expected before the evidence, the likelihood is how probable the evidence is under each possible state, and the posterior (proportional to their product) is the estimate to act on.
18. **Precision** (Ch6): The reliability of a signal or belief, formally the inverse of its variance. Evidence and priors are weighted by their relative precision.
19. **Predictive coding** (Ch6; retinal origin Ch12): The proposal that each level of the cortical hierarchy sends predictions downward and passes upward only the prediction error. It is one specific process theory of how the brain predicts, and the evidence for it is mixed.
20. **Attention** (Ch6, Ch14): The weighting of signals by their expected reliability or relevance (on the predictive coding account, the gain on prediction errors), drawing on a limited capacity that must be allotted.
21. **Homeostasis** (Ch1, Ch7): The maintenance of the body's essential internal variables near set points by negative feedback that detects deviations and reverses them.
22. **Allostasis** (Ch7): Predictive regulation, "stability through change": anticipating what the body will need and adjusting in advance instead of waiting for an error. Some treat it as homeostasis with good forecasting.
23. **Interoception** (Ch7): The sensing of the body's internal condition (heartbeat, breathing, visceral stretch, temperature, blood chemistry, inflammation, pain). Like other perception, it is an inference.
24. **Emotion** (Ch7): At its core, the brain's running estimate of the state of the body and of what the current situation means for it. It is felt as valence and arousal, and named as fear, anger, or relief.
25. **Homeostatic plasticity / synaptic scaling** (Ch1 / Ch5): Mechanisms by which a neuron keeps its average activity within a working range. Synaptic scaling multiplies all of a neuron's excitatory synapses by a common factor over a day or two, preserving their relative strengths.
26. **Stability-plasticity dilemma** (Ch3, Ch5): The fact that a system cannot both change quickly and retain what it knows.
27. **Catastrophic interference** (Ch1, Ch5): The overwriting of old knowledge when a single distributed network learns new material fast or in sequence.
28. **Complementary learning systems** (Ch1, Ch5): McClelland, McNaughton, and O'Reilly's theory that the brain avoids catastrophic interference with a fast, sparse hippocampal learner and a slow cortical learner, joined by interleaved replay.
29. **Consolidation (synaptic and systems)** (Ch5): Synaptic consolidation is the hour-scale stabilization of changed synapses (early to late LTP). Systems consolidation is the transfer over weeks to years of a memory from dependence on the hippocampus toward cortex. Reconsolidation is the restabilization required after a memory is reactivated.
30. **Replay** (Ch1, Ch5): The reactivation, during sleep and quiet rest, of activity sequences from recent experience, often compressed in time during sharp-wave ripples. It is generated by the network, not played from a recording.
31. **Engram** (Ch5): The physical trace of a particular memory: a sparse ensemble of neurons whose mutual connections were strengthened during learning, so that a partial cue recalls the whole (pattern completion).
32. **Sensitive period / critical period** (Ch1 / Ch6): A window, usually early in life, during which a circuit is unusually open to being shaped by experience. A critical period is the strict form, which closes and cannot be reopened under normal conditions.
33. **Goal-directed action and habit** (Ch8, Ch9): Goal-directed actions are chosen from their expected outcomes and adjust at once when an outcome is devalued (dorsomedial striatum and prefrontal cortex). Habits are triggered by context and persist after devaluation (dorsolateral striatum). They are often modeled as model-based and model-free control.
34. **Learning rate** (Ch12; previewed Ch3, Ch8): The fraction of a prediction error by which an estimate is revised. In the brain it rises with uncertainty and change, a rise linked to norepinephrine.
35. **Free-energy principle** (Ch1, Ch12): Friston's proposal that any self-maintaining system can be described as minimizing variational free energy, an information-theoretic bound on surprise, by perceiving, learning, or acting (active inference). It is a modeling framework, not a testable hypothesis, and its quantity is not the thermodynamic free energy of Ch0.
36. **Learning** (Ch1, Ch2): The process by which experience produces lasting physical changes in neural structure or function that alter future behavior.
37. **Memory** (Ch1, Ch5): The persistence of the changes that learning makes, and the capacity they give the system to behave differently because of past experience. It is held in altered tissue, not stored records, and is divided among several systems working on different clocks.
38. **Representation** (Ch1, Ch10): A pattern of neural activity or connection strength that varies systematically with something, so that it can be described as standing for it. It is a description of what activity carries, not a stored copy.
