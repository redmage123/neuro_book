---
title: "Chapter 5 Student Notes and Labs"
subtitle: "Plasticity and Memory: How Experience Becomes Structure"
---

# Student Notes

## What this chapter is for

Every earlier chapter ended by pointing at this one. Chapter 1 said there is no reset button. Chapter 2 said learning must be physical change. Chapter 3 said neuromodulators decide when change is allowed. Chapter 4 built the hippocampal loop and deferred the question of how its synapses change. Chapter 5 answers it: how activity becomes a lasting alteration of tissue, how that alteration is kept stable, how it is made durable, and why it is deliberately allowed to fade.

If you are coming from software or machine learning, this chapter is designed to correct three instincts:
1) thinking of memory as storage with write and read operations,
2) assuming that a learning rule only needs to say when to strengthen, and
3) treating forgetting and the drift of recalled memories as faults.

Your goal is to be able to explain, in plain language, how a single receptor implements Hebb's rule, why the same calcium signal can strengthen or weaken a synapse, why a neuron needs whole-cell stabilizers, what the two consolidation clocks are and why the brain needs both, and why a memory that changes when it is recalled is a feature.

## Memory is not storage

There is no address, no write, and no read that leaves the record unchanged. Use alters the physical structure of the circuit so that the next similar input unfolds differently. "Memory is something the brain's tissue has become." This single reframing predicts the rest of the chapter: slow learning, blurring between memories, recall that modifies, the role of sleep, and forgetting as mechanism.

## What can change

Four groups, all modifications of machinery that is also doing its ordinary job:
- Strength of an existing synapse: presynaptic release probability; postsynaptic receptor number (receptors are inserted from or removed to a reserve within minutes).
- Structure: dendritic spines grow, shrink, appear, and vanish. A stable core persists for life; a changeable fringe tracks recent experience.
- Intrinsic excitability: ion channel density changes how many spikes a given input produces. Faster, less specific.
- New synapses and, in the dentate gyrus, new neurons. Slowest.

## Hebb's rule and its problem

"Cells that fire together wire together." Local, needs no global error signal. But it only goes up: strengthening makes the correlation more likely, which strengthens further, until every active synapse hits its ceiling and selectivity is gone. A working rule needs three additions: a way to weaken, a bound on strength, and a criterion for which correlations count.

## The coincidence detector

AMPA receptors do fast transmission: glutamate binds, sodium enters. NMDA receptors also bind glutamate but are plugged by a magnesium ion at rest. The plug is expelled only when the membrane is already depolarized. So the NMDA receptor conducts only when presynaptic release AND postsynaptic depolarization coincide: a molecular AND gate for Hebb's two conditions. What it admits is calcium, the signal that starts the plasticity cascade.

## LTP and LTD

Long-term potentiation (strengthening) and long-term depression (weakening) are both downstream of calcium. Large, brief calcium rises activate kinases, which drive extra AMPA receptors into the synapse. Modest, prolonged rises activate phosphatases, which remove them. One ion, two directions, decided by amount and timing.

Numbers to remember: one second at 100 Hz potentiates for hours in a slice and weeks in an animal; fifteen minutes at 1 Hz depresses the same synapse. Early LTP (an hour or two) uses existing proteins; late LTP needs new protein synthesis and comes with visible spine growth. Block protein synthesis within an hour of learning and the memory forms but does not last.

## Timing is causation

Spike-timing-dependent plasticity: presynaptic spike a few to a few tens of milliseconds before the postsynaptic spike strengthens the synapse; the reverse order weakens it; nothing beyond about 50 ms either way. The logic is causal: an input that arrived just before the spike may have helped cause it. The window comes from NMDA kinetics (a back-propagating spike arriving while glutamate is bound expels the magnesium). STDP strengthens chains that fire in order and supplies the weakening Hebb lacked, aimed exactly at out-of-order connections.

## Keeping the whole neuron stable

Local rules do not keep total input in range. Two whole-cell mechanisms do:
- The sliding threshold (Bienenstock, Cooper, and Munro, 1982): the calcium level separating LTD from LTP moves with the neuron's recent average activity. After intense firing it rises; after quiet it falls. The more a neuron fires, the harder its inputs are to strengthen.
- Synaptic scaling: if firing stays too high for hours, every excitatory synapse is multiplied by the same factor below one; too low, above one. Ratios between synapses, where the learned information lives, survive. Timescale about a day.
Inhibitory synapses are plastic too and track excitation. Together these are the cellular counterpart of Chapter 4's excitation-inhibition balance.

## The third factor

Early LTP sets a transient tag at the synapse (an hour or two). Late LTP needs proteins made in the cell body; only tagged synapses capture them. A weak event that tags but does not trigger synthesis fades, unless something, such as dopamine, triggers synthesis within the tag's lifetime. A synapse active during an unremarkable moment can be consolidated retroactively by a reward an hour later. This is synaptic tagging and capture: Chapter 3's eligibility trace at the level of molecules.

## From synapse to engram

A memory is a sparse ensemble (a few percent of cells in a region) whose mutual connections have been strengthened. Engram cells can now be genetically labeled, reactivated with light (producing the learned behavior with no cue), silenced (blocking recall despite the cue), and even combined to implant a memory of an event that never happened. Recall is pattern completion: a cue activates a few engram cells, the strengthened recurrent connections drive the rest, and the whole pattern returns. Recall is a dynamical event, not a lookup.

## Two clocks

Synaptic consolidation (minutes to hours): the early-to-late LTP transition. During this window the memory can be blocked by drugs, interference, or injury.

Systems consolidation (weeks to years): the memory moves from hippocampal dependence to cortical independence. The hippocampus holds a rapidly formed index binding the cortical regions that represented the experience; repeated reactivation strengthens direct cortical connections until the index is unnecessary.

Why two systems (McClelland, McNaughton, and O'Reilly, 1995): a network that learns fast enough to capture one experience overwrites what it knows (catastrophic interference, a mathematical property of distributed representations). A network slow enough to avoid interference cannot capture a single experience. Solution: a fast, sparse hippocampal learner and a slow, statistical cortical learner, with the fast one training the slow one by interleaved replay.

## Sleep

Place-cell sequences from the day replay during slow-wave sleep, compressed about twentyfold, inside sharp-wave ripples that drive cortex. Disrupting ripples impairs memory; prolonging them improves it; cueing a memory during sleep strengthens it preferentially. Sleep also scales synapses down overall, preserving ratios while restoring a sustainable baseline. Sleep is the second half of learning.

## Recall changes the record

Reactivation reopens the plasticity window: for some hours after retrieval a consolidated memory is labile and must be reconsolidated. This produces drift (each recall blends in the present context; confident eyewitnesses who have retold a story many times) and permits revision (a reactivated fear memory given corrective information in the window is weakened more durably). A record that changes when read is a bad database and a good adaptive system.

## Forgetting is a mechanism

The forgetting curve (Ebbinghaus, 1885) drops steeply in hours and days, then slowly; meaning changes the starting point, not the shape. Retrieval, spaced retrieval especially, sleep, and emotional significance all slow it. Forgetting is also actively produced: adult-born dentate neurons rewire circuits and accelerate loss of recent memories; signaling proteins shrink unused spines. These cost energy, which is the evidence that forgetting is function. Flexibility requires generalization, and generalization requires that specifics go.

## Kinds of memory, kinds of circuit

Not storage tiers but different circuits with different mechanisms:
- Episodic and semantic: hippocampus, then cortex via systems consolidation.
- Procedural: basal ganglia and cerebellum (Chapter 4), dopamine-gated striatal plasticity and climbing-fiber LTD; no episode recalled.
- Emotional: amygdala; fast, durable LTP, hard to erase, only suppressed.
- Working: persistent activity and seconds-long synaptic facilitation in prefrontal and parietal cortex, no structural trace.
Patient H. M. lost new episodic memory but learned mirror drawing normally while denying he had seen the task.

## Why learning is slow

Minutes for early LTP, hours and new protein for late LTP, weeks for systems consolidation, thousands of repetitions for a skill. The slowness is also a design requirement: the stability-plasticity dilemma is solved by quarantining fast learning in the hippocampus and letting everything else change at a pace that protects what is there. Slowness is the price of not overwriting yourself.

## Implications for artificial intelligence

1) Catastrophic interference is the central unsolved problem of continual learning; the brain's answer is architectural (two rates plus replay). Experience replay is a direct borrowing.
2) Local rules plus a broadcast modulator can be enough; the brain is an existence proof.
3) Stability must be engineered: sliding threshold, scaling, inhibitory plasticity; per-unit homeostasis is underexplored.
4) Forgetting should be a mechanism: spend effort to remove specifics and keep gist.
5) A memory that changes when read trades fidelity for relevance.

## Practical summary

- Memory is altered structure, not stored data. No address, no write, no unchanged read.
- The NMDA receptor is the coincidence detector; calcium amount and timing decide LTP versus LTD.
- STDP makes the rule causal and supplies weakening.
- Sliding threshold and synaptic scaling keep the whole neuron in range.
- Tagging and capture is where the third factor plugs in.
- A memory is a sparse engram; recall is pattern completion.
- Two clocks: synaptic (hours) and systems (weeks to years); two learners and replay solve catastrophic interference.
- Sleep replays and rescales. Recall reconsolidates. Forgetting is active and adaptive.
- Kinds of memory are kinds of circuit.

# Labs

## Lab Notes: how to succeed in these labs

These labs make the chapter's learning rules concrete with pencil, paper, and small recurrences. Each one isolates a single idea: runaway, calcium control, timing, homeostasis, interference, spacing. The arithmetic is deliberately light; the point is to watch a rule behave.

General rules:
1) Write every intermediate value.
2) Draw the circuit or the timeline before computing.
3) End with an interpretation: what would change if a parameter changed, and what does the biology gain or lose?

### What to hand in for every lab

- A table of values.
- A diagram or sketch where requested (a photo of a hand drawing is fine).
- A short interpretation (6-12 sentences).

## Lab 5.1 - Hebb Runs Away (and one way to stop it)

### Purpose

To see with numbers why the bare Hebbian rule cannot be the whole story, and what a bound on total strength does.

### Given model

One synapse of strength w from input x to output y. The input is constant, x = 1. The output is y = w * x.
Hebbian rule: w_next = w + 0.1 * x * y.
Oja's rule (Hebb plus a decay that grows with the output): w_next = w + 0.1 * y * (x - y * w).
Starting strength w = 1.0 unless stated.

### Procedure

Part A - Pure Hebb
1) Run the Hebbian rule for 10 steps. Record y and w at each step. (Check: w = 1.464 after step 4, 2.594 after step 10.)
2) By what factor does w grow per step? What is w after 50 steps? Is there any value at which it stops?

Part B - Oja's rule
3) Run Oja's rule for 10 steps from w = 1.0. What happens, and why is 1.0 special?
4) Run Oja's rule for 10 steps from w = 0.3. (Check: w = 0.421 after step 4, 0.643 after step 10.) Where is it heading?
5) Run Oja's rule for 5 steps from w = 1.5. Which direction does it move?

Part C - Interpretation
6) Write 6-10 sentences: what did the extra term do, what biological mechanism from the chapter plays the same role, and what would be lost if a neuron had only the Hebbian term?

## Lab 5.2 - One Signal, Two Directions (calcium control)

### Purpose

To reproduce Figure 5.2A of the chapter: the same calcium signal, in different amounts, strengthens or weakens a synapse.

### Given model

Each active input adds 0.3 to the postsynaptic calcium at the synapse. A postsynaptic spike that coincides with the input adds a further 1.0 (the back-propagating spike expels the magnesium plug).
Rule: calcium below 0.5 does nothing; from 0.5 up to but not including 1.4 produces LTD of -0.2; 1.4 or above produces LTP of +0.4.

### Procedure

1) Draw a spine with AMPA and NMDA receptors, as in Figure 5.1.
2) Make a table with columns: active inputs, postsynaptic spike (yes/no), calcium, change. Fill it for these six cases: 1 input alone; 3 inputs alone; 5 inputs alone; 1 input plus spike; 2 inputs plus spike; 4 inputs plus spike. (Check: 3 inputs alone gives calcium 0.9 and LTD; 2 inputs plus spike gives 1.6 and LTP.)
3) Notice the case of 1 input plus a spike. It produces LTD even though pre and post were both active. Explain what this says about weak inputs that happen to coincide with a spike driven by other inputs.
4) Suppose the neuron has recently been very active and its LTD/LTP crossover has slid from 1.4 up to 2.0. Recompute the six cases. Which outcomes changed?
5) Write 6-10 sentences: why is it useful for one signal to encode two opposite instructions, and what would happen to a neuron with a fixed crossover during a day of intense input?

## Lab 5.3 - Timing Is Causation (STDP on a chain)

### Purpose

To show that the timing rule strengthens a circuit's causal order and weakens its reverse, using the window of Figure 5.3.

### Given model

Three neurons A, B, C fire once each: A at 0 ms, B at 10 ms, C at 20 ms.
For a synapse from pre to post, the timing difference is dt = t_post - t_pre.
Window: if dt > 0, change = 1.0 * exp(-dt / 17); if dt < 0, change = -0.5 * exp(dt / 34).
Useful values: exp(-10/17) = 0.555, exp(-20/17) = 0.308, exp(-10/34) = 0.745, exp(-20/34) = 0.555.

### Procedure

1) Draw A, B, C in a row and all six possible synapses between them (A to B, B to A, and so on).
2) Make a table with columns: synapse, dt, change. Fill all six rows. (Check: A to B gives +0.555; B to A gives -0.373.)
3) Mark each synapse on your drawing as strengthened or weakened. What structure emerges after this single pass?
4) Now suppose B fires late, at 40 ms, while A and C keep their times. Recompute A to B and B to C. (Check: A to B gives +0.095; B to C gives -0.278.) What has the rule concluded about B's role, and is that conclusion reasonable?
5) Write 8-12 sentences: why does a causal interpretation of the window make sense given the NMDA mechanism, how does STDP provide the weakening that Lab 5.1 showed was necessary, and what would happen to a recurrent circuit under STDP if all its neurons fired together at exactly the same time?

### Optional code extension (Python, about 20 lines)

Build a ring of 10 neurons that fire in order, 8 ms apart, and apply the window to every pair for 50 passes with strengths clipped to [0, 1]. Print the final weight matrix and confirm that only the forward neighbors are strong. Then jitter each spike time by a random amount up to 15 ms per pass and see how much jitter the structure survives.

## Lab 5.4 - The Sliding Threshold (a self-correcting neuron)

### Purpose

To see how a threshold that follows the neuron's own activity keeps a Hebbian neuron from running away or dying, as in Figure 5.4A.

### Given model

One synapse w, constant input x = 1, output y = w.
A threshold theta that tracks recent activity.
Each step, compute all three from the old values:
change = 0.1 * y * (y - theta)
w_next = w + change (if this is below 0, use 0)
theta_next = 0.7 * theta + 0.3 * y * y
Start with theta = 0.5.

### Procedure

1) Run 15 steps from w = 0.5. Record y, change, w, theta each step. (Check: after step 5, w = 0.530 and theta = 0.301.)
2) Run 15 steps from w = 2.0. (Check: after step 5, w = 1.639 and theta = 4.387; after step 15, w = 0.388.)
3) In the second run, find the step at which the change switches sign. What made it switch?
4) Both runs are drifting toward the same value. Find it by asking: at a fixed point, what must y equal, and what must theta equal?
5) Write 8-12 sentences: compare this neuron with the pure Hebbian neuron of Lab 5.1, explain in words why "the more it fires, the harder it is to strengthen" produces stability, and say what role synaptic scaling (Figure 5.4B) plays that the sliding threshold does not.

## Lab 5.5 - Catastrophic Interference and the Cure (two learners)

### Purpose

To produce catastrophic interference in the smallest possible network, and to see why interleaving fixes it, as the complementary learning systems theory predicts.

### Given model

A "cortex" with two weights, w1 and w2, both starting at 0. Its output for an input (x1, x2) is out = w1 * x1 + w2 * x2.
Two experiences:
Experience A: input (1.0, 0.5), target output 1.
Experience B: input (0.5, 1.0), target output 0.
Learning step (delta rule, learning rate 0.5): error = target - out; w1_next = w1 + 0.5 * error * x1; w2_next = w2 + 0.5 * error * x2.

### Procedure

Part A - Sequential learning (one fast learner)
1) Train on A four times in a row. Record w1, w2 after each step. (Check: after four steps, w = (0.784, 0.392), and the output for A is 0.98.)
2) Compute the output for B at this point.
3) Now train on B four times in a row. (Check: w = (0.476, -0.223).)
4) Compute the output for A. It was 0.98. What is it now? This is catastrophic interference.

Part B - Interleaved learning (replay)
5) Reset to w = (0, 0). Train alternately: A, B, A, B, A, B, A, B. (Check: w = (0.806, -0.268).)
6) Compute the outputs for A and for B. Compare with Part A.
7) Continue interleaving for four more pairs. Do both outputs keep improving?

Part C - Interpretation
8) Write 8-12 sentences: why did sequential training destroy A, why does interleaving help, which structure in the brain does the interleaving and when, and what would it cost the organism to interleave all of its past experiences with every new one?

### Optional code extension (Python, about 25 lines)

Use a 20-weight "cortex" and 10 random experiences with random targets. Train sequentially (each experience 20 times, one after another) and interleaved (200 random draws). Plot the error on all 10 experiences after training under each schedule. Then add a "hippocampus" that stores the last 3 experiences exactly and replays them, interleaved with the current one, and compare.

## Lab 5.6 - Forgetting and Spacing (what retrieval buys)

### Purpose

To reproduce Figure 5.9 of the chapter: retention decays, and each successful retrieval slows the next decay, with spaced retrievals doing more than massed ones.

### Given model

Retention after a gap of g days since the last learning or retrieval is R = 100 * exp(-g / s), where s is the memory's stability in days.
Initial stability s = 6 days.
Each retrieval resets the gap to 0 and multiplies s by 1.9.
Useful values: exp(-1/6) = 0.846, exp(-30/6) = 0.007.

### Procedure

1) With no retrieval, compute retention at days 1, 4, 10, 20, and 30. (Check: 0.7 percent at day 30.)
2) Massed schedule: retrievals on days 1, 2, 3, and 4. Compute s after each retrieval and the retention at day 30. (Check: 71.7 percent.)
3) Spaced schedule: retrievals on days 1, 4, 10, and 20. Compute the retention just before each retrieval (Check: 84.6 percent before the day-1 retrieval, 78.4 percent before the day-20 retrieval) and the retention at day 30. (Check: 88.0 percent.)
4) Both schedules use four retrievals and end with the same stability. Why does the spaced schedule score higher at day 30? Look at when the last retrieval happened.
5) Design a five-retrieval schedule that keeps retention above 75 percent at all times through day 60. State the schedule and show the retention just before each retrieval.
6) Write 8-12 sentences: what does retrieval do that re-reading does not, which mechanisms from the chapter (reconsolidation, tagging, consolidation) could implement "retrieval multiplies stability," and why would an organism benefit from a memory system in which stability grows only when a memory is actually used?

## Lab 5.7 - From Synapse to Memory (concept map)

### Purpose

To integrate the chapter on one page: the chain from coincidence to durable memory and back, with every stabilizer and gate in place.

### Procedure

1) Draw one synapse on a spine. Inside it, draw the NMDA receptor with its magnesium plug and the AMPA receptors. Add the calcium arrow and the two cascades (kinases to LTP, phosphatases to LTD).
2) Beside it, draw the STDP window and connect it to the NMDA receptor with a note on why timing matters.
3) Around the neuron, draw the sliding threshold and synaptic scaling as two feedback loops from the neuron's firing back onto the rule.
4) Add a dopaminergic axon above the spine, with a "tag" at the synapse and a "capture" arrow from the cell body, labeled with the time window.
5) Zoom out: draw a sparse engram of eight cells in a hippocampus box with strengthened recurrent links, and a partial cue entering it.
6) Draw the cortex box beside it with the two arrows (replay during sleep, cues) and the two clocks labeled with their timescales.
7) Add a recall event that reopens the plasticity window on the engram, and a forgetting arrow that prunes unused spines.
8) Write a 10-14 sentence caption that follows one experience from the moment two neurons fire together to the day, months later, when it is recalled from the cortex without the hippocampus, naming the mechanism at each step and ending with what has been forgotten and why that is correct.
