---
title: "Chapter 1 Student Notes and Labs"
subtitle: "What the Brain Is (and Is Not)"
---

# Student Notes

## What this chapter is for

Chapter 1 contains almost no neurobiology on purpose. Its job is to change the frame through which you will read everything that follows. If you arrive from software, engineering, physics, or machine learning, you carry a set of instincts about what an information-processing system should look like: discrete symbols, separated memory and computation, central control, a clock, noise as an enemy, and correctness as the goal. Those instincts are productive in your own field and misleading here.

The chapter's claim is not that the computational vocabulary is wrong. It is that the vocabulary smuggles in assumptions about precision, modularity, and design that biological tissue does not satisfy. Treated as a poorly documented program, the brain looks badly engineered. Treated as an evolved physical control system whose objective is viability rather than truth, it starts to make sense.

Your goal is to be able to state, in plain language, what the brain was actually selected to do, why that goal makes apparent defects reasonable, and which of your own assumptions you will need to suspend before meeting your first neuron in Chapter 2.

## Why introspection fails as a guide

We experience the brain from the inside, continuously. That intimacy produces confidence without understanding: we feel we know what memory or perception is because we have memories and perceptions. The chapter's point is that experience and mechanism are different levels. The brain does not expose its implementation by being used. Keep this in mind whenever an explanation "feels obviously right"; that feeling is a product of the system under study, not evidence about it.

The chapter's example is Nisbett and Wilson's stocking experiment: shoppers choosing among four identical pairs preferred the rightmost by about four to one and explained the choice by knit and sheerness, never by position. Fluent reasons are not access to causes.

## The brain is not a digital computer

The chapter lists the defining properties of a designed computer and then denies each of them for the brain. You should be able to reproduce both columns:

- Instruction stream: computers execute explicit instructions; the brain has none.
- Control: computers centralize it; the brain has no central controller.
- Memory versus processing: separated in a computer; the brain has no clear boundary between storage and computation. Synapses both transmit and store.
- Time: a computer is clocked and discrete; neural signals are continuous in time, variable in amplitude, and asynchronous.
- Noise: suppressed in a computer; present everywhere in the brain and, as later sections argue, exploited.
- Self-modification: a computer's hardware is fixed while it runs; the brain rewires itself while it is running.

Know the numbers behind the contrast: about 86 billion neurons and well over a hundred trillion synapses; a spike of about a millisecond and a synaptic delay of about half a millisecond, against transistors that switch in picoseconds. Against a processor's clock, the brain is roughly a million times slower per step, yet it can tell whether a briefly flashed photograph contains an animal within about 150 milliseconds (Thorpe and colleagues, 1996). That leaves room for only about a hundred sequential steps (Feldman and Ballard's hundred-step constraint), so perception must be massively parallel and shallow, not a long serial program.

The contrast is one of emphasis rather than kind. Von Neumann himself showed in 1952 that reliable computation can be built from unreliable components by redundancy and majority voting.

The differences trace back to different goals. Computers are built to produce correct answers to well-specified problems. Brains evolved to keep organisms alive in uncertain, hostile environments. Precision is useful only when it serves survival; flexibility, robustness, and speed frequently matter more.

The chapter's honest formulation is worth memorizing: brains and computers are both physical systems capable of computation under radically different constraints. Neither is a model of the other. Marr's three levels of analysis (what is computed, the procedure, the hardware) keep these apart: two systems can compute the same thing while sharing nothing at the level of procedure or hardware.

## The brain is a physical system

Every thought corresponds to physical change. Signals are ions crossing membranes; components are proteins changing shape, channels opening and closing, molecules diffusing through crowded cells. The decisive demonstration is Hodgkin and Huxley's 1952 model of the squid giant axon: four differential equations for a sodium and a potassium current reproduced the impulse's shape, threshold, and conduction velocity (18.8 meters per second computed against 21.2 measured), with nothing left over.

The energy budget is the constraint that shapes everything else. The brain is about 2 percent of body mass and uses about 20 percent of resting energy, roughly 20 watts. Attwell and Laughlin's budget for rodent gray matter puts about 47 percent on action potentials, 34 percent on glutamate's effects on receiving cells, and 13 percent on resting potentials; Lennie calculated that the cortex can afford only about one neuron in a hundred firing at any moment. Sparse codes, low firing rates, and short wiring follow from that budget.

The consequences follow directly from physics:
- Physical processes take time, so lasting learning is slow because molecular change is slow (one of two reasons; see the next note).
- Physical changes persist, so memory persists because structure persists.
- Physical systems consume energy and are noisy, so cognition is energy-limited and variable.
- Physical systems are affected by their chemistry, so fatigue, intoxication, and disease change cognition by changing metabolism and signaling.

The chapter's strongest statement here is that biology is not an imperfect implementation of abstract computation. Biology is the source of the computation. There is no cleaner process underneath.

## Why learning is slow

The chapter gives two reasons, and they are different in kind:
1) Lasting change is molecular construction. Early potentiation of a synapse takes a minute or two (receptors already waiting near the membrane are inserted), but change that lasts beyond a few hours needs new protein synthesis and structural growth, which take hours; blocking protein synthesis spares the early change and erases the late one. Kandel's Aplysia work shows the same split: one tail shock gives minutes of sensitization with no new protein, while five spaced shocks give days to weeks that depend on gene expression.
2) Fast change is dangerous. A system that rewrote itself on every experience would overwrite what it already knew, as McCloskey and Cohen's catastrophic interference shows for artificial networks. In the complementary learning systems account (McClelland, McNaughton, and O'Reilly, 1995), the hippocampus learns in one exposure and replays to the cortex, which integrates slowly and interleaved with old knowledge. Slow cortical learning is a requirement of stability, not a hardware limitation. Chapter 5 elaborates both reasons.

## No reset button

A computer can be restarted, cleared, and reinitialized. A brain cannot be returned to an earlier state without destroying it. Every experience leaves some trace, and development, learning, aging, and injury accumulate into a continuous, irreversible history.

The chapter's key experiment is Wiesel and Hubel's 1963 monocular deprivation: closing one eye of a newborn kitten during a sensitive period left almost every visual cortical neuron answering only to the open eye, largely permanently, while the same closure in an adult cat did nothing. Knudsen found the same logic in owl auditory maps, birdsong, and human language.

Three consequences to carry forward:
1) Learning is always incremental and constrained by what is already there.
2) Habits form because the system carries its past forward.
3) Early experiences can have outsized effects because they set the initial conditions for all later learning.

The same logic applies to evolution. It cannot redesign from scratch; it modifies what exists. Workable solutions persist once they support survival, even when better ones exist in principle. Historical contingency is a defining feature of living systems, not a flaw. Jacob called evolution a tinkerer, not an engineer; the recurrent laryngeal nerve, which loops down around an artery near the heart and back up to the larynx (several meters round trip in a giraffe), is the standard example. Gould and Lewontin add the caution that not every feature is an adaptation; some are byproducts.

## The brain as an adaptive control system

The chapter's positive proposal: view the brain as an adaptive control system embedded in a body, regulating behavior in an environment that is uncertain, dynamic, and only partially observable. Perception and action are continuously coupled. The system adjusts its own internal organization based on the consequences of its behavior. What it controls is a set of internal variables that must stay in bounds (Cannon's homeostasis; Ashby's essential variables), and learning is the controller changing its own organization when old behavior no longer keeps them there. The sentence to remember: the brain generates behavior, and the world corrects it.

Under this view:
- Perception is an active process of inference shaped by prior experience and biological need, not passive recording (Helmholtz's "unconscious inference," ancestor of the modern view of the brain as a prediction machine).
- Learning is how the controller adapts.
- Memory is the persistence of those adaptations.
- The objective is viability, not truth. Accuracy matters only insofar as it serves survival, and when precision conflicts with speed, energy, or robustness, precision often loses. Friston's free-energy principle is one contemporary, contested attempt to formalize this; whether it adds anything to Ashby is disputed.

This is why cognition is full of heuristics, biases, and shortcuts: Simon's satisficing, the systematic errors Tversky and Kahneman documented, and Gigerenzer and Brighton's finding that simple rules often predict better than complex models when data are few and noisy. They are trade-offs that favor survival under uncertainty.

## Noise, degeneracy, and the myth of optimization

Engineers suppress noise, and they use redundancy deliberately, by duplication: error-correcting memory, mirrored disks, triple-redundant flight computers. The brain is built from far noisier parts, and its redundancy is of a different kind.

The noise is measurable. Allen and Stevens (1994) found that more than half of the impulses arriving at single hippocampal synapses evoked no response; Shadlen and Newsome found that the spike-count variance of cortical neurons to repeated identical stimuli is about as large as the mean.

The brain uses rather than eliminates this variability:
- Populations of neurons average over the failures of their members.
- Feedback stabilizes dynamics, and homeostatic plasticity (Turrigiano and Nelson) scales a neuron's synapses over a day or more to hold its average activity in a working range.
- Inhibition prevents runaway excitation (Chapter 4); slow cortical learning is itself a stabilizing device (Chapter 5); distributed representations remove single points of failure.

Degeneracy (Edelman and Gally) is the ability of structurally different elements to perform the same function: many different neuron combinations can produce the same movement, many synaptic configurations can store the same memory. Unlike duplicated copies, which all fail under the same unanticipated condition, degenerate elements offer many partially independent answers, and they are raw material for evolution. Recovery after stroke is degeneracy at work: surviving tissue is not a spare copy but can be taught to do part of the lost tissue's job.

"Optimization" in biology means maintaining function across a wide range of conditions with limited resources, not maximizing a benchmark score. Judged by that standard, and by the 20-watt budget, Sterling and Laughlin argue the nervous system is near-optimal. Nor does the brain optimize nothing: there is no single global objective, but many circuits minimize a local error or cost, such as the reward prediction error of Chapter 3 and the sensory prediction error of Chapter 6.

## Why this matters before we study neurons

The mechanisms in Chapter 2 (electrical signaling, chemical communication, physical change with use) look arbitrary or overcomplicated without this frame, and intelligible with it. The sentence to keep: the brain is not an engineered solution to a clean problem; it is an evolved solution to a messy one. The chapter closes on Cajal's 1899 drawing of a Purkinje cell (Golgi stain): a dendritic tree with on the order of 200,000 inputs and a single axon that is the only output of the cerebellar cortex, a component whose shape is a wiring solution and whose synapses help the cerebellum learn to correct movements (Chapter 4).

## Implications for artificial intelligence

The chapter draws four lessons and a caution:
- Energy: the 20-watt budget forced sparse activity, low rates, local wiring, and prediction; as power becomes the binding constraint for AI, these economies are a design guide.
- Noise: artificial networks are deterministic and made robust only as an afterthought; noise injection and distributed representations rediscover the brain's strategy.
- No reset: catastrophic interference is still unsolved in general for artificial networks. The brain's answer, a fast learner replaying into a slow one, was arrived at independently in machine learning as experience replay (Lin 1992 predates the discovery of hippocampal replay in 1994; the two are convergent, not a borrowing).
- Control: most artificial systems are trained and then frozen; the brain generates behavior, observes consequences, and corrects, never frozen. Reinforcement learning faces the same problems of partial observability and delayed, noisy feedback.
- Caution: the brain's solutions are not the only ones. Some respond to constraints silicon does not share (no exact copies, no clock, no reset) and would be foolish to imitate; the point is to know which is which.

## Practical summary

- Computational vocabulary is useful but imports assumptions (precision, modularity, central control, clocking, noise-free operation) that the brain does not satisfy.
- The brain is matter. Every cognitive property is a property of tissue: slow, energy-limited (about 20 watts), noisy, persistent.
- Learning is slow for two reasons: lasting change is molecular construction, and fast change would overwrite old knowledge (complementary learning systems).
- There is no reset. Learning is incremental, history-dependent, and early experience sets the initial conditions.
- The brain is an adaptive controller whose objective is viability, not truth. It generates behavior, and the world corrects it. Heuristics and biases are trade-offs.
- Noise is exploited, not eliminated, and the brain's redundancy is degeneracy rather than duplication. Biological optimization means robustness under constraint, and many circuits do minimize local errors even though there is no single global objective.
- Suspend the intuition that apparent defects are design errors. Ask instead what problem the brain was actually solving.

# Labs

## Lab Notes: how to succeed in these labs

Chapter 1 is conceptual, so these labs are mostly about making your own assumptions explicit and then testing them against small, concrete models. Several labs ask you to compute; the arithmetic is deliberately simple. The value is in seeing a principle appear in numbers you produced yourself.

General rules:
1) Write your assumptions down before you start; you will compare them with your conclusions.
2) Draw the system where a diagram is requested.
3) Finish every lab with an interpretation that says what would change if the constraints changed.

### What to hand in for every lab

- A clean diagram or table (a photo of a hand drawing is fine).
- Any calculations, with intermediate values.
- A short interpretation (6-12 sentences).

## Lab 1.1 - Brains vs Computers (structured comparison)

### Purpose

To construct, from the chapter and your own knowledge, an explicit comparison between digital computers and biological brains, and to trace each difference to the constraint that produced it.

### Materials

Notebook, pen or pencil.

### Procedure

Part A - The comparison table

1) Make a table with three columns: Property, Digital computer, Brain.
2) Add at least these ten rows: instruction stream, locus of control, memory versus processing, timing, signal type, noise, component reliability, self-modification during operation, objective, and failure mode.
3) Fill each cell with a short concrete statement. Avoid the words "better" and "worse."

Part B - The fourth column

4) Add a fourth column headed "Constraint or goal behind the brain's version."
5) For each row, name the constraint that explains the biological choice (energy, survival under uncertainty, unreliable components, evolutionary history, no designer, partial observability, or another you can defend).

Part C - Find the leak

6) Pick three everyday sentences about the mind that use computational vocabulary (for example "I stored that in memory," "my brain is processing," "I need to reboot").
7) For each, write what the sentence quietly assumes and which row of your table shows the assumption failing.
8) Write 8-12 sentences: which difference in your table did you find most surprising, and which computational term do you now consider most dangerous?

### What to record

The four-column table, the three sentences with their analysis, and your interpretation.

## Lab 1.2 - No Reset Button (history-dependent learning by hand)

### Purpose

To feel, numerically, why a system that cannot reset is shaped by the order of its experiences, why early experiences have outsized effects, and why undoing learning is expensive.

### Given model

One internal variable w represents a learned tendency (positive = approach, negative = avoid). It starts at w = 0.
Each experience has a target T of +1 (good outcome) or -1 (bad outcome).
Update after experience number t: w_new = w + alpha_t * (T - w).
Plasticity declines with experience, as it does during development: alpha_t = 0.5 * 0.7^(t-1), so alpha_1 = 0.50, alpha_2 = 0.35, alpha_3 = 0.245, alpha_4 = 0.1715.

### Setup diagram

1) Draw a number line from -1 to +1 and mark w = 0.
2) You will plot the trajectory of w for two different orderings on this line.

### Procedure

Part A - Order matters

1) Sequence 1: experiences +1, +1, -1, -1. Compute w after each step. Record intermediate values. (Check: after step 2 you should have w = 0.675.)
2) Sequence 2: experiences -1, -1, +1, +1. Compute w after each step.
3) Both sequences contain exactly the same experiences. Compare the final values and their signs.

Part B - Early experience sets the initial conditions

4) Sequence 3: experiences +1, -1, -1, -1. Compute the final w.
5) Sequence 4: experiences -1, -1, -1, +1. Compute the final w.
6) One good experience appears in each sequence. Where does it have the larger effect, and why?

Part C - The cost of undoing

7) Start from the final w of Sequence 1. Plasticity is now low and fixed at alpha = 0.1.
8) Apply repeated -1 experiences and count how many are needed before w falls below -0.5. (Hint: the distance to -1 shrinks by a factor of 0.9 on each step.)
9) Compare with a computer: how many operations does it take to set a variable to -0.5?

Part D - Interpretation

10) Write 8-12 sentences: what does this model say about habits, about why childhood experiences persist, and about why "just unlearn it" is not an available operation? Name one thing the model leaves out that the real brain has.

### Optional code extension (Python, about 15 lines)

Implement the update rule and run 1,000 random sequences of ten experiences each, half +1 and half -1 in random order. Plot the distribution of final w. Then repeat with constant alpha = 0.3 and compare. Which schedule produces more diverse adults from the same set of experiences?

## Lab 1.3 - Noise and Redundancy (why unreliable parts make a reliable system)

### Purpose

To show with dice that averaging over noisy components and duplicating unreliable pathways produce reliability that no single component has, and to make the cost of that strategy explicit.

### Materials

One or more six-sided dice, notebook, calculator (recommended).

### Given model

A true signal has the value 10.
Each neuron reports the true value plus noise: report = 10 + (die roll - 3.5), so a single report lies between 7.5 and 12.5.
Each synapse transmits a spike with probability 1/2 (roll 4, 5, or 6 = transmitted).

### Procedure

Part A - Population averaging

1) Roll one die and compute a single neuron's report. Record the error (report minus 10).
2) Roll six dice, compute six reports, and average them. Record the error of the average.
3) Repeat steps 1 and 2 five times. Compare the typical size of the single-neuron error with the typical size of the six-neuron error.
4) Without rolling, predict what happens to the error of the average when the population is 36 neurons, then 360.

Part B - Redundant pathways

5) A message must cross one synapse. Flip or roll: what is the probability it gets through? Confirm by trying it ten times.
6) The same message is sent over five parallel synapses and succeeds if any one transmits. Compute the probability of success as 1 minus the probability that all five fail. Confirm by trying it ten times.
7) Repeat for ten parallel synapses.

Part C - The bill

8) Suppose each neuron costs one unit of energy per report and each synapse one unit per attempt. Compute the cost of Part A with 1, 6, and 36 neurons, and of Part B with 1, 5, and 10 synapses.
9) Write 8-12 sentences: why would evolution pay for redundancy instead of building a reliable synapse? What does the organism gain when a neuron dies in the redundant design versus the single-component design? Where does the strategy stop paying off?

## Lab 1.4 - Viability, Not Truth (decisions under asymmetric cost)

### Purpose

To show that a "biased" decision rule can be the correct one for an organism whose objective is survival, and to see the speed-accuracy trade-off in numbers.

### Given model

A rustle in the grass is a predator with probability 0.05, and nothing with probability 0.95.
Fleeing costs 1 unit (lost foraging time) whether or not a predator was present.
Staying costs 0 if nothing is there and 100 units if a predator is there.

### Procedure

Part A - Asymmetric costs

1) Compute the expected cost of fleeing.
2) Compute the expected cost of staying.
3) Decide. Then note the fact that the organism is "wrong" 95 percent of the time when it flees, and explain why this is still the right rule.
4) Find the predator probability at which the two choices break even.

Part B - The speed-accuracy trade-off

5) Suppose the animal can classify the rustle and act on its verdict, fleeing if it judges "predator" and staying otherwise. Acting immediately, it takes the wrong action 30 percent of the time. Waiting 1 second to gather more evidence cuts that to 5 percent, but if a predator really is present the second of waiting costs 40 units on top of whatever the action costs (the predator is closer now and may strike first).
6) For a true predator, compare the expected cost of acting immediately against waiting 1 second. For a false alarm, do the same. (Check: for a true predator, 30.7 against 45.95.)
7) Combine the two cases using the 0.05 and 0.95 probabilities. Compare acting immediately, waiting, and the always-flee rule of Part A, and decide which is best. Then find the cost of waiting at which waiting and acting immediately break even. (Check: 1.82, 2.345, and 1.0; break-even at 29.5 units.)

Part C - Interpretation

8) Write 8-12 sentences: what does this model say about why perception is biased toward threat, why reflexes trade accuracy for speed, and what "optimization" means for a system whose objective is to remain alive rather than to be right? Name one human cognitive bias that fits this template.

## Lab 1.5 - Engineering Autopsy and AI Reflection

### Purpose

To practice the chapter's central move: when the brain looks badly engineered, identify the problem it was actually solving. Then to test the chapter's principles against an artificial system you know.

### Procedure

Part A - The autopsy table

1) Make a table with three columns: Apparent defect, The problem a computer engineer thinks the brain is solving, The problem the brain is actually solving.
2) Fill at least six rows: slow learning, forgetting, perceptual bias, confabulation or filling-in, fatigue, and habit.
3) For each row, add a fourth column: what would break if the "defect" were removed.

Part B - AI reflection (the optional extension from the original companion, now required)

4) Choose one artificial system you know well: a large language model, a reinforcement-learning agent, a classifier, or a control system.
5) Take the six properties from the Student Notes (instruction stream, control, memory versus processing, timing, noise, self-modification) and classify your chosen system on each: computer-like, brain-like, or neither.
6) Identify one place where your system has a reset button that the brain lacks, and one place where it has no reset and suffers for it (for example, a deployed model that cannot forget a bad example).
7) Write 10-14 sentences: which of the chapter's principles does your system already honor, which does it violate, and which violation would you fix first if the system had to keep itself viable in an open environment rather than score well on a benchmark?
