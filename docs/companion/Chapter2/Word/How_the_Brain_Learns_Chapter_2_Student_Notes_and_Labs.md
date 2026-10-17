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

## A neuron is a cell

A neuron is bounded by a membrane about five nanometers thick separating two salt solutions: potassium concentrated inside, sodium outside. The sodium-potassium pump moves three sodium ions out and two potassium ions in per molecule of ATP, and because the resting membrane leaks potassium more easily than sodium, the inside sits about 70 millivolts negative: the resting potential. Every signal is a brief departure from it, and most of the gray matter's energy budget goes to pumping back the ions that signaling lets through (Attwell and Laughlin).

## The parts of a neuron, and what each part is for

A typical neuron is polarized: many inputs, one output (Cajal's law of dynamic polarization). The numbers are lopsided: a CA1 pyramidal neuron carries about 30,000 excitatory and 1,700 inhibitory synapses (Megías and colleagues), a Purkinje cell on the order of 200,000, and all of them are reduced to one axon carrying one signal.
- Dendrites: where most synaptic inputs arrive. Dendrites are not just "wires." Their geometry sets how signals decay and combine, and their voltage-gated channels and NMDA receptors let them generate local dendritic spikes.
- Soma (cell body): holds the nucleus and metabolic machinery and sums what the dendrites deliver. It has a low density of sodium channels, so it relays rather than decides.
- Axon initial segment (AIS): the spike trigger zone, the first few tens of micrometers of the axon, with a sodium-channel density about fifty times that of the nearby dendrites (Kole and colleagues).
- Axon: the transmission line built to regenerate a signal repeatedly, myelinated in long-range axons and mostly unmyelinated locally in cortex.
- Axon terminals: the output interface that converts a spike into chemical release.

You should be able to say: dendrites integrate (with active parts of their own), the soma relays, the AIS decides, and the axon transmits, while the spike also travels back into the dendrites to tell the synapses that the neuron fired.

## What counts as an input to dendrites

The immediate input to a dendrite is usually chemical.
At a chemical synapse, a presynaptic neuron releases neurotransmitter molecules into the synaptic cleft. Those molecules bind to receptors on the postsynaptic membrane. Receptor activation changes ion flow across the membrane, producing a local change in voltage.

That local voltage change is a postsynaptic potential. It is graded, local, and temporary. Loewi's 1921 frog-heart experiment showed that the message is chemical: fluid from a heart slowed by vagus stimulation slowed a second heart.

Not every synapse is chemical. Electrical synapses (gap junctions), common between inhibitory interneurons, connect two cells' interiors directly, with no transmitter and almost no delay; they help synchronize activity, and mice lacking connexin 36 show weakened gamma oscillations (Connors and Long).

## Quanta, failures, and noise

Transmitter is released in fixed packets, quanta, each the contents of one vesicle. Fatt and Katz (1952) saw spontaneous half-millivolt events at the frog neuromuscular junction, and del Castillo and Katz (1954) found that in low calcium the evoked response fluctuated in steps of that size, with counts following the statistics of independent random events. In the brain an impulse often releases one vesicle or none: more than half of impulses at single hippocampal synapses fail (Allen and Stevens), and in connected cortical pyramidal pairs the response's standard deviation is about half its mean (Markram and colleagues). A neuron's input is a sample from a distribution, not a clean number.

## EPSPs and IPSPs: excitation and inhibition in plain terms

Synaptic inputs come in two broad functional flavors:
- EPSP (excitatory postsynaptic potential): nudges the membrane potential upward (toward threshold).
- IPSP (inhibitory postsynaptic potential): nudges the membrane potential downward (away from threshold) or stabilizes it.

A neuron's firing is governed by the balance of EPSPs and IPSPs over time. Inhibition is not a mere "brake"; it is a core part of computation and stabilization.

Real synaptic potentials are small: Markram and colleagues measured an average of 1.3 millivolts at the soma (about 0.15 to 5.5 across connections), and Song and colleagues found a long-tailed distribution with most connections weak. Threshold is about 15 millivolts above rest, so tens of coincident inputs are needed.

The chapter's worked example: with 0.5-millivolt EPSPs, 30 inputs arriving within a couple of milliseconds sum to 15 millivolts and fire the cell. Spread over a tenth of a second with a 20-millisecond time constant, the same 30 give only about 3 millivolts on average (rate times size times time constant). Add ten 1-millivolt IPSPs to the burst and about 50 EPSPs are needed. What drives a neuron is how many inputs are active together, and against how much inhibition.

## Integration: a passive baseline and active dendrites

The baseline is Rall's cable theory: treated as a passive cable, a dendrite attenuates a voltage change and smears it in time as it spreads toward the soma.
1) Distance matters: far synapses often have less influence at the soma and AIS than near synapses (some neurons partly compensate by making distal synapses stronger).
2) Timing matters: inputs that arrive close together can sum before they decay.

For small, scattered inputs this passive account is a good approximation. But dendrites are not passive cables. They carry voltage-gated sodium, calcium, and potassium channels and NMDA receptors, and they can fire their own regenerative events:
- NMDA spikes: enough coactive neighboring synapses on a thin basal branch trigger a local plateau lasting tens of milliseconds, confined to that branch (Schiller and colleagues, 2000).
- Calcium spikes: a zone near the top of the apical dendrite of layer 5 pyramidal neurons fires broad calcium spikes that drive bursts of output (Larkum, Zhu, and Sakmann).

So a dendrite is a set of semi-independent compartments, each able to detect when its own inputs coincide and to amplify them: roughly linear for weak, scattered input and nonlinear when inputs cluster. Dendritic spikes also matter for learning: distal CA1 synapses can be strengthened by a local dendritic spike even when the neuron does not fire (Golding, Staff, and Spruston). This is why neurons do not behave like crisp boolean logic: their behavior depends on geometry, active membrane properties, and recent history.

## Where spikes start, and where they go

Spikes start at the AIS, not the soma. Eccles's group inferred this in 1957 from spinal motor neurons, and Palmer and Stuart located the origin in cortical pyramidal neurons about 35 micrometers down the axon. The soma has a low sodium-channel density and does not initiate the spike.

Once initiated, the spike travels both ways. It runs forward down the axon, and it invades the soma at full amplitude and actively back-propagates into the dendrites, carried by the dendrites' own voltage-gated sodium channels rather than merely leaking into them (Stuart and Sakmann, 1994). Back-propagation weakens with distance, can fail in the finest distal branches, and is regulated by potassium channels and inhibition, but over much of the tree it tells each synapse that the neuron has just fired. That report is how a synapse learns whether its input helped: Chapter 5 shows the back-propagating spike relieving the NMDA receptor's magnesium block. It also couples inputs: a back-propagating spike coinciding with weak distal apical input can trigger a dendritic calcium spike and a burst (Larkum and colleagues).

## Action potential propagation: what travels

A spike does not propagate because ions physically travel from the AIS to the terminals like current in a wire. Propagation works as a chain reaction along the membrane:
- Segment 1 depolarizes past threshold and opens its own channels.
- That depolarization spreads locally to segment 2.
- Segment 2 reaches threshold and opens its own channels.
- Segment 1 becomes refractory, preventing immediate re-firing.

What travels is a pattern of membrane state change, regenerated at each step. Nothing travels the length of the axon except causation.

The mechanism (Hodgkin and Huxley): past threshold, sodium channels open and the inflow opens more (positive feedback, to about +40 millivolts); within a millisecond they inactivate while slower potassium channels repolarize the membrane. The refractory period of a millisecond or two makes propagation one-way and limits firing to a few hundred impulses per second.

Myelin changes the speed. In a myelinated axon sodium channels are concentrated at the nodes, and the spike jumps from node to node (saltatory conduction, shown by Huxley and Stämpfli in 1949). The fastest myelinated axons conduct at about 100 meters per second, against about 1 meter per second for thin unmyelinated fibers, and at lower metabolic cost.

## Coding: where information lives

Spikes are all-or-nothing events with fairly stereotyped amplitude. Adrian and Zotterman (1926) showed that a heavier weight on a stretch receptor produced more impulses per second, not larger ones. Information tends to live in:
- timing (precise spike times; Mainen and Sejnowski showed millisecond-reproducible timing to fluctuating input),
- rate (how often spikes occur),
- patterns across populations,
- and context (neuromodulatory state).

Speed argues against pure rate codes: if an animal-detection signal appears about 150 milliseconds after a flash (Thorpe and colleagues) and passes through about ten stages, each stage has time for one spike or none. How circuits weigh rate, timing, and synchrony is an active research question.

One qualification to all-or-none: small changes in spike shape modulate release. Terminal spikes in hippocampal mossy fibers broaden up to threefold during high-frequency firing (Geiger and Jonas), and subthreshold somatic voltage spreads down the axon and changes how much each later spike releases (Alle and Geiger; Shu, McCormick, and colleagues). The axon carries a mainly digital signal with an analog component.

## Plasticity: why learning must be physical

A neuron cannot store a variable the way a computer can. Learning is implemented as physical change: synaptic strengthening/weakening, receptor changes, structural remodeling, and changes in intrinsic excitability.

Memory persists because structure persists.

Hebb proposed the rule in 1949; Bliss and Lømo found long-term potentiation (LTP) in the rabbit hippocampus in 1973. What changes is physical: more transmitter per impulse, more receptors, and a larger spine (Matsuzaki, Kasai, and colleagues showed that potentiating a single spine also enlarges it). The synapse that stores a past experience is the same one that transmits the next impulse, so every use of a memory runs through, and may alter, the stored change. Chapter 5 develops this.

## Why neurons look inefficient, and why they are not

Judged as switches, neurons are slow (a spike lasts about a millisecond, about ten million times longer than a 100-picosecond transistor switch), noisy, and expensive (about 2 percent of body mass, about 20 percent of resting energy). Noise even sets a floor on wiring: axons thinner than about a tenth of a micrometer would fire spontaneously from single-channel noise (Faisal, White, and Laughlin). These costs are tolerable because the brain computes with populations (a coincidence of many noisy synapses is a reliable vote), with parallelism, and with elements that rewire themselves while they work. Sterling and Laughlin argue that, under these constraints, neural design is close to efficient.

## A neuron in context

The same neuron with the same wiring and input can fire very differently depending on its chemical setting: neuromodulators such as dopamine, acetylcholine, and noradrenaline change how neurons fire and how their synapses learn. They decide much of when physical changes are made and kept, and they are the subject of Chapter 3.

## Implications for artificial intelligence

- The McCulloch-Pitts unit (weighted sum and threshold, 1943) is the ancestor of every deep-network unit, but a biological neuron is closer to a small network: Poirazi and Mel modeled a pyramidal cell as a two-layer network of dendritic subunits, and Beniaguev, Segev, and London needed five to eight layers to mimic a cortical neuron (one hidden layer sufficed without NMDA receptors). Human cortical dendrites can compute exclusive-or (Gidon, Larkum, and colleagues), which a single artificial unit cannot.
- The brain sends sparse, all-or-none events whose cost scales with how many are sent, a reason to take event-driven, spiking hardware seriously.
- Synaptic failure may play a role loosely like dropout, though this is an analogy, not an established equivalence.
- Both store knowledge in weights; the difference is how they change. Artificial weights are set by a separate training procedure and fixed during use unless trained online; synapses change during use by local rules, including the back-propagating spike.

## Practical summary

\- Dendrites receive chemical inputs, released in unreliable quanta, that produce small graded voltage changes (EPSPs/IPSPs).
- Those voltage changes sum in space and time, decaying with distance and time in the passive baseline, while clustered inputs can trigger active dendritic spikes.
- If the AIS crosses threshold, the neuron generates a spike; the soma relays rather than decides.
- The spike propagates by local regeneration along the axon (saltatory in myelinated axons) and back-propagates actively into the dendrites, telling synapses the neuron fired.
- Learning occurs when synapses and cellular properties change physically, and neuromodulators shape much of when those changes are made and kept.

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

These parameters model the passive baseline described in the Student Notes; they leave out the active dendritic events (NMDA and calcium spikes) that clustered inputs can trigger.

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
