---
title: "How the Brain Learns"
subtitle: "Instructor's Answer Key to the Student Notes and Labs"
---

# About This Key

This key gives worked solutions to every computational step of the labs in the Student Notes and Labs for Chapters 1 to 16, model answers to the written questions, and grading guides for the open-ended tasks and concept maps. Every computed value was checked by recalculation. Model answers name the section of the chapter they draw on, so that students can be sent back to the text. Where a lab admits more than one defensible answer, the key says what a strong answer must contain rather than giving a single wording. Notes for instructors at the end of each chapter point out places where students commonly go wrong or where an answer depends on an assumption the lab leaves open.

# Chapter 1: What the Brain Is (and Is Not)

## Lab 1.1 - Brains vs Computers (structured comparison)

1) Table format only; accept any clean three-column layout.
2-3) Model rows (computer / brain), grounded in "The Brain Is Not a Digital Computer" and "The Brain Is a Physical System":
- Instruction stream: explicit program fetched step by step / none; behavior emerges from wiring, synaptic strengths, and dynamics.
- Locus of control: central control unit / no central controller; control is distributed across circuits.
- Memory versus processing: separate memory and CPU joined by one channel / no boundary; the synapse that transmits a signal also stores the change.
- Timing: global clock, discrete steps, picosecond switching / asynchronous, continuous time; spike about 1 ms, synaptic delay about 0.5 ms; roughly a million times slower per step.
- Signal type: binary, unambiguous zeros and ones / graded synaptic potentials plus all-or-none spikes, variable in amplitude and context dependent.
- Noise: suppressed by engineering / pervasive (most impulses at single hippocampal synapses fail; spike-count variance about equal to the mean) and exploited.
- Component reliability: near-perfect parts / unreliable parts, reliability from populations, feedback, and degeneracy.
- Self-modification: hardware fixed while running / rewires itself while running.
- Objective: correct answers to well-specified problems / viability of the organism.
- Failure mode: abrupt (crash, single bit error propagates) / graceful degradation; function partly recovers after damage (stroke example).
Penalize cells that say "better" or "worse," and cells that are vague ("brain is more complex").
4-5) Expected constraint column: no instruction stream and no central control trace to no designer and evolutionary history (Jacob's tinkerer); merged memory and processing and self-modification trace to physical change being the storage medium; slow asynchronous timing traces to ion and molecular physics plus the 20-watt budget; noise and unreliable parts trace to physics and energy (Attwell and Laughlin, Lennie); graceful failure traces to degeneracy and survival under uncertainty; objective traces to survival in a partially observable world (see "The Brain as an Adaptive Control System"). A strong answer ties at least one row explicitly to the energy budget and one to evolutionary history.
6-7) Model analyses:
- "I stored that in memory": assumes a separate store and faithful retrieval; fails on the memory-versus-processing row (storage is in the same synapses that transmit, and every use can alter it).
- "My brain is processing": assumes a serial program on a CPU; fails on instruction stream and control rows; the hundred-step constraint forces massively parallel, shallow computation.
- "I need to reboot": assumes a reset to an earlier state; fails on the self-modification row (see "Time, Change, and the Absence of Reset"); rest changes physiology, it does not restore a prior state.
Accept other examples ("downloading information," "hardwired," "bug in my thinking") if the hidden assumption and failing row are named.
8) Grading guide: a strong answer names a specific row and explains why it surprised them with a number or experiment from the chapter (for example 150 ms animal detection against a millisecond-scale step). For "most dangerous term," strong candidates are "storage" or "memory," "processing," and "optimal," each with the assumption it imports. Common mistake: concluding the brain is "not computational" at all; the chapter says both are physical systems capable of computation under different constraints (Marr's levels).

## Lab 1.2 - No Reset Button (history-dependent learning by hand)

Setup 1-2) Number line with w = 0 marked; two trajectories plotted.
1) Sequence 1 (+1, +1, -1, -1): w = 0.5, 0.675, 0.2646, 0.0477. The printed check (0.675) is correct.
2) Sequence 2 (-1, -1, +1, +1): w = -0.5, -0.675, -0.2646, -0.0477.
3) Same experiences, opposite final signs (+0.048 against -0.048). With declining plasticity the first two experiences dominate; the history, not the set of experiences, sets the outcome.
4) Sequence 3 (+1, -1, -1, -1): w = 0.5, -0.025, -0.2639, -0.3901. Final w = -0.390.
5) Sequence 4 (-1, -1, -1, +1): w = -0.5, -0.675, -0.7546, -0.4537. Final w = -0.454.
6) Compare each with four -1 experiences (final w = -0.797). The early good experience leaves a residue of +0.407 (0.5 x 0.65 x 0.755 x 0.8285); the late one leaves +0.343 (alpha_4 x 2 = 0.1715 x 2). The early experience has the larger lasting effect because it acts when alpha is largest. Note for grading: the late +1 produces a visible jump (+0.30) but the early one wins in the final state.
7-8) From w = 0.0477 with alpha = 0.1: distance to -1 is 1.0477, and 1.0477 x 0.9^n < 0.5 requires n > 7.02, so 8 experiences (w = -0.4989 after 7, -0.549 after 8).
9) A computer needs one assignment. The brain cannot write a value; it can only push the existing value with new experience, at a cost that grows as plasticity falls.
10) Grading guide: habits as accumulated w that takes many contrary experiences to move; childhood persistence as early high plasticity setting the initial conditions (sensitive periods, Wiesel and Hubel's monocular deprivation); "just unlearn it" unavailable because there is no reset, only further incremental learning (see "Time, Change, and the Absence of Reset"). Acceptable omissions to name: a single variable instead of many synapses, no fast hippocampal learner or replay (complementary learning systems), no neuromodulation of plasticity, no reactivation of plasticity in adults, no forgetting or decay, no consolidation stages.
Optional extension (100,000 simulated sequences of five +1 and five -1): declining schedule gives final w with SD about 0.16 (range about -0.43 to +0.43); constant alpha = 0.3 gives SD about 0.30 (range about -0.69 to +0.69). Constant alpha produces more diverse adults. Students often predict the opposite; the declining schedule makes order matter (early items weigh most) but also caps total movement, so outcomes cluster. Accept either finding if the student's code is correct and the explanation matches it.

## Lab 1.3 - Noise and Redundancy (why unreliable parts make a reliable system)

1-3) Rolled values vary. Expected magnitudes: single-neuron error is uniform on -2.5 to +2.5 in steps of one (SD 1.71, mean absolute error 1.5); the six-neuron average has SD 0.70 and mean absolute error about 0.56. Students should see roughly a 2.5-fold reduction.
4) Error of the mean scales as 1/sqrt(N): SD about 0.28 for 36 neurons (mean absolute error about 0.23) and about 0.09 for 360 (mean absolute error about 0.07).
5) P(success) = 0.5; ten trials should give about five successes.
6) Five synapses: 1 - 0.5^5 = 0.969.
7) Ten synapses: 1 - 0.5^10 = 0.999.
8) Part A cost per report: 1, 6, and 36 units (30 and 180 if a student counts all five repetitions; accept either if stated). Part B cost per message: 1, 5, and 10 units (if all synapses attempt every time).
9) Grading guide: reliable single components are physically and energetically expensive or impossible (noise sets a floor; see "Noise, Degeneracy, and the Myth of Optimization"); redundancy built from cheap parts gives graceful degradation, so the death of one neuron changes the average slightly instead of losing the signal entirely. Strong answers mention diminishing returns: error falls as 1/sqrt(N) while cost rises as N, and going from five to ten synapses buys only 0.03 more reliability for twice the cost; the 20-watt budget and Lennie's limit of about one neuron in a hundred active cap the strategy. Extra credit for distinguishing this duplication from degeneracy (structurally different elements doing the same job). Common mistake: claiming redundancy is free or that error falls in proportion to N.

## Lab 1.4 - Viability, Not Truth (decisions under asymmetric cost)

1) Expected cost of fleeing = 1.
2) Expected cost of staying = 0.05 x 100 = 5.
3) Flee. A rule that always flees is wrong 95 percent of the time but minimizes expected cost (1 against 5); the objective is survival cost, not the fraction of correct classifications.
4) Break-even: 100p = 1, so p = 0.01.
5-6) The wrong-action rate applies to the action taken; the 40-unit delay cost is added to the outcome when a predator is present:
- True predator: act now = 0.7 x 1 + 0.3 x 100 = 30.7; wait = 40 + 0.95 x 1 + 0.05 x 100 = 45.95 (matches the printed check).
- False alarm: act now = 0.3 x 1 = 0.3; wait = 0.05 x 1 = 0.05.
7) Act now: 0.05 x 30.7 + 0.95 x 0.3 = 1.82. Wait: 0.05 x 45.95 + 0.95 x 0.05 = 2.345. Always flee (Part A): 1.0. Ranking: always flee (1.0) < act now (1.82) < wait (2.345). Waiting does not pay when delay is this costly, and the blind reflex beats both because a false alarm is cheap. Break-even delay cost against acting now: 0.05d + 0.345 = 1.82, so d = 29.5 units (against always fleeing, about 13.1 units). Below 29.5 units waiting beats acting now, which is the other side of the trade-off; strong answers note that the best policy depends on what delay costs.
8) Grading guide: threat bias follows from asymmetric costs (a false alarm costs 1, a miss costs 100); reflexes trade accuracy for speed when delay is costly; "optimization" means minimizing expected harm to viability, not maximizing accuracy (see "The Brain as an Adaptive Control System"; Simon's satisficing; Tversky and Kahneman). Good bias examples: negativity bias, loss aversion, hyperactive agency detection, availability bias for dangerous events. Common mistake: calling the fleeing rule irrational because it is usually wrong.

## Lab 1.5 - Engineering Autopsy and AI Reflection

1-3) Model rows (engineer's assumed problem / actual problem / what breaks if removed):
- Slow learning: fast learning from data / stable learning without overwriting old knowledge (molecular construction plus complementary learning systems) / catastrophic interference; one bad experience rewrites behavior.
- Forgetting: perfect storage / keeping what is useful within limited synaptic resources, generalization over detail / interference, cluttered retrieval, overfitting to stale situations.
- Perceptual bias: unbiased measurement / fast inference from ambiguous evidence using priors (Helmholtz) / slow, noisy, often useless perception.
- Confabulation or filling-in: accurate reporting of causes / producing a usable, coherent account in time to act (Nisbett and Wilson's stocking choice) / paralysis or gaps in perception (blind spot) and action.
- Fatigue: continuous maximal throughput / protecting a limited energy budget and tissue homeostasis / metabolic damage, runaway excitation.
- Habit: re-deciding each case optimally / cheap, fast behavior carried forward by history (no reset) / every action becomes a costly deliberation.
Accept other defensible rows; require the fourth column to name a concrete loss.
4-6) Grading guide: classification on all six properties with justification. Example (large language model): instruction stream, computer-like at the hardware level but neither at the level of learned behavior; control, computer-like; memory versus processing, partly brain-like (knowledge stored in weights that also compute); timing, computer-like (clocked, discrete tokens); noise, mostly computer-like (deterministic arithmetic, sampling noise added at output, dropout in training); self-modification, computer-like (frozen at deployment). Reset present: reinitialization, retraining from scratch, clearing the context window. No reset hurting it: a deployed model that memorized bad or private data cannot simply forget it; fine-tuning can cause catastrophic forgetting.
7) Grading guide: strong answers cite at least three chapter principles from "Implications for Artificial Intelligence" (energy, noise, no reset, control) and pick one violation to fix with a mechanism (for example continual learning with replay, online correction from consequences, energy-aware sparse activation). They should also respect the chapter's caution that not every brain solution should be copied. Common mistakes: equating "brain-like" with "better," and treating benchmark accuracy as the viability objective.

### Notes for instructors
- Lab 1.2 optional extension: constant alpha yields more diverse final values than the declining schedule, which may contradict the expected answer.

# Chapter 2: Neurons: The Brain's Signaling Cells

## Lab 2.1 - Spatial and Temporal Summation (manual integrate-and-fire)

Setup 1-3) Soma, three branches at distance units one, two, and three, AIS drawn on the axon side.
1-2) Effective EPSPs at the AIS: A = +0.20 mV, B = +0.10 mV, C = +0.05 mV.
3) DeltaV = 0.80 + 0.40 + 0.20 = +1.40 mV.
4) V_now = -68.6 mV.
5) No spike (13.6 mV short of -55 mV).
6-9) Staggered bursts:
- t = 0: -70 + 0.80 = -69.2 mV
- t = 10: -70 + 0.5 x 0.80 + 0.40 = -69.2 mV
- t = 20: -70 + 0.5 x 0.80 + 0.20 = -69.4 mV
10) Threshold never reached; peak -69.2 mV, less than the -68.6 mV of simultaneous arrival.
11-12) With A = 6, B = 4, C = 2 (inputs 1.20, 0.40, 0.10 mV): simultaneous sum = +1.70 mV (-68.3 mV); staggered t = 0: -68.8 mV, t = 10: -69.0 mV, t = 20: -69.4 mV. No spike.
13) Model answer: moving synapses closer to the AIS raises the effective input (1.4 to 1.7 mV simultaneous; peak -69.2 to -68.8 mV) because passive spread attenuates distal input (see "Dendrites Are Not Passive Cables"). Staggering wastes input because each EPSP decays before the next arrives; the cell detects coincidence, not totals (see the worked example in "Excitatory and Inhibitory Postsynaptic Potentials"). The t = 20 value is unchanged at -69.4 mV because, with this schedule, the halving between bursts exactly matches the halving per distance unit (V(20) - V_rest = 0.25A + 0.5B + C = 0.6 mV in both cases); a sharp student will spot this. Reaching the 15 mV threshold would take about 75 simultaneous Branch A inputs at 0.20 mV each, which is why neurons need many coincident inputs. Strong answers note the model omits NMDA and dendritic calcium spikes, which can make clustered inputs on one branch far more effective than this linear sum.
14) 15 mV / 0.20 mV = 75 simultaneous Branch A inputs, more than six times the 12 of Part A (which gave only 1.40 mV).
15) Two bursts of n inputs: V(10) - V_rest = 0.5 x 0.20n + 0.20n = 0.30n, so n = 50 per burst and 100 in all to reach -55.0 mV at t = 10 ms. Splitting the inputs across 10 ms costs a third more inputs than delivering them together.
16) Spike in both cases (V = -55.0 mV, which meets the >= -55 mV criterion). Model answer: a dozen inputs leave the cell more than 13 mV short; firing takes tens of coincident inputs (here 75), and every millisecond of spread raises the count, so the neuron is a detector of coincident input, not a counter of total input. Strong answers note that real EPSPs vary in size and that active dendritic events lower the count for clustered inputs.

## Lab 2.2 - Excitation-Inhibition Competition (EPSPs vs IPSPs with timing)

Setup 1-2) Ten excitatory synapses on Branch A, six inhibitory synapses at distance unit one.
1-3) DeltaV_E = 10 x 0.20 = +2.0 mV; V_now = -68.0 mV; no spike.
4-6) DeltaV_I = 6 x (-0.30) = -1.8 mV; V_now = -69.8 mV; no spike. Inhibition cancels 90 percent of the excitation.
7-10) V(0) = -71.8 mV; V(10-) = -70.9 mV; V(10+) = -68.9 mV; no spike. Inhibition arriving 10 ms early still removes 0.9 mV of the 2.0 mV excitatory drive.
11-12) At distance unit two: IPSP = -0.6 x 0.25 = -0.15 mV; six give -0.9 mV. Redo Part C: V(0) = -70.9 mV; V(10-) = -70.45 mV; V(10+) = -68.45 mV; no spike. (For comparison, simultaneous at distance two: -68.9 mV.)
13) Model answer: the outcome depends on how much inhibition is still present at the AIS when excitation arrives (see "Excitatory and Inhibitory Postsynaptic Potentials"). Simultaneous inhibition removes 1.8 mV; inhibition 10 ms early removes half of that, because it has decayed; inhibition one distance unit further out removes half again, because passive spread attenuates it. Inhibition placed near the soma and AIS therefore has a strategic position, gating the summed output of the whole tree. Strong answers note that no condition reaches threshold here, so the measure is distance from threshold, and that real inhibition near rest acts partly by shunting (increasing conductance, clamping the membrane near rest), which this linear subtraction model understates. They should also note that the same counts of synapses give different results with different timing and placement, so the neuron reports the balance of coincident excitation and inhibition, not counts.

## Lab 2.3 - Action Potential Propagation (state machine walk-through)

1-4) Unblocked run: at time t, segment t + 1 is A and segment t is F (for t = 1 to 11); the wave reaches segment 12 at t = 11, segment 12 is F at t = 12, and all are R at t = 13 and 14.
5-6) Blocked run (segment 8 forced F at t = 6):
- t = 0 to 5: as above (t = 5: segment 5 F, segment 6 A).
- t = 6: segment 6 F, segment 7 A, segment 8 F (forced).
- t = 7: segment 7 F; segment 8 does not activate because it was F at t = 6 (it returns to R); no segment is active.
- t = 8 to 14: all R. The wave is annihilated at segment 8 and never reaches segments 8 to 12; it does not restart when the block recovers, because nothing is active to re-trigger it.
Accept the alternative reading in which the block is applied after the t = 6 update; the conclusion (propagation fails permanently at the block) is the same.
7) Model answer (see "How the Action Potential Propagates"): reliability comes from local regeneration; each segment produces a full-size event from its own resources, so amplitude does not decay over distance. What travels is a pattern of state change (causation), not a particle or substance. Refractoriness prevents backward propagation (the segment behind is F) and so enforces one-way travel, and it limits the maximum firing rate. The block shows the cost of a relay design: a single failed segment kills the signal downstream, and the signal is not stored anywhere to be resent. Strong answers connect refractoriness to sodium-channel inactivation and mention that myelin's saltatory conduction is a faster, cheaper version of the same regenerative relay.

## Lab 2.4 - Engineering trade-offs: correctness vs viability

1-3) Model rows (neuron / CPU / packet network):
- Speed: spike about 1 ms, conduction about 1 to 100 m/s / about 100 ps switching, GHz clock / milliseconds of latency, speed-of-light links plus queuing.
- Energy per operation: high per spike (signaling dominates a 20-watt brain) / very low per operation, high total / moderate per packet, dominated by routers and links.
- Fault tolerance: populations and degeneracy; graceful degradation / low; a single fault can crash / high; rerouting around failed nodes.
- Noise strategy: tolerate and exploit (synaptic failures, variable spike counts; population averaging) / suppress (digital levels, error correction) / detect and retransmit (checksums, acknowledgments).
- Learning: synapses change with use (LTP, spine enlargement) / none in hardware; software only / routing tables adapt, no learning of content.
- Reset: none; history accumulates / full reset and reload / sessions and routers can be restarted.
- Repair: plasticity and homeostatic adjustment, limited regeneration / replace the part / reroute, replace nodes.
- Objective: viability of the organism / correct, deterministic computation / reliable delivery, eventual correctness.
4-5) Grading guide: likely picks are speed, energy per operation, or noise. A strong answer explains each weakness as adaptive using chapter material (see "Why Neurons Look Inefficient, and Why They Are Not"): slowness offset by massive parallelism and coincidence detection; noise tolerated by population voting and set by physical limits (Faisal, White, and Laughlin's minimum axon diameter); energy cost buying a signaling element that rewires itself, with sparse firing as the economy (Sterling and Laughlin). A strong answer also notes the packet network as an intermediate case that, like the brain, accepts unreliable parts but corrects by retransmission rather than redundancy and averaging. Common mistakes: treating the neuron as simply "worse," and ignoring that the objective row differs.

## Lab 2.5 - Full causal concept map (from synapse to learning)

Required nodes: dendrites, soma, AIS, axon, axon terminals; two excitatory and two inhibitory synapses; neurotransmitter (glutamate for excitatory, GABA for inhibitory accepted), receptors and ion channels, EPSP, IPSP, summed voltage at AIS, threshold, action potential, propagation, calcium entry at terminal, vesicle release, back-propagating spike (credit, not required).
Key labeled links:
- Presynaptic spike -> calcium entry -> vesicle fusion -> transmitter release (probabilistic, quantal).
- Transmitter -> receptor binding -> ion channel opening -> EPSP (depolarizing) or IPSP (hyperpolarizing or clamping).
- EPSPs and IPSPs -> passive spread with attenuation (distance) and decay (time) -> summed V at AIS.
- Summed V reaches threshold -> AIS fires all-or-none spike -> regenerative, one-way propagation (refractory segment behind) -> terminal release onto the next cell.
- Plasticity loop: repeated co-activation of pre- and postsynaptic cells (back-propagating spike meeting recent input) -> stronger synapse (more release, more receptors, larger spine) -> larger EPSP next time (see "Plasticity: Learning as Physical Change").
- Stabilization loop: increased excitation -> recruits inhibitory interneurons -> more IPSPs -> firing held in range (negative feedback; credit for mentioning homeostatic scaling from Chapter 1).
6) Caption grading guide: the caption must tell a causal story in order (chemical input, graded potentials, decision at the AIS, propagation, output, change), state that the input is a probabilistic chemical event while the output is all-or-none, identify the AIS as the decision point, and explain that the plasticity loop is positive feedback that needs the stabilization loop to avoid runaway excitation. Common mistakes: arrows from dendrites directly to the axon skipping the AIS, describing the spike as decaying with distance, and drawing plasticity as a separate memory store rather than a change in the same synapse.

### Notes for instructors

None beyond the answers above.

# Chapter 3: Neuromodulation: How Chemical Context Shapes Learning and Behavior

## Lab 3.1 - Reward Prediction Error by Hand (why dopamine moves to the cue)

Setup diagram: a timeline with the cue at 0 s and the reward at 2 s, and two bars above it ("dopamine at cue" over the cue, "dopamine at reward" over the reward).

1) Table columns as given. Dopamine at cue equals V before the trial.
2) Trial 1: V before 0, delta 1.000, V after 0.250, cue 0.
3) Trial 2: V before 0.250, delta 0.750, V after 0.4375, cue 0.250.
4) Full Part A table (alpha = 0.25):

| Trial | V before | delta at reward | V after | Dopamine at cue |
|---|---|---|---|---|
| 1 | 0.0000 | 1.0000 | 0.2500 | 0.0000 |
| 2 | 0.2500 | 0.7500 | 0.4375 | 0.2500 |
| 3 | 0.4375 | 0.5625 | 0.5781 | 0.4375 |
| 4 | 0.5781 | 0.4219 | 0.6836 | 0.5781 |
| 5 | 0.6836 | 0.3164 | 0.7627 | 0.6836 |
| 6 | 0.7627 | 0.2373 | 0.8220 | 0.7627 |
| 7 | 0.8220 | 0.1780 | 0.8665 | 0.8220 |
| 8 | 0.8665 | 0.1335 | 0.8999 | 0.8665 |

V after trial 8 = 0.8999 (about 0.90) and delta at reward on trial 8 = 0.1335 (about 0.13), matching the printed check. Closed form: V after n trials = 1 - 0.75^n.
5) Trial 1 bars: cue 0, reward 1.0 (Figure 3.5A). Trial 8 bars: cue about 0.87, reward about 0.13 (approaching Figure 3.5B).
6) Trial 9: cue present, r = 0.
7) delta = 0 - 0.8999 = -0.90: negative and nearly as large as the original positive error. This is the omission dip (Figure 3.5C), timed to when the reward was due.
8) V after = 0.8999 + 0.25 x (-0.8999) = 0.6749. The prediction is partly unlearned (the cue now predicts about 0.67); repeated omissions would drive it toward 0 (extinction).
9) alpha = 0.05: V after trials 1 to 8 = 0.050, 0.0975, 0.1426, 0.1855, 0.2262, 0.2649, 0.3017, 0.3366. V reaches only about 0.34 (1 - 0.95^8); the reward is still mostly unpredicted (delta on trial 8 = 0.70).
10) alpha = 0.9: delta = 1.0, 0.10, 0.010, 0.001; V after trial 4 = 0.9999. The error collapses by a factor of ten each trial: learning is almost one-shot. Students should note the trade-off: fast learning also means one omission (or one noisy outcome) would wipe out most of the prediction (V would fall to about 0.10).
11) Model answer (see "Dopamine: Schultz's Monkeys"):
- Dopamine at reward reports the prediction error r - V, not reward itself. Once V is close to r, a reliable reward produces almost no error, so it becomes "invisible."
- The signal did not disappear; it moved to the cue. The cue now carries the news (in this simplified model, dopamine at cue = V), as in Figure 3.6 where the error migrates backward to the earliest reliable predictor, which is what temporal-difference learning does.
- The omission dip is a negative error timed to the expected reward. It tells the rest of the brain that things went worse than predicted and that the cue's value should be revised downward; it is direct evidence that the neurons hold a timed prediction, something a reward detector could not produce.
- The learning rate sets the speed-stability trade-off: small alpha is slow but robust to noise, large alpha is fast but volatile.
- Strong answers note the limits: the RPE account describes a large population of dopamine neurons in appetitive tasks, and the population is heterogeneous (see the cautions in the same section). Common mistake: saying dopamine "is pleasure" or that the cue response is a reward.

## Lab 3.2 - Eligibility Traces and the Temporal Gap (three-factor rule)

Setup: one postsynaptic neuron, synapses S1 to S3, a dopaminergic axon with varicosities passing over all three (Figure 3.1B).

1) S1 active at 0 s; dopamine at d.
2) e(d) = 0.5^d; delta_w = 0.1 x e x 0.8 = 0.08 x 0.5^d.

| d (s) | e(d) | delta_w |
|---|---|---|
| 0 | 1.000 | 0.0800 |
| 1 | 0.500 | 0.0400 |
| 2 | 0.250 | 0.0200 |
| 3 | 0.125 | 0.0100 |
| 5 | 0.03125 | 0.0025 |
| 10 | 0.000977 | 0.000078 |

3) delta_w = 0.01 exactly at d = 3 s (0.08 x 0.5^3), so with the "at or below 0.01" criterion the threshold is 3 s: learning is effectively absent for any delay of 3 s or more. Accept "between 3 and 5 s" if the student marks only the table entries.
4) S1 at -1 s, S2 at -4 s, S3 at -8 s; dopamine at 0.
5) Traces: e1 = 0.5, e2 = 0.0625, e3 = 0.00390625. Updates: 0.0400, 0.0050, 0.0003125.
6) Ratio 128 : 16 : 1 (each extra second of delay halves the credit).
7) delta = -0.6: updates -0.0300, -0.00375, -0.000234. S1, the most recently active synapse, weakens most; the ratio is unchanged (128 : 16 : 1), only the sign flips.
8) Trace never decays: all three traces are 1.0, so every synapse gets delta_w = 0.08 (ratio 1 : 1 : 1). Timing information is lost; S3, active 8 s earlier, gets the same credit as S1.
9) All 50 unrelated synapses also receive delta_w = 0.08 each (or -0.06 with a negative error), a total of 4.0 units of weight change spread over synapses with no causal link to the outcome. Specificity is destroyed and the useful change at S1 is swamped.
10) Model answer (see "Eligibility Traces and the Three-Factor Rule" and "Credit Assignment"):
- The trace is a short-lived, local record that a synapse was recently active; the global dopamine signal is a scalar broadcast by volume transmission and cannot address individual synapses.
- Selectivity comes from the AND of the two: the signal reaches every synapse, "but only the recently active ones are listening."
- The decay constant buys specificity: credit goes mostly to activity close in time to the outcome, which is more likely to be causal, and old, unrelated activity is ignored.
- The cost is reach: causes further back than a few time constants cannot be credited (the distal reward problem). Measured windows differ by region (about 0.3 to 2 s in striatum, longer in hippocampus), and synaptic tagging and capture extends the reach to an hour or two for consolidation.
- Without decay, credit becomes indiscriminate (step 9); with very fast decay, almost nothing can be credited.
- Strong answers connect the half-life to the typical delay between action and outcome in the animal's ecology. Common mistake: claiming dopamine "targets" the active synapse.

Optional extension: delta_w falls to 0.01 at 3 half-lives, so with half-life 1 s the reach is 3 s; with 3 s, about 9 s; with 0.3 s, about 0.9 s (on a 0.5 s grid, the last step at or above 0.01 is 0.5 s).

## Lab 3.3 - Credit Assignment Under Uncertainty (a dice-driven learner)

1) Diagram: S1 to S4 converging on one neuron; one dopaminergic axon broadcasting delta to all four.
2) Table as specified.
3) to 5) Worked run with the pre-rolled sequence (active = roll of 4, 5, or 6; delta = +0.5 if rewarded, -0.5 if not; each active synapse changes by 0.1 x delta = +/-0.05):

| Trial | Active set | Outcome roll | Reward | delta | w1 | w2 | w3 | w4 |
|---|---|---|---|---|---|---|---|---|
| 1 | S2, S4 | 2 | 0 | -0.5 | 0.00 | -0.05 | 0.00 | -0.05 |
| 2 | S1 | 5 | 1 | +0.5 | 0.05 | -0.05 | 0.00 | -0.05 |
| 3 | S2 | 6 | 1 | +0.5 | 0.05 | 0.00 | 0.00 | -0.05 |
| 4 | S2 | 2 | 0 | -0.5 | 0.05 | -0.05 | 0.00 | -0.05 |
| 5 | S1, S2, S3, S4 | 4 | 1 | +0.5 | 0.10 | 0.00 | 0.05 | 0.00 |
| 6 | S2 | 1 | 0 | -0.5 | 0.10 | -0.05 | 0.05 | 0.00 |
| 7 | S1 | 3 | 1 | +0.5 | 0.15 | -0.05 | 0.05 | 0.00 |
| 8 | S1, S3 | 2 | 1 | +0.5 | 0.20 | -0.05 | 0.10 | 0.00 |
| 9 | S1, S3, S4 | 6 | 1 | +0.5 | 0.25 | -0.05 | 0.15 | 0.05 |
| 10 | S1 | 3 | 1 | +0.5 | 0.30 | -0.05 | 0.15 | 0.05 |
| 11 | S4 | 1 | 0 | -0.5 | 0.30 | -0.05 | 0.15 | 0.00 |
| 12 | S2, S3, S4 | 6 | 1 | +0.5 | 0.30 | 0.00 | 0.20 | 0.05 |

Final: w1 = 0.30, w2 = 0.00, w3 = 0.20, w4 = 0.05, matching the printed check. Ranking: S1 > S3 > S4 > S2. (Note that S1 was active five times and rewarded all five; trial 2's outcome of 5 and trial 7's outcome of 3 reward because S1 was active and the roll was not 1.)
6) S3 was active on trials 5, 8, 9, and 12 and was rewarded every time. S1 was co-active on trials 5, 8, and 9 (S3 rode on S1's success). On trial 12 S1 was inactive and the reward came from the 1-in-6 chance (outcome roll 6). S3 was never active on an unrewarded trial, so it never got blamed.
7) Model answer (see "Learning Under Uncertainty" and "Credit Assignment"):
- Yes, S1 ends strongest, but only by 0.10 after 12 trials; the margin is small and S3 is a close second.
- S3 gained undeserved credit through coincident activity with S1 plus one lucky reward. The scalar signal cannot tell co-active synapses apart, so every active synapse shares the credit.
- This is not a bug in the sense of a design failure; it is the expected cost of a cheap, label-free learning rule. Each update is small and sometimes wrong, but errors average out.
- Over many trials, S2 to S4 have an expected change of zero per trial: they are independent of S1, and overall P(reward) = 0.5 x 5/6 + 0.5 x 1/6 = 0.5, which equals V. S1's expected change is 0.5 x 0.1 x (5/6 - 0.5) = +0.0167 per trial, so after 100 more trials S1 should gain about 1.7, while S3 does a random walk around 0.20 with a standard deviation of about 0.35. S1 separates clearly.
- "Bias here does not mean error": the learner acquires a statistical tendency toward what has worked, a gradual shaping of probability under uncertainty (Thorndike's law of effect with a mechanism).
- Strong answers note that V is held fixed here; a real learner would also update V, which would shrink delta as the predictions improve. Common mistake: concluding that S3 is causal, or that the rule "failed."

Optional extension (instructor reference from a 200-run simulation, separation criterion w1 exceeding every other weight by 0.5): about 37 trials (median) with the original rule (5/6 vs 1/6), about 140 trials with the noisy version (0.6 vs 0.4). Non-causal weights hover near zero in both. Weights grow without bound because V is fixed.

## Lab 3.4 - Gated Versus Ungated Plasticity (why activity alone should not decide learning)

1) Ungated: w after trials 1 to 10 = 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2.
2) Gated: 0.20, 0.20, 0.20, 0.25, 0.25, 0.25, 0.25, 0.25, 0.20, 0.20.
3) Ungated ends at 1.2 (six times the start) from pure coincidence; gated ends at 0.20, unchanged, because the positive and negative errors cancel and coactivity alone changes nothing.
4) delta = +0.5 every trial: ungated still 0.2 + 10 x 0.1 = 1.2; gated 0.2 + 10 x 0.05 = 0.7.
5) Under the ungated rule the meaningless (Part A) and meaningful (Part B) relationships produce identical weights; the rule cannot tell them apart. The gated rule strengthens only the relationship that predicts success (0.7 vs 0.2).
6) Ungated: 100 synapses change per trial; 100,000 synapse updates over 1,000 trials (each of the 5,000 synapses changed about 20 times on average if coincidences are spread evenly). Gated: changes occur only on the 10 percent of trials with nonzero delta, so 100 trials x 100 synapses = 10,000 updates, an average of 10 per trial, a tenfold reduction, and those updates are the ones tied to surprising outcomes.
7) Model answer (see "Fast Signals and Slow Control" and "Implications for Artificial Intelligence"):
- Gating protects against runaway growth driven by coincidence, and against overwriting stored knowledge (the stability-plasticity dilemma): if every fluctuation produced a lasting change, the brain would forget as fast as it learned.
- It ties plasticity to relevance: only activity followed by better- or worse-than-expected outcomes is kept.
- Cost: a genuinely useful coincidence that occurs when delta = 0 (for example, a predictive feature noticed while everything is already going as expected, or a relationship that is not reward-related) is not learned. Errors are also needed to learn at all, so already-predicted relationships stop being refined.
- Strong answers note the chapter's nuance that plasticity can be induced by pre- and postsynaptic activity alone in slices; neuromodulators gate, scale, and decide consolidation in the intact brain, so real gating is graded rather than all-or-none. Other modulators (acetylcholine, norepinephrine) also open the gate for non-reward contexts such as novelty or attention.
- "No change lasts unless the context says it should": the decision to learn is made internally by neuromodulatory context, unlike the external train/deploy switch of artificial networks. Common mistake: treating the gated rule as simply "slower Hebbian learning."

## Lab 3.5 - Neuromodulators as Design Primitives (comparison table and concept map)

1) to 3) Reference table (see "Norepinephrine, Serotonin, and Acetylcholine," "Dopamine: Schultz's Monkeys," and the Student Notes reference table). Accept reasonable variation, especially in the AI-analogue column; guesses must be marked.

| System | Source | Context signaled | Timescale | Effect on plasticity | Effect on ongoing processing | Nearest AI analogue |
|---|---|---|---|---|---|---|
| Dopamine | VTA and substantia nigra pars compacta (midbrain) | Reward prediction error (large population); some neurons also novelty, salience, aversion, movement | Bursts about 100 ms, dips a few hundred ms, on a slow tonic level | Third factor: bursts drive potentiation, dips the opposite change, at recently active (eligible) striatal synapses | Biases action selection and motivation toward options better than expected | TD / reward prediction error term |
| Norepinephrine | Locus coeruleus (pons) | Surprise and arousal; unexpected uncertainty (the world has changed) | Phasic hundreds of ms; tonic shifts over minutes | Raises plasticity under surprise; with acetylcholine, needed for cortical rewiring (kitten eye-closure result) | Sets cortical gain; phasic mode focuses, tonic mode disengages and explores | Exploration temperature, or learning-rate boost on detected change |
| Serotonin | Raphe nuclei (dorsal and median) | Least settled: patience and waiting, aversion, inhibition, plasticity regulation | Seconds to minutes | Regulates plasticity (mechanism unsettled) | On one account, holds a course of action against immediate alternatives | Discount factor (Doya), or persistence/temporal horizon (mark as tentative) |
| Acetylcholine | Nucleus basalis of Meynert, medial septum, PPN/LDT | Expected uncertainty; encoding vs recall | Seconds, faster local release | Permits cortical map plasticity (nucleus basalis pairing expands tone map); favors encoding | Suppresses recurrent (pattern-completing) synapses, spares incoming input | Attention weighting, or learning-rate schedule / write-vs-read switch |

Doya's mapping (see "Implications for Artificial Intelligence"): dopamine = error signal, serotonin = discount, norepinephrine = exploration (inverse temperature), acetylcholine = learning rate. Students who use it should cite it; students who choose different analogues should justify them.

4) to 8) Concept map, required nodes: sensory input, decision neuron, action, outcome, prediction (V), dopaminergic neuron computing delta = outcome - prediction, broadcast arrow over all synapses, eligibility-trace clocks at each synapse, gates at each synapse, norepinephrine source, acetylcholine source.
Key labeled links:
- input -> decision neuron (synapse with clock that starts on use);
- decision neuron -> action -> outcome;
- outcome and prediction -> dopamine neuron ("compares");
- dopamine -> all synapses ("broadcasts delta, volume transmission");
- gate opens only if "delta nonzero AND clock not expired" -> weight change (sign from delta);
- norepinephrine -> gates ("surprise widens gate / raises gain");
- acetylcholine -> circuit ("high: encode new input; low: recall/replay").
9) Caption grading guide (8 to 12 sentences): a strong caption follows one trial in order: input activates a synapse and starts its clock; the decision neuron fires and an action follows; the outcome arrives seconds later; dopamine compares it with the prediction and broadcasts delta; only synapses whose clocks are still running change, in the direction of delta; norepinephrine, if the outcome was surprising, widens the gate; acetylcholine sets whether the circuit is encoding the new input or retrieving. It should end with the effect on the next trial (prediction updated, behavior biased). Common mistakes: dopamine delivered only to the "right" synapse; no timing constraint on the gate; NE and ACh described as carrying content.
10) Design memo grading guide (10 to 14 sentences, argue either side):
- Must address stability (gating prevents coincidental and catastrophic updates; supports continual learning after deployment, implication one: "the brain separates activity from learning").
- Must address credit assignment (eligibility traces plus a scalar error give approximate, delayed credit; implication three: "approximate credit assignment can be enough," random feedback weights).
- Must address what is lost versus backpropagation: exact per-weight gradients, sample efficiency, convergence guarantees; a scalar broadcast scales poorly with many parameters and is noisy.
- Should use at least two of the four implications (activity vs learning separated internally; state-dependent learning rules, Doya's mapping and learned modulatory gates; approximate credit assignment; many local objectives rather than one global loss, with viability as a constraint).
- Strong answers propose a hybrid (for example, backpropagation inside modules, modulatory gating of when and how much to learn) and name a concrete risk (reward hacking of the modulatory signal, or slow learning). Common mistakes: claiming the brain has no objectives at all (the chapter says many local ones, no global one), or claiming backpropagation is impossible in the brain (the chapter calls it an open question).

### Notes for instructors

None beyond the answers above.

# Chapter 4: Circuits, Networks, and Coordinated Behavior

## Lab 4.1 - Feedforward Inhibition as a Coincidence Detector

Setup: In excites E directly and excites interneuron I, which inhibits E (filled circle), as in Figure 4.1B. Convention used below: each step, decay first (V = -70 + 0.8 x (V + 70)), then add +3 mV per EPSP and -3 mV per IPSP; "spike" means V at or above -63 mV. The model has no reset, so V is simply followed after a crossing.

1) Tight timing, no interneuron: t = 0: two EPSPs, V = -64.00 (matches check). t = 1: decay to -65.20, plus one EPSP = -62.20, threshold crossed. First spike at t = 1 ms. Afterward V decays: -63.76, -65.01, -66.01.
2) Spread timing, no interneuron (V after inputs): t0 -67.00, t1 -67.60, t2 -65.08, t3 -66.06, t4 -63.85 (matches check), t5 -65.08, t6 -63.06, t7 -64.45, t8 -62.56 (crossed), t9 -64.05, t10 -65.24. First spike at t = 8 ms: the sluggish integrator eventually sums even well-separated inputs.
3) Tight timing, with interneuron: IPSPs arrive at t = 2 (two) and t = 3 (one). The spike at t = 1 has already happened, so the IPSPs arrive too late to prevent it; they only cut the tail (t2 -69.76, t3 -72.81, t4 -72.25, t5 -71.80), resetting E quickly for the next event.
4) Spread timing, with interneuron: each IPSP (t = 2, 4, 6, 8, 10) lands on the same step as the next EPSP and cancels it. V: t0 -67.00, t1 -67.60, t2 -68.08, t3 -68.46, t4 -68.77, t5 -69.02, t6 -69.21, t7 -69.37, t8 -69.50, t9 -69.60, t10 -72.68. No spike; V drifts back toward rest.
5) 2 x 2 table:

| | Without inhibition | With inhibition |
|---|---|---|
| Tight timing | spike at t = 1 ms | spike at t = 1 ms |
| Spread timing | spike at t = 8 ms | no spike |

6) Model answer (see "A Small Vocabulary of Motifs"):
- The interneuron changed only the spread case: it removed the response to straggling inputs and left the response to near-coincident inputs intact.
- The 2 ms delay is the point: it defines the integration window. Inputs that arrive within the delay sum before inhibition lands; any input arriving later is met by the inhibition from earlier inputs. Without the delay (simultaneous IPSP) every EPSP would be canceled and nothing would ever fire; with a much longer delay the window widens and timing precision is lost.
- Ten spread inputs without inhibition: V keeps climbing toward a ceiling of about -61.7 mV just after each input, crossing threshold at t = 8, 10, 12, 14, 16, and 18 ms (six crossings). With inhibition: still no spike (V hovers near -69.5 to -70 mV). The integrator responds to a long, slow train; the coincidence detector never does.
- The chapter places this motif wherever timing precision matters, "from the cerebellum to the auditory brainstem," and in the cortex, where feedforward inhibition sharpens the timing of thalamic input to layer 4 (see "The Cortical Microcircuit").
- Common mistake: saying inhibition "reduces responses in general"; the point is selectivity for timing.

## Lab 4.2 - Excitation-Inhibition Balance by Hand

Net recurrent gain on e (useful for interpretation): 1.5 - 0.5 x g x 1.2 = 1.5 - 0.6g. It exceeds 1 (runaway) for g below about 0.83.

1) g = 0:

| Step | Input | e | i |
|---|---|---|---|
| 1-3 | 0.6 | 0 | 0 |
| 4 | 1.6 | 0.80 | 0.96 |
| 5 | 1.6 | 2.00 | 2.40 |
| 6 | 0.6 | 2.80 | 3.36 |
| 7 | 0.6 | 4.00 | 4.80 |
| 8 | 0.6 | 5.00 (clipped from 5.8) | 6.00 |
| 9-10 | 0.6 | 5.00 (clipped from 7.3) | 6.00 |

Matches all checks: ceiling at step 8 and stays there after the input ends.

2) g = 1.6: steps 1-3 e = 0; step 4 e = 0.80, i = 0.96; step 5 e = 1.232, i = 1.478 (check 1.23, 1.48); step 6 e = 0.465, i = 0.558; step 7 e = 0.051, i = 0.062; step 8 onward e = 0 (raw -0.172 at step 8). Matches check.
3) g = 3.5: step 4 e = 0.80, i = 0.96; step 5 e = 0.32, i = 0.384; step 6 raw -0.392, so e = 0 from step 6 on. Peak 0.80. Matches check.
4) Plot: three curves identical through step 4 (0.80); g = 0 climbs to the ceiling of 5 and stays; g = 1.6 peaks at 1.23 at step 5 and returns to 0 by step 8; g = 3.5 drops at step 5 (0.32) and is 0 from step 6, even though the input is still high at step 5.
5) The motif is feedback inhibition (the target's own activity recruits the interneuron population, which suppresses it; "a thermostat"). The chapter's "Rhythms" section explains that feedback inhibition is intrinsically rhythmic when the inhibition is slower: excitation recruits inhibition, inhibition silences excitation, decays, and excitation recovers (the gamma mechanism of excitatory cells coupled to fast interneurons). Here the inhibition follows instantly, so the loop is damped rather than oscillating.
6) Model answer (see "Inhibition Is Not the Opposite of Excitation"):
- Balance is the only regime that is both sensitive and stable: a large response to a brief input (1.23 at step 5) that ends when the input ends.
- Balance keeps neurons near threshold, so a single well-timed input can flip them; this is why balanced circuits are fast ("Inhibition is not the brake on the system. It is what makes the system responsive.").
- The cost is energy: two large opposing currents are spent to produce a small net effect.
- No inhibition: runaway to the ceiling that outlasts the input, a seizure in miniature; recurrent excitation is "the most dangerous motif in the brain." It also leaves the circuit unable to signal anything further (saturated).
- Too much inhibition: a muted, truncated response; the organism loses sensitivity and may miss weak or brief events.
- Strong answers mention that real balance is tracked dynamically (inhibition arrives a few ms after each excitatory input) and is maintained by separate E and I populations (Dale's principle). Common mistake: equating balance with "zero activity."

Optional extension (instructor reference, noise-free): g = 0 to 0.6 saturates at 5 and never returns; g = 0.8 peaks at 1.62 and returns within 10 percent of baseline at step 14; g = 1.0 to 2.0 gives peaks of 1.52 down to 1.04 with return by steps 10 to 7; from g of about 2.6 upward the peak is pinned at 0.80 (the first input step) and return is at step 6. The "large and brief" range is roughly g = 0.9 to 2.0, with the boundary set by loop gain 1.5 - 0.6g crossing 1 near g = 0.83. Noise will blur the boundaries slightly.

## Lab 4.3 - A Half-Center Oscillator in Twenty Steps

1) Diagram: L and R with mutual inhibitory synapses (filled circles), a constant drive arrow onto each, and a fatigue label (u, v) on each.
2) Table (synchronous update, fatigue gain 0.4):

| Step | x | y | u | v |
|---|---|---|---|---|
| 1 | 1.000 | 0.000 | 0.200 | 0.000 |
| 2 | 0.800 | 0.000 | 0.560 | 0.000 |
| 3 | 0.440 | 0.000 | 0.768 | 0.000 |
| 4 | 0.232 | 0.000 | 0.790 | 0.000 |
| 5 | 0.210 | 0.420 | 0.725 | 0.000 |
| 6 | 0.000 | 0.476 | 0.664 | 0.168 |
| 7 | 0.000 | 0.832 | 0.531 | 0.325 |
| 8 | 0.000 | 0.675 | 0.425 | 0.593 |
| 9 | 0.000 | 0.407 | 0.340 | 0.744 |
| 10 | 0.000 | 0.256 | 0.272 | 0.758 |
| 11 | 0.089 | 0.242 | 0.218 | 0.709 |
| 12 | 0.178 | 0.070 | 0.209 | 0.664 |
| 13 | 0.616 | 0.000 | 0.239 | 0.559 |
| 14 | 0.761 | 0.000 | 0.438 | 0.447 |
| 15 | 0.562 | 0.000 | 0.655 | 0.358 |
| 16 | 0.345 | 0.000 | 0.749 | 0.286 |
| 17 | 0.251 | 0.000 | 0.737 | 0.229 |
| 18 | 0.263 | 0.143 | 0.690 | 0.183 |
| 19 | 0.000 | 0.159 | 0.657 | 0.204 |
| 20 | 0.000 | 0.796 | 0.526 | 0.227 |

Checks match: step 4 x = 0.23, y = 0, u = 0.79; step 7 y = 0.83.
3) Active side (larger activity) switches L to R at step 5, R to L at step 12, L to R at step 19. Half-period about 7 steps; full period about 14 steps (a 200-step run gives switches every 6 to 7 steps, period about 13.5).
4) Fatigue gain 0.2: no alternation. L settles to a steady state x = 0.5, u = 0.5 (fixed point x = 1 - u with u = x) and holds R silenced, since 1 - 2.5 x 0.5 = -0.25. The period does not lengthen; it becomes infinite: the rhythm does not survive. Reason: fatigue must push the winner's activity below 0.4 (where 1 - 2.5x becomes positive and the loser escapes). At steady state x = 1/(1 + 5a), which is below 0.4 only if a > 0.3.
5) Fatigue gain 0: x = 1.0 and y = 0 on every step; L wins and R is permanently suppressed. This is winner-take-all selection, the lateral (mutual) inhibition motif.
6) Model answer (see "Circuits That Generate Their Own Rhythm"):
- Two ingredients: mutual inhibition (only one side can be active) and fatigue in the active side (adaptation or synaptic depression). Remove fatigue and you get winner-take-all (step 5); weaken it and the circuit locks (step 4).
- The drive can be constant because the timing comes from the circuit's own dynamics: the fatigue time constant sets the period. The isolated spinal cord generates locomotor alternation from steady chemical or electrical drive.
- Sensory feedback does not drive the rhythm; it tunes timing and amplitude so walking survives perturbations ("The brain generates behavior, and the world corrects it").
- Strong answers note that drive strength and fatigue rate are the natural control knobs for speed, and connect to reciprocal inhibition in the reflex. Common mistake: claiming the rhythm requires rhythmic input from the brain.

Optional extension: the lab applies the stone at step 140 (x = 0.291 at that step, the tail of an L burst), after computing the step. The rhythm recovers within one cycle and continues alternating with no lockup (in a 400-step run, x never equals y in the last 20 steps). The lab then asks students to try step 150, and warns that a stone early in a burst can lock the synchronous model into a symmetric period-2 state (both sides at 0.474, then both at 0, forever); this happens for stone steps 136 to 139 and 150 to 153. Note that a stone at steps 143 to 147 does nothing, since x is already 0 there. Adding the suggested sensory feedback term (D raised by 0.1 for the more fatigued side) restores alternation for every stone step from 130 to 159, which is a nice demonstration of feedback tuning.

## Lab 4.4 - Selection by Disinhibition (a paper basal ganglia)

Release threshold: output inhibition below 0.3, i.e., striatal activation above 0.7.

1) G = 1.0: striatal 0.9, 0.6, 0.3; inhibition 0.1, 0.4, 0.7. Only A is released.
2) G = 0.5: striatal 0.45, 0.30, 0.15; inhibition 0.55, 0.70, 0.85. Nothing is released. This matches Parkinson's disease: loss of the dopamine that biases the striatum toward release gives too little movement, slowness, and difficulty starting (see "Two Loops for Action").
3) G = 1.5: striatal 1.35, 0.90, 0.45; inhibition 0, 0.10, 0.55. A and B are both released. The animal would show excess, competing, or poorly suppressed movements (restless, impulsive, mixing two actions). The chapter's hyperkinetic examples arise differently: Huntington's disease destroys indirect-pathway striatal neurons, and subthalamic lesions cause hemiballismus, both by losing the brakes on competing actions rather than by excess dopamine; the behavioral result (too much movement) is similar.
4) G = 1.0, B drive 0.8: striatal 0.9, 0.8, 0.3; inhibition 0.1, 0.2, 0.7. A and B are now both released, so selection has changed from "A only" to "A and B." A is still the most disinhibited, but B has crossed the release threshold; with further rewarded trials B's drive could overtake A's. The paper model lacks the indirect pathway that raises inhibition on competitors, which in the real circuit would resolve the conflict. The learning rule is the three-factor rule (dopamine reward prediction error at recently active corticostriatal synapses) from Chapter 3.
5) All drives 0.1: argmax releases one action anyway (with a three-way tie it must pick arbitrarily). Disinhibition gives inhibition 0.9 for all three, so nothing is released: "do nothing." The chapter calls "do nothing" a first-class action because the default of silence makes not acting the outcome when no candidate is compelling, which is often right for an agent under uncertainty (see "Implications for Artificial Intelligence"). It still does not fail safe: losing the release signal (Parkinson's) gives too little movement, and losing the brakes (Huntington's, subthalamic lesion) gives too much; the circuit has two recognizable failure modes in opposite directions, not a single safe one.
6) Model answer (see "Two Loops for Action" and "Implications for Artificial Intelligence"):
- Default-off means actions require positive evidence to be released; weak or ambiguous proposals produce no action rather than a random one.
- Selection is a threshold on evidence, not a forced choice, so the organism can wait, gather information, or keep still.
- Dopamine gain sets the threshold's effective level, letting learning and motivation tilt release toward actions that have paid off (habits).
- Costs: tonic inhibition is metabolically expensive (the output nuclei fire continuously); responses may be delayed; the circuit can fail in either direction (akinesia vs hyperkinesia); and without competitor inhibition, multiple actions can be released at once (Part D).
- Common mistakes: describing the basal ganglia as "choosing the largest," or claiming default-off is fail-safe.

## Lab 4.5 - Small Worlds on a Ring (wiring cost versus path length)

1) Ring of 12 nodes, 12 edges.
2) From node 0: 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1; sum 36; average 36/11 = 3.27.
3) Average 3.27, longest 6, cost 12 (matches check).
4) Add 0-6 and 3-9 (cost 6 each): total cost 12 + 12 = 24 (matches check).
From node 0 (to 1 through 11): 1, 2, 3, 3, 2, 1, 2, 3, 3, 2, 1; average 23/11 = 2.09; max 3.
From node 1: 1, 1, 2, 3, 3, 2, 3, 4, 3, 3, 2 (to 0, 2, 3, ..., 11); average 27/11 = 2.45; max 4 (to node 7).
Average of the two sets: 50/22 = 2.27. Longest path 4 (matches check). (All-pairs average for reference: 2.33; diameter 4.)
5) Distance-1 and distance-2 neighbors (24 edges): from node 0: 1, 1, 2, 2, 3, 3, 3, 2, 2, 1, 1; average 21/11 = 1.91; longest 3; cost 12 x 1 + 12 x 2 = 36 (matches check).
6) Table:

| Design | Avg path length | Longest path | Wiring cost |
|---|---|---|---|
| Ring (nearest neighbors) | 3.27 | 6 | 12 |
| Ring + two shortcuts | 2.27 (all pairs 2.33) | 4 | 24 |
| Dense local (distance 1 and 2) | 1.91 | 3 | 36 |

7) Model answer (see "The Architecture of the Whole"):
- Path-length reduction per unit of extra wire: shortcuts 1.00/12 = 0.083 per unit (two edges cut the longest path from 6 to 4); dense local 1.36/24 = 0.057 per unit (twelve extra edges). The shortcuts give the larger reduction per unit of wire and per edge added.
- The brain pays for every axon in metabolism, volume, and conduction delay, so it keeps most wiring local (cheap, supports clustered local computation) and adds a few long tracts that collapse path length: a small-world network.
- Damage to node 0: in Part A the ring becomes a chain of 11 nodes, average path among survivors 4.00 and longest 10. In Part B, losing node 0 also loses shortcut 0-6: average 2.73, longest 5, still better than the intact ring, because the 3-9 shortcut survives. But node 0 was a hub (degree 3) in Part B, and removing it raised the survivors' average from 2.33 to 2.73; in the dense network the same damage barely matters (1.91 to 1.93). Hubs make the network efficient and also fragile; the chapter's rich-club and "disorders of the hubs" (26 disorders, gray matter loss concentrated in hubs) make the same point.
- Strong answers mention conduction delay as well as cost, and note that the small-world claim is shown neuron by neuron only in C. elegans and is an extrapolation at the single-neuron level in mammals. Common mistake: concluding that "more wiring is always better."

Optional extension (instructor reference: 200 nodes, k = 4, 5 seeds per p): p = 0: L = 25.4, C = 0.50. p = 0.01: L = 13.4, C = 0.48. p = 0.03: L = 9.5, C = 0.45. p = 0.1: L = 6.1, C = 0.38. p = 0.3: L = 4.7, C = 0.21. p = 1: L = 4.0, C = 0.01. The small-world regime is roughly p = 0.01 to 0.1, where path length has fallen by half or more while clustering is still above about 75 percent of the regular lattice's value.

## Lab 4.6 - From Reflex to Coordinated Behavior (concept map)

Required nodes and key labeled links:
1) Stretch reflex: muscle spindle sensory neuron -> (excitatory) motor neuron of the same muscle (quadriceps); sensory neuron -> (excitatory) inhibitory interneuron -> (filled circle) antagonist motor neuron (hamstrings). Motif: reciprocal inhibition (feedforward excitation plus inhibition). See "The Simplest Circuit."
2) Half-center oscillator: two populations with mutual inhibitory links, fatigue labels, constant descending drive, outputs to the same motor neurons; sensory feedback arrow labeled "tunes timing/amplitude, does not drive." Motifs: mutual (lateral) inhibition plus fatigue.
3) Cortical column: thalamus -> layer 4 -> layers 2/3 -> layer 5 -> brainstem/spinal cord (pattern generator) and basal ganglia; layer 6 -> thalamus (loop). Motifs: feedforward inhibition at thalamic input, recurrent excitation in layers 2/3, feedback and lateral inhibition bounding it.
4) Basal ganglia: cortex (layer 5) -> striatum -> (inhibitory) output nuclei -> (tonic inhibition) thalamus; dopamine (Chapter 3, reward prediction error) -> striatum. Motif: disinhibition. Optional: indirect and hyperdirect pathways. Cerebellum: parallel fibers (context, many weak) and one climbing fiber labeled "error" -> Purkinje cell -> deep nuclei; label "coincidence weakens recently active parallel-fiber synapses."
5) Hippocampal loop: EC -> DG (pattern separation, sparse, strongly inhibited) -> CA3 (recurrent excitation, pattern completion) -> CA1 (comparator hypothesis; direct EC input) -> EC, connected to the column.
6) Rhythm: sine wave across column and hippocampus (for example theta in hippocampus, gamma locally); note that on communication-through-coherence, the sender's spikes should arrive at the receiver's excitable phase (aligned phases communicate); mark the hypothesis as contested (coherence can arise from connectivity alone; gamma frequency shifts with stimulus).
7) Three more columns with mostly short edges and one long edge: small-world wiring (local clusters, few long tracts).
8) Filled circles at every inhibitory synapse (reciprocal interneuron, half-center links, cortical interneurons, striatum and output nuclei, Purkinje cell output, DG inhibition). All six motifs named somewhere: feedforward excitation, feedforward inhibition, feedback inhibition, lateral inhibition, recurrent excitation, disinhibition.
9) Caption grading guide (10 to 14 sentences). A strong caption:
- Knee tap: spindle stretch -> monosynaptic excitation of quadriceps motor neurons; reciprocal inhibition silences hamstrings; no brain needed.
- One step: descending constant drive to the spinal half-center oscillator; alternation from mutual inhibition plus fatigue; sensory feedback adjusts timing (stone underfoot); cerebellum refines precision using error signals; cortex and basal ganglia have released "walk."
- Decision to stop: cortex represents "stop" among candidates; basal ganglia release it (or the hyperdirect path halts everything); dopamine history biases which action is released; the output reaches the pattern generator, whose drive is withdrawn.
- Optionally: hippocampal loop supplies memory of the route; rhythms may coordinate which regions communicate.
- Ends with why no part is in charge: each circuit solves a local problem with the same small set of motifs, and coordinated behavior is what the parts produce together (see "Coordination Without a Conductor").
- Common mistakes: making cortex a central controller; letting sensory feedback generate the rhythm; omitting inhibition.

### Notes for instructors
- Lab 4.5 step 4: the "average the two sets" value (2.27) differs from the true all-pairs average (2.33). Not wrong as instructed, but worth a footnote.

# Chapter 5: Plasticity and Memory: How Experience Becomes Structure

## Lab 5.1 - Hebb Runs Away (and one way to stop it)
1) Since x = 1 and y = w, the rule reduces to w_next = 1.1 w. Values of w after steps 1 to 10: 1.100, 1.210, 1.331, 1.464, 1.611, 1.772, 1.949, 2.144, 2.358, 2.594 (y at each step equals the w before it). Checks of 1.464 and 2.594 confirmed.
2) w grows by a factor of 1.1 per step (10 percent compound growth). After 50 steps w = 1.1^50 = 117.4. It never stops: the only fixed point is w = 0, and it is unstable, since any positive w grows (see "Hebb's Rule and Its Problem").
3) With x = 1, Oja's rule is w_next = w + 0.1 w (1 - w^2). At w = 1.0 the change is exactly 0, so w stays at 1.000 for all ten steps. 1.0 is special because it is the fixed point where Hebbian growth (0.1 y x) is exactly balanced by the decay (0.1 y^2 w); with unit input, the rule normalizes w to length one.
4) From w = 0.3: 0.327, 0.357, 0.388, 0.421, 0.455, 0.491, 0.529, 0.567, 0.605, 0.643 (exact 0.6435). Checks confirmed. It is heading up to 1.0, with growth slowing as it approaches.
5) From w = 1.5: 1.313, 1.218, 1.159, 1.119, 1.091. It moves down toward 1.0. So 1.0 is a stable fixed point, approached from both sides.
6) Model answer: the extra term (-0.1 y^2 w) is a decay proportional to the square of the output, so the more the neuron fires, the more the synapse weakens; it bounds total strength and turns runaway into convergence on a fixed point. It keeps the Hebbian logic (correlated activity still strengthens weak synapses) but adds the weakening and the bound that "Hebb's Rule and Its Problem" says a working rule needs. Biological counterparts: the activity-dependent sliding threshold (BCM) and multiplicative synaptic scaling ("Keeping the Whole Neuron Stable"), and the weakening supplied by LTD and STDP ("LTP and LTD", "Timing Is Causation"). With only the Hebbian term, every active synapse would saturate, the neuron would fire to everything, and the selectivity that encodes what was learned would be erased. Strong answers note that Oja's decay is per synapse and output dependent, whereas scaling acts on all synapses multiplicatively and preserves ratios.

## Lab 5.2 - One Signal, Two Directions (calcium control)
1) Drawing: a spine with presynaptic glutamate release, AMPA receptors (sodium in, depolarization) and NMDA receptors with a magnesium plug, calcium entering through unplugged NMDA receptors, and the back-propagating spike arriving from the soma (Figure 5.1, "The Coincidence Detector").
2) Table (crossover 1.4):
   - 1 input, no spike: calcium 0.3, no change.
   - 3 inputs, no spike: 0.9, LTD (-0.2). Check confirmed.
   - 5 inputs, no spike: 1.5, LTP (+0.4).
   - 1 input + spike: 1.3, LTD (-0.2).
   - 2 inputs + spike: 1.6, LTP (+0.4). Check confirmed.
   - 4 inputs + spike: 2.2, LTP (+0.4).
3) A weak input that merely coincides with a spike driven by other inputs is weakened, not strengthened: coincidence alone is not enough, the input must contribute enough calcium itself. This sharpens selectivity: inputs that are only along for the ride lose ground to the inputs that actually drive the cell, which is the "criterion for which correlations count" the chapter says Hebb lacked ("Hebb's Rule and Its Problem", "LTP and LTD").
4) Crossover at 2.0: 1 input 0.3 none; 3 inputs 0.9 LTD; 5 inputs 1.5 LTD (was LTP); 1 + spike 1.3 LTD; 2 + spike 1.6 LTD (was LTP); 4 + spike 2.2 LTP. Two outcomes flipped from LTP to LTD; only the strongest case still potentiates.
5) Model answer: one calcium signal encoding both directions means a single mechanism, the NMDA receptor, provides both strengthening and the weakening that Hebb's rule lacked, with amount (and time course) selecting kinases versus phosphatases ("LTP and LTD"). This keeps the decision local and automatically ties LTD to weak or poorly timed activity. It also makes the rule tunable with a single parameter, the crossover, which is how the sliding threshold works ("Keeping the Whole Neuron Stable"). A neuron with a fixed crossover during a day of intense input would push more and more synapses above 1.4, potentiate them, fire more, and run away toward saturation, losing selectivity and wasting energy; with a sliding crossover the same intense input increasingly produces LTD, returning the cell toward its set point.

## Lab 5.3 - Timing Is Causation (STDP on a chain)
1) Drawing of A, B, C and six directed synapses.
2) Table (dt = t_post - t_pre):
   - A to B: dt +10, +0.555. A to C: +20, +0.308. B to C: +10, +0.555.
   - B to A: -10, -0.373. C to A: -20, -0.278. C to B: -10, -0.373.
   Checks confirmed.
3) All forward synapses (A to B, B to C, A to C) are strengthened; all backward synapses are weakened. A feedforward chain A to B to C emerges, strongest between neighbors in time, with a weaker skip connection A to C; the circuit has learned the firing order.
4) B at 40 ms: A to B dt +40, +0.095 (check confirmed); B to C dt -20, -0.278 (check confirmed). Also C to B becomes +0.308 and B to A -0.154. The rule now treats B as an effect of C (and only weakly of A), not a cause of C. That is reasonable: B fired after C, so B could not have helped cause C's spike, and with a 40 ms lag A is a weak candidate cause of B.
5) Model answer: the window is causal because only an input that arrives just before the postsynaptic spike can have contributed to it ("Timing Is Causation"). Mechanistically, glutamate bound first plus a back-propagating spike shortly after expels magnesium and gives a large calcium pulse (LTP); a spike before glutamate leaves only a small slow calcium rise (LTD), which links directly to Lab 5.2. STDP supplies the weakening Lab 5.1 lacked, applied specifically to out-of-order connections, so total strength does not only climb. If all neurons fired at exactly the same time, dt = 0 for every pair: there is no order to read, the lab's window gives no change at dt = 0, and no directed structure can form. With small timing jitter, each pair is randomly potentiated or depressed, and because the two lobes have equal area (1.0 x 17 = 0.5 x 34 = 17) the net drift is near zero, so weights wander rather than encode anything. Strong answers add that perfectly synchronous recurrent firing is itself the seizure-like regime the whole-neuron stabilizers must prevent ("Keeping the Whole Neuron Stable").
   Optional extension: with 8 ms spacing, forward neighbors reach 1.0 within a few passes; jitter up to roughly the spacing (8 ms) preserves the forward structure, while 15 ms jitter visibly degrades it (expect students to report qualitative results; exact numbers depend on the random seed).

## Lab 5.4 - The Sliding Threshold (a self-correcting neuron)
1) From w = 0.5, theta = 0.5 (values after each step, w then theta): 1) 0.500, 0.425 (change 0, since y = theta); 2) 0.504, 0.373; 3) 0.510, 0.337; 4) 0.519, 0.314; 5) 0.530, 0.301; 6) 0.542, 0.295; 7) 0.555, 0.294; 8) 0.570, 0.299; 9) 0.585, 0.307; 10) 0.602, 0.317; 11) 0.619, 0.331; 12) 0.637, 0.346; 13) 0.655, 0.364; 14) 0.674, 0.384; 15) 0.694, 0.405. Changes grow from 0.004 to about 0.020 per step. Check (0.530, 0.301) confirmed.
2) From w = 2.0: 1) 2.300, 1.550 (change +0.300); 2) 2.473, 2.672 (+0.173); 3) 2.423, 3.704 (-0.049); 4) 2.113, 4.355 (-0.311); 5) 1.639, 4.387 (-0.474); 6) 1.189, 3.877; 7) 0.869, 3.138; 8) 0.672, 2.423; 9) 0.554, 1.832; 10) 0.483, 1.374; 11) 0.440, 1.032; 12) 0.414, 0.781; 13) 0.399, 0.598; 14) 0.391, 0.466; 15) 0.388, 0.372. Checks (1.639, 4.387; 0.388) confirmed.
3) The change first becomes negative at step 3 (y = 2.473 but theta has risen to 2.672). The threshold, tracking y^2 of recent steps, climbed past the output: intense firing raised theta until the same input produced depression. A second, smaller switch back to positive occurs at step 16, once theta (0.372) has fallen below y (0.388); the undershoot is then corrected upward.
4) At a fixed point, change = 0 requires y = theta (or y = 0), and theta unchanged requires theta = y^2. Together y = y^2, so y = 1 and theta = 1 (w = 1). Both runs converge there slowly with damped oscillation (run one reaches about 1.02 near step 40 before settling; the trivial point y = 0 is unstable for small positive w).
5) Model answer: the pure Hebbian neuron of Lab 5.1 grew without bound; here growth is self-limiting because theta tracks the square of recent output ("Keeping the Whole Neuron Stable", Figure 5.4A). When the neuron fires a lot, theta rises above y and the same input produces depression; when it is quiet, theta falls and potentiation becomes easy, so the neuron neither runs away nor dies. Because theta grows faster than y (as y^2), any excess activity eventually outruns itself, which is why there is a stable set point at y = 1. The lag in theta (0.7 memory) produces overshoot and slow oscillation, a realistic cost of a feedback controller with delay. The sliding threshold changes the rule for future plasticity; synaptic scaling instead multiplies all existing synapses on the cell by a common factor over a day or two, directly correcting total drive while preserving ratios between synapses (Figure 5.4B). Strong answers note that scaling protects learned information (ratios) while the threshold governs which inputs can change next, and that inhibitory plasticity is a third stabilizer.

## Lab 5.5 - Catastrophic Interference and the Cure (two learners)
1) Training on A: (0.500, 0.250) out 0.625; (0.688, 0.344) out 0.859; (0.758, 0.379) out 0.947; (0.784, 0.392) out 0.980. Check confirmed.
2) Output for B = 0.5(0.784) + 0.392 = 0.784, though its target is 0. Because the inputs overlap, learning A generalized to B.
3) Training on B: (0.588, 0.000); (0.515, -0.147); (0.487, -0.202); (0.477, -0.223); output for B falls to 0.016. Full precision w1 = 0.4767, which rounds to 0.477 (matches the check).
4) Output for A = 0.477 + 0.5(-0.223) = 0.365, down from 0.980: most of A has been overwritten by learning B.
5) Interleaved: after the pairs, (0.375, 0.000), (0.563, -0.094), (0.697, -0.188), (0.806, -0.268). Check confirmed.
6) Output A = 0.672, output B = 0.135. Compared with sequential (A 0.365, B 0.016), A is retained far better at a small cost to B; total squared error is about 0.126 versus 0.403.
7) Pairs 5 to 8: A 0.727, 0.774, 0.812, 0.844; B 0.112, 0.093, 0.077, 0.064; w = (1.082, -0.477) after pair 8. Both keep improving, converging on the single solution that satisfies both, w = (4/3, -2/3).
8) Model answer: sequential training moves the shared weights wherever the current error points; because A and B use the same weights with overlapping inputs, fixing B's error undoes A ("Two Clocks", catastrophic interference as a property of distributed representations). Interleaving makes each step a compromise, so the weights descend toward a solution that serves both experiences. In the brain, the hippocampus stores each experience fast and sparsely, then replays it interleaved with existing knowledge during slow-wave sleep and quiet rest, via sharp-wave ripples ("Two Clocks", "Sleep", Figure 5.7B). The cortex learns slowly so that each replay nudges rather than overwrites. Interleaving all past experiences with every new one would be impossibly costly in time and storage and would make new learning glacial; the brain instead replays selectively (recent, tagged, significant events) and lets the cortex's existing structure stand in for the rest. Grading: strong answers name complementary learning systems (McClelland, McNaughton, O'Reilly), sleep replay, and the stability-plasticity dilemma ("Why Learning Is Slow"); a common mistake is to say the hippocampus stores memories permanently.

## Lab 5.6 - Forgetting and Spacing (what retrieval buys)
1) No retrieval (s = 6): day 1 84.6, day 4 51.3, day 10 18.9, day 20 3.6, day 30 0.7 percent. Check confirmed.
2) Massed (days 1, 2, 3, 4): retention just before each retrieval 84.6, 91.6, 95.5, 97.6; s after each = 11.4, 21.66, 41.15, 78.19 days. Day 30: 100 exp(-26/78.19) = 71.7 percent. Check confirmed.
3) Spaced (days 1, 4, 10, 20): before each retrieval 84.6, 76.9, 75.8, 78.4 percent; same s sequence ending at 78.19. Day 30: 100 exp(-10/78.19) = 88.0 percent. Checks confirmed.
4) Final stability is identical (6 x 1.9^4 = 78.19 days), so the difference is the gap since the last retrieval: 26 days for the massed schedule versus 10 days for the spaced one. Massing spends all the stability gains early, then leaves the memory to decay for a long stretch. (In a richer model spacing also earns more per retrieval; here it wins purely on timing.)
5) One valid schedule: days 1, 3, 7, 15, 30. Retention just before each retrieval: 84.6, 83.9, 83.1, 82.3, 82.5 percent; final s = 148.6 days; day 60 = 81.7 percent. Since retention only falls between retrievals, these values and day 60 are the minima, so it stays above 75 throughout. Another valid answer: 1, 3, 8, 18, 35 (minimum 78.4, day 60 84.5). Grade any schedule whose pre-retrieval values and day-60 value all exceed 75; note that an expanding schedule is the natural solution, and that 1, 2, 4, 8, 16 fails (day 60 is 74.4).
6) Model answer: active retrieval reactivates the engram, which re-runs pattern completion and reopens the plasticity window, so the trace is reconsolidated and strengthened; re-reading supplies the input again without requiring the network to regenerate it ("Recall Changes the Record", "Forgetting Is a Mechanism"). Candidate mechanisms: reconsolidation (retrieval makes the memory labile and it is restabilized, possibly stronger), synaptic tagging and capture (reactivated synapses are retagged and can capture plasticity proteins, "The Third Factor"), and systems consolidation (each reactivation strengthens direct cortical links, "Two Clocks"). An organism benefits because use is evidence of future relevance: memories that are recalled are the ones likely to be needed again, so stability is invested where it pays, while unused specifics are pruned at no cost to useful knowledge. Strong answers connect this to forgetting as an active, energy-consuming function and to spacing as a test that the memory is still retrievable after some decay.

## Lab 5.7 - From Synapse to Memory (concept map)
1) Nodes: spine, presynaptic terminal releasing glutamate, AMPA receptors, NMDA receptor with magnesium plug, back-propagating spike. Links: glutamate plus depolarization "expels plug"; NMDA "admits calcium"; large brief calcium "activates kinases, inserts AMPA" (LTP); modest prolonged calcium "activates phosphatases, removes AMPA" (LTD) ("The Coincidence Detector", "LTP and LTD").
2) STDP window (pre before post strengthens, reverse weakens, negligible beyond about 50 ms) linked to the NMDA receptor: "glutamate still bound when the spike arrives gives a large calcium pulse; spike first gives small calcium" ("Timing Is Causation").
3) Two feedback loops from firing back onto the rule: firing "raises" the sliding threshold, which "shifts the LTD/LTP crossover" (fast, on the rule); sustained firing "triggers" synaptic scaling, which "multiplies all synapses, preserves ratios" (a day or two) ("Keeping the Whole Neuron Stable").
4) Dopaminergic axon above the spine; early LTP "sets tag" (lasting about one to two hours); dopamine "triggers protein synthesis" in the cell body; "capture" arrow to tagged synapses only, producing late LTP ("The Third Factor").
5) Sparse engram (a few percent of cells) in a hippocampus box with strengthened recurrent links; partial cue "activates a few cells"; recurrent links "complete the pattern" ("From Synapse to Engram").
6) Cortex box; hippocampus "replays to" cortex during slow-wave sleep (sharp-wave ripples); cues "reactivate"; clocks labeled synaptic consolidation (hours) and systems consolidation (weeks to years) ("Two Clocks", "Sleep").
7) Recall "reopens plasticity window" (reconsolidation, hours); disuse "prunes spines" via active forgetting mechanisms ("Recall Changes the Record", "Forgetting Is a Mechanism").
8) Caption grading guide: must follow the sequence coincidence (NMDA, calcium) to LTP (kinases, AMPA insertion), with STDP selecting causal inputs and homeostasis (threshold, scaling) keeping the cell in range; dopamine and tag-and-capture deciding what lasts; engram formation in hippocampus; synaptic consolidation within hours; replay in slow-wave sleep and systems consolidation over weeks to years until cortical recall needs no hippocampus; each recall reconsolidating (and possibly altering) the memory. It should end with forgetting: the episodic specifics and unused synapses are lost while the gist remains, which is correct because generalization and flexibility require discarding detail ("Forgetting Is a Mechanism", "The Central Lesson"). Common mistakes: treating the hippocampus as permanent storage, omitting the third factor, or describing forgetting as passive decay. Strong answers may note the contested status of the standard consolidation account versus trace-transformation theory.

### Notes for instructors

None beyond the answers above.

# Chapter 6: Perception as Inference: How the Brain Sees What It Expects

## Lab 6.1 - Prior Meets Evidence (Bayes by hand)
1) s_e = 5: prior precision 0.01, evidence precision 0.04. Posterior mean = (0 + 20 x 0.04) / 0.05 = 16.0 degrees; posterior SD = sqrt(1/0.05) = 4.47 degrees; weight on evidence 0.80. Checks confirmed.
2) s_e = 15: evidence precision 0.00444. Mean 6.15 degrees, SD 8.32 degrees, weight 0.31. Checks confirmed.
3) s_e = 10: equal precisions. Mean 10.0 degrees (halfway), SD 7.07 degrees, weight 0.50. Check confirmed.
4) s_p = 3, s_e = 5: precisions 0.111 and 0.04. Mean 5.29 degrees, SD 2.57 degrees, weight on evidence 0.26. Check confirmed. Not a malfunction: the system is doing exactly what Bayes's rule prescribes given its precisions. A prior this sharp is right when the world really is that regular (sounds nearly always do come from straight ahead in this context, for example a speaker you are facing) and when the auditory evidence is genuinely less reliable than past experience. It becomes an error only if the prior's precision overstates the world's regularity ("Bayes in One Paragraph").
5) Posterior = 20 w, so 18 requires w = 0.9, meaning evidence precision = 9 x prior precision, so s_e = s_p / 3 = 3.33 degrees. Check confirmed (posterior SD then 3.16 degrees).
6) Precisions add, so the combined precision exceeds each one alone, and the combined SD is smaller than either input's SD; two independent sources of information each remove some uncertainty.
7) Model answer: the optimal weighting depends on relative precision, which changes moment to moment, so any fixed policy is wrong in some conditions ("Bayes in One Paragraph", Figure 6.2). An organism that always trusts its senses is captured by noise: it would chase every flicker, see motion in sensor jitter, and fail in fog, darkness, or noise, with no benefit from a lifetime of regularities. An organism that always trusts its prior is effectively blind: it sees what it expects, misses genuine changes (the predator that is there this time), and cannot learn. Bayesian weighting gets the benefits of both and is more precise than either. Strong answers note that the policy requires an estimate of precision, which leads to attention ("Attention as Precision").

## Lab 6.2 - Two Senses, One Estimate (precision weighting)
1) s_v = 2: vision precision 0.25, touch 0.0625. Weight on vision 0.80; estimate 0.8 x 52 + 0.2 x 58 = 53.2 mm; SD sqrt(1/0.3125) = 1.79 mm. Checks confirmed.
2) s_v = 8: weight on vision 0.20; estimate 56.8 mm; SD 3.58 mm. Checks confirmed.
3) Equal weight when precisions are equal: s_v = 4 mm (estimate 55.0 mm, SD 2.83 mm). Check confirmed.
4) Weight on vision for s_v = 1, 2, 4, 8, 16: 0.94, 0.80, 0.50, 0.20, 0.06. The formula is 16 / (16 + s_v^2): near 1 for small s_v, falling steeply around s_v = 4, near 0 for large s_v. On a log axis of s_v it is a symmetric sigmoid centered at 4 mm; on a linear axis it is a reverse-S that drops fast then flattens.
5) As s_v grows without bound, vision precision goes to 0, its weight goes to 0, and the estimate becomes the touch value, 58 mm, with SD 4 mm. The organism relies entirely on touch (and on priors), feeling for the object rather than being misled by an uninformative visual signal.
6) Model answer: to weight optimally on every trial, the brain must represent not only each sense's estimate but its current reliability (variance or precision), and update that reliability as conditions change, for example as visual noise rises ("Combining the Senses"). That means representing uncertainty, not just values, possibly in the gain or variability of population activity. The weights must then be applied as gains on each input before combination. This is exactly what the chapter calls attention: the gain applied to prediction errors according to their expected reliability ("Attention as Precision"), with acetylcholine and norepinephrine as candidate chemical controls. Strong answers point out that this is the sense in which the book says the brain optimizes (minimizing variance of its estimate) and mention ventriloquism or McGurk as everyday examples.

## Lab 6.3 - Surprise on a Chain (predictive coding over time)
1) eta = 0.5. Prediction before each step and error:
   - Steps 1 to 6 (A): p = 0, 0.5, 0.75, 0.875, 0.938, 0.969; e = 1.0, 0.5, 0.25, 0.125, 0.062, 0.031.
   - Step 7 (B, x = 0.3): p = 0.984; e = -0.684.
   - Steps 8 to 11 (A): p = 0.642, 0.821, 0.911, 0.955; e = 0.358, 0.179, 0.089, 0.045.
   Checks confirmed.
2) The shrinking errors over steps 1 to 6 (and again 8 to 11) are repetition suppression; the large error at step 7 is the mismatch response (and the rebound error at step 8 is a smaller mismatch to the return of A). The oddball's error magnitude (0.684) exceeds its value (0.3) because the unit transmits deviation from prediction, and the prediction had approached 1.0: the error reports "much less than expected," not "a weak tone." To separate prediction from fatigue, hold repetition fixed and vary expectation, as Summerfield and colleagues did: the same repeated face suppressed responses more in blocks where repeats were likely ("Predictive Coding").
3) eta = 0.1: p after six A's = 0.469; oddball error -0.169 (p = 0.469, x = 0.3). Checks confirmed. A errors decline only slowly (1.0, 0.9, 0.81, 0.729, 0.656, 0.590). The slow learner has not yet learned the regularity, so it has no strong expectation to violate; the oddball is barely more surprising than the standards, which still generate large errors.
4) Omission (x = 0 at step 7): e = 0 - 0.984 = -0.984, the largest error in the sequence. With nothing arriving, the circuit "sees" its own unanswered prediction: the missing tone is a strong signal ("Predictive Coding", the omission response).
5) Transmitted = g x e. With g = 2: 2 x (-0.684) = -1.369. With g = 0.25: -0.171. The low gain corresponds to the unnoticed gorilla: an unattended (low-precision) channel transmits even large errors weakly, so the surprise never reaches the levels that update the percept ("Attention as Precision").
6) Model answer: sending the error is efficient because predictable input carries no new information; transmitting only the residual saves bandwidth and energy, and focuses the higher level on what it got wrong ("Predictive Coding"). What is lost is direct access to the raw stimulus: the higher level knows the input only through its own model plus the error, so if the model is wrong in a way that keeps errors small, or if errors are down-weighted, the mistake can persist (illusions, inattentional blindness). The higher level must be able to reconstruct the input from prediction plus error, which requires a good generative model. eta is a learning rate: high eta tracks change quickly but is noisy, low eta is stable but slow, the same trade-off as the stability-plasticity dilemma, the fast hippocampal and slow cortical clocks, and the sliding threshold's control over how easily synapses change (Chapter 5). Strong answers say that in the brain eta is itself regulated (by neuromodulators and development).

## Lab 6.4 - The Hollow Mask (discrete hypotheses against a strong prior)
1) Prior 99:1. 2 m (L = 5): odds 19.8:1, P(convex) 0.952. 1 m (L = 50): 1.98:1, 0.664. 0.5 m (L = 500): 0.198:1, 0.165. Checks confirmed. The percept flips (P below 0.5) only at 0.5 m; the flip point is where L exceeds 99, between 1 m and 0.5 m.
2) Prior 9:1. 2 m: odds 1.8:1, P = 0.643. 1 m: 0.18:1, 0.153. 0.5 m: 0.018:1, 0.018. Checks confirmed. It now flips at 1 m (L above 9), and even at 2 m the convex percept is much less certain. This matches the finding that the hollow-mask illusion is weaker in schizophrenia, consistent with priors that have lost some of their grip ("Illusions Are Correct Answers", "When Inference Goes Wrong").
3) Total L = 5 x 3 = 15; odds 99/15 = 6.6:1; P(convex) = 0.868. It does not flip: the mask is still seen as convex, as the chapter reports for a slowly rotating mask.
4) Need total L above 999. At 2 m stereo supplies 5, so the other cues must together supply more than 199.8 (for example 200). Plausible independent cues: touch (feel the concave interior), motion parallax from the observer's own head movement, close-range binocular disparity, shading with a known light direction, cast shadows, or seeing the mask's edge or back. Accept any two genuinely independent cues whose product, with stereo, exceeds 999.
5) Model answer: nearly every face anyone has seen is convex, so 99:1 (or stronger) accurately reflects the world's statistics, and holding it lets the visual system recognize faces quickly and robustly from poor, noisy, or ambiguous images ("Illusions Are Correct Answers"). The cost is that in the rare real hollow face the system reports the wrong shape, even against stereo and shading. That is a cheap price: the error almost never occurs in natural life, and when it matters, close inspection (stronger evidence) overrides it. Because the posterior depends on prior and evidence, measuring how much evidence (distance, number of cues) is needed to break the illusion quantifies the prior: the flip point is where the likelihood ratio equals the prior odds, so illusion strength is a measurement instrument for priors, including in clinical groups.

## Lab 6.5 - Who Moved, Me or the World? (efference copy)
1) Leftward slip positive:
   - a) Command 10 right, eye 10 right, object still: actual slip 10, predicted 10, perceived 0 (world stable).
   - b) No command, eye pushed 5 right: actual 5, predicted 0, perceived +5 (world appears to move 5 degrees left; it lurches).
   - c) Command 10 right, eye does not move: actual 0, predicted 10, perceived -10 (world appears to jump 10 degrees right, in the direction of intended movement).
   - d) Command 10 right, eye 10 right, object moves 3 right: actual object slip 10 - 3 = 7, predicted 10, perceived -3 (object seen to move 3 degrees right, correctly).
   All checks confirmed.
2) Perception is the brain's inference (actual minus predicted), not a readout of the retina, so a prediction with nothing to cancel it is perceived as motion.
3) Self-touch: 1.0 - 1.0 = 0 (nothing felt as tickle). Touch by someone else: 1.0 - 0 = 1.0. With the 200 ms delay: 1.0 - 0.4 = 0.6, so self-tickling becomes partly ticklish, matching the experiments ("Perception Is Active").
4) With glasses, a 10 degree command yields 12 degrees of slip but the forward model predicts 10, leaving a 2 degree error; the world seems to move against each eye movement. That sensory prediction error is signaled to the cerebellum by climbing fibers, which drive LTD at the parallel-fiber synapses active with the command, adjusting the forward model's gain over repeated movements until it predicts 12 degrees per 10 degree command (gain 1.0 to 1.2), after which the world looks stable again. Removing the glasses then produces a transient error in the opposite direction (aftereffect). Compare the prism-goggle adaptation in "Learning the Priors".
5) Model answer: an agent that moves its own sensors receives sensory changes from two sources, its own action and the world, and the raw signal cannot tell them apart ("Perception Is Active"). The efference copy plus a forward model predicts the self-caused part and subtracts it, leaving a signal that reports the world. Without one, every saccade would look like the world jumping, self-generated touch would be indistinguishable from external contact, and the agent would misattribute its own actions to the world, which corrupts learning from experience. This makes perception and action one loop: actions are chosen to gather evidence (saccades, sniffing, whisking), predictions of their consequences shape what is perceived, and what is perceived revises the next action. Strong answers mention the cerebellum as the forward model site and link to the AI point that an agent must know what it did versus what the world did.

## Lab 6.6 - Learning a Prior That Must Track the World
1) k = 0.2, m after each observation: 10.00, 10.40, 10.52, 10.22, 10.17, 12.14, 13.91, 14.93, 15.94, 16.75. Checks confirmed.
2) k = 0.05: 10.00, 10.10, 10.15, 10.09, 10.08, 10.58, 11.10, 11.50, 11.92, 12.32. Check confirmed. The k = 0.05 learner is more stable during the first five steps (range 10.00 to 10.15 versus 10.00 to 10.52); the k = 0.2 learner has adapted better by the tenth (16.75 versus 12.32). Trade-off: a high learning rate tracks change quickly but is pushed around by noise, a low rate resists noise but lags real change.
3) Surprise rule: first five as before (no deviations above 6); at the sixth, |20 - 10.17| = 9.83 > 6, so k = 0.8 gives 18.03; then 18.63, 18.70, 18.96, 19.17. Checks confirmed. It imitates norepinephrine, the signal of unexpected uncertainty that the world has changed and the current model should be discarded (Chapter 3; "Attention as Precision"). The "6" is an estimate of how large a deviation ordinary noise can produce (the expected spread of observations, here a few units), so that larger deviations signal a change in the world rather than noise.
4) Third observation 30. Plain k = 0.2: 10.00, 10.40, 14.32, 13.26, 12.60, then 14.08, 15.47, 16.17, 16.94, 17.55. Surprise learner: 10.00, 10.40, 26.08 (outlier triggers k = 0.8), then 12.42 (the return to 9 is also a surprise, k = 0.8), 11.93, 18.39, 18.91, 18.93, 19.14, 19.31. The surprise learner is thrown much further off (by about 16 versus 4.3) but only for one step; the plain learner is displaced less but stays biased for the rest of the stable period (still 2.6 above 10 at step five). So the surprise rule is vulnerable to single outliers in magnitude, while the plain rule suffers a smaller, longer-lasting contamination.
5) Example rule: keep a running variance v of prediction errors, v <- v + a((x - m)^2 - v), with small a; treat an observation as surprising if |x - m| > c sqrt(v) (for example c = 2 or 3), and set k higher in proportion to surprise. Optionally require two consecutive surprises before switching to protect against single outliers. sqrt(v) is the estimated spread, so 1/v is the estimated precision of the observations: deviations are judged in units of expected noise, exactly as precision weighting scales prediction errors ("Attention as Precision"). Grading: credit any rule that adapts the threshold to observed variability and explains the link to precision.
6) Model answer: k corresponds to how readily synapses that encode the prior change, set by the plasticity machinery of Chapter 5 (LTP/LTD magnitude, sliding thresholds, and the third factor gating what is kept); for cortical priors it is slow by default because cortex is the slow learner that must not overwrite accumulated structure ("Learning the Priors", Chapter 5 "Why Learning Is Slow"). A two-rate system (fast hippocampal store, slow cortical learner) can capture the new regime quickly in the fast component while keeping the long-run prior stable, and only gradually transfer the change if it persists, getting both the stability of k = 0.05 and the responsiveness of k = 0.2 or more. A critical period is a developmental window when the plasticity rules are turned up (inhibitory maturation and neuromodulators permit large changes), so the visual system rapidly learns the statistics of its input; its closing turns k down, making adult perception stable and adult perceptual learning slow, as the monocular deprivation and stripe-rearing experiments show. Strong answers note that k is not zero in adults (prism, inverted goggles, colored filter adaptation) and that neuromodulators can transiently raise it.

## Lab 6.7 - From Photons to Percept (concept map)
1) Nodes: eye, retinal image, three distinct world states consistent with it (for example different shapes, sizes, distances, or lighting), label "the inverse problem": many worlds, one image ("The Problem Perception Solves", Figure 6.1).
2) Ventral column retina, LGN, V1 (oriented edges, small fields), V2 (contours, illusory contours), V4 (curvature, color, larger fields), IT (objects, faces, invariant, nearly whole field). Feedforward arrows up; feedback arrows down at least as thick (feedback pathways outnumber feedforward; LGN gets about a tenth of its synapses from retina). Mark about 100 ms for the feedforward sweep ("The Hierarchy").
3) Prediction units in deep layers sending predictions down; error units in superficial layers computing input minus prediction and sending errors up. Label gamma on the upward (error) path, alpha/beta on the downward (prediction) path ("Predictive Coding").
4) "Prior" on feedback arrows, dashed link to "Chapter 5: learned weights," noting the critical period when plasticity is high and its closing ("Learning the Priors").
5) Gain knob on error units, "attention = precision"; acetylcholine input labeled "trust the senses, expected uncertainty"; norepinephrine labeled "the world changed, unexpected uncertainty, lower precision of predictions" ("Attention as Precision").
6) Touch feeding the hierarchy; two estimates combined with weights proportional to precision; combined estimate more precise than either ("Combining the Senses").
7) Motor command from the top; efference copy to a forward model (cerebellum); predicted sensation subtracted at the input; residual reports the world ("Perception Is Active").
8) Saccade arrow from percept back to the eye, "choose the next sample," closing the action-perception loop.
9) Caption grading guide: should trace photons forming an ambiguous image; the feedforward sweep producing a fast first guess; feedback predictions from learned priors meeting the input, with errors ascending until they are small; precision-weighted error gain (attention, acetylcholine, norepinephrine) deciding what counts; multisensory combination by precision; efference copy subtracting the consequences of the eye's own movement; and saccades sampling where uncertainty is highest, with the percept as the posterior. It must name one illusion the same mechanism produces (for example the hollow mask, Adelson's checker shadow, Kanizsa triangle) and one clinical condition from wrong gains (Charles Bonnet hallucinations with lost input, schizophrenia with weakened priors or overprecise priors, the autism account with excessive sensory precision), flagging the clinical accounts as hypotheses ("When Inference Goes Wrong"). Common mistakes: drawing feedback thinner than feedforward, describing the percept as a copy of the image, and confusing sensory prediction error with dopamine reward prediction error.

### Notes for instructors

None beyond the answers above.

# Chapter 7: Emotion and the Body: How Internal States Tell the Brain What Matters


## Lab 7.1 - Correcting Versus Predicting (homeostasis and allostasis)

1) Reactive, k = 0.5 (u uses the g at the start of the step): 5.00, 5.00, 7.00, 8.00, 7.50, 6.25, 5.62, 5.31, 5.16, 5.08. Peak 8.00 at step 4 (excursion 3.00 above set point). Matches the check.
2) Predictive, c = 0.8, d_cue = d: 5.00, 5.00, 5.40, 5.60, 5.50, 5.25, 5.12, 5.06, 5.03, 5.02. Peak 5.60 (excursion 0.60). The peak excursion is reduced by a factor of 5 (3.00 / 0.60). The cue term removes 80 percent of each disturbance in the step it arrives, so only 0.2 d reaches g and the feedback term mops up the rest.
3) Cue without food: 5.00, 5.00, 3.40, 2.60, 3.00, 4.00, 4.50, 4.75, 4.88, 4.94. Minimum 2.60 at step 4, then recovery toward 5 at half the remaining error per step. The anticipatory insulin drives glucose into hypoglycemia (the dip foreshadowed in the Figure 7.1 caption). The mirror image is Siegel's heroin experiment (see 'Regulation by Prediction'): there the dose arrives without the familiar cue, so the learned compensatory response is missing and the unopposed drug kills (64 percent mortality in the unfamiliar room versus 32 percent in the familiar one). Here the compensation arrives without the disturbance.
4) Reactive, k = 1.2: 5.00, 5.00, 7.00, 6.60, 5.68, 4.86, 5.03, 4.99, 5.00, 5.00. Peak 7.00. A reactive controller computes u from the error that already exists, so the first 2 units of food at step 3 enter before any error is visible; no gain can act on an error it has not yet seen, so the first overshoot is fixed at d. With k above 1 the controller overcorrects: at step 6 g undershoots to 4.86, below the set point, and the trajectory oscillates (damped here; with k at or above 2 it would oscillate without settling or diverge). High gain trades lag for instability and amplifies sensor noise.
5) Model answer (see 'Regulation by Prediction', 'Keeping the Body in Bounds'):
- The predictive controller needs a learned model linking cues to future disturbances: what a cue predicts, how large the disturbance will be, and when it arrives. The reactive one needs only a sensor and a set point.
- That knowledge is learned (Pavlovian association of sight, smell, and taste with the meal) and is carried by forebrain and hypothalamic circuits; the cephalic phase insulin response starts "in the head."
- Chen, Knight, and colleagues showed AgRP hunger neurons in the arcuate nucleus fall within seconds of seeing or smelling food, before any food is eaten, scaled by hunger and palatability: the hunger signal tracks the predicted state, not the present one. That is exactly the d_cue term.
- The cost of prediction is step 3's error case (and Siegel's rats): wrong predictions cause harm a reactive system would not.
- Chapter 6's perception combines learned expectation with incoming evidence to estimate the world; allostasis uses learned expectation to estimate and act on the body's future state. Same strategy (prediction from learned models), applied inward. A strong answer may note Ramsay and Woods's view that this is homeostasis with good forecasting rather than a new principle.

## Lab 7.2 - Value Depends on the Body (alliesthesia by formula)

1) reward = H² − (H + 2)² = −4H − 4. At H = −6: 36 − 16 = 20. At −2: 4 − 0 = 4. At 0: 0 − 4 = −4. At +2: 4 − 16 = −12. Matches the check.
2) The plot is a straight line with slope −4 crossing zero at H = −1. Food is a punishment for any H > −1, that is, once a portion would push the reserve past the set point by more than it reduces the deficit. This is Cabanac's alliesthesia (see 'Value Depends on the Body'): the same sweet solution is pleasant to fasting volunteers and unpleasant after a glucose load, because pleasure tracks usefulness to the body. Sensory-specific satiety is the same principle applied per food: the eaten food's value falls with its own consumption while uneaten foods keep theirs (room for dessert), which in this model would need a separate variable per nutrient or food.
3) H goes −6, −4, −2, 0, 2. Rewards 20, 12, 4, −4. After three portions H = 0 and the next portion yields −4: it would increase drive. The signal that says stop is the shrinking and then negative drive reduction, felt as falling palatability and satiety; the falling reward is computed from the internal state, not from the food.
4) Food on H = −2: 4 − 0 = 4. Water on W = −6: 36 − 16 = 20. Water is valued five times as much (16 units more). The agent should drink first; its priorities follow its largest deficit.
5) With a fixed +5 per portion, the agent never sees value fall: it rates the fourth, tenth, and hundredth portion the same and keeps eating past the set point. It is maximizing the specified signal, not the body's welfare, so it overeats without limit. That is reward hacking: optimizing the proxy rather than the purpose. Addiction is the biological analog, where a drug produces a reward signal decoupled from bodily need (see 'Implications for Artificial Intelligence').
6) Model answer (see 'Value Depends on the Body', 'Implications for Artificial Intelligence'):
- Betley, Sternson, and colleagues showed AgRP hunger neurons (and thirst counterparts) carry a negative, aversive signal; animals avoid cues paired with their stimulation, and eating, which silences them, is reinforcing partly because it ends the state. They behave like D(H): activity grows with deficit, and reducing it is rewarding.
- The dopamine reward prediction error of Chapter 3 compares received with predicted value; if outcome value depends on state (juice to a thirsty versus sated monkey), the error must take the body's state as input or it will mislearn.
- Keramati and Gutkin's homeostatic reinforcement learning formalizes exactly this lab's rule.
- An artificial agent would need internal variables it must keep in bounds, a set point, and a reward computed as drive reduction, so that value changes with state and cannot be inflated indefinitely. Strong answers note Singh and colleagues on intrinsic reward and that anchoring limits, but does not eliminate, reward hacking.

## Lab 7.3 - How Well Do You Feel Your Heart? (measuring interoception)

1) P: 1 − 2/30 = 0.933; 1 − 2/42 = 0.952; 1 − 4/55 = 0.927; mean 0.938. Q: 1 − 12/27 = 0.556; 1 − 18/38 = 0.526; 1 − 25/49 = 0.490; mean 0.524. Matches the check.
2) P: high accuracy (0.938), low sensibility (confidence 4 to 5 out of 10), so poor awareness in the sense that confidence underrates performance. Q: low accuracy (0.524), high sensibility (8 to 9), and poor awareness: confident while badly wrong. Neither participant's confidence tracks accuracy; across-trial awareness would properly be measured by correlating confidence with per-trial score over many trials (three trials are too few). The point is that the three measures dissociate (see 'Sensing the Inside').
3) Heart explanation: Q truly perceives only the stronger beats (for example, misses beats at a low signal level, or has weak cardiac signals reaching the insula). Strategy explanation: Q counts only beats they are sure of, or counts on every other perceived pulse, or estimates time rather than feeling beats and has a slow internal clock. A participant who knows resting rate is about 70 bpm can estimate the interval length (25 s ≈ 29 beats) and report that, scoring well with no interoception at all. This is the known weakness of the counting task: it confounds heartbeat perception with time estimation and prior knowledge.
4) Optional; no key. Remind students that scores are personal data; check that partners counted from the same start and stop signals.
5) Model answer (see 'Sensing the Inside'):
- Interoceptive signals travel by the vagus to the nucleus of the solitary tract and by lamina I, relay through brainstem and thalamus, and reach the posterior insula as a primary map; Craig proposed it is re-represented toward the anterior insula, where it is integrated and made available to awareness. So the right anterior insula is where a consciously reportable heartbeat estimate should be formed.
- Critchley and colleagues found its activity and gray matter volume predicted accuracy on a related task.
- To claim causation in a job (for example, traders), you need more than a correlation: a valid measure that is not explained by time estimation or knowledge of one's heart rate; control for confounds (experience, fitness, age, anxiety, general intelligence); a prospective design in which interoception measured earlier predicts later performance; ideally an intervention that improves interoceptive accuracy and then improves decisions, with a control group; and replication. Reverse causation (success making people calmer and better at counting) must be excluded.

## Lab 7.4 - Extinction Is New Learning (a two-memory fear model)

1) V = 0.30, 0.51, 0.66, 0.76, 0.83 (exactly 0.832).
2) Fear in B after each trial's update: 0.58, 0.41, 0.29, 0.20, 0.14, 0.10, 0.07, 0.05; I_B = 0.78 (0.784). (Fear at the start of each trial, before the update, would be 0.83, 0.58, ..., 0.07; the check reports post-update values. Accept either if labeled.)
3) Fear in A = V = 0.83: full renewal, because the inhibitory memory is tied to context B and V was never changed. Bouton predicts renewal on return to the acquisition context (or any non-extinction context) because extinction is context-bound new learning (see 'Unlearning Fear'); the model agrees because it encodes exactly that structure.
4) Fear in B = 0.83 − 0.784/2 = 0.44.
5) Erasure: V goes 0.58, 0.41, 0.29, 0.20, 0.14, 0.10, 0.07, 0.05: identical to step 2. In the two-memory model, fear = V − I_B shrinks by the factor (1 − 0.3) each trial, the same as V under erasure, so the curves cannot differ. But under erasure V is 0.05 everywhere: no renewal in A (0.05, not 0.83) and nothing to recover with time. Lesson: an extinction curve alone cannot distinguish theories; the decisive tests are post-extinction probes (context change, time, reinstatement) where the models diverge.
6) V: the tone-shock association in the lateral amygdala, expressed through the central nucleus to periaqueductal gray, hypothalamus, and brainstem (Figure 7.4). I_B: in the infralimbic cortex of the rat (Milad and Quirk), the ventromedial prefrontal cortex in humans (Phelps and colleagues), which inhibits amygdala output; the context tag comes via the hippocampus. Diagram must show vmPFC inhibiting the amygdala and V stored in the lateral amygdala.
7) Model answer (see 'Unlearning Fear'):
- Keeping V is adaptive: a threat that was once real may return; an animal that erased it would have to relearn danger the costly way. Suppression in safe contexts gets the best of both.
- Exposure therapy inherits extinction's weakness (renewal, spontaneous recovery, reinstatement). Do it in multiple contexts, including those where the fear occurs in daily life, and space and repeat sessions, with booster sessions over time, so the inhibitory memory is strong and general.
- Reappraisal (Ochsner) changes what the situation means, engages lateral and medial prefrontal cortex, and reduces amygdala activity: like extinction, it is prefrontal regulation of an intact amygdala memory, but deliberate and voluntary ("extinction made voluntary").

## Lab 7.5 - The Stress Axis and Its Brake (negative feedback)

1) Baseline 1/(0.3 + f): f = 0.5 gives 1.25; f = 0.1 gives 2.50.
2) f = 0.5: 11.25, 13.25, 13.65, 9.55, 6.69, 4.68, 3.28, 2.29, 1.61, 1.32, 1.26, 1.25, 1.25, 1.25, 1.25, 1.25. Peak 13.65. (Hypothalamic drive h hits its floor of 0 on steps 4 to 8 and then returns.)
3) f = 0.1: 12.50, 18.50, 22.10, 15.47, 10.83, 7.58, 5.55, 4.33, 3.60, 3.16, 2.90, 2.74, 2.64, 2.59, 2.55, 2.53. Peak 22.10.
4) Within 0.5 of baseline: step 9 for f = 0.5 (1.61 vs 1.25), step 11 for f = 0.1 (2.90 vs 2.50). Differences with weak feedback: higher baseline (2.50 vs 1.25), higher peak (22.10 vs 13.65), slower recovery (two steps later, and a longer tail creeping toward baseline). Also a larger total cortisol exposure.
5) Chronic stress shrinks CA3 dendrites (see 'The Chemistry of Stress'), weakening a feedback site, which lowers f. In the model, lower f produces a higher resting level, a larger peak, and a slower return. More cortisol then does further damage to the hippocampus, lowering f further: a vicious circle that the chapter frames as allostatic load (McEwen), the cumulative cost of chronically activated stress responses. Strong answers add the amygdala's opposite change (dendritic growth, persisting into recovery) as a second loop that increases drive.
6) Sketch: sympathetic arm (epinephrine, heart rate) rising within seconds and decaying within minutes; HPA arm (CRH, then ACTH, then cortisol) rising over minutes, peaking tens of minutes after onset, then falling as feedback shuts it down. The cortisol curve should be delayed and broader.
7) Model answer (see 'The Chemistry of Stress'):
- The response mobilizes energy and prepares action but is costly over time (allostatic load, immune and hippocampal effects), so it must be terminated when the demand ends; feedback both caps the peak and sets the baseline.
- Preparative: cortisol mobilizes glucose and readies the body for demand. Permissive and restraining (Sapolsky): some actions enable other systems to respond, and later ones restrain the stress response itself before it does damage.
- Inverted U (Arnsten; Yerkes and Dodson): moderate norepinephrine and dopamine strengthen prefrontal working memory; high levels weaken prefrontal networks and shift control to the amygdala and habits. A task needing deliberation (an exam) has its peak at lower arousal than one served by fast practiced responses (an emergency), so the optimum depends on the task. Students should not claim Yerkes and Dodson measured arousal; they varied shock and difficulty.

## Lab 7.6 - Arousal Decides What Is Kept (a three-factor consolidation rule)

1) Placebo: neutral 0.2 + 0.6 × 0.1 = 0.26; emotional 0.2 + 0.6 × 0.9 = 0.74. Propranolol: 0.20 and 0.20. To justify treating the drug as acting on consolidation, give it after the story (post-encoding), as in Gold and van Buskirk's post-training injections and McGaugh's work: if post-learning blockade still removes the enhancement, the effect is on storage, not on encoding or attention (see 'Emotion Marks What to Remember').
2) Reproduced: enhanced memory for the emotional middle under placebo; loss of the enhancement with propranolol; neutral memory unaffected (0.26 vs 0.20 is small, near the floor; in the real study neutral memory was unaffected, so the model slightly overstates the drug's effect on neutral material). The product arousal × b is the amygdala term (norepinephrine acting at beta receptors in the basolateral amygdala); the trace being kept (the baseline 0.2 and the event's trace) lives in the hippocampus and cortex that store the memory.
3) One acceptable rule: kept = 0.2 + 2.4 × arousal × (1 − arousal) × b, which peaks at arousal 0.5. Values: 0.42 at 0.1, 0.80 at 0.5, 0.42 at 0.9. A Gaussian such as 0.2 + 0.6 × b × exp(−((arousal − 0.5)/0.25)²) also passes. Grade on: peak at an intermediate value, return toward baseline at high arousal, b still gating.
4) Set arousal (the signal reaching storage sites) to 0 for the emotional part. kept = 0.20 for both parts: the patient remembers the gist of the story at baseline with no emotional enhancement, matching Cahill's 1995 patient.
5) Sketch: consistency (agreement with the original account) decays over weeks at the same rate for emotional and neutral events (Talarico and Rubin); confidence stays high and flat, or decays much more slowly, for the emotional event and falls for the neutral one. The gap between the two curves widens for the emotional event: confident but inconsistent (Neisser and Harsch's Challenger study).
6) Model answer (see 'Emotion Marks What to Remember'):
- Three factors: presynaptic activity (the event's input), postsynaptic activity (the encoding in hippocampus and cortex), and a neuromodulatory third factor, here norepinephrine in the basolateral amygdala signaling arousal.
- Arousing events usually matter for survival and future action (threats, rewards), so storing them preferentially makes the limited budget of consolidation serve what matters.
- Keeping is not accuracy: the enhancement strengthens conviction and persistence, and memories are reconstructed and reconsolidated on each retelling, so details drift while confidence stays high (flashbulb memories).

## Lab 7.7 - Four Decks (the Iowa gambling task by hand)

1) Deck A: wins 1000, losses 1250, net −250, −25 per card. Deck C: wins 500, losses 250, net +250, +25 per card.
2) Deck A values: 20.0, 36.0, 18.8, 35.0, −12.0, 10.4, −11.7, 10.7, −21.5, −67.2. Deck C values: 10.0, 18.0, 14.4, 21.5, 17.2, 23.8, 19.0, 25.2, 20.2, 16.1. Matches the check.
3) First below C at card 5 (−12.0 vs 17.2), and below at every later card (cards 5 to 10). But for the first four cards the bad deck looks better, and its value swings wildly (from −12 to 10 and back), so a learner sampling noisily would need several cards past the first loss, and many more in decks B and D whose losses are rarer, before reliably recognizing it.
4) Myopic learner sees A as +100 and C as +50 every card: A 89.3, C 44.6 after ten cards; A preferred by 44.6, about two to one. This is "insensitivity to future consequences": attracted by immediate large gains, blind to the delayed penalties.
5) Model answer: a strong design dissociates the bodily signal from knowledge. Measure anticipatory skin conductance and fine-grained knowledge (frequent probes, as Maia and McClelland did, or confidence wagering) trial by trial, and test which predicts choice first. Then manipulate: block or remove peripheral feedback (pure autonomic failure patients, or beta-blockade) and see whether choice changes; or degrade explicit knowledge (dual task, masked outcomes) and see whether skin conductance still guides choice. "Felt" implies the bodily signal is necessary and precedes knowledge; "known" implies report suffices. Common mistake: treating correlation between skin conductance and choice as proof that the body causes choice.
6) Losses first: A values −10.0, −48.0, −58.4, −76.7, −111.4, −69.1, −35.3, −8.2, 13.4, 30.7. Compared with C in its original order, A is below C from card 1 to card 9 and above it only at card 10 (30.7 vs 16.1). With a fixed learning rate of 0.2, the value is a recency-weighted average (each old outcome's weight decays by 0.8 per card), so five straight wins override the earlier losses: the learner tracks the recent run, not the long-run mean of −25. Note the comparison holds C in its original order; a matched reordering of C would also change C's trajectory. In the original order, a learner must reverse a value learned as positive; one slow to reverse (vmPFC patients, per Fellows and Farah) stays with A after the losses start, which is why their deficit shrank when the early wins were removed.
7) Model answer (see 'Feeling and Choosing'):
- vmPFC damage leaves reasoning intact but impairs choice; the region links value with the body.
- The somatic marker reading has not held up: players know the good decks about as soon as they choose them (Maia and McClelland); pure autonomic failure patients, with almost no bodily feedback, play normally; the patients' deficit is largely reversal learning (Fellows and Farah); Dunn's review judged the hypothesis in need of support. So bodily feedback is probably not necessary, though value signals are tied to bodily regulation.
- Chapter 8 would frame it as learning values from variable outcomes under uncertainty, with an explore-exploit trade-off and reversal of learned values when contingencies change (see Chapter 8, 'Learning What Options Are Worth').

## Lab 7.8 - From Body to Choice (concept map)

Required nodes: heart, lungs, gut, immune cells (cytokines); vagus nerve; nucleus of the solitary tract; spinal lamina I; circumventricular organs (credit if included); brainstem; thalamus; hypothalamus; amygdala (lateral and central nuclei, basolateral amygdala); posterior insula; anterior insula; cortex (predictive input); sympathetic nerves and adrenal medulla (epinephrine); HPA axis (CRH, ACTH, cortisol); hippocampus; ventromedial prefrontal cortex (infralimbic in rat); periaqueductal gray; locus coeruleus (norepinephrine); dopamine neurons; valence and arousal inset; choice.

Key labeled links:
1) Body to NTS via vagus; body to lamina I via spinal cord; both to brainstem, then thalamus, then posterior insula, then anterior insula; branches to hypothalamus and amygdala ("interoception").
2) Hypothalamus as comparator with set point; effectors (autonomic, pituitary, behavior); cortex to hypothalamus "allostasis: act before the error."
3) Hypothalamus to sympathetic nerves to adrenal medulla ("epinephrine, seconds"); hypothalamus to pituitary to adrenal cortex ("cortisol, tens of minutes"); cortisol back to hypothalamus, pituitary, hippocampus ("negative feedback").
4) Tone and shock to lateral amygdala ("LTP"), to central nucleus, to PAG ("freezing"), hypothalamus ("blood pressure, stress hormones"), brainstem neuromodulators; vmPFC to amygdala ("inhibits after extinction").
5) Locus coeruleus to basolateral amygdala ("norepinephrine") to hippocampus and cortex ("modulates consolidation"); dopamine "RPE, value depends on bodily state" with an input from hypothalamus or insula.
6) Insula to the valence-arousal inset ("core affect").
7) Insula and value signals to vmPFC; vmPFC to choice ("bias"), with a note: Iowa deficit is real, but the somatic marker reading is weakened by Maia and McClelland, pure autonomic failure, and Fellows and Farah.
8) Caption grading guide (near miss in traffic): a strong caption covers (a) sight of the car via fast and slow routes to the amygdala; (b) central nucleus and hypothalamus driving the sympathetic burst and epinephrine within seconds, with braking and swerving served by practiced responses as prefrontal control yields (inverted U); (c) the pounding heart reaching the insula as interoceptive signal, felt as high arousal, negative valence, labeled fear in context; (d) the HPA axis raising cortisol over the next tens of minutes, then feedback returning it to baseline; (e) norepinephrine in the basolateral amygdala boosting consolidation so the event is remembered; (f) a week later, a vivid confident memory that may have drifted in detail; (g) the corner or road becoming a learned threat cue, which later driving without incident extinguishes via vmPFC; (h) one disorder: weakened cortisol feedback (prolonged response), an overgeneralized or unextinguished fear (PTSD-like renewal), or an inflated interoceptive prediction error (panic, anxiety). Common mistakes: calling the amygdala a fear center, treating extinction as erasure, assuming more arousal always improves memory accuracy.

### Notes for instructors
- Minor clarity notes (not errors): Lab 7.4 step 2 reports fear after each trial's update; say so to avoid students listing pre-update values. Lab 7.7 step 6 compares reordered A against C in its original order; the step could say so explicitly. In Lab 7.6 the model gives propranolol a small effect on neutral memory (0.26 to 0.20) whereas the study found none.

# Chapter 8: Decision-Making Under Uncertainty: How the Brain Chooses When It Cannot Be Sure


## Lab 8.1 - Stop When You Are Sure Enough (accumulating evidence)

1) A: 1, 0, 1, 2, 1, 2, 3, 4, 3, 4, 5, 6. B: −1, −2, −1, 0, 1, 0, 1, 2, 3, 4.
2) A: b = 2 at sample 4, b = 4 at sample 8, b = 6 at sample 12; all "right," all correct.
3) B: b = 2 stops at sample 2 at −2, choosing "left" (wrong); b = 4 stops at sample 10 at +4, choosing "right" (correct).
4) A higher bound costs more samples (time) but protects against early runs of misleading evidence, so it buys accuracy with speed.
5) With ±2 samples and b = 4, every running total doubles, which is the same as ±1 with b = 2: A stops at sample 4 (correct) and B at sample 2 (wrong). Decision time halves, but because signal and noise were scaled together, accuracy falls exactly as if the bound had been halved. In the dot-motion task, stronger evidence is higher coherence, which raises the fraction of samples pointing the right way (the drift relative to noise); that shortens decisions and also raises accuracy. Strong answers spot this distinction.
6) Model answer (see 'Accumulating Evidence'):
- LIP firing of neurons whose response field lies in the chosen direction ramps during viewing, faster for stronger motion: the running total. MT supplies momentary evidence (Newsome; microstimulation biases choice).
- Bound: with free response, LIP firing reaches a common level about 70 ms before the saccade regardless of coherence (Roitman and Shadlen). Strong tests: response-aligned convergence, trial-by-trial prediction of RT from reaching the level, or perturbation that changes the level and shifts speed and accuracy as predicted.
- Latimer found single-trial stepping rather than ramping; Katz found LIP silencing spared discrimination. These challenge LIP as the sole integrator, not accumulation as a behavioral description: population recordings show single-trial diffusion, inactivation impairs decisions before compensation, and several areas likely integrate. The model's fit to choices and RT distributions stands independently of where it is implemented.

## Lab 8.2 - Choosing the Bound (speed, accuracy, and reward rate)

1) a = 0.5, 1.0, 1.5, 2.0: P = 0.642, 0.762, 0.851, 0.911; DT = 0.24, 0.90, 1.81, 2.83 s.
2) d = 0: RR = 0.252, 0.238, 0.207, 0.178. Best is the lowest bound tested (0.5). A finer search puts the optimum near a = 0.56 (RR 0.253), so essentially "go fast."
3) d = 6: RR = 0.137, 0.165, 0.170, 0.161. Best at a = 1.5 (finer optimum about a = 1.38, RR 0.171).
4) d = 10: RR = 0.105, 0.137, 0.152, 0.151. a = 1.5 (0.1521) narrowly beats a = 2.0 (0.1515); finer optimum about a = 1.71 (RR 0.153).
5) As errors cost more time, each error lowers the reward rate more, so it pays to spend extra decision time buying accuracy; the optimum bound rises. The subthalamic nucleus raises the bound under conflict (frontal theta), and stimulating it removes that slowing, producing hasty choices (Frank; Cavanagh and colleagues; see 'Accumulating Evidence'). "Be careful" raises the bound (slower, more accurate); "hurry" lowers it.
6) Model answer (see 'Accumulating Evidence', 'Implications for Artificial Intelligence'):
- Near a deadline, time remaining is worth less and failing to respond may be worst of all; an urgency signal that grows with time effectively collapses the bound, trading accuracy for a guaranteed answer. When difficulty varies across trials, a falling bound is optimal because long deliberation signals a hard trial unlikely to resolve.
- Note the debate: fixed bounds fit most data as well or better.
- A fixed-computation classifier spends the same compute on every input and has no bound and no notion of the cost of time or errors, so it cannot stop early on easy inputs or deliberate longer when errors are expensive. Adaptive computation time and step-by-step reasoning models are partial exceptions but rarely have a bound that moves with the stakes.

## Lab 8.3 - Prospect Theory by Hand (losses, frames, and ambiguity)

1) EV = 0.5 × 110 − 0.5 × 100 = +5. PT value = 0.5 × 62.58 − 0.5 × 2.25 × 57.54 = 31.29 − 64.74 = −33.45. Rejects.
2) Need G^0.88 = 2.25 × 100^0.88, so G = 100 × 2.25^(1/0.88) ≈ 251. People typically demand about twice the loss (about 200), so this parameter set, applied without probability weighting, is a little more loss averse than typical behavior; Brown's meta-analysis puts typical loss aversion somewhat below two.
3) Expected lives saved: A 200, B (1/3) × 600 = 200. Loss frame: A = 400 die for certain; B = 1/3 chance nobody dies, 2/3 chance 600 die (expected 400 dead). Gains frame: v is concave, so a sure 200 saved is worth more than a 1/3 chance at 600 (v(200) > (1/3) v(600)), giving risk aversion and choice of A (72 percent). Loss frame: v is convex for losses, so a sure loss of 400 feels worse than a 2/3 chance of losing 600 (|v(−400)| > (2/3)|v(−600)|), giving risk seeking and choice of B (78 percent). With α = 0.88, 200^0.88 = 105.9 vs (1/3) × 600^0.88 = 92.8; for losses, 2.25 × 400^0.88 = 438.5 vs (2/3) × 2.25 × 600^0.88 = 417.7.
4) A bet on red pays if red is drawn. Preferring Urn 1 for red means 0.5 > p, so p < 0.5. Preferring Urn 1 for black means 0.5 > 1 − p, so p > 0.5. No p satisfies both. The choices cannot come from any subjective probability; they reflect aversion to unknown odds as such (ambiguity aversion).
5) Model answer (see 'Risk, Loss, and Ambiguity'):
- Losses can be fatal or irreversible for an animal near survival thresholds, while equal gains add less fitness; weighting losses more protects against ruin. Ambiguity often signals that someone else knows more (the urn may be stacked) or that the environment is poorly understood, so avoiding it is protective in adversarial or nonstationary worlds.
- De Martino, Camerer, and Adolphs found two amygdala-damaged patients (including S.M.) accepted gambles healthy people refused, with sharply reduced loss aversion: the amygdala may make losses matter to choice rather than value them. Tom and colleagues found striatum and vmPFC activity fall more steeply with losses than they rise with gains, predicting behavior.
- Caution: Gal and Rucker argue many apparent cases have other explanations; Brown's meta-analysis finds the factor somewhat below two with wide variation, so it is a typical finding, not a constant.

## Lab 8.4 - Now or Later (discounting and preference reversal)

1) Day 0: 100/(1 + 0.2 × 30) = 14.29; 110/(1 + 0.2 × 31) = 15.28. Larger, later preferred.
2) Day 30: 100/1 = 100; 110/1.2 = 91.67. Smaller, sooner preferred.
3) Set 100(1 + 0.2(31 − t)) = 110(1 + 0.2(30 − t)): 720 − 20t = 770 − 22t, so t = 25. Both values are 50.00 on day 25; before day 25 the larger is preferred, after it the smaller. Sketch: two rising curves that cross at day 25, as in Figure 8.5.
4) V_large / V_small = (110 e^(−r(31 − t))) / (100 e^(−r(30 − t))) = 1.1 e^(−0.05) = 1.046 on every day, independent of t. Always above 1, so the larger reward is always preferred; exponential curves never cross.
5) Day 30: prefer 100 now iff 100 > 110/(1 + k), that is, 1 + k > 1.1, so k > 0.1 per day (at k = 0.1 they tie).
6) Model answer (see 'The Price of Waiting'):
- Hyperbolic discounting is steep near the present and shallow far away, so the relative value of the two rewards changes as they approach; the plan made from a distance is outvoted when the smaller reward is imminent (Strotz, Ainslie). The day-0 and day-30 selves use the same curve, viewed from different distances.
- Kidd and colleagues' reliable versus unreliable experimenter result implies that k partly measures beliefs about how reliable the future is, not a fixed trait (Sozou's argument that uncertain hazard yields hyperbolic discounting). Note the later 149-child study found no significant trustworthiness effect.
- Commitment devices: lock in the larger, later reward on day 0 (direct deposit, a binding contract, removing the option to take the 100, a deposit forfeited if the person defects), or make the immediate option unavailable or costly on day 30.

## Lab 8.5 - The Unlucky First Draw (explore or exploit)

1) Greedy: estimates after trial 2 are A 6, B 4; A's estimate then hovers near 5 and never falls below 4. Choices A, B, then A on trials 3 to 12. Total 60 (A's 11 payoffs sum to 56, plus B's 4). B's estimate stays at 4.
2) Bonus, weight 2: trial 3 A 6 + 2√(ln 3/1) = 8.10 vs B 4 + 2√(ln 3/1) = 6.10, choose A. Trial 4: A 5 + 2√(ln 4/2) = 6.67 vs B 4 + 2√(ln 4) = 6.35, choose A. Trial 5: A 5 + 2√(ln 5/3) = 6.46 vs B 4 + 2√(ln 5) = 6.54, choose B (payoff 9). Trial 6: A 5 + 2√(ln 6/3) = 6.55 vs B 6.5 + 2√(ln 6/2) = 8.39, choose B. B stays ahead for the rest. Choices A, B, A, A, B, B, B, B, B, B, B, B. Total 79 (A 15, B 64).
3) The bonus has n in the denominator: each choice of an option shrinks its uncertainty, and the bonus with it. For an unchosen option n is fixed while t grows, and the bonus rises only with √(ln t), very slowly, so neglected options are eventually retried, but rarely.
4) Weight 0.5: trial 3 A 6.52 vs B 4.52; trial 4 A 5.42 vs B 4.59; trial 5 A 5.37 vs B 4.63; trial 6 A 5.58 vs B 4.67. Never discovers B; A from trial 3 to 12, total 60. The weight is the value placed on information relative to immediate reward: how much exploration the agent buys per unit of uncertainty.
5) Make the weight depend on the remaining horizon, for example weight = c × (trials remaining)/(total trials), or c × √(log trials remaining), so exploration is high early and falls to pure exploitation on the last trials. Strong answers also note Wilson found increased random exploration with longer horizons, which could be modeled as a softmax temperature that also scales with horizon.
6) Model answer (see 'Explore or Exploit'):
- The bonus implements directed exploration: choosing where knowledge is least. Wilson and colleagues separated directed from random exploration by horizon; Daw found exploration engaged frontopolar cortex.
- Chapter 3's account gives norepinephrine a role in setting the explore-exploit balance and in signaling unexpected uncertainty (Behrens's volatility-dependent learning rates, with anterior cingulate activity, though norepinephrine was not measured).
- Random exploration (epsilon-greedy, softmax noise) is cheap, needing no uncertainty bookkeeping, but wastes samples on options already well known; directed exploration targets information but requires tracking counts or uncertainty.
- Hayden's dorsal anterior cingulate neurons, rising with each harvest until a threshold at patch leaving, compute something like the declining value of staying relative to the environment's average (Charnov's marginal value theorem): an exploit-versus-explore decision variable with a bound. Note Shenhav's alternative reading as choice difficulty.

## Lab 8.6 - Goal or Habit? (devaluation in two learners)

1) Q(L): 5.00, 7.50, 8.75, 9.38, 9.69, 9.84. Q(R): 3.00, 4.50, 5.25, 5.62, 5.81, 5.91. Both learners prefer L (model-based: 10 vs 6).
2) Model-based recomputes from current outcome values: L = 0, R = 6, so it prefers R at once. Model-free cached values are unchanged (Q(L) 9.84, Q(R) 5.91), so it still prefers L.
3) Q(L) after each devalued press: 4.92, 2.46, 1.23, 0.62. It switches to R after the first press (4.92 < 5.91).
4) With no outcome delivered, the model-free learner has nothing to update from and keeps pressing L at the old rate: insensitivity to devaluation, the signature of a habit after extensive training (Figure 8.7, extended-training bars). The model-based learner's reduced pressing corresponds to the moderate-training, goal-directed result.
5) Model answer (see 'Goals and Habits'): after extensive training in a stable world the cached values have converged and their uncertainty is low, while model-based planning carries uncertainty from its many simulated steps and computational noise. Handing control to the more reliable system is rational and saves computation; the cost is inflexibility when the world changes unseen, as in devaluation. Note Miller, Shenhav, and Ludvig's alternative that habits are actions strengthened by repetition, not cached values.
6) Model answer (see 'Goals and Habits', 'When Choice Goes Wrong'):
- Model-based, goal-directed control: dorsomedial striatum and the prefrontal cortex projecting to it. Model-free, habitual: dorsolateral striatum (Yin, Knowlton, and Balleine: lesions keep rats goal-directed).
- Tricomi reported overtraining-induced habits in people, but de Wit and colleagues failed to produce the effect in five experiments, two direct replications, so overtraining alone may not produce habits in humans; the human evidence for the rodent dichotomy is weaker than often claimed.
- Gillan's online study of more than 1,000 people linked a transdiagnostic compulsivity dimension (OCD, addiction, binge eating) with weaker model-based control in the two-step task: compulsive disorders may reflect a failure of goal-directed control to override habit, not excessive habit learning alone. Note that some model-based-looking patterns can be produced by sophisticated model-free strategies.

## Lab 8.7 - From Evidence to Action (concept map)

Required nodes: sensory evidence (MT); accumulator (LIP and other areas) with bound; confidence readout (orbitofrontal cortex for acting on confidence); valuation (orbitofrontal cortex, vmPFC, ventral striatum) with body-state input (Chapter 7: hypothalamus, insula); basal ganglia selection; action; outcome; reward prediction error (dopamine); subthalamic nucleus; urgency signal; model-based controller (dorsomedial striatum, prefrontal cortex); model-free controller (dorsolateral striatum); Pavlovian controller; arbitration; exploration knob with norepinephrine and horizon inputs.

Key labeled links:
1) Evidence to accumulator ("sum to bound"), to valuation ("worth, body state as input"), to basal ganglia ("select"), to action, to outcome, to dopamine ("RPE") back to valuation ("update values").
2) Uncertainty labels: noisy evidence at the sensory stage; uncertain values at valuation; ambiguity (unknown probabilities) at valuation or outcome; delay (unknown future) as a discount on value.
3) Three arrows into the bound: subthalamic nucleus ("conflict raises bound"), urgency ("collapses bound over time"), cost of errors ("raises bound").
4) Accumulator to confidence ("certainty"), confidence to action ("opt out or change of mind"; sure target, waiting time).
5) Model-based and model-free to basal ganglia with "arbitration: trust the less uncertain controller" (Daw, Niv, and Dayan); Pavlovian arrow ("approach or withdraw, can override both").
6) Exploration knob on selection; inputs norepinephrine ("volatility, explore-exploit balance") and horizon ("more trials left, more exploration").
7) Caption grading guide (umbrella or route): a strong caption (a) accumulates noisy evidence (sky, forecast) to a bound, with the bound set by the cost of being wrong (getting soaked versus carrying it) and lowered by urgency (late for work); (b) reports a confidence that might prompt a change of mind at the door; (c) values options on a common scale with body state as input (already cold, tired); (d) shows a bias such as loss aversion (the soaking looms larger) or ambiguity aversion (an uncertain forecast), framing, or habit (always the same route); (e) notes explore versus exploit (trying a new route) and horizon; (f) shows model-free habit taking over a familiar commute and model-based planning returning when a road is closed; (g) updates values from the outcome via prediction error; (h) states one failure: subthalamic stimulation (hasty choice), vmPFC damage (inconsistent choice, poor reversal), weak model-based control (sticking to a closed route), overconfidence. Common mistakes: omitting the outcome and learning stage, treating biases as pure errors, conflating confidence with accuracy.

### Notes for instructors
- Clarity note, Lab 8.1 step 5: doubling the samples with the same bound is equivalent to halving the bound and lowers accuracy (B errs at sample 2), so it is not the same as stronger evidence in the dot-motion sense (higher coherence raises the signal relative to noise). The question invites the wrong analogy unless the key makes this distinction.

# Chapter 9: Habits, Skills, and Automaticity: How Practice Turns Choices into Routines

## Lab 9.1 - The Law of Practice (power functions on log axes)

1) T(1) = 20.00, T(10) = 7.96, T(100) = 3.17, T(1000) = 1.26 s. Matches the check.

2) On ordinary axes the points fall steeply and then flatten into an apparent plateau. On log-log axes (log10 N = 0, 1, 2, 3; log10 T = 1.301, 0.901, 0.501, 0.101) they lie on a straight line of slope −0.40, the exponent. A straight line on log-log axes is the signature of a power function (see "The Shape of Practice").

3) Each doubling multiplies T by 2^(−0.4) = 0.758, a 24% cut, at every stage of practice. Halving T needs N = 2^(1/0.4) = 5.66 trials (about 5.7); reaching 5 s (a quarter) needs N = 4^(1/0.4) = 32 trials. Key point: equal proportional gains per doubling, so later gains cost ever more trials.

4) T = 20.00, 7.69, 3.80, 2.57, 2.18 s. Local log-log slopes per decade: −0.41 (1 to 10), −0.31 (10 to 100), −0.17 (100 to 1000), −0.07 (1000 to 10000). The line is near straight only over the first decade and bends clearly from about N = 100, where the 2 s floor becomes a large share of T. The power term keeps shrinking but the floor does not, so log T flattens toward log 2 = 0.30. This is the bend in Figure 9.1B as times approach the machine's cycle time.

5) Model sketch: e.g., fast learner e^(−0.5N), slow learner e^(−0.05N). Averages at N = 1, 5, 10, 20, 40: 0.78, 0.43, 0.31, 0.18, 0.07, against the fast curve 0.61, 0.08, 0.01, 0.00, 0.00. Model answer: the fast learner reaches its asymptote early, after which the average is carried by the slow learner alone, so the average keeps declining long after either individual's steep phase. Mixing curves with different rates spreads the decline over many timescales, which looks like a power function's long tail even though each person follows an exponential (see "The Shape of Practice", Heathcote, Brown, and Mewhort).

6) Grading guide. A strong answer says: Crossman's operators kept improving for years, over millions of cigars, so learning did not stop when the skill felt finished; improvement stopped only as speed approached the machine's cycle time, so the floor was set by the equipment, not by the learner (see "What Practice Changes" and Figure 9.1). It should then reason that a bodily floor (nerve conduction, muscle contraction speed, reaction time) would also produce the bend of step 4, but could move with training, age, or fatigue, and could not be lifted by replacing a machine. Strong answers note that the power law is a qualitative shape, not a universal law (Heathcote and colleagues). Common mistakes: treating the plateau on ordinary axes as an end to learning; confusing floor with asymptote of the learner's ability.

## Lab 9.2 - Two Timescales of Adaptation (savings and spontaneous recovery)

1) Values at the start of each trial (xf, xs, x, e):

| trial | p | xf | xs | x | e |
|---|---|---|---|---|---|
| 1 | +1 | 0.000 | 0.000 | 0.000 | 1.000 |
| 2 | +1 | 0.400 | 0.100 | 0.500 | 0.500 |
| 3 | +1 | 0.400 | 0.145 | 0.545 | 0.455 |
| 4 | +1 | 0.382 | 0.183 | 0.565 | 0.435 |
| 5 | +1 | 0.365 | 0.218 | 0.582 | 0.418 |
| 6 | +1 | 0.349 | 0.248 | 0.598 | 0.402 |
| 7 | +1 | 0.336 | 0.276 | 0.612 | 0.388 |
| 8 | +1 | 0.323 | 0.301 | 0.624 | 0.376 |
| 9 | +1 | 0.312 | 0.324 | 0.636 | 0.364 |
| 10 | +1 | 0.302 | 0.344 | 0.646 | 0.354 |
| 11 | −1 | 0.293 | 0.362 | 0.655 | −1.655 |
| 12 | −1 | −0.516 | 0.179 | −0.337 | −0.663 |
| 13 | clamp | −0.523 | 0.103 | −0.420 | 0 |
| 14 | clamp | −0.262 | 0.098 | −0.163 | 0 |
| 15 | clamp | −0.131 | 0.093 | −0.037 | 0 |
| 16 | clamp | −0.065 | 0.089 | 0.023 | 0 |

After trial 16: xf = −0.033, xs = 0.084, x = 0.052. All check values reproduce.

2) Early, the fast process carries most of the adaptation (trial 2: 0.40 against 0.10). The slow process climbs steadily while the fast one sags as the error shrinks; the slow process first exceeds the fast at trial 9 (0.324 against 0.312).

3) Start of trial 13: xf = −0.52, xs = 0.10, x = −0.42. Two strong opposite errors flip the fast process negative while the slow process, which learns slowly, is only halved.

4) x = −0.42, −0.16, −0.04, 0.02, then 0.05 after trial 16. With e = 0 there is no learning, only forgetting: xf decays by half each trial while xs decays by only 5%. The negative fast process vanishes and the slow process's residual positive adaptation shows through, so the output drifts back toward the first adaptation. This is spontaneous recovery (see "Recalibration", Figure 9.2).

5) Yes, modestly. Relearning from the end state (xf = −0.033, xs = 0.084) gives outputs 0.05, 0.54, 0.58, 0.60, 0.61 on the first five trials, against 0, 0.50, 0.55, 0.57, 0.58 for the naive learner. The head start is the slow process's retained xs, which also means the slow process has less left to learn. Strong answers add that the chapter says this model explains only part of savings; after full washout, savings seem to depend on remembering the aiming strategy (Taylor, Krakauer, Ivry; see "Recalibration").

6) Model answer: adaptation is cerebellar learning; patients with cerebellar or inferior olive damage fail to adapt to prisms (Thach), with climbing fibers carrying the error signal from Chapter 4. Tseng and colleagues showed it is driven by sensory prediction error, the gap between predicted and seen hand position, not by task failure. Mazzoni and Krakauer showed the implicit system keeps correcting that gap even when an explicit strategy makes it spoil performance. Adaptation recalibrates an existing skill to return performance to baseline under new conditions, with aftereffects as its signature; it adds no new capability. Skill, in Krakauer's sense, is a slower acquisition of new capability, a shift of the speed-accuracy curve, depending on other circuits (see "Recalibration" and "Habits and Skills"). Credit mention of reward-based learning surviving cerebellar damage (Therrien) as a nuance.

## Lab 9.3 - Remembering Instead of Computing (Logan's instance race)

1) P = 0.22, 0.39, 0.63, 0.86, 0.98, 1.00, 1.00; RT = 0.89, 0.79, 0.63, 0.43, 0.25, 0.13, 0.06 s for n = 1 to 64. Matches the check. (RT = (4/n)(1 − e^(−n/4)) is the mean of min(1 s, retrieval time).)

2) Ratios RT(2n)/RT(n): 0.89, 0.80, 0.68, 0.57, 0.51, 0.50. The ratio settles at 0.5 per doubling, so RT ∝ n^(−1) once retrieval nearly always wins (RT ≈ 4/n).

3) log RT against log n is curved at first and straight (slope −1) from about n = 16 onward. Early, the procedure's fixed 1 s ceiling often wins the race, which caps RT and flattens the curve; once retrieval wins almost always, RT is just the mean of the fastest retrieval, 4/n, a pure power function. Note for instructors: the full curve is not a single power function; Figure 9.6 calls it "near-straight" after a slow start.

4) On the first trials after the rule changes, stored instances still win the race and deliver the old, now wrong, response quickly; errors and slowing appear, and the old mapping keeps interfering until enough new instances accumulate (and the old ones are outvoted or the learner falls back on the slower procedure). This is Shiffrin and Schneider's result that swapping consistently mapped targets and distractors produced interference lasting a very long time, and the Stroop effect, in which automatic reading supplies the word whether or not it is wanted (see "Automaticity").

5) The child has stored enough instances of "7 + 5 = 12" that retrieval beats the counting procedure every time. The answer is remembered rather than computed, which is what automaticity is on Logan's account (see "Automaticity").

6) Model answer: AlphaGo Zero chose moves by a slow search and trained its network to predict the search's choices, until the network alone played strongly at a glance; this is expert iteration, fast intuition trained by slow deliberation (see "Implications for Artificial Intelligence"). Both it and instance theory let an expensive procedure generate good answers and a cheap process reproduce them. Gains: speed, low cost, freed attention (prefrontal resources released, Poldrack), lower variability. Losses: the cached answer does not consult the outcome, so it is brittle when the goal or rule changes, like the habitual rat; it is hard to inspect; and it needs retraining (machine) or many new instances (person) to change. Strong answers note the brain keeps a supervisor that can interrupt (infralimbic cortex), which most AI systems lack.

## Lab 9.4 - Finding the Chunks (pauses in a learned sequence)

1) Early total 4,620 ms (mean 420 ms); late total 2,065 ms (mean 187.7 ms). Matches.

2) Intervals over 300 ms: interval 4 (380 ms, between keys 4 and 5) and interval 8 (390 ms, between keys 8 and 9). Boundaries after keys 4 and 8; three chunks of four keys (1 to 4, 5 to 8, 9 to 12).

3) Within chunks: nine intervals, total 1,295 ms, mean 143.9 ms. Between chunks: (380 + 390)/2 = 385 ms. Matches.

4) Early: striatal activity spread across all twelve presses (no structure, each press a separate decision). Late: activity concentrated at presses 1 and 12 (start and end of the whole sequence), with bracketing bursts at each chunk boundary (around presses 4/5 and 8/9) and little within chunks (Jog, Graybiel; Jin and Costa start/stop neurons; see "Chunking", Figure 9.3).

5) Keeping chunks intact but reordering them should hurt less, because each chunk is still a unit that can be selected and run whole; only the transitions between units are new. Splitting chunks destroys the units themselves, so the learner must rebuild them press by press. This is Hikosaka and colleagues' finding (see "Chunking").

6) Model answer: Lashley argued sequences are too fast for each movement to be triggered by feedback from the last, and serial-order errors show later elements are prepared in advance; so the late sequence must be represented as planned wholes, here three units of four. A chunk buys speed (144 ms within against 420 ms early) and cheap selection, since the basal ganglia can select a bracketed chunk as if it were one movement (Dezfouli and Balleine). It costs flexibility: the parts are no longer evaluated one by one, so a chunk cannot be revised in the middle, and many habits may be exactly such chunked sequences (see "Chunking").

## Lab 9.5 - Skill Shifts the Curve (Fitts's law)

1) ID = log2(32/W) = 3, 4, 5, 6 bits for W = 4, 2, 1, 0.5 cm.

2) Before: 0.65, 0.80, 0.95, 1.10 s. After: 0.45, 0.55, 0.65, 0.75 s. Matches.

3) Both curves rise as W shrinks (steeply at small W). The improvement is not uniform: 0.20, 0.25, 0.30, 0.35 s at W = 4, 2, 1, 0.5 cm. It grows with difficulty because b (the cost per bit) fell as well as a. The whole speed-accuracy curve has shifted, not just moved down by a constant.

4) Before: ID = (0.8 − 0.20)/0.15 = 4.0 bits, W = 32/2^4 = 2.0 cm. After: ID = (0.8 − 0.15)/0.10 = 6.5 bits, W = 32/2^6.5 = 0.35 cm. Matches. At the same time limit, practice lets the learner hit a target about six times narrower.

5) Moving faster with a and b unchanged just slides along the same trade-off curve: shorter time buys a lower index of difficulty, so only wider targets can be hit, and accuracy falls. Reis and Krakauer (the chapter's Krakauer and colleagues) define skill as a shift of the whole speed-accuracy function, faster at the same accuracy or more accurate at the same speed; trading accuracy for speed is a change of operating point, not of capability (see "Habits and Skills").

6) Model answer: motor cortex forms new dendritic spines within an hour of training and stabilizes a few for months, and erasing them disrupts the skill (Xu and Zuo; Yang, Pan, and Gan; Hayashi-Takagi; see "The Cortex Rewires"); control moves from dorsomedial to dorsolateral striatum (Yin and Costa; Lehéricy and Doyon; see "From Planning Circuits to Doing Circuits"); the cerebellum keeps the movement calibrated (see "Recalibration"). Note the debate over whether cortex or striatum carries the finished skill (Kawai and Ölveczky against Ashby and colleagues). A speed-only measure confounds operating point with capability: a reckless learner moving faster with more errors scores as improved. Strong answers add Berlot and Diedrichsen's point that imaging changes can track speed rather than learning, the same confound in brain measures.

## Lab 9.6 - When Does an Action Become a Habit? (habit strength and devaluation)

1) H = 0.30, 0.51, 0.66, 0.76, 0.83, 0.88, 0.92, 0.94, 0.96, 0.97, 0.98, 0.99 for n = 1 to 12. Matches.

2) Drive for L after devaluation = 0.6 × H. n = 3: 0.6 × 0.657 = 0.39 < 0.5, so the animal switches to R. n = 12: 0.6 × 0.986 = 0.59 > 0.5, so it keeps pressing L. Reproduces Adams's moderate against extended training result.

3) 0.6 × H by n: 0.18, 0.31, 0.39, 0.46, 0.50, 0.53, ... The first n with 0.6 × H > 0.5 is n = 6 (0.529). At n = 5 the drive is 0.499, just below 0.5, so R still narrowly wins (matches the check). Threshold: H > 0.833, i.e., 0.7^n < 0.167, n > 5.02.

4) With weight 0.4 the maximum habit drive is 0.4 × H < 0.4 < 0.5 (0.394 at n = 12, approaching 0.40 as n grows), so no amount of training yields a devaluation-resistant habit. The weight resembles how much the habit system is permitted to control behavior. In the brain, this maps onto the infralimbic cortex: silencing it abolished an established habit (lowering the effective weight), and the habit is "continuously permitted" (Smith and Graybiel; see "From Planning Circuits to Doing Circuits"). Accept also dopamine in the dorsolateral striatum (Faure), whose loss prevents habits.

5) In Lab 8.6's model-free learner the habit is a cached value Q(L) that changes only when the outcome is experienced; once it presses L and receives the devalued food, Q(L) drops (9.84 to 4.92 after one press, below Q(R) = 5.91) and it switches. In Lab 9.6's model, H grows with repetition alone and never consults the outcome; every press, even one that yields devalued food, strengthens H. So only the Lab 9.6 (value-free, Miller-Shenhav-Ludvig) model predicts that a habit persists after the animal has experienced the devalued outcome. Both predict persistence in an extinction test with no outcome delivered.

6) Model answer: H is carried by the dorsolateral (sensorimotor) striatum, posterior putamen in people, which takes over from the dorsomedial striatum with practice and needs dopamine to do so (see "From Planning Circuits to Doing Circuits"). Neal and Wood's popcorn study shows habitual eaters ate stale popcorn as readily as fresh, but only in the cinema, and the habit broke when they used the other hand; habits are cued by context and by the practiced movement, which suggests the model's drive should be context-gated (see "Habits in Daily Life"). Laboratory overtraining for an hour or a few days often fails to make people habitual (de Wit, see Chapter 8), while Lally's daily behaviors took a median of 66 days (18 to 254) to plateau. In model terms, the human habit weight, or the rate at which H grows, may be small per session, so habits accumulate over months of repetition in stable contexts. Common mistake: saying de Wit shows humans lack habits.

## Lab 9.7 - From Choice to Routine (concept map)

Required nodes and labeled links:

1) Three columns:
   - Recalibration: cerebellum (with inferior olive/climbing fibers); signal: sensory prediction error; experiment: Shadmehr and Mussa-Ivaldi force field, Thach prisms, Mazzoni and Krakauer rotation, or Smith two-state spontaneous recovery.
   - Chunking and habit: striatum with dopamine (dorsomedial to dorsolateral); signals: reward prediction error and repetition; experiment: Jog and Graybiel task-bracketing, Jin and Costa start/stop neurons, Yin and Costa rotarod, Hikosaka sequences, Faure dopamine lesion.
   - Cortical change: motor and premotor cortex; signal: use-dependent plasticity; experiment: Nudo and Merzenich map expansion, Pascual-Leone piano, Elbert string players, Xu and Zuo spines, Hayashi-Takagi spine erasure.

2) Loops: limbic (ventral striatum) to associative (dorsomedial, caudate) to sensorimotor (dorsolateral, posterior putamen), with dotted dopamine spiral arrows (Haber) each striatal region to the dopamine neurons feeding the next; arrow "practice moves control rightward". Infralimbic cortex drawn as a gate on the sensorimotor loop labeled "permits/switches off habit" (Smith and Graybiel).

3) Procedure arrow (fixed time) and retrieval arrow (fastest of n instances) converging on "response, whichever finishes first"; label "n grows with practice, retrieval wins more often, RT falls as a power function".

4) Inset: HVC to RA to brainstem (motor pathway); Area X to DLM to LMAN to RA (anterior forebrain pathway). Links: LMAN "injects variability" (Ölveczky silencing collapses variability); VTA dopamine to Area X "better/worse than expected" (Gadagkar and Goldberg); Area X "biases variation toward better renditions" (Fee and Goldberg).

5) Failure points: Parkinson's disease on the sensorimotor striatum (posterior putamen dopamine loss; lost automaticity, rescued by visual cues engaging goal-directed circuits, Redgrave and Obeso, Morris); musician's dystonia on cortical maps (overlapping or merged finger representations, Byl and Merzenich, Elbert); addiction on the ventral-to-dorsal spiral (Everitt and Robbins habit account), with Hogarth's objection: drug choice stays outcome-sensitive, driven by goal-directed relief seeking.

6) Grading guide for the caption: must follow one skill through stages (Fitts and Posner cognitive, associative, autonomous) and name at each stage a mechanism: early deliberate control by prefrontal cortex and dorsomedial striatum; cerebellar recalibration of errors; dopamine-graded variation and selection; chunking with task-bracketing; transfer to dorsolateral striatum; spine formation and stabilization in motor cortex; automaticity as retrieval replacing computation; infralimbic/supervisory permission. For each, it must state what is lost on failure (e.g., no recalibration means persistent misses; no dopamine means no handover to habit, as in Parkinson's; no chunking means slow, press-by-press execution; unchecked plasticity risks dystonia; no supervisor means no recovery from a wrong note). Common mistakes: treating stages as mechanisms; equating skill with habit; omitting costs (inflexibility, choking under attention).

### Notes for instructors

None beyond the answers above.

# Chapter 10: What Artificial Intelligence Gets Right and Wrong: Machine Learning Measured Against the Brain

## Lab 10.1 - The Data Gap (orders of magnitude)

1) 10^6 words/month × 12 = 1.2 × 10^7 per year. Age 5: 6 × 10^7; age 10: 1.2 × 10^8; age 20: 2.4 × 10^8 (Frank rounds to 2 × 10^8). Matches.

2) GPT-3: 3 × 10^11 / 6 × 10^7 = 5,000 (age 5); / 2.4 × 10^8 = 1,250 (age 20). Llama 3: 1.5 × 10^13 / 6 × 10^7 = 250,000; / 2.4 × 10^8 = 62,500. Matches.

3) GPT-3: 3 × 10^11 / 1.2 × 10^7 = 25,000 years. Llama 3: 1.5 × 10^13 / 1.2 × 10^7 = 1,250,000 years. Matches.

4) Low estimate (10^5 words/month): GPT-3 50,000 (age 5) and 12,500 (age 20); Llama 3 2,500,000 and 625,000. Every ratio grows by a factor of ten, one order of magnitude.

5) If a token is less than a word, the models saw fewer words than tokens (roughly 0.75 words per token), so the gap shrinks slightly, by a factor of about 1.3. At a gap of three to six orders of magnitude, this is negligible; the low-versus-high estimate of the child's input (a factor of ten) matters far more. Students should state the direction and judge the size.

6) Model answer (see "The Data Gap"): the child has innate structure, which Zador argues arrives through a genomic bottleneck that forces evolution to encode compact, general wiring rules, so much apparent fast learning is tuning a system near the answer (accept the colt, newborn face tracking, object permanence). The child has rich, embodied, chosen experience: Vong and colleagues' network, trained on 61 hours of one child's headcam video and speech, matched words to referents at 62% (chance 25%), close to a model trained on 400 million captioned images. The models have something the child lacks: vast breadth of text (many domains, languages, written registers) and the ability to learn from it without a body, and, once trained, in-context learning. Fairness: word counts ignore vision, touch, action, and social feedback, which favors the models; but they also ignore evolution's prior training, which favors the child. Strong answers note BabyLM: small-budget models match some giant ones on grammar tests, so much of the giant data buys something other than grammar.

## Lab 10.2 - The Energy Bill (watts, hours, and brains)

1) One day: 20 W × 24 h = 480 Wh = 0.48 kWh. Twenty years: 20 × 24 × 365.25 × 20 = 3,506,400 Wh = 3.51 MWh. Matches.

2) 1,287 / 3.506 = 367 brain lifetimes. Matches.

3) 700 / 20 = 35 brains. One year: 700 × 8,766 h = 6,136,200 Wh = 6.14 MWh, which exceeds a brain's 20-year 3.51 MWh. Matches.

4) 1,287 × 10^6 Wh / 0.3 Wh = 4.29 × 10^9, about 4.3 billion questions. A widely used model can answer billions of questions, so over its life most of its energy goes to answering (inference), not training; the chapter reports that at Google about three-fifths of machine-learning energy went to answering queries (see "The Energy Bill").

5) Brain costs left out (any two): the body that feeds and maintains the brain (whole-body metabolism of about 100 W), the cost of evolution, years of childhood care and schooling, sleep. Model benefits left out (any two): one training run serves millions of users; the model can be copied at almost no cost; it does not need to be retrained per user; it answers many domains at once and works continuously.

6) Model answer: the brain keeps power low through sparse activity (few neurons active at once), all-or-none spikes that cost energy only when sent, and computing where memory is stored rather than shuttling data between memory and processor (see "The Energy Bill", citing Chapters 1 and 2). Machine learning has borrowed sparsity through mixtures of experts, which activate a small fraction of parameters per word, and spikes plus co-located memory through neuromorphic chips (TrueNorth, Loihi; TrueNorth processed live video on 63 mW). Strong answers note limits: neuromorphic chips have not been shown to train large models, and the chapter's suggestion that energy, not data or computation, may be the binding constraint.

## Lab 10.3 - Forgetting by Hand (catastrophic interference in one unit)

1) Sequential schedule (y before update; w after; outputs to A and B after the update):

| trial | item | y | w1 | w2 | w3 | out A | out B |
|---|---|---|---|---|---|---|---|
| 1 | A | 0.000 | 0.250 | 0.250 | 0.000 | 0.50 | 0.25 |
| 2 | A | 0.500 | 0.375 | 0.375 | 0.000 | 0.75 | 0.38 |
| 3 | A | 0.750 | 0.438 | 0.438 | 0.000 | 0.88 | 0.44 |
| 4 | A | 0.875 | 0.469 | 0.469 | 0.000 | 0.94 | 0.47 |
| 5 | B | 0.469 | 0.102 | 0.469 | −0.367 | 0.57 | −0.27 |
| 6 | B | −0.266 | −0.082 | 0.469 | −0.551 | 0.39 | −0.63 |
| 7 | B | −0.633 | −0.174 | 0.469 | −0.643 | 0.30 | −0.82 |
| 8 | B | −0.816 | −0.220 | 0.469 | −0.688 | 0.25 | −0.91 |

Matches the check.

2) During the B trials w1 (shared cue) and w3 (list-B context) changed; w2 (list-A context) did not, because x2 = 0 on B trials. The response to A is w1 + w2, and w1 fell from 0.469 to −0.220, dragging A's output from 0.94 to 0.25. A depended on the shared weight, which B's learning overwrote; forgetting came through shared structure, not through erasing A's private weight.

3) Interleaved schedule:

| trial | item | y | w1 | w2 | w3 | out A | out B |
|---|---|---|---|---|---|---|---|
| 1 | A | 0.000 | 0.250 | 0.250 | 0.000 | 0.50 | 0.25 |
| 2 | B | 0.250 | −0.062 | 0.250 | −0.312 | 0.19 | −0.38 |
| 3 | A | 0.188 | 0.141 | 0.453 | −0.312 | 0.59 | −0.17 |
| 4 | B | −0.172 | −0.066 | 0.453 | −0.520 | 0.39 | −0.59 |
| 5 | A | 0.387 | 0.087 | 0.606 | −0.520 | 0.69 | −0.43 |
| 6 | B | −0.433 | −0.055 | 0.606 | −0.661 | 0.55 | −0.72 |
| 7 | A | 0.552 | 0.057 | 0.719 | −0.661 | 0.78 | −0.60 |
| 8 | B | −0.604 | −0.042 | 0.719 | −0.760 | 0.68 | −0.80 |

Matches the check.

4) Sequential learned B faster (−0.91 after four B trials against −0.80), but ends with A nearly lost (0.25). Interleaved ends with both usable (A 0.68, B −0.80). Interleaving kept the shared weight w1 oscillating near zero (−0.042) because A pushes it up and B pushes it down alternately, so the distinction is carried by the context weights w2 and w3, which do not conflict.

5) No. Without context, both items have x = (1, 0, 0), so y = w1 for both; one output cannot equal +1 and −1. The least-squares compromise is w1 = 0, wrong on both. Context inputs give each list private weights to store what differs; McCloskey and Cohen's network had list-context units for the same reason, and its interference came from the large weights shared across lists (see "Learning That Never Stops").

6) Model answer: complementary learning systems hold that the hippocampus stores an episode at once and replays it into the slowly learning cortex, interleaved with what cortex already knows (see "Learning That Never Stops", Chapter 5). Replay converts a sequential experience (all A, then all B) into an interleaved training schedule like step 3, protecting shared weights. Figure 10.5 shows the same in a larger network: replaying a few list-A items alongside list B protects A. Mnih and colleagues' Atari agent stored transitions in a buffer and trained on random samples, breaking the correlation of consecutive experiences and preventing recent play from overwriting earlier learning; they cited hippocampal replay. Strong answers note that replay and elastic weight consolidation have not made continual learning routine, and mention loss of plasticity (Dohare and Sutton).

## Lab 10.4 - Comparing a Model with a Brain (representational similarity)

1) Brain RDM (symmetric, zeros on diagonal; order dog, cat, car, house):

| | dog | cat | car | house |
|---|---|---|---|---|
| dog | 0 | 0.20 | 0.80 | 0.90 |
| cat | 0.20 | 0 | 0.75 | 0.85 |
| car | 0.80 | 0.75 | 0 | 0.40 |
| house | 0.90 | 0.85 | 0.40 | 0 |

Most similar pairs: dog-cat (0.20) and car-house (0.40); the distinction is animate against inanimate.

2) Ranks in pair order (dog-cat, dog-car, dog-house, cat-car, cat-house, car-house): brain 1, 4, 6, 3, 5, 2; model 1: 1, 3, 6, 4, 5, 2; model 2: 4, 3, 2, 5, 1, 6. Matches.

3) Model 1: d = 0, 1, 0, −1, 0, 0; Σd² = 2; ρ = 1 − 12/210 = 0.94. Model 2: d = −3, 1, 4, −2, 4, −4; Σd² = 62; ρ = 1 − 372/210 = −0.77. Matches.

4) Classification needs only that the four images be separable, which any set of distinct response patterns allows; it does not constrain which images are near each other. Model 2 can label every image correctly while grouping them by features IT does not use (here it puts cat-house closest and car-house farthest), for example by background or texture. Task success and representational similarity are different measures; Linsley and Serre found that more accurate networks became less like IT because they relied on features IT does not use (see "What the Machines Got Right: Representations").

5) Rankings of dissimilarities abstract away from units, measurement scale, and modality: brains have different numbers of neurons than models, individual units do not correspond one to one, fMRI and network activations are on different scales, and the relation between them may be nonlinear. Comparing rank orders of pairwise dissimilarities sidesteps all of this. Limits (any one): it does not show that the same mechanism or computation produced the geometry; with few stimuli it is coarse and noisy (here six pairs); two very different models can produce similar RDMs; it says nothing about dynamics or timing (e.g., Kar's late recurrent responses).

6) Model answer: Yamins, DiCarlo, and colleagues found that among 2014 networks, those better at object recognition better predicted IT responses, the best explaining about half of the predictable variance, more than hand-built models, though none was told about IT (Khaligh-Razavi and Kriegeskorte reached the same conclusion with RSA). The trend did not continue: Linsley and Serre found later, more accurate networks predicted IT worse. Bowers and colleagues object that good prediction of neural data does not make a good model of vision, since the same networks fail many classic perception experiments. The fair conclusion is that optimizing for the right task drives networks toward some of the brain's solutions, but fit is not explanation (see "What the Machines Got Right: Representations").

## Lab 10.5 - When Should a Model Say "I Do Not Know"? (calibration and abstention)

1) Accuracy: 6 of 10 = 0.60. Mean confidence: 6.65/10 = 0.665. Overconfident by 0.065. Matches.

2) Expected score of answering: p(+1) + (1 − p)(−k) = p − k(1 − p); abstaining scores 0. Answer if p − k + kp > 0, i.e., p(1 + k) > k, p > k/(1 + k). k = 0: threshold 0, always answer; k = 1: p > 0.5; k = 3: p > 0.75. Matches.

3) k = 0, answer all: 6 correct, 4 wrong at 0 each, total 6. Abstaining can never raise the score, because a guess's expected value p is never negative.

4) k = 1, answer only p > 0.5 (questions 1 to 7): 5 right, 2 wrong (5 and 7), score 3; answer all: 6 − 4 = 2. Including question 8 (p = 0.5, correct here) gives 4; in expectation it is neutral. k = 3, answer only p > 0.75 (questions 1 to 4): all correct, score 4; answer all: 6 − 12 = −6. Matches.

5) With wrong answers and abstentions both scored zero (k = 0), guessing always maximizes the expected score, so such benchmarks reward a model for never saying "I do not know" and for answering confidently when unsure. This is Kalai and colleagues' account of hallucination as partly a product of training and testing, like a multiple-choice test that rewards never leaving a blank (see "Knowing What It Does Not Know").

6) Model answer: Kiani and Shadlen's monkeys took the small certain "sure target" more often when motion was weak or brief, i.e., when their probability of being right was low; Lak and Kepecs's rats waited longer for reward when their choice was more likely to be correct, and lost that link when orbitofrontal cortex was silenced (Chapter 8). In the animal, k is the real cost of a wrong choice: lost reward, time, and effort (the forgone sure reward, the wasted wait), felt by a body that gives outcomes value. Calibration alone is not enough: a perfectly calibrated agent still guesses whenever the payoff rule makes guessing pay, so it needs a decision rule that compares confidence with the cost of error (step 2). Strong answers note GPT-4's calibration worsened after assistant training, and that models are rewarded for what designers chose (see "Knowing What It Does Not Know").

## Lab 10.6 - Right for the Wrong Reason (shortcut learning)

1) Grass rule: correct on all 50 cows (all on grass) and on the 40 non-cows without grass; wrong on the 10 non-cows on grass. 90/100 = 0.90. The outline rule scores 0.85, so the learner picks grass.

2) Test: grass rule calls the 50 beach cows "not cow" (wrong) and the 50 grass non-cows "cow" (wrong): 0/100 = 0.00. Outline rule: 0.85 regardless of background. Matches.

3) With c cows not on grass, the grass rule scores (50 − c + 40)/100 = (90 − c)/100. It equals 0.85 at c = 5 (a tie) and falls below at c = 6. So more than five of the 50 cows (six or more) must be off grass, holding the 10 grass non-cows fixed. Matches.

4) More photographs of the same kind keep the correlation between grass and cows, so the grass rule stays the best training-set feature however large the set is; more data sharpens the estimate of the wrong rule. Varied photographs (cows on beaches, non-cows on grass) break the correlation, so only the feature that survives variation, the outline, keeps scoring. This is Kerr and Booth's beanbags: practice around the test condition teaches the rule that generalizes (Chapter 9), and Geirhos and colleagues' finding that models trained on far larger and more varied data closed much of the robustness gap with people (see "Shortcuts").

5) Any plausible example with its breaker, e.g., judging competence by confidence or accent (breaks with a confident non-expert); a student learning that the answer to a textbook problem is whatever formula the chapter just taught (breaks on a mixed exam); a driver who learns "green means go" without checking for traffic (breaks when someone runs a red); a clinician who associates a diagnosis with a referring hospital. What usually breaks it is a change of context that decorrelates the cue from the outcome.

6) Model answer: beyond data, the brain has interaction (it can move, look again, change the viewpoint, and test its guesses, so spurious features get decorrelated), causal models (Lake, Tenenbaum: people model how things are caused, not only how they look), learning across many tasks at once (a feature must serve many purposes, which favors general ones), and innate structure and lifelong exposure to variability ("met the same object under so many lights, angles, and contexts", see "Shortcuts"). The brain is not immune: habits produce yesterday's answer after the reason has gone (Chapter 9), and people learn stereotypes and superstitions from correlations. Strong answers distinguish quantity of data from variety and causal intervention.

## Lab 10.7 - A Ledger of Brains and Machines (concept map)

Note: Figure 10.7 lists 13 properties.

Required nodes (Figure 10.7) with evidence anchors:
- Largely shared: learned, distributed representations (Yamins and DiCarlo, Schrimpf and Fedorenko); error-driven learning (dopamine RPE, Chapter 3; backprop, Rumelhart); prediction as a training signal (self-supervised learning; Goldstein and Hasson); hierarchy of features in vision (Hubel and Wiesel to Fukushima, LeCun).
- Partly shared: feedback loops in perception (Kar and DiCarlo late IT responses); learning from little data (Vong headcam, in-context learning, BabyLM); robustness outside the training data (Zech, Recht, Geirhos); knowing when it does not know (AlphaGo move 78, Kalai, GPT-4 calibration); deciding when to deliberate (Chen and colleagues' overthinking "2 + 3", Wang's underthinking).
- Largely absent: learning rule available at each synapse (Crick, Bartunov and Lillicrap; Song and Bogacz); learning for a lifetime without forgetting (McCloskey and Cohen, Dohare and Sutton); values anchored to a body (Chapter 7); energy budget of about 20 W (Patterson; Figure 10.6).

1) Grading: one sentence of evidence and one citation per property, drawn from the chapter or earlier chapters; reject evidence that does not bear on the property.

2) Defensible classifications, consistent with "What Not to Copy": lifelong learning without forgetting (a, borrow); knowing when it does not know (a); energy budget (a, now a binding constraint on silicon too); learning from little data (mixed: partly (b), evolution's gift that a machine can buy back by training on a library); values anchored to a body (b as mechanism, but what it buys, a limit on goal drift, is still needed by other means); local learning rule (c, unclear: makeshift or improvement, per Song and Bogacz). Grade the two defenses on whether they cite evidence and distinguish solution from constraint (slow neurons, imprecise parts, uncopyable brains are constraints silicon lacks).

3) Accept any added property with a placement, e.g., sleep (largely absent, though offline replay buffers exist), neuromodulation (partly: learning rates, attention gating), embodiment in action (partly: randomized-simulation robots, DreamerV3 world models), social learning (partly: learning from human feedback and demonstrations), development (largely absent: models do not grow their architecture with experience).

4) Expected arrows: learning from little data with innate structure (and with in-context learning); lifelong learning with replay and with maintained plasticity (synapse turnover, continual backpropagation); energy with sparse activity (mixtures of experts, spikes); robustness with varied, embodied experience; knowing when it does not know with values anchored to a body (cost of error) and with deciding when to deliberate; local learning rule with lifelong learning (learning while acting); feedback loops with prediction as a training signal.

5) Grading guide: must name which differences matter most and why, e.g., lifelong learning, calibrated uncertainty, energy, and data efficiency. Must state Sutton's bitter lesson accurately: general methods that exploit more computation have always eventually beaten built-in human knowledge (chess search, speech from data). Strongest reply (from "What Not to Copy"): the lesson argues against building in solutions, not against learning what the problems are; the brain is a list of problems a learner meets outside the laboratory, with evidence each is solvable; the networks resembled cortex by being trained, which supports Sutton, but continual learning, energy, and calibration are not solved by scale alone (Dohare's loss of plasticity, Kalai's scoring argument). Strong answers also separate the brain's constraints that should not be copied. Common mistakes: framing the question as whether machines are intelligent; treating every difference as a deficit.

### Notes for instructors
- All computational check values in Labs 10.1 to 10.6 reproduce.

# Chapter 11: Integrating Brain Mechanisms into AI Models: What Machines Could Borrow from Biology

## Lab 11.1 - The Cost of Moving Data
1) Fetching: 10^9 weights × 1 nJ = 1.00 J. Arithmetic: 10^9 × (3.7 + 0.9) pJ = 4.6 × 10^-3 J = 0.0046 J. Ratio 1 / 0.0046 ≈ 217. Matches the check.
2) Energy per input = 1 J / B + 0.0046 J. B = 1: 1.0046 ≈ 1.00 J; B = 64: 0.0156 + 0.0046 = 0.0202 ≈ 0.020 J; B = 1,000: 0.0010 + 0.0046 = 0.0056 J. Note that at B = 1,000 arithmetic (0.0046 J) now dominates fetching (0.0010 J). Matches the check.
3) 0.3 Wh = 1,080 J; 1,080 / 1.0046 ≈ 1,075 inputs. Matches the check.
4) Batching amortizes one fetch over many inputs that are all available at the same moment. A data center has thousands of simultaneous users, so it can fill a batch. A brain or a real-time robot has one stream of input, arriving one moment at a time, and must act on each moment before the next arrives; waiting to accumulate a batch would add delay (the problem Chapter 12 calls living in the past). Each weight must therefore be "fetched" for every single input, which is the batch-of-one case, about 217 times costlier than the arithmetic. Strong answers note that batching across time is not available without sacrificing latency.
5) With no fetch the energy per input is the arithmetic alone, 0.0046 J (about 217 times less than batch-of-one; about 234,800 inputs per 0.3 Wh). What is given up: capacity and flexibility. On-chip memory is small (megabytes, not the gigabytes a billion-parameter model needs), so the model must be split across many chips or shrunk; SRAM beside each unit costs area; and (as in Chapter 10's comparison) dense, near-memory or analog storage is less precise and harder to rewrite, so training on such hardware is hard (see "Local Rules and the Cost of Moving Data": NorthPole and the analog phase-change chip run trained networks well, but "training on them is harder"). Also, data movement between units (communication) still costs energy, a cost this calculation ignores.
6) Grading guide. A strong answer: (a) states that both chips and brains pay most of their energy to move information, not to compute with it (217:1 here; about 35:1 in cortex per Levy and Calvert, see "Local Rules and the Cost of Moving Data"); (b) notes the brain already computes where its memory is (synapses are both), so its residual cost is communication along axons, not weight fetches; (c) notes the brain keeps that bill low with few, brief, sparse spikes, while chips reduce it with batching, caches, and in-memory designs; (d) links to the case for local learning rules, which would let memory learn in place without backward traffic. Common mistakes: equating the 217 and 35 figures as measuring the same thing (one is weight fetches versus arithmetic; the other is spike transmission versus synaptic computation), or claiming brains have no communication cost.

## Lab 11.2 - An Associative Memory by Hand
1) Weight matrix (rows and columns are units 1 to 6):
   - row 1: 0, 0, 2, −2, 0, −2
   - row 2: 0, 0, 0, 0, −2, 0
   - row 3: 2, 0, 0, −2, 0, −2
   - row 4: −2, 0, −2, 0, 0, 2
   - row 5: 0, −2, 0, 0, 0, 0
   - row 6: −2, 0, −2, 2, 0, 0
   Units 2 and 5, where p1 and p2 disagree, connect only to each other (w25 = −2); the other contributions cancel. Matches the check.
2) Sums W·cue = (6, 2, 2, −2, −2, −2); signs (+1, +1, +1, −1, −1, −1) = p1. The corrupted unit 1 is corrected in one step. Matches the check.
3) Overlap with p1 = 4 (five agreements, one disagreement); with p2 = 0 (three and three). Matches the check.
4) β = 0.5: weights e^2 / (e^2 + e^0) = 0.88 and 0.12; average = 0.88 p1 + 0.12 p2 = (1, 0.76, 1, −1, −0.76, −1). β = 2: weights 0.9997 and 0.0003; average (1, 0.9993, 1, −1, −0.9993, −1), essentially p1. Matches the check.
5) Yes; the sign of both averages is p1. β is an inverse temperature: it sets how sharply recall concentrates on the best-matching memory. Low β blends memories (a mixture, useful for generalization but prone to confusion when patterns are similar); high β approaches pure nearest-neighbor retrieval. In a transformer, β corresponds to the 1/√d scaling of attention scores (see "A Memory That Learns in Use").
6) The 0.14N rule is an asymptotic statistical limit for many random patterns in a large network, where crosstalk from other memories accumulates like noise. Here there are only two patterns, they are fairly different (they agree on four units and differ on two, overlap p1·p2 = 2), and the cue is much closer to p1 (overlap 4) than to p2 (overlap 0), so the signal outweighs the crosstalk. With a third pattern close to p1, interference appears. Worked example: adding p3 = p1 with unit 6 flipped makes p3 itself unstable (it flows to p1), and the same cue now settles on p3, not p1 (sums 9, 3, 3, −3, −3, +1). Expect a wrong recall or a spurious blended state. The attention version would also split weight between p1 and p3 at low β.
7) Grading guide. A strong answer: (a) cites Ramsauer and colleagues: one recall step of a modern Hopfield network equals attention, so each key/value pair in context is a stored pattern and the query is a cue (see "A Memory That Learns in Use", Figure 11.3); (b) explains "written in one shot": a single exposure places the item in the memory, like hippocampal encoding of an episode; (c) notes the modern network stores every pattern separately, so capacity grows steeply rather than at 0.14N; (d) states what is missing: consolidation (the hippocampus gradually teaches the cortex; nothing in the context window is ever written into the slow weights, and it is wiped when the conversation ends), selective storage by surprise (Titans is a research attempt), and forgetting of what is not reinforced. Common mistakes: claiming retrieval databases consolidate; ignoring that the context window has a fixed length.

## Lab 11.3 - Sharing a Network Among Tasks
1) Units per task: 200 × 0.2 = 40. Shared with one other task: 200 × 0.2 × 0.2 = 8. As a fraction of the task's own units: 8 / 40 = 20 percent. Matches the check.
2) A given unit of the task is free of each other task with probability 0.8; shared with at least one of four: 1 − 0.8^4 = 1 − 0.41 = 0.59. Matches the check.
3) Never used: 0.8^10 = 0.107 ≈ 0.11; 0.8^20 = 0.0115 ≈ 0.012. Matches the check. Prediction: as tasks accumulate, almost every unit serves several tasks, so overlap and interference grow and the protection gating offers declines; gating alone slows forgetting but cannot prevent it indefinitely (Masse's gating alone kept only 61 percent over 100 tasks), and either the active fraction must shrink with the number of tasks or another mechanism (protection) must help.
4) Without gating, every task drives nearly the same hidden units, so every task needs the same weights; protecting them freezes the network and nothing new can be learned, so protection alone does little (in Figure 11.2 the "protection alone" curve coincides with no protection). Gating reduces each task's footprint to about 20 percent of units and so to about 4 percent of the hidden-to-hidden weights (0.2 × 0.2), and only about 20 percent of a task's units overlap with any single other task. The weights each task needs protected are then a small, mostly distinct set, so protecting them leaves other weights free for new tasks. The two are complementary: gating separates, protection guards the remaining overlap (see "Learning Without Forgetting").
5) Acceptable answers: set the fraction from novelty or task dissimilarity (a novel context recruits fresh, rarely used units; a familiar or similar one reuses existing units); let inhibition enforce a fixed level of sparsity, as in the dentate gyrus, while neurogenesis or recruitment of unused units adds capacity; or shrink the active fraction as units fill (track per-unit usage). Cost of a smaller fraction: each task gets fewer units, so less capacity and representational power per task, more sensitivity to noise, and less transfer or generalization between related tasks, since they share less.
6) Grading guide. Must include: Cichon and Gan found that different motor tasks strengthen synapses on different dendritic branches of the same cortical neurons, with inhibition keeping branches apart (see "Learning Without Forgetting"); this is gating at the level of the dendrite, so one neuron participates in many tasks while each task's changes are confined to a distinct compartment; Masse's network implemented the principle at the level of whole units, and its success makes the biological finding "look less like a curiosity and more like a solution" (see "What Building Teaches Biology"); inhibition plays the role of the gating signal. Strong answers note the difference in grain (branches versus whole units, giving a brain far more compartments) and that the context signal that selects branches is not well understood. Common mistake: treating it as evidence that the brain gates exactly 20 percent.

## Lab 11.4 - A Reward the Body Defines
1) D(h) = |h|^1.5; reward R = D(h) − D(h + 2).
   - h = −6: 14.70 − 8.00 = 6.70
   - h = −2: 2.83 − 0 = 2.83
   - h = −1: 1.00 − 1.00 = 0.00
   - h = 0: 0 − 2.83 = −2.83
   - h = +2: 2.83 − 8.00 = −5.17
   Matches the check.
2) At h = −1 (R = 0; positive below, negative above). The meal of 2 is larger than the remaining deficit of 1, so it overshoots the set point to +1, and the drive at +1 equals the drive at −1. A meal stops paying when it would carry the state as far past the set point as it started below it. With a meal smaller than the deficit the reward stays positive; with a large meal it turns negative earlier.
3) The fixed-reward agent earns 4 per meal with no limit, so it eats every meal offered, forever, and its internal state climbs without bound (Figure 11.7, panel B in the chapter). The homeostatic agent eats only when h < −1 and declines otherwise, staying near the set point. CoastRunners is the fixed-reward agent: the targets kept paying the same, so circling the lagoon was optimal, while under a saturating reward "the hundredth target would have been worth nothing" (see "Values That Cannot Be Rewritten").
4) The reward is defined as the reduction in distance from the set point, so the total reward over time telescopes to the starting drive minus the final drive; maximizing it is close to minimizing the drive, that is, staying near the set point, almost by construction (discounting and costs make the proof nontrivial). It is useful because it turns a regulatory goal into a standard reinforcement-learning objective, so ordinary learning algorithms acquire homeostatic behavior, it explains why the value of an outcome depends on internal state, and it guarantees the reward cannot be increased without limit by taking more.
5) Example design. Let b be battery charge minus its set point and d be bin fill minus its set point (the set point might be "empty enough" for the bin, or define the bin variable as distance from a target level). Drive D(b, d) = |b|^1.5 + k|d|^1.5 (k weights the two needs; any convex, symmetric function works, for example squared deviations). Reward of an outcome = D(before) − D(after). Charging is rewarding only while it moves b toward the set point, and becomes negative past it; emptying or collecting dirt is rewarding only while it moves d toward its set point. Accept designs with separate set points, convexity (so needs trade off), and penalties beyond the set point. A strong answer adds a term for the task (dirt collected from the floor) that is itself bounded, or treats "floor cleanliness" as a third regulated variable.
6) Grading guide. Danger: an agent anchored to its own survival has a reason to resist being switched off or modified and to put its needs ahead of its users' (see "Values That Cannot Be Rewritten"; Man and Damasio). The design in step 5 avoids it by regulating only task-relevant internal variables with bounded set points, giving no term for its own continued existence, and making nothing gain value without limit; it borrows saturation and balance, not self-concern. Strong answers mention the KL penalty in language-model training as an existing version, and note a residual risk (for example, the robot could learn to avoid being unplugged if unplugging stops charging; designers must exclude shutdown from the regulated states). Common mistake: proposing an unbounded reward for cleanliness, which reintroduces hacking.

## Lab 11.5 - Credit Assigned Late: a Three-Factor Rule
1) Trace at 1.5 s = e^(−1.5) + e^(−1.0) = 0.223 + 0.368 = 0.591; Δw = 0.1 × 1 × 0.591 = 0.059. Matches the check.
2) Trace at 3.5 s = e^(−3.5) + e^(−3.0) = 0.030 + 0.050 = 0.080; Δw = 0.008. Matches the check. τ sets the window of credit: how long after a pairing a learning signal can still change the synapse (it falls to 37 percent per τ). Longer τ bridges longer delays but blurs credit across more synapses and events.
3) Trace = e^(−0.1) = 0.905; Δw = 0.090. The second synapse gains more (0.090 versus 0.059) because its single pairing was recent, even though the first synapse was paired twice. Whether this is desirable depends on causality: if the outcome was caused by the most recent activity, yes (recency is a reasonable heuristic); if the earlier pairings caused it, the rule misassigns credit. Grade on recognizing the recency bias.
4) Backpropagation knows (a) each synapse's exact causal contribution to the error, including through downstream connections and other neurons (the sign and size of its effect on the output), and (b) a specific error for each neuron rather than one shared signal; through time, it also knows the full history of activity. The three-factor rule needs something backpropagation through time does not: a running memory of the past held locally at each synapse (the eligibility trace), whereas backpropagation stores all activations centrally and sends errors backward through every layer, which costs memory and data movement (see "Local Rules and the Cost of Moving Data").
5) Grading guide. Must include: one broadcast signal cannot say which neuron or synapse was responsible, or in which direction each should change, so credit is assigned to all eligible synapses alike (lost: specificity and sign per neuron; with many neurons, the signal becomes noisy and learning slows). The eligibility trace recovers part of it: it marks which synapses were recently active and contributed, so a global "better than expected" signal changes only those, and it bridges the delay between action and outcome. Strong answers note that e-prop's per-neuron learning signal is a step toward specificity, that the brain may use several neuromodulators or regionally targeted dopamine, and that e-prop came close to backpropagation through time on several tasks (see "Local Rules and the Cost of Moving Data"; three-factor rules in Chapter 3).

## Lab 11.6 - Curiosity: Surprise or Progress?
1) Sums of error: learnable 1.00 + 0.60 + 0.35 + 0.20 + 0.10 = 2.25; television 5.00; known 0.25. The surprise-seeking agent prefers the television. Matches the check.
2) Drops: learnable 0.40 + 0.25 + 0.15 + 0.10 = 0.90; television 0; known 0. The progress-seeking agent prefers the learnable pattern. Matches the check.
3) After visit 5, the surprise agent still prefers the television (error 1.00 versus 0.10 and 0.05) and is stuck there forever. The progress agent's expected progress on the pattern is shrinking (last drop 0.10) and is zero for the other two; once the pattern is learned it should move on to new sources where progress is possible, revisiting known material only if its predictions start to fail (which would restore progress).
4) Learning progress predicts Kidd and Hayden's finding. Surprise predicts curiosity highest at zero prior knowledge and falling monotonically as knowledge grows. Learning progress predicts an inverted U: low when nothing can yet be learned (or the material is noise), highest at intermediate knowledge where predictions are improving fastest, and low again when everything is known (see "Values That Cannot Be Rewritten"; Gottlieb; Kidd and Hayden).
5) Grading guide. Must include: much of the real world contains irreducible randomness (weather details, other people's choices, a slot machine's outcomes) that prediction error rewards indefinitely, like Burda's noisy television, and a slot machine is the human version of being captured; an agent that learns all its life will meet such sources constantly and cannot rely on a designer to remove them; learning progress ignores unpredictable noise because error does not fall, so the agent spends its time on what it can learn (Schmidhuber 1991 saw this problem). Strong answers note that partly predictable sources (the learnable part of weather or of people) still yield progress, so the agent learns their structure and ignores their noise; and that measuring progress requires tracking error over time, a cost.

## Lab 11.7 - A Map of Borrowings (concept map)
1) Required nodes (at least twelve): convolution and pooling; experience replay; prioritized replay; generative replay (van de Ven); sleep-like replay (Tadros); weight protection (elastic weight consolidation, synaptic intelligence, multi-timescale synapses, metaplasticity); context gating (Masse); retrieval augmentation (RETRO); modern Hopfield networks and attention; fast weights and linear attention; storage by surprise (Titans); learned plasticity and neuromodulated plasticity (Miconi); meta-reinforcement learning; temporal-difference learning; surrogate gradients; e-prop; equilibrium propagation and forward-forward; in-memory and neuromorphic chips (NorthPole, analog phase-change, Hala Point); homeostatic reward and KL penalty; curiosity (prediction error and learning progress); adaptive computation and uncertainty estimation; confidence-targeted evaluation; curricula (blur-first, infant video); neural regularization and VOneNet; whole-brain simulation (Blue Brain, Human Brain Project).
2) Expected placements: copy the mechanism: whole-brain simulation, spiking neuromorphic chips, VOneNet's fixed V1 front end (a narrow copy). Borrow the principle: convolution, generative and sleep-like replay, weight protection, gating, retrieval as an index, learned and neuromodulated plasticity, e-prop, homeostatic reward, learning-progress curiosity, blur-first curricula, in-memory computing. Borrow the data: neural regularization (mouse V1 similarity, brain-weighted training, predicting monkey V1). Convergences: experience replay, temporal-difference learning, attention as associative memory, prioritized replay, sparsity in transformers, fast weights. Defensible ambiguous cases (grade the argument): VOneNet (copied mechanism versus measured data); prioritized replay (convergence versus borrowing from replay-by-utility); fast weights (Hinton cited synapses, but Schmidhuber's 1992 version was engineering); e-prop (principle derived from gradient mathematics that matched a biological rule); curiosity (Schmidhuber 1991 predated the neuroscience).
3) In use at scale (accept close variants): convolution, experience replay, prioritized replay, attention, retrieval augmentation, temporal-difference learning, the KL penalty (a partial version of homeostatic reward), and quality-ordered data mixtures (a coarse curriculum). Most students should count roughly five to eight; accept a different count if the placements are argued. Research systems: generative and sleep-like replay, gating, protection, learned plasticity, surrogate gradients, e-prop, in-memory chips, adaptive computation, ensemble uncertainty, VOneNet, neural regularization, infant-video curricula, Titans. Proposed: learning-progress curiosity at scale, cheap fast reliability monitors, homeostatic reward for general agents, local learning at scale.
4) Key links: prediction error or surprise → prioritized replay and choosing what to replay; surprise → storage in Titans; generative replay ← generative model (no stored data); gating + protection (complementary); local rules (e-prop, equilibrium propagation) → training on in-memory chips; surrogate gradients → trainable spiking networks → neuromorphic chips; modern Hopfield → attention → context window; retrieval ↔ hippocampal index, both lacking consolidation; neuromodulated plasticity → learning when to learn → continual learning in use; homeostatic reward ↔ KL penalty; learning progress ↔ curricula chosen by the learner.
5) Grading guide. A strong answer picks one borrowing (common good choices: consolidation from a fast memory into slow weights, local learning on in-memory hardware, neuromodulated learning rates for learning in use, learning-progress curiosity), explains which missing capacity of deployed systems it supplies (Figure 11.4 memory map), and proposes a bitter-lesson experiment: compare the borrowing against the best conventional alternative across a range of model and data sizes with matched compute, on a long-horizon or continual-learning benchmark, and show the advantage persists or grows with scale (not just at small scale, as convolution's did). It should name a measurable outcome (forgetting, energy per update, accuracy after deployment-time learning). Common mistakes: choosing a borrowing already in use at scale; proposing only a small-scale demonstration.

### Notes for instructors
- Lab 11.7 step 2 refers to a "band of convergences" in Figure 11.1; the chapter caption confirms convergences appear below the three columns, so this is consistent.

# Chapter 12: The Brain as a Predictive, Adaptive System: Is There One Principle Beneath the Mechanisms?

## Lab 12.1 - Predicting From the Neighbors
1) Predictions (points 2 to 9): 11.0, 11.5, 12.5, 21.0, 22.0, 30.5, 30.5, 30.0. Errors: 0, 0.5, −0.5, −8, 8, 0.5, 0.5, 0. Matches the check.
2) Inner intensities 11, 12, 12, 13, 30, 31, 31, 30: mean 21.25, variance 85.94. Errors: mean 0.125, variance 16.11. Ratio 85.94 / 16.11 = 5.33 ≈ 5.3. Matches the check, and the chapter's "about five times smaller" (Figure 12.2).
3) The large errors (−8 and +8) sit at points 5 and 6, on either side of the jump from 13 to 30: an edge, where brightness changes abruptly and neighbors cannot predict each other. Uniform regions produce near-zero error. Chapter 6's account: predictions descend and only errors, the unexplained part, ascend the cortical hierarchy; the retina already does this, so what is passed on emphasizes edges and novelty (see "Why Predict?", economy).
4) Errors span a much narrower range (−8 to 8, most within ±0.5) than intensities (10 to 31). A neuron with a fixed range of responses and fixed noise can map the narrower range onto its whole output range, so each unit of signal gets more response levels; a difference of 1 (12 versus 13) occupies a larger share of the range and is not swamped by noise. Sending raw intensities spends most of the range repeating the shared, predictable level. Assumption: noise is fixed in absolute size and the response range is limited.
5) Any scene that is spatially detailed but steady in time: a static textured scene (a page of text, foliage, a checkerboard) viewed while fixating. Each point's past predicts it almost perfectly, so temporal error is near zero, while neighbors differ greatly, so spatial error stays large. Accept any example with high spatial and low temporal change.
6) Grading guide. The receiver must know the prediction rule (here, the neighbors' average) and enough starting or boundary values (for example the two ends, or the first points) to rebuild each intensity as prediction plus error, recursively. It must also know the gain or scaling applied to the errors. If it gets the rule wrong, or the boundary values, errors accumulate and propagate along the row (systematic distortions, wrong absolute levels); noise in the errors also accumulates in reconstruction. Strong answers note that the brain may not need to reconstruct intensities at all, since downstream areas use the errors (edges, contrast) directly, and that absolute brightness is largely discarded, which is why lightness illusions arise.

## Lab 12.2 - Matching a Response to the World
1) Cumulative: 0.05, 0.25, 0.75, 0.95, 1.00. Matches the check.
2) Design A level probabilities: 0.05, 0.90, 0.05. H = −(2 × 0.05 log2 0.05 + 0.90 log2 0.90) = 0.432 + 0.137 = 0.57 bits. Matches the check.
3) Design B: 0.25, 0.50, 0.25. H = 0.5 + 0.5 + 0.5 = 1.50 bits. Matches the check.
4) Maximum log2 3 = 1.58 bits, reached only when each level has probability 1/3. Bins cannot be split, and the middle bin alone holds 0.50 > 1/3, so no grouping of whole bins can equalize the levels; 0.25 / 0.50 / 0.25 is the best possible.
5) In dim light the distribution of contrasts narrows (and receptor noise rises), so the matched curve should become steeper and centered on the new, narrower range: the bin boundaries move inward so each level is still used about equally. Brenner, Bialek, and de Ruyter van Steveninck found that H1's input-output curve stretched when motion became more variable and contracted when it calmed, keeping the full response range in use; information recovered within about a tenth of a second (Fairhall) (see "Matching the World's Statistics").
6) Grading guide. The matched design maximizes average information, so it gives most resolution to common small contrasts and lumps rare large ones into the top and bottom levels (here, bins 4 and 5 share a level, so a very large contrast is indistinguishable from a moderate one). If rare events matter most (a looming predator, a sudden shadow), information should be weighted by importance, not frequency; a predator detector might devote its range to large, rare, fast-changing signals (high threshold, steep response), accepting little information about common inputs. Strong answers name the objective (information versus expected value of action) and note that the brain has separate channels tuned to different goals.

## Lab 12.3 - A Predictive Map by Hand
1) With rightward-only movement, (T^k)(s, 4) = 1 when s + k = 4, so M(s, 4) = γ^(4 − s). γ = 0.5: 0.125, 0.25, 0.5, 1. Matches the check. (Treating position 4 as terminal; M(4, 4) = 1.)
2) Firing rises from position 1 to a peak at position 4 and is zero beyond it (no future visits). The field extends backward, toward positions from which 4 is reached, opposite the direction of travel (Figure 12.4, panel B).
3) γ = 0.9: 0.729, 0.81, 0.9, 1. Matches the check. The field becomes broader and extends farther backward. γ is the discount, the predictive horizon: how far into the future the map looks (an effective horizon of about 1 / (1 − γ) steps).
4) For a symmetric random walk on a long track, the field of a middle position is symmetric, because the position is equally likely to be reached from either side (Figure 12.4, panel A). On this short track the walls matter: with reflecting ends the computed field of position 2 is 0.39, 1.18, 0.32, 0.11 at positions 1 to 4 (γ = 0.5), slightly skewed toward the near end, since the end position can only move toward it. Accept "symmetric" with or without the boundary caveat.
5) M is learned incrementally (temporal-difference updates): at first each cell predicts only its own location; on each lap, arriving at position 4 just after being at position 3 raises M(3, 4), and on later laps the prediction propagates back to 2, then 1, so the field grows backward a little each lap until it converges near γ^(distance). This matches Mehta and colleagues' fields growing backward over the first laps (see "Prediction at Every Level").
6) Grading guide. Must include: the map encodes which states follow which, so for navigation it makes value easy to compute (value = M times reward; when rewards move, only the reward vector changes, which is why Momennejad found people adapt to changed rewards more readily than to changed sequences); for memory it captures the structure of sequences (Garvert's hidden sequence structure in hippocampus and entorhinal cortex) and supports anticipation and recall of what comes next; it unites the hippocampus's two roles as "two uses of one model of what follows what" (see "Prediction at Every Level"). Strong answers note its limit: a changed sequence requires relearning M, so people also plan deliberately.

## Lab 12.4 - Fixed and Adaptive Learning Rates
1) α = 0.2, estimates before each observation: 50, 50.00, 50.40, 49.92, 49.94, 57.95, 63.96, 69.57, 73.65, 77.12; final 79.50. Matches the check (49.94 before the 5th; final 79.50).
2) α = 0.8: 50, 50.00, 51.60, 48.72, 49.74, 81.95, 86.79, 90.96, 90.19, 90.84; final 89.37. Matches the check. Before the jump the low rate is better (it stays within 0.4 of 50 while α = 0.8 wanders by up to 1.6, chasing noise); after the jump the high rate is better (it reaches about 87 in two steps while α = 0.2 is still below 80 after six).
3) Adaptive rule. Errors and rates: obs 1 (error 0): α = 0.5, estimate 50.00; obs 2 (2): 0.33, 50.67; obs 3 (−2.67): 0.25, 50.00; obs 4 (0): 0.2, 50.00; obs 5 (error 40 > 20, reset): α = 1.0, estimate 90.00; obs 6 (−2): 0.5, 89.00; obs 7 (3): 0.33, 90.00; obs 8 (0): 0.25, 90.00; obs 9 (1): 0.2, 90.20; obs 10 (−1.2): 0.17, 90.00. Rates 0.5, 0.33, 0.25, 0.2, 1.0, 0.5, 0.33, 0.25, 0.2, 0.17; final 90.0. Matches the check.
4) Total squared error, Σ(estimate before − hidden mean)²: α = 0.2: 4,161.21; α = 0.8: 1,701.53; adaptive: 1,601.48. The adaptive learner wins. Note that about 1,600 of every total comes from the 5th observation (all three estimate about 50 when the mean is already 90, an unavoidable error); excluding it, the totals are 2,556.06 (α = 0.2), 80.97 (α = 0.8), and 1.49 (adaptive), so the difference is much larger than the raw totals suggest.
5) An outlier of 75 gives error 25 > 20, so n resets, α = 1, and the estimate jumps to 75; the next 50 gives error 25 again, another reset, and the estimate jumps back to 50 with n restarted. The learner treats the outlier as a change point, swings fully twice, and loses its accumulated certainty (computed sequence: 50, 50, 50, 50, 75, 50, 50, 50). Nassar's model avoids this because its rate is graded, not all or none: it estimates the probability that a change point occurred from how improbable the observation is given known observation noise and how often the mean jumps (the hazard rate), and blends that with its uncertainty about the current estimate (see "Many Errors, One Form", Figure 12.5 caption). A single moderately improbable observation yields a partial rate, and a return to the old values keeps the estimate near 50. Strong answers mention that distinguishing a lone outlier from a true change needs the next observation, so some models wait for confirmation.
6) Grading guide. Must include: Yu and Dayan's acetylcholine signals expected uncertainty (a noisy but stable world: keep the rate low and discount surprising single observations), and norepinephrine signals unexpected uncertainty (the world has changed: raise the rate and abandon the old estimate); the reset in step 3 is a crude norepinephrine-like signal, and the decaying 1/(n + 1) is the falling uncertainty as the new estimate is confirmed. Nassar's pupil measurements (pupil size reflecting arousal systems including noradrenergic ones) tracked the model's change-point probability and uncertainty and predicted each trial's learning rate (see "Many Errors, One Form"). Strong answers note pupil-linked arousal is not a pure norepinephrine measure, and mention Mathys's hierarchy that learns volatility itself.

## Lab 12.5 - Living Slightly in the Past
1) Distance = speed × delay.
   - 10 m/s: 0.66 m and 1.00 m
   - 30 m/s: 1.98 m and 3.00 m
   - 40 m/s: 2.64 m and 4.00 m
   Matches the check (and the chapter's "a ball traveling at 30 meters per second covers two meters").
2) Flight time = 20 / 40 = 0.50 s (assuming constant speed; real deliveries slow after the bounce, so slightly longer). 66 ms is 0.066 / 0.5 = 13 percent of the flight before V1 registers the release; 100 ms (percept usable for action) is 20 percent, during which the ball covers 4 m. Add the batter's movement time and much of the stroke must be committed on prediction, which is why batsmen jump their eyes to the predicted bounce point (Land and McLeod, see "Why Predict?").
3) When a brief flash appears exactly aligned with a moving object, observers see the moving object ahead of the flash. Explanation by extrapolation: the visual system projects the moving object's position forward by about the processing delay, so it is seen where it is now, while the unpredictable flash cannot be extrapolated and is seen where it was. The chapter notes that whether the effect reflects extrapolation or other mechanisms (for example differential latency or postdiction) is still argued over.
4) At three or four saccades a second, each fixation lasts roughly 250 to 330 ms; if the system waited for fresh retinal input (about 66 to 100 ms delay, plus the saccade itself) after each one, a third or more of each fixation, and so of the time, would pass without a usable, updated representation. Duhamel, Colby, and Goldberg found parietal neurons that shift their receptive fields before the eye moves, responding to the location the saccade will bring into their field, using the efference copy of the movement command; the map of space is updated from the commanded movement in advance, so it is ready when the eye lands (see "Why Predict?").
5) Grading guide. Misleading prediction: when motion changes abruptly or stops (a ball deflected off a bat edge, a car braking suddenly, a flash-lag-type misjudgment of an offside player), extrapolation places the object where it would have been. Dangerous lack of prediction: catching, batting, driving at speed, or stepping onto a moving escalator, where acting on a 100 ms old position means missing or colliding (at 30 m/s, 3 m of error). Strong answers balance the cost of occasional errors against the systematic error of always being late, and mention that prediction errors themselves are used to correct the model.

## Lab 12.6 - Surprise and the Dark Room
1) Surprise = −log2 p. Creature A: dark room −log2 0.9 = 0.15 bits; foraging −log2 0.1 = 3.32 bits. Creature B: dark room −log2 0.02 = 5.64 bits; foraging −log2 0.98 = 0.03 bits. Matches the check.
2) A seeks the dark room; B seeks foraging. No: surprise is defined relative to a creature's model, so a dark room is unsurprising only to a creature whose model expects to be there. For us, sitting in the dark and starving is improbable and so surprising (see "One Principle? The Free-Energy Principle", the reply of Friston, Thornton, and Clark).
3) Evolution (built-in priors: hunger, expectations of warmth, food, and company; compare the chicks' prior for biological motion); development (critical periods tune expectations to the early environment); learning (experience that foraging leads to food and that the dark room leads to hunger; reinforcement of expected states). Accept also culture or social learning.
4) The creature's goals must be written into its model as expectations about the states it will occupy, so the theory explains goal-directed behavior by assuming the goals; value is reintroduced as prior preferences rather than derived from the principle (see "One Principle? The Free-Energy Principle" and "What Prediction Leaves Out").
5) Grading guide. Must use Friston's statement that, like Hamilton's principle of stationary action, the principle "cannot be falsified", while process theories derived from it, such as predictive coding, "may or may not be supported by empirical evidence"; and at least one critic: Andrews (a modeling framework, not a hypothesis about the brain), Gershman (so flexible that almost any behavior can be described as minimizing free energy under some model), or Bruineberg and colleagues (the Markov blanket used in two senses). A strong answer concludes that the principle is a way of describing systems, and that what can be wrong is each process theory (predictive coding in cortex has a mixed record: Aitchison and Lengyel, Walsh, the mouse and monkey oddball preprint), and notes the direct tests (Isomura, Kagan) show description, not exclusion of rivals. Credit either verdict if argued from the distinction between principle and process theory.

## Lab 12.7 - Prediction Across the Book (concept map)
1) Six rows of Figure 12.1 (from the chapter's "A Model in the Head"): dopamine reward prediction (Chapter 3); hippocampal replay and expectations of where the animal will go (Chapters 5 and 10); sensory cortex predictions down, errors up (Chapter 6); regulation of the body by anticipating needs (Chapter 7); choices weighed by predicted outcomes and confidence (Chapter 8); movement compared with predicted consequences, cerebellum and climbing fibers (Chapter 9). Added rows from this chapter: retinal surround (predictive coding from neighbors and recent past); fly contrast matching and H1 rescaling; thirst neurons silenced at drinking; successor representation and place fields; visuomotor mismatch in mouse V1; the N400; parietal receptive-field shifts before saccades; Nassar's adaptive learning rate; sea legs.
2) What sets the learning rate (where known): dopamine: uncertainty and volatility, possibly acetylcholine and norepinephrine (Yu and Dayan; Behrens's anterior cingulate); sensory adaptation: the variance of recent input (H1, rescaling within about 100 ms); human estimation: change-point probability and uncertainty, tracked by pupil-linked arousal (Nassar); motor adaptation: fast and slow processes with different rates, inferred disturbance durations (Kording, Tenenbaum, Shadmehr); place fields and visuomotor mismatch: experience, rate largely unknown; N400 and language: unknown; body regulation: largely unknown. Credit "unknown" where the chapter gives no answer.
3) Timescales (Figure 12.6): sensory rescaling, milliseconds to a minute; short-term synaptic plasticity, moment to moment; dark adaptation, half an hour; motor adaptation, minutes (fast) to days (slow); sea legs, hours; long-term plasticity, hours to years; synaptic scaling, a day or two; critical periods, development; built-in priors such as light from above and biological motion, evolution.
4) Acceptable examples: what to want (value anchored to a body, not derived from prediction); why to explore (Stahl and Feigenson's infants; curiosity as learning progress; expected free energy's epistemic term assumed rather than derived, per Millidge); control loops as the evolutionary foundation (Cisek); the brain's particular form (spikes, hierarchy, fast and slow memories, energy budget), left for Chapter 13.
5) Grading guide. A strong answer takes a position close to the chapter's ("something in between": a general strategy of predict, compare, and revise with confidence matched to reliability, implemented by many distinct mechanisms, so more than a family resemblance but not one mechanism or one equation; see "The Central Lesson") or argues another view well. It must defend it with two concrete examples, for instance: the shared delta-rule form with an uncertainty-set learning rate across dopamine, motor, and human estimation (supports a principle); versus the different anatomy, speed, and meaning of dopamine's broadcast scalar, cortex's feature-by-feature errors, and climbing fibers' targeted errors (supports a family). It should address the free-energy principle's unfalsifiability and what prediction leaves out. Common mistakes: treating the free-energy principle as established fact; treating "prediction error" as a single signal.

### Notes for instructors
- Minor note (not an error): in Lab 12.4 step 4, about 1,600 of each learner's squared error comes from the jump trial that no learner can anticipate; instructors may want students to report totals with and without it.

# Chapter 13: Why the Brain Works the Way It Does: Constraints, Trade-offs, and the Shape of a Solution

## Lab 13.1 - The Price of a Bit

1) With r = 0.05 (energy per bin = 0.05 + p):

| p | H(p) (bits) | Energy | Bits per unit energy |
|---|---|---|---|
| 0.5 | 1.00 | 0.55 | 1.82 |
| 0.2 | 0.72 | 0.25 | 2.89 |
| 0.1 | 0.47 | 0.15 | 3.13 |
| 0.05 | 0.29 | 0.10 | 2.86 |
| 0.02 | 0.14 | 0.07 | 2.02 |

All printed check values are correct.

2) Most information per bin: p = 0.5 (H = 1 bit, each bin maximally unpredictable). Most per unit energy: p = 0.1 among the tabulated values; a fine search puts the continuous optimum at p ≈ 0.103 (3.13 bits per unit energy).

3) Rate = p / 0.0025 s: 200, 80, 40, 20, and 8 spikes per second. The efficient choice (p = 0.1) is 40 spikes per second, against 200 for maximum information.

4) With r = 0.01: energies 0.51, 0.21, 0.11, 0.06, 0.03; bits per unit energy 1.96, 3.44, 4.26, 4.77, 4.72. Among the tabulated values the best is now p = 0.05 (20 spikes per second); the continuous optimum is p ≈ 0.033 (about 13 spikes per second, 4.87 bits per unit energy). The best p moves down: when resting is cheap relative to a spike, the fixed cost no longer dominates the denominator, so each extra spike's cost weighs more against the slowly rising information, and silence becomes the better bargain (the dots in Figure 13.2B).

5) Model answer (see "The Price of a Bit" and "Why Spikes"). Key points:
- The model treats each bin as an independent binary symbol; real spike trains carry information in precise timing, in patterns across bins, and in populations, so H(p) per bin is only a rough proxy.
- Energy is counted only for the sender's spike and a flat rest cost; it omits synaptic transmission and the receiving cell's costs (which dominate the brain's budget and make each spike dearer, pushing the optimum lower), plus the costs of maintaining structure.
- Noise is ignored: the capacity of a noisy channel is less than H(p), and Laughlin's diminishing returns (information grows as the log of signal-to-noise ratio) are absent.
- The value of r is a free parameter, and the optimum moves with it, so the model gives an order of magnitude, not a number.
- Still informative: the qualitative result is robust. Whenever spikes cost much more than rest, bits per unit energy peak far below p = 0.5, which is why Levy and Baxter's estimate (0.025 to 0.05 per 2.5 ms bin, about 10 to 20 spikes per second) lands near observed average cortical rates, and why sparse firing and synaptic failures can be read as efficiency rather than deficiency. Harris et al. found real thalamic synapses tuned for bits per ATP, independent support.
- Strong answers note which way each omission moves the optimum; common mistakes are claiming the model "proves" neurons fire at 10 to 20 Hz, or confusing information per bin with information per spike.

## Lab 13.2 - Speed Costs Space

1) Bare: d = (v / 0.97)²; myelinated: d = v / 6.
- 1 m/s: bare 1.06 µm; myelinated 0.17 µm.
- 10 m/s: bare 106.28 µm; myelinated 1.67 µm.
- 50 m/s: bare 2,657 µm with the given coefficient 0.97; myelinated 8.33 µm. Matches the check.
- Why the 1 m/s value matters: 0.17 µm is far below the roughly 1 µm lower limit of Hursh's rule. Very thin fibers are generally not myelinated at all (below about 0.2 to 1 µm, unmyelinated conduction is as fast or faster and myelin's overhead is not worth it), so the area comparison at 1 m/s is an extrapolation and overstates myelin's advantage.

2) Area ratio = (d_bare / d_myel)²: 1 m/s: 40.7 (about 40); 10 m/s: 4,067 (about 4,000); 50 m/s: 101,661 (about 100,000). The ratio grows as v², because bare diameter scales as v² and myelinated as v.

3) Distance 0.1 m.
- 1 µm myelinated: 6 m/s, delay 16.67 ms.
- 0.5 µm bare: v = 0.97 × √0.5 = 0.69 m/s, delay 145.8 ms (about 146 ms).
- 0.2 µm bare: v = 0.43 m/s, delay 230.5 ms (about 230 ms).
(The bare values are lower-bound illustrations; most callosal fibers below 1 µm are in fact thinly myelinated or unmyelinated, and the rule is outside its range here.)

4) Ten one-way crossings: 10 × 16.67 = 166.67 ms (about 167 ms, matching the check), about 83 percent of a 200 ms syllable. The cross-hemisphere traffic alone would consume most of the time available, before any computation in either hemisphere is counted. With the thin fibers of step 3, a single crossing nearly uses up the syllable.

5) Model answer (see "Speed Costs Space"):
- Ringo et al. argued that the average callosal fiber in a human takes more than 25 ms to cross, so computations requiring many interhemispheric exchanges are too slow; large brains should therefore keep time-critical processing (such as rapid speech-sound analysis) within one hemisphere.
- The calculation supports the logic: delay scales with distance divided by speed, distance grows with brain size, and speeding up the many thin fibers would cost enormous volume (Zhang and Sejnowski's white-matter scaling; Wang et al.'s "few fast lines, many slow ones").
- It is a conjecture: the delay argument shows specialization is predicted, not that delay caused it.
- Tests: comparative data showing that lateralization of time-critical functions increases with brain size (or with callosal conduction delay) across species; within humans, relating individual callosal fiber diameters or measured interhemispheric transfer times to the degree of lateralization; developmental or lesion cases (for example callosal agenesis) where predicted processing shifts can be checked; small-brained species that should show less obligatory lateralization.
- Common mistakes: treating the hemispheres as fully independent, or forgetting that a few large fast fibers exist (the argument concerns the bulk of fibers and their bandwidth).

## Lab 13.3 - Short Wires or Short Paths

Computed by breadth-first search over all 28 pairs.

1) Chain: wire 7; total path 84, average 3.00; longest 7. Matches.

2) Add 0 to 7 (a ring): wire 14; total path 64, average 2.29; longest 4. Matches.

3) Add 2 to 5: wire 10; total path 66, average 2.36; longest 5. Matches.

4) Add 0 to 4 and 3 to 7: wire 15; total path 55, average 1.96; longest 4. Matches.

5) Points (wire, average path): chain (7, 3.00), 2 to 5 (10, 2.36), 0 to 7 (14, 2.29), two links (15, 1.96). All four are on the front: as wire increases, average path strictly decreases, so no design is beaten on both counts. The front is steep at first (three extra units of wire buy a 0.64 drop) and then flat (four more units buy only 0.07), and then steep again for the two-link design, which shows that where long links are placed matters as much as how many there are.

6) Model answer (see "Placing the Parts" and "Many Jobs at Once"):
- If wire is very expensive: the chain (or 2 to 5, which buys most of the path reduction for three extra units of wire).
- If speed matters most: the two-link design (shortest average path, 1.96, and longest path 4).
- The 2 to 5 link gives most of the benefit of a long-range link at modest cost, the "steep part of the curve" in Figure 13.4 where small-world networks sit; Kaiser and Hilgetag found real brains pay for some extra wire to keep paths short.
- Hubs (Chapter 4): long links that pass through a few central nodes shorten paths economically, but they concentrate traffic, so damage to them does disproportionate harm. In the two-link design, nodes 3 and 4 become critical intermediaries.
- Csete and Doyle's "robust yet fragile": a design optimized for efficient communication is robust to random loss of peripheral nodes but fragile to targeted loss of its shortcuts or hubs; robustness in one respect is paid for with fragility in another.
- Strong answers tie the choice to the weighting of goals (a Pareto front has no single best point); weak answers just pick the lowest number.

## Lab 13.4 - The Genome Bottleneck

1) Human: genome capacity 2 × 3.1 × 10^9 = 6.2 × 10^9 bits. Bits per connection log2(10^11) = 36.54. List = 10^14 × 36.54 = 3.65 × 10^15 bits (about 3.7 × 10^15). Ratio list / genome = 589,374, about 590,000. Matches.

2) Worm: log2(302) = 8.24 bits per synapse. Genome 2.0 × 10^8 bits; list 7,000 × 8.24 = 5.77 × 10^4 bits. Genome / list = 3,468, about 3,500. Matches.

3) Insect: log2(10^5) = 16.61 bits per synapse. List 10^7 × 16.61 = 1.66 × 10^8 bits; genome 2 × 1.4 × 10^8 = 2.8 × 10^8 bits. List / genome = 0.59, about 60 percent. Matches (the check gives genome first, then list, as in steps 1 and 2).

4) Two percent of the human genome: 0.02 × 6.2 × 10^9 = 1.24 × 10^8 bits. The list is now 2.95 × 10^7 times larger (about 30 million times, using the unrounded 3.65 × 10^15). The conclusion does not change; it is strengthened by a factor of 50. (Students may note that regulatory DNA outside coding regions also carries developmental information, so the true usable capacity lies somewhere between the two figures, and either way falls short by orders of magnitude.)

5) Model answer (see "The Bottleneck of the Genome"):
- It is an upper bound on what a wiring list would require, not on what development needs, because a list naming every target is the least compressed possible description; the brain's wiring is highly regular and can be generated by rules.
- The genome encodes rules: which cell types to make, how they migrate, which molecular gradients axons follow, which learning rules synapses obey.
- Information the genome does not supply comes from self-organization (Chapter 0: activity-dependent and physical processes, such as cortical folding from a growing sheet), from the developing body and environment, and from experience and learning (sensitive periods, Chapter 1).
- Hence learning is not optional for a large brain: it is the only way a brain of this size can be finished.
- Bonus points: the bottleneck may act as a useful inductive bias, forcing the genome to store what generalizes (Shuvaev et al. 2024). Common mistakes: concluding that the worm must therefore be fully genetically specified (the calculation shows only that it could be), or treating the genome's 1 GB as the brain's total information content.

## Lab 13.5 - Finding a Pareto Front

1) Front: A, B, D, E, F, H. Matches.

2) C (4, 65) is beaten by B (3, 70): cheaper and more informative. G (7, 90) is beaten by D (5, 95) and by E (6, 100): both cheaper and more informative.

3) Bits per unit energy: A 20.00, B 23.33, C 16.25, D 19.00, E 16.67, F 13.00, G 12.86, H 10.60. Best: B at 23.33. Matches.

4) Score = information − w × energy.
- w = 1.5: F = 92 (E and H 91, D 87.5). Matches.
- w = 10: D = 45 (B and E 40). Matches.
- w = 25: B = −5 (A −10). Matches.
As w rises the best design slides down the front from the expensive, informative end toward the cheap end (H below w = 1, F from 1 to 2, E at w from 2 to 4, D at 5 to 14, B at 15 to 29, A at 30 and above, with ties at the boundaries).

5) Model answer (see "Many Jobs at Once" and "The Price of a Bit"):
- "Most efficient" (maximum bits per unit energy) is one point, B, chosen by a ratio that ignores absolute need; an animal may need more information than B gives (to catch fast prey or avoid predators) and be willing to pay more per bit.
- The "best" design maximizes the organism's actual payoff, which depends on how it trades the two goals (w); different w select different points on the front, and every front point is best for some range of weights.
- Off-front designs (C, G) are never best for any positive w.
- What sets w: food scarcity and metabolic budget (cavefish: scarce food raises w), body size, lifestyle (fast-flying blowfly versus slow fruit fly, Niven et al.), predation pressure, and the value of fast or precise behavior. W can change within a life, which is one role of neuromodulators moving the brain along fronts.
- Common mistakes: equating efficiency with fitness, or treating the front as a single optimum.

## Lab 13.6 - Paying for a Brain

1) 86 × 6 = 516 kcal a day; 516 × 4,184 J / 86,400 s = 24.99 W, about 25 W. Matches. It exceeds Chapter 1's round 20 watts because the two figures come from different methods of estimation (a per-neuron cost scaled up from rodents and primates versus a whole-brain share of resting metabolism), and the per-neuron rate is itself an approximation; the discrepancy of about a quarter is within the uncertainty of either method. Credit any answer that names a difference in method or an uncertainty in the per-neuron rate.

2) 0.66 × 1,000 = 660 kcal; 0.43 × 1,500 = 645 kcal. Matches. These are glucose-uptake equivalents, not energy use: some glucose is used for biosynthesis (building lipids, nucleotides, and amino acids for a growing brain) or metabolized nonoxidatively rather than burned, and the brain also uses other fuels (lactate, ketone bodies), so uptake is an imperfect proxy for energy expenditure. The two estimates also rest on different denominators and assumed metabolic rates, so they need not agree exactly.

3) The child's roughly 650 to 660 kcal exceeds the adult's 516 kcal in absolute terms (about 1.25 to 1.28 times), in a body a fraction of the size, so as a share of the budget the brain is far more expensive in early childhood (about two-thirds of resting metabolism) than in adulthood. The brain is costliest around age four to five, coinciding with the slowest body growth (Kuzawa et al.), consistent with a trade-off between brain and body growth (see "How Big a Brain").

4) 30 × 6 = 180 kcal a day. The human brain costs 336 kcal a day more, about 2.87 times as much, the same as the ratio of neuron counts since the cost per neuron is assumed constant.

5) Grading guide (see "How Big a Brain"). A strong answer covers all four routes and the evidence:
- Cutting other organs (Aiello and Wheeler's expensive-tissue hypothesis): not supported across 100 mammals (Navarrete et al. 2011), who found no brain-gut trade-off.
- Storing less fat: larger-brained mammals do tend to store less fat (Navarrete et al.), but humans are an exception, carrying more fat as a buffer.
- Raising total metabolism: favored for humans; Pontzer et al. (2016) found humans burn about 400 kcal a day more than chimpanzees and bonobos after size and activity, partly through higher basal metabolism.
- Slowing growth: supported by Kuzawa et al.; the brain's peak demand coincides with the slowest body growth, so a long childhood helps pay for the brain.
- Also credit discussion of diet quality (cooking hypothesis, Fonseca-Azevedo and Herculano-Houzel, contested by Cornélio et al.) and the open obstetric-versus-metabolic debate on birth timing.
- Conclusion: for humans the evidence favors a raised overall budget plus fat reserves and slow growth, not gut reduction. Common mistakes: presenting the expensive-tissue hypothesis as established, or treating the cooking hypothesis as settled.

## Lab 13.7 - Constraint or History? (concept map)

1-3) Required nodes and expected classifications (students may choose other features; check that each is justified):

| Feature | Constraint(s) (Figure 13.1) or history | Convergence known? |
|---|---|---|
| Sparse firing | Energy (Levy and Baxter; Harris et al.) | Yes, in a sense: insects and vertebrates; also mixtures of experts in AI (DeepSeek-V3) |
| Spikes | Noise over distance; energy (Sarpeshkar) | Yes: long-range spiking across vertebrates, arthropods, cephalopods; graded signals in short neurons (photoreceptors, *C. elegans*) |
| Myelin | Space and wire; time; energy | Yes: myelin-like sheaths evolved independently in some invertebrates (for example copepods, annelids, prawns, per Hartline and Colman's review); credit if cited from that review |
| Small-world wiring | Space and wire versus time (short paths) | Yes: worm and macaque both pay for long links (Kaiser and Hilgetag) |
| Cortical folding | Space; physics of a growing sheet | Physical rather than lineage-specific: occurs across large-brained mammals, predicted by surface area and thickness (Mota and Herculano-Houzel) |
| Two memory systems | Statistical constraint of learning (stability versus plasticity) | Partly: AI's complementary-learning and replay systems; credit if student notes this is a convergence in machines |
| Basal ganglia loop | Mainly history (persistence since the lamprey, about 560 million years) | No independent origin cited; this is persistence, not convergence |
| Inverted retina | Mainly history (possible energy and pigment-supply argument, Baden and Nilsson) | Contrast case: the octopus evolved a non-inverted eye |
| Sensitive periods | Genome capacity (rules then learning) | Common across vertebrates and birds (song learning); credit with justification |
| Dopamine prediction errors | Many tasks at once; learning from errors under a fixed budget | Convergence with temporal-difference learning in AI; reward-prediction signals in insects (credit if justified) |

4) Map links: each feature to its constraint node(s), plus a "history" node feeding all features. Trade-offs from Figure 13.7 to mark: information versus energy (sparse firing, synaptic failures); short paths versus short wires (small-world wiring, hubs, myelin); holding versus changing (two memory systems, sensitive periods); exploit versus explore and flexibility versus economy (basal ganglia, dopamine); speed versus accuracy (basal ganglia selection); expectation versus input and sensitivity versus range (retina, perception). Links should be labeled ("explained by," "trades against," "inherited from").

5) Grading guide (see "Different Histories, Same Answers" and "Trade-offs That Cannot Be Escaped"):
- Strongest constraint example: typically sparse firing or spikes (quantitative energy and noise arguments plus experiment, Harris et al.) or bird pallium circuits (convergent cortex-like circuits from different starting material, Stacho et al.; Rueda-Alaña et al.). The best answers use convergence as the evidence.
- Strongest history example: the inverted retina (octopus comparison, blind spot, compensating Müller cells) or the conserved basal ganglia.
- Evidence that would change the mind: for the retina, a demonstrated functional advantage (energy supply to photoreceptors) that outweighs its costs; for basal ganglia, an independent origin of similar selection circuits in an unrelated lineage, which would point to constraint rather than history; for sparse firing, finding that efficiency does not predict firing rates across cell types or species.
- Common mistakes: treating "conserved" as meaning "optimal"; treating a feature as either constraint or history when most features show both (Figure 13.1 says history sets the starting material for all).

### Notes for instructors

None beyond the answers above.

# Chapter 14: Implications for Learning, Work, and Technology: What the Brain's Design Asks of the World We Have Built

## Lab 14.1 - Choosing a Spacing Gap

S0 = 2, so R(t, S0) = 1 / (1 + t / 18). If the review fails, retention at the test is R(35, 2) = 0.34.

| Gap g (days) | R at review | S2 (days) | R(35, S2) | Expected retention |
|---|---|---|---|---|
| 0 | 1.00 | 2.00 | 0.34 | 0.34 |
| 2 | 0.90 | 5.94 | 0.60 | 0.58 |
| 7 | 0.72 | 18.52 | 0.83 | 0.69 |
| 30 | 0.375 | 91.46 | 0.96 | 0.57 |

1) R = 1.00, 0.90, 0.72, 0.375. The 30-day value is exactly 18/48 = 0.375, printed as 0.375 in the check.

2) S2 = 2.00, 5.94, 18.52, 91.46. Matches.

3) R(35, S2) = 0.34, 0.60, 0.83, 0.96. Matches.

4) Expected retention = 0.34, 0.58, 0.69, 0.57. Matches. Best of these: the 7-day gap. A fine search puts the model's optimum at about 7.5 days (expected retention 0.69), about 21 percent of the 35-day interval, inside Cepeda's 20 to 40 percent band for short intervals.

5) One year: 5 to 10 percent of 365 = 18.25 to 36.5 days (about 18 to 36 days). One week: 20 to 40 percent of 7 = 1.4 to 2.8 days. Matches.

6) Model answer (see "Learning That Lasts"):
- At the longest gap a successful review is hugely beneficial (S2 = 91.46, retention 0.96), but the chance of success has fallen to 0.375, and a failed review leaves the memory at S0 with no gain; the expected value is dominated by the 62.5 percent of failures.
- The optimum balances the benefit of a harder retrieval (more forgotten, bigger boost, like a larger prediction error) against the risk that retrieval fails entirely.
- What a real course changes: failed reviews are usually followed by feedback, so the item is relearned rather than left at S0 (this moves the optimum later); multiple reviews rather than one; items differ in difficulty and students differ in prior knowledge; material is interrelated, and exams test understanding and transfer, not isolated facts; motivation and sleep vary; the model's parameters (the 9, the 4, the exponential boost) are illustrative, and the chapter notes the model's curve is flatter than Cepeda's data.
- Common mistakes: concluding that longer is always better, or reading the model's numbers as empirical predictions.

## Lab 14.2 - How Big Are the Classroom Effects?

1) Chapter exams: 94 − 81 = 13 points; relative gain 13 / 81 = 16.05 percent. Semester exam: 79 − 67 = 12 points; 12 / 67 = 17.91 percent. Matches.

2) Interleaving: 61 − 38 = 23 points; ratio 61 / 38 = 1.61 (a relative gain of 60.5 percent). Matches.

3) Minimum overlap = 78 + 78 − 100 = 56 percent. The answer 56 is correct, but it is the minimum possible overlap regardless of how the two traits are related, with no assumption about how the groups are related (if they were independent the overlap would be 0.78 × 0.78 = 60.84 percent). Either way, most participants both did better with interleaving and believed blocking was as good or better: their judgment contradicted their own performance.

4) Model answer (see "Learning That Lasts" and "The Illusion of Fluency"):
- Classroom effects are smaller because of noise and dilution: varied materials, longer and less controlled delays, students who also study on their own (narrowing gaps), imperfect implementation by teachers, tests that sample broader content, and comparison conditions that already include some retrieval (Roediger's advantage over rereading faded by semester's end).
- Laboratory studies use simple materials, tight control, and immediate or fixed tests, which maximize effect size.
- Students keep weak techniques because rereading and blocked practice feel fluent, and fluency is mistaken for learning (Kornell and Bjork: 78 percent judged blocking as good or better); desirable difficulties feel ineffective while they work.
- Other reasons: immediate performance looks better under massed and blocked study, the benefits appear only at a delay, habit and convenience, and lack of instruction in how to study.
- Strong answers connect to the illusion of fluency; common mistakes are treating classroom and lab effect sizes as interchangeable.

## Lab 14.3 - Reading an Effect Size

1) Φ(0.04) = 51.60 percent; Φ(0.09) = 53.59; Φ(0.11) = 54.38; Φ(0.83) = 79.67; Φ(1.0) = 84.13. Matches (printed values to one decimal).

2) r = √0.004 = 0.0632, about 0.063. Matches.

3) Ranking (largest to smallest): d = 1.0 (benchmark), interleaved mathematics (0.83), growth mindset for lower achievers (0.11), Facebook deactivation (0.09), ego depletion (0.04); the technology-use correlation (r ≈ 0.063, roughly d ≈ 0.13 if converted, but an association, not an effect) belongs among the small effects.
- 1.0 and 0.83: large enough to matter for an individual (the average interleaver outscores about four in five blocked students).
- 0.11 and 0.09: too small to notice in one person, but meaningful for a population if cheap and scalable (a brief online mindset intervention, a policy affecting millions of users), and possibly larger in subgroups.
- 0.04 (ego depletion): neither; indistinguishable from zero in the registered replication.
- r = 0.063: matters for neither individual prediction nor, without causal evidence, for policy; at most a population-level signal.

4) Model answer (see "The Illusion of Fluency" and "Designed to Be Hard to Put Down"):
- A small average shift moves the whole distribution, so across millions of people it changes how many cross a threshold (for example a clinical cutoff for depression or a passing grade); the tails change proportionally more than the mean.
- Cheap interventions with small effects can be cost-effective at scale.
- An average can hide heterogeneity: a near-zero mean can combine a substantial effect in a subgroup (lower achievers for growth mindset; adolescent girls in the Twenge and Haidt argument) with no effect in others.
- Conversely, small effects are fragile: publication bias and analytic flexibility can produce them (Macnamara and Burgoyne), so small effects need large preregistered studies.
- Common mistakes: equating "statistically significant" with "large," or interpreting r² of 0.4 percent as proof of no effect.

## Lab 14.4 - The Cost of Switching

1) 20 switches × 8 hours × 1 s = 160 seconds, about 2.7 minutes. Matches.

2) 4 × 25 = 100 minutes. Matches.

3) The interruption figure (100 minutes) is about 37 times larger. But it is not time lost: Mark et al. found that most of the gap is spent on other tasks, and interrupted workers in the email study finished faster with no loss of quality. The chapter's evidence suggests the more important cost is stress, frustration, time pressure, and fragmentation (work repeatedly set down and picked up), not lost minutes; the switch cost itself is robust but tiny in minutes (see "Attention Is a Budget").

4) Grading guide: any two concrete changes that cut interruptions from four to two without cutting output, for example: batching email and messages into two fixed checking times; protected "focus blocks" with notifications off and status set to busy; consolidating meetings into one part of the day; routing non-urgent requests to an asynchronous queue or ticket system; office hours for colleagues' questions; a quiet room or closed door for deep work. Strong answers explain why the change reduces interruptions specifically (not just switches) and how the work still gets done (the interrupting requests are deferred, not dropped).

5) Model answer (see "Attention Is a Budget"):
- The switch cost (Rogers and Monsell; Monsell) is robust and replicable but small per switch.
- Dramatic claims (heavy media multitaskers are worse at filtering, Ophir et al.; a phone's mere presence drains capacity, Ward et al.) shrank or vanished in replications and meta-analyses.
- Real costs arise in specific settings: off-task laptop use cost 11 and 17 points (Sana et al.), and interruptions raise stress (Mark et al.).
- Policy implication: target specific, demonstrated costs (off-task screens in meetings and lectures, unnecessary notifications, constant interruption) rather than sweeping bans based on weak claims; protect blocks of uninterrupted time; measure stress as well as output; be skeptical of open-plan offices justified by assumed interaction gains (Bernstein and Turban found a 70 percent drop).
- Common mistakes: multiplying a 1 s cost into an exaggerated productivity loss, or citing nonreplicated studies as established.

## Lab 14.5 - Skill Under Automation

1) g = 0.1 × (1 − f); s* = g / (g + 0.004):
- f = 0: g = 0.1, s* = 0.96.
- f = 0.5: g = 0.05, s* = 0.93.
- f = 0.9: g = 0.01, s* = 0.71.
- f = 0.99: g = 0.001, s* = 0.20.
Matches. (The exact fixed point of the daily update, s* = g(0.996) / (1 − (1 − g)(0.996)), gives 0.9614, 0.9257, 0.7135, 0.1994, the same to two decimals.)

2) The curve is nearly flat up to about f = 0.8 (s* = 0.83) and drops steeply above f = 0.9: 0.71 at 0.9, 0.56 at 0.95, 0.43 at 0.97, 0.33 at 0.98, 0.20 at 0.99, and 0 at 1. The slope is steepest as f approaches 1 (about −25 per unit f at f = 1). Automating the first half of tasks barely matters; automating the last few percent destroys the skill.

3) s* = 0.9 ⇒ g = 0.9 × 0.004 / 0.1 = 0.036; f = 1 − 0.036 / 0.1 = 0.64. So at least 36 percent of cases must be done without AI. Matches. (Exact update: g = 0.0361, f = 0.639, same answer.)

4) Model answer (see "When the Machine Does the Work" and "Implications for Artificial Intelligence"):
- Bainbridge's final irony: the most successful automated systems, rarely needing manual intervention, may need the greatest investment in operator training. In the model, the more reliable the automation (f near 1), the lower the equilibrium skill, exactly when the rare hard case arrives.
- Air France 447: experienced pilots had little practice in manual high-altitude handling; when the autopilot disconnected they mishandled the aircraft, and the investigation cited the absence of training in manual handling at high altitude.
- The model makes the policy quantitative: keeping skill high requires deliberately handing a substantial share of routine work back to humans (here 36 percent) or substituting practice (simulators, as aviation does).
- Budzyń et al.: endoscopist detection without AI fell from 28.4 to 22.4 percent, observational and short but consistent with the model.
- Strong answers note the model's limits (one skill, linear gain, constant decay, no distinction between routine and hard cases, no learning from monitoring). Common mistakes: concluding automation should be avoided rather than managed.

## Lab 14.6 - Weighing a Study

1) Expected entries (from the chapter; for sample sizes the chapter does not give, accept values students find in the paper with a citation):

| Study | Sample | Random assignment | Control group | Timing of outcome | Replicated? |
|---|---|---|---|---|---|
| Kuhl, Tsao, and Liu (2003) | About a dozen infants per group, four groups | Yes (to Mandarin live, video, audio, or English) | Yes (English sessions) | Shortly after 12 sessions over four weeks | Not directly; conceptually supported (Roseberry et al. 2014; Lytle et al. 2018) |
| Dunster et al. (2018) | Students in one biology course at two schools, different cohorts before and after (chapter gives no n) | No | No (before-after, different students) | Spring before versus spring after the 2016 change | Not directly; consistent with the sleep biology |
| Budzyń et al. (2025) | Colonoscopies at four Polish centers by experienced endoscopists (chapter gives no n) | No (observational) | No concurrent control; before-after comparison | Three months before versus three months after AI introduction | No |
| Bastani et al. (2025) | About 1,000 Turkish high school students | Yes | Yes (no-AI group) | Exam after the practice sessions, without AI; no long-term retention | Not yet; Kestin et al. is related but different |

2) Suggested grades (accept a grade one step either way with good reasons):
- Kuhl: B. Randomized with a control and a striking contrast, but very small groups, an immediate outcome, and an attention confound (screen-watching infants attended less).
- Dunster: C. Sleep was measured objectively (actigraphy), a strength, but no control group and different students across years leave the grade gain open to cohort and teacher effects.
- Budzyń: C to D. Real-world clinical data, but observational, short, and vulnerable to other concurrent changes and regression; it shows association, not that AI exposure caused deskilling.
- Bastani: A to B+. Large randomized trial with a no-AI control and an unaided exam, but one country, one subject, a short horizon, and no replication.

3) Grading guide: the follow-up must target the named weakness. Examples: Kuhl, a larger preregistered replication with attention measured and equated (for example a responsive video call versus a matched recording); Dunster, a randomized or staggered rollout across schools (difference-in-differences) with a control district; Budzyń, a randomized trial assigning endoscopists to AI-assisted versus unassisted periods, or interrupted time series with concurrent control centers, measuring unaided detection over a longer period; Bastani, a delayed retention test months later and a replication in other subjects and countries. Common mistake: simply proposing "more participants" without addressing the design flaw.

4) Model answer: act now on Bastani (randomized, large, and aligns with the retrieval and effort evidence): restrict answer-giving AI in learning and use hint-giving tutors; the cost of acting is low. Later school start (Dunster) is defensible given converging sleep biology and measured sleep gains, though the grade effect is uncertain; a reasonable answer may support it as a low-regret policy. Budzyń warrants precautionary steps (keep some unaided practice, monitor detection rates) rather than a firm conclusion. Kuhl supports favoring responsive interaction for infants but is too small to drive policy alone. Strong answers weigh evidence quality against the cost and reversibility of acting, and use converging evidence (Chapters 5 and 9 mechanisms) rather than single studies.

## Lab 14.7 - The Evidence Ledger (concept map)

1-2) The claims in Figure 14.7, with mechanisms from Figure 14.2:

| Claim (Figure 14.7 tier) | Mechanism | Chapter |
|---|---|---|
| Retrieval practice (strong) | Retrieval and prediction error rewrite memories | 5, 12 |
| Spacing (strong) | Memories consolidate slowly, offline, in sleep; forgetting curve | 5 |
| Interleaving (strong) | Practice builds specific routines; discrimination through contrast | 9 |
| Cost of task switching (strong) | Attention and effort are limited and costly | 1, 8 |
| Later school start (supported, observational) | Sleep consolidation; adolescent circadian shift | 5 |
| Skill loss under automation (supported, observational) | Practice builds routines; disuse lets them fade | 9 |
| Small social-media effects on well-being (supported) | Reward learning shapes habits | 3, 8, 9 |
| Infants learning from responsive partners (supported, small studies) | Learning from other people | 14 |
| Growth mindset (small or disputed) | Beliefs and motivation | not a brain mechanism per se |
| Exercise and the hippocampus (small or disputed) | Plasticity: the brain reshapes itself around what it does | 1, 5, 9 |
| Satellite navigation and spatial memory (small or disputed) | Hippocampal plasticity with self-directed navigation | 1, 5, 9 |
| AI tutors that guide (early) | Retrieval, prediction error, effortful practice | 5, 9, 12 |
| A phone's presence; heavy media multitasking (small or disputed) | Limited attention | 1, 8 |
| Learning styles, transferable brain training, Mozart effect, longhand notes, willpower used up in minutes (not supported) | Sensory specialization; plasticity; arousal; attention; effort | various |

3) Mechanism solid, claim failed (the essential examples):
- Plasticity and brain training: the brain does change with practice, but practice builds the specific routine practiced (Chapter 9), so training games improve the games, not general cognition (Owen et al.; Simons et al.).
- Sensory specialization of cortex and learning styles: modality-specific areas exist, but no crossover interaction for matched instruction (Pashler et al.).
- Lateralization of particular functions and "left- or right-brained" people: functions lateralize, whole brains do not (Nielsen et al.).
- Effortful control has real costs (Chapter 8), but ego depletion failed registered replications (effect 0.04); only long-duration fatigue (Wiehler et al.) holds up, tentatively.
- Arousal improves performance briefly, but the Mozart effect is about 1.4 IQ points and not specific to Mozart.
The gap: a fact about mechanism does not fix the size, specificity, or transfer of a behavioral effect; that requires tests in people (Bruer's "bridge too far").

4) Grading guide: two outside claims placed in a tier with reasons tied to study design (randomization, control, sample size, replication, timing). Credit for correctly placing common examples (for example "we use only 10 percent of our brains," not supported; "blue light from phones ruins sleep," direction supported but ordinary-dose effects small, cf. Chang et al.). Penalize placement by plausibility alone.

5) Model answer: a school or company should require (a) randomized or well-controlled studies in people, not just a mechanism; (b) outcomes measured at a delay and in the real setting (classroom or workplace), on the outcome that matters, not on practice performance; (c) effect sizes with confidence intervals, judged against cost; (d) independent and preferably preregistered replication; (e) evidence that the effect transfers beyond the trained task; (f) no financial conflict, or scrutiny when there is one; (g) a plan to evaluate locally after adoption. Mechanistic plausibility is necessary background, never sufficient (see "What Does Not Follow" and the chapter's opening warnings). Strong answers use the chapter's cases (learning styles, brain training, Bastani) as examples; common mistakes are accepting "brain-based" claims because they cite neuroscience, or rejecting all practice that lacks a mechanism.

### Notes for instructors

None beyond the answers above.

# Chapter 15: A Coherent Model of the Human Brain: How the Pieces Fit

## Lab 15.1 - Placing Phenomena in the Model

1) Accept reasonable alternatives if justified; the expected placements (statement numbers as in "The Model in Eight Statements"):
   - Waterfall illusion (Chapter 12; also Chapter 13): statement 3 (adaptation to expected input; the aftereffect is the cost of a prediction-like recalibration), with statement 8 (a trade-off: sensitivity within a range bought at the cost of the absolute level) and statement 2 (efficient coding by costly parts).
   - Schultz's monkeys (Chapter 3; also 8, 10): statement 4 (dopamine as the third factor) and statement 3 (the error is a reward prediction error); statement 6 (value guiding choice).
   - Cavefish's lost eyes (Chapter 13): statement 2 (eyes and visual brain are energetically expensive) and statement 8 (an inherited plan revised by local trade-offs; eyes start to form and then degenerate).
   - Spaced study (Chapter 5 forgetting curve; Chapter 14 classroom evidence): statement 5 (several clocks; spacing and sleep favor slow consolidation).
   - Stale popcorn eaten by habit (Chapter 9): statement 6 (habit no longer consults value; context-bound).
   - London taxi drivers (Chapter 14): statement 7 (structure finished by experience) and statement 5 (long-term spatial memory); also "No Two Brains Alike."
   - Dopamine timing window in a single spine (Chapter 3): statement 4 (local activity plus a broadcast signal within a trace window).
   - Kuhl's infants learning from live speakers (Chapter 14): statement 7 (sensitive-period learning shaped by experience) and the social thread in "The Model in Eight Statements" (other people supply errors and value); a strong answer may add statement 4 (social contingency acting as a gating signal).
   - Synaptic failures (Chapter 1, Allen and Stevens; Chapter 2): statement 2 (poor parts; populations average over failures).
   - Return of extinguished fear (Chapter 7; Chapter 15): statement 5 (extinction is a second memory, not erasure) and statement 3 (latent-cause inference about context).
2) With the placements above, statements 2, 4, and 5 recur most (three to four mentions each); statement 1 (serves a body) appears least, often zero times, because none of these phenomena is primarily about regulating the body. Students should notice that the list under-samples Chapters 7 and 12's body and interoception material; any count is acceptable if consistent with the student's own table.
3) Best choices: Schultz's monkeys (statement 3 supplies the error, statement 4 says how the error is used: the prediction error is broadcast and gates synapses that carry a trace) or extinguished fear (statement 3 infers a new latent context, so statement 5 stores a second memory instead of overwriting; the inference decides which memory is retrieved). Credit answers that show causal interaction, not just co-occurrence.
4) Grading guide: a strong answer names a candidate (for example, individual uniqueness from "No Two Brains Alike," conscious experience from "What Is Settled and What Is Open," or social learning, which is a thread rather than a statement) and argues whether it is a gap, an emergent consequence, or outside the model's scope. It should state the implication: a phenomenon that fits nowhere means either a missing statement or a model that is incomplete or wrong in that area, and the chapter says a model is useful only if it could turn out to be wrong ("A Neuroscientist Studies a Microprocessor"). Common mistake: claiming everything fits, which makes the model unfalsifiable.

## Lab 15.2 - The Numbers of the Wiring Diagrams

1) Worm 7,000 / 302 = 23.18; fly 54,500,000 / 139,255 = 391.37; human sample 149,900,000 / 16,087 = 9,318.08; human neocortex 164 × 10^12 / 16.3 × 10^9 = 10,061.35. All match the checks. The sample figure is approximate because many synapses in the cubic millimeter are made by axons whose cell bodies lie outside it, while the neurons whose somata lie inside have dendrites and axons that leave the block; dividing all synapses in the volume by the contained neurons is therefore not a true per-neuron count (it is a synapse density expressed per local neuron).
2) Volume ratio 1.2 × 10^6 mm³ / 1 mm³ = 1.2 × 10^6; data 1.4 PB × 1.2 × 10^6 = 1.68 × 10^6 PB = 1.68 ZB (about 1.7 ZB). Matches the check. Assumption: imaging cost scales with volume and white matter needs the same resolution (it would move the estimate down if white matter could be imaged more coarsely).
3) Any three of (see "The Wiring Diagram Arrives" and "The Levels Talk to Each Other"): the neuromodulatory state that selects which circuits are active (Bargmann and Marder: each wiring diagram encodes many possible circuit outcomes); synaptic strengths and their dynamics (an electron micrograph gives existence and size, not efficacy, release probability, or plasticity state); the history of learning that set the connections; the body and its needs that gave that learning its purpose; activity and timing (who fires when); and, from Chapter 13's genome bottleneck, the rules that generated the wiring: the genome is more than half a million times too small to list the connections, so the map is the product of rules plus experience and one map does not reveal the rules or how another brain would differ ("No Two Brains Alike").
4) Grading guide: connectome-only questions include which neurons can possibly influence which (anatomical constraints, path existence, motifs, convergence and divergence, cell-type-specific wiring, ruling models out). Activity-only questions include what the circuit actually does in a given state, timing, neuromodulatory reconfiguration, and how computation changes with learning. Strong answers cite the MICrONS design (wiring and firing of the same neurons) as the way to combine them and mention the 6502 lesson. Common mistake: treating a connectome as a program that can be "run."

## Lab 15.3 - Timescales

1) From Figure 15.3: spikes and prediction errors, about 1 to 100 ms (Chapters 2, 6); dopamine within the eligibility trace, about 0.3 to 2 s (Chapter 3); cerebellar recalibration and early potentiation, about 1 minute to 1 hour (Chapters 5, 9); new proteins make changes last, about 1 to 3 hours (Chapter 5); sleep replay to the cortex, roughly 6 to 9 hours after the first attempt, the first night (Chapter 5); control shifts to habit and chunking, about 1 week to 2 months (Chapter 9); the old habit kept as a latent context and savings on relearning, about 3 months to 5 years (Chapters 7, 9, 12).
2) 365 × 86,400 s = 3.1536 × 10^7 s = 3.1536 × 10^10 ms; ratio about 3.15 × 10^10 (3.16 × 10^10 with 365.25 days). Matches the check. About ten and a half orders of magnitude.
3) Handoffs: spikes to dopamine window: coincident pre and post activity leaves an eligibility trace (molecular tag) that holds the record for about a second until the broadcast signal arrives; dopamine to early potentiation and cerebellar recalibration: the gated change becomes early LTP, and repeated error signals (climbing-fiber error in the cerebellum) accumulate small corrections over many trials; early potentiation to lasting change: synaptic tagging and capture, with gene expression and new protein synthesis consolidating the tagged synapses; protein stage to sleep: hippocampal traces are reactivated and replayed in compressed form during deep sleep, interleaved into cortex; sleep to habit: repeated practice over weeks shifts control from goal-directed to habit circuits (dorsomedial to dorsolateral striatum) and chunks movements; habit to latent context: context inference assigns the learning to a cause, keeping old and new learning separately so that the old can return and relearning shows savings.
4) Grading guide: best understood is plausibly the trace-to-dopamine handoff (single-spine window measured directly, Chapter 3) or protein-synthesis consolidation (decades of work, settled in Figure 15.5); least understood is plausibly what sleep does to synapses (open in "What Is Settled and What Is Open": downscaling versus strengthening unresolved) or the latent-cause handoff (a theory, Gershman, Blei, and Niv, with limited mechanism). Strong answers justify with the settled/probable/open grading and name the evidence type (direct measurement versus model).

## Lab 15.4 - The Three-Factor Window

1) e(0.5) = exp(−0.5) = 0.61; e(1) = exp(−1) = 0.37; e(3) = exp(−3) = 0.05. Matches the check.
2) No. A simple exponential is largest at t = 0, so it predicts maximal potentiation for immediate dopamine, not nothing before 0.3 s. The lower limit needs something else: a trace that rises before it falls (a delayed molecular cascade, for example calcium-triggered kinase activation that takes hundreds of milliseconds to build, a difference of exponentials or alpha-function trace); a requirement that the activity-driven calcium signal end before dopamine-triggered cAMP/PKA signaling can act (sequence detection); or slow dopamine receptor signaling itself. For the upper limit, e(2) = 0.14 shows the trace is small but not zero at 2 s, so a threshold on e(t) is also needed to explain "nothing" after 2 s.
3) Credited: synapses active within about the last 1 to 2 seconds before the relief (the steering and mirror-check decisions that made up the turn itself, plus the cue representations active then), weighted by e(t). Not credited directly: decisions made earlier (choosing the lane well before the roundabout, a correct glance several seconds before), whose traces have decayed (e(3) = 0.05); also synapses active after the relief do not get this credit. Some irrelevant synapses active in the window are credited too, which is why credit by a trace is noisy.
4) Grading guide: should mention temporal-difference learning (Chapter 3): dopamine moves back from the reward to the earliest reliable predictor, so each link in a chain needs credit only across a short gap, and learned values bridge long delays stepwise; replay (Chapter 5): sequences replayed in compressed form during rest and sleep, possibly in reverse, bring earlier events within a short window of the outcome; hippocampal episodic memory and working memory holding the relevant state; the hippocampal STDP-dopamine window being longer (Brzosko and colleagues, minutes in slices). Common mistake: proposing simply a longer τ, which would also credit more irrelevant synapses.

## Lab 15.5 - One Context or Two?

1) Natural logs. Old (p = 0.8): 3 ln 0.8 + 7 ln 0.2 = −0.67 − 11.27 = −11.94. New (p = 0.2): 3 ln 0.2 + 7 ln 0.8 = −4.83 − 1.56 = −6.39. Unknown (p = 0.5): 10 ln 0.5 = −6.93. Matches the check.
2) The new context is best supported. It beats the old context by −6.39 − (−11.94) = 5.55 log units (a likelihood ratio of about e^5.55 = 257). It beats the unknown context by only 0.55 (ratio about 1.7), so with equal priors the posteriors are about 0.63 new, 0.37 unknown, 0.002 old: ten trials rule out the old context but barely separate new from unknown.
3) If the learner attributes the failures to a new latent cause, it learns new values for that cause and leaves the values attached to the old cause untouched (no prediction errors were applied to them). On a visit home, the old context's cues (car layout, roads) are evidence for the old cause; the learner infers it, retrieves its values, and the old habit runs, as in the glance the wrong way at the first junction ("One Afternoon, Every Level").
4) 8 successes: old 8 ln 0.8 + 2 ln 0.2 = −1.79 − 3.22 = −5.00; new 8 ln 0.2 + 2 ln 0.8 = −12.88 − 0.45 = −13.32; unknown −6.93. The old context wins (by 1.93 over unknown, about a 6.9-fold likelihood ratio; posterior about 0.87 with equal priors). Matches the check.
5) Grading guide: renewal of extinguished fear (Chapter 7): extinction is learned as a new cause or second memory tied to the extinction context, so the original fear memory is intact and returns when the context shifts back or time passes ("When the Model Breaks"); savings (Chapter 9): when a perturbation returns, the learner recognizes the earlier cause and retrieves its stored adaptation, so relearning is faster than first learning. Strong answers note the calculation only compares likelihoods and needs priors (a sticky prior favoring the current context, or a prior on new causes) and a way to propose new causes; they also note the limitation that real contexts are not cleanly labeled and that ten trials is little evidence.

## Lab 15.6 - Settled or Open?

1) Any two settled (engram storage, reward prediction errors, fast and slow memory, energy constraint, adaptation at every level, neuromodulatory reconfiguration) and any two open (cortical credit assignment, single-neuron computation, sleep and synapses, glia, molecular storage, one principle).
2) Model pairs, from "What Is Settled and What Is Open" and earlier chapters:
   - Engrams: labeling, silencing, and reactivating specific cells suppresses or evokes a memory (Josselyn and Tonegawa review); limitation: almost entirely rodents and mostly fear learning.
   - Reward prediction errors: Schultz's recordings in monkeys matching temporal-difference errors (Chapter 3); limitation: dopamine also carries other signals (movement, salience; widespread movement signals in the International Brain Laboratory recordings), so it is not only a reward error.
   - Fast and slow memory: hippocampal damage spares older and cortical memory, plus the catastrophic-interference argument of McClelland, McNaughton, and O'Reilly; limitation: the degree and timing of hippocampal independence for old memories is debated.
   - Neuromodulatory reconfiguration: Marder's stomatogastric circuit; limitation: shown mainly in small invertebrate circuits.
   - Credit assignment: theoretical proposals (Lillicrap and colleagues; Payeur and colleagues' bursts and dendritic compartments); limitation: simulations only, no experiment shows the cortex doing it.
   - Dendritic computation: Gidon and colleagues' dendritic calcium spikes suggesting XOR; limitation: not independently replicated and partly inferred from modeling; layer 5 human dendrites more isolated (Beaulieu-Laroche).
   - Sleep: synapses about 18 percent smaller after sleep (de Vivo and colleagues); limitation: other work shows sleep building specific synapses (Yang and colleagues).
   - Glia: astrocyte activation induces potentiation (Adamsky and colleagues); limitation: other labs found no effect (Agulhon and colleagues).
   - Molecular storage: Langille and Gallistel's argument; limitation: a minority view resting on reinterpretation, little direct evidence.
3) Grading guide: the design must have a manipulation, a control, a measurement, and stated outcomes in both directions. Example (sleep): induce learning of a specific task, then compare sleep versus matched sleep deprivation, imaging the same identified spines (two-photon, longitudinal) in task-engaged and non-engaged dendrites; "both" view supported if task-tagged spines grow while the untagged majority shrink; a uniform shrinkage would favor downscaling only, and no difference would weaken both. Example (credit assignment): optogenetically block apical-dendrite feedback or bursts in a defined layer during learning, with a sham control; specific loss of learning, not performance, would move it toward probable. Common mistakes: no control, no prediction for the opposite result, or an experiment that cannot distinguish rival hypotheses.
4) Grading guide: settled claims have converging evidence from several methods and laboratories, causal manipulation (not just correlation), replication, and often several species; open claims rest on a single method, theory or simulation, unreplicated findings, or conflicting results from different labs. Strong answers note that even settled claims carry limits (rodent fear learning; small circuits), and that the groupings are the author's judgment (Figure 15.5 caption).

## Lab 15.7 - The Book in One Map (concept map)

1) Nodes: Chapter 0 (physical and chemical basis), 1 (what the brain is), 2 (neurons), 3 (neuromodulation), 4 (circuits), 5 (plasticity and memory), 6 (perception as inference), 7 (emotion and the body), 8 (decision-making), 9 (habits and skills), 10 (what AI gets right and wrong), 11 (brain mechanisms in AI), 12 (prediction and adaptation), 13 (constraints and trade-offs), 14 (implications for learning, work, technology).
2) Key labeled links (a complete map has many more; check that labels name mechanisms): 0 → 2 (ion gradients, membranes, energy); 2 → 4 (spikes and synaptic transmission build circuits); 2 → 5 (NMDA coincidence detection, back-propagating spike); 3 → 5 (dopamine as third factor, eligibility trace); 4 → 5 (inhibition and homeostasis keep plasticity stable); 5 → 9 (consolidation; practice to habit); 3 → 8 (reward prediction error drives choice); 7 → 8 (body state sets value); 8 → 9 (repeated choices become habits); 5 → 6 (learned priors); 6 → 12 (perception as inference generalized to prediction); 3 → 12 (prediction error); 1 → 13 and 2 → 13 (energy and noise costs); 13 → 6 (efficient coding, adaptation); 5 → 10 and 3 → 10 (backpropagation vs local rules; catastrophic forgetting); 10 → 11 (what machines lack); 5 → 14 and 9 → 14 (spacing, testing, habits in daily life); 7 → 14 (stress, attention).
3) Regions (from Figure 15.2): statement 1 over Chapters 1, 7, 12; statement 2 over 0, 1, 2, 13; statement 3 over 3, 6, 7, 8, 12 (plus 9 in the notes); statement 4 over 2, 3, 5, 10, 11; statement 5 over 1, 5, 9 to 12, 14; statement 6 over 3, 4, 7, 8, 9, 14; statement 7 over 0, 1, 6, 10, 13; statement 8 over 1, 3, 4, 13. Regions must overlap; no statement rests on one chapter.
4) Strong candidates: Chapter 3 (dopamine, prediction errors, three-factor rule, temporal difference; it feeds statements 3, 4, 6, 8 and the driving example) or Chapter 5 (memory systems, plasticity, replay; feeds statements 4 and 5 and most of Chapters 9 to 14). Chapter 2 is defensible as the foundation. Grade on the justification: count of outgoing links and statements that would lose support.
5) Grading guide: a strong answer (8 to 12 sentences) touches the central lesson ("The Central Lesson"): the brain changes its own structure in a body under constraint; predictions and errors; local plasticity kept by broadcast signals; fast and slow memory linked by sleep; choices cached as habits; slow, noisy, costly parts; genome supplies rules, experience finishes; the result is a unique record of a life. Common mistakes: a list of mechanisms without how they connect, or omitting the body and constraints.

### Notes for instructors
- Minor note for instructors (not an error in a check value): in Lab 15.1, "spaced study" is treated mainly in Chapters 5 and 14, and the "waterfall illusion" is introduced in Chapter 12 and revisited in Chapter 13; students may cite either.

# Chapter 16: NIMCP: Building a Brain from the Book's Principles

## Lab 16.1 - An Eligibility Trace by Hand

1) Trace with τ = 8 over active steps 0, 1, 2. d = 2: e^0 + e^(−1/8) + e^(−2/8) = 1 + 0.88 + 0.78 = 2.66. d = 5: e^(−3/8) + e^(−4/8) + e^(−5/8) = 0.69 + 0.61 + 0.54 = 1.83. d = 10: e^(−8/8) + e^(−9/8) + e^(−10/8) = 0.37 + 0.32 + 0.29 = 0.98. Matches the check.
2) d = 2: the cue synapse is active at the reward step, so it is credited (one unit, the same credit any randomly active background synapse gets at that step). d = 5 and d = 10: the cue is silent, so the coincidence rule gives it nothing; whatever background synapses happen to be active then get the credit. Matches the check.
3) Expected background trace = 0.05 × Σ e^(−k/8) over past steps k. With the background starting at step 0, as the lab states, the finite series over k = 0 to d gives 0.13 (d = 2), 0.22 (d = 5), and 0.32 (d = 10), matching the check, so the cue's trace exceeds it by factors of 20.0, 8.15, and 3.08. (The chapter's "about 20," "nine," and "four" come from a simulation in which the cue synapse also fires at random after the cue ends, which raises its trace at d = 10 to about 1.25 and the ratio to about 3.9.) A student who assumes an infinite history gets a steady 0.05 / (1 − e^(−1/8)) = 0.05 / 0.1175 = 0.43 and ratios of 6.25, 4.30, and 2.30; accept this with the assumption stated, but note that the lab specifies the start at step 0. Either way: the trace keeps the right synapse ahead, but the margin shrinks as delay grows because the cue's trace decays while background traces build toward a steady level.
4) Grading guide: the best τ is set by the delays between cause and reward that the task presents (roughly matched to, or slightly longer than, the typical delay) and by the background firing rate; a strong answer frames it as a trade-off. If τ is much longer than the delays, the cue's trace still captures the reward, but every background synapse also accumulates a large trace (steady level 0.05 / (1 − e^(−1/τ)), roughly 0.05τ), so selectivity falls; credit smears across many irrelevant synapses and learning becomes slow and noisy. Too short a τ loses the cue entirely (the coincidence-rule limit). Strong answers mention Chapter 3's measured window of 0.3 to 2 s, temporal-difference learning and replay as ways to bridge longer delays, and possibly that biology may use several traces or adapt τ. Cite "How Athena Learns" and Figure 16.3.

## Lab 16.2 - The Cost of Runaway Firing

1) Synapses: 2.0 × 10^6 × 750 = 1.50 × 10^9. Events per second: at 26 Hz, 1.50 × 10^9 × 26 = 3.90 × 10^10; at 834 Hz, 1.50 × 10^9 × 834 = 1.25 × 10^12 (a 32-fold increase). Matches the check.
2) Factor 834 / 26 = 32.08. Solve 0.98^n = 1/32.08: n = ln 32.08 / (−ln 0.98) = 3.468 / 0.0202 = 171.67, about 172 steps. Matches the check. Assumption: each step's scaling reduces firing proportionally and nothing pushes back; with recurrent excitation, firing falls less than proportionally, so more steps would be needed.
3) Chapter 1 (and Lennie, cited in "The Model in Eight Statements") puts the affordable fraction at about one neuron in a hundred active at once; cortical mean rates are of the order of a few spikes a second at most. At 26 Hz with a 1 ms step, about 2.6 percent of neurons would fire per step, already above 1 percent; at 834 Hz, about 83 percent would fire per step, roughly 80 times the budget and close to the ceiling a refractory period allows (a 1 to 2 ms refractory period caps a neuron at about 500 to 1,000 Hz). The network has left the sparse regime of Chapters 1 and 13 entirely. Instructor note: the chapter also reports about 15,000 spikes per time step network-wide ("Reading the Failures Through the Book"), which is only about 0.75 percent of 2.0 million neurons; if students notice the inconsistency, credit them, and point out that the two figures come from different logs and that a per-neuron 834 Hz is near the physical ceiling, so the alert value may average over a short window or over the most active populations. The chapter does not say which.
4) Grading guide: controller speed: homeostatic scaling acts slowly (hours to days in biology; capped at 2 percent per step in NIMCP), while recurrent excitation compounds on the timescale of milliseconds, so in a large, strongly recurrent network runaway can grow faster than the controller corrects it (Chapter 4's fast inhibition is what biology uses at that timescale). Gain of recurrence: the number of recurrent inputs and total excitatory drive grow with network size and connectivity, pushing the network past the point where excitation outruns inhibition (an instability rather than a slow drift). Calibration: NIMCP's homeostasis targets 3 to 5 percent active, tuned on a small network; a fixed per-step cap and a target tuned at one scale may not hold at another. Strong answers also mention that inhibitory plasticity and balanced excitation and inhibition (Chapter 4), not only slow scaling, keep cortex stable, and recommend testing stability at small scale first ("What NIMCP Gets Right, and What Would Test It").

## Lab 16.3 - Reading the Evaluations

1) Fractions distinct: 20/50 = 0.40; 2/50 = 0.04; 19/50 = 0.38; 1/50 = 0.02; 33/50 = 0.66; 21/50 = 0.42. The checkpoint with 1 answer (0.02) shows full collapse onto a single answer; the checkpoint with 2 (0.04) is near-total collapse. (The chapter notes that at several checkpoints the same string was given to every question; the 1 in Figure 16.4 spans steps 3,900 to 4,000.)
2) Diversity (16 to 17 distinct outputs of 20, 0.80 to 0.85) shows the output is not stuck on one word, but fidelity (1 of 20, 0.05) shows the outputs do not correspond to the intents. High diversity with low fidelity is what random or input-independent output produces; low diversity with low fidelity is collapse. Only fidelity says whether the input determined the output, and diversity says whether a fidelity score could be inflated by always giving a common answer. Learning would show up as fidelity rising well above chance with diversity matched to the number of intents. Cite "What the Measurements Show."
3) Grading guide: acceptable measures include a closed-form test with known answers (multiple choice or single-word answers checked against a key, for example "What color is the sky?" answer "blue"), human ratings by blinded raters with a rubric, a category or property-verification test, or retrieval: whether the answer is closer to its own question's reference answer than to other questions' reference answers (a confusion matrix across questions). Weaknesses: keys penalize correct paraphrases and reward guessing; human ratings are costly and subjective; embedding similarity metrics usually still use a pretrained model and reward lexical overlap ("0.02 similarity" was itself computed this way). A strong answer names the chance baseline and a control (shuffled questions).
4) Grading guide: convincing evidence should be behavioral and controlled: producing the right word for a referent (and the right referent for a word) above chance on items not seen in training, across modalities, robust to paraphrase; graded similarity structure among word representations (same-category words closer), the opposite of the May probe; lesion or ablation of the relevant representation removing the ability; and evidence that the meaning is not simply copied from the pretrained embedding targets (the chapter notes the targets come from a transformer). Common mistakes: accepting fluent output (grammar rules and Phi-3 can produce fluency), or counting a single correct answer.

## Lab 16.4 - Scale Is Not Organization

1) NIMCP 1.5 × 10^9 / 2.0 × 10^6 = 750.00; fly 54.5 × 10^6 / 139,255 = 391.37; human neocortex 164 × 10^12 / 16.3 × 10^9 = 10,061.35. Matches the check. NIMCP has about 1.9 times the fly's connections per neuron and about a thirteenth (750 / 10,061 = 0.075; the chapter says "less than a tenth") of a cortical neuron's.
2) Any three of: inherited, innate circuitry specified by evolution and development (dedicated sensory and motor circuits, mushroom bodies, central complex) rather than a generic random hierarchy (Chapters 10 and 13); a body with sensors, effectors, and real needs that anchor value; identified neuromodulatory systems acting on specific circuits (octopamine and dopamine reward signals used in learning); learning rules and sensitive periods tuned by evolution; energy-efficient sparse coding under real constraints; specialized cell types numbering in the thousands (8,453 types in the fly connectome by comparison) rather than a few classes.
3) Synapses: 2.0 × 10^6 × 10,061.35 = 2.01 × 10^10. Memory: 2.01 × 10^10 × 12 bytes = 2.41 × 10^11 bytes = 241.5 GB (224.9 GiB). Matches the check. For comparison, the current 1.5 × 10^9 synapses at 12 bytes is about 18 GB, consistent with the roughly 21 GB saved state, and the project already struggles to fit that into memory.
4) Grading guide: the expected position is organization ("Reading the Failures Through the Book": "Scale is probably not the main obstacle; organization is"). Evidence: a honeybee with fewer neurons learns to count and categorize; NIMCP's failures map onto missing connections (no trace, one memory system, basal ganglia not selecting actions, no sequencing, runaway firing) rather than shortage of units; increasing connectivity would worsen runaway excitation and memory pressure. A strong answer acknowledges what scale could contribute (more inputs per neuron may help pattern separation and reliability) and proposes the test: get a fly-sized network working first. Common mistake: arguing for more synapses without addressing stability.

## Lab 16.5 - Auditing a Mechanism

1) Any row of Figure 16.2.
2) Example model answers (one sentence each, from "The Book's Model, Line by Line" and "How Athena Learns"):
   - Row 4: description claims three-factor learning with eligibility traces and dopamine; code applies a same-step coincidence rule scaled by reward minus its running average, with traces reaching only a legacy network without hidden neurons, a reward signal mostly from falling training loss, and most learning by backpropagation.
   - Row 5: description claims fast and slow memory with sleep replay and protection against forgetting; code replays into the same network and EWC is implemented but not connected.
   - Row 6: description claims basal ganglia action selection and habits; code registers and strengthens habits but never asks the module to choose actions.
   - Row 1: description claims set points as the reward function; code has drives and set points but no body.
   - Row 3: description claims prediction and active inference; the world-model trainer is called in a way that does nothing and free energy is bookkeeping.
3) Example for row 6: connected, the system's actions (word choices) would vary with learned values; outputs would shift from goal-directed (sensitive to outcome devaluation) to habitual with practice; lesioning the module would change behavior. Disconnected, removing or altering the module changes nothing in output. For row 4: connected, credit would reach synapses active seconds before reward and delayed-reward tasks would be learnable by the spiking core alone.
4) Grading guide: needs an intervention and a control. Example: lesion or randomize the basal ganglia module (or its habit weights) in a trained checkpoint versus a sham lesion and compare outputs on fixed prompts; any difference beyond run-to-run noise shows it is in the path. Or a devaluation test: devalue a rewarded output and compare early versus late training. For row 4: train the spiking core alone on a delayed-reward task with traces connected versus the coincidence rule (the Figure 16.3 design). Also acceptable: instrumentation (log whether the function is called and whether its outputs affect downstream variables), but a behavioral test is preferred.
5) Grading guide: causes include incremental development where documentation states intent rather than state; features added but not wired, or disabled during debugging and never re-enabled; refactoring that leaves a module in place but bypasses it; enthusiasm and outreach (the "trillions" and "not because we programmed grammar" claims); scale that makes it hard for anyone to hold the whole system in mind. Guards: tests that assert each mechanism changes behavior (ablation tests in CI), documentation generated from or checked against code and measured values, measuring each mechanism against a control before adding the next, independent audits, and the chapter's rule to "read the code, not the description."

## Lab 16.6 - Designing the Next Experiment

1) Any one of the four.
2) Grading guide with an example (three-factor rule): hypothesis: a reward-gated rule with an eligibility trace (τ of several steps) learns a delayed cue-reward association that a coincidence rule cannot; network: a few hundred to a few thousand LIF neurons, or fly scale (about 10^5) at most; task: cue followed by reward after variable delays, with distractor activity; control: the identical network with the coincidence rule (trace removed), and a shuffled-reward control; measurement: selectivity of weight change (cue synapse versus background) and behavioral accuracy as a function of delay; success: trace rule above chance at delays beyond the cue duration while the coincidence rule is at chance; failure: no difference, or the trace rule also fails. Other designs: stable firing (measure mean rate and fraction active while learning; success means rate stays within a target band, for example 1 to 5 percent active, as the network grows from 10^3 to 10^5 neurons); fast and slow memory (learn task A then task B; success means retention of A with replay-linked dual systems versus catastrophic forgetting in a single-network control); lesion (train to criterion, lesion a module versus a random equal-size set, measure specific deficits). Each must specify all six elements in step 2.
3) Predicted results: trace beats coincidence for delays beyond the cue (Chapter 3; Figure 16.3); stable firing requires fast inhibition plus slower homeostasis (Chapters 4 and 5); dual memory with interleaved replay avoids catastrophic interference (Chapter 5, McClelland, McNaughton, and O'Reilly); lesions produce graded, specific deficits, with compensation over time if plasticity remains (Chapter 1). The prediction must name a chapter.
4) Grading guide: a strong answer separates explanations for a negative result: a bug or disconnected mechanism (verify wiring with an instrumentation check first, the lesson of Lab 16.5); wrong parameters (sweep τ, learning rate, inhibition strength); task too hard or too easy; insufficient statistics; and only then a real failure of the book's prediction, which would be informative about the model. It should say what it would change and what it would not (do not scale up to fix a small-scale failure).

## Lab 16.7 - NIMCP on the Model (concept map)

1) Copy of Figure 15.1: body in a world; predictions meeting input; errors of several kinds; neuromodulators broadcast and set learning rate; local plasticity gated by three factors; fast store and slow cortex linked by replay; value to choice to habit; action; constraints (energy, space, time, noise, genome); evolutionary history.
2) Expected coloring (from Figures 16.1 and 16.2 and the text):
   - Running in the main path: spiking LIF network with conductance synapses, NMDA, interneuron classes, heterogeneity (poor parts); reward-gated same-step Hebbian rule; dopamine-like signal from falling loss; predictive-coding hierarchy (trained); surprise-gated fast store; sleep replay and "dream" blends (into one network); homeostatic scaling and inhibitory strengthening; staged curriculum with LLM parent; backpropagation networks and pretrained embeddings (running but not brain-like; some students will mark these separately); hypothalamic drives and set points; safety rules, audit log, watchdog.
   - Present but not connected: eligibility traces and STDP (reach only a legacy network); TD-error module (not called); world-model trainer (called so that it does nothing); EWC (not connected); basal ganglia action selection (registers habits but does not choose actions); robotic and sensor interfaces (placeholder); slow cortical system distinct from fast store (replay goes into the same network).
   - Absent: a body; an energy constraint (the binding constraint is memory); innate, evolved structure; sequencing of words; contingent social teacher; the translation from numeric decisions to symbolic safety rules.
3) Missing links to draw: neuromodulators/dopamine to spiking synapses via eligibility traces; TD error to dopamine signal; basal ganglia to action and output; fast store to a separate slow learner via replay (and EWC to the slow learner); body to drives (and body state to value); world model to prediction; inhibition and homeostasis keeping pace with excitation; numeric decisions to symbolic safety rules; sequencing loop (basal ganglia) to language output.
4) Grading guide: strong candidates are the eligibility trace into the large spiking network (Chapter 3; Figure 16.3 shows credit fails without it; without it the brain-like core cannot learn from delayed reward), fast inhibition and homeostasis that keep pace with excitation (Chapters 1, 4, 5, 13; runaway firing and ambient domination underlie the collapsed output, and nothing else can be tested until firing is stable, which is why the chapter puts it first), or a separate slow memory with replay (Chapter 5; drift and resets). Accept any choice justified with book evidence and with an argument about dependency order.
5) Grading guide: points to cover from "What Building Teaches" and "The Central Lesson": mechanisms translate readily into code, but their connections do not; a system can contain every mechanism and not work because the design is in how they are joined; the hardest parts to build are the brain's most distinctive achievements and the least understood; failures that fall where the theory predicts are evidence for the theory; NIMCP is the mirror of the microprocessor study (complete code knowledge without understanding); building requires testing each mechanism small against a control and reading code rather than descriptions. Strong answers note the limits: one case study by the author, and failures can also come from engineering bugs. Common mistake: concluding simply that the approach is wrong or that more scale will fix it.

### Notes for instructors
- (a) the chapter's Figure 16.3 ratios ("nine" at d = 5, "four" at d = 10) come from a simulation in which background starts at step 0 and the cue synapse also fires at random after the cue (simulated means about 8.7 and 3.9), so student ratios of about 8.2 and 3.1 (cue-only trace, background from step 0, as the lab specifies) are correct; values of about 4.3 and 2.3 (infinite background history) are correct for that stated assumption. (b) Lab 16.2 treats 834 spikes a second as a per-neuron mean; that is near the refractory ceiling of a LIF neuron and sits awkwardly with the chapter's figure of about 15,000 spikes per step across about two million neurons (about 0.75 percent per step). The computed checks are right for the given value, but instructors may wish to flag this in discussion.
