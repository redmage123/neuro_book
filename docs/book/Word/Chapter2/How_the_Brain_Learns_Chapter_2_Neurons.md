---
title: "Chapter 2"
subtitle: "Neurons: The Brain's Signaling Cells"
---

> *"Like the entomologist in pursuit of brightly coloured butterflies, my attention hunted, in the flower garden of the gray matter, cells with delicate and elegant forms, the mysterious butterflies of the soul, the beating of whose wings may some day—who knows?—clarify the secret of mental life."*
>
> --- Santiago Ramón y Cajal, *Recollections of My Life* (1937)

# Matter That Signals

The previous chapter argued that the brain is not a digital computer but a physical, biological system shaped by evolutionary constraint. That argument now has to be paid for in detail. If cognition arises from matter, what kind of matter can support perception, memory, and action, and what do its physical properties allow and forbid?

The answer begins with a single kind of cell. At the end of the nineteenth century, Santiago Ramón y Cajal stained slices of brain with Camillo Golgi's silver method (Chapter 1) and drew what he saw: discrete, branching cells, each bounded by its own membrane, touching but not fused with their neighbors. Wilhelm Waldeyer gave the cell its name, the neuron, in 1891, and the claim that the nervous system is built from such units, the neuron doctrine, rests chiefly on Cajal's drawings.[^1] The cells Cajal called the butterflies of the soul were pyramidal neurons of the cerebral cortex, and the hope in the epigraph above, that their study would one day explain the mind, is the program this book follows.

Neurons are living cells, governed by the same physical and chemical laws as every other biological system; they consume energy, respond to stress, and eventually fail, and yet, organized in vast networks, they give rise to perception, memory, and thought. This chapter follows a signal through one neuron, from the chemical event at a synapse to the electrical impulse that leaves along the axon, and asks at each step what the physics costs and what it buys. Readers who want the underlying cell biology in more detail will find it in Chapter 0.

# A Neuron Is a Cell

That statement is easy to say and easy to forget. Neurons are not logic gates. They do not execute instructions, store variables, or manipulate symbols; those descriptions are metaphors imposed at higher levels of analysis, useful for some purposes and misleading for others.[^2] At the level of mechanism, a neuron integrates physical inputs and generates physical outputs according to biophysical rules, and it has no place to hold a variable apart from its own structure.

Like all cells, a neuron is bounded by a membrane, a film of fatty molecules about five nanometers thick that water and charged particles cannot easily cross.[^3] On either side of the membrane is a salt solution, but not the same one. Inside, potassium ions are concentrated and sodium ions are scarce; outside, the reverse. The difference is maintained by a protein embedded in the membrane, the sodium-potassium pump, which on each cycle pushes three sodium ions out and brings two potassium ions in. Each cycle is paid for with one molecule of ATP (adenosine triphosphate), the small molecule that cells use as an energy currency, spending it to drive reactions that would not run on their own. Because the membrane at rest lets potassium leak out more easily than sodium leaks in, the unequal distribution leaves the inside of the cell about 70 millivolts negative relative to the outside. This is the resting potential, and every signal the neuron produces is a brief departure from it.

Figure 2.1 shows the arrangement: two salt solutions, a thin membrane, pumps that burn ATP without pause, and channels, pores in the membrane that open and close, through which ions cross when the cell signals. The cost of keeping this order is large. By Attwell and Laughlin's estimate in Chapter 1, most of the energy budget goes to pumping back the ions that signaling lets through.[^4]

![Figure 2.1. A neuron is a living cell. A membrane separates two salt solutions; pumps burn ATP continuously to keep sodium out and potassium in, and gated channels let ions cross when the cell signals. Nothing here is a logic gate.](images/fig_cell.png)

What distinguishes neurons from most other cells is not excitability alone, which they share with muscle and some gland cells, but a combination: the ability to generate electrical signals, to transmit them over long distances, to influence particular other cells, and to modify those influences over time.[^5]

# The Polarized Structure of Neurons

Despite their diversity, most neurons share a common structural plan, and the plan constrains how information can flow. At one end are the dendrites, branching structures that receive signals from other neurons. At the center is the cell body, or soma, which holds the nucleus and the cell's metabolic machinery. Extending from the soma is the axon, a long, thin projection that carries the neuron's output, a brief all-or-none electrical impulse called the action potential, or spike, sometimes for a millimeter and sometimes for a meter. In long-range axons the fiber is wrapped in myelin, an insulating sheath of fatty membrane laid down in many layers by neighboring support cells and interrupted at regular intervals by short bare gaps; most local axons in the cortex are unmyelinated. At its far end the axon branches into terminals that contact other cells.

The inputs are numerous. Megías and colleagues reconstructed pyramidal neurons from the CA1 region of the rat hippocampus and counted about 30,000 excitatory synapses and 1,700 inhibitory ones on a single cell, and a typical neuron in the mouse cortex carries several thousand.[^6] The Purkinje cell of the cerebellum, whose drawing closed Chapter 1, receives on the order of 200,000. Against those thousands of inputs stands one axon. It may branch to reach thousands of targets, but it carries a single signal, the same to every branch. Cajal called this arrangement the law of dynamic polarization: signals enter through the dendrites and soma and leave through the axon, in one direction.[^7]

![Figure 2.2. The polarized plan of a neuron. Thousands of inputs arrive on the dendrites and soma; a single axon, insulated by myelin in long-range axons, carries the one output, decided at the initial segment, to the terminals. Signals travel one way.](images/fig_polarized.png)

Figure 2.2 shows the plan. The many-to-one shape is the first constraint on what a neuron can compute: whatever happens on the dendrites must eventually be reduced to a single decision, made at a single place, about whether and when to fire.

# The Physical Form of Inputs to a Neuron

Neurons receive their inputs at specialized junctions that Charles Sherrington named synapses in 1897, before anyone knew how they worked.[^8] The answer came from a frog's heart. In 1921 Otto Loewi stimulated the vagus nerve of one isolated heart, which slowed its beat, then transferred the fluid that had bathed it to a second heart, which slowed too. Something released by the nerve had carried the message.[^9] That something was a neurotransmitter, and most synapses in the brain work the same way.

At a chemical synapse, an electrical impulse arriving at the axon terminal opens channels that let calcium ions in. The calcium triggers small membrane-bound packets of neurotransmitter, called vesicles, to fuse with the terminal membrane and release their contents into the synaptic cleft, a gap about twenty nanometers wide between the terminal and the receiving cell. The transmitter diffuses across the cleft in a fraction of a millisecond and binds receptors on the membrane of the receiving neuron, and the receptors open ion channels.[^10] Figure 2.3 shows the sequence, including the clearing of transmitter from the cleft by reuptake into cells, enzymatic breakdown, and diffusion away.

![Figure 2.3. A chemical synapse. An action potential arriving at the terminal opens calcium channels; calcium triggers vesicles to release neurotransmitter into the cleft; the transmitter binds receptors on the postsynaptic membrane and produces a small graded potential, then is cleared by reuptake, breakdown, and diffusion.](images/figure_2_3.png)

The point to hold on to is that the immediate input to a neuron is not an electrical spike but a small, local chemical event that produces a graded electrical change, larger or smaller depending on how much transmitter was released and how many receptors received it.[^11] This is what makes the synapse adjustable, and it is why learning, as later sections show, lives mostly at synapses.

Not every synapse is chemical. Some neurons, especially the inhibitory interneurons of the cortex and hippocampus, are also joined by electrical synapses, or gap junctions: protein channels that connect the interiors of two cells directly, so that current flows from one to the other with no transmitter and almost no delay. Barry Connors and Michael Long reviewed the evidence that such coupling is widespread in the mammalian brain, and mice lacking the main neuronal gap-junction protein, connexin 36, show weakened gamma oscillations, the fast rhythm that Chapter 4 describes.[^12] Electrical synapses synchronize; chemical synapses do almost everything else.

# Quanta, Failures, and Noise

The chemical event at a synapse is not a smooth flow but a set of discrete packets, and it is unreliable. Both facts were discovered by Bernard Katz and his colleagues at the junction between nerve and muscle in the frog, the largest and most accessible synapse there is.

In 1952 Paul Fatt and Katz, recording with a fine electrode inside a muscle fiber, saw small depolarizations of about half a millivolt that appeared at random, with no nerve impulse to trigger them. They had the same time course as the full response to a nerve impulse, only much smaller, and curare, which blocks the muscle's receptors for the transmitter acetylcholine, shrank them.[^13] Two years later José del Castillo and Katz lowered the calcium and raised the magnesium in the bath until the nerve impulse released very little transmitter and found that the response to each impulse now fluctuated in steps: sometimes nothing, sometimes one unit the size of the spontaneous event, sometimes two or three. The counts followed the statistics of independent random events. They concluded that transmitter is released in fixed packets, quanta, each almost certainly the contents of one vesicle, and that each impulse releases a random number of them.[^14]

The same randomness governs synapses in the brain, where an impulse often releases one vesicle or none. Chapter 1 described Christopher Allen and Charles Stevens's finding that at single hippocampal synapses more than half of the arriving impulses evoked no response at all. In pairs of connected cortical pyramidal neurons recorded by Henry Markram and his colleagues, the amplitude of the response to a single presynaptic impulse varied from trial to trial so much that its standard deviation was on average about half its mean.[^15] A. Aldo Faisal, Luc Selen, and Daniel Wolpert surveyed the sources of such noise in the nervous system, from the random opening of single ion channels to the random number of vesicles released, and concluded that noise is present at every stage and limits what any single element can do reliably.[^16] The neuron's input is therefore not a clean number but a sample from a distribution, and the cell must make its decisions from many such samples at once.

# Excitatory and Inhibitory Postsynaptic Potentials

Not all synaptic inputs push a neuron toward firing; some do the opposite. When transmitter binds receptors on a dendrite or the soma, it changes the membrane's permeability to particular ions, and the direction of the change determines whether the synapse excites or inhibits.

An excitatory postsynaptic potential (EPSP) slightly depolarizes the membrane, making the inside less negative and moving it closer to the threshold at which an impulse is triggered. EPSPs are produced mostly by glutamate acting on receptors whose channels admit positive ions without much selectivity; sodium flowing in outweighs potassium flowing out, and the net inward current depolarizes the cell.[^17] An inhibitory postsynaptic potential (IPSP) moves the membrane away from threshold or clamps it near rest, usually by opening channels for chloride or potassium ions, and makes firing less likely.[^18] Figure 2.4 shows both, and what happens when they combine.

![Figure 2.4. Excitatory and inhibitory postsynaptic potentials. A: one EPSP depolarizes the membrane. B: one IPSP hyperpolarizes it. C: five EPSPs in quick succession sum to threshold and trigger an action potential. D: an EPSP and an IPSP arriving together nearly cancel. Traces are simulated, not recorded, and the EPSPs are exaggerated for clarity: real ones are a fraction of a millivolt to a few millivolts, and tens are needed to reach threshold.](images/fig_psp.png)

Real synaptic potentials are small. Markram and his colleagues measured the response at the soma of one cortical pyramidal neuron to a single impulse in another and found an average of 1.3 millivolts, ranging from about 0.15 to 5.5 millivolts across connections; Sen Song and his colleagues, recording from hundreds of such pairs, found that most connections were weak and a few strong, with a long-tailed distribution of sizes.[^19] A few millivolts is the exception, a fraction of a millivolt the rule. EPSPs and IPSPs are graded, local, and short-lived, and they fade over tens of milliseconds as charge leaks back across the membrane. The neuron's firing reflects the balance of excitation and inhibition summed across its dendritic tree and soma over time.[^20]

A worked example shows what that summing means. Suppose the membrane rests at −70 millivolts and the threshold for firing is about −55, fifteen millivolts higher. Suppose each excitatory input adds half a millivolt at the soma, and, as a first approximation, that inputs add linearly. Thirty inputs arriving within a couple of milliseconds then sum to fifteen millivolts and fire the cell. Now spread the same thirty inputs evenly across a tenth of a second. Each EPSP decays with a time constant, the time for its size to fall to about a third, which for illustration we take to be twenty milliseconds, so the sum never builds: the average depolarization is the rate of arrival, three inputs every ten milliseconds, times the size of each, times the time constant, or about three millivolts, far below threshold. The same thirty inputs fire the cell when they arrive together and leave it silent when they straggle. Add ten IPSPs of one millivolt each arriving with the burst, and the thirty excitatory inputs are no longer enough; about fifty are needed. Thirty synapses are a tenth of a percent of the 30,000 on a CA1 pyramidal cell. What drives a neuron is not how many of its inputs are active over a long period but how many are active together, and against how much inhibition.

# Dendrites Are Not Passive Cables

The synaptic potentials spread from where they arise, along the dendrites and into the soma. The baseline description of this spread was worked out by Wilfrid Rall, who in 1959 treated a dendrite as an electrical cable: a thin conducting core surrounded by a leaky insulator. In a passive cable, a voltage change shrinks as it travels and is smeared out in time, because charge leaks across the membrane along the way and the membrane's capacitance slows every change.[^21] A synapse at the tip of a long dendrite therefore has much less effect at the soma than the same synapse near it; in a pyramidal neuron a distal input can shrink many times over before it arrives.[^22] Some neurons partly compensate by making their distal synapses stronger, and for small, scattered inputs the passive account is a good approximation of what the dendrite does.[^23]

But dendrites are not passive cables. Their membranes carry voltage-gated channels for sodium, calcium, and potassium, channels that open when the membrane depolarizes, and they carry NMDA receptors, a type of glutamate receptor whose current grows as the membrane depolarizes because depolarization expels a magnesium ion that plugs the channel at rest (Chapter 5 tells that story). With these channels a dendrite can generate its own regenerative events. Jackie Schiller and her colleagues showed in 2000 that when enough neighboring synapses on a thin basal dendrite of a cortical pyramidal neuron are activated together, the branch fires a local NMDA spike, a plateau of depolarization lasting tens of milliseconds and confined to that branch.[^24] Matthew Larkum, Julius Zhu, and Bert Sakmann found that the long apical dendrite of a layer 5 pyramidal neuron has its own zone near the top that fires broad calcium spikes, which drive the axon to fire bursts.[^25] A dendrite, on this evidence, is not a wire that delivers its inputs to the soma but a set of semi-independent compartments, each able to detect when its own inputs coincide and to amplify them.

These dendritic spikes matter for learning. Nace Golding, Nathan Staff, and Nelson Spruston showed that synapses on the far dendrites of hippocampal CA1 neurons, which the cell's own output impulse barely reaches, can be strengthened when cooperative input triggers a local dendritic spike, even when the neuron does not fire at all.[^26] The integration that the earlier sections described is real, but it is done by a structure with active parts.

# The Axon Initial Segment: Where Spikes Begin

All this graded activity converges on one place. Just beyond the soma lies the axon initial segment, the first few tens of micrometers of the axon, and it is packed with voltage-gated sodium channels at a far higher density than the soma or dendrites. Maarten Kole and his colleagues estimated that in cortical pyramidal neurons the sodium-channel density at the initial segment is about fifty times that in the nearby dendrites, and their models could account for where and how the neuron initiates impulses only with such a density.[^27] When the summed depolarization arriving there reaches threshold, about fifteen millivolts above rest, the initial segment fires an action potential. That the impulse starts in the axon rather than the soma was inferred by John Eccles's group from recordings in spinal motor neurons in 1957, and shown directly by Lucy Palmer and Greg Stuart, who used voltage-sensitive dyes to watch the impulse arise in cortical pyramidal neurons and located its origin about 35 micrometers down the axon from the point where it leaves the soma.[^28] Figure 2.5 shows the arrangement.

![Figure 2.5. The axon initial segment. Top: voltage-gated sodium channels are sparse in the soma and densest in the first stretch of axon, which therefore has the lowest threshold. Bottom: the soma's graded sum of inputs (blue) crosses threshold there and the initial segment fires a stereotyped spike (red). Simulated traces.](images/fig_ais.png)

Once initiated, the action potential does not only travel forward. It invades the soma at full amplitude, which is why every electrode in a neuron's cell body records the familiar spike, and from the soma it spreads back into the dendrites. Greg Stuart and Bert Sakmann recorded simultaneously from the soma and from the apical dendrite of the same layer 5 pyramidal neurons in 1994. They found voltage-gated sodium channels in patches of dendritic membrane and showed that the spike appears first in the axon and then actively propagates back into the dendritic tree, carried by the dendrites' own channels rather than merely leaking into them. This is the back-propagating action potential.[^29] Back-propagation weakens with distance and can fail in the finest distal branches, and it is regulated by the dendrite's potassium channels and by inhibition, but over much of the dendritic tree it reports to every synapse that the neuron has just fired.[^30]

That report is what allows a synapse to know whether its input helped. Chapter 5 shows that the back-propagating spike, arriving at a synapse whose NMDA receptors have just bound glutamate, expels their magnesium block and admits the calcium that triggers lasting change. It also couples inputs: Larkum and his colleagues found that one back-propagating spike, coinciding within a few milliseconds with weak input to the far apical dendrite, could trigger a dendritic calcium spike and a burst of output.[^25]

The division of labor is therefore subtler than a simple picture of passive input and active output. Dendrites integrate, mostly linearly for weak input and nonlinearly when inputs cluster; the soma, with a lower density of sodium channels, relays rather than decides; the initial segment decides; and the axon transmits. Evolution separated integration, decision, and transmission into distinct regions while letting the decision travel back to every place where it can be used for learning.

# How the Action Potential Propagates

In 1939 Alan Hodgkin and Andrew Huxley threaded a fine electrode down the inside of a squid's giant axon and measured, for the first time, the voltage across a nerve membrane during an impulse. The inside swung from its negative resting value not merely to zero, as the leading theory of the day predicted, but well past it, to tens of millivolts positive.[^31]

Chapter 1 described how, by 1952, Hodgkin and Huxley had separated the current into its sodium and potassium components and written equations that reproduced the impulse. The mechanism the equations describe is this. When the membrane depolarizes past threshold, voltage-gated sodium channels open within a fraction of a millisecond, sodium ions rush in down their concentration gradient, and the inflow depolarizes the membrane further, which opens more sodium channels. This positive feedback drives the inside to about +40 millivolts. Within a millisecond the sodium channels close of their own accord, a process called inactivation, while slower voltage-gated potassium channels open and let potassium flow out, returning the membrane to rest and briefly below it. For a millisecond or two afterward the inactivated sodium channels cannot reopen, and the membrane cannot fire again; this refractory period limits a neuron to a few hundred impulses per second at most.[^32] The ions exchanged are a tiny fraction of those in the cell, and the pumps restore the balance later, at the cost of ATP.

Propagation follows from the same mechanism. Sodium entering at the active patch of membrane spreads inside the axon and depolarizes the patch ahead of it to threshold, which then fires, injecting its own current further along. The patch behind is refractory and cannot fire again, so the impulse travels in one direction only. Each patch regenerates the impulse from its own ion gradients, so the impulse arrives at the far end of a meter-long axon as large as it started. No particle travels the length of the axon; what travels is a pattern of channel openings, each triggered by the one before.

![Figure 2.6. How the action potential travels. A: in a bare axon, sodium entering the active patch spreads inside and brings the next patch to threshold, while the patch behind is refractory; the spike is regenerated at every point. B: in a myelinated axon, channels are confined to the nodes and the spike jumps from node to node (saltatory conduction).](images/fig_propagation.png)

Figure 2.6 shows both forms of propagation. In a bare axon the impulse creeps, at speeds of the order of a meter per second in thin fibers. Myelin changes this. Because the insulating sheath prevents current from leaking out and reduces the charge needed to change the voltage, the current from one bare gap, or node, can bring the next node, up to a millimeter or so away, to threshold, and sodium channels are concentrated at the nodes. The impulse jumps from node to node, a mode of conduction called saltatory, from the Latin for leaping. Andrew Huxley and Robert Stämpfli demonstrated it in 1949 by measuring the currents around single frog nerve fibers along their length and showing that excitation passes from node to node, skipping the insulated stretches between.[^33] The fastest myelinated axons conduct at around 100 meters per second, against about a meter per second for thin unmyelinated fibers, and at a lower metabolic cost, since only the nodes exchange ions.[^34]

# Rate, Timing, and the All-or-None Spike

If every action potential is the same size, how does a neuron say more or less? Edgar Adrian answered the question in 1926 with Yngve Zotterman. Working with a small muscle of the frog, they cut away tissue until the nerve carried impulses from a single stretch receptor, then hung weights from the muscle. Each impulse was the same size whatever the weight. A heavier weight produced impulses at a higher frequency, and a sustained weight produced a frequency that declined over seconds as the receptor adapted.[^35] The message was carried by the number of impulses per second, not by their size. Adrian generalized the finding across sense organs, and firing rate has been the default currency of neural coding ever since. Figure 2.7A shows the principle: a stronger stimulus produces more spikes, not larger ones.

![Figure 2.7. Spikes are all the same size. A: a stronger stimulus produces more spikes, not larger ones. B: the same number of spikes arranged as bursts carries a different message. Information lies in rate and timing. Simulated traces.](images/fig_timing.png)

The all-or-none rule needs one qualification. Action potentials are stereotyped, and their presence rather than their size is the message, but small variations in their shape do modulate what they release. In hippocampal mossy fibers, Jörg Geiger and Peter Jonas found that the impulse in the axon terminal broadens up to threefold during high-frequency firing, letting more calcium in and releasing more transmitter. Henrik Alle and Geiger, and separately Yousheng Shu, David McCormick, and their colleagues in cortex, showed that subthreshold voltage changes at the soma spread hundreds of micrometers down the axon and change how much transmitter each subsequent spike releases.[^36] The axon carries a mainly digital signal with an analog component riding on it.

Rate is also not the only code. Figure 2.7B shows the same number of spikes arranged as bursts, which a downstream neuron with the summing properties described above would read differently from evenly spaced spikes. Zachary Mainen and Terrence Sejnowski showed in 1995 that cortical neurons can time their spikes precisely: driven by a constant current, a neuron in a brain slice fired at slightly different times on each trial, but driven by a fluctuating current resembling real synaptic input, it fired at times reproducible to within a millisecond from trial to trial.[^37] Speed argues the same way. In Simon Thorpe's experiment of Chapter 1, brain signals distinguishing photographs with and without an animal appeared about 150 milliseconds after a twenty-millisecond flash.[^38] If that signal passes through something like ten stages of processing between the eye and the decision, each stage has roughly fifteen milliseconds, time enough for a neuron firing at typical rates to emit one spike or none. A code that required counting spikes over long windows could not work at that speed. Information is carried by the rate of firing, by the timing of spikes, and by which neurons fire together, and how the brain weighs these in each circuit is an active research question.[^39]

# Plasticity: Learning as Physical Change

Synapses strengthen or weaken with use. Donald Hebb proposed in 1949 that when one cell repeatedly takes part in firing another, some growth process or metabolic change makes the connection more effective, and in 1973 Timothy Bliss and Terje Lømo found such a change in the hippocampus of anesthetized rabbits: brief high-frequency trains of impulses in the input pathway left the response of the receiving cells enlarged for hours afterward, a phenomenon now called long-term potentiation, or LTP.[^40]

What changes is physical. A strengthened synapse can release more transmitter per impulse, can have more receptors in its membrane, and can sit on a larger spine, the small protrusion from the dendrite that carries most excitatory synapses in the cortex. Masanori Matsuzaki, Haruo Kasai, and their colleagues released glutamate onto single spines with flashes of light and showed that the stimulation that potentiates a synapse also enlarges its spine, and that in small spines the enlargement persists for more than an hour.[^41] Figure 2.8 shows the before and after: more docked vesicles, a larger spine head, more receptors, and an EPSP that more than doubles.

![Figure 2.8. Learning as physical change. Before: a weak synapse with fewer docked vesicles and few receptors gives a small EPSP. After repeated correlated activity, the same synapse holds more docked vesicles, a larger spine head, and more receptors, and the EPSP more than doubles. Simulated traces.](images/fig_plasticity.png)

This is the sense in which learning is physical. Storage in the brain is physical and distributed, held in the strengths and structure of many synapses, and there is no separate memory in which records sit apart from the machinery that uses them. The synapse that encodes a past experience is the same synapse that transmits the next impulse, so every use of the memory runs through the stored change and may alter it. Chapter 5 develops this account, from the molecular steps of potentiation to the reasons it makes memory reconstructive.

# Why Neurons Look Inefficient, and Why They Are Not

Judged as switching elements, neurons are slow, noisy, and expensive. An action potential lasts about a millisecond; a transistor in a modern processor switches in roughly a hundred picoseconds, ten million times faster. A synapse fails more often than it succeeds at many connections, and the same stimulus never produces exactly the same spikes twice. Faisal, John White, and Laughlin calculated that axons thinner than about a tenth of a micrometer would be unusable, because the random opening of single sodium channels would fire spontaneous impulses often enough to drown the real ones; the thinnest axons found in brains sit just above that limit, so noise sets a floor on how small the wiring can be.[^42] And the brain is about two percent of the body's mass but uses about twenty percent of its resting energy, most of it, by Attwell and Laughlin's estimate, on signaling itself: their budget predicts that a cortex paying these costs can afford to have no more than about fifteen percent of its neurons active at the same time, and Peter Lennie's later calculation, described in Chapter 1, puts the affordable fraction nearer one in a hundred.[^43] Figure 2.9 summarizes the three costs.

![Figure 2.9. Slow, noisy, and expensive. A: a spike lasts about a millisecond, ten million times longer than a transistor switch of about 100 picoseconds. B: the same stimulus gives a different spike pattern on every trial (simulated raster). C: the brain is about 2 percent of body mass but uses about 20 percent of resting energy.](images/fig_costs.png)

The slowness and noise are tolerable because the brain computes with populations rather than single cells. Thirty unreliable synapses that must coincide to fire a neuron, as in the worked example above, amount to a vote, and a vote among many noisy voters is reliable even when each voter is not. Slowness is offset by parallelism: billions of neurons each doing a little at once. The expense buys something no transistor has, a signaling element that can rewire itself while it works. Peter Sterling and Simon Laughlin argue, as Chapter 1 noted, that under these constraints neural design is close to efficient, with neurons firing sparsely because every spike is paid for.[^44] What looks like inefficiency is the shape of a good solution to a different problem from the one a computer solves.

# A Neuron in Context

The account so far has treated a neuron's response as fixed by its inputs and its synapses, but the same neuron, with the same wiring and the same input, can respond quite differently depending on the chemical setting it is in. Figure 2.10 shows the same neuron answering the same train of input spikes with three spikes in one chemical setting and eleven in another; the difference comes from substances such as dopamine, acetylcholine, and norepinephrine that are released widely and change how neurons fire and how their synapses learn.

![Figure 2.10. The same input, a different output. With no neuromodulator present the neuron responds to a train of input spikes with three spikes; with a neuromodulator present it responds with eleven. The wiring has not changed. Chapter 3 explains how chemical context does this. Schematic, not data.](images/fig_context.png)

Those substances are the neuromodulators, and they are the subject of the next chapter. They decide much of when the physical changes described above are made and kept, and they turn one circuit into many.

# Implications for Artificial Intelligence

The artificial neuron began as a deliberate simplification of the one described in this chapter. Warren McCulloch and Walter Pitts proposed in 1943 a unit that sums its weighted inputs and fires if the sum exceeds a threshold, and showed that networks of such units could compute any logical function.[^45] The units of modern deep networks are its descendants: a weighted sum followed by a smooth nonlinearity. Several of this chapter's findings bear on how far that simplification reaches.

First, a biological neuron is not a single unit but a small network. Panayiota Poirazi, Bartlett Mel, and a colleague found that the firing of a detailed model of a hippocampal pyramidal neuron was well predicted by a two-layer network, in which each thin dendritic branch acts as a separate nonlinear subunit and the soma sums their outputs. David Beniaguev, Idan Segev, and Michael London went further and trained deep networks to reproduce, millisecond by millisecond, the output of a detailed model of a cortical pyramidal neuron; they needed a network five to eight layers deep, and when they removed the model's NMDA receptors a network with a single hidden layer sufficed.[^46] Albert Gidon, Matthew Larkum, and their colleagues found that dendrites of human cortical neurons produce a kind of calcium spike whose amplitude is largest for inputs just above threshold and smaller for stronger ones, which lets a single neuron compute exclusive-or, a function that a single artificial unit cannot compute.[^47] If one cortical neuron is worth a small deep network, comparing brains and models by counting units understates what the brain's units do.

Second, the brain communicates with sparse, all-or-none events whose cost scales with how many are sent, while a conventional artificial network computes every unit on every step. As hardware becomes power-limited, the energy figures above are a reason to take event-driven, spiking computation seriously.

Third, biological components are unreliable, and the system is robust anyway. Dropout, a training technique that randomly silences units, makes artificial networks generalize better.[^48] Synaptic failure may serve the brain in a related way, by keeping any one pathway from becoming indispensable, though this is an analogy, not an established equivalence.

Finally, the brain and artificial networks both store what they learn in connection weights, so the difference is not where knowledge is kept but how it changes. In an artificial network, weights are changed by a separate training procedure and are fixed when the network is used, unless it is trained online. In the brain, synapses are adjusted during use, by rules that depend on signals available at the synapse itself, among them the back-propagating spike that tells it whether the neuron fired. How such local rules add up to learning that serves the whole organism is a central question for both fields.

# The Central Lesson

A neuron is a living cell that turns many small, noisy, chemical inputs into one all-or-none electrical output, and changes its own connections in the process. Its dendrites integrate actively rather than passively, its axon initial segment makes the decision, its spike travels forward to other cells and back to its own synapses, and every step is paid for in energy and limited by noise. These physical facts are not implementation details beneath the level of computation; they define what a neuron can compute, how fast, at what cost, and how it learns.

# Next Chapter

Chapter 3: Neuromodulation: How Chemical Context Shapes Learning and Behavior

# References and Attribution

## Figure Attribution

Figures 2.1, 2.2, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, and 2.10 were drawn for this book. The voltage traces in Figures 2.4, 2.5, 2.7, and 2.8 and the spike raster in Figure 2.9 are illustrative simulations, not recorded data; the EPSP amplitudes in Figure 2.4 are exaggerated for clarity. Figure 2.10 is a schematic.

Figure 2.3: the chemical synapse figure from *Anatomy and Physiology* by OpenStax (Rice University), licensed CC BY 4.0, via openstax.org.

## Epigraph

Santiago Ramón y Cajal, *Recollections of My Life*, trans. E. Horne Craigie with the assistance of Juan Cano (American Philosophical Society, 1937; reprinted MIT Press, 1989), p. 363 of the MIT Press edition. Cajal's autobiography *Recuerdos de mi vida* was published in Spanish in 1901–1917.

## References

Adrian, E. D. (1928). *The Basis of Sensation: The Action of the Sense Organs*. Christophers.

Adrian, E. D., & Zotterman, Y. (1926). The impulses produced by sensory nerve-endings: Part II. The response of a single end-organ. *Journal of Physiology*, 61(2), 151–171.

Alberts, B., Johnson, A., Lewis, J., Morgan, D., Raff, M., Roberts, K., & Walter, P. (2015). *Molecular Biology of the Cell* (6th ed.). Garland Science.

Alle, H., & Geiger, J. R. P. (2006). Combined analog and action potential coding in hippocampal mossy fibers. *Science*, 311(5765), 1290–1293.

Allen, C., & Stevens, C. F. (1994). An evaluation of causes for unreliability of synaptic transmission. *Proceedings of the National Academy of Sciences*, 91(22), 10380–10383.

Attwell, D., & Laughlin, S. B. (2001). An energy budget for signaling in the grey matter of the brain. *Journal of Cerebral Blood Flow & Metabolism*, 21(10), 1133–1145.

Beniaguev, D., Segev, I., & London, M. (2021). Single cortical neurons as deep artificial neural networks. *Neuron*, 109(17), 2727–2739.

Bliss, T. V. P., & Lømo, T. (1973). Long-lasting potentiation of synaptic transmission in the dentate area of the anaesthetized rabbit following stimulation of the perforant path. *Journal of Physiology*, 232(2), 331–356.

Braitenberg, V., & Schüz, A. (1998). *Cortex: Statistics and Geometry of Neuronal Connectivity* (2nd ed.). Springer.

Connors, B. W., & Long, M. A. (2004). Electrical synapses in the mammalian brain. *Annual Review of Neuroscience*, 27, 393–418.

Coombs, J. S., Curtis, D. R., & Eccles, J. C. (1957). The generation of impulses in motoneurones. *Journal of Physiology*, 139(2), 232–249.

Coombs, J. S., Eccles, J. C., & Fatt, P. (1955). The specific ionic conductances and the ionic movements across the motoneuronal membrane that produce the inhibitory post-synaptic potential. *Journal of Physiology*, 130(2), 326–374.

del Castillo, J., & Katz, B. (1954). Quantal components of the end-plate potential. *Journal of Physiology*, 124(3), 560–573.

Eccles, J. C. (1964). *The Physiology of Synapses*. Springer.

Faisal, A. A., Selen, L. P. J., & Wolpert, D. M. (2008). Noise in the nervous system. *Nature Reviews Neuroscience*, 9(4), 292–303.

Faisal, A. A., White, J. A., & Laughlin, S. B. (2005). Ion-channel noise places limits on the miniaturization of the brain's wiring. *Current Biology*, 15(12), 1143–1149.

Fatt, P., & Katz, B. (1951). An analysis of the end-plate potential recorded with an intra-cellular electrode. *Journal of Physiology*, 115(3), 320–370.

Fatt, P., & Katz, B. (1952). Spontaneous subthreshold activity at motor nerve endings. *Journal of Physiology*, 117(1), 109–128.

Foster, M., & Sherrington, C. S. (1897). *A Textbook of Physiology, Part III: The Central Nervous System* (7th ed.). Macmillan.

Geiger, J. R. P., & Jonas, P. (2000). Dynamic control of presynaptic Ca2+ inflow by fast-inactivating K+ channels in hippocampal mossy fiber boutons. *Neuron*, 28(3), 927–939.

Gidon, A., Zolnik, T. A., Fidzinski, P., Bolduan, F., Papoutsi, A., Poirazi, P., Holtkamp, M., Vida, I., & Larkum, M. E. (2020). Dendritic action potentials and computation in human layer 2/3 cortical neurons. *Science*, 367(6473), 83–87.

Golding, N. L., Staff, N. P., & Spruston, N. (2002). Dendritic spikes as a mechanism for cooperative long-term potentiation. *Nature*, 418(6895), 326–331.

Hebb, D. O. (1949). *The Organization of Behavior: A Neuropsychological Theory*. Wiley.

Hodgkin, A. L. (1964). *The Conduction of the Nervous Impulse*. Liverpool University Press.

Hodgkin, A. L., & Huxley, A. F. (1939). Action potentials recorded from inside a nerve fibre. *Nature*, 144, 710–711.

Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. *Journal of Physiology*, 117(4), 500–544.

Hormuzdi, S. G., Pais, I., LeBeau, F. E. N., Towers, S. K., Rozov, A., Buhl, E. H., Whittington, M. A., & Monyer, H. (2001). Impaired electrical signaling disrupts gamma frequency oscillations in connexin 36-deficient mice. *Neuron*, 31(3), 487–495.

Huxley, A. F., & Stämpfli, R. (1949). Evidence for saltatory conduction in peripheral myelinated nerve fibres. *Journal of Physiology*, 108(3), 315–339.

Kandel, E. R., Koester, J. D., Mack, S. H., & Siegelbaum, S. A. (Eds.). (2021). *Principles of Neural Science* (6th ed.). McGraw-Hill.

Katz, B. (1969). *The Release of Neural Transmitter Substances*. Liverpool University Press.

Kole, M. H. P., Ilschner, S. U., Kampa, B. M., Williams, S. R., Ruben, P. C., & Stuart, G. J. (2008). Action potential generation requires a high sodium channel density in the axon initial segment. *Nature Neuroscience*, 11(2), 178–186.

Larkum, M. E., Zhu, J. J., & Sakmann, B. (1999). A new cellular mechanism for coupling inputs arriving at different cortical layers. *Nature*, 398(6725), 338–341.

Lennie, P. (2003). The cost of cortical computation. *Current Biology*, 13(6), 493–497.

Loewi, O. (1921). Über humorale Übertragbarkeit der Herznervenwirkung. *Pflügers Archiv für die gesamte Physiologie*, 189, 239–242.

London, M., & Häusser, M. (2005). Dendritic computation. *Annual Review of Neuroscience*, 28, 503–532.

Magee, J. C. (2000). Dendritic integration of excitatory synaptic input. *Nature Reviews Neuroscience*, 1(3), 181–190.

Mainen, Z. F., & Sejnowski, T. J. (1995). Reliability of spike timing in neocortical neurons. *Science*, 268(5216), 1503–1506.

Markram, H., Lübke, J., Frotscher, M., Roth, A., & Sakmann, B. (1997). Physiology and anatomy of synaptic connections between thick tufted pyramidal neurones in the developing rat neocortex. *Journal of Physiology*, 500(2), 409–440.

Marr, D. (1982). *Vision: A Computational Investigation into the Human Representation and Processing of Visual Information*. W. H. Freeman.

Matsuzaki, M., Honkura, N., Ellis-Davies, G. C. R., & Kasai, H. (2004). Structural basis of long-term potentiation in single dendritic spines. *Nature*, 429, 761–766.

McCulloch, W. S., & Pitts, W. (1943). A logical calculus of the ideas immanent in nervous activity. *Bulletin of Mathematical Biophysics*, 5(4), 115–133.

Megías, M., Emri, Z., Freund, T. F., & Gulyás, A. I. (2001). Total number and distribution of inhibitory and excitatory synapses on hippocampal CA1 pyramidal cells. *Neuroscience*, 102(3), 527–540.

Palmer, L. M., & Stuart, G. J. (2006). Site of action potential initiation in layer 5 pyramidal neurons. *Journal of Neuroscience*, 26(6), 1854–1863.

Poirazi, P., Brannon, T., & Mel, B. W. (2003). Pyramidal neuron as two-layer neural network. *Neuron*, 37(6), 989–999.

Raichle, M. E., & Gusnard, D. A. (2002). Appraising the brain's energy budget. *Proceedings of the National Academy of Sciences*, 99(16), 10237–10239.

Rall, W. (1959). Branching dendritic trees and motoneuron membrane resistivity. *Experimental Neurology*, 1(5), 491–527.

Ramón y Cajal, S. (1909–1911). *Histologie du système nerveux de l'homme et des vertébrés* (2 vols., trans. L. Azoulay). Paris: Maloine.

Rieke, F., Warland, D., de Ruyter van Steveninck, R., & Bialek, W. (1997). *Spikes: Exploring the Neural Code*. MIT Press.

Schiller, J., Major, G., Koester, H. J., & Schiller, Y. (2000). NMDA spikes in basal dendrites of cortical pyramidal neurons. *Nature*, 404(6775), 285–289.

Shepherd, G. M. (1991). *Foundations of the Neuron Doctrine*. Oxford University Press.

Shu, Y., Hasenstaub, A., Duque, A., Yu, Y., & McCormick, D. A. (2006). Modulation of intracortical synaptic potentials by presynaptic somatic membrane potential. *Nature*, 441(7094), 761–765.

Song, S., Sjöström, P. J., Reigl, M., Nelson, S. B., & Chklovskii, D. B. (2005). Highly nonrandom features of synaptic connectivity in local cortical circuits. *PLoS Biology*, 3(3), e68.

Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014). Dropout: A simple way to prevent neural networks from overfitting. *Journal of Machine Learning Research*, 15, 1929–1958.

Sterling, P., & Laughlin, S. (2015). *Principles of Neural Design*. MIT Press.

Stuart, G. J., & Sakmann, B. (1994). Active propagation of somatic action potentials into neocortical pyramidal cell dendrites. *Nature*, 367, 69–72.

Stuart, G., Spruston, N., Sakmann, B., & Häusser, M. (1997). Action potential initiation and backpropagation in neurons of the mammalian CNS. *Trends in Neurosciences*, 20(3), 125–131.

Thorpe, S., Fize, D., & Marlot, C. (1996). Speed of processing in the human visual system. *Nature*, 381(6582), 520–522.

Waldeyer, W. (1891). Ueber einige neuere Forschungen im Gebiete der Anatomie des Centralnervensystems. *Deutsche medicinische Wochenschrift*, 17, 1213–1218, 1244–1246, 1267–1269, 1287–1289, 1331–1332, 1352–1356.

[^1]: Waldeyer, W. (1891). Ueber einige neuere Forschungen im Gebiete der Anatomie des Centralnervensystems. *Deutsche medicinische Wochenschrift*, 17, 1213–1218, 1244–1246, 1267–1269, 1287–1289, 1331–1332, 1352–1356; Ramón y Cajal, S. (1909–1911). *Histologie du système nerveux de l'homme et des vertébrés* (2 vols., trans. L. Azoulay). Paris: Maloine; Shepherd, G. M. (1991). *Foundations of the Neuron Doctrine*. Oxford University Press. The word "neuron" was introduced by Waldeyer in 1891; the doctrine that the nervous system is built of discrete cells rests chiefly on Cajal's histology.

[^2]: Marr, D. (1982). *Vision: A Computational Investigation into the Human Representation and Processing of Visual Information*. W. H. Freeman.

[^3]: Alberts, B., Johnson, A., Lewis, J., Morgan, D., Raff, M., Roberts, K., & Walter, P. (2015). *Molecular Biology of the Cell* (6th ed.). Garland Science. The pump moves three sodium ions out and two potassium ions in for each ATP molecule it consumes.

[^4]: Attwell, D., & Laughlin, S. B. (2001). An energy budget for signaling in the grey matter of the brain. *Journal of Cerebral Blood Flow & Metabolism*, 21(10), 1133–1145.

[^5]: Kandel, E. R., Koester, J. D., Mack, S. H., & Siegelbaum, S. A. (Eds.). (2021). *Principles of Neural Science* (6th ed.). McGraw-Hill.

[^6]: Megías, M., Emri, Z., Freund, T. F., & Gulyás, A. I. (2001). Total number and distribution of inhibitory and excitatory synapses on hippocampal CA1 pyramidal cells. *Neuroscience*, 102(3), 527–540; Braitenberg, V., & Schüz, A. (1998). *Cortex: Statistics and Geometry of Neuronal Connectivity* (2nd ed.). Springer. A rat hippocampal CA1 pyramidal cell carries roughly 30,000 excitatory and 1,700 inhibitory synapses.

[^7]: Ramón y Cajal, S. (1909–1911). *Histologie du système nerveux de l'homme et des vertébrés* (2 vols., trans. L. Azoulay). Paris: Maloine. Cajal's "law of dynamic polarization."

[^8]: Foster, M., & Sherrington, C. S. (1897). *A Textbook of Physiology, Part III: The Central Nervous System* (7th ed.). Macmillan. The term was coined by Sherrington.

[^9]: Loewi, O. (1921). Über humorale Übertragbarkeit der Herznervenwirkung. *Pflügers Archiv für die gesamte Physiologie*, 189, 239–242.

[^10]: Katz, B. (1969). *The Release of Neural Transmitter Substances*. Liverpool University Press; Kandel, E. R., Koester, J. D., Mack, S. H., & Siegelbaum, S. A. (Eds.). (2021). *Principles of Neural Science* (6th ed.). McGraw-Hill. The synaptic cleft is about 20 nanometers wide.

[^11]: Fatt, P., & Katz, B. (1951). An analysis of the end-plate potential recorded with an intra-cellular electrode. *Journal of Physiology*, 115(3), 320–370.

[^12]: Connors, B. W., & Long, M. A. (2004). Electrical synapses in the mammalian brain. *Annual Review of Neuroscience*, 27, 393–418; Hormuzdi, S. G., Pais, I., LeBeau, F. E. N., Towers, S. K., Rozov, A., Buhl, E. H., Whittington, M. A., & Monyer, H. (2001). Impaired electrical signaling disrupts gamma frequency oscillations in connexin 36-deficient mice. *Neuron*, 31(3), 487–495.

[^13]: Fatt, P., & Katz, B. (1952). Spontaneous subthreshold activity at motor nerve endings. *Journal of Physiology*, 117(1), 109–128.

[^14]: del Castillo, J., & Katz, B. (1954). Quantal components of the end-plate potential. *Journal of Physiology*, 124(3), 560–573; Katz, B. (1969). *The Release of Neural Transmitter Substances*. Liverpool University Press.

[^15]: Allen, C., & Stevens, C. F. (1994). An evaluation of causes for unreliability of synaptic transmission. *Proceedings of the National Academy of Sciences*, 91(22), 10380–10383; Markram, H., Lübke, J., Frotscher, M., Roth, A., & Sakmann, B. (1997). Physiology and anatomy of synaptic connections between thick tufted pyramidal neurones in the developing rat neocortex. *Journal of Physiology*, 500(2), 409–440. In Markram and colleagues' recordings the coefficient of variation of unitary EPSP amplitude averaged 0.52.

[^16]: Faisal, A. A., Selen, L. P. J., & Wolpert, D. M. (2008). Noise in the nervous system. *Nature Reviews Neuroscience*, 9(4), 292–303.

[^17]: Eccles, J. C. (1964). *The Physiology of Synapses*. Springer.

[^18]: Coombs, J. S., Eccles, J. C., & Fatt, P. (1955). The specific ionic conductances and the ionic movements across the motoneuronal membrane that produce the inhibitory post-synaptic potential. *Journal of Physiology*, 130(2), 326–374.

[^19]: Markram, H., Lübke, J., Frotscher, M., Roth, A., & Sakmann, B. (1997). Physiology and anatomy of synaptic connections between thick tufted pyramidal neurones in the developing rat neocortex. *Journal of Physiology*, 500(2), 409–440; Song, S., Sjöström, P. J., Reigl, M., Nelson, S. B., & Chklovskii, D. B. (2005). Highly nonrandom features of synaptic connectivity in local cortical circuits. *PLoS Biology*, 3(3), e68.

[^20]: Magee, J. C. (2000). Dendritic integration of excitatory synaptic input. *Nature Reviews Neuroscience*, 1(3), 181–190.

[^21]: Rall, W. (1959). Branching dendritic trees and motoneuron membrane resistivity. *Experimental Neurology*, 1(5), 491–527.

[^22]: London, M., & Häusser, M. (2005). Dendritic computation. *Annual Review of Neuroscience*, 28, 503–532.

[^23]: Magee, J. C. (2000). Dendritic integration of excitatory synaptic input. *Nature Reviews Neuroscience*, 1(3), 181–190.

[^24]: Schiller, J., Major, G., Koester, H. J., & Schiller, Y. (2000). NMDA spikes in basal dendrites of cortical pyramidal neurons. *Nature*, 404(6775), 285–289; London, M., & Häusser, M. (2005). Dendritic computation. *Annual Review of Neuroscience*, 28, 503–532.

[^25]: Larkum, M. E., Zhu, J. J., & Sakmann, B. (1999). A new cellular mechanism for coupling inputs arriving at different cortical layers. *Nature*, 398(6725), 338–341.

[^26]: Golding, N. L., Staff, N. P., & Spruston, N. (2002). Dendritic spikes as a mechanism for cooperative long-term potentiation. *Nature*, 418(6895), 326–331.

[^27]: Kole, M. H. P., Ilschner, S. U., Kampa, B. M., Williams, S. R., Ruben, P. C., & Stuart, G. J. (2008). Action potential generation requires a high sodium channel density in the axon initial segment. *Nature Neuroscience*, 11(2), 178–186.

[^28]: Coombs, J. S., Curtis, D. R., & Eccles, J. C. (1957). The generation of impulses in motoneurones. *Journal of Physiology*, 139(2), 232–249; Palmer, L. M., & Stuart, G. J. (2006). Site of action potential initiation in layer 5 pyramidal neurons. *Journal of Neuroscience*, 26(6), 1854–1863.

[^29]: Stuart, G. J., & Sakmann, B. (1994). Active propagation of somatic action potentials into neocortical pyramidal cell dendrites. *Nature*, 367, 69–72.

[^30]: Stuart, G., Spruston, N., Sakmann, B., & Häusser, M. (1997). Action potential initiation and backpropagation in neurons of the mammalian CNS. *Trends in Neurosciences*, 20(3), 125–131; Golding, N. L., Staff, N. P., & Spruston, N. (2002). Dendritic spikes as a mechanism for cooperative long-term potentiation. *Nature*, 418(6895), 326–331.

[^31]: Hodgkin, A. L., & Huxley, A. F. (1939). Action potentials recorded from inside a nerve fibre. *Nature*, 144, 710–711.

[^32]: Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. *Journal of Physiology*, 117(4), 500–544; Hodgkin, A. L. (1964). *The Conduction of the Nervous Impulse*. Liverpool University Press; Kandel, E. R., Koester, J. D., Mack, S. H., & Siegelbaum, S. A. (Eds.). (2021). *Principles of Neural Science* (6th ed.). McGraw-Hill.

[^33]: Huxley, A. F., & Stämpfli, R. (1949). Evidence for saltatory conduction in peripheral myelinated nerve fibres. *Journal of Physiology*, 108(3), 315–339.

[^34]: Kandel, E. R., Koester, J. D., Mack, S. H., & Siegelbaum, S. A. (Eds.). (2021). *Principles of Neural Science* (6th ed.). McGraw-Hill.

[^35]: Adrian, E. D., & Zotterman, Y. (1926). The impulses produced by sensory nerve-endings: Part II. The response of a single end-organ. *Journal of Physiology*, 61(2), 151–171; Adrian, E. D. (1928). *The Basis of Sensation: The Action of the Sense Organs*. Christophers.

[^36]: Geiger, J. R. P., & Jonas, P. (2000). Dynamic control of presynaptic Ca2+ inflow by fast-inactivating K+ channels in hippocampal mossy fiber boutons. *Neuron*, 28(3), 927–939; Alle, H., & Geiger, J. R. P. (2006). Combined analog and action potential coding in hippocampal mossy fibers. *Science*, 311(5765), 1290–1293; Shu, Y., Hasenstaub, A., Duque, A., Yu, Y., & McCormick, D. A. (2006). Modulation of intracortical synaptic potentials by presynaptic somatic membrane potential. *Nature*, 441(7094), 761–765.

[^37]: Mainen, Z. F., & Sejnowski, T. J. (1995). Reliability of spike timing in neocortical neurons. *Science*, 268(5216), 1503–1506.

[^38]: Thorpe, S., Fize, D., & Marlot, C. (1996). Speed of processing in the human visual system. *Nature*, 381(6582), 520–522.

[^39]: Rieke, F., Warland, D., de Ruyter van Steveninck, R., & Bialek, W. (1997). *Spikes: Exploring the Neural Code*. MIT Press.

[^40]: Hebb, D. O. (1949). *The Organization of Behavior: A Neuropsychological Theory*. Wiley; Bliss, T. V. P., & Lømo, T. (1973). Long-lasting potentiation of synaptic transmission in the dentate area of the anaesthetized rabbit following stimulation of the perforant path. *Journal of Physiology*, 232(2), 331–356.

[^41]: Matsuzaki, M., Honkura, N., Ellis-Davies, G. C. R., & Kasai, H. (2004). Structural basis of long-term potentiation in single dendritic spines. *Nature*, 429, 761–766.

[^42]: Faisal, A. A., White, J. A., & Laughlin, S. B. (2005). Ion-channel noise places limits on the miniaturization of the brain's wiring. *Current Biology*, 15(12), 1143–1149.

[^43]: Raichle, M. E., & Gusnard, D. A. (2002). Appraising the brain's energy budget. *Proceedings of the National Academy of Sciences*, 99(16), 10237–10239; Attwell, D., & Laughlin, S. B. (2001). An energy budget for signaling in the grey matter of the brain. *Journal of Cerebral Blood Flow & Metabolism*, 21(10), 1133–1145; Lennie, P. (2003). The cost of cortical computation. *Current Biology*, 13(6), 493–497.

[^44]: Sterling, P., & Laughlin, S. (2015). *Principles of Neural Design*. MIT Press.

[^45]: McCulloch, W. S., & Pitts, W. (1943). A logical calculus of the ideas immanent in nervous activity. *Bulletin of Mathematical Biophysics*, 5(4), 115–133.

[^46]: Poirazi, P., Brannon, T., & Mel, B. W. (2003). Pyramidal neuron as two-layer neural network. *Neuron*, 37(6), 989–999; Beniaguev, D., Segev, I., & London, M. (2021). Single cortical neurons as deep artificial neural networks. *Neuron*, 109(17), 2727–2739.

[^47]: Gidon, A., Zolnik, T. A., Fidzinski, P., Bolduan, F., Papoutsi, A., Poirazi, P., Holtkamp, M., Vida, I., & Larkum, M. E. (2020). Dendritic action potentials and computation in human layer 2/3 cortical neurons. *Science*, 367(6473), 83–87.

[^48]: Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014). Dropout: A simple way to prevent neural networks from overfitting. *Journal of Machine Learning Research*, 15, 1929–1958.
