---
title: "Chapter 2"
subtitle: "Neurons: The Brain's Signaling Cells"
---

# Introduction

In the previous chapter, we argued that the brain is not a digital computer, but a physical, biological system shaped by evolutionary constraint. That argument now demands specificity. If cognition arises from matter, what kind of matter can support perception, memory, and action?

The answer is deceptively simple: the neuron.[^1]

Neurons are not abstract processing units. They are living cells, governed by the same physical and chemical laws as every other biological system. They consume energy, maintain internal order, respond to stress, and eventually fail. And yet, when organized in vast networks, they give rise to perception, memory, emotion, and thought.

This chapter introduces neurons not as symbols or algorithms, but as physical signaling systems whose structure and limitations shape everything the brain can do.

# What a Neuron Is --- and What It Is Not

A neuron is a cell. That statement is easy to say and easy to forget.

Neurons are not logic gates. They do not execute instructions, store variables, or manipulate symbols. Those descriptions are metaphors imposed at higher levels of analysis.[^2] At the level of mechanism, neurons integrate physical inputs and generate physical outputs according to biophysical rules.

Like all cells, neurons are bounded by a membrane.[^3] Inside that membrane is a dense molecular environment filled with proteins, structural elements, and chemical machinery. Energy is consumed continuously simply to maintain this ordered state against entropy.[^4]

What distinguishes neurons from most other cells is excitability: the ability to generate electrical signals, transmit them over distance, influence other cells, and modify those influences over time.[^5]

![Figure 2.1. A neuron is a living cell. A membrane separates two salt solutions; pumps burn ATP continuously to keep sodium out and potassium in, and gated channels let ions cross when the cell signals. Nothing here is a logic gate.](images/fig_cell.png)

# The Polarized Structure of Neurons

Despite their diversity, most neurons share a common structural plan that immediately constrains how information can flow.

At one end are dendrites: branching structures that receive signals from other neurons. These inputs are local, chemical, and numerous. A single neuron may receive thousands of such inputs.[^6]

At the center is the cell body, or soma. This is where incoming signals are integrated and where the cell's metabolic machinery resides.

Extending from the soma is the axon, a long, thin projection capable of transmitting electrical signals over distance. At its far end, the axon branches into terminals that form connections with other cells.

This polarized structure---many inputs, one output---is fundamental.[^7]

![Figure 2.2. The polarized plan of a neuron. Thousands of inputs arrive on the dendrites and soma; a single axon, decided at the initial segment and insulated by myelin, carries the one output to the terminals. Signals travel one way.](images/fig_polarized.png)

# The Physical Form of Inputs to a Neuron

Neurons receive their inputs primarily on dendrites, through specialized junctions called synapses.[^8]

At a typical chemical synapse, an incoming action potential in a presynaptic neuron triggers the release of neurotransmitter molecules into a tiny gap. These molecules diffuse across the gap and bind to receptors on the dendritic membrane of the receiving neuron.[^9]

The crucial point is this: the immediate input to a neuron is not an electrical spike, but a small, local chemical event that produces a graded electrical change.[^10]

![Figure 2.3. A chemical synapse. An action potential arriving at the terminal opens calcium channels; calcium triggers vesicles to release neurotransmitter into the cleft; the transmitter binds receptors on the postsynaptic membrane and produces a small graded potential, then is cleared by reuptake, breakdown, and diffusion.](images/figure_2_3.png)

# Excitatory and Inhibitory Postsynaptic Potentials (EPSPs and IPSPs)

Not all synaptic inputs push a neuron toward firing. Some do the opposite.

When a neurotransmitter binds to receptors on a dendrite or soma, it changes the permeability of the membrane to specific ions. The direction of this change determines whether the synapse is excitatory or inhibitory.

An excitatory postsynaptic potential (EPSP) slightly depolarizes the membrane, moving it closer to the threshold required to trigger an action potential at the axon initial segment. EPSPs are commonly produced by synapses that allow positive ions, such as sodium, to enter the cell.[^11]

An inhibitory postsynaptic potential (IPSP) hyperpolarizes the membrane or stabilizes it against depolarization. IPSPs move the membrane potential farther from threshold and reduce the likelihood that the neuron will fire. These effects are often mediated by chloride or potassium ions.[^12]

EPSPs and IPSPs are graded, local, and short-lived. Neurons continuously sum thousands of such inputs across their dendritic tree and soma. Firing reflects the balance of excitation and inhibition over time.[^13]

![Figure 2.4. Excitatory and inhibitory postsynaptic potentials. A: one EPSP depolarizes the membrane a few millivolts. B: one IPSP hyperpolarizes it. C: five EPSPs in quick succession sum to threshold and trigger an action potential. D: an EPSP and an IPSP arriving together nearly cancel. Traces are simulations with exponential synaptic kernels, not recordings.](images/fig_psp.png)

# Dendrites and Soma: Passive Integration

The electrical changes produced at synapses spread through the dendrites and into the soma. This spread is passive.

Voltage changes weaken with distance and time.[^14] No new electrical signal is regenerated. The soma acts as an integrator, summing excitatory and inhibitory influences across space and time.

Importantly, the soma does not normally propagate action potentials.

# The Axon Initial Segment: Where Spikes Begin

Just beyond the soma lies the axon initial segment.

This region is densely packed with voltage-gated sodium channels.[^15] If the integrated voltage arriving from the soma exceeds threshold here, an action potential is triggered.[^16]

This is the transformation from graded input to discrete output.

![Figure 2.5. The axon initial segment. Top: voltage-gated sodium channels are sparse in the soma and densest in the first stretch of axon, which therefore has the lowest threshold. Bottom: the soma's graded sum of inputs (blue) crosses threshold there and the initial segment fires a stereotyped spike (red). Simulated traces.](images/fig_ais.png)

# How the Action Potential Propagates

Once initiated, the action potential propagates along the axon.

Each segment of axon opens sodium channels, injecting current into neighboring regions. Those regions reach threshold and regenerate the spike using their own ion gradients.[^17]

Nothing travels the length of the axon except causation.

![Figure 2.6. How the action potential travels. A: in a bare axon, sodium entering the active patch spreads inside and brings the next patch to threshold, while the patch behind is refractory; the spike is regenerated at every point. B: in a myelinated axon, channels are confined to the nodes and the spike jumps from node to node.](images/fig_propagation.png)

# Why the Soma Does Not Propagate Spikes

The soma lacks the channel density required for reliable propagation. It is optimized for integration, not transmission.

Evolution separated integration, decision, and transmission into distinct regions.

# Timing, Not Amplitude, Carries Information

Action potentials are uniform in size.[^18] Information is encoded in timing, firing rate, and coordination across neurons.[^19]

![Figure 2.7. Spikes are all the same size. A: a stronger stimulus produces more spikes, not larger ones. B: the same number of spikes arranged as bursts carries a different message. Information lies in rate and timing. Simulated traces.](images/fig_timing.png)

# Plasticity: Learning as Physical Change

Synapses strengthen or weaken with use.[^20] Learning is physical reconfiguration, not information storage.

![Figure 2.8. Learning as physical change. Before: a weak synapse with few vesicles and few receptors gives a small EPSP. After repeated correlated activity, the same synapse holds more vesicles, a larger spine head and more receptors, and the EPSP more than doubles. Simulated traces.](images/fig_plasticity.png)

# Why Neurons Look Inefficient --- and Why They Are Not

Neurons are slow, noisy, and metabolically expensive.[^21] These properties enable robustness and adaptability.

![Figure 2.9. Slow, noisy and expensive. A: a spike lasts about a millisecond, ten million times longer than a transistor switch. B: the same stimulus gives a different spike pattern on every trial (simulated raster). C: the brain is about 2 percent of body mass but uses about 20 percent of resting energy.](images/fig_costs.png)

# Looking Ahead

Neurons do not operate in a fixed mode. Their behavior is shaped by chemical context.

The next chapter introduces neuromodulators---signals that change how neurons operate, learn, and adapt.

Next Chapter: Chapter 3 --- Neuromodulation: How Chemical Context Shapes Neural Behavior

![Figure 2.10. The same input, a different output. With no neuromodulator present the neuron responds to a train of input spikes with three spikes; with a neuromodulator present it responds with eleven. The wiring has not changed. Chapter 3 explains how chemical context does this. Schematic.](images/fig_context.png)

# References and Attribution

## Figure Attribution

Figures 2.1, 2.2, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, and 2.10 were drawn for this book. The voltage traces in Figures 2.4, 2.5, 2.7, and 2.8 and the spike raster in Figure 2.9 are illustrative simulations, not recorded data.

Figure 2.3: the chemical synapse figure from *Anatomy and Physiology* by OpenStax (Rice University), licensed CC BY 4.0, via openstax.org.

## References

Adrian, E. D. (1928). *The Basis of Sensation: The Action of the Sense Organs*. Christophers.

Adrian, E. D., & Zotterman, Y. (1926). The impulses produced by sensory nerve-endings: Part II. The response of a single end-organ. *Journal of Physiology*, 61(2), 151–171.

Alberts, B., Johnson, A., Lewis, J., Morgan, D., Raff, M., Roberts, K., & Walter, P. (2015). *Molecular Biology of the Cell* (6th ed.). Garland Science.

Attwell, D., & Laughlin, S. B. (2001). An energy budget for signaling in the grey matter of the brain. *Journal of Cerebral Blood Flow & Metabolism*, 21(10), 1133–1145.

Bliss, T. V. P., & Lømo, T. (1973). Long-lasting potentiation of synaptic transmission in the dentate area of the anaesthetized rabbit following stimulation of the perforant path. *Journal of Physiology*, 232(2), 331–356.

Braitenberg, V., & Schüz, A. (1998). *Cortex: Statistics and Geometry of Neuronal Connectivity* (2nd ed.). Springer.

Coombs, J. S., Curtis, D. R., & Eccles, J. C. (1957). The generation of impulses in motoneurones. *Journal of Physiology*, 139(2), 232–249.

Coombs, J. S., Eccles, J. C., & Fatt, P. (1955). The specific ionic conductances and the ionic movements across the motoneuronal membrane that produce the inhibitory post-synaptic potential. *Journal of Physiology*, 130(2), 326–374.

Eccles, J. C. (1964). *The Physiology of Synapses*. Springer.

Faisal, A. A., Selen, L. P. J., & Wolpert, D. M. (2008). Noise in the nervous system. *Nature Reviews Neuroscience*, 9(4), 292–303.

Fatt, P., & Katz, B. (1951). An analysis of the end-plate potential recorded with an intra-cellular electrode. *Journal of Physiology*, 115(3), 320–370.

Fatt, P., & Katz, B. (1952). Spontaneous subthreshold activity at motor nerve endings. *Journal of Physiology*, 117(1), 109–128.

Foster, M., & Sherrington, C. S. (1897). *A Textbook of Physiology, Part III: The Central Nervous System* (7th ed.). Macmillan.

Hebb, D. O. (1949). *The Organization of Behavior: A Neuropsychological Theory*. Wiley.

Hodgkin, A. L. (1964). *The Conduction of the Nervous Impulse*. Liverpool University Press.

Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. *Journal of Physiology*, 117(4), 500–544.

Kandel, E. R., Koester, J. D., Mack, S. H., & Siegelbaum, S. A. (Eds.). (2021). *Principles of Neural Science* (6th ed.). McGraw-Hill.

Katz, B. (1969). *The Release of Neural Transmitter Substances*. Liverpool University Press.

Kole, M. H. P., Ilschner, S. U., Kampa, B. M., Williams, S. R., Ruben, P. C., & Stuart, G. J. (2008). Action potential generation requires a high sodium channel density in the axon initial segment. *Nature Neuroscience*, 11(2), 178–186.

Loewi, O. (1921). Über humorale Übertragbarkeit der Herznervenwirkung. *Pflügers Archiv für die gesamte Physiologie*, 189, 239–242.

London, M., & Häusser, M. (2005). Dendritic computation. *Annual Review of Neuroscience*, 28, 503–532.

Magee, J. C. (2000). Dendritic integration of excitatory synaptic input. *Nature Reviews Neuroscience*, 1(3), 181–190.

Marr, D. (1982). *Vision: A Computational Investigation into the Human Representation and Processing of Visual Information*. W. H. Freeman.

Megías, M., Emri, Z., Freund, T. F., & Gulyás, A. I. (2001). Total number and distribution of inhibitory and excitatory synapses on hippocampal CA1 pyramidal cells. *Neuroscience*, 102(3), 527–540.

Palmer, L. M., & Stuart, G. J. (2006). Site of action potential initiation in layer 5 pyramidal neurons. *Journal of Neuroscience*, 26(6), 1854–1863.

Rall, W. (1959). Branching dendritic trees and motoneuron membrane resistivity. *Experimental Neurology*, 1(5), 491–527.

Ramón y Cajal, S. (1909–1911). *Histologie du système nerveux de l'homme et des vertébrés* (2 vols., trans. L. Azoulay). Paris: Maloine.

Rieke, F., Warland, D., de Ruyter van Steveninck, R., & Bialek, W. (1997). *Spikes: Exploring the Neural Code*. MIT Press.

Shepherd, G. M. (1991). *Foundations of the Neuron Doctrine*. Oxford University Press.

Sterling, P., & Laughlin, S. (2015). *Principles of Neural Design*. MIT Press.

Stuart, G. J., & Sakmann, B. (1994). Active propagation of somatic action potentials into neocortical pyramidal cell dendrites. *Nature*, 367, 69–72.

Waldeyer, W. (1891). Ueber einige neuere Forschungen im Gebiete der Anatomie des Centralnervensystems. *Deutsche medicinische Wochenschrift*, 17, 1213–1218, 1244–1246, 1267–1269, 1287–1289, 1331–1332, 1352–1356.

[^1]: Waldeyer, W. (1891). Ueber einige neuere Forschungen im Gebiete der Anatomie des Centralnervensystems. *Deutsche medicinische Wochenschrift*, 17, 1213–1218, 1244–1246, 1267–1269, 1287–1289, 1331–1332, 1352–1356; Ramón y Cajal, S. (1909–1911). *Histologie du système nerveux de l'homme et des vertébrés* (2 vols., trans. L. Azoulay). Paris: Maloine; Shepherd, G. M. (1991). *Foundations of the Neuron Doctrine*. Oxford University Press. The word "neuron" was introduced by Waldeyer in 1891; the doctrine that the nervous system is built of discrete cells rests chiefly on Cajal's histology.

[^2]: Marr, D. (1982). *Vision: A Computational Investigation into the Human Representation and Processing of Visual Information*. W. H. Freeman.

[^3]: Alberts, B., Johnson, A., Lewis, J., Morgan, D., Raff, M., Roberts, K., & Walter, P. (2015). *Molecular Biology of the Cell* (6th ed.). Garland Science.

[^4]: Attwell, D., & Laughlin, S. B. (2001). An energy budget for signaling in the grey matter of the brain. *Journal of Cerebral Blood Flow & Metabolism*, 21(10), 1133–1145.

[^5]: Kandel, E. R., Koester, J. D., Mack, S. H., & Siegelbaum, S. A. (Eds.). (2021). *Principles of Neural Science* (6th ed.). McGraw-Hill.

[^6]: Megías, M., Emri, Z., Freund, T. F., & Gulyás, A. I. (2001). Total number and distribution of inhibitory and excitatory synapses on hippocampal CA1 pyramidal cells. *Neuroscience*, 102(3), 527–540; Braitenberg, V., & Schüz, A. (1998). *Cortex: Statistics and Geometry of Neuronal Connectivity* (2nd ed.). Springer. A rat hippocampal CA1 pyramidal cell carries roughly 30,000 excitatory and 1,700 inhibitory synapses.

[^7]: Ramón y Cajal, S. (1909–1911). *Histologie du système nerveux de l'homme et des vertébrés* (2 vols., trans. L. Azoulay). Paris: Maloine. Cajal's "law of dynamic polarization."

[^8]: Foster, M., & Sherrington, C. S. (1897). *A Textbook of Physiology, Part III: The Central Nervous System* (7th ed.). Macmillan. The term was coined by Sherrington.

[^9]: Loewi, O. (1921). Über humorale Übertragbarkeit der Herznervenwirkung. *Pflügers Archiv für die gesamte Physiologie*, 189, 239–242; Katz, B. (1969). *The Release of Neural Transmitter Substances*. Liverpool University Press; Fatt, P., & Katz, B. (1952). Spontaneous subthreshold activity at motor nerve endings. *Journal of Physiology*, 117(1), 109–128.

[^10]: Fatt, P., & Katz, B. (1951). An analysis of the end-plate potential recorded with an intra-cellular electrode. *Journal of Physiology*, 115(3), 320–370.

[^11]: Eccles, J. C. (1964). *The Physiology of Synapses*. Springer.

[^12]: Coombs, J. S., Eccles, J. C., & Fatt, P. (1955). The specific ionic conductances and the ionic movements across the motoneuronal membrane that produce the inhibitory post-synaptic potential. *Journal of Physiology*, 130(2), 326–374.

[^13]: Magee, J. C. (2000). Dendritic integration of excitatory synaptic input. *Nature Reviews Neuroscience*, 1(3), 181–190.

[^14]: Rall, W. (1959). Branching dendritic trees and motoneuron membrane resistivity. *Experimental Neurology*, 1(5), 491–527; Stuart, G. J., & Sakmann, B. (1994). Active propagation of somatic action potentials into neocortical pyramidal cell dendrites. *Nature*, 367, 69–72; London, M., & Häusser, M. (2005). Dendritic computation. *Annual Review of Neuroscience*, 28, 503–532. Rall's cable theory describes the passive case; dendrites also contain voltage-gated channels and can regenerate signals locally, a refinement taken up in later chapters.

[^15]: Kole, M. H. P., Ilschner, S. U., Kampa, B. M., Williams, S. R., Ruben, P. C., & Stuart, G. J. (2008). Action potential generation requires a high sodium channel density in the axon initial segment. *Nature Neuroscience*, 11(2), 178–186.

[^16]: Coombs, J. S., Curtis, D. R., & Eccles, J. C. (1957). The generation of impulses in motoneurones. *Journal of Physiology*, 139(2), 232–249; Palmer, L. M., & Stuart, G. J. (2006). Site of action potential initiation in layer 5 pyramidal neurons. *Journal of Neuroscience*, 26(6), 1854–1863.

[^17]: Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. *Journal of Physiology*, 117(4), 500–544; Hodgkin, A. L. (1964). *The Conduction of the Nervous Impulse*. Liverpool University Press.

[^18]: Adrian, E. D., & Zotterman, Y. (1926). The impulses produced by sensory nerve-endings: Part II. The response of a single end-organ. *Journal of Physiology*, 61(2), 151–171; Adrian, E. D. (1928). *The Basis of Sensation: The Action of the Sense Organs*. Christophers.

[^19]: Rieke, F., Warland, D., de Ruyter van Steveninck, R., & Bialek, W. (1997). *Spikes: Exploring the Neural Code*. MIT Press.

[^20]: Hebb, D. O. (1949). *The Organization of Behavior: A Neuropsychological Theory*. Wiley; Bliss, T. V. P., & Lømo, T. (1973). Long-lasting potentiation of synaptic transmission in the dentate area of the anaesthetized rabbit following stimulation of the perforant path. *Journal of Physiology*, 232(2), 331–356.

[^21]: Faisal, A. A., Selen, L. P. J., & Wolpert, D. M. (2008). Noise in the nervous system. *Nature Reviews Neuroscience*, 9(4), 292–303; Attwell, D., & Laughlin, S. B. (2001). An energy budget for signaling in the grey matter of the brain. *Journal of Cerebral Blood Flow & Metabolism*, 21(10), 1133–1145; Sterling, P., & Laughlin, S. (2015). *Principles of Neural Design*. MIT Press.
