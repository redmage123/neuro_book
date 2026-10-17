# Expert review: Chapter 2, Neurons: The Brain's Signaling Cells

File: `docs/book/Word/Chapter2/How_the_Brain_Learns_Chapter_2_Neurons.md`

## Overall assessment

Technical accuracy score: **3 / 5**

The chapter's spine (membrane, ion gradients, graded synaptic potentials, integration, initiation at the axon initial segment, regenerative propagation, rate and timing codes, use-dependent synaptic change) is correct and the historical footnotes are accurate (Waldeyer 1891 for "neuron", Sherrington for "synapse", Kole et al. 2008 for AIS sodium-channel density, Megías et al. 2001 for synapse counts). The simulated figures are labeled as simulations, which is good practice. The serious problem is the chapter's account of what happens outside the axon initial segment: it states that dendritic integration is passive and that the soma does not propagate action potentials. Both statements are wrong as written, the chapter's own footnote 14 half-admits it, and Chapter 5 depends on the opposite being true (back-propagating action potentials opening NMDA receptors). The chapter also overstates the uniformity of action potentials and the size of single EPSPs.

## Major (factually wrong, must fix)

- **Lines 68 to 72**: "This spread is passive. Voltage changes weaken with distance and time. No new electrical signal is regenerated." and **line 72**: "Importantly, the soma does not normally propagate action potentials." and **line 96**: "The soma lacks the channel density required for reliable propagation." These are wrong or badly outdated. (1) The action potential initiated at the AIS invades the soma at full amplitude; the somatic spike is what every whole-cell recording shows, including the chapter's own Figure 2.5 trace style. (2) From the soma the spike back-propagates actively into the dendrites (Stuart and Sakmann 1994, Nature 367:69, which the chapter cites in footnote 14). (3) Dendrites contain voltage-gated Na+, Ca2+ and NMDA conductances and generate local dendritic spikes (Larkum, Zhu and Sakmann 1999, Nature 398:338; London and Häusser 2005, cited). Chapter 5 (lines 44 and 72) relies on "an action potential propagating back from the soma into the dendrite" to expel the magnesium block. The correct statement: the AIS has the lowest threshold and is where the spike is decided (Kole et al. 2008; Palmer and Stuart 2006), the soma has a lower sodium-channel density than the AIS, and dendritic integration is approximately passive for small inputs but active mechanisms (back-propagating spikes, dendritic spikes) are essential to plasticity and are taken up in Chapter 5. Footnote 14's caveat should be promoted into the text.

## Moderate (misleading or outdated, should fix)

- **Line 102**: "Action potentials are uniform in size." All-or-none at initiation, but amplitude and width are not invariant: spikes broaden during trains and with slow inactivation, and subthreshold somatic depolarization modulates axonal spike shape and transmitter release ("analog-digital" signaling: Alle and Geiger 2006, Science 311:1290; Shu et al. 2006, Nature 441:761; Geiger and Jonas 2000, Neuron 28:927). Suggested: "Action potentials are stereotyped; their presence, not their size, is the message, although small variations in shape do modulate release."
- **Line 64, Figure 2.4 caption and figure**: "one EPSP depolarizes the membrane a few millivolts" and "five EPSPs in quick succession sum to threshold". Unitary EPSPs between cortical pyramidal cells are about 0.2 to 2 mV at the soma (Markram et al. 1997, J. Physiol. 500:409, mean about 1.3 mV; Song et al. 2005, PLoS Biol. 3:e68, median about 0.5 mV), and reaching threshold from rest takes tens to hundreds of near-coincident inputs. The simulation (about 4 mV per EPSP, five to threshold) is pedagogically fine but the caption should say "exaggerated for clarity" and the text "a fraction of a millivolt to a few millivolts". Note the chapter's own Figure 2.8 uses 1.5 mV, which is more realistic.
- **Line 108**: "Learning is physical reconfiguration, not information storage." (Repeated as "Nothing is stored" in Chapter 5, line 178.) Physical reconfiguration of synaptic weights is information storage in a physical substrate; the contrast the author wants is with addressable, read-without-modification storage, which Chapter 5 states correctly at line 14. As written the sentence is a false dichotomy that a technical reader will reject.
- **Lines 44 to 48**: The account of inputs ("the immediate input to a neuron is not an electrical spike, but a small, local chemical event") omits electrical synapses (gap junctions). These are not a footnote in mammalian cortex: they couple interneuron networks and are essential to the gamma oscillations of Chapter 4 (Hormuzdi et al. 2001, Neuron 31:487; Connors and Long 2004, Annu. Rev. Neurosci. 27:393). One sentence would fix it.

## Minor (imprecise wording)

- **Line 40, Figure 2.2 caption**: "a single axon, decided at the initial segment and insulated by myelin". Most local cortical axons are unmyelinated; the "typical" neuron drawn here is a projection neuron. Add "(in long-range axons)".
- **Line 110, Figure 2.8 caption and figure labels**: "5 vesicles (low release probability)" and "11 vesicles (high release probability)". Vesicle count and release probability are different quantities (release probability depends on calcium-channel coupling and priming, not on how many vesicles are drawn). Either label the before/after as "fewer/more docked vesicles" or as "lower/higher release probability", not both as one.
- **Line 116, Figure 2.9 caption**: "ten million times longer than a transistor switch". With a 1 ms spike and a 100 ps switch this is 10^7, consistent with panel A. Fine, but state the assumed switch time somewhere; modern transistors switch in roughly 10 to 100 ps.
- **Line 124**: "Chapter 3 --- Neuromodulation: How Chemical Context Shapes Neural Behavior". Chapter 3's actual subtitle is "How Chemical Context Shapes Learning and Behavior". Align.
- **Line 24**: "What distinguishes neurons from most other cells is excitability." Muscle fibers, cardiac cells and some endocrine cells are also excitable; "most" covers it, but "and the ability to transmit over distance and to change those influences" is the actual distinguishing combination, which the sentence then lists. Fine as is; flagged only because the opening clause is stronger than the list.
- **Line 58**: "synapses that allow positive ions, such as sodium, to enter the cell". AMPA channels are non-selective cation channels (Na+ in, K+ out); the net inward current is what depolarizes. Accurate enough for the audience.
- **Line 90**: "Nothing travels the length of the axon except causation." Rhetorical; acceptable, but a technical reader may object that charge (ionic current) does travel locally ahead of the spike, which the figure correctly shows.
- **Line 132 (attribution)**: The chapter correctly labels all drawn traces as simulations. Good.

## Citation support check

- Footnote 6 (Megías et al. 2001): the numbers quoted (about 30,000 excitatory, 1,700 inhibitory on a rat CA1 pyramidal cell) match the paper.
- Footnote 14: Stuart and Sakmann 1994 and London and Häusser 2005 are cited for "Voltage changes weaken with distance and time", but both papers are about active dendritic propagation, that is, the opposite of the sentence they support. The footnote text acknowledges this; the main text does not.
- Footnote 16 (Coombs, Curtis and Eccles 1957; Palmer and Stuart 2006) supports initiation at the AIS.
- Footnote 18 (Adrian and Zotterman 1926; Adrian 1928) supports rate coding and all-or-none spikes in sensory nerves; it does not address the shape modulation noted above.
- All other footnotes support their sentences.

## Figures

- Figure 2.1: correct (3 Na+ out, 2 K+ in, 5 nm bilayer, about −70 mV).
- Figure 2.3 (OpenStax): correct and correctly attributed.
- Figure 2.4: simulated, labeled as such; EPSP amplitude exaggerated (see Moderate).
- Figure 2.5: correct; "schematic density" is stated on the figure. Good.
- Figure 2.6: correct description of continuous and saltatory conduction.
- Figure 2.7: simulated, labeled; fine.
- Figure 2.9: panel C's "2 percent of body mass, 20 percent of resting energy" is the standard figure (Attwell and Laughlin 2001; Raichle and Gusnard 2002, PNAS 99:10237).
- Figure 2.10: labeled "Schematic"; fine.
