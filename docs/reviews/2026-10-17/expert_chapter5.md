# Expert review: Chapter 5, Plasticity and Memory: How Experience Becomes Structure

File: `docs/book/Word/Chapter5/How_the_Brain_Learns_Chapter_5_Plasticity_and_Memory.md`

## Overall assessment

Technical accuracy score: **4 / 5**

The molecular and cellular core of this chapter is accurate and well sourced: NMDA receptor magnesium block (Nowak 1984; Mayer 1984), calcium-dependent direction of change (Lisman 1989), early versus late LTP and protein synthesis (Frey 1988), STDP (Markram 1997; Bi and Poo 1998), BCM sliding threshold, synaptic scaling (Turrigiano 1998), synaptic tagging and capture (Frey and Morris 1997), engram manipulations (Liu 2012; Ramirez 2013), replay and ripples (Wilson and McNaughton 1994; Girardeau 2009), reconsolidation (Nader 2000), and H.M. The simulated traces are labeled. The problems are at the edges: one date error, one historically wrong attribution in the AI section, and four places where contested findings (adult human neurogenesis, the standard model of systems consolidation, the reconsolidation-update clinical paradigm, the synaptic homeostasis hypothesis) are presented as settled.

## Major (factually wrong, must fix)

- **Line 54**: "LTD was established in the cerebellum in 1982 and in the hippocampus a decade after LTP." LTP was reported in 1973; the hippocampal homosynaptic LTD the footnote cites (Dudek and Bear 1992; Mulkey and Malenka 1992) is two decades later, and the footnote itself says 1992. (Heterosynaptic and associative LTD in hippocampus were reported earlier: Lynch, Dunwiddie and Gribkoff 1977, Nature 266:737; Levy and Steward 1979, Brain Res. 175:233.) Fix to "two decades after LTP" or "a decade after the cerebellar form".
- **Line 166 (AI section)**: "Experience replay in reinforcement learning is a direct borrowing." The cited Lin 1992 introduced experience replay two years before hippocampal replay was first reported (Wilson and McNaughton 1994), so it was not borrowed from neuroscience. Mnih et al. 2015 (cited) note the analogy after the fact. Correct wording: "Experience replay in reinforcement learning (Lin 1992) was invented independently and later recognized as the analog of hippocampal replay."

## Moderate (misleading or outdated, should fix)

- **Line 28 and line 144**: "in a few regions, chiefly the dentate gyrus of the hippocampus, new neurons are born throughout life" and "The dentate gyrus grows new neurons throughout life". Established in rodents; contested in adult humans. Sorrells et al. 2018 (Nature 555:377) found neurogenesis undetectable in adult human dentate gyrus; Boldrini et al. 2018 (Cell Stem Cell 22:589) and Moreno-Jiménez et al. 2019 (Nat. Med. 25:554) found it persists; single-nucleus studies (Franjic et al. 2022, Neuron; Zhou et al. 2022, Nature) give mixed results, and the debate turns on tissue fixation and marker specificity. The neurogenesis-driven forgetting result (Akers et al. 2014, cited) is in mice. Add "in rodents, and probably at a low rate in adult humans, though this is disputed".
- **Line 114**: "Patients with hippocampal damage ... retain old ones, with the boundary falling years before the injury. The hippocampus, on this account, holds a rapidly formed index ... Over time ... the index is no longer needed." This is the standard consolidation model presented without its main rival. Multiple trace / trace transformation theory holds that detailed episodic memories remain hippocampus-dependent indefinitely, and that only schematic (semanticized) versions become hippocampus-independent (Nadel and Moscovitch 1997, Curr. Opin. Neurobiol. 7:217; Winocur and Moscovitch 2011, J. Int. Neuropsychol. Soc. 17:766). H.M.'s retrograde amnesia extended about 11 years and his remote autobiographical memories were semantic rather than episodic (Corkin 2002, cited; Steinvorth, Levine and Corkin 2005). The phrase "on this account" acknowledges a model; name the alternative in one sentence.
- **Line 60**: "Neither effect requires anything from outside the synapse and its immediate neighborhood." True of induction and early-phase expression; late-phase maintenance in slices can require dopamine (Frey, Schroeder and Matthies 1990, cited at footnote 21) and the chapter's own line 92 says so. Also, Chapter 3 (lines 155 to 157) claims neuromodulation gates plasticity absolutely, which this sentence contradicts. Qualify: "Neither effect, in its early phase, requires ...".
- **Line 132**: "a fear memory reactivated and then given corrective information in the reconsolidation window is weakened more durably than one treated outside it, which is the basis of several clinical approaches to trauma.[^41]" The Monfils 2009 rat result holds up reasonably; the human version (Schiller et al. 2010, cited) has multiple failed replications (Kindt and Soeter 2011, 2013; Golkar et al. 2012; Klucken et al. 2016), a high-powered registered replication found no effect (Chalkia et al. 2020, Cortex 129:496), and a reanalysis reported inconsistencies in the original exclusions (Chalkia, Schroyens et al. 2020, Cortex). Propranolol-based approaches (Brunet et al. 2008) show modest effects. State that the human evidence is mixed.
- **Lines 44 and 72** depend on action potentials "propagating back from the soma into the dendrite". Correct here, but Chapter 2 (lines 68 to 72, 94 to 96) says dendritic integration is passive and the soma does not propagate spikes. The fix belongs in Chapter 2; flagging here for cross-chapter consistency.
- **Line 120**: "The replay is real, and it happens mainly during sleep." Replay during quiet wakefulness (awake sharp-wave ripples) is at least as prominent and is causally important for learning (Jadhav et al. 2012, Science 336:1454; Foster and Wilson 2006). "during slow-wave sleep and quiet rest" is accurate.

## Minor (imprecise wording)

- **Line 42**: "a single protein, the NMDA receptor". It is a tetrameric receptor assembled from GluN1 and GluN2/3 subunits, and NMDA-receptor-independent LTP exists (mossy fiber LTP; voltage-gated calcium-channel-dependent LTP). "a single receptor type" and "for most forms of LTP" would be correct.
- **Line 96**: "a few percent of the cells in a region take part in encoding any particular event". About 2 to 6 percent in dentate gyrus, but 10 to 20 percent in lateral amygdala and 20 to 40 percent in CA1 (Josselyn and Tonegawa 2020, cited). "a few to a few tens of percent, depending on the region".
- **Line 126**: The synaptic homeostasis hypothesis is hedged with "appears", which is right; note that it is contested (sleep also potentiates and forms spines, especially REM: Li et al. 2017, Nat. Neurosci. 20:427; Frank and Cantera 2014, Trends Neurosci. 37:491).
- **Line 138**: "the curve is roughly the same whether the material is nonsense or meaningful. What changes with meaning is the starting point, not the shape." Neither cited source (Ebbinghaus; Murre and Dros 2015) tests this; Ebbinghaus found meaningful material (Don Juan stanzas) far faster to learn. The shape claim is broadly consistent with the power-law forgetting literature (Wixted and Ebbesen 1991, Psychol. Sci. 2:409) and should cite it.
- **Line 152**: "Working memory ... is not synaptic change at all but persistent activity ... and by short-term facilitation of synapses". Self-contradictory as written (short-term facilitation is a synaptic change). "no lasting synaptic change" fixes it. Also note the "activity-silent" working memory debate (Stokes 2015; Mongillo 2008, cited).
- **Line 154**: "after his hippocampi were removed". H.M. underwent bilateral medial temporal lobe resection that removed the amygdala, entorhinal cortex and roughly the anterior two-thirds of the hippocampus; posterior hippocampus was spared (Corkin et al. 1997, J. Neurosci. 17:3964). "after most of both hippocampi and the surrounding medial temporal cortex were removed".
- **Line 112, Figure 5.7A** says systems consolidation takes "days to years"; text at line 114 says "weeks to years". Align.
- **Line 168**: "the brain is an existence proof that they [local three-factor rules] can learn language, motor skill, and science." Circular: whether the brain learns with only local rules is the open question stated in the previous sentence. "the brain is an existence proof that some biologically available rule can" is accurate.
- **Line 172**: "Artificial systems mostly have no equivalent to deliberate, selective forgetting." Machine unlearning, pruning, and continual-learning regularizers exist; "few deployed systems forget deliberately" is safer.
- **Line 84**: "slow, on the order of a day"; Turrigiano et al. 1998 used 48 hours of activity blockade. "a day or two".
- **Line 100**: "In the last fifteen years it has become an experimental object." Reijmers 2007 and Han 2007/2009 (cited) make it closer to twenty. Minor.

## Citation support check

- Footnote 10: correctly dates cerebellar LTD to 1982 and hippocampal LTD to 1992; the text at line 54 contradicts the footnote.
- Footnote 12: "900 pulses at 1 Hz" is the standard protocol (Dudek and Bear 1992); correct.
- Footnote 23 (Han 2007; Reijmers 2007) supports sparse allocation.
- Footnote 25: the five engram papers support the three manipulations described.
- Footnote 41: supports the claim as stated but not its reliability (see Moderate).
- Footnote 54: Lin 1992 contradicts "direct borrowing" (see Major).
- Footnote 56: Ioffe and Szegedy 2015 and Krogh and Hertz 1992 support "normalization layers and weight decay"; fine.
- All other footnotes support their sentences.

## Figures

- Figure 5.1: correct.
- Figure 5.2: panel B simulated and labeled; magnitudes (about 150 to 160 percent LTP, about 65 percent LTD) are typical.
- Figure 5.3: simulated, labeled; window shape and asymmetry are standard.
- Figure 5.4: correct depiction of BCM and multiplicative scaling.
- Figure 5.5: fine.
- Figure 5.6 (Blausen limbic system): correctly described.
- Figure 5.7: timescale mismatch with text (see Minor).
- Figure 5.8: correctly described.
- Figure 5.9: simulated, labeled.
- Figure 5.10: fine; note the "Emotional" column lists ventral striatum, which the text does not mention.
