---
title: "Chapter 13 Student Notes and Labs"
subtitle: "Why the Brain Works the Way It Does: Constraints, Trade-offs, and the Shape of a Solution"
---

# Student Notes

## What this chapter is for

The earlier chapters described how the brain works. Chapter 13 asks why it works that way, in Tinbergen's sense of survival value and evolutionary history. Its answer: the brain's form is where a few hard constraints (energy, space and wire, time, noise, the capacity of the genome, and the need to serve many tasks at once) meet a history that could only modify what already existed. Many features are trade-offs, positions on a front between goals, rather than optimal solutions; some are simply inherited.

If you come from software or machine learning, the chapter is designed to correct three instincts:
1) reading every feature of the brain as either optimal or a flaw, when most are compromises among goals that cannot all be maximized,
2) treating information as free once the hardware exists, when in the brain every bit has an energy price that rises with the bit rate, and
3) copying a biological feature without asking which constraint it answers, when a feature is worth copying only if the machine faces the same constraint.

Your goal is to be able to explain what information costs and why sparse firing and unreliable synapses can be efficient, why long-distance signals are spikes, how speed trades against space, why wiring is not simply minimized, what a Pareto front is, how energy limits brain size, how convergence helps separate constraint from history, why the genome forces the brain to learn, and how mismatch arises.

## The fish that gave up its eyes

- Cavefish: the eyes and visual brain of a one-gram river fish cost an estimated 15 percent of resting metabolism (Moran, Softley, and Warrant 2015); whether the saving explains eye loss is debated.
- Tinbergen's four questions (1963): causation, development, survival value, evolution. The chapter addresses the last two.
- Figure 13.1 maps constraints to the features they help explain.

## The price of a bit

- Blowfly: about 10,000 ATP per bit at a synapse, a million to ten million in a photoreceptor or interneuron; a law of diminishing returns (Laughlin et al. 1998).
- Blowfly photoreceptors carry about five times the information of the fruit fly's at about ten times the energy per bit (Niven et al. 2007).
- Bits per unit energy peak at low firing probability (Levy and Baxter 1996) (Figure 13.2): about 10 to 20 spikes a second rather than 200; synaptic failures can raise efficiency in theory (Levy and Baxter 2002).
- Thalamic relay synapses are tuned close to the most bits per ATP, not the most bits (Harris et al. 2015).
- Efficient spikes: 1.3 times the minimum sodium entry in mossy fibers (Alle et al. 2009); fast-spiking cells pay about twice the minimum (Carter and Bean 2009).

## Why spikes

- Graded signals carry more (about 1,650 bits per second in blowfly interneurons) but degrade with distance.
- Hybrid computation: graded locally, restored to discrete form over distance (Sarpeshkar 1998).
- Short neurons compute in graded form: photoreceptors, most bipolar cells, most *C. elegans* neurons (which also have calcium spikes in a few cells).

## Speed costs space

- Bare axons: speed rises with the square root of diameter (squid: 476 µm, 21.2 m/s). Myelinated fibers: about 6 m/s per µm (Hursh 1939) (Figure 13.3).
- Few fast lines, many slow ones (Wang et al. 2008); interhemispheric delay and hemispheric specialization (Ringo et al. 1994, a conjecture).
- White matter grows faster than gray (Zhang and Sejnowski 2000); folding follows the physics of a growing sheet (Mota and Herculano-Houzel 2015; Tallinen et al. 2016).

## Placing the parts

- The worm's ganglia sit in the wire-minimizing order out of about 40 million (Cherniak 1994).
- But rearrangement could cut wiring by 48 percent (worm) and 32 percent (macaque) at the cost of longer paths (Kaiser and Hilgetag 2006). The brain's economy is a trade (Bullmore and Sporns 2012) (Figure 13.4).
- A cost on connections makes evolved networks modular and, on nested problems, hierarchical, and they adapt faster (Clune, Mouret, and Lipson 2013; Mengistu et al. 2016): small abstract networks, but a possible reason for the brain's modules and hierarchy of areas.

## Many jobs at once

- Pareto fronts and archetypes (Shoval et al. 2012) (Figure 13.5).
- Very different combinations of ion channels and synapses give nearly the same rhythm in a model circuit (Prinz, Bucher, and Marder 2004); Pareto optimality may pick among them (Jedlicka et al. 2022, a proposal).
- "Robust yet fragile" (Csete and Doyle 2002); the hubs of Chapter 4.

## How big a brain

- About 6 kcal a day per billion neurons (Herculano-Houzel 2012); the cooking hypothesis (Fonseca-Azevedo and Herculano-Houzel 2012) and its critics (Cornélio et al. 2016).
- Childhood: brain glucose equivalent to about two-thirds of resting metabolism at about age four; body growth slowest then; total glucose use peaks at about five (Kuzawa et al. 2014).
- No gut trade-off across 100 mammals, but less fat (Navarrete et al. 2011); humans raised the whole budget (Pontzer et al. 2016).
- Obstetric dilemma versus a metabolic limit (Dunsworth et al. 2012; Warrener et al. 2015; Cordey et al. 2023): open.
- Extremes: the elephantnose fish's brain uses roughly 60 percent of its oxygen (Nilsson 1996); *Megaphragma* has about 7,400 neurons, most without nuclei (Polilov 2012); bees with fewer than a million neurons (Chittka and Niven 2009).

## Different histories, same answers

- Persistence: lamprey basal ganglia (Grillner and Robertson 2016).
- Convergence: dense bird forebrains (Olkowicz et al. 2016), cortex-like circuits in birds (Stacho et al. 2020), largely convergent (Rueda-Alaña et al. 2025); the octopus (Young 1963; Hochner 2012).
- History: the inverted retina, partly compensated by Müller cells (Franze et al. 2007; Labin et al. 2014); some argue the arrangement serves the photoreceptors' supply of energy and pigment (Baden and Nilsson 2022).

## The bottleneck of the genome

- About 1 GB of genome against about 3.7 × 10^15 bits to list the brain's connections (Zador 2019) (Figure 13.6).
- The genome encodes rules; self-organization and learning finish the brain.
- Compression through a "genome" network can give good performance before training (Shuvaev et al. 2024).

## Trade-offs that cannot be escaped

- Figure 13.7: holding versus changing, expectation versus input, sensitivity versus range, speed versus accuracy, exploiting versus exploring, flexibility versus economy, information versus energy, short paths versus short wires.
- Neuromodulators move the brain along these fronts as conditions change.

## Built for a different world

- Supernormal stimuli (Tinbergen and Perdeck 1950; Tinbergen 1951); beetles and beer bottles (Gwynne and Rentz 1983).
- The mismatch hypothesis (Li, van Vugt, and Colarelli 2018): plausible, hard to test.

## Implications for artificial intelligence

- In chips, moving data costs far more than arithmetic (Chapter 11); sparse mixtures of experts (DeepSeek-V3: 37 billion of 671 billion parameters active per word) largely converge on the brain's economy.
- Copy a feature only if the machine shares the constraint it answers; a chip already restores its signals at every step, as an axon does with spikes.
- The genome bottleneck as a possible inductive bias.
- Many tasks under one budget, and moving along fronts per situation.

## Practical summary

- Information costs energy, and the cost per bit rises with the rate.
- Speed costs space; the brain buys it sparingly.
- Most features are compromises among goals, not optima.
- The genome cannot specify a large brain, so the brain must learn.
- Ask whether a feature reflects a constraint or a history: look for convergence.

# Labs

## Lab Notes: how to succeed in these labs

These labs turn the chapter's argument into short calculations: what firing rate gives the most information for the energy spent, what conduction speed costs in space, how a few long connections shorten paths, how far a genome falls short of a wiring list, how to find a Pareto front, and what a growing brain costs a child. Each isolates one idea. The arithmetic is light; the point is to see where the numbers come from and how much they depend on assumptions.

General rules:
1) Write every intermediate value, rounded to two decimal places unless told otherwise.
2) State every assumption you add, and say which way it would move the answer.
3) End with an interpretation: what does the calculation show, and what does it leave out?

### What to hand in for every lab

- A table of values.
- A diagram or sketch where requested (a photo of a hand drawing is fine).
- A short interpretation (6-12 sentences).

## Lab 13.1 - The Price of a Bit

### Purpose

To see why the most efficient firing rate is far below the most informative one (Levy and Baxter; Figure 13.2).

### Given values

A neuron either fires or stays silent in each 2.5 ms time bin, with spike probability p. Information per bin: H(p) = −p log2 p − (1 − p) log2 (1 − p). Energy per bin = r + p, where the cost of rest r = 0.05 of a spike.

### Procedure

1) For p = 0.5, 0.2, 0.1, 0.05, and 0.02, compute H(p), the energy per bin, and the bits per unit energy. (Check: H = 1.00, 0.72, 0.47, 0.29, 0.14; bits per unit energy = 1.82, 2.89, 3.13, 2.86, 2.02.)
2) Which p gives the most information per bin, and which the most per unit energy? (Check: 0.5; about 0.1.)
3) Convert each p to spikes per second. (Check: 200, 80, 40, 20, 8.)
4) Repeat step 1 with r = 0.01. Does the best p move up or down? Explain why in one sentence.
5) Write 6-10 sentences: what this simple model leaves out (for example, information carried by spike timing, or the cost of synapses on the receiving side), and why Levy and Baxter's estimate of 10 to 20 spikes a second is still informative.

## Lab 13.2 - Speed Costs Space

### Purpose

To compare bare and myelinated fibers and connect conduction delay to brain size (Figure 13.3).

### Given values

Bare axon: speed = 0.97 × √d m/s, with d the diameter in µm (calibrated to the squid giant axon, 476 µm and 21.2 m/s).
Myelinated fiber: speed = 6 × d m/s (Hursh's rule, valid from about 1 to 20 µm).
Cross-sectional area is proportional to d².

### Procedure

1) For speeds of 1, 10, and 50 m/s, find the diameter needed by each kind of fiber. (Check: bare 1.1, 106, and 2,657 µm; myelinated 0.17, 1.67, and 8.33 µm. The myelinated value at 1 m/s lies outside the rule's range: say why that matters.)
2) For each speed, compute the ratio of cross-sectional areas. (Check: about 40, 4,000, and 100,000.)
3) A signal crosses 10 cm between the hemispheres. Compute the delay for a 1 µm myelinated fiber and for bare axons of 0.5 and 0.2 µm. (Check: 16.7 ms; about 146 ms; about 230 ms.)
4) A computation needs ten one-way crossings between the hemispheres. Compute the total delay for the myelinated fiber, and compare it with a spoken syllable of about 200 ms. (Check: about 167 ms.)
5) Write 6-10 sentences relating your answer to Ringo's conjecture, and say what evidence would test it.

## Lab 13.3 - Short Wires or Short Paths

### Purpose

To see, by hand, how a few long connections shorten paths at a cost in wire (Figure 13.4).

### Given values

Eight neurons sit on a line at positions 0 to 7. Each connects to its immediate neighbors (a chain). The wire cost of a connection is the distance between its ends. Path length is the number of connections a signal must cross.

### Procedure

1) For the chain alone, compute the total wire, the average path length over all 28 pairs, and the longest path. (Check: 7; 3.00; 7.)
2) Add one long connection from 0 to 7. Recompute. (Check: 14; 2.29; 4.)
3) Instead add one connection from 2 to 5. Recompute. (Check: 10; 2.36; 5.)
4) Instead add two connections, 0 to 4 and 3 to 7. Recompute. (Check: 15; 1.96; 4.)
5) Plot the four designs as points, wire on the horizontal axis and average path on the vertical. Which designs are on the front (no other design has both less wire and a shorter average path)?
6) Write 6-10 sentences: which design would you choose if wire were very expensive, and which if speed mattered most? How does this connect to the hubs of Chapter 4 and Csete and Doyle's "robust yet fragile"?

## Lab 13.4 - The Genome Bottleneck

### Purpose

To redo Zador's calculation and see where it does and does not bite (Figure 13.6).

### Given values

A genome holds 2 bits per base pair. Naming the target of one connection among N neurons takes log2 N bits.
Human: genome 3.1 × 10^9 base pairs; 10^11 neurons; 10^14 connections.
Worm: genome 1.0 × 10^8 base pairs; 302 neurons; about 7,000 synapses.
Hypothetical insect (for this exercise only): genome 1.4 × 10^8 base pairs; 10^5 neurons; 10^7 synapses.

### Procedure

1) Compute the genome's capacity in bits and the wiring list's size in bits for the human. (Check: 6.2 × 10^9; about 3.7 × 10^15; the list is about 590,000 times larger.)
2) Repeat for the worm. (Check: 8.24 bits per synapse; 2.0 × 10^8 against 5.8 × 10^4; the genome is about 3,500 times larger.)
3) Repeat for the hypothetical insect. (Check: 16.61 bits per synapse; 2.8 × 10^8 against 1.7 × 10^8; the list would use about 60 percent of the genome.)
4) Only a few percent of the human genome codes for proteins. Recompute step 1 using 2 percent of the genome, and say whether the conclusion changes.
5) Write 6-10 sentences: why is this an upper bound on what development needs, and what supplies the information the genome does not?

## Lab 13.5 - Finding a Pareto Front

### Purpose

To find the designs no other design beats and see how the "best" design depends on the weight given to each goal (Figure 13.5).

### Given data

Eight neuron designs, each with an energy cost (arbitrary units) and the information it transmits (bits per second):

| Design | Energy | Information |
|---|---|---|
| A | 2 | 40 |
| B | 3 | 70 |
| C | 4 | 65 |
| D | 5 | 95 |
| E | 6 | 100 |
| F | 8 | 104 |
| G | 7 | 90 |
| H | 10 | 106 |

### Procedure

1) Plot the eight designs. Identify those that no other design beats on both counts (cheaper or equal, and at least as informative). (Check: A, B, D, E, F, H.)
2) Explain in one sentence each why C and G are off the front.
3) Compute bits per unit energy for every design. Which is best by that measure? (Check: B, at about 23.3.)
4) Suppose the organism values information minus w times energy. Find the best design for w = 1.5, 10, and 25. (Check: F, D, B.)
5) Write 6-10 sentences: why is "the most efficient design" not the same as "the best design," and what in an animal's life might set w?

## Lab 13.6 - Paying for a Brain

### Purpose

To put the chapter's energy figures on a common scale.

### Given values

About 6 kcal a day per billion neurons (Herculano-Houzel); 86 billion neurons in the adult human brain.
At about age four, brain glucose uptake is equivalent to about 66 percent of resting metabolic rate and 43 percent of total daily energy needs (Kuzawa and colleagues).
For this exercise, assume a four-year-old's resting metabolic rate is 1,000 kcal a day and total daily needs are 1,500 kcal.

### Procedure

1) Compute the adult brain's daily cost, and convert it to watts (1 kcal a day is about 0.0484 W). Why might it exceed the round 20 watts of Chapter 1? (Check: 516 kcal; about 25 W.)
2) Compute the four-year-old's brain glucose equivalent using each figure. (Check: 660 kcal and 645 kcal.) Why are these not exactly the brain's energy use? (Hint: not all glucose is burned.)
3) Compare the child's figure with the adult's. What does it imply about when the brain is most expensive?
4) Suppose an ape brain has 30 billion neurons (a round number for this exercise). Compute its cost at the same rate, and compare it with the human brain's.
5) Write 6-10 sentences: what are the ways an animal can pay for a more expensive brain (cutting other organs, storing fat, raising total metabolism, slowing growth), and which does the chapter's evidence favor for humans?

## Lab 13.7 - Constraint or History? (concept map)

### Purpose

To sort the brain's features by the kind of explanation they need.

### Procedure

1) List ten features from this book: for example, sparse firing, spikes, myelin, small-world wiring, cortical folding, two memory systems, the basal ganglia loop, the inverted retina, sensitive periods, dopamine prediction errors.
2) For each, name the constraint or constraints that help explain it (use Figure 13.1), or mark it as mainly historical.
3) For each, say whether convergence (the same feature in an unrelated lineage) is known, and cite the example if so.
4) Draw a map linking features to constraints, and mark every trade-off from Figure 13.7 that applies.
5) Write 8-12 sentences answering: which feature on your list is the strongest example of a constraint at work, and which the strongest example of history? What evidence would change your mind?
