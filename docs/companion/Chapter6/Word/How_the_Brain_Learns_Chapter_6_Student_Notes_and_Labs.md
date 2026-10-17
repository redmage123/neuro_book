---
title: "Chapter 6 Student Notes and Labs"
subtitle: "Perception as Inference: How the Brain Sees What It Expects"
---

# Student Notes

## What this chapter is for

Chapter 1 said in one sentence that perception is an active process of inference shaped by prior experience. Chapter 6 spends a whole chapter earning that sentence. It uses the circuits of Chapter 4, the neuromodulators of Chapter 3, and the learned structure of Chapter 5 to explain why you see a stable world when the eye delivers a jittering, ambiguous, hole-ridden sample of it.

If you come from software or machine learning, the chapter is designed to correct three instincts:
1) treating perception as decoding, as if the image contained the answer and the brain only had to read it out,
2) treating illusions and hallucinations as bugs, and
3) treating attention as a spotlight that selects, rather than a gain that weights evidence by its reliability.

Your goal is to be able to explain, in plain language, why the inverse problem forces the brain to use priors, how a prior and a likelihood combine, what predictive coding says travels up and down the cortical hierarchy and which observations (expectation suppression, omission responses, and the mismatch negativity) test it, how sensory prediction error differs from Chapter 3's reward prediction error, why attention is precision, how two senses are combined, why the world does not jump when your eyes do, and where priors come from.

## The problem perception solves

The retinal image is a two-dimensional projection and is ambiguous: many arrangements of the world produce the same image (Figure 6.1). This is an inverse problem and it is ill-posed. The evidence does not determine the answer, yet we perceive an answer, so something else supplies the rest. Helmholtz (1867) called it unconscious inference: perceive the state of the world that would most probably have produced these sensations under ordinary conditions. It is not reasoning and cannot be overruled by reasoning, which is why illusions survive explanation.

## The senses deliver evidence, not pictures

- About 92 million rods and 4.6 million cones (Curcio et al. 1990), but only about 1 million ganglion-cell axons per eye: about 97-to-1, roughly a hundred-to-one compression before the brain. What is kept: contrast, change, edges (Chapter 4).
- Information rate of the optic nerve: on the order of 10 megabits per second.
- High acuity only in the fovea, whose region of highest acuity covers one to two degrees (a thumbnail at arm's length). The blind spot is about 6 degrees across, 15 degrees to the side, and you have never seen it.
- The eye jumps about three times a second (saccades); vision is suppressed during each jump.
- The stable scene is not an input. It is an output.

## Bayes in one paragraph

Prior: a distribution over possible states of the world encoding what is usually true. Likelihood: for each possible state, how probable are the sensations just received. Posterior is proportional to prior times likelihood, and it leans toward whichever is more precise (Figure 6.2). Sharp evidence: the posterior follows the senses. Noisy evidence: the posterior stays near the prior. Neither extreme is a failure.
Priors are learned structure: the statistics of a lifetime of input, written into synaptic weights by the plasticity of Chapter 5. Example: light comes from above, so a disc shaded lighter on top is a bump and the same disc upside down is a dent (Figure 6.3). Chicks reared under light from below still assume light from above, so the prior is partly in place before experience, but it is not fixed: the adult prior is above and slightly left, and Adams, Graf, and Ernst (2004) shifted it by having observers touch shaded discs whose felt shape agreed with a rotated light source. The shift transferred to an untrained lightness task. A prior is in the weights, and the weights can be rewritten.

## The hierarchy

Retina to LGN (thalamus) to V1 to V2 to V4 to IT along the ventral stream (Figure 6.4). At each stage receptive fields grow (a fraction of a degree in V1, most of the visual field in IT) and preferences become more abstract (oriented edge, contour, shape part, object or face), building invariance to position, size, and lighting. The feedforward sweep reaches IT in about 100 ms; humans categorize animal/non-animal in about 150 ms. Convolutional networks were modeled on this sweep (Fukushima's neocognitron, 1980) and the best predict IT responses.
But feedback connections are at least as numerous as feedforward ones. Markov and colleagues (2014) counted more feedback than feedforward pathways in the macaque, but a pathway count is not an axon or synapse count, and "outnumber" is not established at every stage. At the thalamus it plainly holds: the LGN gets only about a tenth of its synapses from the retina. The visual system is a loop whose downward half is at least as large as its upward half.

## Predictive coding

Each level holds a hypothesis about the level below and sends it down as a prediction. The lower level sends up only the difference: the prediction error. The upper level revises, and the loop repeats until error is small (Figure 6.5A). What ascends is not the image but its surprise.
This sensory prediction error is not Chapter 3's reward prediction error. That one is a single number about value, broadcast by a large population of dopamine neurons; this one is a high-dimensional pattern of errors about content, one per feature per level, passed between cortical layers within the sensory hierarchy, with no reward in it.
The predictions, all observed:
- Expected stimuli evoke less activity. Repetition suppression (Figure 6.5B) is consistent with this but is weak evidence on its own, since fatigue or sharpened tuning would also produce it. The decisive test holds repetition fixed and varies expectation: Summerfield and colleagues (2008) found that the same repeated face suppressed the fusiform face area more when the repeat was expected. This expectation suppression has since been separated in time from repetition suppression in human auditory cortex.
- An omitted expected stimulus evokes activity: a prediction with nothing to cancel it.
- The mismatch negativity, 100-200 ms after a deviant tone, present (attenuated) in sleeping adults and in newborns; it reflects a violated prediction, not the tone itself.
- End-stopping in V1 (a line that stops inside the receptive field excites more than one that continues) fell out of the first predictive-coding model of V1 (1999) without being designed in.
Proposed mapping onto the Chapter 4 microcircuit: error units in superficial layers (project forward, gamma), prediction units in deep layers (project backward, alpha/beta). A model, not settled, but testable.

## Illusions are correct answers

An illusion is what inference looks like when the prior is right about the world and wrong about the picture. Each illusion is a probe for a prior.

| Illusion | What is seen | The prior it reveals |
|---|---|---|
| Checker-shadow (Figure 6.6) | identical grays look different | surfaces in shadow reflect less light; discount the illuminant |
| Light-from-above discs (Figure 6.3) | bumps become dents when rotated | light comes from above |
| Kanizsa triangle (Figure 6.7A) | a white triangle with no drawn edges | aligned gaps are caused by an occluding surface |
| Müller-Lyer (Figure 6.7B) | equal lines look unequal | fins are corners at different depths (one account; debated) |
| Hollow mask | a concave mask looks convex | faces are convex; strong enough to beat stereo at a distance |
| Ventriloquism | the voice comes from the dummy | vision localizes better than hearing, so it gets the weight |
| McGurk effect | a third syllable is heard | lip movements are reliable evidence about speech |

Neurons in V2 respond to Kanizsa's illusory contours as if they were real.

## Attention as precision

The brain must estimate how reliable each signal is and weight it accordingly. The proposal: attention is the gain on prediction errors, raised where evidence is expected to be reliable. This unifies three findings: attention raises responses of neurons covering the attended location and lowers neighbors (biased competition, built on Chapter 4's lateral inhibition); attention raises gamma synchrony, which lets spikes arrive in the receptive phase of the next area (Chapter 4's oscillatory gating); attention makes attended evidence count more in the posterior.
Chemistry (Chapter 3): acetylcholine raises the gain of feedforward sensory input relative to feedback, so a cholinergic cortex trusts its senses more; one account assigns acetylcholine to expected uncertainty and norepinephrine to unexpected uncertainty (the world changed; lower the precision of every prediction now).
Cost: what is not attended is barely seen. The gorilla in the basketball video; change blindness across a blink or a cut.

## Combining the senses

If the brain weights by precision, the estimate from two senses should lie between them, closer to the more reliable one, and be narrower than either. Ernst and Banks (2002): vision plus touch judging a bar's width, with visual noise varied. Observed weights matched the computed optimum at every noise level (Figure 6.8). The senses are pooled sources of evidence, not separate channels to a viewer.
This is the sense in which the book says the brain optimizes: there is no single global objective trained by gradient descent, but circuits such as this one (and the dopamine error of Chapter 3) behave as if minimizing a well-defined local cost, here the variance of the estimate.

## Perception is active

Two consequences of a brain that moves its sensors:
- It must tell self-caused sensation from world-caused sensation. A copy of every motor command (efference copy) goes to a forward model, which predicts the sensory consequence; the prediction is subtracted (Figure 6.9). Eye moves by command: world stays still. Eye moved by pressing the eyelid: no prediction, the world lurches. The cerebellum (Chapter 4) is a principal site. Same mechanism: you cannot tickle yourself.
- Movement is a tool of inference. A saccade is a decision about where evidence is needed; whisking, sniffing, and reading fixations all sample where uncertainty is greatest. Hypothesis chooses where to look; what is seen revises the hypothesis.

## Learning the priors

Some priors are present at or near birth (newborns orient to faces; chicks reared under light from below still assume light from above), but present at birth is not fixed for life, as the Adams experiment shows. Most of sensory cortex is learned from input statistics, and the learning is slow, gated, and windowed, as Chapter 5 predicts.
- Critical period (Hubel and Wiesel): one eye closed for weeks early in life permanently loses its cortical representation; the same closure in an adult does nothing. Kittens raised among vertical stripes had almost no horizontal-edge neurons. The window is controlled by inhibitory maturation and neuromodulators.
- Olshausen and Field (1996): a model trained only to represent natural image patches sparsely learned localized, oriented, band-pass filters (Figure 6.10), the receptive fields Hubel and Wiesel found in V1. Edges are what the world contains. The receptive fields of sensory cortex are the priors of the natural world made into tissue.
- Adult recalibration continues: prism goggles (reaching errors vanish in minutes); inverting goggles (motor adaptation in six to ten days, but whether the world ever looks upright again is disputed; a controlled 1999 study found no perceptual re-inversion); a colored filter worn a few hours a day for several days shifts perceived pure yellow for a week or two afterward (Neitz et al. 2002). Slow at the core, fast at the periphery, like Chapter 5's two clocks.

## When inference goes wrong

- Evidence removed: priors run unopposed. Charles Bonnet syndrome (vivid hallucinations after late-life vision loss, with insight); phantom limbs.
- Precision misweighted: hollow-mask illusion is weaker in schizophrenia (weaker priors at one level) while hallucinations and delusions can be read as priors too strong, or noise in the error channel read as signal, at another. One account of autistic perception proposes sensory precision too high relative to priors. All hypotheses, not settled findings; the value of the framework is a vocabulary in which disorders of perception are disorders of weighting, set by measurable mechanisms.

## Implications for artificial intelligence

1) The feedforward sweep is reproduced: deep convolutional networks predict IT responses. Gradient descent and evolution found a similar solution to the same statistical problem. The match is partial: networks lean on texture where humans lean on shape, and diverge from IT outside their training distribution.
2) The loops are not: no feedback, no prediction, no error signal at inference time. Adversarial examples are not "evidence without priors": a trained classifier is all priors, stored in its weights, but has no way to check them. The vulnerability is better explained by near-linear behavior in high dimensions and reliance on features invisible to us (briefly glimpsed, such images can fool humans too). A brain would compare its prediction with the input and look again.
3) Precision is missing: nothing estimates input reliability per channel, and nothing plays norepinephrine's role of saying "distrust the model now."
4) Generative models are the right direction: a system that can generate its data has a prior and a likelihood. Whether predictive coding can replace backpropagation as a learning rule is open; the strongest results show predictive-coding networks can approximate backpropagation, not surpass it.
5) Perception should be active: sampling where uncertainty is greatest is an easier problem; an agent without a forward model cannot tell what it did from what the world did.

## Practical summary

- The retinal image does not determine the world; perception is inference from evidence plus priors.
- Posterior is proportional to prior times likelihood; weights are set by relative precision.
- Priors are learned structure (Chapter 5), stored in synaptic weights; some are present at birth, and even those (light from above) can be retrained in adults.
- The cortical hierarchy sends predictions down and errors up; expected input is quiet, surprise is loud. Expectation suppression, not repetition suppression alone, is the decisive evidence.
- Sensory prediction error (high-dimensional, about content) is a different signal from Chapter 3's reward prediction error (a scalar about value).
- Illusions are correct inferences from the wrong picture; each reveals a prior.
- Attention is precision: gain on errors, implemented by biased competition, gamma synchrony, and acetylcholine.
- Senses are combined by precision weighting, near-optimally.
- Efference copy and forward models cancel the sensory consequences of one's own actions.
- Critical periods window the learning of priors; adult recalibration continues more slowly.
- Hallucinations and some disorders are inference with the weights wrong.

# Labs

## Lab Notes: how to succeed in these labs

These labs make inference concrete with pencil, paper, and short recurrences. Each isolates a single idea: combining a prior with evidence, weighting two senses, prediction error over a sequence, discrete hypotheses against a strong prior, cancelling self-caused sensation, and learning a prior that must track a changing world. The arithmetic is light; the point is to watch the rule behave.

General rules:
1) Write every intermediate value.
2) Draw the curves or the circuit before computing.
3) End with an interpretation: what would change if a parameter changed, and what does the biology gain or lose?

### What to hand in for every lab

- A table of values.
- A diagram or sketch where requested (a photo of a hand drawing is fine).
- A short interpretation (6-12 sentences).

## Lab 6.1 - Prior Meets Evidence (Bayes by hand)

### Purpose

To reproduce Figure 6.2 numerically: how a prior and a likelihood combine, and why the result follows whichever is more precise.

### Given model

Both prior and likelihood are bell curves. The prior has mean m_p and standard deviation s_p; the evidence has mean m_e and standard deviation s_e. Precision is 1/s². Then:
posterior mean = (m_p / s_p² + m_e / s_e²) / (1 / s_p² + 1 / s_e²)
posterior standard deviation = square root of 1 / (1 / s_p² + 1 / s_e²)
weight on the evidence = (1 / s_e²) / (1 / s_p² + 1 / s_e²)
Scenario: estimating the direction of a sound. The prior says sounds usually come from straight ahead: m_p = 0 degrees, s_p = 10 degrees. The ears report m_e = 20 degrees.

### Procedure

1) Precise evidence: s_e = 5. Compute the posterior mean, posterior standard deviation, and weight on the evidence. (Check: 16 degrees, 4.47 degrees, weight 0.80.)
2) Noisy evidence: s_e = 15. Recompute. (Check: 6.15 degrees, weight 0.31.)
3) Equal precision: s_e = 10. Recompute. (Check: 10 degrees, exactly halfway.)
4) Strong prior: put s_p = 3 with s_e = 5. (Check: 5.29 degrees.) The senses say 20 and the brain reports 5. Is this a malfunction? Under what conditions would a prior this sharp be the right thing to have?
5) How precise would the evidence have to be for the posterior to reach 18 degrees with the original prior (s_p = 10)? Solve for s_e. (Check: 3.33 degrees.)
6) Note that in every case the posterior standard deviation is smaller than both inputs. Explain in one sentence why combining two uncertain estimates produces a more certain one.
7) Write 6-10 sentences: why is neither "always trust the senses" nor "always trust the prior" a good policy, and what would an organism with each policy do wrong?

## Lab 6.2 - Two Senses, One Estimate (precision weighting)

### Purpose

To reproduce the Ernst and Banks result of Figure 6.8: the brain combines vision and touch by their precisions, and shifts the weight when one is degraded.

### Given model

Vision reports a bar width of 52 mm with standard deviation s_v. Touch reports 58 mm with standard deviation s_h = 4 mm. Use the formulas from Lab 6.1 with the two senses in place of prior and evidence.

### Procedure

1) Clear view: s_v = 2 mm. Compute the weight on vision, the combined estimate, and the combined standard deviation. (Check: 0.80, 53.2 mm, 1.79 mm.)
2) Blurred: s_v = 8 mm. Recompute. (Check: 0.20, 56.8 mm, 3.58 mm.)
3) Find the value of s_v at which the two senses get equal weight. (Check: 4 mm, the same as touch.)
4) Plot, by hand, the weight on vision as a function of s_v for s_v = 1, 2, 4, 8, 16. Describe the shape.
5) Now suppose the room goes dark so that vision reports nothing usable (s_v very large). What does the formula do? What does the organism do?
6) Write 6-10 sentences: Ernst and Banks found that people's weights matched the optimum at every noise level. What would the brain need to represent, and update trial by trial, for that to be possible? Relate it to the chapter's claim that attention is precision.

## Lab 6.3 - Surprise on a Chain (predictive coding over time)

### Purpose

To reproduce Figure 6.5B: a single predicting unit facing a repeated input with one oddball, showing repetition suppression and the mismatch response.

### Given model

One level holds a prediction p, starting at 0. On each step a stimulus x arrives, the error is e = x − p, the error is transmitted, and the prediction is updated: p ← p + η e.
Sequence: x = 1.0 for six steps (tone A), then x = 0.3 (tone B, the oddball), then x = 1.0 for four more steps.

### Procedure

1) With η = 0.5, tabulate p before each step and the error e for all eleven steps. (Check: errors for the six A's are 1.0, 0.5, 0.25, 0.125, 0.062, 0.031; the oddball error is −0.684; the first A after it gives 0.358.)
2) Mark on your table which errors a physiologist would call repetition suppression and which the mismatch response. Note that the oddball's error is larger in magnitude than the oddball's own value. Explain why. (In this model repetition and expectation always coincide, so it cannot distinguish prediction from fatigue; say what experiment would, as the chapter's expectation-suppression study does.)
3) Repeat with η = 0.1. (Check: after six A's, p = 0.469; the oddball error is −0.169.) The slow learner shows a smaller mismatch. Why? What has it failed to do?
4) Now remove the oddball and instead omit the seventh stimulus entirely (treat it as x = 0). With η = 0.5, what is the error at that step? This is the omission response of the chapter. What does the circuit "see" when nothing arrives?
5) Suppose the error unit's output is multiplied by a gain g before it is transmitted upward (attention as precision). With g = 2 on the oddball step only, what is transmitted? With g = 0.25? Which one corresponds to the gorilla going unnoticed?
6) Write 6-10 sentences: why is it efficient to transmit the error rather than the stimulus, what information is lost if the higher level never sees the stimulus itself, and how does η relate to the sliding threshold and consolidation rates of Chapter 5?

### Optional code extension (Python, about 20 lines)

Implement the recurrence and plot |e| against step for η = 0.1, 0.3, 0.5, 0.9. Then build a two-level chain: level 2 predicts level 1's prediction with its own η, and plot both error signals. Observe which level responds to the oddball and which to the longer-run change when you switch permanently from A to B at step 7.

## Lab 6.4 - The Hollow Mask (discrete hypotheses against a strong prior)

### Purpose

To work the hollow-mask illusion as a two-hypothesis Bayesian decision, and to see why it survives at a distance, breaks up close, and weakens when the prior weakens.

### Given model

Two hypotheses: the face is convex (normal) or hollow. Work in odds.
Prior odds convex:hollow = 99:1 (almost every face ever seen was convex).
Stereo and shading evidence favor "hollow" by a likelihood ratio L that depends on viewing distance, because stereo precision falls with distance: at 2 m, L = 5 (the evidence is 5 times more likely under "hollow"); at 1 m, L = 50; at 0.5 m, L = 500.
Posterior odds convex:hollow = prior odds / L. Probability of convex = odds / (1 + odds).

### Procedure

1) Compute posterior odds and the probability of "convex" at 2 m, 1 m, and 0.5 m. (Check: 19.8:1 and 0.952 at 2 m; 1.98:1 and 0.664 at 1 m; 0.198:1 and 0.165 at 0.5 m.) At which distance does the percept flip?
2) Now take a weaker face prior, 9:1, as one account proposes for schizophrenia. Recompute the three distances. (Check: 0.643, 0.153, 0.018.) At which distance does the percept flip now? Compare with step 1 and relate it to the clinical finding in the chapter.
3) Suppose the mask is rotating, which adds motion-parallax evidence for "hollow" with its own likelihood ratio of 3, independent of stereo. Likelihood ratios from independent cues multiply. Recompute the 2 m case with the 99:1 prior. Does it flip?
4) Design the evidence needed to flip a 999:1 prior at 2 m. State the required total likelihood ratio and name two independent cues that could supply it.
5) Write 6-10 sentences: why is a prior of 99:1 for convex faces the correct prior to have, what does the organism gain from it, and what does the illusion cost? Then explain why the strength of an illusion can be used as a measurement of a prior.

## Lab 6.5 - Who Moved, Me or the World? (efference copy)

### Purpose

To work the comparison in Figure 6.9 for several cases, including the two that Helmholtz used to argue for the efference copy.

### Given model

Perceived motion of the world = actual retinal slip − predicted retinal slip.
A commanded eye movement of d degrees to the right produces a predicted slip of d degrees to the left (write leftward slip as positive).
The forward model predicts slip only from commands, never from external pushes.

### Procedure

1) Make a table with columns: case, command, actual eye movement, object movement, actual slip, predicted slip, perceived motion. Fill it for:
a) command 10 degrees right, eye moves 10 degrees right, object still;
b) no command, eyelid pressed so the eye turns 5 degrees right;
c) command 10 degrees right, but the eye muscle is paralyzed and the eye does not move (Helmholtz's patient);
d) command 10 degrees right, eye moves 10 degrees right, and the object moves 3 degrees right at the same time.
(Check: a) 0; b) 5 degrees of apparent world motion; c) −10, the world appears to jump in the direction of the intended movement; d) the object is seen to move 3 degrees right.)
2) In case c, the retina reported nothing at all, and yet motion was perceived. Explain, in one sentence, what that tells you about where perception happens.
3) Tickling: let the predicted touch intensity be 1.0 when you move your own hand and 0 when someone else does; actual intensity is 1.0 in both cases. Compute what is felt. Now suppose a 200 ms delay is inserted between your command and the touch, so that the forward model's prediction arrives at the wrong time and only 0.4 of it is subtracted. What is felt? (Experiments show that self-tickling becomes more ticklish as the delay grows.)
4) The forward model is learned by the cerebellum (Chapter 4). Describe, using the climbing-fiber error signal of that chapter, how the model would be corrected if you began wearing glasses that magnified the visual scene by 20 percent, so that a 10 degree eye movement produced a 12 degree slip.
5) Write 6-10 sentences: why must any agent that moves its own sensors have an efference copy, what goes wrong in an agent without one, and how does this relate to the chapter's claim that perception and action are one loop?

## Lab 6.6 - Learning a Prior That Must Track the World

### Purpose

To see how a prior is learned from a sequence of observations, why a fixed learning rate is a compromise, and what a norepinephrine-like "unexpected uncertainty" signal buys.

### Given model

The prior's mean m is updated after each observation x by m ← m + k (x − m), with learning rate k.
Observations, in order: 10, 12, 11, 9, 10 (the world is near 10), then 20, 21, 19, 20, 20 (the world has shifted to near 20).
Start with m = 10.

### Procedure

1) With k = 0.2, tabulate m after each of the ten observations. (Check: 10.17 after the fifth, 12.14 after the sixth, 16.75 after the tenth.)
2) With k = 0.05, repeat. (Check: 12.32 after the tenth.) Which learner is more stable during the first five steps? Which has adapted better by the tenth? State the trade-off in one sentence.
3) Now add a surprise rule: if the observation differs from m by more than 6, use k = 0.8 for that step only, then return to k = 0.2. Repeat. (Check: 18.03 after the sixth observation, 19.17 after the tenth.) Which neuromodulator of Chapter 3 does this rule imitate, and what is the "6" in the rule an estimate of?
4) The surprise rule has a cost. Insert a single outlier of 30 into the first five observations (make the third observation 30 instead of 11) and run both the plain k = 0.2 learner and the surprise learner. Which one is thrown further off, and for how long?
5) Propose a rule that uses a running estimate of the spread of recent observations to decide whether a deviation counts as surprise. How does this relate to precision?
6) Write 8-12 sentences: relate the learning rate k to the plasticity mechanisms of Chapter 5 (which mechanism sets how fast a cortical prior changes, and why is it slow by default), explain why a system with two learning rates (Chapter 5's two clocks) would handle this sequence better than either single learner, and explain why a critical period can be described as a time when k is high and its closing as k being turned down.

## Lab 6.7 - From Photons to Percept (concept map)

### Purpose

To integrate the chapter on one page: the chain from an ambiguous image to a stable percept, with every prior, gain, and loop in place.

### Procedure

1) Draw an eye and the retinal image. Beside it, draw three different world states that could have produced it (as in Figure 6.1). Label this "the inverse problem."
2) Draw the ventral hierarchy as a column of boxes (retina, LGN, V1, V2, V4, IT). Give each box a receptive field circle of increasing size and a note on what it prefers. Draw feedforward arrows up and feedback arrows down, the feedback at least as thick. Mark the 100 ms sweep.
3) Inside two adjacent boxes, draw the prediction units (deep layers) and error units (superficial layers), the prediction arrow down, the subtraction, and the error arrow up. Label the rhythms (gamma up, alpha/beta down).
4) Add a "prior" label to the feedback arrows and connect it with a dashed line to a synapse labeled "Chapter 5: learned weights," with a note on the critical period.
5) Add a gain knob on the error units labeled "attention = precision," and draw two neuromodulatory inputs to it from Chapter 3: acetylcholine (trust the senses) and norepinephrine (the world changed).
6) Draw a second sense (touch) feeding the same hierarchy and show the two estimates combining with weights.
7) Draw a motor command leaving the top of the hierarchy, its efference copy going to a forward model (cerebellum), and the predicted sensation being subtracted at the input.
8) Draw a saccade arrow from the percept back to the eye, labeled "choose the next sample."
9) Write a 10-14 sentence caption that follows one glance at a scene from photons to percept, naming the mechanism at each step, including one illusion that the same mechanism would produce and one clinical condition that would result if one of the gains were set wrong.
