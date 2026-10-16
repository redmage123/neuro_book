---
title: "Chapter 2 Student Notes and Labs"
subtitle: "Neurons: The Brain's Signaling Cells"
---

# Student Notes

## What this chapter is for

Chapter 2 gives you a working, mechanistic model of a neuron: a living physical system that receives chemical inputs, integrates them in space and time, and sometimes generates a spike that travels along an axon to influence other cells.

If you are coming from software, engineering, or math, this chapter is designed to correct three common instincts:
1) treating neurons like logic gates,
2) imagining signals as clean "packets" that move through a pipeline, and
3) assuming the system's main goal is correctness rather than viability.

Your goal is not to memorize vocabulary. Your goal is to be able to explain, in plain language, how inputs at synapses can change a neuron's probability of firing, how a spike propagates, and why learning has to be implemented as physical change.

## The parts of a neuron, and what each part is for

A typical neuron is polarized: many inputs, one output.
- Dendrites: where most synaptic inputs arrive. Dendrites are not just "wires." Their geometry and membrane properties shape how signals decay and combine.
- Soma (cell body): the integration hub and metabolic center.
- Axon initial segment (AIS): the spike trigger zone with a high density of voltage-gated sodium channels.
- Axon: the transmission line built to regenerate a signal repeatedly.
- Axon terminals: the output interface that converts a spike into chemical release.

You should be able to say: dendrites and soma integrate; the AIS decides; the axon transmits.

## What counts as an input to dendrites

The immediate input to a dendrite is usually chemical.
At a chemical synapse, a presynaptic neuron releases neurotransmitter molecules into the synaptic cleft. Those molecules bind to receptors on the postsynaptic membrane. Receptor activation changes ion flow across the membrane, producing a local change in voltage.

That local voltage change is a postsynaptic potential. It is graded, local, and temporary.

## EPSPs and IPSPs: excitation and inhibition in plain terms

Synaptic inputs come in two broad functional flavors:
- EPSP (excitatory postsynaptic potential): nudges the membrane potential upward (toward threshold).
- IPSP (inhibitory postsynaptic potential): nudges the membrane potential downward (away from threshold) or stabilizes it.

A neuron's firing is governed by the balance of EPSPs and IPSPs over time. Inhibition is not a mere "brake"; it is a core part of computation and stabilization.

## Integration is passive: why location and timing matter

Postsynaptic potentials spread through dendrites and soma mostly passively.
1) Distance matters: far synapses often have less influence at the soma/AIS than near synapses.
2) Timing matters: inputs that arrive close together can sum before they decay.

This is why neurons do not behave like crisp boolean logic. They behave like physical integrators whose behavior depends on geometry, membrane properties, and recent history.

## Where spikes start, and why the soma typically does not propagate them

Most spikes start at the AIS. The soma is optimized for integration and maintenance, not for regenerative propagation. In some neurons, spikes can back-propagate into dendrites under some conditions, but the canonical forward spike begins near the AIS and proceeds down the axon.

## Action potential propagation: what travels

A spike does not propagate because ions physically travel from the AIS to the terminals like current in a wire. Propagation works as a chain reaction along the membrane:
- Segment 1 depolarizes past threshold and opens its own channels.
- That depolarization spreads locally to segment 2.
- Segment 2 reaches threshold and opens its own channels.
- Segment 1 becomes refractory, preventing immediate re-firing.

What travels is a pattern of membrane state change, regenerated at each step.

## Coding: where information lives

Spikes are all-or-nothing events with fairly stereotyped amplitude. Information tends to live in:
- timing (precise spike times),
- rate (how often spikes occur),
- patterns across populations,
- and context (neuromodulatory state).

## Plasticity: why learning must be physical

A neuron cannot store a variable the way a computer can. Learning is implemented as physical change: synaptic strengthening/weakening, receptor changes, structural remodeling, and changes in intrinsic excitability.

Memory persists because structure persists.

## Practical summary

\- Dendrites receive chemical inputs that produce graded voltage changes (EPSPs/IPSPs).
- Those voltage changes sum in space and time, decaying with distance and time.
- If the AIS crosses threshold, the neuron generates a spike.
- The spike propagates by local regeneration along the axon.
- Learning occurs when synapses and cellular properties change physically.

# Labs

## Lab Notes: how to succeed in these labs

These labs are designed for technically trained readers. You will treat a neuron like a constrained dynamical system and simulate it in simplified form with pencil-and-paper and small calculations. The aim is explicit reasoning about decay, timing, balance of excitation/inhibition, and regenerative propagation.

General rules:
1) Work in steps. Write intermediate values.
2) Draw the system.
3) Finish with an interpretation: what changes if parameters change?

### What to hand in for every lab

\- A clean diagram (photo is fine if hand-drawn).
- A calculation table.
- A short interpretation (6-12 sentences).

## Lab 2.1 - Spatial and Temporal Summation (manual integrate-and-fire)

### Purpose

To feel, numerically, why neurons must integrate many weak synaptic inputs, and why location and timing change the outcome even if the number of inputs is the same.

### Materials

Notebook, pen/pencil, calculator (recommended).

### Given parameters (use exactly these)

V_rest = -70 mV
V_th = -55 mV
EPSP at synapse location A_E = +0.4 mV
Spatial decay: each distance unit halves the effect at the soma/AIS
Temporal decay: each EPSP halves after 10 ms if not reinforced
Time step: 5 ms

### Setup diagram (do this first)

1\) Draw a soma as a circle.
2) Draw three dendritic branches:
Branch A: distance unit 1
Branch B: distance unit 2
Branch C: distance unit 3
3) Mark the AIS as a small segment emerging from the soma.

### Procedure (follow in order)

Part A - Spatial summation, simultaneous inputs

1) Place 4 excitatory synapses on Branch A, 4 on Branch B, 4 on Branch C (12 total).
2) Compute effective EPSP at AIS using spatial decay:
Branch A: 0.4 \* (1/2)\^1 = +0.20 mV
Branch B: 0.4 \* (1/2)\^2 = +0.10 mV
Branch C: 0.4 \* (1/2)\^3 = +0.05 mV
3) Compute total depolarization if all 12 fire at the same instant:
DeltaV = 4\*(0.20) + 4\*(0.10) + 4\*(0.05)
4) Compute V_now = V_rest + DeltaV.
5) Record whether V_now crosses threshold (\>= -55 mV).

Part B - Temporal summation, staggered inputs

6) Reset: V_now = -70 mV.
7) Schedule inputs in three bursts:
t = 0 ms: Branch A synapses fire
t = 10 ms: Branch B synapses fire
t = 20 ms: Branch C synapses fire
8) Apply temporal decay between bursts (halve after 10 ms):
V(t+10) = V_rest + 0.5\*(V(t) - V_rest) + (new inputs at t+10)
9) Compute V_now at t=0, t=10, t=20.
10) Record if threshold is reached at any time.

Part C - Sensitivity check

11) Move two Branch C synapses to Branch A (A has 6; C has 2).
12) Repeat Part B computations.
13) Write 6-10 sentences: what changed and why?

### What to record

Diagram, time-by-time table, and spike/no-spike decisions.

## Lab 2.2 - Excitation-Inhibition Competition (EPSPs vs IPSPs with timing)

### Purpose

To show that inhibition can dominate outcome depending on timing and location.

### Given parameters

Use Lab 2.1 values plus:
IPSP at synapse location A_I = -0.6 mV
Assume inhibitory synapses start at distance unit 1
Same temporal decay rule (halve after 10 ms)
Time step: 5 ms

### Setup

1\) Place 10 excitatory synapses on Branch A (distance unit 1).
2) Place 6 inhibitory synapses near the soma (distance unit 1).

### Procedure

Part A - Excitation alone

1) Effective EPSP at AIS: +0.4 \* 0.5 = +0.20 mV.
2) At t=0, fire all 10 EPSPs: DeltaV_E = 10\*(+0.20).
3) V_now = V_rest + DeltaV_E. Record spike/no-spike.

Part B - Simultaneous inhibition

4) Effective IPSP at AIS: -0.6 \* 0.5 = -0.30 mV.
5) At t=0, fire 6 IPSPs with EPSPs: DeltaV_I = 6\*(-0.30).
6) V_now = V_rest + DeltaV_E + DeltaV_I. Record spike/no-spike.

Part C - Inhibition arrives early

7) Reset to V_rest.
8) t=0: fire IPSPs only. Compute V(0).
9) t=10 ms: decay toward rest: V(10-) = V_rest + 0.5\*(V(0)-V_rest).
10) t=10 ms: fire EPSPs. Compute V(10+). Record spike/no-spike.

Part D - Location change

11) Move inhibitory synapses to distance unit 2.
12) Recompute effective IPSP and redo Part C only.
13) Write 8-12 sentences: why did timing and location matter so much?

## Lab 2.3 - Action Potential Propagation (state machine walk-through)

### Purpose

To understand propagation as local regeneration with refractoriness.

### Given model

Model an axon as 12 discrete segments. Each segment state:
R = Resting, A = Active, F = Refractory
Rule: if segment i is A at time t, then at t+1:
- segment i becomes F
- segment i+1 becomes A (unless it is F)
- F lasts exactly one step (F -\> R next step)

### Procedure

1\) Draw 12 boxes labeled 1-12.
2) Make a table with rows t=0..14 and columns 1..12.
3) Initialize: at t=0, segment 1 = A, all others = R.
4) Apply the rule step-by-step to fill the table.
5) At t=6, force segment 8 to be F (a temporary block).
6) Continue and note what happens when the wave reaches segment 8.
7) Write 8-12 sentences interpreting reliability, what travels, and what refractoriness prevents.

## Lab 2.4 - Engineering trade-offs: correctness vs viability

### Purpose

To make constraints explicit by comparing optimization targets.

### Procedure

1\) Make a 3-column table: Neuron, CPU, Packet Network.
2) Add at least 8 rows: speed, energy/op, fault tolerance, noise strategy, learning, reset, repair, objective.
3) Fill each cell with a short concrete statement.
4) Pick two rows where the neuron looks worst.
5) Write 10-14 sentences explaining why those weaknesses are adaptive.

## Lab 2.5 - Full causal concept map (from synapse to learning)

### Purpose

To integrate chemical input -\> graded potentials -\> spike decision -\> propagation -\> output -\> plasticity.

### Procedure

1\) Draw a neuron with labeled parts: dendrites, soma, AIS, axon, terminals.
2) Add 4 synapses: 2 excitatory, 2 inhibitory.
3) Draw arrows for: neurotransmitter release -\> receptor binding -\> EPSP/IPSP -\> summed V at AIS -\> spike -\> terminal release.
4) Add one plasticity loop: repeated co-activation -\> stronger synapse.
5) Add one stabilization loop: increased excitation -\> increased inhibition -\> stabilized firing.
6) Write an 8-12 sentence caption that tells the story of your diagram.
