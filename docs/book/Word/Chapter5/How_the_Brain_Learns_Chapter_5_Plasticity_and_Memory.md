---
title: "Chapter 5"
subtitle: "Plasticity and Memory: How Experience Becomes Structure"
---

> *"When an axon of cell A is near enough to excite a cell B and repeatedly or persistently takes part in firing it, some growth process or metabolic change takes place in one or both cells such that A's efficiency, as one of the cells firing B, is increased."*
>
> --- Donald Hebb, *The Organization of Behavior* (1949)

# Memory Is Not Storage

Every chapter so far has ended at the same door. Chapter 1 said that the brain has no reset button because every experience leaves a trace. Chapter 2 said that a neuron cannot hold a variable, so learning must be physical change. Chapter 3 said that neuromodulators decide when that change is permitted. Chapter 4 said that the hippocampus separates, stores, completes, and compares, and deferred the question of how its synapses change. This chapter walks through the door.

The first thing to leave behind is the vocabulary of storage. A computer writes a value to an address and reads it back unchanged. Nothing in the brain does this. There is no address, no write operation, and no read that leaves the record as it found it. What there is instead is a system whose physical structure is altered by use, so that the next time similar activity arrives it unfolds differently. Memory is not something the brain has. It is something the brain's tissue has become.

This reframing is not a philosophical nicety. It predicts most of what follows: why learning is slow, why memories blur into one another, why recalling a memory can change it, why sleep matters, and why forgetting is a mechanism rather than a malfunction.

# What Can Change

Hebb's postulate, quoted above, is the founding statement of the field, and it is deliberately vague about mechanism: "some growth process or metabolic change." Seventy-five years later the list of things that can change is long. The important ones fall into four groups.

The strength of an existing synapse can change. On the presynaptic side, the probability that an action potential releases neurotransmitter can rise or fall. On the postsynaptic side, the number of receptors in the membrane can be increased or reduced within minutes, by inserting or removing receptor proteins from a reserve just beneath the surface. A synapse that doubles its receptors roughly doubles its effect.

The structure of the synapse can change. Most excitatory synapses on cortical neurons sit on dendritic spines, small protrusions a micrometer long. Spines grow, shrink, appear, and vanish. A spine that enlarges carries a stronger synapse; a spine that disappears takes its synapse with it. Imaging the same neurons over weeks shows a population of spines in constant slow turnover, with a stable core that persists for the life of the animal and a changeable fringe that reflects recent experience.

The neuron's own excitability can change. The density and type of ion channels in the membrane are adjusted by activity, so that the same synaptic input produces more or fewer spikes. This is plasticity of the cell rather than of the connection, and it is less specific but often faster.

Finally, new synapses can form between neurons that were not connected, and in a few regions, chiefly the dentate gyrus of the hippocampus, new neurons are born throughout life. These are the slowest changes and the ones most clearly tied to structural growth.

All four share a property that distinguishes them from writing to memory: they are modifications of machinery that is also doing something else. The synapse that is strengthened is still transmitting. The spine that grows is still part of a dendrite that integrates thousands of inputs. There is no separate medium.

# Hebb's Rule and Its Problem

Hebb's postulate says that cells that fire together wire together. The strength of a synapse should increase when the presynaptic and postsynaptic neurons are active at the same time.

This rule is attractive because it is local. Each synapse needs only information available at the synapse itself, the activity of the two cells it joins, and no global error signal. It also has an immediate problem, which the first computational models exposed in the 1970s: it only goes up. A synapse strengthened by correlated activity makes that correlation more likely, which strengthens it further. Left alone, Hebbian learning drives every active synapse to its ceiling and erases whatever selectivity it began with.

A working learning rule therefore needs three things Hebb did not specify: a way to weaken synapses, a bound on how strong they can become, and a criterion for which correlations count. The biology supplies all three, and the rest of this chapter is largely an account of how.

# The Coincidence Detector

The mechanism that implements Hebb's "fire together" is a single protein, the NMDA receptor.

Most fast excitatory transmission uses AMPA receptors: glutamate binds, the channel opens, sodium enters, the membrane depolarizes. The NMDA receptor also binds glutamate and also conducts, but at the resting membrane potential its pore is plugged by a magnesium ion from outside the cell. Glutamate alone opens nothing. The plug is expelled only when the membrane is already depolarized, by many simultaneous AMPA inputs or by an action potential propagating back from the soma into the dendrite.

![Figure 5.1. The NMDA receptor opens only when glutamate is present and the membrane is depolarized, so the calcium it admits reports that presynaptic and postsynaptic activity coincided.](images/fig_nmda.png)

So the NMDA receptor conducts only when two conditions hold at once: the presynaptic neuron has released glutamate, and the postsynaptic neuron is depolarized. It is a molecular AND gate for the two halves of Hebb's rule. What passes through it when it opens is calcium, and calcium is the signal that sets the plasticity machinery in motion.

Figure 5.1 shows the two states. In the first, glutamate is bound but the magnesium plug holds and nothing passes. In the second, depolarization has removed the plug, calcium enters, and a cascade of enzymes begins that can last for hours.

# LTP and LTD

The two outcomes of that cascade are long-term potentiation, a lasting increase in synaptic strength, and long-term depression, a lasting decrease. Both were first measured in the hippocampus, LTP in 1973 and LTD a decade later, and both are now known throughout the brain.

What decides the direction is the calcium signal itself. A large, brief rise in calcium, the kind produced by strong input coinciding with postsynaptic spikes, activates kinases, which add phosphate groups to proteins and drive extra AMPA receptors into the synapse. A smaller, more prolonged rise, the kind produced by weak or poorly timed input, preferentially activates phosphatases, which remove phosphate groups and pull receptors out. The same ion in different amounts produces opposite results (Figure 5.2A).

![Figure 5.2. A: postsynaptic calcium determines the direction of change; modest, prolonged rises weaken a synapse, large brief rises strengthen it. B: simulated time course of a synapse's response after brief high-frequency stimulation (LTP) and after prolonged low-frequency stimulation (LTD).](images/fig_ltp_ltd.png)

Experimentally, a second of stimulation at 100 Hz potentiates a synapse within minutes and the potentiation persists for hours in a slice and for weeks or longer in a living animal. Fifteen minutes at 1 Hz depresses the same synapse (Figure 5.2B). Neither effect requires anything from outside the synapse and its immediate neighborhood. Hebb's growth process is real, and so is its opposite.

LTP has two phases. Early LTP, lasting an hour or two, uses proteins already present in the spine. Late LTP requires new protein synthesis and gene expression in the nucleus, and it is accompanied by visible enlargement of the spine. Block protein synthesis within an hour of learning and the memory forms but does not last. This is the first of the chapter's two consolidation clocks.

# Timing Is Causation

Hebb's phrase "takes part in firing" contains a subtlety that the rate-based LTP experiments missed. For cell A to take part in firing cell B, A must fire first.

Experiments in the late 1990s, pairing single presynaptic and postsynaptic spikes at controlled intervals, showed that the synapse respects this order. If the presynaptic spike precedes the postsynaptic spike by a few milliseconds to a few tens of milliseconds, the synapse strengthens. If the order is reversed, it weakens. The effect falls off exponentially with the interval and is negligible beyond about 50 ms in either direction (Figure 5.3).

![Figure 5.3. Spike-timing-dependent plasticity. A presynaptic spike shortly before a postsynaptic spike strengthens the synapse; the reverse order weakens it. Dots: simulated single-pairing measurements.](images/fig_stdp.png)

This is spike-timing-dependent plasticity, and its logic is causal. A synapse whose input arrived just before the neuron fired may have helped cause the spike, and it is rewarded. A synapse whose input arrived just after the spike could not have contributed, and it is penalized. The window is set by the kinetics of the NMDA receptor: a back-propagating spike that arrives while glutamate is still bound expels the magnesium and admits a large calcium pulse; one that arrives before the glutamate finds the receptor closed, and the glutamate that follows meets a membrane that has already repolarized, producing only a small, slow calcium signal.

The timing rule does two things rate-based Hebbian learning cannot. It strengthens chains of neurons that fire in sequence, which is how a circuit can learn an ordered pattern. And it provides the weakening that Hebb's rule lacked, applied precisely to the connections that fire out of order.

# Keeping the Whole Neuron Stable

Local rules, even with weakening built in, do not by themselves keep a neuron's total input within a usable range. A neuron whose synapses have all been potentiated fires to everything; one whose synapses have all been depressed fires to nothing. Two further mechanisms, operating on the whole cell rather than the single synapse, prevent this.

The first adjusts the rule itself. The calcium threshold that separates LTD from LTP is not fixed; it slides with the neuron's recent average activity. After a period of intense firing the threshold rises, so that the same input now produces depression where before it produced potentiation. After a quiet period it falls. This sliding threshold, proposed by Bienenstock, Cooper, and Munro in 1982, makes the neuron self-correcting: the more it fires, the harder it becomes to strengthen its inputs (Figure 5.4A).

![Figure 5.4. Two whole-neuron stabilizers. A: the crossover point between depression and potentiation slides with the neuron's recent activity. B: synaptic scaling multiplies every input by the same factor, preserving the pattern of relative strengths that learning established.](images/fig_homeostasis.png)

The second adjusts all the synapses at once. If a neuron's firing stays too high for hours, every excitatory synapse on it is scaled down by the same factor; if too low, all are scaled up. Because the scaling is multiplicative, the ratios between synapses, which is where the learned information lives, are preserved (Figure 5.4B). This synaptic scaling is slow, on the order of a day, and it is the cellular counterpart of the excitation-inhibition balance of Chapter 4.

Inhibitory synapses are plastic too, and their plasticity is largely homeostatic: inhibition onto a neuron grows in step with the excitation it receives. Between the sliding threshold, scaling, and inhibitory plasticity, the brain solves the stability problem that a pure Hebbian rule creates, and it does so without a global supervisor.

# The Third Factor

Chapter 3 described a three-factor rule: a synapse changes when it was recently active, when its neuron fired, and when a neuromodulatory signal arrives saying that something significant happened. The mechanisms in this chapter supply the first two factors. The third plugs into them in a specific place.

Early LTP sets a tag at the synapse, a transient biochemical mark lasting an hour or two. Late LTP requires proteins that are made in the cell body and shipped to every dendrite. Only tagged synapses capture them. A weak stimulus that sets a tag but does not trigger protein synthesis produces LTP that fades, unless, within the tag's lifetime, something else triggers synthesis. Dopamine, acting on the cell, is one of the things that can. The result is that a synapse activated during an unremarkable event can be consolidated retroactively by a reward that arrives an hour later. This is synaptic tagging and capture, and it is the eligibility trace of Chapter 3 seen at the level of molecules.

# From Synapse to Engram

A memory is not a synapse. It is a pattern of strengthened connections among a set of neurons, and the set is sparse: in the hippocampus and amygdala, a few percent of the cells in a region take part in encoding any particular event.

![Figure 5.5. A memory as a sparse ensemble. Encoding strengthens the connections among a small set of cells (A); a partial cue activates a few of them (B); the strengthened recurrent connections complete the pattern (C).](images/fig_engram.png)

The word for this set is the engram, a term coined in 1904 for a hypothetical physical trace of memory. For a century the engram was an inference. In the last fifteen years it has become an experimental object. Neurons that are active during a learning event can be labeled genetically and later made to fire with light. Reactivating them, in the absence of any cue, produces the behavior the animal learned, such as freezing in a chamber where it was once shocked. Silencing them prevents recall even when the cue is present. And activating the engram of one place while an animal is being shocked in another creates a memory of a fear that never happened: the animal later freezes in the first place.

These experiments establish that a specific, identifiable set of cells and connections is both necessary and sufficient for a specific memory. They also show the mechanism of recall that Chapter 4 called pattern completion. The engram cells are connected to one another more strongly than to their neighbors, as in Figure 5.5. A cue that activates a few of them drives the rest through those connections, and the whole pattern returns. Recall is a dynamical event, not a lookup.

![Figure 5.6. The hippocampus and amygdala in the medial temporal lobe, with the structures around them. The hippocampus encodes episodes; the amygdala attaches emotional weight.](images/limbic.png)

# Two Clocks

A memory that has been encoded is not yet durable. It becomes durable through two processes on very different timescales (Figure 5.7A).

Synaptic consolidation is the hour-scale transition from early to late LTP described above: protein synthesis, spine growth, and the structural stabilization of the changed synapses. During this window the memory can be blocked by drugs, by a second competing experience, or by a blow to the head. After it, the memory survives these insults.

![Figure 5.7. A: synaptic consolidation stabilizes a memory within hours; systems consolidation moves it over weeks and years. B: complementary learning systems: a fast hippocampal learner captures the day, a slow cortical learner integrates it, and replay carries one to the other.](images/fig_consolidation.png)

Systems consolidation is the transfer, over weeks to years, of the memory from dependence on the hippocampus to independence from it. Patients with hippocampal damage lose the ability to form new episodic memories and lose recent memories, but retain old ones, with the boundary falling years before the injury. The hippocampus, on this account, holds a rapidly formed index that binds together the cortical regions that represented the experience. Over time, repeated reactivation strengthens the direct cortical connections until the index is no longer needed.

The theory that explains why the brain would bother with two systems was set out in 1995 by McClelland, McNaughton, and O'Reilly, and it is the most important idea in this chapter for readers from machine learning. A single network that learns fast enough to capture a single experience will overwrite what it already knows; this is catastrophic interference, and it is a mathematical property of distributed representations, not a biological quirk. A network that learns slowly enough to avoid interference cannot capture a single experience at all. The solution is two networks: a fast, sparse hippocampal learner that stores each day's events with minimal overlap, and a slow cortical learner that extracts their statistical structure. The fast one trains the slow one gradually, by replaying its contents interleaved with everything else (Figure 5.7B).

# Sleep

The replay is real, and it happens mainly during sleep.

Place cells in the hippocampus fire in sequence as an animal runs along a track. During the slow-wave sleep that follows, the same cells fire in the same sequence, compressed roughly twentyfold, during brief high-frequency events called sharp-wave ripples. The ripples drive cortical activity. Disrupt them selectively and the animal's memory of the track is impaired; prolong them and it improves. Cue a memory during sleep, with an odor or a sound that was present during learning, and that memory is preferentially strengthened.

![Figure 5.8. A night's sleep, with its alternation of slow-wave and REM stages. Hippocampal replay and sharp-wave ripples are concentrated in slow-wave sleep.](images/hypnogram.png)

Sleep also appears to do a complementary job: scaling down. Synapses strengthened during the day make the cortex progressively more excitable and more expensive to run. Across a night of slow-wave sleep the average synaptic strength falls, by the homeostatic mechanisms of the previous section. The net effect is to preserve the ratios that encode what was learned while returning the total to a sustainable baseline. On this view sleep is not a pause in learning but its second half.

# Recall Changes the Record

Because recall is reactivation of the engram, and reactivation reopens the window of synaptic plasticity, recalling a memory makes it labile again. For some hours after retrieval, a consolidated memory can be strengthened, weakened, or altered, and must be reconsolidated to persist. Block protein synthesis in that window and the memory, which was stable the day before, is lost.

This reconsolidation is the mechanism behind two things that look like faults from the storage point of view. Memories drift: each recall is an opportunity for the present context to be blended into the trace, and eyewitnesses who have told their story many times are confident and wrong in ways that match what they have been told since. And memories can be revised: a fear memory reactivated and then given corrective information in the reconsolidation window is weakened more durably than one treated outside it, which is the basis of several clinical approaches to trauma.

A record that changes when read is a bad database. It is a good adaptive system, because the point of a memory is not fidelity to the past but usefulness in the future, and the future keeps changing.

# Forgetting Is a Mechanism

The default fate of a memory is to be lost. Ebbinghaus measured the forgetting curve in 1885 on himself and lists of nonsense syllables; it has been replicated for every kind of material since. Retention drops steeply in the first hours and days and then more slowly, and the curve is roughly the same whether the material is nonsense or meaningful. What changes with meaning is the starting point, not the shape.

![Figure 5.9. Retention after a single exposure (gray) and with retrieval at increasing intervals (blue). Each successful retrieval slows the subsequent decay.](images/fig_forgetting.png)

Three things slow the curve. Retrieval slows it: a memory that is actively recalled, rather than re-read, decays more slowly afterward, and the effect grows when the retrievals are spaced out (Figure 5.9). Sleep slows it, through the consolidation above. And emotional significance slows it, through the third factor.

Forgetting is also actively produced. The dentate gyrus grows new neurons throughout life, and their integration rewires existing circuits; increasing neurogenesis in mice accelerates the loss of recent memories, and suppressing it preserves them. Small signaling proteins in the spine actively shrink synapses that are not being used. These mechanisms cost energy, which is the strongest evidence that forgetting is not decay but function. A system that must remain flexible cannot afford to keep everything, and what it keeps must be generalized, which means the specifics must go.

# Kinds of Memory, Kinds of Circuit

Psychology distinguishes many kinds of memory: episodic and semantic, procedural, emotional, working. The distinction is real, but it is not a hierarchy of storage tiers. Each kind is a different circuit using a different physical mechanism (Figure 5.10).

![Figure 5.10. Kinds of memory are kinds of circuit. Each row is a different region and a different physical mechanism, not a different level of one storage system.](images/fig_systems.png)

Episodic and semantic memory, the memory for events and facts, depend on the hippocampus and its systems consolidation into cortex. Procedural memory, for skills and habits, lives in the basal ganglia and cerebellum of Chapter 4, where dopamine-gated striatal plasticity and climbing-fiber-driven cerebellar LTD change what the body does without any episode being recalled. Emotional memory depends on the amygdala, where LTP is fast, durable, and notoriously hard to erase, which is why fear is easily learned and rarely unlearned, only suppressed. Working memory, the few seconds of holding a number in mind, is not synaptic change at all but persistent activity in prefrontal and parietal circuits, sustained by the recurrent excitation of Chapter 4 and by short-term facilitation of synapses that lasts seconds and leaves no structural trace.

A patient can lose one of these without the others. The amnesic patient H. M., who could form no new episodic memories after his hippocampi were removed, learned to trace a star in a mirror as well as anyone, improving day by day while denying each day that he had ever seen the task. His skill was in a circuit his lesion had not touched.

# Why Learning Is Slow

Chapter 1 promised that learning is slow because physical change is slow. This chapter has shown the detail. Early LTP takes minutes; late LTP takes hours and new protein; systems consolidation takes weeks; a skill takes thousands of repetitions because striatal and cerebellar synapses change by small increments gated by a scarce teaching signal.

But the chapter has also shown that the slowness is not only a limitation of the hardware. It is a design requirement. The stability-plasticity dilemma, the fact that a system cannot both change quickly and retain what it knows, is solved by learning slowly in the cortex and letting the hippocampus take the speed. Fast learning is quarantined to a structure built for it, and everything else changes at a pace that protects what is already there. Slowness is the price of not overwriting yourself, which, for a system without a reset button, is the price of staying coherent.

# Implications for Artificial Intelligence

Memory is where biological and artificial learning differ most, and where the biology has the most to offer.

First, catastrophic interference is the central unsolved problem of continual learning in artificial networks, and the brain's solution is architectural: two learners with different rates, and replay to interleave them. Experience replay in reinforcement learning is a direct borrowing. Systems that train a fast episodic store and distill it gradually into slow weights are the closest artificial analog of consolidation.

Second, local rules can be enough. Backpropagation needs a global error signal delivered to every weight. LTP, LTD, and timing-dependent plasticity need only what is present at the synapse plus a broadcast modulator. Whether local three-factor rules can match gradient descent on hard problems is open, but the brain is an existence proof that they can learn language, motor skill, and science.

Third, stability must be engineered. Pure Hebbian learning runs away, and the brain's answer is a sliding threshold, synaptic scaling, and inhibitory plasticity. Normalization layers and weight decay are rough analogs; a homeostatic mechanism that adapts to each unit's own history is closer to the biology and less explored.

Fourth, forgetting should be a mechanism, not an accident. A model that stores everything generalizes poorly and grows without bound. The brain spends energy to remove specifics and keep gist. Artificial systems mostly have no equivalent to deliberate, selective forgetting.

Finally, a memory that changes when read is a feature. Artificial retrieval systems return the stored record unchanged. Biological recall reconsolidates, blending the record with the present. That costs fidelity and buys relevance. For agents that must act in a changing world, the trade is worth considering.

# The Central Lesson

Experience becomes structure. A coincidence detector at the synapse turns correlated activity into calcium, calcium into receptor traffic and spine growth, and spine growth into a lasting change in what the circuit does next. Whole-cell mechanisms keep the process stable, neuromodulators decide when it counts, and two consolidation clocks turn a day's traces into durable knowledge without overwriting the knowledge that was there. Recall reopens the trace, and forgetting prunes it. Nothing is stored. Everything is rebuilt.

# Next Chapter

Chapter 6: Perception as Inference --- How the Brain Sees What It Expects

# Figure Credits

Figures 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 5.9, and 5.10 were drawn for this book. The traces in Figure 5.2B and the curves in Figures 5.3 and 5.9 are illustrative simulations, not data.

Figure 5.6: "Limbic System" by BruceBlaus (Blausen.com staff, "Medical gallery of Blausen Medical 2014," WikiJournal of Medicine), CC BY 3.0, via Wikimedia Commons.

Figure 5.8: "Sleep Hypnogram" by Wikimedia Commons user RazerM, CC BY-SA 3.0; composited on a white background.
