---
title: "Chapter 15 Student Notes and Labs"
subtitle: "A Coherent Model of the Human Brain: How the Pieces Fit"
---

# Student Notes

## What this chapter is for

Chapter 15 assembles the book into one model of how the brain learns: eight statements, each supported by evidence from several earlier chapters, that together explain one another. It traces a single piece of learning through every level, shows how the levels change one another, asks what complete wiring diagrams will and will not reveal, explains disorders as failures of particular parts of the model, and sorts the model's claims into settled, probable, and open.

If you come from software or machine learning, the chapter is designed to correct three instincts:
1) believing that enough data about the parts will reveal how a system works, when understanding requires a model of how the parts relate,
2) treating the brain's levels as a stack of modules, when every level changes the others, and
3) treating a wiring diagram as a program, when the same wiring computes different things in different chemical states and records a history of learning.

Your goal is to be able to state the eight statements and the evidence for each, trace one learning episode across timescales, explain why connectomes are necessary but not sufficient, place common disorders within the model, and say which claims are settled and which are open.

## A neuroscientist studies a microprocessor

- Applying neuroscience's methods to the MOS 6502 chip, with a complete wiring diagram, did not reveal how it worked (Jonas and Kording 2017); biologists and the broken radio (Lazebnik 2002).
- Lesson: data need a model.

## A model built over a century

- Cajal's neurons; Helmholtz's inference; Cannon and Ashby's regulation; Craik's model in the head; Hebb's rule and Bliss and Lømo's LTP; Hodgkin and Huxley's impulse; Hubel and Wiesel's sensitive period; Schultz's dopamine and temporal-difference learning; McClelland, McNaughton, and O'Reilly's two memory systems.
- Pieces found from different directions that fit together.

## The model in eight statements

1) It serves a body (Chapters 1, 7, 12).
2) It is built from poor parts (0, 1, 2, 13).
3) It predicts (3, 6, 7, 8, 9, 12).
4) It learns locally and keeps globally (2, 3, 5, 10, 11).
5) It remembers on several clocks (1, 5, 9–12, 14).
6) It turns value into action, and action into habit (3, 4, 7, 8, 9, 14).
7) It is grown, not specified (0, 1, 6, 10, 13).
8) It is a compromise and an inheritance (1, 3, 4, 13).
- A thread through several statements: much learning comes from other people (Chapter 14).
- Figures 15.1 and 15.2.

## One afternoon, every level

- Learning to drive on the left: prediction errors, norepinephrine and attention, cerebellar recalibration, dopamine and eligibility traces, hippocampal encoding, sleep replay, the shift to habit (Figure 15.3).
- The old habit kept as a separate latent cause, which returns in the old context (Gershman, Blei, and Niv 2010).

## The levels talk to each other

- Neuromodulators reconfigure fixed wiring (Marder 2012; Bargmann 2012).
- Brain-wide recordings: movement and reward signals almost everywhere (International Brain Laboratory 2025); the prior represented in a fifth to a third of regions (Findling et al. 2025); multiscale networks (Bassett and Sporns 2017).

## When the model breaks

- Parkinson's disease (dopamine and action), with Oliver Sacks's L-dopa patients waking and then overshooting (Sacks et al. 1970; Sacks 1990), addiction (habit, disputed), returning fear (extinction as a second memory), hallucinations (expectation weighted too heavily), Alzheimer's disease (hubs; retrieval failures in mouse models; Josselyn and Tonegawa 2020).

## The wiring diagram arrives

- Crick (1979) called a cubic millimeter's wiring diagram impossible.
- FlyWire: 139,255 neurons and 54.5 million synapses (Dorkenwald et al. 2024; Schlegel et al. 2024); MICrONS: over 200,000 cells and about half a billion synapses in a cubic millimeter of mouse cortex (2025); H01: about 57,000 cells and 150 million synapses in a cubic millimeter of human cortex (Shapson-Coe et al. 2024); a human cell census of 3,313 subclusters (Siletti et al. 2023) (Figure 15.4).
- "Each wiring diagram encodes many possible circuit outcomes" (Bargmann and Marder 2013).

## No two brains alike

- Degeneracy and individual histories make every brain unique: 40 genetically identical mice in one enclosure diverged, and the widest explorers made the most new hippocampal neurons (Freund et al. 2013). The model describes the rules, not a particular brain.

## What is settled and what is open

- Settled: engrams (mostly rodent work), dopamine prediction errors, fast and slow memory, energy constraints, adaptation at every level, neuromodulatory reconfiguration (shown mainly in small circuits). Probable: prediction as the cortex's general strategy, three-factor rules, replay in sleep, habit circuits, body-anchored value (Figure 15.5).
- Open: credit assignment in cortex (Lillicrap et al. 2020; Payeur et al. 2021), dendritic computation (Gidon et al. 2020; Beaulieu-Laroche et al. 2018), what sleep does to synapses (Tononi and Cirelli 2014; de Vivo et al. 2017; Yang et al. 2014), glia (Adamsky et al. 2018; Agulhon et al. 2010), molecular storage (Langille and Gallistel 2020), one principle.
- Beyond the book: consciousness.

## Implications for artificial intelligence

- Shared: prediction errors, learned hierarchies, sparse activation.
- Lacking: a body and its values, multi-timescale memory with replay, local learning gated by several signals, neuromodulatory reconfiguration, an energy constraint.

## Practical summary

- The brain learns by changing its own structure, in a body, under constraint.
- Prediction errors drive learning; broadcast signals decide what is kept.
- Fast and slow memory, linked by sleep; choices become habits.
- The same wiring does different things in different states.
- Each brain is the record of a life.

# Labs

## Lab Notes: how to succeed in these labs

These labs ask you to use the whole book: to place phenomena in the model, to work with the numbers of the new wiring diagrams, to compute a three-factor learning window and a latent-cause inference, and to judge which claims are settled. The arithmetic is light; the point is to connect the levels.

General rules:
1) Write every intermediate value, rounded to two decimal places unless told otherwise.
2) State every assumption you add, and say which way it would move the answer.
3) End with an interpretation: what does the calculation show, and what does it leave out?

### What to hand in for every lab

- A table of values.
- A diagram or sketch where requested (a photo of a hand drawing is fine).
- A short interpretation (6-12 sentences).

## Lab 15.1 - Placing Phenomena in the Model

### Purpose

To use the eight statements as a map.

### Procedure

1) For each of these phenomena, name the statement or statements of the model it illustrates, and the chapter where it was described: the waterfall illusion; Schultz's monkeys; the cavefish's lost eyes; spaced study; the stale popcorn eaten by habit; the London taxi drivers; the dopamine timing window in a single spine; Kuhl's infants learning from live speakers; synaptic failures; the return of extinguished fear.
2) Which statement appears most often in your list? Which least?
3) Pick one phenomenon that fits two statements and explain how the two interact in it.
4) Write 6-10 sentences: is any phenomenon from the book hard to place in the model? What would that imply?

## Lab 15.2 - The Numbers of the Wiring Diagrams

### Purpose

To get a feel for the scale of the new connectomes and what a whole human brain would require.

### Given values

Worm: 302 neurons, about 7,000 synapses. Fly: 139,255 neurons, 54.5 million synapses. Human cortex sample: 16,087 neurons, about 149.9 million synapses, 1.4 petabytes of data, about 1 cubic millimeter. Human neocortex: about 16.3 billion neurons, about 164 trillion synapses. Assume (for the exercise) a human brain volume of 1.2 million cubic millimeters.

### Procedure

1) Compute synapses per neuron for the worm, the fly, the human sample, and the human neocortex. (Check: about 23; about 391; about 9,318; about 10,061.) Why is the human-sample figure only an approximation? (Hint: many synapses in the sample come from axons whose cell bodies lie outside it.)
2) Estimate the data needed to image a whole human brain at the same resolution. (Check: about 1.68 million petabytes, or about 1.7 zettabytes.)
3) The fly's wiring diagram took years of work by a large consortium. List three things a complete human wiring diagram would still not tell you, using Bargmann and Marder's argument and Chapter 13's genome bottleneck.
4) Write 6-10 sentences: what kind of question could a connectome answer that recordings of activity cannot, and the reverse?

## Lab 15.3 - Timescales

### Purpose

To appreciate the range of timescales the model must span.

### Procedure

1) Using Figure 15.3, list the timescale of each mechanism and the chapter where it was described.
2) Compute the ratio between one year and one millisecond. (Check: about 3.15 × 10^10^.)
3) For each adjacent pair of mechanisms in the figure, describe the signal or process that hands information from the faster to the slower.
4) Write 6-10 sentences: which handoff is best understood, and which least?

## Lab 15.4 - The Three-Factor Window

### Purpose

To compute how an eligibility trace limits when a reward signal can strengthen a synapse.

### Given values

A synapse's eligibility trace decays as e(t) = exp(−t / τ), with τ = 1 second. The weight change is proportional to e(t) at the moment dopamine arrives.

### Procedure

1) Compute e(t) for dopamine arriving 0.5, 1, and 3 seconds after the activity. (Check: 0.61, 0.37, 0.05.)
2) The spine experiment described in Chapter 3 found potentiation only for dopamine arriving between about 0.3 and 2 seconds later. Does a simple exponential trace explain the lower limit? What else might?
3) In the driving example, a well-judged turn earns a sense of relief a second or two later. Which synapses can be credited, and which cannot?
4) Write 6-10 sentences: how does the brain bridge delays longer than a few seconds? (Consider Chapter 3's temporal-difference account and Chapter 5's replay.)

## Lab 15.5 - One Context or Two?

### Purpose

To work through a simple latent-cause inference like the one in the driving example.

### Given values

After moving, a driver's habitual action succeeds on 3 of 10 occasions. Three hypotheses about the current context: the old context, in which the action succeeds 80 percent of the time; a new context, in which it succeeds 20 percent; or an unknown context, 50 percent. The log likelihood of k successes in n trials with success probability p is k log p + (n − k) log(1 − p).

### Procedure

1) Compute the log likelihood under each hypothesis. (Check: −11.94, −6.39, −6.93.)
2) Which hypothesis is best supported? By how much does it beat the old context, in log units?
3) A learner that infers a new context keeps the old values intact. Explain why this predicts that the old habit returns on a visit home.
4) Repeat step 1 for 8 successes in 10. Which hypothesis wins now? (Check: −5.00, −13.32, −6.93; the old context.)
5) Write 6-10 sentences relating this calculation to the return of extinguished fear (Chapter 7) and to savings (Chapter 9).

## Lab 15.6 - Settled or Open?

### Purpose

To practice judging the state of evidence for a claim.

### Procedure

1) Choose two claims from the "Settled" box of Figure 15.5 and two from the "Open" box.
2) For each, name the strongest piece of evidence described in the book, and the most serious limitation of that evidence.
3) For one open claim, design an experiment that could move it to "Probable" or "Settled". State what result would do so and what result would move it the other way.
4) Write 6-10 sentences: what distinguishes the settled claims from the open ones?

## Lab 15.7 - The Book in One Map (concept map)

### Purpose

To build your own version of the model.

### Procedure

1) Draw a map with one node for each of Chapters 0 to 14.
2) Draw an arrow from one chapter to another whenever the later chapter depends on a mechanism described in the earlier one, and label each arrow with the mechanism.
3) Overlay the eight statements of Figure 15.1 as regions of your map.
4) Identify the single chapter whose removal would most damage the model, and justify your choice.
5) Write 8-12 sentences: in your own words, how does the brain learn?
