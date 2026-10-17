# Expert review: Chapter 6, Perception as Inference: How the Brain Sees What It Expects

File: `docs/book/Word/Chapter6/How_the_Brain_Learns_Chapter_6_Perception_as_Inference.md`

## Overall assessment

Technical accuracy score: **4 / 5**

The chapter is accurate on the inverse problem, Bayesian cue combination (Ernst and Banks 2002, correctly described; Figure 6.8's numbers are internally consistent), the ventral hierarchy and its timing (Thorpe 1996; Hung 2005), the LGN input fraction (Sherman and Guillery), predictive coding and its laminar/frequency mapping (hedged correctly as "not settled"), the illusions, efference copy (von Holst and Sperry 1950), critical periods, sparse coding (Olshausen and Field 1996), and the clinical hypotheses (hedged correctly as hypotheses). The problems are one cited study described inaccurately (Neitz 2002), two numbers that do not match the cited sources (cone count; feedback versus feedforward), a conflation of repetition suppression with prediction error, overstated claims about innate priors and inverting-goggle adaptation, and an AI analogy about adversarial examples that does not hold.

## Major (factually wrong, must fix)

- **Line 132**: "Spend a month in a room lit by a single color and color constancy recalibrates.[^48]" The cited study (Neitz, Carroll, Yamauchi, Neitz and Williams 2002, Neuron 35:783) did not do this. Its abstract: "Chromatic experience was altered using colored filters. Over days there was a shift in color perception, as measured by the wavelength of unique yellow, which persisted 1-2 weeks after the filters were discontinued." Subjects wore colored filters for part of each day over days, the measured variable was the red-green balance point (unique yellow), not color constancy, and there was no monochromatic room or month. Rewrite: "View the world through a colored filter for a few hours a day for several days and the point you call pure yellow shifts, and stays shifted for a week or two after the filter is removed." Source: PubMed 12194876.

## Moderate (misleading or outdated, should fix)

- **Line 24 and footnote 2**: "roughly a hundred million rods and six million cones". The cited Curcio et al. 1990 reports about 92 million rods and about 4.6 million cones (range 4.08 to 5.29 million). Six to seven million is Østerberg's 1935 figure. Change to "four to five million cones", or cite Østerberg.
- **Line 56 and Figure 6.4 caption (line 50)**: "Feedback connections ... outnumber the feedforward ones" / "feedback connections, which outnumber them". Well supported for the thalamus (retinal input is about 5 to 10 percent of synapses on LGN relay cells, Sherman and Guillery, cited), and Markov et al. 2014 (J. Comp. Neurol. 522:225) found feedback pathways more numerous than feedforward pathways in macaque cortex, but counts of pathways are not counts of axons or synapses, and the cited Felleman and Van Essen 1991 lists pathways as largely reciprocal without counting either direction. Hedge: "feedback pathways are at least as numerous as feedforward ones, and at the thalamus they dominate", and cite Markov et al. 2014.
- **Line 68**: "A stimulus repeated several times evokes a smaller response each time ... this is called repetition suppression, and it is the single most reproducible phenomenon in sensory cortex (Figure 6.5B)." Repetition suppression is presented as one of three predictions of predictive coding, but it is equally explained by neuronal fatigue or sharpening; the cited review (Grill-Spector, Henson and Martin 2006) lays out three competing models and does not endorse prediction error. The evidence that distinguishes prediction from adaptation is expectation suppression, where an expected stimulus evokes less activity than an unexpected one at equal repetition (Summerfield et al. 2008, Nat. Neurosci. 11:1004; Todorovic and de Lange 2012, J. Neurosci. 32:13389). Cite those and drop "single most reproducible phenomenon", which is unsupported.
- **Line 148 (AI section)**: "Adversarial examples ... are what a system looks like when it has evidence but no priors with which to check it." A trained classifier embodies strong learned priors (that is what its weights are). The cited Goodfellow et al. 2015 attributes adversarial vulnerability to the near-linearity of networks in high dimensions; later work attributes it to reliance on non-robust but predictive features (Ilyas et al. 2019, NeurIPS). Humans can also be fooled by adversarial images under brief presentation (Elsayed et al. 2018, NeurIPS). The honest version: feedforward classifiers have no mechanism for checking a hypothesis against the input (no generative loop), which is the point the next sentence makes.
- **Line 42 and line 124**: "No one is taught this. It is in the weights." and "the light-from-above assumption is present in several species that have never been taught it". The prior is modifiable by about an hour of visual-haptic training in adults (Adams, Graf and Ernst 2004, Nat. Neurosci. 7:1057, "Experience can change the 'light-from-above' prior"), and in humans it is actually "light from above-left" (Sun and Perona 1998, Nat. Neurosci. 1:183; Mamassian and Goutcher 2001). Footnote 40 cites one species (chickens, Hershberger 1970), not several. Rewrite: "It is present without instruction in chicks and in human infants, and it can be retuned by experience in adults."
- **Line 132**: "Wear goggles that invert the world and within days it begins to look upright again." Stratton (1897) reported adaptive behavior and intermittent impressions of uprightness; a controlled replication found motor adaptation but no perceptual re-inversion after 6 to 10 days (Linden et al. 1999, Perception 28:469). "within days you can act in it fluently, and whether it comes to look upright is disputed" is accurate.

## Minor (imprecise wording)

- **Line 24**: "less than a single compressed video stream". Koch et al. 2006 (cited) extrapolate about 10 Mbit/s for the human optic nerve; a 1080p streaming video is 5 to 8 Mbit/s. "comparable to" rather than "less than".
- **Line 54**: "Convolutional neural networks were modeled on this sweep." Correct but uncited; add Fukushima 1980 (Biol. Cybern. 36:193) or LeCun et al. 1989.
- **Line 68**: MMN "is present in sleeping adults". It is attenuated or absent in some sleep stages (Sallinen, Kaartinen and Lyytinen 1994; Nashida et al. 2000); "detectable even in sleeping adults and newborns" with "attenuated" is accurate.
- **Line 50, Figure 6.4 caption**: "There is no feedback to the retina." Mammals have sparse centrifugal (retinopetal) fibers, mostly histaminergic and serotonergic from the hypothalamus and raphe (Gastinger et al. 2006, Ophthalmic Res. 38:241); birds have a substantial isthmo-optic projection. "essentially no" for mammals.
- **Line 18**: "the idea has been made precise, mapped onto cortical anatomy, and measured with electrodes". "mapped" overstates; line 70 correctly says "the mapping is not settled". Use "provisionally mapped".
- **Line 146**: "the fact that gradient descent and evolution arrived at the same place is evidence that the place is not arbitrary". The resemblance is partial: CNNs are texture-biased where humans are shape-biased (Geirhos et al. 2019, ICLR) and diverge from IT on adversarial and out-of-distribution images. A clause acknowledging the divergence would make the claim robust.
- **Line 152**: "an open research question with a biological existence proof on one side". The brain is an existence proof that some learning rule works, not that predictive coding does. Same circularity as Chapter 5 line 168.
- **Line 26**: "about two degrees of the visual field" for the fovea; the rod-free foveola is about 1.2 degrees and the fovea about 5 degrees. "one to two degrees of highest acuity" is fine.
- **Line 28**: "the image sweeps across the retina at hundreds of degrees per second". Peak saccade velocities are 300 to 700 degrees per second; correct.
- **Line 96**: Acetylcholine and norepinephrine as expected and unexpected uncertainty is a model (Yu and Dayan 2005); the text hedges with "one influential account", which is right.
- **Line 108**: "heard as a third syllable, a compromise". The classic McGurk fusion (auditory /ba/ plus visual /ga/ heard as /da/) is a fusion, and other pairings give combinations rather than compromises; fine for the audience.

## Citation support check

- Footnote 2: cone count misquoted (see Moderate).
- Footnote 3 (Koch et al. 2006): supports about 10 Mbit/s.
- Footnote 13: Sherman and Guillery supports the LGN fraction; Felleman and Van Essen does not support "outnumber" (see Moderate).
- Footnote 15 (Grill-Spector et al. 2006): does not support repetition suppression as prediction error (see Moderate).
- Footnote 31 (Ernst and Banks 2002): the description at line 104 is accurate.
- Footnote 40: one species cited for "several species" (see Moderate).
- Footnote 47: Stratton and Kohler cited for "begins to look upright" (see Moderate).
- Footnote 48 (Neitz et al. 2002): does not support the sentence (see Major).
- Footnote 54 (Szegedy 2014; Goodfellow 2015): does not support "no priors" (see Moderate).
- All other footnotes support their sentences.

## Figures

- Figure 6.2: internally consistent (posterior means at 16 and 6 degrees follow from the drawn widths).
- Figure 6.3: correct, and the effect is visible in the image.
- Figure 6.4: "more numerous axons" for feedback is overstated (see Moderate); receptive-field progression and labels are correct.
- Figure 6.5: panel B simulated and labeled; panel A correctly described as "proposed mapping".
- Figure 6.6 (Adelson): correct and attributed.
- Figure 6.7: correct.
- Figure 6.8: correct (sigma_combined = 1.8 and 3.6 mm, weights 0.8 and 0.2, follow from the stated sigmas).
- Figure 6.9: correct.
- Figure 6.10: labeled schematic; fine.
- Attribution block (line 168) correctly lists which curves are computed rather than recorded.
