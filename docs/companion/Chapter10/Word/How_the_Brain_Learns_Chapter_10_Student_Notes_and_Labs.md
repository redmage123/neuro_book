---
title: "Chapter 10 Student Notes and Labs"
subtitle: "What Artificial Intelligence Gets Right and Wrong: Machine Learning Measured Against the Brain"
---

# Student Notes

## What this chapter is for

Each chapter so far ended by asking what its subject means for artificial intelligence. Chapter 10 gathers those questions and measures machine learning against the brain directly: which of the brain's solutions machine learning has found, which it has not, and which it does not need.

If you come from software or machine learning, the chapter is designed to correct three instincts:
1) treating "brain-like" as one question, rather than three (performance, representation, mechanism), on which current systems score very differently,
2) treating the brain as a blueprint to copy, rather than as a list of problems a learner meets outside the laboratory, with evidence that each can be solved, and
3) treating the differences as all deficits, rather than sorting them into solutions worth borrowing and responses to biological constraints that silicon does not share.

Your goal is to be able to explain where trained networks resemble the brain and where the resemblance breaks down, why the data and energy gaps exist, why networks forget and how replay helps, what is and is not known about credit assignment in the brain, what bodies give an organism, how fluency differs from thought, why models answer when they should not, the case for and against the bitter lesson, and what machine learning has given neuroscience.

## What is being measured

- Rosenblatt's perceptron (1958): the Navy expected its descendants to walk, talk, and be conscious. The idea, a network that learns by adjusting connection strengths after errors, came from the brain.
- Three scales: performance (does it do the task?), representation (is it organized inside like the brain?), mechanism (does it get there the same way?). They borrow loosely from Marr's levels (Chapter 1).
- Thesis: machine learning got the core idea right (learned, distributed knowledge shaped by error and prediction). It differs in the conditions of learning: data, lifetime, energy, values, local rules, learning during use. Some differences are failures to repair; others are constraints not to copy.

## A shared ancestry

- McCulloch and Pitts (1943); Hebb (1949); the perceptron (1958); Minsky and Papert (1969) on what one layer cannot compute.
- Hubel and Wiesel to Fukushima's neocognitron (1980) to LeCun's convolutional network (1989) to Krizhevsky, Sutskever, and Hinton (2012): error from 26 to 15 percent (Figure 10.1).
- Backpropagation: the gradient calculation came from mathematics and control; Rumelhart, Hinton, and Williams (1986) showed it learns useful hidden representations.
- The other direction: Rescorla and Wagner to Sutton and Barto's TD learning to Schultz's dopamine neurons; distributional RL to distributional dopamine (Dabney 2020; Sousa 2025).

## What the machines got right: representations

- Networks trained to categorize objects predict IT, and better categorizers predicted better, for the models of 2014 (Yamins 2014; Khaligh-Razavi and Kriegeskorte 2014) (Figure 10.2).
- The relation broke down: more accurate later networks predict IT worse (Linsley 2023).
- Networks copy the feedforward sweep, not the loops: challenge images resolve about 30 ms later in IT; feedforward networks predict these late responses poorly and deeper ones better, read as a sign of recurrent processing (Kar 2019).
- Language models predict the language network, best when best at next-word prediction (Schrimpf 2021); the brain predicts words before they arrive (Goldstein 2022); the convergence is partial (Caucheteux and King 2022).
- Grid-like units emerge from path integration (Banino 2018), but only under specific modeling choices (Schaeffer, Khona, and Fiete 2022).
- Caution: good neural prediction is not the same as a good model of vision (Bowers 2023).

## What the machines got right: error and prediction

- Both learn from the difference between expected and actual: dopamine (Chapter 3), the third factor (Chapter 5), predictive coding (Chapter 6).
- Self-supervised learning (predict part of the input from the rest) is the brain's regime. But next-token prediction is not hierarchical predictive coding, and the final stages of training use rewards.
- Scaling laws: error falls as a power of size, data, and compute (Kaplan 2020); balance data with size (Hoffmann 2022, Chinchilla).

## Shortcuts

- Networks use whatever feature reduces error (Geirhos 2020). The pneumonia detector learned to recognize hospitals from tokens on the films (Zech 2018).
- A fresh ImageNet test set cost every model 11 to 14 points (Recht 2019), largely through subtle selection differences (Engstrom 2020).
- Larger, more varied training data narrow the robustness gap (Geirhos 2021): varied practice again (Chapter 9).

## The data gap

- A child hears at most about 10^6 words a month: 6 × 10^7 by five, 2 × 10^8 by 20 (Frank 2023). GPT-3: 3 × 10^11 tokens; Llama 3: about 1.5 × 10^13 (Figure 10.3).
- Innate structure: newborn face tracking (Johnson 1991); object permanence tested at four to five months (Baillargeon 1985), debated; the genomic bottleneck (Zador 2019).
- Rich, embodied experience: a network trained on 61 hours from one child's headcam matched words to pictures 62 percent of the time against 25 percent chance (Vong 2024). BabyLM: on mostly grammatical tests, the best models trained on a child's budget matched some trained on trillions of words (Warstadt 2023).
- One-shot learning by causal models (Lake 2015, 2017); in-context learning (Brown 2020) as a fast learner trained by a slow one (Wang 2018).

## Learning that never stops

- Deployed models are trained once and then frozen; context windows, retrieval, and text memories are not learning in the weights (Figure 10.4).
- Catastrophic interference (McCloskey and Cohen 1989) (Figure 10.5); complementary learning systems and replay (McClelland 1995; Kumaran 2016); experience replay (Lin 1992; Mnih 2015).
- Loss of plasticity: after thousands of tasks, networks learn no better than one with no hidden layers; continual backpropagation reinitializes little-used units (Dohare 2024).
- The brain maintains plasticity: synapse turnover; adult neurogenesis in many mammals, disputed in humans (Sorrells 2018; Boldrini 2018).

## Credit without backpropagation

- Weight transport: the brain has no obvious backward pathway (Crick 1989; Chapter 3).
- Candidate answers: random feedback (Lillicrap 2016), apical bursts (Payeur 2021), predictive coding (Whittington and Bogacz 2017), dendritic microcircuits (Sacramento 2018). None shown in cortex; they fall short at scale (Bartunov 2018).
- Prospective configuration: settle activity first, then change synapses; faster and with less interference in simulations (Song 2024).

## The energy bill

- Brain: 20 W, about 3.5 MWh over 20 years. GPT-3 training: about 1,287 MWh (Patterson 2021) (Figure 10.6). Inference is about three-fifths of machine-learning energy at Google (Patterson 2022).
- Rediscoveries: sparse activation in mixtures of experts (Shazeer 2017; Fedus 2022); spiking neuromorphic chips (TrueNorth at 63 mW; Loihi).

## Bodies

- AlphaGo beat Lee Sedol 4 to 1, but a person placed its stones. Moravec's paradox: perception and movement are hard for machines because evolution hid their difficulty.
- Robots now fold laundry from demonstrations (Black 2024), but need far more practice than a child, who has forward models and a cerebellum.
- A body anchors value (Chapter 7); a model values what training rewarded.

## Fluency and thought

- Formal versus functional linguistic competence (Mahowald 2024). Language and thought use different networks: agrammatic aphasic patients solve nested arithmetic (Varley 2005; Fedorenko 2024).
- Traces of training statistics: rot-13 versus rot-12 (McCoy 2024); the reversal curse, 79 versus 33 percent (Berglund 2024); planning collapses when disguised (Valmeekam 2023).
- Reasoning models (Wei 2022; DeepSeek-R1 2025) solve nearly all plain block problems and about half of disguised ones (Valmeekam 2024).
- World models: DreamerV3 collects diamonds in Minecraft (Hafner 2025); hippocampal sequences sketch future paths (Pfeiffer and Foster 2013).

## Knowing what it does not know

- AlphaGo did not know it was losing after Lee's move 78 (mistake at 79, realized around 87).
- Hallucination is rewarded by evaluations that score abstention as zero (Kalai 2025). Pretrained GPT-4 was well calibrated; post-training degraded it (OpenAI 2023).
- People are miscalibrated too, but consequences pull confidence toward accuracy.
- Chapter 9's question: reasoning models overthink easy problems (Chen 2024) and underthink hard ones (Wang 2025); the brain's trigger is a missing expected outcome.

## What not to copy

- The bitter lesson: general methods that use computation win (Sutton 2019). Reply: the brain is a list of problems, not a blueprint (Figure 10.7).
- Do not copy slowness, imprecision, or the inability to copy, reset, or inspect.
- Sorting: lifelong learning and honest confidence are solutions to borrow; frugality is a solution now needed; small data is partly evolution's gift; bodily values are a constraint whose benefit must be bought otherwise; the local rule is open.

## Implications for neuroscience

1) Trained networks are models of the brain, judged by neural prediction; describe brains by objectives, rules, and architectures (Kriegeskorte 2015; Richards 2019).
2) Models can control neurons: synthesized images drive V4 beyond natural ones (Bashivan 2019); neurons guide image evolution (Ponce 2019).
3) The innateness debate reopened (Piantadosi 2024 versus the data-gap reply; BabyLM).

## Practical summary

- Trained networks resemble the brain in representation, up to a point, and mostly in the feedforward sweep.
- Error-driven learning of predictions is shared; the procedure (backpropagation) probably is not.
- Machines need far more data and energy, forget when trained in sequence, and stop learning when deployed.
- Bodies give skills their difficulty and values their anchor.
- Fluent language is not proof of thought; reasoning models narrow but do not close the gap.
- Calibration exists in models and is lost when training rewards answering.
- Copy the problems the brain solves, not its constraints.

# Labs

## Lab Notes: how to succeed in these labs

These labs turn the chapter's comparisons into short calculations: how much language a child and a model receive, what learning costs in energy, why a network forgets and how interleaving prevents it, how a model is compared with a brain, how a model's confidence should decide whether it answers, and how a learner can be right for the wrong reason. Each isolates one idea. The arithmetic is light; the point is to see where the numbers come from and how much they depend on assumptions.

General rules:
1) Write every intermediate value, rounded to two decimal places unless told otherwise. Where a lab carries values forward from row to row, keep three decimals while computing; your answers may then differ from the check values by 0.01.
2) State every assumption you add, and say which way it would move the answer.
3) End with an interpretation: what does the comparison show, and what does it leave out?

### What to hand in for every lab

- A table of values.
- A diagram or sketch where requested (a photo of a hand drawing is fine).
- A short interpretation (6-12 sentences).

## Lab 10.1 - The Data Gap (orders of magnitude)

### Purpose

To reproduce the comparison in Figure 10.3 and to see how much of it survives a change of assumptions.

### Given values

A child hears at most about 1,000,000 (10^6) words a month (Frank's high estimate; his low estimate is about ten times less).
GPT-3 was trained on 3 × 10^11 tokens; Llama 3 on about 1.5 × 10^13 tokens. Treat one token as one word.

### Procedure

1) At the high rate, how many words has a person heard by age 5, 10, and 20? (Check: 6 × 10^7, 1.2 × 10^8, 2.4 × 10^8. Frank rounds the last to 2 × 10^8.)
2) How many times more language did GPT-3 and Llama 3 see than a five-year-old? Than a 20-year-old? (Check: GPT-3 5,000 and 1,250; Llama 3 250,000 and 62,500.)
3) At the high rate, how many years would a person have to listen to hear as much as GPT-3? As Llama 3? (Check: 25,000 years; 1,250,000 years.)
4) Repeat step 2 with Frank's low estimate. By how many orders of magnitude does the gap change? (Check: it grows by one, a factor of ten.)
5) A token is on average a little less than a word. Does correcting for this make the gap larger or smaller, and does it matter at this scale?
6) Write 6-10 sentences: name two things a child has that the models lack (use Zador's genomic bottleneck and Vong and colleagues' headcam study), and one thing the models have that the child lacks. Is the comparison fair to either side?

## Lab 10.2 - The Energy Bill (watts, hours, and brains)

### Purpose

To reproduce Figure 10.6 and to practice converting between power and energy.

### Given values

A brain uses about 20 W. One year is 365.25 days. Training GPT-3 used an estimated 1,287 MWh. A current data-center processor can draw up to 700 W.
Energy (watt-hours) = power (watts) × time (hours). 1 MWh = 1,000 kWh = 1,000,000 Wh.

### Procedure

1) How much energy does a brain use in one day? In 20 years? (Check: 0.48 kWh; 3.51 MWh.)
2) How many 20-year brain lifetimes would equal the training of GPT-3? (Check: about 367.)
3) How many brains draw as much power as one 700 W processor? How much energy does that processor use in a year of continuous running? (Check: 35 brains; 6.14 MWh, more than a brain uses in 20 years.)
4) A trained model answers millions of questions. Suppose answering one question costs 0.3 Wh. How many questions use as much energy as training GPT-3? (Check: about 4.3 billion.) What does this suggest about where most of a widely used model's energy goes?
5) List two costs the brain's figure leaves out and two benefits the model's figure leaves out.
6) Write 6-10 sentences: which features of the brain described in Chapters 1 and 2 keep its power low, and which of them machine learning has begun to borrow (mixtures of experts; neuromorphic chips).

## Lab 10.3 - Forgetting by Hand (catastrophic interference in one unit)

### Purpose

To watch a single learning unit forget, and to see why interleaving protects it. This is Figure 10.5 reduced to three weights.

### Given model

A linear unit with three weights w = (w1, w2, w3), all starting at 0. Its output is y = w1·x1 + w2·x2 + w3·x3.
Input x1 is a shared cue present in every item. Inputs x2 and x3 are context: x2 = 1 for list A, x3 = 1 for list B.
Item A: x = (1, 1, 0), target +1. Item B: x = (1, 0, 1), target −1.
Learning rule (the delta rule, a one-layer form of backpropagation): after each trial, w ← w + 0.25 × (target − y) × x.

### Procedure

1) Sequential training: four trials of A, then four trials of B. Tabulate trial, item, y before the update, the three weights after it, and the output the unit would now give to A and to B. (Check: after trial 4, w = (0.469, 0.469, 0), output to A = 0.94; after trial 8, w = (−0.220, 0.469, −0.688), output to A = 0.25, output to B = −0.91.)
2) Which weight changed during the B trials, and which did not? Explain why the response to A collapsed although w2 was untouched.
3) Interleaved training: eight trials in the order A, B, A, B, A, B, A, B. Tabulate as before. (Check: after trial 8, w = (−0.042, 0.719, −0.760), output to A = 0.68, output to B = −0.80.)
4) Compare the two schedules after eight trials. Which learned B faster? Which ends with both lists usable? What did interleaving do to the shared weight w1?
5) Remove the context inputs (set x2 = x3 = 0 always). Can any weights give A and B their different targets? What does this say about the importance of context, and about the list-context units in McCloskey and Cohen's experiment?
6) Write 6-10 sentences relating this lab to complementary learning systems: which part of the brain stores an episode at once, how replay turns a sequential schedule into an interleaved one, and why experience replay helped Mnih and colleagues' Atari agent.

## Lab 10.4 - Comparing a Model with a Brain (representational similarity)

### Purpose

To carry out, by hand, the comparison Kriegeskorte and colleagues use to ask whether a model represents things as a brain does.

### Given data

Four images: a dog, a cat, a car, and a house. For each pair, the dissimilarity of the response patterns (0 = identical, 1 = completely different):

| pair | brain (IT) | model 1 | model 2 |
|---|---|---|---|
| dog-cat | 0.20 | 0.30 | 0.60 |
| dog-car | 0.80 | 0.70 | 0.50 |
| dog-house | 0.90 | 0.95 | 0.40 |
| cat-car | 0.75 | 0.80 | 0.70 |
| cat-house | 0.85 | 0.90 | 0.30 |
| car-house | 0.40 | 0.50 | 0.90 |

### Procedure

1) Draw the brain's 4 × 4 dissimilarity matrix. Which two pairs are most similar, and what category distinction does that reflect? (Check: dog-cat and car-house; animate against inanimate.)
2) Rank the six brain values from 1 (most similar) to 6. Do the same for each model. (Check: brain 1, 4, 6, 3, 5, 2; model 1: 1, 3, 6, 4, 5, 2; model 2: 4, 3, 2, 5, 1, 6.)
3) Compute the Spearman rank correlation between the brain and each model: ρ = 1 − 6Σd² / (n(n² − 1)), with n = 6 and d the difference in rank for each pair. (Check: Σd² = 2 and ρ = 0.94 for model 1; Σd² = 62 and ρ = −0.77 for model 2.)
4) Model 2 might still classify the four images perfectly. Explain how a model can do the task and still represent the images differently from the brain.
5) Why compare rankings of dissimilarities rather than the raw activity of individual units? Name one thing this method cannot tell you.
6) Write 6-10 sentences: what Yamins and colleagues found about task performance and similarity to IT, and Bowers and colleagues' objection that a good fit to neural data is not the same as a good model of vision.

## Lab 10.5 - When Should a Model Say "I Do Not Know"? (calibration and abstention)

### Purpose

To see how the scoring of answers decides whether guessing pays, the argument of Kalai and colleagues, and to measure calibration.

### Given data

A model answers ten questions. Its stated confidence and whether it was right:

| question | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| confidence | 0.95 | 0.90 | 0.90 | 0.80 | 0.70 | 0.60 | 0.60 | 0.50 | 0.40 | 0.30 |
| correct? | yes | yes | yes | yes | no | yes | no | yes | no | no |

Scoring: +1 for a correct answer, 0 for "I do not know", and −k for a wrong answer.

### Procedure

1) Compute the model's accuracy and its average confidence. Is it overconfident or underconfident, and by how much? (Check: accuracy 0.60; mean confidence 0.665; overconfident by 0.065.)
2) Show that a model that is right with probability p should answer only if p − k(1 − p) > 0, that is, if p > k/(1 + k). What is the threshold for k = 0, 1, and 3? (Check: answer always; p > 0.5; p > 0.75.)
3) For k = 0, compute the total score if the model answers everything. Can abstaining ever raise the score? (Check: 6; no.)
4) For k = 1 and k = 3, compute the total score if the model answers only above its threshold, and if it answers everything. (Check: k = 1: 3 against 2, or 4 if you also answer question 8, where p = 0.5 makes answering neither better nor worse in expectation; k = 3: 4 against −6.)
5) Most benchmarks score wrong answers and abstentions both as zero. What does step 3 say about what such benchmarks teach a model to do?
6) Write 6-10 sentences: how the monkey that takes the sure target and the rat that waits in proportion to its confidence (Chapter 8) solve this problem, what in an animal plays the role of k, and why calibration alone is not enough without a rule for acting on it.

## Lab 10.6 - Right for the Wrong Reason (shortcut learning)

### Purpose

To see how a learner can choose a feature that works in training and fails in the world, as in the cows-on-grass and hospital-token examples of Geirhos and colleagues and Zech and colleagues.

### Given data

A training set of 100 photographs: 50 of cows and 50 of other things. All 50 cows are standing on grass; 10 of the non-cow photographs also show grass.
Two candidate features: "grass in the picture" and "cow-shaped outline". The outline detector is right on 85 of every 100 photographs, whatever the background.
A learner picks the single feature with the highest accuracy on the training set.

### Procedure

1) What is the accuracy of the rule "say cow if there is grass" on the training set? (Check: 90 of 100, 0.90.) Which feature does the learner pick?
2) A test set has 50 cows photographed on beaches and 50 non-cows on grass. What is the accuracy of the grass rule? Of the outline rule? (Check: 0.00; 0.85.)
3) How many cows on beaches would the training set have needed for the outline rule to win? (Check: more than five of the 50 cows not on grass would bring the grass rule below 0.85 if nothing else changes; show your reasoning.)
4) Explain why collecting more photographs of the same kind would not fix the problem, and why varied photographs would. Relate this to Chapter 9's beanbags and to Geirhos and colleagues' finding that models trained on far larger and more varied data became more robust.
5) Give one shortcut a person might learn in the same way, and say what usually breaks it.
6) Write 6-10 sentences: what a brain has, beyond more data, that makes it less prone to shortcuts (consider interaction, causal models, and learning across many tasks at once), and whether the brain is immune.

## Lab 10.7 - A Ledger of Brains and Machines (concept map)

### Purpose

To assemble the chapter, and the AI sections of the earlier chapters, into one argued map.

### Procedure

1) Copy the eleven properties in Figure 10.7. For each, write one sentence of evidence from this chapter or an earlier one and one citation.
2) For each property marked "largely absent" or "partly shared", decide whether it is (a) a solution machine learning should borrow, (b) a response to a biological constraint that silicon does not share, or (c) unclear. Defend two of your choices in three sentences each.
3) Add one property the figure leaves out (candidates: sleep, neuromodulation, embodiment in action, social learning, development) and mark where current systems stand.
4) Draw arrows between properties that depend on one another (for example, learning from little data and innate structure; lifelong learning and replay; energy and sparse activity).
5) Write 8-12 sentences answering the chapter's question in your own words: which differences between brains and current machines matter most, and why. Include Sutton's bitter lesson and the strongest reply to it you can give.
