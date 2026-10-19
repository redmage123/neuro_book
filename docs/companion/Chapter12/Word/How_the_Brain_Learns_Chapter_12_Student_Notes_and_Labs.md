---
title: "Chapter 12 Student Notes and Labs"
subtitle: "The Brain as a Predictive, Adaptive System: Is There One Principle Beneath the Mechanisms?"
---

# Student Notes

## What this chapter is for

The earlier chapters met prediction in dopamine neurons, the hippocampus, sensory cortex, the regulation of the body, decisions, and movement. Chapter 12 asks whether prediction is one principle beneath all these mechanisms, and answers: it is the brain's most general strategy, with adaptation as its counterpart, but it is carried out by many mechanisms, and the claim that one equation captures it is weakly supported.

If you come from software or machine learning, the chapter is designed to correct three instincts:
1) treating "prediction error" as one signal, when the brain uses several, with different cells, speeds, and meanings, that share a form rather than a mechanism,
2) treating the learning rate as a hyperparameter set in advance, when the brain sets it moment by moment from its uncertainty, and
3) treating a unifying framework as a theory, when a framework that can describe any behavior must be judged by the specific, testable hypotheses built under it.

Your goal is to be able to explain the three reasons to predict, how neurons match and track the statistics of their input, the evidence for prediction in the hippocampus, cortex, and language, why the best learning rate depends on uncertainty, why adaptation runs on many timescales, what the free-energy principle claims and the main objections to it, and what prediction leaves unexplained.

## A model in the head

- Craik (1943): an organism carrying a "small-scale model" of the world and of its own actions can try alternatives and react to situations before they arise. Craik died in 1945, aged 31.
- Figure 12.1 maps prediction across Chapters 3 to 11: what each system predicts, its error signal, and what learns.
- Thesis: prediction is a strategy implemented by many mechanisms; the evidence for one equation is weak.

## Why predict?

- Delay: V1 responds about 66 ms after a stimulus (Schmolesky 1998); the flash-lag effect (Nijhawan 1994); batsmen's eyes jump to where the ball will bounce, earliest in the best (Land and McLeod 2000); parietal neurons update their receptive fields before an eye movement (Duhamel 1992).
- Economy: the retina subtracts the prediction from neighbors and sends the error (Srinivasan, Laughlin, and Dubs 1982) (Figure 12.2), 17 years before predictive coding in cortex (Rao and Ballard 1999).
- Regulation: thirst neurons fall silent at drinking before the blood changes (Zimmerman 2016); predictive regulation (Sterling 2012; Chapter 7).

## Matching the world's statistics

- The fly's contrast-response curve matches the cumulative distribution of natural contrasts, using every response level equally (Laughlin 1981; Barlow 1961) (Figure 12.3).
- H1 rescales to the variance of motion (Brenner 2000); information recovers within about 100 ms while firing rate adjusts over a minute (Fairhall 2001); adaptation often follows a power law (Wark 2007).
- The waterfall illusion (Addams 1834): a recalibrated expectation of motion.
- Retinal groups carry nearly the maximum possible information about the future (Palmer 2015); efficient and predictive coding in one framework (Chalk 2018).

## Prediction at every level

- Place fields grow backward with one-way running (Mehta 1997); the successor representation, a predictive map (Stachenfeld 2017) (Figure 12.4); humans adjust to changed rewards more easily than changed sequences (Momennejad 2017); hidden sequence structure in hippocampus and entorhinal cortex (Garvert 2017).
- Visuomotor mismatch responses in mouse V1 (Keller 2012) develop only with coupled experience (Attinger 2017).
- The N400 (Kutas and Hillyard 1980) tracks expectation (Kutas and Federmeier 2011); pre-activation of specific words is contested (Nieuwland 2018).

## Many errors, one form

- Errors differ (dopamine, sensory, climbing fiber) but share a form: change in proportion to the mismatch (the delta rule).
- The learning rate should depend on uncertainty (Kalman 1960; Dayan 2000). People raise it after change-points (Nassar 2010); the helicopter task (McGuire 2014); pupil measures predict it (Nassar 2012) (Figure 12.5).
- Acetylcholine and norepinephrine as expected and unexpected uncertainty (Yu and Dayan 2005); a hierarchy that learns volatility (Mathys 2011).
- Bayesian "just-so stories" (Bowers and Davis 2012) and the reply (Griffiths 2012): "approximately optimal" describes, it does not guarantee.

## When the learning rate goes wrong

- Conditioned hallucinations: voice-hearers weight priors more (Powers 2017).
- Autistic adults overestimate volatility (Lawson 2017).
- Small studies, no causal claim; but a measurable parameter for each person.

## Adaptation on every timescale

- Sea legs and their aftereffect ashore (Stoffregen 2013).
- From milliseconds to evolution (Figure 12.6): sensory adaptation, dark adaptation (Lamb and Pugh 2004), motor adaptation, synaptic scaling (Turrigiano 1998), critical periods (Hensch 2005).
- Many timescales as inference about disturbances of different durations (Kording 2007).
- Priors revised: the slow-speed prior (Snowden 1998; Pretto 2012; Stocker and Simoncelli 2006; Sotiropoulos 2011); chicks prefer biological motion without experience (Vallortigara 2005).

## One principle? The free-energy principle

- Systems that persist minimize variational free energy, a computable bound on surprise, by perceiving and learning or by acting (Friston 2006, 2010) (Figure 12.7); predictive processing philosophy (Clark 2013; Hohwy 2013).
- Dark-room problem and reply (Friston 2012): goals become expectations.
- Unfalsifiable as a principle (Friston 2018; Andrews 2021; Gershman 2019; Bruineberg 2022).
- Process theories: Bayes and predictive coding separable (Aitchison and Lengyel 2017); evidence mixed (Walsh 2020); global oddballs mainly in higher areas (Westerberg 2025 preprint).
- Direct tests: cultured neurons separate sources as predicted (Isomura 2023), also predicted by Hebbian rules; DishBrain Pong (Kagan 2022) and the critique (Balci 2023).

## What prediction leaves out

- What to want: value, anchored to a body (Chapter 7).
- Why to explore: infants explore objects that broke their expectations (Stahl and Feigenson 2015); epistemic value in active inference (Friston 2015), questioned (Millidge 2021).
- Control before prediction (Cisek 2019).
- Why the brain is built as it is: the subject of Chapter 13.

## Implications for artificial intelligence

- Language models are predictors, but mostly of text they did not produce; world models and prediction in representation space (LeCun 2022).
- Learning rates set by schedule; per-weight learned rates (Sutton 1992) not used at scale.
- Two timescales in deployed models, nothing in between.
- One loss versus many local errors.

## Practical summary

- Predict, compare, and revise, with a confidence that matches the world's reliability.
- Different error signals, one form.
- The best learning rate rises with surprise and falls with confirmation.
- Adaptation runs on every timescale; slow priors set fast learning's starting point.
- The free-energy principle is a framework; judge the hypotheses built under it.

# Labs

## Lab Notes: how to succeed in these labs

These labs turn the chapter's argument into short calculations: how much a prediction from neighbors saves, how a response curve should be matched to the statistics of its input, how a predictive map is built, why the best learning rate changes, how far the world moves during the brain's delays, and what "surprise" means in the free-energy account. Each isolates one idea. The arithmetic is light; the point is to see where the numbers come from and how much they depend on assumptions.

General rules:
1) Write every intermediate value, rounded to two decimal places unless told otherwise.
2) State every assumption you add, and say which way it would move the answer.
3) End with an interpretation: what does the calculation show, and what does it leave out?

### What to hand in for every lab

- A table of values.
- A diagram or sketch where requested (a photo of a hand drawing is fine).
- A short interpretation (6-12 sentences).

## Lab 12.1 - Predicting From the Neighbors

### Purpose

To reproduce, by hand, the saving of Figure 12.2: how much smaller a signal becomes when each point's predictable part is subtracted.

### Given data

Intensities along a row of ten photoreceptors: 10, 11, 12, 12, 13, 30, 31, 31, 30, 29.
For each of the eight inner points (the 2nd to the 9th), the prediction is the average of its two neighbors, and the error is the intensity minus the prediction.

### Procedure

1) Compute the eight predictions and errors. (Check: predictions 11.0, 11.5, 12.5, 21.0, 22.0, 30.5, 30.5, 30.0; errors 0, 0.5, −0.5, −8, 8, 0.5, 0.5, 0.)
2) Compute the variance of the eight inner intensities and of the eight errors (divide by 8). What is the ratio? (Check: 85.94; 16.11; about 5.3.)
3) Where are the large errors? What feature of the scene do they mark? Relate this to Chapter 6's account of what ascends the cortical hierarchy.
4) Suppose every response is corrupted by noise of the same size. Explain why sending the errors rather than the intensities lets fine differences, such as 12 versus 13, survive the noise.
5) The retina's surround also uses the recent past of each point. Give an example of a scene in which a temporal prediction would remove much more than a spatial one.
6) Write 6-10 sentences: what does the receiver need to know to reconstruct the original intensities from the errors, and what is lost if it gets that wrong?

## Lab 12.2 - Matching a Response to the World

### Purpose

To see why a response curve shaped like the cumulative distribution of the input carries the most information, as in Laughlin's fly (Figure 12.3).

### Given data

Contrasts fall into five bins, from most negative to most positive, with probabilities 0.05, 0.20, 0.50, 0.20, 0.05.
A neuron has only three distinguishable response levels. Information carried = entropy of the response levels, H = −Σ p log2 p.

### Procedure

1) Compute the cumulative distribution across the bins. (Check: 0.05, 0.25, 0.75, 0.95, 1.00.)
2) Design A, "linear": the three levels divide the contrast range into equal parts, so bin 1 gives level 1, bins 2 to 4 give level 2, and bin 5 gives level 3. Compute the probability of each level and H. (Check: 0.05, 0.90, 0.05; H ≈ 0.57 bits.)
3) Design B, "matched": bins 1 and 2 give level 1, bin 3 gives level 2, bins 4 and 5 give level 3. Compute H. (Check: 0.25, 0.50, 0.25; H = 1.50 bits.)
4) What is the most a three-level response can carry? (Check: log2 3 ≈ 1.58 bits.) Why can no design reach it with these bins?
5) The fly's world changes: in dim light contrasts are smaller. Describe how the matched design should change, and relate it to Brenner and colleagues' rescaling in H1.
6) Write 6-10 sentences: what the matched design gives up (consider rare, large contrasts, which might matter most), and why a predator detector might use a different design.

## Lab 12.3 - A Predictive Map by Hand

### Purpose

To compute the successor representation of Figure 12.4 for a short track and see why place fields extend backward.

### Given values

A track has four positions, 1 to 4. The animal always moves one step to the right and the run ends at position 4. The successor representation M(s, s') is the expected discounted number of future visits to s' starting from s: M = I + γT + γ²T² + …, where T is the transition matrix and γ the discount.

### Procedure

1) With γ = 0.5, write M(s, 4) for s = 1, 2, 3, 4: how strongly each position predicts a future visit to position 4. (Check: 0.125, 0.25, 0.5, 1.)
2) A "place cell" for position 4 fires in proportion to M(current position, 4). Sketch its firing along the track. Which way does its field extend?
3) Repeat with γ = 0.9. (Check: 0.729, 0.81, 0.9, 1.) What happens to the field, and what does γ represent?
4) Now let the animal move left or right with equal probability. Without calculating, will the field for a middle position be skewed? Why?
5) Mehta and colleagues saw fields grow backward over the first laps of a session. Explain how learning M from experience, lap by lap, would produce the growth.
6) Write 6-10 sentences: why a map that encodes "what comes next" is useful for both memory and navigation.

## Lab 12.4 - Fixed and Adaptive Learning Rates

### Purpose

To see, with ten numbers, why no fixed learning rate is best and how an uncertainty-dependent rate does better (Figure 12.5).

### Given data

Observations: 50, 52, 48, 50, 90, 88, 92, 90, 91, 89. The hidden mean is 50 for the first four and 90 after.
Delta rule: estimate ← estimate + α × (observation − estimate), starting at 50.

### Procedure

1) With α = 0.2, compute the estimate before each observation and after the last. (Check: before the 5th observation 49.94; final 79.50.)
2) With α = 0.8. (Check: before the 5th 49.74; final 89.37.) Which rate is better before the jump, and which after?
3) Adaptive rule: let n count the observations since the last surprise, starting at n = 1; use α = 1/(n + 1), then add 1 to n; but if the error exceeds 20, first reset n to 0. Compute the estimates and the rates. (Check: rates 0.5, 0.33, 0.25, 0.2, 1.0, 0.5, 0.33, 0.25, 0.2, 0.17; final estimate 90.0.)
4) Compute the total squared error, Σ(estimate before observation − hidden mean)², for all three learners. Which wins?
5) What would happen to the adaptive learner if an outlier of 75 appeared once in a stable run of 50s? How did Nassar's model avoid overreacting to single outliers?
6) Write 6-10 sentences relating the adaptive rule to Yu and Dayan's proposal about acetylcholine and norepinephrine, and to Nassar's pupil measurements.

## Lab 12.5 - Living Slightly in the Past

### Purpose

To estimate how far the world moves during the brain's processing delays, and so how much prediction is needed.

### Given values

First responses in monkey V1 arrive about 66 ms after a stimulus; take 100 ms as the delay before a percept is available to guide action.

### Procedure

1) How far does an object move during 66 ms and during 100 ms at 10, 30, and 40 meters per second? (Check: 0.66 and 1.00 m; 1.98 and 3.00 m; 2.64 and 4.00 m.)
2) A cricket ball bowled at 40 m/s travels about 20 m. How long is its flight, and what fraction of it passes before the batter's visual cortex has registered the release?
3) Describe the flash-lag effect, and explain how it could result from a brain that extrapolates moving objects forward to compensate for its delay.
4) Saccades occur three or four times a second. Explain why a visual system that waited for the retina after each one would be blind for much of the time, and how the shifting receptive fields of Duhamel and colleagues avoid this.
5) Write 6-10 sentences: name one situation in which prediction to cancel delay would mislead you, and one in which having no prediction would be dangerous.

## Lab 12.6 - Surprise and the Dark Room

### Purpose

To make concrete what "surprise" means in the free-energy account and why the dark-room objection depends on the model.

### Given values

Surprise of a state = −log2 of its probability under the creature's model. Two states: sitting in a dark room, or foraging in the open.
Creature A's model (a cave-dwelling creature): dark room 0.9, foraging 0.1. Creature B's model (a creature like us): dark room 0.02, foraging 0.98.

### Procedure

1) Compute the surprise of each state for each creature. (Check: A, 0.15 and 3.32 bits; B, 5.64 and 0.03 bits.)
2) Which state does each creature seek if it minimizes surprise? Is a dark room "unsurprising" in general?
3) Where did creature B's expectation of foraging come from? List three possible sources (evolution, development, learning).
4) The chapter says the reply to the dark-room problem works "at a price". In two or three sentences, state the price.
5) Write 6-10 sentences: is the free-energy principle a theory that could be wrong, or a way of describing any creature? Use Friston's own statement and one critic's.

## Lab 12.7 - Prediction Across the Book (concept map)

### Purpose

To assemble the book's examples of prediction into one argued map.

### Procedure

1) Copy the six rows of Figure 12.1 and add at least three more from this chapter (for example, retinal surround, thirst neurons, visuomotor mismatch, the N400).
2) For each row, say what sets the learning rate, if anything is known.
3) Mark each row with the timescales over which its predictions are revised (use Figure 12.6).
4) Add one example that prediction does not explain well, from the chapter's section "What Prediction Leaves Out" or from earlier chapters.
5) Write 8-12 sentences answering the chapter's question: is prediction one principle beneath the mechanisms, a family resemblance among them, or something in between? Defend your answer with two examples.
