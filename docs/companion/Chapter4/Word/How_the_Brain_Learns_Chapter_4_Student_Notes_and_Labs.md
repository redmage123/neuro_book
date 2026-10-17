---
title: "Chapter 4 Student Notes and Labs"
subtitle: "Circuits, Networks, and Coordinated Behavior"
---

# Student Notes

## What this chapter is for

Chapters 2 and 3 gave you a neuron and the chemical context that decides when it may change. Chapter 4 moves up one level and makes a claim that reorganizes everything that follows: behavior belongs to circuits, not to cells. A single neuron cannot walk, breathe, decide, or remember. What it can do is take part in a wiring pattern, and the nervous system uses a surprisingly small set of such patterns, at every scale and in every region.

If you are coming from machine learning, this chapter is designed to correct three instincts:
1) treating inhibition as a negative weight,
2) assuming that choosing an action means picking the largest output, and
3) assuming that fixed connections mean fixed information flow.

Your goal is to be able to name the six motifs, say what each one buys the organism, explain why excitation and inhibition are kept in near-cancellation, and describe how the basal ganglia, cerebellum, hippocampus, rhythms, and the brain's wiring plan each solve a coordination problem without a central controller.

## The reflex arc and the first lesson

Sherrington's stretch reflex is two neurons and one synapse: a sensory neuron from the muscle spindle excites a motor neuron to the same muscle. The part that is easy to miss is the inhibitory interneuron on the same sensory axon, which suppresses the motor neurons of the opposing muscle. This is reciprocal inhibition. The first lesson of circuit organization is that useful behavior requires turning things off as much as turning them on.

## The six motifs

You should be able to draw each of these from memory and state what it buys:
- Feedforward excitation: a chain. Transmits, does not shape.
- Feedforward inhibition: input excites a target and, a millisecond or two later, inhibits it through an interneuron. Creates a narrow window; turns an integrator into a coincidence detector.
- Feedback (recurrent) inhibition: the target's own output recruits an interneuron that suppresses the target. A thermostat; the main reason cortex does not explode.
- Lateral inhibition: neighbors suppress each other. Sharpens contrast, produces winner-take-all selection, lets "which neuron" carry information.
- Recurrent excitation: activity feeds back on itself. Sustains patterns after input ends (working memory, pattern completion). The most dangerous motif: uncontained, it is a seizure.
- Disinhibition: inhibition of an inhibitor. The target is off by default and released by an input, so nothing happens unless the circuit is explicitly opened. The basal ganglia are built from it.

## Inhibition is not the opposite of excitation

About one in five cortical neurons is inhibitory, in dozens of types that target different compartments of the excitatory cell. Inhibition on the dendrite vetoes particular inputs; on the soma it vetoes output; on the axon initial segment it controls spike timing.

The central fact is balance. In awake cortex, every excitatory input is tracked a few milliseconds later by a nearly equal inhibitory input. The neuron sits close to threshold, held there by two large forces that almost cancel. This is expensive (two big currents spent for a small net effect) and it is the only regime in which the circuit is both sensitive and stable. It also makes the circuit fast: a neuron near threshold can be flipped by one well-timed input.

Figure 4.2 simulates the same recurrent excitatory population three times. With no inhibition, the population is quiet until a brief input arrives; the input then tips it into a runaway to the ceiling that outlasts the input. With balanced inhibition the response is brief and proportionate, and with excessive inhibition the input barely registers.

You should be able to say: inhibition is not the brake; it is what makes the system responsive.

## Computation before the brain

The retina processes the image through three layers of circuitry before the optic nerve leaves the eye. Horizontal cells apply lateral inhibition across the photoreceptor layer, so edges produce strong output and uniform regions produce little. Amacrine cells add temporal sensitivity. What leaves the eye is a map of edges and changes, not a copy of the image. Mach bands, described by Ernst Mach in 1865 and shown in Figure 4.4, are lateral inhibition made visible: on a staircase of uniform gray steps, each step looks lighter at its border with the darker step and darker at its border with the lighter one. A cell just on the bright side of an edge is inhibited by fewer bright neighbors than a cell in the middle of the step, so it fires more; a cell just on the dark side is inhibited by more, so it fires less. The bands are a trade of fidelity for information under a strict budget of axons.

## Central pattern generators

Walking, swimming, breathing, chewing, and gut peristalsis are rhythmic, and the rhythm is generated by small spinal and brainstem networks without any rhythmic input. The minimal version is the half-center oscillator: two populations that inhibit each other and fatigue while active. The active side tires, loses its grip, the other side escapes, and the cycle repeats. A constant drive produces alternation. Sensory feedback tunes the rhythm (a stone underfoot) but does not drive it. The chapter quotes Chapter 1: "The brain generates behavior, and the world corrects it."

## The cortical microcircuit

Neocortex, the six-layered kind (older regions such as the hippocampus have three layers), is a sheet built from one six-layered circuit repeated with only local variations. Thalamic input arrives mainly in layer 4; layer 4 projects to layers 2 and 3 (local processing, connections to other areas); layers 2 and 3 project to layer 5 (output to brainstem, spinal cord, basal ganglia); layer 6 projects back to the thalamus. Every motif from the list above is present inside this stack. Vertically, neurons that share inputs form columns. The chapter's inference: the same circuit learns to see or to hear depending on where its input comes from, which is the strongest anatomical hint that cortical computation is general. In ferrets whose retinal axons were rerouted during development into the auditory pathway, auditory cortex came to respond to visual input, and the adult animals responded to light through it.

## Two loops for action

The basal ganglia solve selection. Their output nuclei fire continuously, holding motor targets under tonic inhibition, so by default no action is released. A cortical pattern that excites the striatum inhibits the inhibitors covering one action, and that action alone is freed. A second, indirect pathway raises the inhibition on competing actions, and a hyperdirect path from cortex to the output nuclei can stop everything at once.

Two consequences. First, the circuit can fail in either direction, and the clinic shows both. Losing the dopamine neurons that bias the striatum toward release (Parkinson's disease) produces too little movement: slowness, rigidity, and difficulty starting. Losing the indirect-pathway neurons that hold competing actions off (Huntington's disease) produces chorea, a stream of unwanted movements, and a lesion of the subthalamic nucleus produces hemiballismus, violent flinging of the limbs on one side. The classical model of Albin, Young, and Penney and of DeLong rests on this contrast between hypokinetic and hyperkinetic disorders. The circuit does not fail safe: it fails toward too little when the release signal is lost and toward too much when the brakes are lost. Second, dopamine acts on exactly the synapses that decide what is released, so the reward prediction error of Chapter 3, carried by a large population of midbrain dopamine neurons, arrives where the choice is made. Habits are the result.

The cerebellum solves precision. Each Purkinje cell receives about two hundred thousand weak parallel-fiber inputs (context: body state and current command) and one powerful climbing-fiber input that fires when a movement goes wrong. In the classical theory of Marr, Albus, and Ito, the climbing fiber is a teaching signal: recently active parallel-fiber synapses are weakened, an eligibility-trace mechanism of the kind Chapter 3 described. Ito demonstrated this weakening, cerebellar long-term depression (LTD), in 1982. It is one important mechanism, not the whole story: mice in which parallel-fiber LTD was blocked still adapted the vestibulo-ocular reflex and learned eyeblink conditioning (Schonewille et al., 2011), so plasticity at other sites, including the deep cerebellar nuclei, shares the work, and climbing fibers also signal expected reward and learned predictions. What survives is the division of labor: a massive context input, a sparse instructive input, and synapses that change when the two coincide. Over repetitions the cerebellum learns to predict the consequences of a command and to correct before errors are felt. Its lesions do not abolish movement; they make it clumsy.

## The hippocampal loop

Entorhinal cortex to dentate gyrus to CA3 to CA1 and back. The dentate's sparse, strongly inhibited granule cells make similar inputs less similar (pattern separation). CA3's dense recurrent excitation regenerates a whole pattern from a partial cue (pattern completion). On one account, CA1 compares the retrieved pattern with the current input arriving directly from entorhinal cortex; this comparator role is a hypothesis supported by modeling and slice physiology, not an established function. Separation, storage, completion, comparison, each implemented by a motif from the list. Chapter 5 returns to how its synapses change.

## Rhythms

Oscillations are the collective behavior of circuits built from the motifs: feedback inhibition is intrinsically rhythmic (excitation recruits inhibition, inhibition silences excitation, inhibition decays, excitation recovers). The bands, roughly: delta below 4 Hz (deep sleep), theta 4-8 Hz (exploration, memory tasks), alpha 8-12 Hz (idle cortex), beta 13-30 Hz (holding a posture or plan), gamma 30-100 Hz (intense local processing). The associations are statistical, not exclusive.

Rhythms may do two jobs. It has been proposed that they route: a neuron is more excitable at one phase than at the opposite phase, so two regions whose oscillations are aligned would communicate well and two out of alignment would communicate poorly, even though the wiring is unchanged, and changing the phase relation would change effective connectivity without changing a synapse. This is the communication-through-coherence hypothesis (Fries), and the evidence is mixed: coherence between areas does rise with attention, but coherence can also arise simply from connectivity and the sender's oscillatory power with no phase-dependent gating, and gamma frequency shifts with stimulus contrast and size, which makes it an unreliable clock. Whether rhythm routes information or merely reflects it is open. Rhythms also compress: hippocampal place cells fire at progressively earlier theta phases as an animal crosses a location, squeezing seconds of experience into tens of milliseconds, which is the window in which synapses can change.

## The architecture of the whole

Most connections are short and local, forming dense clusters; a minority are long, linking clusters. The result is a small-world network: any two regions are only a few connections apart, yet almost all wiring is local and cheap. The same structure has been shown neuron by neuron in the nematode worm; at the level of single neurons the mammalian brain is an extrapolation. Long axons cost energy, volume, and time, so the brain uses as few as it can. A few hub regions carry most long-distance traffic and are densely connected to one another. This is efficient and fragile in the way an airline network is: damage to a hub is far more consequential than damage elsewhere. Across 26 brain disorders, including schizophrenia and Alzheimer's disease, gray matter loss falls disproportionately on hub regions.

## Coordination without a conductor

Reflexes handle the fastest demands locally. Pattern generators produce rhythm and accept correction. Balanced inhibition keeps every circuit sensitive without runaway. The basal ganglia release one action from default silence. The cerebellum corrects before errors are felt. Rhythms may decide who can talk to whom. Small-world wiring keeps everything close. No component sees the whole; behavior is what the local solutions add up to.

## Implications for artificial intelligence

The chapter's five lessons:
1) Inhibition is a separate population held in balance with excitation, not a negative weight (a biological neuron is excitatory or inhibitory, not both: Dale's principle). This design space is largely unexplored in artificial networks, though first attempts show such networks can match unconstrained ones when the learning rule is adjusted.
2) Selection by disinhibition makes "do nothing" the default and a first-class action, and it gives the circuit two recognizable failure modes, too little and too much, rather than a diffuse degradation.
3) Rhythm may be a routing mechanism: on the coherence hypothesis, phase reconfigures effective connectivity without changing parameters, where artificial systems add attention mechanisms.
4) The wiring budget shapes architecture; artificial networks pay far less per connection than an axon costs (in parameters, memory, and arithmetic rather than volume and metabolism) and are correspondingly dense.
5) A single repeated circuit with different inputs may be sufficient for general computation; what that circuit does, in transferable form, is an open problem.

## Practical summary

- The unit of function is the circuit. Six motifs recur everywhere; inhibition does most of the shaping.
- Excitation and inhibition are balanced near cancellation: expensive, sensitive, stable, fast.
- The retina computes edges and changes before the brain sees anything.
- Pattern generators make rhythm from constant drive through mutual inhibition plus fatigue.
- Neocortex is one six-layer circuit tiled across the sheet with local variations.
- Basal ganglia select by disinhibition and fail in both directions (hypokinetic and hyperkinetic disorders); the cerebellum learns from a climbing-fiber teaching signal at several plasticity sites; the hippocampus separates, stores, completes, and (on one account) compares.
- Rhythms compress experience into the plasticity window and may route information (communication through coherence, a hypothesis with mixed evidence).
- Small-world wiring with hubs: short paths, cheap wiring, fragile hubs.
- No conductor. Coordination is what the parts produce together.

# Labs

## Lab Notes: how to succeed in these labs

As in earlier chapters, you will simulate circuits in simplified form with pencil, paper, and a little arithmetic. The models are discrete-time caricatures of the ones in the chapter's figures; they keep the mechanism and drop everything else. Each optional code extension is short.

General rules:
1) Draw the circuit before computing. Mark excitatory synapses with arrowheads and inhibitory ones with filled circles.
2) Work in steps and write every intermediate value.
3) Finish with an interpretation: what changes if a parameter changes, and what does the biology gain or lose?

### What to hand in for every lab

- A clean circuit diagram (a photo of a hand drawing is fine).
- A calculation table.
- A short interpretation (6-12 sentences).

## Lab 4.1 - Feedforward Inhibition as a Coincidence Detector

### Purpose

To see how adding one inhibitory interneuron turns a sluggish integrator into a circuit that responds only to inputs arriving close together in time.

### Given parameters

Target neuron E starts at V = -70 mV; threshold V_th = -63 mV.
Each input spike produces an EPSP of +3 mV at E on the step it arrives.
Through the interneuron, the same input spike also produces an IPSP of -3 mV at E, arriving 2 steps (2 ms) later.
Between steps, E's deviation from rest shrinks to 80 percent (V = -70 + 0.8 * (V_previous + 70)) before new inputs are added.
Time step: 1 ms.

### Setup

1) Draw input neuron In, interneuron I, and target E as in Figure 4.1B of the chapter.
2) Make a table with columns: t, EPSPs arriving, IPSPs arriving, V after decay, V after inputs, spike?

### Procedure

Part A - Without the interneuron (ignore the IPSPs)

1) Tight timing: three input spikes arrive at t = 0, 0, 1 ms (two together, one a millisecond later). Compute V at each step and record the first step at which threshold is crossed. (Check: V = -64.0 at t = 0.)
2) Spread timing: five input spikes arrive at t = 0, 2, 4, 6, 8 ms. Repeat, running to t = 10. (Check: V = -63.85 at t = 4.)

Part B - With the interneuron (include the IPSPs)

3) Repeat step 1. Does the IPSP arrive in time to matter?
4) Repeat step 2. Record V at every step through t = 10.

Part C - Interpretation

5) Fill a 2 x 2 table (tight vs spread timing; with vs without inhibition) with "spike at t = ..." or "no spike."
6) Write 6-10 sentences: which of the four cases did the interneuron change, why does the 2 ms delay of the IPSP matter, what would happen to the spread case if the inputs were ten instead of five, and where in the chapter does the brain use this trick?

## Lab 4.2 - Excitation-Inhibition Balance by Hand

### Purpose

To reproduce Figure 4.2 of the chapter with a two-line recurrence: the same excitatory population sits quiet until a brief input arrives, and then is tipped into a runaway, responds briefly, or is muted, depending only on inhibitory gain.

### Given model

Two population activities, e (excitatory) and i (inhibitory), both starting at 0.
Input is 0.6 on every step, except steps 4 and 5 when it is 1.6 (a brief sensory event).
Update rules, applied in this order each step:
e_next = clip(1.5 * e - 0.5 * g * i + input - 0.8, 0, 5)
i_next = 1.2 * e_next (use the new e: the fast interneurons follow the excitatory cells at once)
"clip(x, 0, 5)" means: if x is below 0 use 0; if above 5 use 5 (the ceiling: every neuron firing flat out).
The "- 0.8" is the population's firing threshold. The background input of 0.6 stays below it, so the quiet state (e = 0) is stable until the event arrives.

### Procedure

1) Make a table with columns: step, input, e, i. Run 10 steps for g = 0 (no inhibition). Check: e = 0 through step 3, e = 0.80 at step 4, and e = 2.00, i = 2.40 at step 5; e reaches the ceiling at step 8 and stays there after the input is gone.
2) Run 10 steps for g = 1.6 (balanced). Check: at step 5, e = 1.23, i = 1.48; e is back to 0 by step 8.
3) Run 10 steps for g = 3.5 (too much inhibition). (Check: peak e = 0.80 at step 4; e = 0.32 at step 5 and 0 from step 6.)
4) Plot the three e trajectories on one set of axes.
5) In the balanced case, note what e does after the input event: without inhibition the same recurrent weight carried it to the ceiling, yet here it falls back to 0 within three steps of the input ending. Name the motif responsible, and find the section of the chapter that explains why this same motif, with slower inhibition, becomes rhythmic.
6) Write 8-12 sentences: why is the balanced regime worth the energy of two large opposing currents, and what does each of the other two regimes cost the organism?

### Optional code extension (Python, about 15 lines)

Run the same recurrence for 300 steps with small random noise added to the input and sweep g from 0 to 4 in steps of 0.2. For each g record the peak response to the event and the time for e to return to within 10 percent of baseline. Plot both against g and find the range in which the response is both large and brief.

## Lab 4.3 - A Half-Center Oscillator in Twenty Steps

### Purpose

To generate alternation from a constant input using nothing but mutual inhibition and fatigue, as in Figure 4.5 of the chapter.

### Given model

Two sides, L and R, each with an activity (x for L, y for R) and a fatigue level (u for L, v for R).
Constant drive D = 1.0. Inhibition strength w = 2.5.
Start: x = 0.5, y = 0, u = 0, v = 0.
Each step, compute all four new values from the old ones:
x_next = max(0, D - w * y - u)
y_next = max(0, D - w * x - v)
u_next = 0.8 * u + 0.4 * x
v_next = 0.8 * v + 0.4 * y

### Procedure

1) Draw the circuit: L and R with mutual inhibitory synapses, a drive arrow onto each, and a "fatigue" label on each.
2) Make a table with columns: step, x, y, u, v. Run 20 steps. Check: at step 4 you should have x = 0.23, y = 0, u = 0.79; at step 7, y = 0.83.
3) Mark the steps at which the active side switches. Estimate the period of the rhythm.
4) Change the fatigue accumulation from 0.4 to 0.2 and rerun 20 steps. What happens to the period, and does the rhythm survive?
5) Set the fatigue accumulation to 0 and run 6 steps. What does the circuit do, and what is that behavior called in the chapter's motif vocabulary?
6) Write 8-12 sentences: what two ingredients are necessary for alternation, why is the drive allowed to be constant, and what role is left for sensory feedback?

### Optional code extension (Python, about 20 lines)

Run the model for 400 steps and add a one-step "stone underfoot": at step 150, force x to 0 for one step. Observe how the rhythm recovers. Then add a small sensory feedback term that increases D for whichever side has the higher fatigue, and see whether the rhythm becomes more regular.

## Lab 4.4 - Selection by Disinhibition (a paper basal ganglia)

### Purpose

To see why holding every action off by default and releasing one is different from picking the largest output, and how dopamine gain changes what gets released.

### Given model

Three candidate actions, A, B, C, with cortical drive 0.9, 0.6, 0.3.
Striatal activation for each action = drive x dopamine gain G.
The output nucleus holds each action under tonic inhibition of 1.0, reduced by the striatal activation: output inhibition = max(0, 1.0 - striatal activation).
An action is released if its output inhibition falls below 0.3.

### Procedure

Part A - Normal dopamine

1) With G = 1.0, compute striatal activation and output inhibition for A, B, C. Which actions are released?

Part B - Low dopamine

2) Repeat with G = 0.5. Which actions are released? Relate the result to the chapter's remark about Parkinson's disease.

Part C - High dopamine

3) Repeat with G = 1.5. Which actions are released? What would an animal in this state look like? Compare it with the hyperkinetic disorders the chapter describes (chorea, hemiballismus), which arise from losing the indirect pathway's brakes rather than from excess dopamine.

Part D - Learning

4) Return to G = 1.0. Suppose action B was followed by a positive prediction error on the last three trials and its cortex-to-striatum synapses have strengthened so that its effective drive is now 0.8. Recompute. Has the selection changed? Name the chapter in which this learning rule was introduced.

Part E - Comparison with argmax

5) Suppose instead that the system simply released whichever action had the largest cortical drive. With drives 0.9, 0.6, 0.3 the result is the same as Part A. Now set all three drives to 0.1 and compare the two rules. Which rule produces "do nothing," and why does the chapter call "do nothing" a first-class action? Then explain why the chapter nonetheless says the circuit does not fail safe.
6) Write 8-12 sentences: what does default-off buy an organism in an uncertain environment, and what does it cost?

## Lab 4.5 - Small Worlds on a Ring (wiring cost versus path length)

### Purpose

To compute, on a network small enough to do by hand, why a few long connections give most of the benefit of many, and what each design costs in wire.

### Given model

Twelve nodes arranged in a ring, numbered 0 to 11.
Path length between two nodes = the smallest number of edges you must cross to get from one to the other.
Wiring cost of an edge = the shorter distance around the ring between its endpoints (so the edge 0-1 costs 1 and the edge 0-6 costs 6).

### Procedure

Part A - Nearest neighbors only

1) Draw the ring with each node connected to its two neighbors (12 edges).
2) From node 0, write the path length to every other node. Average them.
3) By symmetry the average is the same from every node. Record the average path length, the longest path, and the total wiring cost. (Check: average 3.27, longest 6, cost 12.)

Part B - Two shortcuts

4) Add edges 0-6 and 3-9. Recompute path lengths from node 0 and from node 1 (the two are no longer identical; average the two sets). Record the longest path and the total wiring cost. (Check: cost 24, longest path 4.)

Part C - Dense local wiring

5) Remove the shortcuts. Instead connect every node to its neighbors at distance 1 and 2 (24 edges). Recompute from node 0. (Check: average 1.91, longest 3, cost 36.)

Part D - Interpretation

6) Make a table: design, average path length, longest path, wiring cost.
7) Write 8-12 sentences: which design gives the largest reduction in path length per unit of wire? Why does the brain, which pays for every axon, end up with mostly local wiring and a few long tracts? What happens to the network of Part B if node 0 is damaged, compared with the network of Part A?

### Optional code extension (Python, about 25 lines)

Build a ring of 200 nodes with neighbors at distance 1 and 2, then rewire each edge with probability p to a random node. For p from 0 to 1 in logarithmic steps compute the average path length and the clustering coefficient. Plot both against p and find the range in which paths are short while clustering is still high: the small-world regime.

## Lab 4.6 - From Reflex to Coordinated Behavior (concept map)

### Purpose

To integrate the chapter: every level of coordination, from spinal reflex to whole-brain network, drawn on one page with the motif that implements it.

### Procedure

1) At the bottom of a large sheet, draw a stretch reflex with reciprocal inhibition.
2) Above it, draw a half-center oscillator feeding the same motor neurons, with a sensory feedback arrow that tunes but does not drive it.
3) Above that, draw a cortical column with six layers: thalamic input to layer 4, layers 2 and 3 above, layer 5 output down to the pattern generator and to the basal ganglia, layer 6 back to the thalamus.
4) Beside the column, draw the basal ganglia loop with its tonic inhibition on the thalamus and the dopamine arrow from Chapter 3 onto the striatum. Draw the cerebellum beside it with one climbing fiber labeled "error."
5) Draw a hippocampal loop (EC to DG to CA3 to CA1 to EC) connected to the column.
6) Add a rhythm: a sine wave across the column and the hippocampus, with a note on which phase would allow communication on the communication-through-coherence hypothesis (and that the hypothesis is contested).
7) Around the whole drawing, sketch three more columns and connect them with mostly short edges and one long one.
8) Label every inhibitory synapse with a filled circle and name the motif at each point where one of the six appears.
9) Write a 10-14 sentence caption that follows one tap on the knee, one step of walking, and one decision to stop walking through your diagram, naming the circuit responsible at each stage and ending with why no part of the diagram is in charge.
