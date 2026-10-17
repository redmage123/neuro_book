# Expert review summary: "How the Brain Learns", Chapters 0 to 6

Reviewer role: systems and cellular neuroscience, synaptic plasticity, computational neuroscience. Read-only review of the seven chapter sources and all figures. Per-chapter reports are in `expert_chapter0.md` to `expert_chapter6.md` beside this file.

## Book-level assessment

The manuscript is substantially correct and unusually well referenced for popular science: the foundational numbers (86 billion neurons, 37 trillion cells, 69 billion cerebellar neurons, about 200,000 parallel fibers per Purkinje cell, about 20 nm cleft, 2 percent of mass and 20 percent of resting energy, 130 Hz / 60 microsecond DBS, 900 pulses at 1 Hz for LTD, about 10 percent retinal input to LGN) are right, the attributions of discoveries are right (Waldeyer, Sherrington, Hodgkin and Huxley, Brown, Hartline, Bliss and Lømo, Ito, Semon, Nader), and every drawn figure with simulated data is labeled as such in its attribution block. The citations are real and, with about fifteen exceptions listed in the chapter reports, support the sentences they are attached to.

Average score: 3.7 / 5. The chapters that explain mechanism carefully (4, 5, 6) are stronger than the chapters that make sweeping claims (2, 3).

### Recurring problems

1. **Contested claims stated as settled.** The book's rhetorical style ("The brain cannot do this." "Dopamine encodes prediction error." "Two regions out of phase cannot communicate.") turns live hypotheses into facts. The clearest cases: biologically plausible credit assignment (Ch3), dopamine heterogeneity (Ch3), neuromodulatory gating of all plasticity (Ch3), communication through coherence (Ch4), cerebellar LTD as the learning rule (Ch4), adult human neurogenesis (Ch5), the standard model of systems consolidation (Ch5), the reconsolidation-update therapy paradigm (Ch5), feedback outnumbering feedforward (Ch6), innateness of the light-from-above prior (Ch6). Chapter 6 shows how to do it right (predictive-coding laminar mapping "is not settled"; psychiatric accounts "are hypotheses").
2. **Figure captions that describe a different figure.** Four public-domain images were captioned for what the author wanted rather than what they show: Fig 0.2 (metabolism diagram captioned as entropy), Fig 0.7 (generic schematic captioned as Hodgkin and Huxley's work), Fig 0.9 (neurulation captioned as axon guidance and activity-dependent refinement), Fig 4.5 (Cajal's Nissl/Nissl/Golgi panels mislabeled). Fig 4.1A also contradicts the text's knee-jerk example (flexor/extensor swapped).
3. **Cited studies misdescribed.** Neitz et al. 2002 (Ch6: colored filters over days, not a month in a colored room); Matsuda et al. 2009 (Ch3: 2.7 percent mean, not 6 percent); Curcio et al. 1990 (Ch6: 4.6 million cones, not six); Brzosko et al. 2015 (Ch3: minute-scale window, not seconds); Lin 1992 (Ch5: experience replay predates hippocampal replay, so it was not "borrowed"); Lillicrap et al. 2020 (Ch3: cited for a claim it argues against).
4. **False dichotomies in the rhetoric.** "Learning is physical reconfiguration, not information storage" (Ch2), "Nothing is stored" (Ch5), "Biological systems do not optimize a loss function" (Ch3). Technical readers will reject these as stated, and the book elsewhere (Ch5 line 14, Ch6 line 152) makes the defensible versions.
5. **AI analogies that are technically off.** "A unit's output can be positive or negative" (Ch4; it is the weights), "every forward pass is a learning opportunity" (Ch3; not at inference), "adversarial examples are evidence without priors" (Ch6), "experience replay is a direct borrowing" (Ch5), "backpropagation is optimal" (Ch3).

### Cross-chapter inconsistencies

| Topic | Says one thing | Says another |
|---|---|---|
| Dendrites and soma | Ch2 L68-72, 94-96: integration passive, soma does not propagate spikes | Ch5 L44, 72: back-propagating action potentials expel the NMDA magnesium block |
| Neuromodulatory gating | Ch3 L155-157: plasticity occurs only when neuromodulators permit | Ch5 L60: LTP/LTD require nothing from outside the synapse |
| Credit assignment | Ch3 L97-105: the brain cannot; ill-posed | Ch5 L168, Ch6 L152: open question |
| Loss functions | Ch3 L137, 183: brain does not optimize a loss | Ch6 L152: cortex is a generative model trained by prediction error; Ch3 Fig 3.6 is TD error minimization |
| Why learning is slow | Ch1 L46: because molecular change is slow | Ch5 L158-160: because of the stability-plasticity dilemma; hippocampus learns fast |
| Systems consolidation timescale | Ch5 text L114: weeks to years | Ch5 Fig 5.7A: days to years |
| Hippocampal LTD date | Ch5 L54: a decade after LTP (1983) | Ch5 footnote 10: 1992 |
| Chapter 3 subtitle | Ch2 L124: "Shapes Neural Behavior" | Ch3 title: "Shapes Learning and Behavior" |
| "The controller generates, the world corrects" | Ch4 L80, Ch6 L112 attribute it to Chapter 1 | Chapter 1 does not say it |
| Cone count | Ch6 L24: six million | Cited Curcio 1990: about 4.6 million |

### The most important corrections (in priority order)

1. **Ch2 L68-72, 94-96**: Dendrites are not purely passive and the soma does propagate (and back-propagates) spikes. This is the one place the book is wrong about basic cell physiology, and Chapter 5 depends on the correct version.
2. **Ch4 L106**: Basal ganglia damage produces hyperkinetic disorders (chorea, hemiballismus) as well as hypokinetic ones; the "fails safe" claim is false and the cited Albin/DeLong model says so.
3. **Ch4 Fig 4.5 caption**: the panels are Nissl, Nissl, Golgi; the caption describes stains that are not there.
4. **Ch3 Fig 3.4**: human nucleus basalis has about 200,000 cholinergic neurons per hemisphere, not "a few thousand".
5. **Ch6 L132**: Neitz et al. 2002 used colored filters over days and measured unique yellow; there was no month in a monochromatic room.
6. **Ch3 L97-105 and L77**: soften "the brain cannot" (credit assignment) and "dopamine encodes prediction error" to the actual state of evidence; cite Lillicrap 2020 for what it says.
7. **Ch0 Figs 0.7, 0.9, 0.2**: recaption or replace the three mismatched images.
8. **Ch5 L54 and L166**: "two decades after LTP"; experience replay was not borrowed from neuroscience.
9. **Ch5 L28, L114, L132**: hedge adult human neurogenesis, the standard consolidation model, and the reconsolidation-update paradigm (registered replication failed).
10. **Ch3 L161 and Figs 3.9-3.10**: DBS is not evidence about neuromodulator tone; either reframe or move.
11. **Ch0 L272**: remove the ATP "bond energy" misconception.
12. **Ch4 L162, Ch3 L177, Ch6 L148**: fix the three technically incorrect AI analogies.

### Per-chapter scores and finding counts

| Chapter | Score (1-5) | Major | Moderate | Minor |
|---|---|---|---|---|
| 0 Foundations | 4 | 2 | 5 | 10 |
| 1 What the Brain Is | 4 | 0 | 2 | 6 |
| 2 Neurons | 3 | 1 | 4 | 9 |
| 3 Neuromodulation | 3 | 2 | 7 | 8 |
| 4 Circuits | 4 | 2 | 5 | 11 |
| 5 Plasticity and Memory | 4 | 2 | 6 | 11 |
| 6 Perception as Inference | 4 | 1 | 6 | 11 |
| **Total** | **3.7 avg** | **10** | **35** | **66** |

Major = factually wrong, must fix. Moderate = misleading, outdated, or a contested claim presented as settled. Minor = imprecise wording, citation fit, or figure-text alignment. Each finding in the chapter reports gives the line number, the quoted text, the problem, the correction, and a source.

### Figures and simulated data

All figures referenced exist. Every drawn figure containing simulated traces (Chs 2, 3, 4, 5, 6) is identified as a simulation in the chapter's attribution block, and most captions repeat it. Quantitatively checked figures (Fig 2.9A ratio, Fig 6.2 posterior means, Fig 6.8 combined sigmas and weights, Fig 3.10 DBS parameters, Fig 4.10 band limits) are internally consistent. Caption errors are listed under recurring problem 2. One modeling caveat: Fig 4.2's "no inhibition" panel runs away before the input arrives, which the caption does not describe.

### Sources consulted for corrections

- Nucleus basalis counts: https://pmc.ncbi.nlm.nih.gov/articles/PMC4184885
- Cajal cortex drawing panels: https://embryology.med.unsw.edu.au/embryology/index.php/File:Neural-_cortex_Cajal_drawing_01.jpg
- Matsuda et al. 2009 arbor figures: https://www.jneurosci.org (29(2):444) via https://www.mrcbndu.ox.ac.uk/papers/single-nigrostriatal-dopaminergic-neurons-form-widely-spread-and-highly-dense-axonal
- Neitz et al. 2002 abstract: PubMed 12194876 (E-utilities fetch)
- Adult human neurogenesis debate: https://www.explorationpub.com/Journals/en/Article/1006128
- Feedback versus feedforward (Markov 2014): https://ekmillerlab.mit.edu/2013/08/29/the-anatomy-of-hierarchy
- Schiller 2010 replication record: https://pmc.ncbi.nlm.nih.gov/articles/PMC7115861
- Adams, Graf and Ernst 2004: Nature Neuroscience 7(10):1057-1058
- Brzosko et al. 2015 timing: https://elifesciences.org/articles/09685
- Dopamine RPE alternatives: https://thetransmitter.org/dopamine/does-a-new-theory-of-dopamine-replace-the-classic-model
