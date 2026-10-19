---
title: "Chapter 16 Student Notes and Labs"
subtitle: "NIMCP: Building a Brain from the Book's Principles"
---

# Student Notes

## What this chapter is for

Chapter 16 applies the book's model to NIMCP, the author's own experimental attempt to build a brain from the mechanisms the book describes. It sets out what the system implements, what it has measured, and why, read through the earlier chapters, its difficulties fall where they do. It is a case study in turning principles into a working system, and in measuring the result honestly.

If you come from software or machine learning, the chapter is designed to correct three instincts:
1) assuming that a system containing the right mechanisms will work, when what matters is how the mechanisms are connected,
2) judging a system by its documentation, when the code and the measurements are what count, and
3) scaling up before each mechanism has been shown to work at a small scale.

Your goal is to be able to describe NIMCP's architecture, map it onto the eight statements of Chapter 15, explain why a learning rule without an eligibility trace assigns credit poorly, interpret the project's measurements, and design experiments that would test its mechanisms one at a time.

## A brain built from the book

- NIMCP ("Neuro-Inspired Modular Control Protocol"; trained instance "Athena"): about two million spiking neurons, six neuromodulators, sleep, homeostasis, a staged curriculum.
- Disclosure: the author's project. The account follows the code as of October 2026.

## What was built

- Conductance-based leaky integrate-and-fire neurons with AMPA, NMDA, and GABA receptors, Dale's principle, PV/SOM/VIP interneurons, 10 percent heterogeneity.
- About 2 million neurons and about 1.5 billion synapses (not "trillions"); a few hundred to a thousand inputs per neuron.
- An eight-tier generic hierarchy; named "regions" are mostly algorithmic modules; "hemispheres" are a routing rule (Figure 16.1).
- Backpropagation in a 150,000-unit network does much of the learning; text targets come from pretrained embeddings (Xiao et al. 2024); the parent is an LLM; output uses a lexicon, grammar rules, and in some interfaces Phi-3 (Abdin et al. 2024).

## The book's model, line by line

- Figure 16.2: body (partial: drives without a body), poor parts (running), prediction (partial), local learning with global gating (partial), several memory clocks (partial; EWC not connected), value-action-habit (partial: habits registered, but the basal ganglia never select actions), grown not specified (partial), compromise and inheritance (absent).

## How Athena learns

- In the large spiking network: Δw proportional to (reward − running average) when pre and post spike in the same step, with decay of the same synapses and reward-driven strengthening of co-active inhibition; no timing window, no eligibility trace.
- Dopamine-like signal from the falling training loss; TD module present but unused.
- Figure 16.3: without a trace, credit goes to whatever is active when reward arrives.

## What the measurements show

- May 2026: one to 33 different answers to 50 questions, none appropriate; intended word produced 1 of 20 times in every probe; no category structure in word representations (Figure 16.4).
- Firing-rate warnings of roughly 800 to 900 spikes a second from April to June; training stopped in late June 2026; October restarts killed dozens of times for exceeding memory.

## Reading the failures through the book

- Runaway firing: excitation outrunning inhibition and homeostasis (Chapters 1, 4, 5, 13).
- Collapsed output: background activity swamps the few neurons carrying the prompt ("ambient domination"), the readout face of runaway firing; no sequencing (Chapters 6, 9).
- Credit assignment without eligibility traces limits what the spiking core can learn, while backpropagation does most of the learning (Chapter 3).
- Drifting representations: one memory system instead of two (Chapter 5).
- Slow learning from a random start: no innate structure (Chapters 10, 13); scale is probably not the main obstacle (Figure 16.5).

## Safety written into the code

- Locked, hash-checked rules; locked drive set points; audit log; watchdog.
- Thin content: symbolic rules that the brain's numeric outputs rarely match; a per-decision ethics check based mainly on confidence.

## What NIMCP gets right, and what would test it

- The bet matches the book's model; several components are faithful to biology.
- Proposed order: stable firing at small scale; a three-factor rule with a trace against a control; fast and slow memory with replay; then lesions of a trained system.

## What building teaches

- Mechanisms translate readily; their connections do not. The hard parts of building are the brain's most distinctive achievements.

## Practical summary

- Read the code, not the description.
- Test each mechanism small, against a control, before scaling.
- A failure that falls where the theory predicts is evidence for the theory.

# Labs

## Lab Notes: how to succeed in these labs

These labs turn the chapter's case study into calculations and designs: an eligibility trace computed by hand, the cost of runaway firing, the arithmetic of the evaluations, the scale comparison, and the design of experiments that would test a brain-like system one mechanism at a time.

General rules:
1) Write every intermediate value, rounded to two decimal places unless told otherwise.
2) State every assumption you add, and say which way it would move the answer.
3) End with an interpretation: what does the calculation show, and what does it leave out?

### What to hand in for every lab

- A table of values.
- A diagram or sketch where requested (a photo of a hand drawing is fine).
- A short interpretation (6-12 sentences).

## Lab 16.1 - An Eligibility Trace by Hand

### Purpose

To see why a trace lets reward reach a synapse that is no longer active (Figure 16.3).

### Given values

A cue synapse is active at time steps 0, 1, and 2. Its eligibility trace at time d is the sum of exp(−(d − t)/τ) over the active steps t ≤ d, with τ = 8 steps. A coincidence rule credits the synapse only if it is active at the moment of reward.

### Procedure

1) Compute the trace at reward delays d = 2, 5, and 10. (Check: 2.66, 1.83, 0.98.)
2) What credit does the coincidence rule give at each delay? (Check: credit at d = 2; none at 5 and 10.)
3) Background synapses fire at random with probability 0.05 per step. Estimate the expected trace of a background synapse at the moment of reward, for τ = 8 (hint: a geometric series). Compare it with your answers in step 1.
4) Write 6-10 sentences: what sets the best τ for a task, and what happens if τ is much longer than the delays the animal faces?

## Lab 16.2 - The Cost of Runaway Firing

### Purpose

To put the firing-rate alerts in terms of work done.

### Given values

NIMCP's spiking network: 2.2 million neurons, about 682 synapses per neuron. Early firing rate: 26 spikes per second. Alert-level rate: 834 spikes per second. The homeostatic rule can scale weights by at most 2 percent per step.

### Procedure

1) Compute synaptic events per second at each rate. (Check: about 3.9 × 10^10^ and 1.25 × 10^12^.)
2) If scaling weights by 0.98 reduced firing in proportion, how many steps would it take to bring 834 down to about 28 spikes a second, a factor of 30? (Check: about 168 steps.)
3) Compare your answers with Chapter 1's estimate that the cortex can afford about one neuron in a hundred firing at any moment.
4) Write 6-10 sentences: why might homeostasis that works in a small network fail in a large one? Consider the speed of the controller and the strength of recurrent excitation (Chapter 4).

## Lab 16.3 - Reading the Evaluations

### Purpose

To practice interpreting measurements of a system that does not yet work.

### Given data

May 2026 evaluations: different answers to 50 questions at six checkpoints: about 20, 2, 19, 1, 33, and 21. Probes of 20 single-word intents: 1 correct in each of four runs; 16 to 17 different outputs per run.

### Procedure

1) For each checkpoint, compute the fraction of distinct answers. Which checkpoints show collapse onto a single answer?
2) A system can produce many different answers and still be wrong. Explain why the probe's "diversity" and "fidelity" must be read together.
3) Propose a measure of whether an answer is appropriate to its question that does not depend on another language model. What are its weaknesses?
4) Write 6-10 sentences: what would count as the first convincing evidence that the system has learned the meaning of a word?

## Lab 16.4 - Scale Is Not Organization

### Purpose

To compare NIMCP's size with biological nervous systems (Figure 16.5).

### Given values

NIMCP: 2.2 million neurons, 1.5 billion synapses. Fruit fly brain: 139,255 neurons, 54.5 million synapses. Human neocortex: 16.3 billion neurons, 164 trillion synapses. Honeybee: under a million neurons.

### Procedure

1) Compute synapses per neuron for NIMCP, the fly, and the human neocortex. (Check: about 682, 391, and 10,061.)
2) NIMCP has more neurons than a bee. List three things a bee brain has that NIMCP lacks, using Chapters 10 and 13.
3) If NIMCP's connections per neuron were raised to the cortical figure, how many synapses would it have, and how much memory would that need at 12 bytes per synapse? (Check: about 2.2 × 10^10^ synapses; about 265 GB.)
4) Write 6-10 sentences: is the obstacle to NIMCP's learning more likely to be its size or its organization? Defend your answer.

## Lab 16.5 - Auditing a Mechanism

### Purpose

To practice the chapter's method: compare what a system's description says with what it does.

### Procedure

1) Choose one row of Figure 16.2.
2) Write down, in one sentence each, what the description of that mechanism claims and what the chapter reports the code does.
3) List the observable behavior that would differ if the mechanism were fully connected.
4) Design a test that would detect the difference, with a control condition.
5) Write 6-10 sentences: why do descriptions of complex systems drift away from their implementations, and how can a project guard against it?

## Lab 16.6 - Designing the Next Experiment

### Purpose

To plan one of the small experiments the chapter proposes.

### Procedure

1) Choose one: stable firing at small scale; a three-factor rule against a coincidence rule on a delayed-reward task; fast and slow memory joined by replay; or a lesion of a trained system.
2) State the hypothesis, the network size, the task, the control, the measurement, and the result that would count as success or failure.
3) Predict the result from the book's model, and say which chapter supports your prediction.
4) Write 6-10 sentences: what would you do next if the result came out the other way?

## Lab 16.7 - NIMCP on the Model (concept map)

### Purpose

To place NIMCP's components on the model of Chapter 15.

### Procedure

1) Copy Figure 15.1.
2) Mark each component of Figure 16.1 on it, using one color for components that run in the main path, another for those present but not connected, and a third for those absent.
3) Draw the connections between components that the chapter says are missing.
4) Identify the single missing connection whose addition you think would help most, and justify it with evidence from the book.
5) Write 8-12 sentences: what does this case study teach about the relation between understanding a system and building one?
