---
title: "Chapter 3 Student Notes and Labs"
subtitle: "Neuromodulation"
---

# Student Notes

## What this chapter is for

Chapters 1 and 2 gave you a neuron that integrates inputs and sometimes fires. Chapter 3 answers a question that model cannot answer on its own: given that neurons are firing all the time, when does the brain actually learn, and what decides which synapses change?

The chapter's answer is that fast electrical signaling and learning are separate processes, coupled by a slow chemical layer called neuromodulation. A handful of small brainstem and basal forebrain nuclei broadcast chemicals across most of the brain. Those chemicals do not carry sensory content. They carry context: safe or threatened, better or worse than expected, stable or surprising. Plasticity is permitted only when that context says it should be.

If you are coming from machine learning, this chapter is designed to correct three instincts:
1) treating learning as something that happens on every forward pass,
2) assuming an error signal can always be traced back to the parameter that caused it, and
3) reading "dopamine" as "reward."

Your goal is to be able to explain, in plain language, why the brain cannot run backpropagation, what it does instead, and why that alternative is a reasonable design under uncertainty rather than a defect.

## Two timescales, one circuit

Synaptic transmission is fast (milliseconds), spatially precise, and short-lived. It moves information.

Neuromodulation is slow (seconds to minutes, sometimes hours), spatially diffuse, and persistent. It does not move information. It changes how circuits respond to information: it raises or lowers excitability, biases competition between pathways, and gates whether synapses are allowed to change.

The same wiring therefore behaves differently depending on chemical state. This is why the "rigid machine" picture from the start of the chapter fails: identical inputs do not produce identical outcomes, because the circuit is never in exactly the same chemical state twice.

You should be able to say: synapses carry the message; neuromodulators set the terms on which the message is received.

## Volume transmission versus synaptic transmission

At a classical synapse, neurotransmitter crosses a gap of tens of nanometers and acts within microseconds to milliseconds on one postsynaptic cell.

Neuromodulators are often released from varicosities along the axon rather than at a tight synapse. They diffuse through extracellular space over hundreds of nanometers to micrometers and act over milliseconds to minutes on every receptor they reach. This is called volume transmission (Figure 3.1 in the chapter).

The engineering consequence: a neuromodulator cannot address a single synapse. It addresses a region. Any precision in the resulting learning has to come from somewhere else (see eligibility traces below).

## The "-ergic" vocabulary

Neurons are often named by the chemical they release. The suffix "-ergic" means using or releasing.
- dopaminergic: releases dopamine
- noradrenergic: releases norepinephrine (noradrenaline)
- serotonergic: releases serotonin
- cholinergic: releases acetylcholine

These labels describe chemical influence, not meaning. A dopaminergic neuron does not "represent reward"; it releases a chemical that other circuits interpret in context.

## Why the systems are diffuse

Neuromodulatory nuclei contain very few cells, yet one cell can influence tens of thousands of synapses through widely branching axons.

To an engineer this looks wasteful. It is not. The signal being sent is global by nature. "Outcomes are better than expected" or "the environment just became unpredictable" is information every circuit needs at once. Broadcasting it from a small source is cheaper and more coherent than computing it locally in millions of places. Diffuse projection lets a few hundred thousand neurons coordinate billions without a central controller.

## Dopamine encodes prediction error, not reward

The chapter's most important correction: dopamine activity tracks the difference between what was expected and what occurred.

- Outcome better than expected: dopamine increases above baseline.
- Outcome exactly as expected: dopamine stays near baseline.
- Outcome worse than expected: dopamine dips below baseline.

Two consequences follow. First, a fully predicted reward produces almost no dopamine response, even though the reward is still pleasant. Second, once a cue reliably predicts a reward, the dopamine response moves earlier in time, to the cue (Figure 3.6 in the chapter). The signal is about surprise, and surprise moves to wherever the new information first arrives.

Dopamine says that learning should happen now. It does not say what should be learned, or which neurons were responsible.

## The credit assignment problem

When an action succeeds or fails, which internal components deserve the credit or blame?

In an artificial network this is solved by construction: the architecture is layered, the objective is explicit, the correct answer is supplied, and backpropagation computes each weight's exact contribution to the error.

The brain has none of those conditions. It receives no labels. Outcomes are delayed, noisy, and ambiguous. Circuits are recurrent and overlapping, and each neuron takes part in many functions at once. By the time an outcome is known, the activity that caused it has been overwritten.

The chapter's claim is stronger than "this is hard." It says the question "which synapse caused this?" often has no well-defined answer. Credit assignment in the brain is ill-posed, not merely unsolved.

## Eligibility traces: the physical workaround

If a global signal cannot identify the responsible synapse, how does any specificity arise?

Each synapse keeps a short-lived chemical memory of its own recent activity. When a synapse is used, molecular processes put it into a transient modifiable state, an eligibility trace, which decays over seconds. If a neuromodulatory signal arrives while the trace is still present, the synapse changes. If the signal arrives after the trace has faded, nothing happens.

This produces what is often called a three-factor learning rule:

change in strength = (learning rate) x (eligibility trace at the moment the signal arrives) x (prediction error)

Factor one and two are local to the synapse and say "I was recently involved." Factor three is global and says "something significant just happened." Neither factor alone is enough. The trace is the brain's answer to the temporal gap between action and outcome, and it supplies the locality that volume transmission cannot.

## Bias, not optimization

Each update is small and probabilistic. A synapse that was active by coincidence just before a reward will be strengthened a little too, and nothing prevents that. Over many trials, however, synapses that genuinely tend to precede success accumulate more strengthening than synapses that were merely present.

The result is a bias: a statistical tendency toward activity patterns that have tended to work. The chapter is careful with the word. Bias here is not an error term to be minimized. It is the mechanism. The brain does not descend a loss function; it shifts probabilities.

## The other neuromodulators regulate how, not what

Dopamine is one of several systems, and the chapter frames the others by the kind of context they supply:
- Norepinephrine: alertness and responsiveness, especially under uncertainty or surprise.
- Serotonin: stability, patience, damping of impulsive reaction.
- Acetylcholine: attention, and the balance between encoding new information and retrieving stored information.

Together they regulate the mode of processing rather than its content.

## Reference: the four major neuromodulatory systems

The chapter names the systems by their chemistry and their role but not by their anatomy. Use this table for Lab 3.5 and as a lookup when later chapters refer to a nucleus by name.

| System | Source nuclei (location) | Main targets | Context it signals | Typical timescale |
|---|---|---|---|---|
| Dopamine (dopaminergic) | Ventral tegmental area and substantia nigra pars compacta (midbrain) | Striatum, nucleus accumbens, prefrontal cortex | Reward prediction error; salience of unexpected events | Phasic bursts and dips of about 100 ms to 1 s on a slowly varying tonic level |
| Norepinephrine (noradrenergic) | Locus coeruleus (pons) | Almost the entire cortex, hippocampus, thalamus, cerebellum | Arousal, surprise, uncertainty; a signal to reset or re-engage networks | Phasic responses of hundreds of ms; tonic level shifts over minutes |
| Serotonin (serotonergic) | Raphe nuclei, chiefly the dorsal and median raphe (brainstem) | Widespread cortex, hippocampus, striatum, amygdala | Patience and waiting, mood and stability, damping of impulsive responses | Seconds to minutes; among the slowest modulatory signals |
| Acetylcholine (cholinergic) | Basal forebrain (nucleus basalis of Meynert, medial septum) for cortex and hippocampus; pedunculopontine and laterodorsal tegmental nuclei for thalamus and brainstem | Cortex, hippocampus, thalamus | Attention and expected uncertainty; the balance between encoding new information and retrieving stored information | Seconds, with faster local release in cortex |

Two cautions. First, every one of these chemicals is also used in fast, point-to-point synapses somewhere in the nervous system; the table describes their modulatory role, which is the chapter's subject. Second, the "context" column is a summary of current understanding, not a settled fact. Serotonin in particular has several proposed roles, and the chapter commits only to the broad framing of stability and damping.

## What physically changes

A synapse is a molecular machine, not a gap. Learning can change receptor density, neurotransmitter release probability, the protein scaffolding that holds the synapse together, the shape of the dendritic spine, and gene expression in the cell. "Memory" is a change in structure and in probability, carried forward because structure persists.

## Neuromodulation as the gatekeeper of plasticity

If synapses changed every time neurons fired, the brain would be unstable: every stray coincidence would be learned and every memory would be overwritten by ongoing activity. Separating activity from learning, and gating learning on chemical context, is the chapter's candidate design principle for biological intelligence.

The clinical evidence supports it. Drugs, neuromodulatory disorders, and deep brain stimulation change learning and behavior dramatically without rewiring circuits, by changing the chemical context those circuits operate in.

## Implications for artificial intelligence

The chapter draws four lessons for AI design:
1) Separating activity from learning improves stability. Not every forward pass should be a learning opportunity.
2) Learning rules themselves should depend on state: uncertainty, novelty, and context should modulate how much the system updates.
3) Approximate credit assignment can be sufficient. Probabilistic biasing over time produces robust behavior without exact gradients.
4) The goal of biological learning is viability under uncertainty, not minimization of a loss. Success is defined operationally.

## Practical summary

- Fast synaptic signaling moves information; slow neuromodulation sets the chemical context in which that information is processed.
- Neuromodulatory nuclei are small and project diffusely because the signal they carry is global by nature.
- Dopamine encodes reward prediction error. Predicted rewards produce no response; the response migrates to the earliest predictive cue.
- The brain cannot solve credit assignment precisely; the question is often ill-posed.
- Eligibility traces plus a global modulatory signal form a three-factor rule that bridges the gap between action and outcome.
- Updates are small and probabilistic; learning is the accumulation of bias, not the descent of a loss function.
- Plasticity is gated. Nothing changes unless context says it should.

# Labs

## Lab Notes: how to succeed in these labs

These labs continue the approach of Chapter 2: you will treat learning as a constrained dynamical process and simulate it in simplified form with pencil, paper, dice, and small calculations. Where a lab offers an optional code extension, it is deliberately short; the point is to see the mechanism, not to build a simulator.

General rules:
1) Work in steps. Write intermediate values.
2) Draw the system before computing.
3) Finish every lab with an interpretation: what changes if the parameters change, and what does the biology gain or lose?

### What to hand in for every lab

- A clean diagram (a photo of a hand drawing is fine).
- A calculation table.
- A short interpretation (6-12 sentences).

## Lab 3.1 - Reward Prediction Error by Hand (why dopamine moves to the cue)

### Purpose

To reproduce, numerically, the two signature findings in Figures 3.5 and 3.6 of the chapter: the dopamine response to a reward shrinks as the reward becomes predictable, and the response reappears at the cue that predicts it.

### Materials

Notebook, pen or pencil, calculator (recommended).

### Given parameters (use exactly these)

Prediction V (how much reward the cue predicts) starts at V = 0.
Reward on every trial: r = 1.
Learning rate: alpha = 0.25.
Prediction error at the reward: delta = r - V.
Update after each trial: V_new = V + alpha * delta.
Treat the dopamine response at the reward as delta, and the dopamine response at the cue as V (the amount of reward the cue now predicts).

### Setup diagram (do this first)

1) Draw a timeline for one trial: a cue at t = 0 s, a reward at t = 2 s.
2) Above the timeline, leave space for two bars: "dopamine at cue" and "dopamine at reward."

### Procedure (follow in order)

Part A - Learning the prediction

1) Make a table with columns: trial, V before, delta at reward, V after, dopamine at cue.
2) Trial 1: V = 0, so delta = 1 - 0 = 1.0. V after = 0 + 0.25 * 1.0 = 0.25. Dopamine at cue = 0.
3) Trial 2: delta = 1 - 0.25 = 0.75. V after = 0.4375. Dopamine at cue = 0.25.
4) Continue through trial 8. You should find V after trial 8 is about 0.90 and delta at the reward has fallen to about 0.13.
5) Draw the two bars for trial 1 and for trial 8 on your diagram.

Part B - Omission

6) On trial 9 the cue appears but no reward is delivered (r = 0).
7) Compute delta = 0 - V. Record its sign and size.
8) Update V as usual and note what happened to the prediction.

Part C - Sensitivity check

9) Repeat Part A with alpha = 0.05 for 8 trials. How far does V get?
10) Repeat Part A with alpha = 0.9 for 4 trials. What does the sequence of delta values look like?
11) Write 6-10 sentences: why does a reliable reward become "invisible" to dopamine, where did the signal go, and what does the omission dip tell the rest of the brain?

### What to record

Table for Parts A through C, the two-bar diagrams for trial 1 and trial 8, and your interpretation.

## Lab 3.2 - Eligibility Traces and the Temporal Gap (three-factor rule)

### Purpose

To see why a global, late-arriving signal can still produce synapse-specific learning, and what is lost when the delay between activity and outcome grows.

### Given parameters

When a synapse is active, its eligibility trace is set to e = 1.0.
The trace halves every 1 s if the synapse is not reactivated (so after d seconds, e = 0.5^d).
Learning rate: eta = 0.1.
Prediction error carried by dopamine: delta = +0.8 (unless stated otherwise).
Three-factor update at the moment dopamine arrives: delta_w = eta * e * delta.

### Setup

1) Draw one postsynaptic neuron with three input synapses labeled S1, S2, S3.
2) Draw a dopaminergic axon passing over all three (volume transmission: it cannot single any of them out).

### Procedure

Part A - One synapse, varying delay

1) S1 is active once at t = 0. Dopamine arrives at t = d.
2) Compute e(d) and delta_w for d = 0, 1, 2, 3, 5, and 10 s. Enter them in a table.
3) Mark the delay beyond which delta_w is below 0.01 (effectively no learning).

Part B - Three synapses, one outcome

4) S1 is active at t = -1 s, S2 at t = -4 s, S3 at t = -8 s. Dopamine arrives at t = 0.
5) Compute the three traces at t = 0 and the three updates.
6) Express the result as a ratio delta_w(S1) : delta_w(S2) : delta_w(S3).

Part C - Negative error

7) Repeat Part B with delta = -0.6 (outcome worse than expected). Which synapses weaken most?

Part D - A trace that never decays

8) Suppose the trace stayed at 1.0 forever. Recompute Part B.
9) Now suppose 50 unrelated synapses were each active at some point during the previous hour. What happens to them when dopamine arrives?
10) Write 8-12 sentences: what does the decay constant buy the organism, what does it cost, and why can the dopaminergic axon be so unselective without destroying specificity?

### Optional code extension (Python, about 15 lines)

Write a loop that, for a synapse active at t = 0, computes e(t) every 0.5 s with exponential decay, and prints delta_w for dopamine arrival at each step. Then change the half-life to 3 s and to 0.3 s and compare how far the organism can "reach back" to credit an action.

## Lab 3.3 - Credit Assignment Under Uncertainty (a dice-driven learner)

### Purpose

To experience credit assignment as the brain faces it: no labels, noisy outcomes, overlapping activity, and a single global signal that cannot name the responsible synapse.

### Given model

Four synapses, S1 to S4, each with starting strength w = 0.
On each trial every synapse is independently active with probability 1/2 (die roll of 4, 5, or 6 = active).
Hidden rule (the "truth," which the learner never sees): S1 is the causal synapse. If S1 is active, reward occurs unless the outcome die shows 1. If S1 is inactive, reward occurs only if the outcome die shows 6.
The learner's prediction is fixed at V = 0.5, so delta = r - 0.5 = +0.5 after reward and -0.5 after no reward.
Three-factor update, applied to every synapse that was active on the trial: w = w + 0.1 * delta. Inactive synapses have no trace and do not change.

### Procedure

1) Draw the four synapses converging on one neuron, with a dopaminergic axon broadcasting to all four.
2) Make a table with columns: trial, roll S1-S4, active set, outcome roll, reward, delta, w1, w2, w3, w4.
3) Run 12 trials. Either roll your own dice, or use the pre-rolled sequence below so your results can be compared with the class.
4) After each trial update only the active synapses.
5) At the end, rank the four synapses by strength.

Pre-rolled sequence (activity rolls S1, S2, S3, S4; then outcome roll):
trial 1: 1, 4, 1, 4; outcome 2
trial 2: 6, 1, 2, 1; outcome 5
trial 3: 2, 6, 2, 2; outcome 6
trial 4: 1, 6, 1, 2; outcome 2
trial 5: 5, 6, 4, 5; outcome 4
trial 6: 2, 5, 1, 1; outcome 1
trial 7: 4, 3, 2, 2; outcome 3
trial 8: 4, 3, 5, 2; outcome 2
trial 9: 6, 2, 4, 5; outcome 6
trial 10: 5, 1, 1, 2; outcome 3
trial 11: 2, 2, 2, 4; outcome 1
trial 12: 1, 6, 5, 4; outcome 6

Check: with this sequence, after 12 trials you should have w1 = 0.30, w2 = 0.00, w3 = 0.20, w4 = 0.05.

6) Notice that S3 ended with substantial strength although it has no causal role. Find the trials on which it was rewarded, and check whether S1 was also active on those trials.
7) Write 8-12 sentences: did the learner find the causal synapse? Why did S3 get credit it did not deserve? Is that a bug, and what would happen to S3 over 100 more trials? Relate your answer to the chapter's phrase "bias as a learning strategy."

### Optional code extension (Python, about 25 lines)

Simulate the same model for 1,000 trials with random rolls and plot the four strengths over time. Then make the outcome noisier (reward with probability 0.6 when S1 is active, 0.4 when inactive) and see how many trials it takes for S1 to separate from the others. The brain lives at the noisy end of this spectrum.

## Lab 3.4 - Gated Versus Ungated Plasticity (why activity alone must not cause learning)

### Purpose

To make the chapter's design principle concrete: if synapses changed whenever neurons fired, the system would be unstable.

### Given parameters

One synapse between neuron A and neuron B, starting strength w = 0.2.
Over 10 trials, A and B happen to fire together on every trial (a coincidence driven by shared input noise, not by any useful relationship).
Ungated (Hebbian) rule: whenever A and B fire together, w = w + 0.1.
Gated (three-factor) rule: w = w + 0.1 * delta, where delta is the prediction error on that trial.
Prediction errors for the 10 trials: 0, 0, 0, +0.5, 0, 0, 0, 0, -0.5, 0.

### Procedure

Part A - Coincidence without consequence

1) Run the 10 trials under the ungated rule. Record w after each trial.
2) Run the same 10 trials under the gated rule. Record w after each trial.
3) Compare the two final strengths.

Part B - A real relationship

4) Repeat both rules with prediction errors of +0.5 on every trial (the coactivity now reliably precedes success).
5) Compare the final strengths again.

Part C - Scaling up

6) Suppose the neuron has 5,000 synapses and, by chance, 100 of them show coincident activity on any given trial. Under the ungated rule, how many synapses change per trial? Over 1,000 trials? Under the gated rule with delta = 0 on 90 percent of trials?
7) Write 8-12 sentences: what does gating protect against, what does it cost (think of a genuinely useful coincidence that occurs when delta happens to be zero), and how does this relate to the chapter's claim that "nothing changes unless the context says it should"?

## Lab 3.5 - Neuromodulators as Design Primitives (comparison table and concept map)

### Purpose

To integrate the chapter's four modulatory systems and its argument about artificial intelligence into one explicit comparison.

### Procedure

Part A - Comparison table

1) Make a table with four rows: dopamine, norepinephrine, serotonin, acetylcholine.
2) Add six columns: source region (from the reference table in the Student Notes), what context it signals, typical timescale, effect on plasticity, effect on ongoing processing, and the nearest artificial-learning analogue (for example: reward prediction error term, exploration temperature, learning-rate schedule, attention weighting).
3) Fill every cell with a short concrete statement. Mark any cell where you are guessing.

Part B - Concept map

4) Draw a circuit: a sensory input, a decision neuron, an action, and an outcome.
5) Add a dopaminergic neuron that compares outcome with prediction and broadcasts delta back over the circuit.
6) Add eligibility traces at the synapses as small clocks that start when the synapse is used.
7) Add one gate symbol at each synapse: it opens only when delta is nonzero and the clock has not run out.
8) Add a norepinephrine arrow that widens the gate under surprise, and an acetylcholine arrow that selects encoding versus retrieval.
9) Write an 8-12 sentence caption that tells the story of one trial through your diagram.

Part C - Design memo

10) In 10-14 sentences, argue for or against adding a neuromodulation-like layer to an artificial agent that must learn in an open-ended environment with delayed, noisy feedback. Address stability, credit assignment, and what you would lose compared with backpropagation. Use at least two of the chapter's four implications for AI.
