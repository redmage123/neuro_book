---
title: "Chapter 4"
subtitle: "Circuits, Networks, and Coordinated Behavior"
---

> *"... an enchanted loom where millions of flashing shuttles weave a dissolving pattern, always a meaningful pattern though never an abiding one."*
>
> --- Charles Sherrington, *Man on His Nature* (1940)

# From Cells to Circuits

The previous chapters built a neuron and then surrounded it with chemical context. A neuron integrates inputs, fires when a threshold is crossed, and changes physically when neuromodulators permit. That account is complete at the level of the cell. It explains almost nothing about behavior.

A single neuron cannot walk, breathe, decide, or remember. It cannot even compute a difference between two inputs in a way that outlasts the inputs themselves. Every capacity that we recognize as behavior belongs to groups of neurons connected in particular ways. The unit of function in the nervous system is not the neuron. It is the circuit.

This creates a problem of description. The human brain contains on the order of 86 billion neurons and hundreds of trillions of synapses.[^1] No account at the level of individual connections is possible, and none would be illuminating if it were. What makes circuits intelligible is that the nervous system reuses a small number of wiring patterns, at every scale, in every region. Learn the patterns and the regions become variations on a theme.

This chapter is about those patterns, the ways they are stacked into larger structures, and the rhythms that coordinate them. It ends where Chapter 1 began: with a system that produces coordinated behavior without anyone in charge.

# The Simplest Circuit

Sherrington's reflex arc remains the clearest place to start. A sensory neuron in a muscle spindle detects stretch. Its axon enters the spinal cord and synapses directly on a motor neuron, which contracts the same muscle. Tap the tendon below the kneecap, the quadriceps stretches, and the leg kicks. Two neurons, one synapse, no brain required.[^2]

Even this minimal circuit contains a second element that is easy to overlook. The same sensory axon also excites an inhibitory interneuron, which suppresses the motor neurons of the opposing muscle. The quadriceps contracts while the hamstring is actively prevented from resisting. This is reciprocal inhibition, and it is the first lesson of circuit organization: useful behavior requires turning things off as much as turning them on.[^3]

Reflexes are not primitive leftovers. They are the fastest and most reliable components of the motor system, and nearly everything the brain does with movement is built by modulating them.

# A Small Vocabulary of Motifs

Across the nervous system, a handful of wiring motifs recur. Figure 4.1 shows six of them. Each buys the organism something specific.

![Figure 4.1. Six circuit motifs that recur throughout the nervous system. Arrowheads mark excitatory synapses, filled circles inhibitory ones.](images/fig_motifs.png)

Feedforward excitation is the trivial case: a signal passes from one neuron to the next. Chains of it carry information from the senses toward the muscles. On its own it transmits but does not shape.

Feedforward inhibition adds a branch. The input excites a target neuron and, through an interneuron, inhibits the same target a millisecond or two later. The effect is a narrow window: the target can respond only to inputs that arrive close together in time. Inputs that straggle are cancelled. This motif turns a sluggish integrator into a coincidence detector, and it appears wherever timing precision matters, from the cerebellum to the auditory brainstem.[^4]

Feedback inhibition closes a loop. The target's own output recruits an interneuron that inhibits the target. The harder the population fires, the harder it is suppressed. This is a thermostat, and it is the primary reason cortical activity does not explode.[^5]

Lateral inhibition lets neighbors suppress one another. The neuron receiving the strongest input wins and silences its competitors. The consequences include sharpened contrast, winner-take-all selection, and the ability to represent a stimulus by which neuron is active rather than by how active everything is.[^6]

Recurrent excitation lets activity feed back on itself. A pattern of firing can be sustained after its input has gone, which is the basis of working memory and of pattern completion.[^7] It is also the most dangerous motif in the brain. Without inhibition to contain it, recurrent excitation is a seizure.

Disinhibition is inhibition of an inhibitor. A target is held silent by default; an input that suppresses the inhibitor releases the target. This sounds like a roundabout way to excite something, but it has a property direct excitation lacks: the default state is off, so nothing happens unless the circuit is explicitly opened. The basal ganglia, discussed below, are built almost entirely from it.[^8]

# Inhibition Is Not the Opposite of Excitation

Engineers encountering these motifs tend to file inhibition under "negative weights" and move on. That misses most of what inhibition does.

Roughly one in five cortical neurons is inhibitory, and those neurons come in dozens of types, each targeting a different part of the excitatory cell: the dendrites, the soma, the axon initial segment, or other interneurons.[^9] Because they target different compartments, they do different jobs. Inhibition at the dendrite vetoes particular inputs. Inhibition at the soma vetoes output. Inhibition at the axon initial segment controls exactly when a spike may leave.

Most importantly, excitation and inhibition are balanced. In an awake cortex, every excitatory input to a neuron is tracked by a nearly equal inhibitory input arriving a few milliseconds later.[^10] The neuron lives close to threshold, held there by two large forces that almost cancel. Small changes in either one move it across the line.

![Figure 4.2. A simulated population of excitatory neurons receiving a brief input (yellow). With no inhibition, recurrent excitation drives the population to its ceiling. With balanced inhibition, the response is brief and proportionate. With excessive inhibition, the input barely registers.](images/fig_ei.png)

Figure 4.2 shows why this arrangement is worth its cost. A recurrently connected excitatory population with no inhibition does not respond to an input; it runs away until every cell is firing flat out. Add inhibition that tracks the excitation and the same population produces a brief, bounded response that ends when the input ends. Add too much and the response is muted. The balanced regime is expensive, because two large currents are spent to produce a small net effect, and it is the only regime in which the circuit is both sensitive and stable.[^11]

Balance is also what makes the circuit fast. A neuron held near threshold by opposing forces can be flipped by a single well-timed input. A neuron resting far below threshold must be dragged up first. Inhibition is not the brake on the system. It is what makes the system responsive.[^12]

# Computation Before the Brain

The retina shows how much can be done with these motifs before any signal reaches the cortex.

![Figure 4.3. Santiago Ramón y Cajal's drawing of the vertebrate retina. Light enters from the left and crosses several layers of neurons before reaching the photoreceptors at the right; the processed signal leaves through the ganglion cell axons at the far left.](images/retina.png)

Light falls on photoreceptors, but the signal that leaves the eye has already passed through three layers of circuitry. Horizontal cells implement lateral inhibition across the photoreceptor layer, so a uniformly lit region produces little output while an edge produces a strong one. Amacrine cells add feedforward and feedback inhibition that make ganglion cells sensitive to change in time as well as space. By the time the optic nerve leaves the eye, the image has been converted into a map of edges and changes. Uniform brightness, which carries no information, has been largely discarded.[^13]

The familiar illusion of Mach bands, in which a gradient appears to have bright and dark fringes at its boundaries, is lateral inhibition made visible. It is not an error. It is the signature of a circuit that trades a faithful copy of the input for an informative one, under a strict budget of axons.[^14]

# Circuits That Generate Their Own Rhythm

Some circuits do not wait for input at all.

Walking, swimming, breathing, chewing, and the peristalsis of the gut are rhythmic, and the rhythm is generated by small networks in the spinal cord and brainstem called central pattern generators.[^15] The surprising fact, established in the early twentieth century and confirmed many times since, is that these networks produce their rhythm without any rhythmic input. A spinal cord isolated from the brain and from sensory feedback will still generate the alternating pattern of locomotion when given a steady chemical or electrical drive.[^16]

![Figure 4.4. A half-center oscillator. Two populations inhibit each other and each fatigues while active. Given a constant drive, they alternate: the active side tires, the suppressed side escapes, and the cycle repeats.](images/fig_cpg.png)

The minimal pattern generator is the half-center oscillator in Figure 4.4. Two populations inhibit each other, so only one can be active at a time. Each population also fatigues while active, through adaptation in its neurons or depression at its synapses. The active side weakens, its grip on the other side loosens, the other side escapes and takes over, and the cycle repeats. Mutual inhibition plus fatigue produces alternation from a constant input.[^17]

Sensory feedback does not drive the rhythm; it tunes it. Signals from the limbs adjust timing and amplitude so that a walking pattern survives a stone underfoot. The division of labor is the one Chapter 1 proposed: the controller generates, the world corrects.[^18]

# The Cortical Microcircuit

The cerebral cortex is a sheet a few millimeters thick, folded to fit the skull. Across its entire surface it is built from the same six-layered circuit, repeated millions of times.

![Figure 4.5. Three of Cajal's drawings of the cerebral cortex, stained to show cell bodies (left), the full extent of a few neurons (center), and the fibers connecting layers (right). The six layers are visible as bands of differing cell density.](images/cajal_cortex.png)

Input from the thalamus, the cortex's gateway for the senses, arrives mainly in layer 4. Layer 4 neurons project upward to layers 2 and 3, where most local processing and most connections to other cortical areas occur. Layers 2 and 3 project down to layer 5, which sends the cortex's output to the brainstem, spinal cord, and basal ganglia. Layer 6 projects back to the thalamus, closing a loop that lets the cortex modulate its own input.[^19]

Within this stack, every motif from Figure 4.1 is present. Feedforward inhibition sharpens the timing of thalamic input. Recurrent excitation among layer 2 and 3 neurons sustains and amplifies patterns. Feedback and lateral inhibition keep the amplification bounded. The whole arrangement has been called the canonical microcircuit, and it is approximately the same whether the cortex in question is processing vision, sound, touch, language, or plans.[^20]

![Figure 4.6. A three-dimensional reconstruction of five neighboring columns in rat somatosensory cortex, each corresponding to one whisker. The six layers run horizontally; the columns run vertically through all of them.](images/columns.jpg)

Vertically, neurons that share a layer stack also share their inputs, forming columns like those in Figure 4.6. A column in visual cortex responds to one orientation at one location; a column in somatosensory cortex responds to one whisker.[^21] The column is not a rigid unit, and its boundaries blur in many species, but the principle is robust: the cortex is a tiled array of nearly identical circuits, differing mostly in what they are connected to.[^22]

This is the strongest hint in neuroanatomy that cortical computation is general. The same circuit learns to see or to hear depending on where its input comes from, which is why, in a famous series of experiments, visual input rerouted to auditory cortex during development produced a cortex that could see.[^23]

# Two Loops for Action

The cortex proposes. Two subcortical systems dispose, in different ways.

The basal ganglia solve the problem of selection. At any moment the cortex represents many candidate actions in parallel, and the body can perform only one. The basal ganglia are built almost entirely from the disinhibition motif. Their output nuclei fire continuously, holding the thalamus and brainstem motor circuits under tonic inhibition, so that by default no action is released. A cortical pattern that excites the striatum, the input stage, inhibits the inhibitors covering one action, and that action alone is freed.[^24]

![Figure 4.7. The direct pathway through the basal ganglia. Output nuclei inhibit motor targets by default; the striatum selects an action by inhibiting the inhibition that covers it. Dopamine sets how readily the striatum does this.](images/fig_bg.png)

The design has two features that matter. Because the default is off, the system fails safe: damage tends to produce too little movement, as in Parkinson's disease, rather than uncontrolled movement.[^25] And because dopamine acts on the striatum, the prediction error of Chapter 3 arrives at exactly the synapses that decide which action is released. The basal ganglia are where "learning should happen now" meets "this is what was chosen." Habits are the result.[^26]

The cerebellum solves a different problem: precision. It contains more neurons than the rest of the brain combined, arranged in a circuit of striking regularity.[^27] Each Purkinje cell receives about two hundred thousand weak inputs from parallel fibers, carrying the current state of the body and the current motor command, and a single powerful input from one climbing fiber, which fires when a movement goes wrong.[^28]

![Figure 4.8. The cerebellar microcircuit. Mossy fibers (MF) and parallel fibers (PF) carry context to the Purkinje cell (PC); a single climbing fiber (CF) from the inferior olive (IO) carries an error signal. Purkinje cells inhibit the deep cerebellar nuclei (DCN), the cerebellum's output.](images/cereb2.png)

The climbing fiber is a teaching signal. When it fires, the parallel fiber synapses that were recently active are weakened, which is an eligibility trace mechanism of the kind Chapter 3 described, implemented in a circuit so regular that it was one of the first to be modeled mathematically.[^29] Over repetitions, the cerebellum learns to predict the sensory consequences of a command and to issue corrections before errors occur.[^30] Reaching, balance, eye movements, and the timing of speech all depend on it. Its lesions do not abolish movement; they make movement clumsy.[^31]

# The Hippocampal Loop

The hippocampus is the circuit most closely identified with memory, and its anatomy is a chain of the motifs already described.[^32]

![Figure 4.9. Cajal's drawing of the hippocampal formation, with a modern summary of its main pathway: entorhinal cortex (EC) to dentate gyrus (DG) to CA3 to CA1 and back to entorhinal cortex.](images/hippo.png)

Cortical input enters through the entorhinal cortex and passes to the dentate gyrus, whose sparse, strongly inhibited granule cells make similar inputs less similar, a process called pattern separation.[^33] The dentate projects to CA3, whose pyramidal cells are densely connected to one another: recurrent excitation on a large scale. A partial cue that activates some CA3 cells can regenerate the whole pattern, which is pattern completion.[^34] CA3 projects to CA1, which compares the retrieved pattern with the current input and returns the result to the cortex.[^35]

Separation, storage, completion, and comparison, in that order, each implemented by a motif from Figure 4.1. The circuit is described here only in outline; Chapter 5 returns to how its synapses change.

# Rhythms

If circuits are the brain's structure, rhythms are its timing.

Record from the scalp and you see oscillations: slow waves during deep sleep, theta during exploration and memory tasks, alpha over idle cortex, beta while a posture or a plan is held, and fast gamma wherever local processing is intense. Figure 4.10 shows one second of each.[^36]

![Figure 4.10. One second of scalp EEG filtered into four frequency bands. Each band is associated with a characteristic behavioral state, though the associations are statistical rather than exclusive.](images/fig_rhythms.png)

Oscillations are the collective behavior of circuits built from the motifs above. Feedback inhibition is intrinsically rhythmic: excitation recruits inhibition, inhibition silences excitation, inhibition decays, excitation recovers. A population of excitatory cells coupled to a population of fast interneurons oscillates in the gamma range for exactly this reason.[^37]

Rhythms do work. A neuron is most excitable at one phase of the oscillation and least at the opposite phase, so a shared rhythm creates windows during which inputs are effective. Two regions oscillating in phase can communicate; two regions out of phase cannot, even if they are wired together. Changing the phase relation changes the effective wiring without changing a synapse. This is the brain's answer to a problem every large network has: how to route information through fixed connections.[^38]

Rhythms also coordinate learning. In the hippocampus, place cells fire at progressively earlier phases of the theta cycle as an animal crosses a location, compressing a sequence of seconds into a sequence of tens of milliseconds. That compressed sequence falls within the window in which synapses can change. The rhythm converts experience into a format plasticity can use.[^39]

# The Architecture of the Whole

Step back from any single region and the brain is a network of regions.[^43] Its wiring is neither random nor fully regular, and the compromise it strikes is the same one found in power grids, social networks, and the internet.

![Figure 4.11. A small-world network: most connections are local, a few are long-range. The result is dense local clustering with short paths between any two nodes.](images/ws.png)

Most connections are short, linking neighbors into dense clusters. A minority are long, linking clusters to one another. The result is a small-world network: any two neurons are only a few synapses apart, yet almost all wiring is local and cheap. Long axons are metabolically expensive, occupy volume, and slow signals, so the brain uses as few of them as it can while keeping the path length between regions short.[^40]

![Figure 4.12. Long-range fiber tracts of the human brain reconstructed from diffusion MRI, viewed from above. Colors indicate fiber direction.](images/connectome.png)

A few regions are hubs with far more long-range connections than average, and these hubs are disproportionately connected to one another, forming a core through which most long-distance traffic passes.[^41] The arrangement is efficient and fragile in the same way an airline network is: it makes the system fast, and it makes damage to a hub far more consequential than damage elsewhere. Several neurological and psychiatric conditions are now described, at least in part, as disorders of the hubs.[^42]

# Coordination Without a Conductor

Chapter 1 claimed that the brain has no central controller. This chapter has described the machinery that makes a controller unnecessary.

Reflexes handle the fastest demands locally. Pattern generators produce rhythmic behavior on their own and accept correction from the body. Balanced inhibition keeps every circuit sensitive without letting it run away. The basal ganglia release one action at a time by default silence. The cerebellum corrects movements before errors are felt. Rhythms decide which regions can talk to which, moment by moment. A small-world wiring plan keeps all of this within a few synapses of everything else.

No component sees the whole. Each solves a local problem using the same small vocabulary of motifs, and the behavior of the animal is what those local solutions add up to. The pattern is meaningful, as Sherrington said, and never abiding: it is re-created from moment to moment by circuits that were never designed to produce it.[^44]

# Implications for Artificial Intelligence

Artificial neural networks borrowed the neuron and left the circuit behind. Several of this chapter's lessons bear directly on how that might be repaired.

First, inhibition is not a negative weight. In most artificial networks a unit's output can be positive or negative, and nothing enforces balance. Biological circuits maintain excitation and inhibition as separate populations and keep them in near-cancellation, which buys speed, stability, and sensitivity at once. Architectures that enforce this division are a largely unexplored design space.[^45]

Second, selection by disinhibition is a different control strategy from choosing the largest output. The basal ganglia hold all actions off by default and release one. The default of silence makes the system fail safe and makes "do nothing" a first-class action, which is often what an agent in an uncertain environment should do.

Third, rhythm is a routing mechanism. Fixed weights cannot change which parts of a network talk to each other, so artificial systems add attention mechanisms to do it.[^46] The brain does it with phase. Oscillatory gating offers a way to reconfigure effective connectivity without changing parameters, at low cost.

Fourth, the brain's wiring budget shapes its architecture. Small-world organization, local clustering, and sparse long-range connections are consequences of paying for every axon. Artificial networks pay nothing for connections and are correspondingly dense. As energy becomes the binding constraint on large models, the brain's economies are worth studying.

Finally, the cortex suggests that general computation can come from a single repeated circuit with different inputs. The question of what that circuit is doing, in a form abstract enough to transfer, remains open. It is one of the most important open problems in both neuroscience and machine learning.

# The Central Lesson

Behavior belongs to circuits, not cells. The nervous system builds its circuits from a small vocabulary of motifs in which inhibition does most of the shaping, stacks them into regions that each solve one kind of problem, and coordinates the regions through rhythm and a wiring plan that keeps everything close. No part is in charge. Coordinated behavior is what the parts produce together.

# Next Chapter

Chapter 5: Plasticity and Memory --- How Experience Becomes Structure

# References and Attribution

## Figure Attribution

Figures 4.1, 4.2, 4.4, and 4.7 were drawn for this book. Figure 4.2 and the output trace in Figure 4.4 are simulations of simple rate models.

Figure 4.3: Santiago Ramón y Cajal, structure of the mammalian retina (1900), public domain, via Wikimedia Commons.

Figure 4.5: Santiago Ramón y Cajal, drawings of the cerebral cortex (1899), public domain, via Wikimedia Commons.

Figure 4.6: "Cortical Columns," underlying image from Marcel Oberländer, Beyond the Cortical Column, Neuroinformatics 2012; composite by Wikimedia Commons user Bodysurfinyon, CC BY-SA 4.0.

Figure 4.8: "CerebCircuit" by Wikipedia user Nrets, CC BY-SA 3.0, via Wikimedia Commons.

Figure 4.9: Santiago Ramón y Cajal, drawing of the hippocampus (1911), public domain, with circuit inset added by Wikimedia Commons contributors.

Figure 4.10: EEG band traces by Hugo Gamboa, CC BY-SA 3.0, via Wikimedia Commons; composite drawn for this book.

Figure 4.11: "Watts-Strogatz small-world model, 100 nodes" by Wikimedia Commons user Keiono, CC BY-SA 3.0.

Figure 4.12: "The Human Connectome" by Wikimedia Commons user Andreashorn, CC BY-SA 4.0.

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

Holmes, G. (1939). The cerebellum of man. *Brain*, 62(1), 1–30.

Horton, J. C., & Adams, D. L. (2005). The cortical column: A structure without a function. *Philosophical Transactions of the Royal Society B*, 360(1456), 837–862.

Hubel, D. H., & Wiesel, T. N. (1962). Receptive fields, binocular interaction and functional architecture in the cat's visual cortex. *Journal of Physiology*, 160(1), 106–154.

Isaacson, J. S., & Scanziani, M. (2011). How inhibition shapes cortical activity. *Neuron*, 72(2), 231–243.

Ito, M. (2001). Cerebellar long-term depression: Characterization, signal transduction, and functional roles. *Physiological Reviews*, 81(3), 1143–1195.

Ito, M., Sakurai, M., & Tongroach, P. (1982). Climbing fibre induced depression of both mossy fibre responsiveness and glutamate sensitivity of cerebellar Purkinje cells. *Journal of Physiology*, 324, 113–134.

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

Pi, H.-J., Hangya, B., Kvitsiani, D., Sanders, J. I., Huang, Z. J., & Kepecs, A. (2013). Cortical interneurons that specialize in disinhibitory control. *Nature*, 503, 521–524.

Pouille, F., & Scanziani, M. (2001). Enforcement of temporal fidelity in pyramidal cells by somatic feed-forward inhibition. *Science*, 293(5532), 1159–1163.

Ratliff, F. (1965). *Mach Bands: Quantitative Studies on Neural Networks in the Retina*. Holden-Day.

Redgrave, P., Prescott, T. J., & Gurney, K. (1999). The basal ganglia: A vertebrate solution to the selection problem? *Neuroscience*, 89(4), 1009–1023.

Reynolds, J. N. J., Hyland, B. I., & Wickens, J. R. (2001). A cellular mechanism of reward-related learning. *Nature*, 413, 67–70.

Rossignol, S., Dubuc, R., & Gossard, J.-P. (2006). Dynamic sensorimotor interactions in locomotion. *Physiological Reviews*, 86(1), 89–154.

Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. *Science*, 275(5306), 1593–1599.

Shadlen, M. N., & Newsome, W. T. (1998). The variable discharge of cortical neurons: Implications for connectivity, computation, and information coding. *Journal of Neuroscience*, 18(10), 3870–3896.

Sherrington, C. S. (1906). *The Integrative Action of the Nervous System*. Yale University Press.

Sherrington, C. S. (1940). *Man on His Nature*. Cambridge University Press.

Skaggs, W. E., McNaughton, B. L., Wilson, M. A., & Barnes, C. A. (1996). Theta phase precession in hippocampal neuronal populations and the compression of temporal sequences. *Hippocampus*, 6(2), 149–172.

Smith, J. C., Ellenberger, H. H., Ballanyi, K., Richter, D. W., & Feldman, J. L. (1991). Pre-Bötzinger complex: A brainstem region that may generate respiratory rhythm in mammals. *Science*, 254(5032), 726–729.

Sporns, O., Tononi, G., & Kötter, R. (2005). The human connectome: A structural description of the human brain. *PLoS Computational Biology*, 1(4), e42.

Sur, M., Garraghty, P. E., & Roe, A. W. (1988). Experimentally induced visual projections into auditory thalamus and cortex. *Science*, 242(4884), 1437–1441.

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

[^1]: Azevedo, F. A. C., Carvalho, L. R. B., Grinberg, L. T., Farfel, J. M., Ferretti, R. E. L., Leite, R. E. P., Jacob Filho, W., Lent, R., & Herculano-Houzel, S. (2009). Equal numbers of neuronal and nonneuronal cells make the human brain an isometrically scaled-up primate brain. *Journal of Comparative Neurology*, 513(5), 532–541.

[^2]: Sherrington, C. S. (1906). *The Integrative Action of the Nervous System*. Yale University Press; Liddell, E. G. T., & Sherrington, C. S. (1924). Reflexes in response to stretch (myotatic reflexes). *Proceedings of the Royal Society B*, 96, 212–242.

[^3]: Sherrington, C. S. (1906). *The Integrative Action of the Nervous System*. Yale University Press. Sherrington introduced the term reciprocal innervation in a series of notes to the Royal Society from 1893 onward and summarized the principle in the 1906 lectures.

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

[^17]: Brown, T. G. (1914). On the nature of the fundamental activity of the nervous centres; together with an analysis of the conditioning of rhythmic activity in progression, and a theory of the evolution of function in the nervous system. *Journal of Physiology*, 48(1), 18–46. Brown's 1914 paper proposed the half-centre model.

[^18]: Rossignol, S., Dubuc, R., & Gossard, J.-P. (2006). Dynamic sensorimotor interactions in locomotion. *Physiological Reviews*, 86(1), 89–154.

[^19]: Douglas, R. J., & Martin, K. A. C. (2004). Neuronal circuits of the neocortex. *Annual Review of Neuroscience*, 27, 419–451; Harris, K. D., & Shepherd, G. M. G. (2015). The neocortical circuit: Themes and variations. *Nature Neuroscience*, 18(2), 170–181.

[^20]: Douglas, R. J., Martin, K. A. C., & Whitteridge, D. (1989). A canonical microcircuit for neocortex. *Neural Computation*, 1(4), 480–488; Douglas, R. J., & Martin, K. A. C. (2004). Neuronal circuits of the neocortex. *Annual Review of Neuroscience*, 27, 419–451.

[^21]: Mountcastle, V. B. (1957). Modality and topographic properties of single neurons of cat's somatic sensory cortex. *Journal of Neurophysiology*, 20(4), 408–434; Hubel, D. H., & Wiesel, T. N. (1962). Receptive fields, binocular interaction and functional architecture in the cat's visual cortex. *Journal of Physiology*, 160(1), 106–154.

[^22]: Horton, J. C., & Adams, D. L. (2005). The cortical column: A structure without a function. *Philosophical Transactions of the Royal Society B*, 360(1456), 837–862.

[^23]: Sur, M., Garraghty, P. E., & Roe, A. W. (1988). Experimentally induced visual projections into auditory thalamus and cortex. *Science*, 242(4884), 1437–1441; von Melchner, L., Pallas, S. L., & Sur, M. (2000). Visual behaviour mediated by retinal projections directed to the auditory pathway. *Nature*, 404, 871–876.

[^24]: Chevalier, G., & Deniau, J. M. (1990). Disinhibition as a basic process in the expression of striatal functions. *Trends in Neurosciences*, 13(7), 277–280; Mink, J. W. (1996). The basal ganglia: Focused selection and inhibition of competing motor programs. *Progress in Neurobiology*, 50(4), 381–425; Redgrave, P., Prescott, T. J., & Gurney, K. (1999). The basal ganglia: A vertebrate solution to the selection problem? *Neuroscience*, 89(4), 1009–1023.

[^25]: Alexander, G. E., DeLong, M. R., & Strick, P. L. (1986). Parallel organization of functionally segregated circuits linking basal ganglia and cortex. *Annual Review of Neuroscience*, 9, 357–381; Albin, R. L., Young, A. B., & Penney, J. B. (1989). The functional anatomy of basal ganglia disorders. *Trends in Neurosciences*, 12(10), 366–375; DeLong, M. R. (1990). Primate models of movement disorders of basal ganglia origin. *Trends in Neurosciences*, 13(7), 281–285.

[^26]: Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. *Science*, 275(5306), 1593–1599; Reynolds, J. N. J., Hyland, B. I., & Wickens, J. R. (2001). A cellular mechanism of reward-related learning. *Nature*, 413, 67–70; Graybiel, A. M. (2008). Habits, rituals, and the evaluative brain. *Annual Review of Neuroscience*, 31, 359–387; Yin, H. H., & Knowlton, B. J. (2006). The role of the basal ganglia in habit formation. *Nature Reviews Neuroscience*, 7(6), 464–476.

[^27]: Azevedo, F. A. C., Carvalho, L. R. B., Grinberg, L. T., Farfel, J. M., Ferretti, R. E. L., Leite, R. E. P., Jacob Filho, W., Lent, R., & Herculano-Houzel, S. (2009). Equal numbers of neuronal and nonneuronal cells make the human brain an isometrically scaled-up primate brain. *Journal of Comparative Neurology*, 513(5), 532–541; Eccles, J. C., Ito, M., & Szentágothai, J. (1967). *The Cerebellum as a Neuronal Machine*. Springer. Azevedo and colleagues count roughly 69 of the brain's 86 billion neurons in the cerebellum.

[^28]: Napper, R. M. A., & Harvey, R. J. (1988). Number of parallel fiber synapses on an individual Purkinje cell in the cerebellum of the rat. *Journal of Comparative Neurology*, 274(2), 168–177; Eccles, J. C., Ito, M., & Szentágothai, J. (1967). *The Cerebellum as a Neuronal Machine*. Springer.

[^29]: Marr, D. (1969). A theory of cerebellar cortex. *Journal of Physiology*, 202(2), 437–470; Albus, J. S. (1971). A theory of cerebellar function. *Mathematical Biosciences*, 10(1–2), 25–61; Ito, M., Sakurai, M., & Tongroach, P. (1982). Climbing fibre induced depression of both mossy fibre responsiveness and glutamate sensitivity of cerebellar Purkinje cells. *Journal of Physiology*, 324, 113–134; Ito, M. (2001). Cerebellar long-term depression: Characterization, signal transduction, and functional roles. *Physiological Reviews*, 81(3), 1143–1195.

[^30]: Wolpert, D. M., Miall, R. C., & Kawato, M. (1998). Internal models in the cerebellum. *Trends in Cognitive Sciences*, 2(9), 338–347.

[^31]: Holmes, G. (1939). The cerebellum of man. *Brain*, 62(1), 1–30.

[^32]: Andersen, P., Bliss, T. V. P., & Skrede, K. K. (1971). Lamellar organization of hippocampal excitatory pathways. *Experimental Brain Research*, 13(2), 222–238; Amaral, D. G., & Witter, M. P. (1989). The three-dimensional organization of the hippocampal formation: A review of anatomical data. *Neuroscience*, 31(3), 571–591.

[^33]: Leutgeb, J. K., Leutgeb, S., Moser, M.-B., & Moser, E. I. (2007). Pattern separation in the dentate gyrus and CA3 of the hippocampus. *Science*, 315(5814), 961–966.

[^34]: Marr, D. (1971). Simple memory: A theory for archicortex. *Philosophical Transactions of the Royal Society B*, 262(841), 23–81; Treves, A., & Rolls, E. T. (1994). Computational analysis of the role of the hippocampus in memory. *Hippocampus*, 4(3), 374–391; Nakazawa, K., Quirk, M. C., Chitwood, R. A., Watanabe, M., Yeckel, M. F., Sun, L. D., Kato, A., Carr, C. A., Johnston, D., Wilson, M. A., & Tonegawa, S. (2002). Requirement for hippocampal CA3 NMDA receptors in associative memory recall. *Science*, 297(5579), 211–218.

[^35]: Lisman, J. E., & Grace, A. A. (2005). The hippocampal-VTA loop: Controlling the entry of information into long-term memory. *Neuron*, 46(5), 703–713.

[^36]: Buzsáki, G. (2006). *Rhythms of the Brain*. Oxford University Press; Buzsáki, G., & Draguhn, A. (2004). Neuronal oscillations in cortical networks. *Science*, 304(5679), 1926–1929.

[^37]: Whittington, M. A., Traub, R. D., & Jefferys, J. G. R. (1995). Synchronized oscillations in interneuron networks driven by metabotropic glutamate receptor activation. *Nature*, 373, 612–615; Buzsáki, G., & Wang, X.-J. (2012). Mechanisms of gamma oscillations. *Annual Review of Neuroscience*, 35, 203–225; Cardin, J. A., Carlén, M., Meletis, K., Knoblich, U., Zhang, F., Deisseroth, K., Tsai, L.-H., & Moore, C. I. (2009). Driving fast-spiking cells induces gamma rhythm and controls sensory responses. *Nature*, 459, 663–667.

[^38]: Fries, P. (2005). A mechanism for cognitive dynamics: Neuronal communication through neuronal coherence. *Trends in Cognitive Sciences*, 9(10), 474–480; Fries, P. (2015). Rhythms for cognition: Communication through coherence. *Neuron*, 88(1), 220–235.

[^39]: O'Keefe, J., & Dostrovsky, J. (1971). The hippocampus as a spatial map: Preliminary evidence from unit activity in the freely-moving rat. *Brain Research*, 34(1), 171–175; O'Keefe, J., & Recce, M. L. (1993). Phase relationship between hippocampal place units and the EEG theta rhythm. *Hippocampus*, 3(3), 317–330; Skaggs, W. E., McNaughton, B. L., Wilson, M. A., & Barnes, C. A. (1996). Theta phase precession in hippocampal neuronal populations and the compression of temporal sequences. *Hippocampus*, 6(2), 149–172.

[^40]: Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. *Nature*, 393, 440–442; Bassett, D. S., & Bullmore, E. (2006). Small-world brain networks. *The Neuroscientist*, 12(6), 512–523; Chklovskii, D. B., Schikorski, T., & Stevens, C. F. (2002). Wiring optimization in cortical circuits. *Neuron*, 34(3), 341–347; Bullmore, E., & Sporns, O. (2012). The economy of brain network organization. *Nature Reviews Neuroscience*, 13(5), 336–349.

[^41]: van den Heuvel, M. P., & Sporns, O. (2011). Rich-club organization of the human connectome. *Journal of Neuroscience*, 31(44), 15775–15786.

[^42]: Crossley, N. A., Mechelli, A., Scott, J., Carletti, F., Fox, P. T., McGuire, P., & Bullmore, E. T. (2014). The hubs of the human connectome are generally implicated in the anatomy of brain disorders. *Brain*, 137(8), 2382–2395.

[^43]: Sporns, O., Tononi, G., & Kötter, R. (2005). The human connectome: A structural description of the human brain. *PLoS Computational Biology*, 1(4), e42; Bullmore, E., & Sporns, O. (2009). Complex brain networks: Graph theoretical analysis of structural and functional systems. *Nature Reviews Neuroscience*, 10(3), 186–198. The word connectome was introduced by Sporns, Tononi, and Kötter.

[^44]: Sherrington, C. S. (1940). *Man on His Nature*. Cambridge University Press.

[^45]: Cornford, J., Kalajdzievski, D., Leite, M., Lamarquette, A., Kullmann, D. M., & Richards, B. A. (2021). Learning to live with Dale's principle: ANNs with separate excitatory and inhibitory units. *International Conference on Learning Representations (ICLR)*.

[^46]: Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30.
