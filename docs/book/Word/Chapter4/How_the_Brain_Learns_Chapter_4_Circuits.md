---
title: "Chapter 4"
subtitle: "Circuits, Networks, and Coordinated Behavior"
---

> *"Swiftly the head mass becomes an enchanted loom where millions of flashing shuttles weave a dissolving pattern, always a meaningful pattern though never an abiding one; a shifting harmony of subpatterns."*
>
> --- Charles Sherrington, *Man on His Nature* (1940)

# From Cells to Circuits

The previous chapters built a neuron and then surrounded it with chemical context. A neuron integrates inputs, fires when a threshold is crossed, and changes physically with use, and neuromodulators decide how much of that change is kept. That account is complete at the level of the cell. It explains almost nothing about behavior.

A single neuron cannot walk, breathe, decide, or remember. It cannot even compute a difference between two inputs in a way that outlasts the inputs themselves. Every capacity that we recognize as behavior belongs to groups of neurons connected in particular ways. The unit of function in the nervous system is not the neuron. It is the circuit.

This creates a problem of description. The human brain contains about 86 billion neurons and, in the neocortex alone, about 164 trillion synapses.[^1] No account at the level of individual connections is possible, and none would be illuminating if it were. What makes circuits intelligible is that the nervous system reuses a small number of wiring patterns, at every scale, in every region. Learn the patterns and the regions become variations on a theme.

This chapter is about those patterns, the ways they are stacked into larger structures, and the rhythms that coordinate them. It ends where Chapter 1 began: with a system that produces coordinated behavior without anyone in charge.

# The Simplest Circuit

Sherrington's reflex arc remains the clearest place to start. A sensory neuron in a muscle spindle detects stretch. Its axon enters the spinal cord and synapses directly on a motor neuron, which contracts the same muscle. Tap the tendon below the kneecap: the quadriceps stretches and the leg kicks. Two neurons, one synapse, no brain required.[^2]

Even this minimal circuit contains a second element that is easy to overlook. The same sensory axon also excites an inhibitory interneuron, which suppresses the motor neurons of the opposing muscles. The quadriceps contracts while the hamstrings are actively prevented from resisting. This is reciprocal inhibition, and it is the first lesson of circuit organization: useful behavior requires turning things off as much as turning them on.[^3]

Reflexes are not primitive leftovers. They are the fastest and most reliable components of the motor system, and nearly everything the brain does with movement is built by modulating them.

# A Small Vocabulary of Motifs

Across the nervous system, a handful of wiring motifs recur. Figure 4.1 shows six of them, beginning with the reflex arc just described. Each buys the organism something specific.

![Figure 4.1. Six circuit motifs that recur throughout the nervous system. Arrowheads mark excitatory synapses and filled circles inhibitory ones; panel A is the knee-jerk arc, in which the stretched extensor is excited and its flexor antagonist is inhibited.](images/fig_motifs.png)

Feedforward excitation is the trivial case: a signal passes from one neuron to the next. Chains of it carry information from the senses toward the muscles. On its own it transmits but does not shape.

Feedforward inhibition adds a branch. The input excites a target neuron and, through an interneuron, inhibits the same target a millisecond or two later. The effect is a narrow window: the target can respond only to inputs that arrive close together in time. Inputs that straggle are canceled. This motif turns a sluggish integrator into a coincidence detector, and it appears wherever timing precision matters, from the cerebellum to the auditory brainstem.[^4]

Feedback inhibition closes a loop. The target's own output recruits an interneuron that inhibits the target. The harder the population fires, the harder it is suppressed. This is a thermostat, and it is the primary reason cortical activity does not explode.[^5]

Lateral inhibition lets neighbors suppress one another. The neuron receiving the strongest input wins and silences its competitors. The consequences include sharpened contrast, winner-take-all selection, and the ability to represent a stimulus by which neuron is active rather than by how active everything is.[^6]

Recurrent excitation lets activity feed back on itself. A pattern of firing can be sustained after its input has gone, which is the basis of working memory, the holding of information in mind for seconds, and of pattern completion, described below.[^7] It is also the most dangerous motif in the brain. Without inhibition to contain it, recurrent excitation is a seizure.

Disinhibition is inhibition of an inhibitor. A target is held silent by default; an input that suppresses the inhibitor releases the target. This sounds like a roundabout way to excite something, but it has a property direct excitation lacks: the default state is off, so nothing happens unless the circuit is explicitly opened. The basal ganglia, discussed below, are built almost entirely from it.[^8]

# Inhibition Is Not the Opposite of Excitation

Engineers encountering these motifs tend to file inhibition under "negative weights" and move on. That misses most of what inhibition does.

Roughly one in five cortical neurons is inhibitory, and those neurons come in dozens of types, each targeting a different part of the excitatory cell: the dendrites, the soma, the axon initial segment, or other interneurons.[^9] Because they target different compartments, they do different jobs. Inhibition at the dendrite vetoes particular inputs. Inhibition at the soma vetoes output. Inhibition at the axon initial segment controls exactly when a spike may leave.

Most importantly, excitation and inhibition are balanced. In an awake cortex, every excitatory input to a neuron is tracked by a nearly equal inhibitory input arriving a few milliseconds later.[^10] The neuron lives close to threshold, held there by two large forces that almost cancel. Small changes in either one move it across the line.

Figure 4.2 shows why this arrangement is worth its cost. It is a simulation of a recurrently connected excitatory population, the same network three times, with only the strength of inhibition changed. With no inhibition the population does not respond to a brief input and then stop; the input tips it into a runaway that ends only when every cell is firing flat out, and it stays there after the input is gone, a seizure in miniature. Add inhibition that tracks the excitation and the same population produces a brief, bounded response that ends when the input ends. Add too much and the response is muted. The balanced regime is expensive, because two large currents are spent to produce a small net effect, and it is the only regime in which the circuit is both sensitive and stable.[^11]

![Figure 4.2. A simulated excitatory population with three levels of inhibition. The yellow band is a brief input: with no inhibition it triggers a runaway to the ceiling that outlasts the input, with balanced inhibition the response is brief and proportionate, and with excessive inhibition the input barely registers.](images/fig_ei.png)

Balance is also what makes the circuit fast. A neuron held near threshold by opposing forces can be flipped by a single well-timed input. A neuron resting far below threshold must be dragged up first. Inhibition is not the brake on the system. It is what makes the system responsive.[^12]

# Computation Before the Brain

The retina shows how much can be done with these motifs before any signal reaches the cortex. Figure 4.3 is Cajal's drawing of it. Light enters at the left, crosses several layers of neurons, and reaches the photoreceptors at the right, so the signal those cells generate travels back through the layers before it leaves through the axons of the ganglion cells, which together form the optic nerve.

![Figure 4.3. Santiago Ramón y Cajal's drawing of the vertebrate retina. Light enters from the left and crosses several layers of neurons before reaching the photoreceptors at the right; the processed signal leaves through the ganglion cell axons at the far left.](images/retina.png)

Light falls on photoreceptors, but the signal that leaves the eye has already passed through three layers of circuitry. Horizontal cells implement lateral inhibition across the photoreceptor layer, so a uniformly lit region produces little output while an edge produces a strong one. Amacrine cells add feedforward and feedback inhibition that make ganglion cells sensitive to change in time as well as space. By the time the optic nerve leaves the eye, the image has been converted into a map of edges and changes. Uniform brightness, which carries little information, has been largely discarded.[^13]

Lateral inhibition can be seen directly. Figure 4.4 shows a staircase of uniform gray steps; each step looks lighter along its border with the darker neighbor and darker along its border with the lighter one, although the luminance within every step is constant. The fringes are Mach bands, described by the physicist Ernst Mach in 1865, and the lower panel shows where they come from: a cell just on the bright side of an edge is inhibited by fewer bright neighbors than a cell in the middle of the step, so it fires more, and a cell just on the dark side is inhibited by more, so it fires less. The bands are the signature of a circuit that trades a faithful copy of the input for an informative one, under a strict budget of axons.[^14]

![Figure 4.4. Mach bands, lateral inhibition made visible. The staircase is made of uniform gray steps, yet each step looks lighter at its border with the darker step and darker at its border with the lighter one; the lower panel compares the true luminance with the illustrative response of a lateral-inhibition network, which overshoots on the bright side of every edge and undershoots on the dark side.](images/fig_mach_bands.png)

# Circuits That Generate Their Own Rhythm

Some circuits do not wait for input at all.

Walking, swimming, breathing, chewing, and the peristalsis of the gut are rhythmic, and the rhythm is generated by small networks in the spinal cord and brainstem called central pattern generators.[^15] The surprising fact, established in the early twentieth century and confirmed many times since, is that these networks produce their rhythm without any rhythmic input. A spinal cord isolated from the brain and from sensory feedback will still generate the alternating pattern of locomotion when given a steady chemical or electrical drive.[^16]

The minimal pattern generator is the half-center oscillator in Figure 4.5. Two populations inhibit each other, so only one can be active at a time. Each population also fatigues while active, through adaptation in its neurons or depression at its synapses. The active side weakens, its grip on the other side loosens, the other side escapes and takes over, and the cycle repeats. Mutual inhibition plus fatigue produces alternation from a constant input.[^17]

![Figure 4.5. A half-center oscillator. Two populations inhibit each other and each fatigues while active; given a constant drive they alternate, as the simulated output trace on the right shows, because the active side tires, the suppressed side escapes, and the cycle repeats.](images/fig_cpg.png)

Sensory feedback does not drive the rhythm; it tunes it. Signals from the limbs adjust timing and amplitude so that a walking pattern survives a stone underfoot. The division of labor is the one Chapter 1 stated: "The brain generates behavior, and the world corrects it."[^18]

# The Cortical Microcircuit

The cerebral cortex is a sheet a few millimeters thick, folded to fit the skull. Most of it is neocortex, the six-layered kind (older cortical regions such as the hippocampus have three layers), and across the whole neocortical sheet the same six-layered circuit is repeated with only local variations. Figure 4.6 shows it as Cajal drew it. Two of the panels use the Nissl stain, which marks only cell bodies, and the third uses the Golgi stain, which fills a few whole neurons, dendrites and axons included; in all three the layers appear as bands of differing cell density.

![Figure 4.6. Three of Cajal's drawings of the cerebral cortex. Nissl stains show cell bodies in adult human visual cortex (left) and motor cortex (center), and a Golgi stain shows whole neurons in the cortex of a one-and-a-half-month-old infant (right); the six layers are visible as bands of differing cell density.](images/cajal_cortex.png)

Input from the thalamus, the cortex's gateway for the senses, arrives mainly in layer 4. Layer 4 neurons project upward to layers 2 and 3, where most local processing and most connections to other cortical areas occur. Layers 2 and 3 project down to layer 5, which sends the cortex's output to the brainstem, spinal cord, and basal ganglia. Layer 6 projects back to the thalamus, closing a loop that lets the cortex modulate its own input.[^19]

Within this stack, every motif from Figure 4.1 is present. Feedforward inhibition sharpens the timing of thalamic input. Recurrent excitation among layer 2 and 3 neurons sustains and amplifies patterns. Feedback and lateral inhibition keep the amplification bounded. The whole arrangement has been called the canonical microcircuit, and it is approximately the same whether the cortex in question is processing vision, sound, touch, language, or plans.[^20]

Vertically, the neurons stacked above one another through all six layers share their inputs, forming columns like those in Figure 4.7. A column in visual cortex responds to one orientation at one location; a column in somatosensory cortex responds to one whisker.[^21] The column is not a rigid unit, and its boundaries blur in many species, but the principle is robust: the cortex is a tiled array of nearly identical circuits, differing mostly in what they are connected to.[^22]

![Figure 4.7. A three-dimensional reconstruction of five neighboring columns in rat somatosensory cortex, each corresponding to one whisker. The six layers run horizontally; the columns run vertically through all of them.](images/columns.jpg)

This is the strongest hint in neuroanatomy that cortical computation is general. The same circuit learns to see or to hear depending on where its input comes from, which is why, in a famous series of experiments in ferrets, retinal axons rerouted during development into the auditory pathway produced an auditory cortex that could see: the animals, tested as adults, responded to light through it.[^23]

# Two Loops for Action

The cortex proposes. Two subcortical systems dispose, in different ways.

The basal ganglia solve the problem of selection. At any moment the cortex represents many candidate actions in parallel, and the body can perform only one. The basal ganglia are the disinhibition motif scaled up to an organ. Their output nuclei fire continuously, holding the thalamus and brainstem motor circuits under tonic inhibition, so that by default no action is released. A cortical pattern that excites the striatum, the input stage, inhibits the inhibitors covering one action, and that action alone is freed. Figure 4.8 draws this direct pathway; a second, indirect pathway through the striatum raises the inhibition on competing actions, and a hyperdirect path from cortex to the output nuclei can stop everything at once.[^24]

![Figure 4.8. The direct pathway through the basal ganglia. Output nuclei inhibit motor targets by default; the striatum selects an action by inhibiting the inhibition that covers it, and dopamine sets how readily the striatum does this.](images/fig_bg.png)

The design has two features that matter. The first is that it can fail in either direction, and the clinic shows both. Parkinson's disease is the loss of the dopamine neurons of the substantia nigra that bias the striatum toward release, and the result is too little movement: slowness, rigidity, and difficulty starting. Huntington's disease destroys the striatal neurons of the indirect pathway that hold competing actions off, and the result is chorea, a stream of unwanted movements; a lesion of the subthalamic nucleus, a station on that same path, produces hemiballismus, violent flinging of the limbs on one side. The classical model of Albin, Young, and Penney and of DeLong is built on exactly this contrast between hypokinetic and hyperkinetic disorders. The circuit does not fail safe: it fails toward too little when the release signal is lost and toward too much when the brakes are lost.[^25] The second feature is that because dopamine acts on the striatum, the reward prediction error of Chapter 3, carried by a large population of midbrain dopamine neurons, arrives at exactly the synapses that decide which action is released. The basal ganglia are where "learning should happen now" meets "this is what was chosen." Habits are the result.[^26]

The cerebellum solves a different problem: precision. It holds about 69 of the brain's 86 billion neurons, more than the rest of the brain combined, arranged in a circuit of striking regularity.[^27] Each Purkinje cell, the large neuron that is the sole output of the cerebellar cortex, receives about two hundred thousand weak inputs from parallel fibers, carrying the current state of the body and the current motor command, and a single powerful input from one climbing fiber, which fires when a movement goes wrong.[^28] Figure 4.9 lays out the circuit.

![Figure 4.9. The cerebellar microcircuit. Mossy fibers (MF) and parallel fibers (PF) carry context to the Purkinje cell (PC); a single climbing fiber (CF) from the inferior olive (IO) carries an error signal. Purkinje cells inhibit the deep cerebellar nuclei (DCN), the cerebellum's output.](images/cereb2.png)

In the classical theory of Marr, Albus, and Ito, the climbing fiber is a teaching signal. When it fires, the parallel fiber synapses that were recently active are weakened, which is an eligibility trace mechanism of the kind Chapter 3 described, implemented in a circuit so regular that it was one of the first to be modeled mathematically; Ito demonstrated the weakening, cerebellar long-term depression, in 1982.[^29] The full picture is richer. Mice in which this depression was blocked still learned several cerebellar tasks, including the adjustment of the reflex that keeps the eyes on a target while the head turns and the conditioning of an eyeblink to a tone, so plasticity at other sites, at the Purkinje cell's other synapses, among the interneurons of the molecular layer, and in the deep nuclei, must share the work; and climbing fibers have since been found to fire not only for errors but for expected reward and for learned predictions of what a movement will produce.[^30] What survives is the division of labor: a massive context input, a sparse instructive input, and synapses that change when the two coincide. Over repetitions, the cerebellum learns to predict the sensory consequences of a command and to issue corrections before errors occur.[^31] Reaching, balance, eye movements, and the timing of speech all depend on it. Its lesions do not abolish movement; they make movement clumsy.[^32]

# The Hippocampal Loop

The hippocampus is the circuit most closely identified with memory, and its anatomy, shown in Figure 4.10, is a chain of the motifs already described.[^33]

![Figure 4.10. Cajal's drawing of the hippocampal formation, with a modern summary of its main pathway: entorhinal cortex (EC) to dentate gyrus (DG) to CA3 to CA1 and back to entorhinal cortex.](images/hippo.png)

Cortical input enters through the entorhinal cortex and passes to the dentate gyrus, whose sparse, strongly inhibited granule cells make similar inputs less similar, a process called pattern separation.[^34] The dentate projects to CA3, whose pyramidal cells are densely connected to one another: recurrent excitation on a large scale. A partial cue that activates some CA3 cells can regenerate the whole pattern, which is pattern completion.[^35] CA3 projects to CA1, which on one account compares the retrieved pattern with the current input, delivered to CA1 directly from the entorhinal cortex, and returns the result to the cortex; the comparator role is a hypothesis supported by modeling and slice physiology rather than an established function.[^36]

Separation, storage, completion, and comparison, in that order, each implemented by a motif from Figure 4.1. The circuit is described here only in outline; Chapter 5 returns to how its synapses change.

# Rhythms

If circuits are the brain's structure, rhythms are its timing.

Record the voltage at the scalp, the electroencephalogram or EEG, and you see oscillations, conventionally sorted into bands named by Greek letters: delta or slow waves (below 4 Hz) during deep sleep, theta (4 to 8 Hz) during exploration and memory tasks, alpha (8 to 12 Hz) over idle cortex, beta (13 to 30 Hz) while a posture or a plan is held, and gamma (30 to 100 Hz) wherever local processing is intense. Figure 4.11 shows one second of each.[^37]

![Figure 4.11. One second of scalp EEG filtered into five frequency bands. Each band is associated with a characteristic behavioral state, though the associations are statistical rather than exclusive.](images/fig_rhythms.png)

Oscillations are the collective behavior of circuits built from the motifs above. Feedback inhibition is intrinsically rhythmic: excitation recruits inhibition, inhibition silences excitation, inhibition decays, excitation recovers. A population of excitatory cells coupled to a population of fast interneurons oscillates in the gamma range for exactly this reason, and a network of interneurons inhibiting one another can do the same on its own.[^38]

Rhythms do real work. A neuron is most excitable at one phase of the oscillation and least at the opposite phase, so a shared rhythm creates windows during which inputs are effective. It has been proposed that this is how the brain routes information through fixed wiring: two regions whose oscillations are aligned so that one's spikes arrive in the other's excitable phase would communicate well, two regions out of alignment would communicate poorly, and changing the phase relation would change the effective wiring without changing a synapse. This is the communication-through-coherence hypothesis, and it is the brain's candidate answer to a problem every large network has.[^39] The evidence is mixed. Coherence between areas does rise with attention, as the hypothesis predicts, but modeling and recordings from visual cortex show that coherence between two areas can arise simply from their connectivity and the sender's oscillatory power, with no phase-dependent gating at all, and the frequency of gamma shifts with the contrast and size of a stimulus, which makes it an unreliable clock for aligning distant areas.[^40] Whether rhythm routes information or merely reflects it is an open question.

Rhythms also coordinate learning. In the hippocampus, place cells, neurons that each fire when the animal is at one particular location, fire at progressively earlier phases of the theta cycle as the animal crosses that location, compressing a sequence of seconds into a sequence of tens of milliseconds. That compressed sequence falls within the window in which synapses can change. The rhythm converts experience into a format plasticity can use.[^41]

# The Architecture of the Whole

Step back from any single region and the brain is a network of regions, which its anatomists now call the connectome.[^42] Its wiring is neither random nor fully regular, and the compromise it strikes, shown in Figure 4.12, is the same one found in power grids, social networks, and the internet.

![Figure 4.12. A small-world network: most connections are local, a few are long-range. The result is dense local clustering with short paths between any two nodes.](images/ws.png)

Most connections are short, linking neighbors into dense clusters. A minority are long, linking clusters to one another. The result is a small-world network: any two regions are only a few connections apart, yet almost all wiring is local and cheap. The same structure has been shown neuron by neuron in the nematode worm, the one animal whose complete wiring diagram was known when the idea was proposed; at the level of single neurons the mammalian brain is an extrapolation. Long axons are metabolically expensive, occupy volume, and slow signals, so the brain uses as few of them as it can while keeping the path length between regions short.[^43] Figure 4.13 shows those long axons in a living human brain, reconstructed by tracing the direction in which water diffuses along the fiber bundles.

![Figure 4.13. Long-range fiber tracts of the human brain reconstructed from diffusion MRI, viewed from above. Colors indicate fiber direction.](images/connectome.png)

A few regions are hubs with far more long-range connections than average, and these hubs are disproportionately connected to one another, forming a core through which most long-distance traffic passes.[^44] The arrangement is efficient and fragile in the same way an airline network is: it makes the system fast, and it makes damage to a hub far more consequential than damage elsewhere. Several neurological and psychiatric conditions, schizophrenia and Alzheimer's disease among them, are now described, at least in part, as disorders of the hubs: across 26 disorders, the sites of gray matter loss fell disproportionately on hub regions.[^45]

# Coordination Without a Conductor

Chapter 1 claimed that the brain has no central controller. This chapter has described the machinery that makes a controller unnecessary.

Reflexes handle the fastest demands locally. Pattern generators produce rhythmic behavior on their own and accept correction from the body. Balanced inhibition keeps every circuit sensitive without letting it run away. The basal ganglia release one action at a time from a default of silence. The cerebellum corrects movements before errors are felt. Rhythms may decide which regions can talk to which, moment by moment. A small-world wiring plan keeps all of this within a few connections of everything else.

No component sees the whole. Each solves a local problem using the same small vocabulary of motifs, and the behavior of the animal is what those local solutions add up to. The pattern is meaningful, as Sherrington said, and never abiding: it is re-created from moment to moment by circuits that were never designed to produce it.[^46]

# Implications for Artificial Intelligence

Artificial neural networks borrowed the neuron and left the circuit behind. Several of this chapter's lessons bear directly on how that might be repaired.

First, inhibition is not a negative weight. In most artificial networks a weight can be positive or negative, so the same unit excites some targets and inhibits others, and nothing enforces balance; a biological neuron is one or the other, a rule known as Dale's principle. Biological circuits maintain excitation and inhibition as separate populations and keep them in near-cancellation, which buys speed, stability, and sensitivity at once. Networks built to respect the division are a largely unexplored design space, and the first attempts to train them show that, with the learning rule adjusted, they can match unconstrained networks.[^47]

Second, selection by disinhibition is a different control strategy from choosing the largest output. The basal ganglia hold all actions off by default and release one. The default of silence makes "do nothing" a first-class action, which is often what an agent in an uncertain environment should do, and it gives the circuit two recognizable failure modes, too little and too much, rather than a diffuse degradation.

Third, rhythm may be a routing mechanism. Fixed weights cannot change which parts of a network talk to each other, so artificial systems add attention mechanisms to do it (Chapter 6 returns to attention).[^48] The brain, on the coherence hypothesis, does it with phase. Oscillatory gating offers a way to reconfigure effective connectivity without changing parameters, at low cost.

Fourth, the brain's wiring budget shapes its architecture. Small-world organization, local clustering, and sparse long-range connections are consequences of paying for every axon. Artificial networks pay far less per connection than an axon costs, in parameters, memory, and arithmetic rather than in volume and metabolism, and they are correspondingly dense; the literature on pruning and sparsity exists because even that smaller cost adds up.

Finally, the cortex suggests that general computation can come from a single repeated circuit with different inputs. The question of what that circuit is doing, in a form abstract enough to transfer, remains open. It is one of the most important open problems in both neuroscience and machine learning.

# The Central Lesson

Behavior belongs to circuits, not cells. The nervous system builds its circuits from a small vocabulary of motifs in which inhibition does most of the shaping, stacks them into regions that each solve one kind of problem, and coordinates the regions through rhythm and a wiring plan that keeps everything close. No part is in charge. Coordinated behavior is what the parts produce together.

# Next Chapter

Chapter 5: Plasticity and Memory: How Experience Becomes Structure

# References and Attribution

## Figure Attribution

Figures 4.1, 4.2, 4.4, 4.5, and 4.8 were drawn for this book. Figure 4.2, the lower panel of Figure 4.4, and the output trace in Figure 4.5 are illustrative simulations of simple rate models, not recordings.

Figure 4.3: Santiago Ramón y Cajal, structure of the mammalian retina (1900), public domain, via Wikimedia Commons.

Figure 4.6: Santiago Ramón y Cajal, drawings of the cerebral cortex (1899), public domain, via Wikimedia Commons ("Cajal cortex drawings"): Nissl-stained adult human visual cortex, Nissl-stained adult human motor cortex, and Golgi-stained cortex of a one-and-a-half-month-old infant.

Figure 4.7: "Cortical Columns," underlying image from Marcel Oberländer, Beyond the Cortical Column, Neuroinformatics 2012; composite by Wikimedia Commons user Bodysurfinyon, CC BY-SA 4.0.

Figure 4.9: "CerebCircuit" by Wikipedia user Nrets, CC BY-SA 3.0, via Wikimedia Commons.

Figure 4.10: Santiago Ramón y Cajal, drawing of the hippocampus (1911), public domain, with circuit inset added by Wikimedia Commons contributors.

Figure 4.11: EEG band traces ("Eeg delta", "Eeg theta", "Eeg alpha", "Eeg beta", "Eeg gamma") by Hugo Gamboa, CC BY-SA 3.0, via Wikimedia Commons; composite drawn for this book.

Figure 4.12: "Watts-Strogatz small-world model, 100 nodes" by Wikimedia Commons user Keiono, CC BY-SA 3.0.

Figure 4.13: "The Human Connectome" by Wikimedia Commons user Andreashorn, CC BY-SA 4.0.

## Epigraph

Charles Sherrington, *Man on His Nature* (Cambridge University Press, 1940), the Gifford Lectures of 1937–38.

## References

Albin, R. L., Young, A. B., & Penney, J. B. (1989). The functional anatomy of basal ganglia disorders. *Trends in Neurosciences*, 12(10), 366–375.

Albus, J. S. (1971). A theory of cerebellar function. *Mathematical Biosciences*, 10(1–2), 25–61.

Alexander, G. E., DeLong, M. R., & Strick, P. L. (1986). Parallel organization of functionally segregated circuits linking basal ganglia and cortex. *Annual Review of Neuroscience*, 9, 357–381.

Amaral, D. G., & Witter, M. P. (1989). The three-dimensional organization of the hippocampal formation: A review of anatomical data. *Neuroscience*, 31(3), 571–591.

Andersen, P., Bliss, T. V. P., & Skrede, K. K. (1971). Lamellar organization of hippocampal excitatory pathways. *Experimental Brain Research*, 13(2), 222–238.

Azevedo, F. A. C., Carvalho, L. R. B., Grinberg, L. T., Farfel, J. M., Ferretti, R. E. L., Leite, R. E. P., Jacob Filho, W., Lent, R., & Herculano-Houzel, S. (2009). Equal numbers of neuronal and nonneuronal cells make the human brain an isometrically scaled-up primate brain. *Journal of Comparative Neurology*, 513(5), 532–541.

Bassett, D. S., & Bullmore, E. (2006). Small-world brain networks. *The Neuroscientist*, 12(6), 512–523.

Brown, T. G. (1911). The intrinsic factors in the act of progression in the mammal. *Proceedings of the Royal Society B*, 84(572), 308–319.

Brown, T. G. (1914). On the nature of the fundamental activity of the nervous centres; together with an analysis of the conditioning of rhythmic activity in progression, and a theory of the evolution of function in the nervous system. *Journal of Physiology*, 48(1), 18–46.

Bullmore, E., & Sporns, O. (2009). Complex brain networks: Graph theoretical analysis of structural and functional systems. *Nature Reviews Neuroscience*, 10(3), 186–198.

Bullmore, E., & Sporns, O. (2012). The economy of brain network organization. *Nature Reviews Neuroscience*, 13(5), 336–349.

Buzsáki, G. (2006). *Rhythms of the Brain*. Oxford University Press.

Buzsáki, G., & Draguhn, A. (2004). Neuronal oscillations in cortical networks. *Science*, 304(5679), 1926–1929.

Buzsáki, G., & Wang, X.-J. (2012). Mechanisms of gamma oscillations. *Annual Review of Neuroscience*, 35, 203–225.

Cardin, J. A., Carlén, M., Meletis, K., Knoblich, U., Zhang, F., Deisseroth, K., Tsai, L.-H., & Moore, C. I. (2009). Driving fast-spiking cells induces gamma rhythm and controls sensory responses. *Nature*, 459, 663–667.

Chevalier, G., & Deniau, J. M. (1990). Disinhibition as a basic process in the expression of striatal functions. *Trends in Neurosciences*, 13(7), 277–280.

Chklovskii, D. B., Schikorski, T., & Stevens, C. F. (2002). Wiring optimization in cortical circuits. *Neuron*, 34(3), 341–347.

Cornford, J., Kalajdzievski, D., Leite, M., Lamarquette, A., Kullmann, D. M., & Richards, B. A. (2021). Learning to live with Dale's principle: ANNs with separate excitatory and inhibitory units. *International Conference on Learning Representations (ICLR)*.

Crossley, N. A., Mechelli, A., Scott, J., Carletti, F., Fox, P. T., McGuire, P., & Bullmore, E. T. (2014). The hubs of the human connectome are generally implicated in the anatomy of brain disorders. *Brain*, 137(8), 2382–2395.

DeLong, M. R. (1990). Primate models of movement disorders of basal ganglia origin. *Trends in Neurosciences*, 13(7), 281–285.

Douglas, R. J., & Martin, K. A. C. (2004). Neuronal circuits of the neocortex. *Annual Review of Neuroscience*, 27, 419–451.

Douglas, R. J., Martin, K. A. C., & Whitteridge, D. (1989). A canonical microcircuit for neocortex. *Neural Computation*, 1(4), 480–488.

Eccles, J. C., Ito, M., & Szentágothai, J. (1967). *The Cerebellum as a Neuronal Machine*. Springer.

Fries, P. (2005). A mechanism for cognitive dynamics: Neuronal communication through neuronal coherence. *Trends in Cognitive Sciences*, 9(10), 474–480.

Fries, P. (2015). Rhythms for cognition: Communication through coherence. *Neuron*, 88(1), 220–235.

Goldman-Rakic, P. S. (1995). Cellular basis of working memory. *Neuron*, 14(3), 477–485.

Graybiel, A. M. (2008). Habits, rituals, and the evaluative brain. *Annual Review of Neuroscience*, 31, 359–387.

Grillner, S., & Zangger, P. (1979). On the central generation of locomotion in the low spinal cat. *Experimental Brain Research*, 34(2), 241–261.

Harris, K. D., & Shepherd, G. M. G. (2015). The neocortical circuit: Themes and variations. *Nature Neuroscience*, 18(2), 170–181.

Hartline, H. K., Wagner, H. G., & Ratliff, F. (1956). Inhibition in the eye of *Limulus*. *Journal of General Physiology*, 39(5), 651–673.

Hasselmo, M. E., & Schnell, E. (1994). Laminar selectivity of the cholinergic suppression of synaptic transmission in rat hippocampal region CA1: Computational modeling and brain slice physiology. *Journal of Neuroscience*, 14(6), 3898–3914.

Heffley, W., Song, E. Y., Xu, Z., Taylor, B. N., Hughes, M. A., McKinney, A., Joshua, M., & Hull, C. (2018). Coordinated cerebellar climbing fiber activity signals learned sensorimotor predictions. *Nature Neuroscience*, 21(10), 1431–1441.

Holmes, G. (1939). The cerebellum of man. *Brain*, 62(1), 1–30.

Horton, J. C., & Adams, D. L. (2005). The cortical column: A structure without a function. *Philosophical Transactions of the Royal Society B*, 360(1456), 837–862.

Hubel, D. H., & Wiesel, T. N. (1962). Receptive fields, binocular interaction and functional architecture in the cat's visual cortex. *Journal of Physiology*, 160(1), 106–154.

Isaacson, J. S., & Scanziani, M. (2011). How inhibition shapes cortical activity. *Neuron*, 72(2), 231–243.

Ito, M. (2001). Cerebellar long-term depression: Characterization, signal transduction, and functional roles. *Physiological Reviews*, 81(3), 1143–1195.

Ito, M., Sakurai, M., & Tongroach, P. (1982). Climbing fibre induced depression of both mossy fibre responsiveness and glutamate sensitivity of cerebellar Purkinje cells. *Journal of Physiology*, 324, 113–134.

Kostadinov, D., Beau, M., Blanco-Pozo, M., & Häusser, M. (2019). Predictive and reactive reward signals conveyed by climbing fiber inputs to cerebellar Purkinje cells. *Nature Neuroscience*, 22(6), 950–962.

Letzkus, J. J., Wolff, S. B. E., Meyer, E. M. M., Tovote, P., Courtin, J., Herry, C., & Lüthi, A. (2011). A disinhibitory microcircuit for associative fear learning in the auditory cortex. *Nature*, 480, 331–335.

Leutgeb, J. K., Leutgeb, S., Moser, M.-B., & Moser, E. I. (2007). Pattern separation in the dentate gyrus and CA3 of the hippocampus. *Science*, 315(5814), 961–966.

Liddell, E. G. T., & Sherrington, C. S. (1924). Reflexes in response to stretch (myotatic reflexes). *Proceedings of the Royal Society B*, 96, 212–242.

Lisman, J. E., & Grace, A. A. (2005). The hippocampal-VTA loop: Controlling the entry of information into long-term memory. *Neuron*, 46(5), 703–713.

Marder, E., & Bucher, D. (2001). Central pattern generators and the control of rhythmic movements. *Current Biology*, 11(23), R986–R996.

Markram, H., Toledo-Rodriguez, M., Wang, Y., Gupta, A., Silberberg, G., & Wu, C. (2004). Interneurons of the neocortical inhibitory system. *Nature Reviews Neuroscience*, 5(10), 793–807.

Marr, D. (1969). A theory of cerebellar cortex. *Journal of Physiology*, 202(2), 437–470.

Marr, D. (1971). Simple memory: A theory for archicortex. *Philosophical Transactions of the Royal Society B*, 262(841), 23–81.

Masland, R. H. (2012). The neuronal organization of the retina. *Neuron*, 76(2), 266–280.

Mink, J. W. (1996). The basal ganglia: Focused selection and inhibition of competing motor programs. *Progress in Neurobiology*, 50(4), 381–425.

Mountcastle, V. B. (1957). Modality and topographic properties of single neurons of cat's somatic sensory cortex. *Journal of Neurophysiology*, 20(4), 408–434.

Nakazawa, K., Quirk, M. C., Chitwood, R. A., Watanabe, M., Yeckel, M. F., Sun, L. D., Kato, A., Carr, C. A., Johnston, D., Wilson, M. A., & Tonegawa, S. (2002). Requirement for hippocampal CA3 NMDA receptors in associative memory recall. *Science*, 297(5579), 211–218.

Napper, R. M. A., & Harvey, R. J. (1988). Number of parallel fiber synapses on an individual Purkinje cell in the cerebellum of the rat. *Journal of Comparative Neurology*, 274(2), 168–177.

O'Keefe, J., & Dostrovsky, J. (1971). The hippocampus as a spatial map: Preliminary evidence from unit activity in the freely-moving rat. *Brain Research*, 34(1), 171–175.

O'Keefe, J., & Recce, M. L. (1993). Phase relationship between hippocampal place units and the EEG theta rhythm. *Hippocampus*, 3(3), 317–330.

Okun, M., & Lampl, I. (2008). Instantaneous correlation of excitation and inhibition during ongoing and sensory-evoked activities. *Nature Neuroscience*, 11(5), 535–537.

Pakkenberg, B., Pelvig, D., Marner, L., Bundgaard, M. J., Gundersen, H. J. G., Nyengaard, J. R., & Regeur, L. (2003). Aging and the human neocortex. *Experimental Gerontology*, 38(1–2), 95–99.

Pi, H.-J., Hangya, B., Kvitsiani, D., Sanders, J. I., Huang, Z. J., & Kepecs, A. (2013). Cortical interneurons that specialize in disinhibitory control. *Nature*, 503, 521–524.

Pouille, F., & Scanziani, M. (2001). Enforcement of temporal fidelity in pyramidal cells by somatic feed-forward inhibition. *Science*, 293(5532), 1159–1163.

Ratliff, F. (1965). *Mach Bands: Quantitative Studies on Neural Networks in the Retina*. Holden-Day.

Ray, S., & Maunsell, J. H. R. (2015). Do gamma oscillations play a role in cerebral cortex? *Trends in Cognitive Sciences*, 19(2), 78–85.

Redgrave, P., Prescott, T. J., & Gurney, K. (1999). The basal ganglia: A vertebrate solution to the selection problem? *Neuroscience*, 89(4), 1009–1023.

Reynolds, J. N. J., Hyland, B. I., & Wickens, J. R. (2001). A cellular mechanism of reward-related learning. *Nature*, 413, 67–70.

Rossignol, S., Dubuc, R., & Gossard, J.-P. (2006). Dynamic sensorimotor interactions in locomotion. *Physiological Reviews*, 86(1), 89–154.

Schneider, M., Broggini, A. C., Dann, B., Tzanou, A., Uran, C., Sheshadri, S., Scherberger, H., & Vinck, M. (2021). A mechanism for inter-areal coherence through communication based on connectivity and oscillatory power. *Neuron*, 109(24), 4050–4067.

Schonewille, M., Gao, Z., Boele, H.-J., Vinueza Veloz, M. F., Amerika, W. E., Šimek, A. A. M., De Jeu, M. T., Steinberg, J. P., Takamiya, K., Hoebeek, F. E., Linden, D. J., Huganir, R. L., & De Zeeuw, C. I. (2011). Reevaluating the role of LTD in cerebellar motor learning. *Neuron*, 70(1), 43–50.

Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. *Science*, 275(5306), 1593–1599.

Shadlen, M. N., & Newsome, W. T. (1998). The variable discharge of cortical neurons: Implications for connectivity, computation, and information coding. *Journal of Neuroscience*, 18(10), 3870–3896.

Sherrington, C. S. (1906). *The Integrative Action of the Nervous System*. Charles Scribner's Sons.

Sherrington, C. S. (1940). *Man on His Nature*. Cambridge University Press.

Skaggs, W. E., McNaughton, B. L., Wilson, M. A., & Barnes, C. A. (1996). Theta phase precession in hippocampal neuronal populations and the compression of temporal sequences. *Hippocampus*, 6(2), 149–172.

Smith, J. C., Ellenberger, H. H., Ballanyi, K., Richter, D. W., & Feldman, J. L. (1991). Pre-Bötzinger complex: A brainstem region that may generate respiratory rhythm in mammals. *Science*, 254(5032), 726–729.

Sporns, O., Tononi, G., & Kötter, R. (2005). The human connectome: A structural description of the human brain. *PLoS Computational Biology*, 1(4), e42.

Sur, M., Garraghty, P. E., & Roe, A. W. (1988). Experimentally induced visual projections into auditory thalamus and cortex. *Science*, 242(4884), 1437–1441.

Tang, Y., Nyengaard, J. R., De Groot, D. M. G., & Gundersen, H. J. G. (2001). Total regional and global number of synapses in the human brain neocortex. *Synapse*, 41(3), 258–273.

Tremblay, R., Lee, S., & Rudy, B. (2016). GABAergic interneurons in the neocortex: From cellular properties to circuits. *Neuron*, 91(2), 260–292.

Treves, A., & Rolls, E. T. (1994). Computational analysis of the role of the hippocampus in memory. *Hippocampus*, 4(3), 374–391.

van den Heuvel, M. P., & Sporns, O. (2011). Rich-club organization of the human connectome. *Journal of Neuroscience*, 31(44), 15775–15786.

van Vreeswijk, C., & Sompolinsky, H. (1996). Chaos in neuronal networks with balanced excitatory and inhibitory activity. *Science*, 274(5293), 1724–1726.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30.

von Melchner, L., Pallas, S. L., & Sur, M. (2000). Visual behaviour mediated by retinal projections directed to the auditory pathway. *Nature*, 404, 871–876.

Wang, X.-J. (2001). Synaptic reverberation underlying mnemonic persistent activity. *Trends in Neurosciences*, 24(8), 455–463.

Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. *Nature*, 393, 440–442.

Wehr, M., & Zador, A. M. (2003). Balanced inhibition underlies tuning and sharpens spike timing in auditory cortex. *Nature*, 426, 442–446.

Whittington, M. A., Traub, R. D., & Jefferys, J. G. R. (1995). Synchronized oscillations in interneuron networks driven by metabotropic glutamate receptor activation. *Nature*, 373, 612–615.

Wolpert, D. M., Miall, R. C., & Kawato, M. (1998). Internal models in the cerebellum. *Trends in Cognitive Sciences*, 2(9), 338–347.

Wässle, H. (2004). Parallel processing in the mammalian retina. *Nature Reviews Neuroscience*, 5(10), 747–757.

Yin, H. H., & Knowlton, B. J. (2006). The role of the basal ganglia in habit formation. *Nature Reviews Neuroscience*, 7(6), 464–476.

[^1]: Azevedo, F. A. C., Carvalho, L. R. B., Grinberg, L. T., Farfel, J. M., Ferretti, R. E. L., Leite, R. E. P., Jacob Filho, W., Lent, R., & Herculano-Houzel, S. (2009). Equal numbers of neuronal and nonneuronal cells make the human brain an isometrically scaled-up primate brain. *Journal of Comparative Neurology*, 513(5), 532–541; Pakkenberg, B., Pelvig, D., Marner, L., Bundgaard, M. J., Gundersen, H. J. G., Nyengaard, J. R., & Regeur, L. (2003). Aging and the human neocortex. *Experimental Gerontology*, 38(1–2), 95–99; Tang, Y., Nyengaard, J. R., De Groot, D. M. G., & Gundersen, H. J. G. (2001). Total regional and global number of synapses in the human brain neocortex. *Synapse*, 41(3), 258–273. Azevedo and colleagues count the neurons; Tang and colleagues count about 164 trillion synapses in the neocortex, and Pakkenberg and colleagues give a similar figure of about 150 trillion for young adults.

[^2]: Sherrington, C. S. (1906). *The Integrative Action of the Nervous System*. Charles Scribner's Sons; Liddell, E. G. T., & Sherrington, C. S. (1924). Reflexes in response to stretch (myotatic reflexes). *Proceedings of the Royal Society B*, 96, 212–242.

[^3]: Sherrington, C. S. (1906). *The Integrative Action of the Nervous System*. Charles Scribner's Sons. Sherrington introduced the term reciprocal innervation in a series of notes to the Royal Society from 1893 onward and summarized the principle in the 1906 lectures.

[^4]: Pouille, F., & Scanziani, M. (2001). Enforcement of temporal fidelity in pyramidal cells by somatic feed-forward inhibition. *Science*, 293(5532), 1159–1163.

[^5]: Isaacson, J. S., & Scanziani, M. (2011). How inhibition shapes cortical activity. *Neuron*, 72(2), 231–243.

[^6]: Hartline, H. K., Wagner, H. G., & Ratliff, F. (1956). Inhibition in the eye of *Limulus*. *Journal of General Physiology*, 39(5), 651–673. Lateral inhibition was first measured in the compound eye of the horseshoe crab.

[^7]: Goldman-Rakic, P. S. (1995). Cellular basis of working memory. *Neuron*, 14(3), 477–485; Wang, X.-J. (2001). Synaptic reverberation underlying mnemonic persistent activity. *Trends in Neurosciences*, 24(8), 455–463.

[^8]: Letzkus, J. J., Wolff, S. B. E., Meyer, E. M. M., Tovote, P., Courtin, J., Herry, C., & Lüthi, A. (2011). A disinhibitory microcircuit for associative fear learning in the auditory cortex. *Nature*, 480, 331–335; Pi, H.-J., Hangya, B., Kvitsiani, D., Sanders, J. I., Huang, Z. J., & Kepecs, A. (2013). Cortical interneurons that specialize in disinhibitory control. *Nature*, 503, 521–524. These papers describe disinhibitory microcircuits in cortex; the basal ganglia case is cited below.

[^9]: Markram, H., Toledo-Rodriguez, M., Wang, Y., Gupta, A., Silberberg, G., & Wu, C. (2004). Interneurons of the neocortical inhibitory system. *Nature Reviews Neuroscience*, 5(10), 793–807; Tremblay, R., Lee, S., & Rudy, B. (2016). GABAergic interneurons in the neocortex: From cellular properties to circuits. *Neuron*, 91(2), 260–292.

[^10]: Wehr, M., & Zador, A. M. (2003). Balanced inhibition underlies tuning and sharpens spike timing in auditory cortex. *Nature*, 426, 442–446; Okun, M., & Lampl, I. (2008). Instantaneous correlation of excitation and inhibition during ongoing and sensory-evoked activities. *Nature Neuroscience*, 11(5), 535–537.

[^11]: van Vreeswijk, C., & Sompolinsky, H. (1996). Chaos in neuronal networks with balanced excitatory and inhibitory activity. *Science*, 274(5293), 1724–1726; Shadlen, M. N., & Newsome, W. T. (1998). The variable discharge of cortical neurons: Implications for connectivity, computation, and information coding. *Journal of Neuroscience*, 18(10), 3870–3896.

[^12]: Isaacson, J. S., & Scanziani, M. (2011). How inhibition shapes cortical activity. *Neuron*, 72(2), 231–243.

[^13]: Masland, R. H. (2012). The neuronal organization of the retina. *Neuron*, 76(2), 266–280; Wässle, H. (2004). Parallel processing in the mammalian retina. *Nature Reviews Neuroscience*, 5(10), 747–757.

[^14]: Ratliff, F. (1965). *Mach Bands: Quantitative Studies on Neural Networks in the Retina*. Holden-Day. Mach described the bands in 1865; Ratliff's monograph connects them quantitatively to lateral inhibition.

[^15]: Marder, E., & Bucher, D. (2001). Central pattern generators and the control of rhythmic movements. *Current Biology*, 11(23), R986–R996; Smith, J. C., Ellenberger, H. H., Ballanyi, K., Richter, D. W., & Feldman, J. L. (1991). Pre-Bötzinger complex: A brainstem region that may generate respiratory rhythm in mammals. *Science*, 254(5032), 726–729. The respiratory rhythm generator in the brainstem is the pre-Bötzinger complex, identified by Smith and colleagues.

[^16]: Brown, T. G. (1911). The intrinsic factors in the act of progression in the mammal. *Proceedings of the Royal Society B*, 84(572), 308–319; Grillner, S., & Zangger, P. (1979). On the central generation of locomotion in the low spinal cat. *Experimental Brain Research*, 34(2), 241–261.

[^17]: Brown, T. G. (1914). On the nature of the fundamental activity of the nervous centres; together with an analysis of the conditioning of rhythmic activity in progression, and a theory of the evolution of function in the nervous system. *Journal of Physiology*, 48(1), 18–46. Brown's 1914 paper proposed the half-center model.

[^18]: Rossignol, S., Dubuc, R., & Gossard, J.-P. (2006). Dynamic sensorimotor interactions in locomotion. *Physiological Reviews*, 86(1), 89–154.

[^19]: Douglas, R. J., & Martin, K. A. C. (2004). Neuronal circuits of the neocortex. *Annual Review of Neuroscience*, 27, 419–451; Harris, K. D., & Shepherd, G. M. G. (2015). The neocortical circuit: Themes and variations. *Nature Neuroscience*, 18(2), 170–181.

[^20]: Douglas, R. J., Martin, K. A. C., & Whitteridge, D. (1989). A canonical microcircuit for neocortex. *Neural Computation*, 1(4), 480–488; Douglas, R. J., & Martin, K. A. C. (2004). Neuronal circuits of the neocortex. *Annual Review of Neuroscience*, 27, 419–451.

[^21]: Mountcastle, V. B. (1957). Modality and topographic properties of single neurons of cat's somatic sensory cortex. *Journal of Neurophysiology*, 20(4), 408–434; Hubel, D. H., & Wiesel, T. N. (1962). Receptive fields, binocular interaction and functional architecture in the cat's visual cortex. *Journal of Physiology*, 160(1), 106–154.

[^22]: Horton, J. C., & Adams, D. L. (2005). The cortical column: A structure without a function. *Philosophical Transactions of the Royal Society B*, 360(1456), 837–862.

[^23]: Sur, M., Garraghty, P. E., & Roe, A. W. (1988). Experimentally induced visual projections into auditory thalamus and cortex. *Science*, 242(4884), 1437–1441; von Melchner, L., Pallas, S. L., & Sur, M. (2000). Visual behaviour mediated by retinal projections directed to the auditory pathway. *Nature*, 404, 871–876.

[^24]: Chevalier, G., & Deniau, J. M. (1990). Disinhibition as a basic process in the expression of striatal functions. *Trends in Neurosciences*, 13(7), 277–280; Mink, J. W. (1996). The basal ganglia: Focused selection and inhibition of competing motor programs. *Progress in Neurobiology*, 50(4), 381–425; Redgrave, P., Prescott, T. J., & Gurney, K. (1999). The basal ganglia: A vertebrate solution to the selection problem? *Neuroscience*, 89(4), 1009–1023.

[^25]: Alexander, G. E., DeLong, M. R., & Strick, P. L. (1986). Parallel organization of functionally segregated circuits linking basal ganglia and cortex. *Annual Review of Neuroscience*, 9, 357–381; Albin, R. L., Young, A. B., & Penney, J. B. (1989). The functional anatomy of basal ganglia disorders. *Trends in Neurosciences*, 12(10), 366–375; DeLong, M. R. (1990). Primate models of movement disorders of basal ganglia origin. *Trends in Neurosciences*, 13(7), 281–285. The Albin, Young, and Penney model attributes hypokinetic disorders to overactive output nuclei and hyperkinetic ones, chorea and hemiballismus among them, to underactive output nuclei after loss of the indirect pathway or of the subthalamic nucleus.

[^26]: Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. *Science*, 275(5306), 1593–1599; Reynolds, J. N. J., Hyland, B. I., & Wickens, J. R. (2001). A cellular mechanism of reward-related learning. *Nature*, 413, 67–70; Graybiel, A. M. (2008). Habits, rituals, and the evaluative brain. *Annual Review of Neuroscience*, 31, 359–387; Yin, H. H., & Knowlton, B. J. (2006). The role of the basal ganglia in habit formation. *Nature Reviews Neuroscience*, 7(6), 464–476.

[^27]: Azevedo, F. A. C., Carvalho, L. R. B., Grinberg, L. T., Farfel, J. M., Ferretti, R. E. L., Leite, R. E. P., Jacob Filho, W., Lent, R., & Herculano-Houzel, S. (2009). Equal numbers of neuronal and nonneuronal cells make the human brain an isometrically scaled-up primate brain. *Journal of Comparative Neurology*, 513(5), 532–541; Eccles, J. C., Ito, M., & Szentágothai, J. (1967). *The Cerebellum as a Neuronal Machine*. Springer. Azevedo and colleagues count roughly 69 of the brain's 86 billion neurons in the cerebellum.

[^28]: Napper, R. M. A., & Harvey, R. J. (1988). Number of parallel fiber synapses on an individual Purkinje cell in the cerebellum of the rat. *Journal of Comparative Neurology*, 274(2), 168–177; Eccles, J. C., Ito, M., & Szentágothai, J. (1967). *The Cerebellum as a Neuronal Machine*. Springer.

[^29]: Marr, D. (1969). A theory of cerebellar cortex. *Journal of Physiology*, 202(2), 437–470; Albus, J. S. (1971). A theory of cerebellar function. *Mathematical Biosciences*, 10(1–2), 25–61; Ito, M., Sakurai, M., & Tongroach, P. (1982). Climbing fibre induced depression of both mossy fibre responsiveness and glutamate sensitivity of cerebellar Purkinje cells. *Journal of Physiology*, 324, 113–134; Ito, M. (2001). Cerebellar long-term depression: Characterization, signal transduction, and functional roles. *Physiological Reviews*, 81(3), 1143–1195.

[^30]: Schonewille, M., Gao, Z., Boele, H.-J., Vinueza Veloz, M. F., Amerika, W. E., Šimek, A. A. M., De Jeu, M. T., Steinberg, J. P., Takamiya, K., Hoebeek, F. E., Linden, D. J., Huganir, R. L., & De Zeeuw, C. I. (2011). Reevaluating the role of LTD in cerebellar motor learning. *Neuron*, 70(1), 43–50; Heffley, W., Song, E. Y., Xu, Z., Taylor, B. N., Hughes, M. A., McKinney, A., Joshua, M., & Hull, C. (2018). Coordinated cerebellar climbing fiber activity signals learned sensorimotor predictions. *Nature Neuroscience*, 21(10), 1431–1441; Kostadinov, D., Beau, M., Blanco-Pozo, M., & Häusser, M. (2019). Predictive and reactive reward signals conveyed by climbing fiber inputs to cerebellar Purkinje cells. *Nature Neuroscience*, 22(6), 950–962. Schonewille and colleagues blocked parallel fiber long-term depression in three mouse lines and found vestibulo-ocular reflex adaptation and eyeblink conditioning intact.

[^31]: Wolpert, D. M., Miall, R. C., & Kawato, M. (1998). Internal models in the cerebellum. *Trends in Cognitive Sciences*, 2(9), 338–347.

[^32]: Holmes, G. (1939). The cerebellum of man. *Brain*, 62(1), 1–30.

[^33]: Andersen, P., Bliss, T. V. P., & Skrede, K. K. (1971). Lamellar organization of hippocampal excitatory pathways. *Experimental Brain Research*, 13(2), 222–238; Amaral, D. G., & Witter, M. P. (1989). The three-dimensional organization of the hippocampal formation: A review of anatomical data. *Neuroscience*, 31(3), 571–591.

[^34]: Leutgeb, J. K., Leutgeb, S., Moser, M.-B., & Moser, E. I. (2007). Pattern separation in the dentate gyrus and CA3 of the hippocampus. *Science*, 315(5814), 961–966.

[^35]: Marr, D. (1971). Simple memory: A theory for archicortex. *Philosophical Transactions of the Royal Society B*, 262(841), 23–81; Treves, A., & Rolls, E. T. (1994). Computational analysis of the role of the hippocampus in memory. *Hippocampus*, 4(3), 374–391; Nakazawa, K., Quirk, M. C., Chitwood, R. A., Watanabe, M., Yeckel, M. F., Sun, L. D., Kato, A., Carr, C. A., Johnston, D., Wilson, M. A., & Tonegawa, S. (2002). Requirement for hippocampal CA3 NMDA receptors in associative memory recall. *Science*, 297(5579), 211–218.

[^36]: Hasselmo, M. E., & Schnell, E. (1994). Laminar selectivity of the cholinergic suppression of synaptic transmission in rat hippocampal region CA1: Computational modeling and brain slice physiology. *Journal of Neuroscience*, 14(6), 3898–3914; Lisman, J. E., & Grace, A. A. (2005). The hippocampal-VTA loop: Controlling the entry of information into long-term memory. *Neuron*, 46(5), 703–713.

[^37]: Buzsáki, G. (2006). *Rhythms of the Brain*. Oxford University Press; Buzsáki, G., & Draguhn, A. (2004). Neuronal oscillations in cortical networks. *Science*, 304(5679), 1926–1929.

[^38]: Whittington, M. A., Traub, R. D., & Jefferys, J. G. R. (1995). Synchronized oscillations in interneuron networks driven by metabotropic glutamate receptor activation. *Nature*, 373, 612–615; Buzsáki, G., & Wang, X.-J. (2012). Mechanisms of gamma oscillations. *Annual Review of Neuroscience*, 35, 203–225; Cardin, J. A., Carlén, M., Meletis, K., Knoblich, U., Zhang, F., Deisseroth, K., Tsai, L.-H., & Moore, C. I. (2009). Driving fast-spiking cells induces gamma rhythm and controls sensory responses. *Nature*, 459, 663–667. Whittington and colleagues describe rhythm generated among interneurons alone; Cardin and colleagues, and Buzsáki and Wang, the loop between excitatory cells and interneurons.

[^39]: Fries, P. (2005). A mechanism for cognitive dynamics: Neuronal communication through neuronal coherence. *Trends in Cognitive Sciences*, 9(10), 474–480; Fries, P. (2015). Rhythms for cognition: Communication through coherence. *Neuron*, 88(1), 220–235.

[^40]: Schneider, M., Broggini, A. C., Dann, B., Tzanou, A., Uran, C., Sheshadri, S., Scherberger, H., & Vinck, M. (2021). A mechanism for inter-areal coherence through communication based on connectivity and oscillatory power. *Neuron*, 109(24), 4050–4067; Ray, S., & Maunsell, J. H. R. (2015). Do gamma oscillations play a role in cerebral cortex? *Trends in Cognitive Sciences*, 19(2), 78–85.

[^41]: O'Keefe, J., & Dostrovsky, J. (1971). The hippocampus as a spatial map: Preliminary evidence from unit activity in the freely-moving rat. *Brain Research*, 34(1), 171–175; O'Keefe, J., & Recce, M. L. (1993). Phase relationship between hippocampal place units and the EEG theta rhythm. *Hippocampus*, 3(3), 317–330; Skaggs, W. E., McNaughton, B. L., Wilson, M. A., & Barnes, C. A. (1996). Theta phase precession in hippocampal neuronal populations and the compression of temporal sequences. *Hippocampus*, 6(2), 149–172.

[^42]: Sporns, O., Tononi, G., & Kötter, R. (2005). The human connectome: A structural description of the human brain. *PLoS Computational Biology*, 1(4), e42; Bullmore, E., & Sporns, O. (2009). Complex brain networks: Graph theoretical analysis of structural and functional systems. *Nature Reviews Neuroscience*, 10(3), 186–198. The word connectome was introduced by Sporns, Tononi, and Kötter.

[^43]: Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. *Nature*, 393, 440–442; Bassett, D. S., & Bullmore, E. (2006). Small-world brain networks. *The Neuroscientist*, 12(6), 512–523; Chklovskii, D. B., Schikorski, T., & Stevens, C. F. (2002). Wiring optimization in cortical circuits. *Neuron*, 34(3), 341–347; Bullmore, E., & Sporns, O. (2012). The economy of brain network organization. *Nature Reviews Neuroscience*, 13(5), 336–349.

[^44]: van den Heuvel, M. P., & Sporns, O. (2011). Rich-club organization of the human connectome. *Journal of Neuroscience*, 31(44), 15775–15786.

[^45]: Crossley, N. A., Mechelli, A., Scott, J., Carletti, F., Fox, P. T., McGuire, P., & Bullmore, E. T. (2014). The hubs of the human connectome are generally implicated in the anatomy of brain disorders. *Brain*, 137(8), 2382–2395.

[^46]: Sherrington, C. S. (1940). *Man on His Nature*. Cambridge University Press.

[^47]: Cornford, J., Kalajdzievski, D., Leite, M., Lamarquette, A., Kullmann, D. M., & Richards, B. A. (2021). Learning to live with Dale's principle: ANNs with separate excitatory and inhibitory units. *International Conference on Learning Representations (ICLR)*.

[^48]: Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30.
