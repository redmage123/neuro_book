---
title: "Chapter 6"
subtitle: "Perception as Inference: How the Brain Sees What It Expects"
---

> *"Such objects are always imagined as being present in the field of vision as would have to be there in order to produce the same impression on the nervous mechanism, the eyes being used under ordinary normal conditions."*
>
> --- Hermann von Helmholtz, *Treatise on Physiological Optics* (1867)

# The Problem Perception Solves

Chapter 1 said, almost in passing, that perception is an active process of inference shaped by prior experience. Every chapter since has built the machinery that makes the sentence true: neurons that integrate evidence, circuits that amplify and compare, neuromodulators that set the context, and synapses that turn experience into structure. This chapter uses that machinery to answer a question that sounds too simple to need one. When you open your eyes, why do you see a world rather than a pattern of light?

The light that reaches the retina is not a world. It is a two-dimensional projection, blurred by the optics of the eye, sampled by a mosaic of receptors, and interrupted three times a second by eye movements. Worse, the projection is ambiguous in a way that no amount of resolution can fix. A trapezoid on the retina can be a trapezoid face-on, a rectangle receding from the viewer, or a painted shape on a billboard; the retina cannot distinguish them, because they all produce the same image (Figure 6.1). A patch of gray can be a dark surface in bright light or a bright surface in shadow. A sound that grows louder can be a source approaching or a source turning toward you. Mathematically this is an inverse problem, and inverse problems of this kind are ill-posed: the evidence does not determine the answer.

![Figure 6.1. The inverse problem. Many arrangements of surfaces in the world produce the same image on the retina. The evidence alone cannot say which one is present.](images/fig_inverse.png)

Helmholtz saw this clearly in the 1860s and drew the only possible conclusion. If the evidence does not determine the answer and yet we perceive an answer, something must be supplying the rest. He called it unconscious inference: the perceptual system settles on the state of the world that, under ordinary conditions, would most probably have produced the sensations it is receiving.[^1] The judgment is not made by reasoning and cannot be overruled by it, which is why an illusion persists after you know it is an illusion. A century and a half later the idea has been made precise, provisionally mapped onto cortical anatomy, and measured with electrodes, and this chapter is an account of that work. The thesis can be stated in one sentence. Perception is not the reading of a signal but the construction of a hypothesis, built from what the senses report and from what the brain already expects, and weighted by how much each can be trusted.

# The Senses Deliver Evidence, Not Pictures

Begin with what the senses actually provide, because it is less than intuition suggests.

The human retina has about 92 million rods and about 4.6 million cones, but only about a million ganglion cell axons leave each eye.[^2] The retina therefore compresses by roughly a hundred to one before any signal reaches the brain, and Chapter 4 described what the compression keeps: contrast rather than brightness, change rather than steady state, edges rather than surfaces. Estimates of the information rate of the optic nerve are on the order of ten megabits per second, comparable to a single compressed video stream.[^3]

That capacity is not spread evenly. Fine resolution is confined to the fovea, a patch of densely packed cones whose region of highest acuity covers only one to two degrees of the visual field, roughly the width of a thumbnail held at arm's length. Outside the fovea acuity collapses, and at fifteen degrees to one side there is a region with no receptors at all, where the optic nerve exits. This blind spot is about six degrees across, a dozen times the width of the full moon, and you have never seen it, because the brain fills it with whatever surrounds it.[^4]

Nor does the eye hold still. It jumps about three times a second in rapid movements called saccades, resting for a few hundred milliseconds between jumps. During each jump the image sweeps across the retina at hundreds of degrees per second and vision is suppressed.[^5] What arrives in the brain is not a stable, wide, high-resolution picture. It is a sequence of small, sharp, overlapping samples, each a fraction of a second long, separated by gaps, with a hole in each one. The stable scene you experience is not among the inputs. It is an output.

The same holds for the other senses. The cochlea delivers a running spectrum, not words. Touch delivers the deformation of skin, not the shape of the object. In every case the sense organ reports local physical quantities, and the rest is inference.

# Bayes in One Paragraph

The mathematics of inference under uncertainty was worked out in the eighteenth century and is short enough to state in full. Suppose the brain must estimate some quantity, say the direction of a sound. Before the sound arrives there is a prior: a distribution over directions that encodes what is usually true, built from a lifetime of sounds. When the sound arrives there is a likelihood: for each possible direction, how probable are these particular sensations? Bayes's rule says that the posterior, the distribution the brain should act on, is proportional to the prior multiplied by the likelihood.[^6] The prior says what to expect; the evidence says what was observed; the posterior is the compromise, and it leans toward whichever of the two is more precise.

Figure 6.2 shows the consequence for the simplest case, where both are bell curves. When the evidence is sharp, the posterior sits almost on the evidence, and the prior barely matters. When the evidence is noisy, the posterior sits near the prior, and the senses barely matter. Neither extreme is a failure. A system that always trusted its senses would be captured by every flicker of noise; a system that always trusted its prior would be blind. The optimal weighting is set by relative precision, the inverse of a distribution's variance (the narrower the curve, the more precise), and it changes from moment to moment as the quality of the evidence changes.

![Figure 6.2. Combining a prior with sensory evidence. A: precise evidence pulls the posterior toward itself. B: the same prior with noisy evidence; the posterior stays near the prior. The weighting is set by the relative precisions.](images/fig_bayes.png)

This is the sense in which perception is inference. The brain does not compute Bayes's rule symbolically any more than a thrown ball solves differential equations. But the system behaves, to a good approximation, as the rule says it should, and the rest of this chapter is about the machinery that produces that behavior and the places where the approximation shows.

Where do the priors come from? From Chapter 5. A prior is learned structure: the accumulated statistical regularities of a lifetime of input, written into synaptic weights by the plasticity mechanisms already described. The light-from-above prior is the clearest example. Light has come from above for the whole of evolutionary history and for the whole of each individual life, and the visual system assumes it. A disc shaded light on top is seen as a bump, a disc shaded light on the bottom as a dent, and rotating the image swaps them (Figure 6.3B).[^7] No one is taught this, and chicks reared from hatching under light from below still behave as if light came from above, so the assumption is at least partly in place before experience. But it is not fixed. The prior that human adults actually hold is light from above and a little to the left, and in 2004 Adams, Graf, and Ernst shifted it: after observers had touched shaded discs whose felt shape agreed with a light source rotated away from the usual direction, their judgments of bumps and dents moved toward the new direction, and the shift carried over to a lightness task that had never been trained.[^8] A prior is in the weights, and the weights can be rewritten.

![Figure 6.3. The light-from-above prior. A: discs shaded lighter on top are seen as bumps and the others as dents. B: the same image rotated by 180 degrees; every disc reverses. The shading is identical in both panels; only the assumption about where the light is differs.](images/fig_light_above.png)

# The Hierarchy

Perception is carried out by a hierarchy of cortical areas, and the visual hierarchy is the best understood (Figure 6.4). Retinal ganglion cells project to the lateral geniculate nucleus of the thalamus, the LGN, and the LGN projects to the primary visual cortex, V1, at the back of the brain. From V1 the signal passes to V2, V4, and the inferotemporal cortex, IT, along what is called the ventral stream, and in parallel to areas specialized for motion and location along the dorsal stream.[^9]

![Figure 6.4. The ventral visual pathway. Receptive fields grow and preferences become more abstract at each stage. Feedforward connections carry evidence upward; feedback connections, at least as numerous, carry predictions and context downward. In mammals there is essentially no feedback to the retina.](images/fig_hierarchy.png)

Two things change at each stage. The receptive field, the region of the visual field that can influence a neuron, grows, from a fraction of a degree in V1 to most of the visual field in IT. And the preferred stimulus becomes more abstract. A V1 neuron responds to an oriented edge at one place.[^10] A V4 neuron responds to a curved contour or a color in a larger region. An IT neuron responds to an object, a face, or a hand, more or less regardless of where it appears, how large it is, or how it is lit.[^11] The hierarchy builds invariance: the same thing is recognized as the same thing across the enormous variation in images that it can produce.

This feedforward sweep is fast. An image flashed for a few tens of milliseconds produces a selective response in IT about a hundred milliseconds later, and a human can categorize a scene as containing an animal or not in about a hundred and fifty milliseconds.[^12] Convolutional neural networks were modeled on this sweep: Fukushima's neocognitron of 1980 stacked alternating layers of feature detectors and pooling units in explicit imitation of Hubel and Wiesel's simple and complex cells, and every later convolutional network keeps that plan.[^13] The best of them predict the responses of IT neurons to novel images better than any model built by hand.[^14] This is the part of perception that artificial systems have reproduced.

But the sweep is not the whole hierarchy, nor even most of it. Feedback connections, running from each area back down to the areas below, are at least as numerous as the feedforward ones. In the most complete count of macaque visual pathways to date, Markov and colleagues found more feedback pathways than feedforward pathways; a count of pathways is not a count of axons or synapses, though, and whether feedback outnumbers feedforward at every stage is not established.[^15] At the thalamus it plainly does. The LGN, the thalamic relay that the retina feeds, receives only about a tenth of its synapses from the retina; the rest come from the cortex and the brainstem.[^16] Anatomically, the visual system is not a pipeline from eye to cortex. It is a loop, and the downward half is at least as large as the upward half. Any account of perception has to say what the downward half is for.

# Predictive Coding

The account that has organized the field for the last three decades is called predictive coding, and it is a direct implementation of Helmholtz's idea in the anatomy of Figure 6.4.[^17]

Each level of the hierarchy holds a hypothesis about what the level below is receiving. It sends that hypothesis downward as a prediction. The level below compares the prediction with what it actually has and sends upward only the difference, the prediction error. The level above uses the error to revise its hypothesis, sends a revised prediction, and the cycle repeats until the error is small. What ascends the hierarchy is not the image but the part of the image that was not expected (Figure 6.5A).

This is prediction error in a different sense from Chapter 3, and the two should not be confused. There, a single number, broadcast by a large population of dopamine neurons, said how much better or worse than expected an outcome was: a scalar about value, the quantity that temporal-difference learning computes. Here, a whole pattern of errors about content, one for every feature at every level, passes between cortical layers and never leaves the sensory hierarchy. Readers who know temporal-difference learning will recognize the family resemblance, and theorists have tried to unify the two, but they are different signals carried by different cells, and the sensory one has no reward in it.

![Figure 6.5. Predictive coding. A: each level sends predictions down and receives errors up; the proposed mapping onto the canonical microcircuit places error units in the superficial layers and prediction units in the deep layers. B: a simulated error signal for a tone repeated six times, replaced once, and repeated again. Error falls with repetition and spikes at the change.](images/fig_predictive.png)

The scheme has three consequences that look surprising until the scheme is understood. The first is that an expected stimulus produces less cortical activity than an unexpected one. If the prediction is good, the error is small, and the error is what is transmitted. The second is that the absence of an expected stimulus produces activity: a prediction with nothing to cancel it is itself an error. The third is that what a neuron responds to depends on context, because the prediction arriving from above depends on everything the higher level knows.

All three are observed, though the first needs care. A stimulus repeated several times evokes a smaller response each time, in single neurons and in whole-brain imaging; this is called repetition suppression, and it is one of the most reproducible phenomena in sensory cortex (Figure 6.5B).[^18] On its own, though, it is weak evidence for prediction, because a fatigued neuron or a population sharpening its tuning would show the same decline, and the review that catalogs these models declines to choose among them. The decisive test holds repetition fixed and varies expectation. In 2008 Summerfield and colleagues showed pairs of faces in blocks where a repeat was likely and blocks where it was rare; the same repeated face suppressed the fusiform face area more when the repeat was expected, so expectation, not repetition itself, was setting the response, and this expectation suppression has since been separated in time from repetition suppression in human auditory cortex.[^19]

A tone omitted from a regular sequence evokes a response at the moment it should have occurred.[^20] The deviant tone in a sequence of standards evokes a distinctive electrical signature at the scalp, the mismatch negativity, about one to two hundred milliseconds after it arrives; it is detectable, though attenuated, in sleeping adults, it is present in newborn infants, and it reflects a prediction being violated rather than anything about the tone itself.[^21]

Neurons in V1, finally, respond to a line most strongly when it ends inside their receptive field, a long-known puzzle called end-stopping, which the first predictive coding model of the visual cortex, published in 1999, reproduced without being designed to: a line that continues is predictable from its surroundings, and a line that stops is not.[^22]

The scheme also fits the microcircuit of Chapter 4 in a specific way. The superficial layers of cortex, which project forward, carry activity dominated by fast gamma rhythms; the deep layers, which project backward, carry activity dominated by the slower alpha and beta rhythms. Predictive coding proposes that the superficial layers hold the error units and the deep layers the prediction units, so that errors ascend on gamma and predictions descend on alpha and beta. Recordings from several areas at once support the direction of this traffic.[^23] It is a model, and the mapping is not settled, but it is the kind of model that could be wrong in detail, which is the kind worth having.

# Illusions Are Correct Answers

If perception is inference, illusions are what inference looks like when the prior is right about the world and wrong about the picture. They are the most direct evidence we have for which priors the visual system holds.

In Adelson's checker-shadow figure (Figure 6.6), the squares marked A and B are printed in exactly the same gray. They do not look it, and they will not look it after you have measured them. The visual system has inferred a cylinder, a light source, and a shadow, and it has discounted the shadow before reporting the surface color of B. That is the correct computation. In a real scene, a surface in shadow that reflects as much light as a surface in the open really is lighter, and a visual system that reported raw luminance would misjudge every surface that fell in shade. The figure defeats the system by presenting a shadow with nothing behind it.[^24]

![Figure 6.6. Adelson's checker-shadow illusion. The squares marked A and B are the same shade of gray. The visual system infers a shadow and discounts it, which is the right inference for a real scene.](images/checker_shadow.png)

The Kanizsa triangle (Figure 6.7A) contains no triangle. Three discs with wedges removed and three corner fragments are arranged so that the most probable cause of the image is a white triangle lying on top of three black discs and an outlined triangle. The visual system reports that cause, complete with edges that are not in the image and a surface that looks whiter than the identical white around it. Neurons in V2 respond to these illusory contours as if they were real, which, under the hypothesis, they are.[^25]

![Figure 6.7. Two illusions as inferences. A: the Kanizsa triangle; the occluding white triangle is inferred, not drawn. B: the Müller-Lyer figure; the two horizontal lines are the same length but are read as corners at different depths.](images/fig_illusions.png)

In the Müller-Lyer figure (Figure 6.7B) two equal lines look unequal. One explanation, due to Richard Gregory, is that the fins are read as the edges of corners in a world of right-angled rooms and buildings, what Gregory called a carpentered world: arrowheads as the near corner of a building, arrow tails as the far corner of a room. A far corner that subtends the same angle as a near one must be longer, and the system scales accordingly.[^26] The explanation is debated, and that is the point. Each illusion is a probe, and arguments about illusions are arguments about which prior the system is using.

The hollow-mask illusion is the strongest of all. A face mask viewed from the inside, concave, is seen as convex, a normal face, even when it is slowly rotating and stereo vision and shading both report the truth. The prior that faces are convex is so strong that it overrides the evidence completely. The illusion weakens at close range, where stereo evidence becomes precise enough to win, and it is measurably weaker in people with schizophrenia, an observation to which the chapter returns.[^27]

What all of these show is that the output of the perceptual system is not the image and not the world but the posterior, and that the posterior can be moved by manipulating either the evidence or the prior.

# Attention as Precision

Bayes's rule weights evidence by its precision, and the brain cannot know the precision of a signal without estimating it. That estimate has to be represented somewhere and has to change what the circuit does. The proposal that follows from predictive coding is that this is what attention is: the gain applied to prediction errors, raised where the evidence is expected to be reliable and lowered where it is not.[^28]

The proposal unifies a great deal. Attention to a location increases the response of neurons whose receptive fields cover it and decreases the response of neighbors, which is the biased competition of Chapter 4's lateral inhibition with a top-down bias setting the winner.[^29] Attention increases the gamma synchrony of the attended population, which, through the oscillatory gating described in Chapter 4, lets its spikes arrive during the receptive phase of the next area and so increases their weight.[^30] And attention makes the attended evidence count for more in the posterior, which is what raising its precision means.

Precision also has a chemistry, and it is the chemistry of Chapter 3. Acetylcholine, released from the basal forebrain into cortex, increases the gain of feedforward sensory input relative to recurrent and feedback input; a cholinergic cortex trusts its senses more and its expectations less.[^31] One influential account assigns acetylcholine to expected uncertainty, the known unreliability of a familiar cue, and norepinephrine to unexpected uncertainty, the moment when the world changes and the current model should be discarded.[^32] The noradrenergic burst that accompanies a surprise is, on this reading, a global instruction to lower the precision of every prediction at once.

The cost of precision weighting is that what is not attended is barely seen. In the best-known demonstration, observers counting passes in a basketball video fail to notice a person in a gorilla suit walking through the middle of the scene.[^33] In change blindness, large alterations to a scene go unnoticed if they coincide with a blink or a cut.[^34] These are not failures of the eye; the gorilla was on the retina for several seconds. They are the consequence of a system that transmits only what it has been told to find surprising.

# Combining the Senses

The clearest quantitative test of the Bayesian account uses two senses at once. If the brain weights evidence by precision, then when vision and touch both report the width of an object, the combined estimate should lie between them, closer to the more reliable sense, and should be more precise than either alone. The weights can be computed exactly from the reliability of each sense measured separately.

In 2002 Marc Ernst and Martin Banks ran this experiment with a bar that observers could see and feel at the same time, degrading vision by adding noise to the display. With clear vision, the estimate followed the eyes. As the visual noise increased, the weight shifted toward touch, and at every noise level the observed weights matched the computed optimum (Figure 6.8).[^35] The brain was not favoring vision as a rule. It was favoring whichever sense was more precise, trial by trial. This is the local sense, argued in Chapter 3, in which the brain optimizes: a circuit behaves as if it were minimizing a well-defined local cost, here the variance of its estimate.

![Figure 6.8. Precision-weighted combination of vision and touch. A: with a clear view, the combined estimate follows vision. B: with vision blurred, touch dominates. In both cases the combined estimate is narrower than either input, and the weights are set by the relative precisions.](images/fig_cues.png)

Everyday perception is full of the same computation. The ventriloquist's voice appears to come from the dummy's mouth because vision locates things more precisely than hearing, so the posterior for the sound's location follows the visible moving mouth.[^36] In the McGurk effect, a recording of one syllable dubbed onto a face mouthing a different syllable is heard as a third syllable, a compromise between what was heard and what was seen.[^37] The senses are not separate channels to a central viewer. They are sources of evidence, pooled in proportion to how much each can be trusted.

# Perception Is Active

The account so far has treated the brain as if it sat still and waited for evidence. It does not. It moves the sense organs to get the evidence it wants, and that changes the problem in two ways.

The first is that the brain must distinguish sensation caused by the world from sensation caused by its own movement. When the eye jumps ten degrees, the image sweeps ten degrees across the retina, exactly as it would if the world had jumped. It does not look that way. The solution, proposed independently by von Holst and by Sperry in 1950, is that every motor command is copied and sent to the sensory system, which uses it to predict the sensory consequence of the movement and subtract it.[^38] The copy is called the efference copy, the prediction is a forward model, and the comparison is shown in Figure 6.9.

![Figure 6.9. Efference copy. A copy of each motor command is sent to a forward model that predicts the resulting sensory change. The prediction is subtracted from the actual sensation, so that self-caused changes are canceled and only changes caused by the world remain.](images/fig_efference.png)

If the predicted slip matches the actual slip, the world is reported as stationary. Press gently on your eyelid and move the eye by hand: there is no command, no prediction, nothing is subtracted, and the world lurches. The cerebellum of Chapter 4, which learns to predict the sensory consequences of commands, is a principal site of this forward model.[^39]

The same mechanism is why you cannot tickle yourself: the sensation is predicted and canceled before it is felt.[^40]

The second is that movement is itself a tool of inference. A saccade is a decision about where evidence is most needed, and the sequence of fixations on a scene depends on the question being asked.[^41] A rat sweeps its whiskers across an object at a rate it controls; a dog sniffs in bursts timed to its uncertainty; a reader's eyes land on the words that the sentence so far has made least predictable.[^42] In each case the organism is not receiving evidence but sampling it, choosing the sample that will reduce its uncertainty most. Perception and action, kept apart in the textbooks, are two halves of one loop: the hypothesis determines where to look, and what is seen revises the hypothesis. Some theorists go further and treat action as inference too, the body moving so as to make the brain's predictions come true.[^43] Whether or not one accepts that framing, the practical lesson is secure. An observer that cannot act is solving a harder problem than any brain has ever had to solve.

# Learning the Priors

If perception rests on priors, the question of where they come from is the question of how perception is learned, and the answer connects this chapter to the last.

Some priors are present at or near birth. Newborns orient to face-like patterns within hours, and the chicks reared under light from below, described earlier, held the light-from-above assumption without instruction.[^44] But a prior present at birth is not a prior fixed for life, as the adults in the Adams experiment show, and most of the structure of sensory cortex is learned from the statistics of the input. That learning has the properties Chapter 5 would predict. It is slow, it is gated, and it has a window.

The window is the one Hubel and Wiesel found in kittens with one eye closed (Chapter 1).[^45] This critical period, the strict form of the sensitive periods introduced there, closes, in the cat, after a few months and in humans after a few years. Kittens raised in environments containing only vertical stripes grew up with cortices in which almost no neuron responded to horizontal edges, and they bumped into horizontal bars.[^46] The critical period opens and closes under the control of inhibitory maturation and of the neuromodulators of Chapter 3; it is a time when the plasticity rules of Chapter 5 are turned up, and its closing is what makes adult perception stable and adult perceptual learning slow.[^47]

What is learned during the window is the statistics of natural images, and that can be shown directly. In 1996 Olshausen and Field trained a simple model to represent patches of photographs using as few active units as possible. The units it learned were localized, oriented, band-pass filters (Figure 6.10), each responding to an edge of one orientation and one spatial scale at one place, essentially the receptive fields that Hubel and Wiesel had found in V1 thirty years earlier.[^48] Nothing about edges was built in. Edges are what the world contains, and a system that learns to predict the world ends up with detectors for them. The same procedure applied to natural sounds produces filters resembling those of the auditory nerve.[^49] The receptive fields of sensory cortex are, to a first approximation, the priors of the natural world made into tissue.

![Figure 6.10. Receptive fields of the kind found in primary visual cortex: each cell responds to an edge of one orientation and scale at one location. Fields of this form emerge in models trained only to represent natural images efficiently.](images/fig_gabor.png)

This learning never fully stops. Wear prism goggles that shift the world sideways and reaching errors vanish in minutes, as the cerebellar forward model relearns.[^50] Wear goggles that invert the world and within days you can walk, reach, and ride a bicycle in it, as Stratton and Kohler reported; whether it ever comes to look upright is disputed, since a controlled study in 1999 found full motor adaptation after six to ten days but no perceptual re-inversion, and Stratton's own reports of uprightness were intermittent.[^51] View the world through a colored filter for a few hours a day for several days and the wavelength you call pure yellow shifts, and it stays shifted for a week or two after the filter comes off.[^52] The adult perceptual system is a model under continual revision, slow at its core and fast at its periphery, exactly as the two consolidation clocks of Chapter 5 would suggest.

# When Inference Goes Wrong

A system that constructs its percepts from priors and evidence can fail in two directions, and both are seen in the clinic.

When the evidence is removed, the priors run unopposed. People who lose their vision late in life through disease of the eye frequently begin to see vivid, detailed hallucinations, faces, patterns, figures in period dress, while knowing perfectly well that nothing is there; the condition is named for Charles Bonnet, who described it in his grandfather in 1760.[^53] A visual cortex that has lost its input does not go silent. It continues to generate hypotheses, and with no error signal to correct them they are experienced as sight. Phantom limbs are the same phenomenon in another modality: the body model persists after the body part is gone, and its predictions, unanswered, are felt.[^54]

When the precision of evidence and prior is misweighted, perception bends. The hollow-mask illusion is weaker in schizophrenia, which suggests that priors there have lost some of their grip; at the same time, hallucinations and delusions can be understood as priors with too much precision, or as noise in the error channel that is read as signal. The two readings are not contradictory; a system can weight its priors too strongly at one level and too weakly at another.[^55] One account of autistic perception proposes the opposite imbalance, sensory precision too high relative to the priors, so that the world is experienced in unfiltered detail and small deviations from expectation are overwhelming.[^56] All of these are hypotheses, not settled findings, and they are offered here because they show what the framework buys: a vocabulary in which disorders of perception are disorders of weighting, and the weights are set by mechanisms that are known and can be measured: inhibition, acetylcholine, norepinephrine, and oscillatory gain, with dopamine, which the accounts of psychosis just cited place at the center, a candidate whose role in perceptual precision is argued rather than shown.

# Implications for Artificial Intelligence

Perception is the domain in which artificial systems most clearly match the brain and in which the comparison is most instructive about what they lack.

First, the feedforward sweep has been reproduced. Deep convolutional networks trained to classify images develop a hierarchy of features, from oriented edges to object parts, that resembles the ventral stream closely enough to predict the responses of its neurons. The resemblance is not a coincidence; both are solutions to the same statistical problem, and the fact that gradient descent and evolution arrived at a similar place is evidence that the place is not arbitrary.[^57] The resemblance is partial, though. Networks trained on photographs lean on texture where humans lean on shape, and they part company with IT on images outside the training distribution, so the shared solution covers the easy part of the problem rather than all of it.[^58]

Second, the loops have not been. Standard networks have no feedback, no prediction, and no error signal at inference time; they map an input to an output in one pass. The brain spends most of its visual anatomy on the other direction. Adversarial examples, in which an imperceptible change to an image produces a confident misclassification, are sometimes described as evidence without priors, but that is not right: a trained classifier is nothing but priors, learned from millions of images and stored in its weights. What it lacks is a way to check them. The vulnerability is better explained by the near-linear behavior of these networks in high dimensions and by their reliance on features that predict the label but are invisible to us, and humans given only a brief glimpse of such images can be fooled by them too.[^59] The difference is what happens next. A feedforward classifier has delivered its answer; a brain confronted with a doubtful image would predict a cat, compare the prediction with the input, find the error large, and look again.

Third, precision is missing. The attention mechanism of transformers weights inputs by learned relevance, which is a cousin of precision weighting, but there is nothing in most artificial systems that estimates how reliable each input is and discounts it accordingly, nor a global signal, like norepinephrine, that says the model should be distrusted now.[^60] Systems that must operate on degraded sensors, in fog or in noise, need exactly this.

Fourth, generative models are the right direction. A network that can generate the data it classifies has, in effect, a prior and a likelihood and can compute something like a posterior; variational autoencoders and diffusion models are explicit attempts to build such machinery, and the best current explanations of cortex are, in essence, hierarchical generative models trained by prediction error.[^61] Whether predictive coding can replace backpropagation as a learning rule is an open research question. The brain is an existence proof that some local rule suffices, not that this one does, and the strongest results so far show that predictive-coding networks can approximate backpropagation, not that they surpass it.[^62]

Fifth, perception should be active. A system that chooses where to sample is solving an easier problem than one that must process everything, and robotics has begun to borrow the saccade, the forward model, and the efference copy for exactly the reasons the brain uses them.[^63] An agent that cannot predict the sensory consequences of its own actions cannot tell what it did from what the world did, and that is a fatal confusion for anything that must learn from experience.

# The Central Lesson

The senses deliver evidence that does not determine the world, and the brain supplies the rest. It holds a model of what is usually true, written into its synapses by the plasticity of Chapter 5, and it combines that model with the incoming evidence in proportion to how much each can be trusted. The combination is carried out by a hierarchy in which predictions descend and errors ascend, so that what the cortex transmits is not the image but its surprise. Attention sets the trust, the neuromodulators of Chapter 3 set the attention, and action chooses what evidence to gather next. Illusions, hallucinations, and the stability of the visual world are all the same mechanism seen from different sides. You do not see what is there. You see your best current hypothesis about what is there, and most of the time it is right.

# Next Chapter

Chapter 7: Emotion and the Body: How Internal States Tell the Brain What Matters

# References and Attribution

## Figure Attribution

Figures 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 6.8, 6.9, and 6.10 were drawn for this book. The curves in Figures 6.2 and 6.8, the error trace in Figure 6.5B, and the receptive fields in Figure 6.10 are illustrative computations, not recorded data.

Figure 6.6: "Checker shadow illusion" by Edward H. Adelson, vectorized by Wikimedia Commons user Pbroks13, CC BY-SA 4.0, via Wikimedia Commons.

## Epigraph

Hermann von Helmholtz, *Treatise on Physiological Optics*, vol. III, §26, trans. J. P. C. Southall (Optical Society of America, 1925); first published in German in 1867.

## References

Adams, W. J., Graf, E. W., & Ernst, M. O. (2004). Experience can change the 'light-from-above' prior. *Nature Neuroscience*, 7(10), 1057–1058.

Adelson, E. H. (2000). Lightness perception and lightness illusions. In M. S. Gazzaniga (Ed.), *The New Cognitive Neurosciences* (2nd ed., pp. 339–351). MIT Press.

Alais, D., & Burr, D. (2004). The ventriloquist effect results from near-optimal bimodal integration. *Current Biology*, 14(3), 257–262.

Bajcsy, R., Aloimonos, Y., & Tsotsos, J. K. (2018). Revisiting active perception. *Autonomous Robots*, 42(2), 177–196.

Bastos, A. M., Usrey, W. M., Adams, R. A., Mangun, G. R., Fries, P., & Friston, K. J. (2012). Canonical microcircuits for predictive coding. *Neuron*, 76(4), 695–711.

Bastos, A. M., Vezoli, J., Bosman, C. A., Schoffelen, J.-M., Oostenveld, R., Dowdall, J. R., De Weerd, P., Kennedy, H., & Fries, P. (2015). Visual areas exert feedforward and feedback influences through distinct frequency channels. *Neuron*, 85(2), 390–401.

Bayes, T. (1763). An essay towards solving a problem in the doctrine of chances. *Philosophical Transactions of the Royal Society of London*, 53, 370–418.

Blakemore, C., & Cooper, G. F. (1970). Development of the brain depends on the visual environment. *Nature*, 228, 477–478.

Blakemore, S.-J., Wolpert, D. M., & Frith, C. D. (1998). Central cancellation of self-produced tickle sensation. *Nature Neuroscience*, 1(7), 635–640.

Bonnet, C. (1760). *Essai analytique sur les facultés de l'âme*. Copenhagen: Philibert.

Curcio, C. A., Sloan, K. R., Kalina, R. E., & Hendrickson, A. E. (1990). Human photoreceptor topography. *Journal of Comparative Neurology*, 292(4), 497–523.

Dayan, P., Hinton, G. E., Neal, R. M., & Zemel, R. S. (1995). The Helmholtz machine. *Neural Computation*, 7(5), 889–904.

Desimone, R., & Duncan, J. (1995). Neural mechanisms of selective visual attention. *Annual Review of Neuroscience*, 18, 193–222.

Dima, D., Roiser, J. P., Dietrich, D. E., Bonnemann, C., Lanfermann, H., Emrich, H. M., & Dillo, W. (2009). Understanding why patients with schizophrenia do not perceive the hollow-mask illusion using dynamic causal modelling. *NeuroImage*, 46(4), 1180–1186.

Elsayed, G. F., Shankar, S., Cheung, B., Papernot, N., Kurakin, A., Goodfellow, I., & Sohl-Dickstein, J. (2018). Adversarial examples that fool both computer vision and time-limited humans. *Advances in Neural Information Processing Systems*, 31.

Ernst, M. O., & Banks, M. S. (2002). Humans integrate visual and haptic information in a statistically optimal fashion. *Nature*, 415, 429–433.

Feldman, H., & Friston, K. J. (2010). Attention, uncertainty, and free-energy. *Frontiers in Human Neuroscience*, 4, 215.

Felleman, D. J., & Van Essen, D. C. (1991). Distributed hierarchical processing in the primate cerebral cortex. *Cerebral Cortex*, 1(1), 1–47.

ffytche, D. H., Howard, R. J., Brammer, M. J., David, A., Woodruff, P., & Williams, S. (1998). The anatomy of conscious vision: An fMRI study of visual hallucinations. *Nature Neuroscience*, 1(8), 738–742.

Fletcher, P. C., & Frith, C. D. (2009). Perceiving is believing: A Bayesian approach to explaining the positive symptoms of schizophrenia. *Nature Reviews Neuroscience*, 10(1), 48–58.

Fries, P. (2015). Rhythms for cognition: Communication through coherence. *Neuron*, 88(1), 220–235.

Fries, P., Reynolds, J. H., Rorie, A. E., & Desimone, R. (2001). Modulation of oscillatory neuronal synchronization by selective visual attention. *Science*, 291(5508), 1560–1563.

Friston, K. (2005). A theory of cortical responses. *Philosophical Transactions of the Royal Society B*, 360(1456), 815–836.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.

Fukushima, K. (1980). Neocognitron: A self-organizing neural network model for a mechanism of pattern recognition unaffected by shift in position. *Biological Cybernetics*, 36(4), 193–202.

Geirhos, R., Rubisch, P., Michaelis, C., Bethge, M., Wichmann, F. A., & Brendel, W. (2019). ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness. *International Conference on Learning Representations (ICLR)*.

Goodfellow, I. J., Shlens, J., & Szegedy, C. (2015). Explaining and harnessing adversarial examples. *International Conference on Learning Representations (ICLR)*.

Gregory, R. L. (1963). Distortion of visual space as inappropriate constancy scaling. *Nature*, 199, 678–680.

Gregory, R. L. (1970). *The Intelligent Eye*. Weidenfeld & Nicolson.

Grill-Spector, K., Henson, R., & Martin, A. (2006). Repetition and the brain: Neural models of stimulus-specific effects. *Trends in Cognitive Sciences*, 10(1), 14–23.

Gross, C. G., Rocha-Miranda, C. E., & Bender, D. B. (1972). Visual properties of neurons in inferotemporal cortex of the macaque. *Journal of Neurophysiology*, 35(1), 96–111.

Hasselmo, M. E. (2006). The role of acetylcholine in learning and memory. *Current Opinion in Neurobiology*, 16(6), 710–715.

Helmholtz, H. von (1867). *Handbuch der physiologischen Optik*. Leipzig: Voss. English edition: *Treatise on Physiological Optics*, vol. III, trans. J. P. C. Southall (Optical Society of America, 1925).

Hensch, T. K. (2005). Critical period plasticity in local cortical circuits. *Nature Reviews Neuroscience*, 6(11), 877–888.

Hershberger, W. (1970). Attached-shadow orientation perceived as depth by chickens reared in an environment illuminated from below. *Journal of Comparative and Physiological Psychology*, 73(3), 407–411.

Ho, J., Jain, A., & Abbeel, P. (2020). Denoising diffusion probabilistic models. *Advances in Neural Information Processing Systems*, 33.

Hubel, D. H., & Wiesel, T. N. (1962). Receptive fields, binocular interaction and functional architecture in the cat's visual cortex. *Journal of Physiology*, 160(1), 106–154.

Hubel, D. H., & Wiesel, T. N. (1965). Receptive fields and functional architecture in two nonstriate visual areas (18 and 19) of the cat. *Journal of Neurophysiology*, 28(2), 229–289.

Hubel, D. H., & Wiesel, T. N. (1970). The period of susceptibility to the physiological effects of unilateral eye closure in kittens. *Journal of Physiology*, 206(2), 419–436.

Hung, C. P., Kreiman, G., Poggio, T., & DiCarlo, J. J. (2005). Fast readout of object identity from macaque inferior temporal cortex. *Science*, 310(5749), 863–866.

Ilyas, A., Santurkar, S., Tsipras, D., Engstrom, L., Tran, B., & Madry, A. (2019). Adversarial examples are not bugs, they are features. *Advances in Neural Information Processing Systems*, 32.

Johnson, M. H., Dziurawiec, S., Ellis, H., & Morton, J. (1991). Newborns' preferential tracking of face-like stimuli and its subsequent decline. *Cognition*, 40(1–2), 1–19.

Jonas, J. B., Schmidt, A. M., Müller-Bergh, J. A., Schlötzer-Schrehardt, U. M., & Naumann, G. O. H. (1992). Human optic nerve fiber count and optic disc size. *Investigative Ophthalmology & Visual Science*, 33(6), 2012–2018.

Kanizsa, G. (1955). Margini quasi-percettivi in campi con stimolazione omogenea. *Rivista di Psicologia*, 49(1), 7–30.

Kingma, D. P., & Welling, M. (2014). Auto-encoding variational Bayes. *International Conference on Learning Representations (ICLR)*.

Kleinfeld, D., Ahissar, E., & Diamond, M. E. (2006). Active sensation: Insights from the rodent vibrissa sensorimotor system. *Current Opinion in Neurobiology*, 16(4), 435–444.

Knill, D. C., & Pouget, A. (2004). The Bayesian brain: The role of uncertainty in neural coding and computation. *Trends in Neurosciences*, 27(12), 712–719.

Koch, K., McLean, J., Segev, R., Freed, M. A., Berry, M. J., Balasubramanian, V., & Sterling, P. (2006). How much the eye tells the brain. *Current Biology*, 16(14), 1428–1434.

Kohler, I. (1962). Experiments with goggles. *Scientific American*, 206(5), 62–72.

Lawson, R. P., Rees, G., & Friston, K. J. (2014). An aberrant precision account of autism. *Frontiers in Human Neuroscience*, 8, 302.

Lewicki, M. S. (2002). Efficient coding of natural sounds. *Nature Neuroscience*, 5(4), 356–363.

Linden, D. E. J., Kallenbach, U., Heinecke, A., Singer, W., & Goebel, R. (1999). The myth of upright vision: A psychophysical and functional imaging study of adaptation to inverting spectacles. *Perception*, 28(4), 469–481.

Markov, N. T., Vezoli, J., Chameau, P., Falchier, A., Quilodran, R., Huissoud, C., Lamy, C., Misery, P., Giroud, P., Ullman, S., Barone, P., Dehay, C., Knoblauch, K., & Kennedy, H. (2014). Anatomy of hierarchy: Feedforward and feedback pathways in macaque visual cortex. *Journal of Comparative Neurology*, 522(1), 225–259.

Martin, T. A., Keating, J. G., Goodkin, H. P., Bastian, A. J., & Thach, W. T. (1996). Throwing while looking through prisms. I. Focal olivocerebellar lesions impair adaptation. *Brain*, 119(4), 1183–1198.

Matin, E. (1974). Saccadic suppression: A review and an analysis. *Psychological Bulletin*, 81(12), 899–917.

McGurk, H., & MacDonald, J. (1976). Hearing lips and seeing voices. *Nature*, 264, 746–748.

Millidge, B., Seth, A., & Buckley, C. L. (2022). Predictive coding: A theoretical and experimental review. *arXiv*, 2107.12979.

Mumford, D. (1992). On the computational architecture of the neocortex. II. The role of cortico-cortical loops. *Biological Cybernetics*, 66(3), 241–251.

Müller-Lyer, F. C. (1889). Optische Urteilstäuschungen. *Archiv für Anatomie und Physiologie, Physiologische Abteilung*, Supplement, 263–270.

Neitz, J., Carroll, J., Yamauchi, Y., Neitz, M., & Williams, D. R. (2002). Color perception is mediated by a plastic neural mechanism that is adjustable in adults. *Neuron*, 35(4), 783–792.

Näätänen, R., Gaillard, A. W. K., & Mäntysalo, S. (1978). Early selective-attention effect on evoked potential reinterpreted. *Acta Psychologica*, 42(4), 313–329.

Näätänen, R., Paavilainen, P., Rinne, T., & Alho, K. (2007). The mismatch negativity (MMN) in basic research of central auditory processing: A review. *Clinical Neurophysiology*, 118(12), 2544–2590.

Olshausen, B. A., & Field, D. J. (1996). Emergence of simple-cell receptive field properties by learning a sparse code for natural images. *Nature*, 381, 607–609.

Pellicano, E., & Burr, D. (2012). When the world becomes 'too real': A Bayesian explanation of autistic perception. *Trends in Cognitive Sciences*, 16(10), 504–510.

Ramachandran, V. S. (1988). Perception of shape from shading. *Nature*, 331, 163–166.

Ramachandran, V. S. (1992). Blind spots. *Scientific American*, 266(5), 86–91.

Ramachandran, V. S., & Hirstein, W. (1998). The perception of phantom limbs: The D. O. Hebb lecture. *Brain*, 121(9), 1603–1630.

Rao, R. P. N., & Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience*, 2(1), 79–87.

Rayner, K. (1998). Eye movements in reading and information processing: 20 years of research. *Psychological Bulletin*, 124(3), 372–422.

Rensink, R. A., O'Regan, J. K., & Clark, J. J. (1997). To see or not to see: The need for attention to perceive changes in scenes. *Psychological Science*, 8(5), 368–373.

Sherman, S. M., & Guillery, R. W. (2006). *Exploring the Thalamus and Its Role in Cortical Function* (2nd ed.). MIT Press.

Simons, D. J., & Chabris, C. F. (1999). Gorillas in our midst: Sustained inattentional blindness for dynamic events. *Perception*, 28(9), 1059–1074.

Sperry, R. W. (1950). Neural basis of the spontaneous optokinetic response produced by visual inversion. *Journal of Comparative and Physiological Psychology*, 43(6), 482–489.

Sterzer, P., Adams, R. A., Fletcher, P., Frith, C., Lawrie, S. M., Muckli, L., Petrovic, P., Uhlhaas, P., Voss, M., & Corlett, P. R. (2018). The predictive coding account of psychosis. *Biological Psychiatry*, 84(9), 634–643.

Stratton, G. M. (1897). Vision without inversion of the retinal image. *Psychological Review*, 4(4), 341–360 and 4(5), 463–481.

Summerfield, C., Trittschuh, E. H., Monti, J. M., Mesulam, M.-M., & Egner, T. (2008). Neural repetition suppression reflects fulfilled perceptual expectations. *Nature Neuroscience*, 11(9), 1004–1006.

Sun, J., & Perona, P. (1998). Where is the sun? *Nature Neuroscience*, 1(3), 183–184.

Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow, I., & Fergus, R. (2014). Intriguing properties of neural networks. *International Conference on Learning Representations (ICLR)*.

Thorpe, S., Fize, D., & Marlot, C. (1996). Speed of processing in the human visual system. *Nature*, 381, 520–522.

Todorovic, A., & de Lange, F. P. (2012). Repetition suppression and expectation suppression are dissociable in time in early auditory evoked fields. *Journal of Neuroscience*, 32(39), 13389–13395.

Ungerleider, L. G., & Mishkin, M. (1982). Two cortical visual systems. In D. J. Ingle, M. A. Goodale, & R. J. W. Mansfield (Eds.), *Analysis of Visual Behavior* (pp. 549–586). MIT Press.

van Kerkoerle, T., Self, M. W., Dagnino, B., Gariel-Mathis, M.-A., Poort, J., van der Togt, C., & Roelfsema, P. R. (2014). Alpha and gamma oscillations characterize feedback and feedforward processing in monkey visual cortex. *Proceedings of the National Academy of Sciences*, 111(40), 14332–14341.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30.

von der Heydt, R., Peterhans, E., & Baumgartner, G. (1984). Illusory contours and cortical neuron responses. *Science*, 224(4654), 1260–1262.

von Holst, E., & Mittelstaedt, H. (1950). Das Reafferenzprinzip: Wechselwirkungen zwischen Zentralnervensystem und Peripherie. *Naturwissenschaften*, 37(20), 464–476.

Wacongne, C., Labyt, E., van Wassenhove, V., Bekinschtein, T., Naccache, L., & Dehaene, S. (2011). Evidence for a hierarchy of predictions and prediction errors in human cortex. *Proceedings of the National Academy of Sciences*, 108(51), 20754–20759.

Whittington, J. C. R., & Bogacz, R. (2017). An approximation of the error backpropagation algorithm in a predictive coding network with local Hebbian synaptic plasticity. *Neural Computation*, 29(5), 1229–1262.

Wiesel, T. N., & Hubel, D. H. (1963). Single-cell responses in striate cortex of kittens deprived of vision in one eye. *Journal of Neurophysiology*, 26(6), 1003–1017.

Wolpert, D. M., Miall, R. C., & Kawato, M. (1998). Internal models in the cerebellum. *Trends in Cognitive Sciences*, 2(9), 338–347.

Yamins, D. L. K., & DiCarlo, J. J. (2016). Using goal-driven deep learning models to understand sensory cortex. *Nature Neuroscience*, 19(3), 356–365.

Yamins, D. L. K., Hong, H., Cadieu, C. F., Solomon, E. A., Seibert, D., & DiCarlo, J. J. (2014). Performance-optimized hierarchical models predict neural responses in higher visual cortex. *Proceedings of the National Academy of Sciences*, 111(23), 8619–8624.

Yarbus, A. L. (1967). *Eye Movements and Vision*. Plenum Press.

Yu, A. J., & Dayan, P. (2005). Uncertainty, neuromodulation, and attention. *Neuron*, 46(4), 681–692.

[^1]: Helmholtz, H. von (1867). *Handbuch der physiologischen Optik*. Leipzig: Voss. English edition: *Treatise on Physiological Optics*, vol. III, trans. J. P. C. Southall (Optical Society of America, 1925). The doctrine of unconscious inference is set out in §26 of vol. III.

[^2]: Curcio, C. A., Sloan, K. R., Kalina, R. E., & Hendrickson, A. E. (1990). Human photoreceptor topography. *Journal of Comparative Neurology*, 292(4), 497–523; Jonas, J. B., Schmidt, A. M., Müller-Bergh, J. A., Schlötzer-Schrehardt, U. M., & Naumann, G. O. H. (1992). Human optic nerve fiber count and optic disc size. *Investigative Ophthalmology & Visual Science*, 33(6), 2012–2018.

[^3]: Koch, K., McLean, J., Segev, R., Freed, M. A., Berry, M. J., Balasubramanian, V., & Sterling, P. (2006). How much the eye tells the brain. *Current Biology*, 16(14), 1428–1434.

[^4]: Ramachandran, V. S. (1992). Blind spots. *Scientific American*, 266(5), 86–91.

[^5]: Matin, E. (1974). Saccadic suppression: A review and an analysis. *Psychological Bulletin*, 81(12), 899–917; Rayner, K. (1998). Eye movements in reading and information processing: 20 years of research. *Psychological Bulletin*, 124(3), 372–422.

[^6]: Bayes, T. (1763). An essay towards solving a problem in the doctrine of chances. *Philosophical Transactions of the Royal Society of London*, 53, 370–418; Knill, D. C., & Pouget, A. (2004). The Bayesian brain: The role of uncertainty in neural coding and computation. *Trends in Neurosciences*, 27(12), 712–719.

[^7]: Ramachandran, V. S. (1988). Perception of shape from shading. *Nature*, 331, 163–166.

[^8]: Hershberger, W. (1970). Attached-shadow orientation perceived as depth by chickens reared in an environment illuminated from below. *Journal of Comparative and Physiological Psychology*, 73(3), 407–411; Sun, J., & Perona, P. (1998). Where is the sun? *Nature Neuroscience*, 1(3), 183–184; Adams, W. J., Graf, E. W., & Ernst, M. O. (2004). Experience can change the 'light-from-above' prior. *Nature Neuroscience*, 7(10), 1057–1058.

[^9]: Ungerleider, L. G., & Mishkin, M. (1982). Two cortical visual systems. In D. J. Ingle, M. A. Goodale, & R. J. W. Mansfield (Eds.), *Analysis of Visual Behavior* (pp. 549–586). MIT Press; Felleman, D. J., & Van Essen, D. C. (1991). Distributed hierarchical processing in the primate cerebral cortex. *Cerebral Cortex*, 1(1), 1–47.

[^10]: Hubel, D. H., & Wiesel, T. N. (1962). Receptive fields, binocular interaction and functional architecture in the cat's visual cortex. *Journal of Physiology*, 160(1), 106–154.

[^11]: Gross, C. G., Rocha-Miranda, C. E., & Bender, D. B. (1972). Visual properties of neurons in inferotemporal cortex of the macaque. *Journal of Neurophysiology*, 35(1), 96–111.

[^12]: Thorpe, S., Fize, D., & Marlot, C. (1996). Speed of processing in the human visual system. *Nature*, 381, 520–522; Hung, C. P., Kreiman, G., Poggio, T., & DiCarlo, J. J. (2005). Fast readout of object identity from macaque inferior temporal cortex. *Science*, 310(5749), 863–866.

[^13]: Fukushima, K. (1980). Neocognitron: A self-organizing neural network model for a mechanism of pattern recognition unaffected by shift in position. *Biological Cybernetics*, 36(4), 193–202.

[^14]: Yamins, D. L. K., Hong, H., Cadieu, C. F., Solomon, E. A., Seibert, D., & DiCarlo, J. J. (2014). Performance-optimized hierarchical models predict neural responses in higher visual cortex. *Proceedings of the National Academy of Sciences*, 111(23), 8619–8624.

[^15]: Markov, N. T., Vezoli, J., Chameau, P., Falchier, A., Quilodran, R., Huissoud, C., Lamy, C., Misery, P., Giroud, P., Ullman, S., Barone, P., Dehay, C., Knoblauch, K., & Kennedy, H. (2014). Anatomy of hierarchy: Feedforward and feedback pathways in macaque visual cortex. *Journal of Comparative Neurology*, 522(1), 225–259.

[^16]: Sherman, S. M., & Guillery, R. W. (2006). *Exploring the Thalamus and Its Role in Cortical Function* (2nd ed.). MIT Press.

[^17]: Mumford, D. (1992). On the computational architecture of the neocortex. II. The role of cortico-cortical loops. *Biological Cybernetics*, 66(3), 241–251; Rao, R. P. N., & Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience*, 2(1), 79–87; Friston, K. (2005). A theory of cortical responses. *Philosophical Transactions of the Royal Society B*, 360(1456), 815–836.

[^18]: Grill-Spector, K., Henson, R., & Martin, A. (2006). Repetition and the brain: Neural models of stimulus-specific effects. *Trends in Cognitive Sciences*, 10(1), 14–23. The review compares fatigue, sharpening, and facilitation models of repetition suppression without endorsing one.

[^19]: Summerfield, C., Trittschuh, E. H., Monti, J. M., Mesulam, M.-M., & Egner, T. (2008). Neural repetition suppression reflects fulfilled perceptual expectations. *Nature Neuroscience*, 11(9), 1004–1006; Todorovic, A., & de Lange, F. P. (2012). Repetition suppression and expectation suppression are dissociable in time in early auditory evoked fields. *Journal of Neuroscience*, 32(39), 13389–13395.

[^20]: Wacongne, C., Labyt, E., van Wassenhove, V., Bekinschtein, T., Naccache, L., & Dehaene, S. (2011). Evidence for a hierarchy of predictions and prediction errors in human cortex. *Proceedings of the National Academy of Sciences*, 108(51), 20754–20759.

[^21]: Näätänen, R., Gaillard, A. W. K., & Mäntysalo, S. (1978). Early selective-attention effect on evoked potential reinterpreted. *Acta Psychologica*, 42(4), 313–329; Näätänen, R., Paavilainen, P., Rinne, T., & Alho, K. (2007). The mismatch negativity (MMN) in basic research of central auditory processing: A review. *Clinical Neurophysiology*, 118(12), 2544–2590.

[^22]: Hubel, D. H., & Wiesel, T. N. (1965). Receptive fields and functional architecture in two nonstriate visual areas (18 and 19) of the cat. *Journal of Neurophysiology*, 28(2), 229–289; Rao, R. P. N., & Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience*, 2(1), 79–87. End-stopped ("hypercomplex") cells were first described by Hubel and Wiesel.

[^23]: Bastos, A. M., Usrey, W. M., Adams, R. A., Mangun, G. R., Fries, P., & Friston, K. J. (2012). Canonical microcircuits for predictive coding. *Neuron*, 76(4), 695–711; van Kerkoerle, T., Self, M. W., Dagnino, B., Gariel-Mathis, M.-A., Poort, J., van der Togt, C., & Roelfsema, P. R. (2014). Alpha and gamma oscillations characterize feedback and feedforward processing in monkey visual cortex. *Proceedings of the National Academy of Sciences*, 111(40), 14332–14341; Bastos, A. M., Vezoli, J., Bosman, C. A., Schoffelen, J.-M., Oostenveld, R., Dowdall, J. R., De Weerd, P., Kennedy, H., & Fries, P. (2015). Visual areas exert feedforward and feedback influences through distinct frequency channels. *Neuron*, 85(2), 390–401.

[^24]: Adelson, E. H. (2000). Lightness perception and lightness illusions. In M. S. Gazzaniga (Ed.), *The New Cognitive Neurosciences* (2nd ed., pp. 339–351). MIT Press.

[^25]: Kanizsa, G. (1955). Margini quasi-percettivi in campi con stimolazione omogenea. *Rivista di Psicologia*, 49(1), 7–30; von der Heydt, R., Peterhans, E., & Baumgartner, G. (1984). Illusory contours and cortical neuron responses. *Science*, 224(4654), 1260–1262.

[^26]: Müller-Lyer, F. C. (1889). Optische Urteilstäuschungen. *Archiv für Anatomie und Physiologie, Physiologische Abteilung*, Supplement, 263–270; Gregory, R. L. (1963). Distortion of visual space as inappropriate constancy scaling. *Nature*, 199, 678–680.

[^27]: Gregory, R. L. (1970). *The Intelligent Eye*. Weidenfeld & Nicolson; Dima, D., Roiser, J. P., Dietrich, D. E., Bonnemann, C., Lanfermann, H., Emrich, H. M., & Dillo, W. (2009). Understanding why patients with schizophrenia do not perceive the hollow-mask illusion using dynamic causal modelling. *NeuroImage*, 46(4), 1180–1186.

[^28]: Feldman, H., & Friston, K. J. (2010). Attention, uncertainty, and free-energy. *Frontiers in Human Neuroscience*, 4, 215.

[^29]: Desimone, R., & Duncan, J. (1995). Neural mechanisms of selective visual attention. *Annual Review of Neuroscience*, 18, 193–222.

[^30]: Fries, P., Reynolds, J. H., Rorie, A. E., & Desimone, R. (2001). Modulation of oscillatory neuronal synchronization by selective visual attention. *Science*, 291(5508), 1560–1563; Fries, P. (2015). Rhythms for cognition: Communication through coherence. *Neuron*, 88(1), 220–235.

[^31]: Hasselmo, M. E. (2006). The role of acetylcholine in learning and memory. *Current Opinion in Neurobiology*, 16(6), 710–715.

[^32]: Yu, A. J., & Dayan, P. (2005). Uncertainty, neuromodulation, and attention. *Neuron*, 46(4), 681–692.

[^33]: Simons, D. J., & Chabris, C. F. (1999). Gorillas in our midst: Sustained inattentional blindness for dynamic events. *Perception*, 28(9), 1059–1074.

[^34]: Rensink, R. A., O'Regan, J. K., & Clark, J. J. (1997). To see or not to see: The need for attention to perceive changes in scenes. *Psychological Science*, 8(5), 368–373.

[^35]: Ernst, M. O., & Banks, M. S. (2002). Humans integrate visual and haptic information in a statistically optimal fashion. *Nature*, 415, 429–433.

[^36]: Alais, D., & Burr, D. (2004). The ventriloquist effect results from near-optimal bimodal integration. *Current Biology*, 14(3), 257–262.

[^37]: McGurk, H., & MacDonald, J. (1976). Hearing lips and seeing voices. *Nature*, 264, 746–748.

[^38]: von Holst, E., & Mittelstaedt, H. (1950). Das Reafferenzprinzip: Wechselwirkungen zwischen Zentralnervensystem und Peripherie. *Naturwissenschaften*, 37(20), 464–476; Sperry, R. W. (1950). Neural basis of the spontaneous optokinetic response produced by visual inversion. *Journal of Comparative and Physiological Psychology*, 43(6), 482–489.

[^39]: Wolpert, D. M., Miall, R. C., & Kawato, M. (1998). Internal models in the cerebellum. *Trends in Cognitive Sciences*, 2(9), 338–347.

[^40]: Blakemore, S.-J., Wolpert, D. M., & Frith, C. D. (1998). Central cancellation of self-produced tickle sensation. *Nature Neuroscience*, 1(7), 635–640.

[^41]: Yarbus, A. L. (1967). *Eye Movements and Vision*. Plenum Press.

[^42]: Kleinfeld, D., Ahissar, E., & Diamond, M. E. (2006). Active sensation: Insights from the rodent vibrissa sensorimotor system. *Current Opinion in Neurobiology*, 16(4), 435–444; Rayner, K. (1998). Eye movements in reading and information processing: 20 years of research. *Psychological Bulletin*, 124(3), 372–422.

[^43]: Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.

[^44]: Johnson, M. H., Dziurawiec, S., Ellis, H., & Morton, J. (1991). Newborns' preferential tracking of face-like stimuli and its subsequent decline. *Cognition*, 40(1–2), 1–19; Hershberger, W. (1970). Attached-shadow orientation perceived as depth by chickens reared in an environment illuminated from below. *Journal of Comparative and Physiological Psychology*, 73(3), 407–411.

[^45]: Wiesel, T. N., & Hubel, D. H. (1963). Single-cell responses in striate cortex of kittens deprived of vision in one eye. *Journal of Neurophysiology*, 26(6), 1003–1017; Hubel, D. H., & Wiesel, T. N. (1970). The period of susceptibility to the physiological effects of unilateral eye closure in kittens. *Journal of Physiology*, 206(2), 419–436.

[^46]: Blakemore, C., & Cooper, G. F. (1970). Development of the brain depends on the visual environment. *Nature*, 228, 477–478.

[^47]: Hensch, T. K. (2005). Critical period plasticity in local cortical circuits. *Nature Reviews Neuroscience*, 6(11), 877–888.

[^48]: Olshausen, B. A., & Field, D. J. (1996). Emergence of simple-cell receptive field properties by learning a sparse code for natural images. *Nature*, 381, 607–609.

[^49]: Lewicki, M. S. (2002). Efficient coding of natural sounds. *Nature Neuroscience*, 5(4), 356–363.

[^50]: Martin, T. A., Keating, J. G., Goodkin, H. P., Bastian, A. J., & Thach, W. T. (1996). Throwing while looking through prisms. I. Focal olivocerebellar lesions impair adaptation. *Brain*, 119(4), 1183–1198.

[^51]: Stratton, G. M. (1897). Vision without inversion of the retinal image. *Psychological Review*, 4(4), 341–360 and 4(5), 463–481; Kohler, I. (1962). Experiments with goggles. *Scientific American*, 206(5), 62–72; Linden, D. E. J., Kallenbach, U., Heinecke, A., Singer, W., & Goebel, R. (1999). The myth of upright vision: A psychophysical and functional imaging study of adaptation to inverting spectacles. *Perception*, 28(4), 469–481.

[^52]: Neitz, J., Carroll, J., Yamauchi, Y., Neitz, M., & Williams, D. R. (2002). Color perception is mediated by a plastic neural mechanism that is adjustable in adults. *Neuron*, 35(4), 783–792.

[^53]: Bonnet, C. (1760). *Essai analytique sur les facultés de l'âme*. Copenhagen: Philibert; ffytche, D. H., Howard, R. J., Brammer, M. J., David, A., Woodruff, P., & Williams, S. (1998). The anatomy of conscious vision: An fMRI study of visual hallucinations. *Nature Neuroscience*, 1(8), 738–742.

[^54]: Ramachandran, V. S., & Hirstein, W. (1998). The perception of phantom limbs: The D. O. Hebb lecture. *Brain*, 121(9), 1603–1630.

[^55]: Fletcher, P. C., & Frith, C. D. (2009). Perceiving is believing: A Bayesian approach to explaining the positive symptoms of schizophrenia. *Nature Reviews Neuroscience*, 10(1), 48–58; Sterzer, P., Adams, R. A., Fletcher, P., Frith, C., Lawrie, S. M., Muckli, L., Petrovic, P., Uhlhaas, P., Voss, M., & Corlett, P. R. (2018). The predictive coding account of psychosis. *Biological Psychiatry*, 84(9), 634–643.

[^56]: Pellicano, E., & Burr, D. (2012). When the world becomes 'too real': A Bayesian explanation of autistic perception. *Trends in Cognitive Sciences*, 16(10), 504–510; Lawson, R. P., Rees, G., & Friston, K. J. (2014). An aberrant precision account of autism. *Frontiers in Human Neuroscience*, 8, 302.

[^57]: Yamins, D. L. K., & DiCarlo, J. J. (2016). Using goal-driven deep learning models to understand sensory cortex. *Nature Neuroscience*, 19(3), 356–365.

[^58]: Geirhos, R., Rubisch, P., Michaelis, C., Bethge, M., Wichmann, F. A., & Brendel, W. (2019). ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness. *International Conference on Learning Representations (ICLR)*.

[^59]: Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow, I., & Fergus, R. (2014). Intriguing properties of neural networks. *International Conference on Learning Representations (ICLR)*; Goodfellow, I. J., Shlens, J., & Szegedy, C. (2015). Explaining and harnessing adversarial examples. *International Conference on Learning Representations (ICLR)*; Ilyas, A., Santurkar, S., Tsipras, D., Engstrom, L., Tran, B., & Madry, A. (2019). Adversarial examples are not bugs, they are features. *Advances in Neural Information Processing Systems*, 32; Elsayed, G. F., Shankar, S., Cheung, B., Papernot, N., Kurakin, A., Goodfellow, I., & Sohl-Dickstein, J. (2018). Adversarial examples that fool both computer vision and time-limited humans. *Advances in Neural Information Processing Systems*, 31.

[^60]: Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30.

[^61]: Dayan, P., Hinton, G. E., Neal, R. M., & Zemel, R. S. (1995). The Helmholtz machine. *Neural Computation*, 7(5), 889–904; Kingma, D. P., & Welling, M. (2014). Auto-encoding variational Bayes. *International Conference on Learning Representations (ICLR)*; Ho, J., Jain, A., & Abbeel, P. (2020). Denoising diffusion probabilistic models. *Advances in Neural Information Processing Systems*, 33.

[^62]: Whittington, J. C. R., & Bogacz, R. (2017). An approximation of the error backpropagation algorithm in a predictive coding network with local Hebbian synaptic plasticity. *Neural Computation*, 29(5), 1229–1262; Millidge, B., Seth, A., & Buckley, C. L. (2022). Predictive coding: A theoretical and experimental review. *arXiv*, 2107.12979.

[^63]: Bajcsy, R., Aloimonos, Y., & Tsotsos, J. K. (2018). Revisiting active perception. *Autonomous Robots*, 42(2), 177–196.
