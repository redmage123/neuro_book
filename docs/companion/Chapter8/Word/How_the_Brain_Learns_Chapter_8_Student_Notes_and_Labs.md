---
title: "Chapter 8 Student Notes and Labs"
subtitle: "Decision-Making Under Uncertainty: How the Brain Chooses When It Cannot Be Sure"
---

# Student Notes

## What this chapter is for

Chapter 7 left a problem: patients with ventromedial prefrontal damage can describe a card game and still lose at it. Chapter 8 asks what choosing well requires when evidence is noisy, outcomes are uncertain, and thinking takes time.

If you come from software or machine learning, the chapter is designed to correct three instincts:
1) treating a decision as a single computation on a fixed input, rather than an accumulation that stops when it is sure enough,
2) treating departures from expected-value maximization as bugs, rather than as features of a chooser with limited time, limited computation, and a body to protect, and
3) treating "the policy" as one thing, rather than several controllers (planning, habit, Pavlovian) that compete according to their reliability.

Your goal is to be able to explain how value is represented and learned, how evidence is accumulated to a bound and what sets the bound, how confidence is computed, how prospect theory departs from expected utility, why hyperbolic discounting produces preference reversals, how directed and random exploration differ, how goal-directed and habitual control are distinguished experimentally, and what each of these implies for artificial agents.

## The problem decision solves

Every decision answers two questions: what the world is like (evidence) and what each option is worth (value). Neither is certain, and deliberation has its own cost.
Thesis: the brain accumulates evidence until it is sure enough, values options on a relative and body-dependent scale, balances exploiting against exploring, and runs more than one decision system. Every one of these settings is tuned by learning (Figure 8.1).
Pascal, who with Fermat founded probability theory in 1654 and gave the first decision-theoretic argument (the wager), also wrote that the heart has its reasons: the chapter is about both halves of him.

## Accumulating evidence

- Random-dot motion task. MT neurons are about as sensitive as the monkey (Newsome 1989), and microstimulation biases choice (Salzman 1990).
- LIP neurons ramp at a rate set by motion strength and reach a common level about 70 ms before the eye movement (Shadlen and Newsome 2001; Roitman and Shadlen 2002) (Figure 8.2).
- Wald's sequential probability ratio test: stop when summed evidence crosses a bound; optimal (Wald and Wolfowitz 1948). Turing used the principle at Bletchley Park. Wald's evidence is a log likelihood ratio, so the test is Chapter 6's Bayesian inference done one sample at a time. Drift diffusion model (Ratcliff 1978) is the continuous form and is optimal for two choices with evidence of fixed strength (Bogacz 2006) (Figure 8.3A).
- Speed-accuracy trade-off: the bound sets it (Figure 8.3B). Worked example: 70 percent correct in 0.5 s needs a bound about 2.5 times higher to reach 90 percent, and takes about five times as long.
- Conflict raises the bound (frontal theta rhythm); deep brain stimulation of the subthalamic nucleus, the hyperdirect relay of Chapter 4, abolishes this and makes choices hasty (Frank 2007; Cavanagh 2011). When difficulty varies, the optimal bound falls with time (Drugowitsch 2012), and an urgency signal appears in some tasks (Churchland 2008), though fixed bounds fit most data sets (Hawkins 2015).
- Challenges: single-trial LIP activity may step rather than ramp (Latimer 2015); silencing LIP did not impair the decision (Katz 2016). Rebuttals: population recordings show single-trial drift and diffusion (Steinemann 2024); LIP inactivation does impair decisions before other areas compensate (Jeurissen 2022). LIP is probably one of several areas that keep the running total.

## Knowing how sure you are

- Kiani and Shadlen (2009): monkeys take a sure small reward more often when evidence is weak; LIP predicts it.
- Lak and Kepecs (2014): rats wait longer for an uncertain reward when their choice is more likely correct; silencing orbitofrontal cortex removes the link without affecting accuracy.
- Decisions stay open: changes of mind come from evidence still in the pipeline (Resulaj 2009).
- Metacognition: anterior prefrontal gray matter predicts how well confidence tracks accuracy (Fleming 2010).

## A common currency

- Bernoulli (1738): utility. Von Neumann and Morgenstern (1947, 2nd ed.): consistent preferences behave as if maximizing expected utility.
- Padoa-Schioppa and Assad (2006), orbitofrontal cortex: offer-value cells for one particular juice; chosen-value cells on a common scale, whatever the juice; taste cells for the juice chosen.
- Plassmann (2007): medial orbitofrontal activity tracks willingness to pay. Bartra (2013), meta-analysis of more than 200 studies: ventromedial prefrontal cortex and ventral striatum track subjective value for money and primary rewards.
- Ventromedial damage makes preferences inconsistent (Camille 2011).
- Contested: Levy and Glimcher (a common currency) against Hayden and Niv (no single value variable is required).
- Value may be relative: parietal value signals are divisively normalized (Louie 2011; Carandini and Heeger 2012), and Louie (2013) proposed this makes choice depend on context, but a preregistered replication did not find the behavioral effect (Gluth 2020).

## Learning what options are worth

- Values are learned by the dopamine reward prediction error of Chapter 3 (Schultz, Dayan, and Montague 1997).
- Matching law (Herrnstein 1961): over a session, choices are divided in proportion to each option's rate of reward. Sugrue (2004): monkeys match recent rewards, and LIP neurons track each option's share of recent income.
- Fellows and Farah (2005): the Iowa deficit is largely a failure to reverse a learned value; the region that should have revised the value is the one that was damaged.
- Value and evidence meet: Krajbich (2010), attentional drift diffusion, people choose what they looked at longest; Hunt (2012), a ventromedial prefrontal signal matching value comparison by mutual competition.

## Risk, loss, and ambiguity

- A 50:50 gamble to win 110 or lose 100 has an expected value of 5 and is usually refused. Rabin (2000): refusing it at every wealth level would, under expected utility, mean refusing to risk 1,000 for any gain at all, so small refusals need another explanation.
- Prospect theory (Kahneman and Tversky 1979; 1992): outcomes as gains and losses from a reference point; for moderate and large probabilities, risk averse for gains and risk seeking for losses; losses weigh about twice as much; small probabilities overweighted, which is why people buy both lottery tickets and insurance (Figure 8.4).
- Framing (Tversky and Kahneman 1981): 72 percent choose the sure option framed as lives saved; 78 percent choose the gamble framed as lives lost. Amygdala tracks the frame; orbital and medial prefrontal activity tracks resistance (De Martino 2006).
- Neural loss aversion in ventral striatum and ventromedial prefrontal cortex predicts behavioral loss aversion (Tom 2007). Two patients with amygdala damage, including S.M. of Chapter 7, showed sharply reduced loss aversion (De Martino 2010). Its size and generality are debated (Gal and Rucker 2018); a meta-analysis puts the typical value somewhat below two (Brown 2024).
- Description versus experience: told the odds, people overweight rare events; learning them from samples, they underweight them (Hertwig 2004).
- Ambiguity (Ellsberg 1961): people prefer the urn with known odds; ambiguity engages amygdala and orbitofrontal cortex, and orbitofrontal damage reduces aversion to both ambiguity and risk (Hsu 2005). No single belief about the unknown urn explains preferring the known urn for both colors.

## The price of waiting

- Discounting is roughly hyperbolic, V = A / (1 + kD) (Mazur 1987), and so preferences reverse as rewards approach (Strotz 1955; Ainslie 1975) (Figure 8.5). Hyperbolic discounting is rational if the hazard rate is uncertain (Sozou 1998).
- Two systems (McClure 2004) or one (Kable and Glimcher 2007)? Or prefrontal modulation of the value signal (Hare 2009)? Debated. Stimulating serotonin neurons makes mice wait longer (Miyazaki 2014).
- Marshmallow test (Mischel 1989; Shoda 1990); replication in about 900 children about half as large, much of it explained by background (Watts 2018); 28 children waited about four times as long after a reliable experimenter (Kidd 2013), but 149 children showed no significant trust effect and a role for habits of waiting (Yanaoka 2026). Waiting is partly a judgment of how reliable the future is.

## Explore or exploit

- No solution that is both general and practical. The multi-armed bandit: Gittins (1979) index; uncertainty bonuses whose losses grow only slowly (Auer 2002) (Figure 8.6).
- Two kinds of exploration, random and directed. People explore partly at random, engaging frontopolar cortex (Daw 2006), and both kinds increase with a longer horizon (Wilson 2014).
- Learning rate rises with volatility, tracked by anterior cingulate cortex (Behrens 2007); consistent with the norepinephrine account, though norepinephrine was not measured.
- Foraging: leave a patch when its yield falls to the environment's average (Charnov 1976); dorsal anterior cingulate neurons rise to a threshold at leaving (Hayden 2011) and track the value of searching (Kolling 2012), or choice difficulty (Shenhav 2014). Tonic dopamine may report the average reward rate, the cost of time (Niv 2007).

## Goals and habits

- Tolman (1948): cognitive maps. Devaluation (Adams and Dickinson 1981; Adams 1982), tested without delivering the outcome: moderately trained rats stop pressing; extensively trained rats keep pressing (Figure 8.7).
- Goal-directed: dorsomedial striatum and prefrontal cortex. Habit: dorsolateral striatum; lesions keep rats goal-directed on habit-inducing interval schedules (Yin 2004; Balleine and O'Doherty 2010). Human overtraining (Tricomi 2009, three days) failed in five experiments, two of them direct replications (de Wit 2018).
- Model-based (plans from a model; flexible, costly) versus model-free (cached values via prediction error; fast, inflexible). Daw, Niv, and Dayan (2005) proposed that control goes to the less uncertain system; others model habits as value-free repetition (Miller 2019). Two-step task shows both influences (Daw 2011), though model-free strategies can mimic some model-based signatures (Akam 2015). Compulsivity is associated with weaker model-based control (Gillan 2016, more than 1,000 people).
- Pavlovian controller: the Brelands' raccoon washing coins (1961); pigeons pecking a key even when pecking cancels food (Williams and Williams 1969); models of Pavlovian override (Dayan 2006).
- Chapter 9 takes up how repeated choices become routines and skills.

## Thinking is costly

- Bounded rationality and satisficing (Simon 1955, 1956). Recognition heuristic: all German students but about 62 percent of American students picked San Diego as larger than San Antonio (Goldstein and Gigerenzer 2002; San Diego was then the larger city). Fast and frugal heuristics (Gigerenzer and Goldstein 1996); resource rationality (Lieder and Griffiths 2020); the expected value of control in dorsal anterior cingulate cortex (Shenhav 2013).
- Many biases make sense as policies of a chooser with limited time and computation in an uncertain, changing, sometimes adversarial world; some are miscalibrated for modern life.

## Choosing among others

- Ultimatum game (Güth 1982): offers below about a fifth are rejected about half the time; proposers offer 40 to 50 percent (Henrich 2001). Anterior insula activity predicts rejection (Sanfey 2003).
- Disrupting right dorsolateral prefrontal cortex with transcranial magnetic stimulation makes people accept unfair offers they still judge unfair (Knoch 2006).
- Offers vary across 15 small-scale societies with market integration and payoffs to cooperation (Henrich 2001).

## When choice goes wrong

- Parkinson's disease (as in Chapter 3): off medication patients learn better from bad outcomes, on medication from good ones (Frank 2004). Impulse control disorders in about one in seven patients, with nearly three times the odds on dopamine agonists (Weintraub 2010).
- Addiction as a prediction error the drug keeps producing (Redish 2004), Chapter 7's reward hacking; but its blocking prediction failed (Panlilio 2007). Computational psychiatry (Huys 2016). What fails is the machinery that learns what to choose, and the most persistent failures are habits that have outlived their reasons.

## Implications for artificial intelligence

1) Accumulation to a bound: spend computation in proportion to difficulty and stakes. Adaptive computation (Graves 2016) and reasoning language models move this way, but rarely set the stopping point by the stakes.
2) Calibrated confidence: mid-2010s deep networks were overconfident (Guo 2017); newer architectures and language models are better calibrated (Minderer 2021; Kadavath 2022), but reliability out of distribution is hard; uncertainty can be estimated (Gal and Ghahramani 2016).
3) Exploration is mostly set by hand, with schedules and novelty bonuses (Bellemare 2016); people adapt it to horizon and volatility.
4) AlphaGo, first to beat a professional on a full board without handicap, combined fast learned evaluation with search (Silver 2016); the brain adds arbitration.
5) Biases can be protections in adversarial or changing environments.

## Practical summary

- Decisions accumulate evidence to a bound; the bound sets speed against accuracy and moves with stakes and conflict.
- Value is learned by prediction error, represented on a relative scale, and tied to the body.
- Confidence is computed and can be acted on.
- Losses, ambiguity, and delay are weighted in ways that depart from expected value and are often adaptive.
- Exploration is directed and random, and depends on horizon and volatility.
- Goal-directed and habitual control compete by reliability; a Pavlovian controller can override both.
- Disorders of choice can be traced to specific components.

# Labs

## Lab Notes: how to succeed in these labs

These labs turn the chapter's models into short calculations: summing evidence to a bound, trading speed against accuracy, pricing gambles with prospect theory, discounting, exploring a two-armed bandit, and testing goal-directed against habitual control. Each isolates one idea. The arithmetic is light; the point is to watch the rule behave and to ask what an organism gains or loses by it.

General rules:
1) Write every intermediate value, rounded to two decimal places unless told otherwise.
2) Draw the process or curve before computing.
3) End with an interpretation: what would change if a parameter changed, and what does the organism gain or lose?

### What to hand in for every lab

- A table of values.
- A diagram or sketch where requested (a photo of a hand drawing is fine).
- A short interpretation (6-12 sentences).

## Lab 8.1 - Stop When You Are Sure Enough (accumulating evidence)

### Purpose

To run the sequential sampling procedure of Wald and of the drift diffusion model by hand, and to see how the height of the bound trades speed against accuracy.

### Given model

Each sample of evidence is +1 (favors "right", which is the correct answer) or −1 (favors "left"). Add the samples as they arrive. Stop when the total reaches +b (choose right) or −b (choose left).
Sequence A: +1, −1, +1, +1, −1, +1, +1, +1, −1, +1, +1, +1
Sequence B: −1, −1, +1, +1, +1, −1, +1, +1, +1, +1

### Procedure

1) Tabulate the running total for both sequences. (Check: A: 1, 0, 1, 2, 1, 2, 3, 4, 3, 4, 5, 6; B: −1, −2, −1, 0, 1, 0, 1, 2, 3, 4.)
2) For sequence A, at which sample is the decision made with b = 2, b = 4, b = 6? Is it correct? (Check: samples 4, 8, and 12; all correct.)
3) For sequence B, with b = 2 and with b = 4. (Check: b = 2 stops at sample 2 with the wrong answer; b = 4 stops at sample 10 with the right one.)
4) Combine steps 2 and 3 into one sentence about the speed-accuracy trade-off.
5) Suppose the sample size doubles in strength (each sample is ±2 instead of ±1) with b = 4. What happens to decision time? What in the dot-motion task corresponds to stronger samples?
6) Write 6-10 sentences: what plays the role of the running total in LIP, what experiment would show that a bound is crossed, and why the Katz and Latimer results do not overturn accumulation as a description of behavior.

## Lab 8.2 - Choosing the Bound (speed, accuracy, and reward rate)

### Purpose

To use the drift diffusion formulas to find the bound that earns the most reward per unit time, and to see how the cost of errors moves it.

### Given model

With drift v (evidence strength) and noise 1, and bounds at ±a:
probability correct P = 1 / (1 + e^(−2va))
mean decision time DT = (a / v) × tanh(av)
Each trial also takes 2.3 seconds of fixed time (seeing the stimulus, moving, waiting). An error adds a penalty delay of d seconds. Reward rate = P / (DT + 2.3 + (1 − P) d). Use v = 0.582, the weak-evidence case of the chapter.

### Procedure

1) Compute P and DT for a = 0.5, 1.0, 1.5, 2.0. (Check: P = 0.642, 0.762, 0.851, 0.911; DT = 0.24, 0.90, 1.81, 2.83 s.)
2) With no error penalty (d = 0), compute the reward rate for each bound. Which bound is best? (Check: 0.252, 0.238, 0.207, 0.178; the lowest bound.)
3) With d = 6 s, recompute. (Check: 0.137, 0.165, 0.170, 0.161; best at a = 1.5.)
4) With d = 10 s. (Check: 0.105, 0.137, 0.152, 0.151; a = 1.5 is marginally best, with a = 2.0 nearly tied.)
5) Explain in two sentences why the best bound rises as errors become more costly. Relate this to the subthalamic nucleus result of Cavanagh and colleagues, and to what instructions such as "be careful" or "hurry" do to people's bounds.
6) Write 6-10 sentences: what an urgency signal does to this calculation when a deadline approaches, and why a fixed-computation artificial classifier cannot make this trade-off.

## Lab 8.3 - Prospect Theory by Hand (losses, frames, and ambiguity)

### Purpose

To compute how a prospect-theory chooser values a simple gamble, how much it needs to be paid to accept one, and why the Ellsberg choice cannot be explained by any probability.

### Given model

Value of a gain x: v(x) = x^0.88. Value of a loss −x: v(−x) = −2.25 × x^0.88. For a 50:50 gamble, use weights of 0.5 on each outcome (ignore probability weighting in this lab).

### Procedure

1) Compute the expected value of a coin flip that wins 110 or loses 100. (Check: +5.) Compute its prospect-theory value. (Check: 110^0.88 = 62.58, 100^0.88 = 57.54, value = −33.45.) Would the chooser accept?
2) How large must the gain G be for the chooser to accept a 50:50 gamble to win G or lose 100? (Check: G = 100 × 2.25^(1/0.88) ≈ 251.) Compare with what people actually demand in such experiments (about twice the loss).
3) Framing: 600 people are at risk. Program A saves 200 for certain; Program B saves all 600 with probability 1/3 and none with probability 2/3. Compute expected lives saved for each. (Check: 200 and 200.) Now restate both programs as lives lost. Using the shape of v(x) (concave for gains, convex for losses), explain why people choose A in the first frame and B in the second.
4) Ellsberg: Urn 1 has 50 red and 50 black balls; Urn 2 has 100 balls in an unknown mix. Most people prefer to bet on red from Urn 1, and also prefer to bet on black from Urn 1. Let p be a person's belief about the probability of red in Urn 2. Show that preferring Urn 1 for red requires p < 0.5 and preferring Urn 1 for black requires p > 0.5, so no single belief explains both choices.
5) Write 6-10 sentences: why might an animal weight losses more than gains, why might it avoid ambiguity, and what the amygdala patients of De Martino and colleagues add to the argument? Note Gal and Rucker's caution about how general loss aversion is.

## Lab 8.4 - Now or Later (discounting and preference reversal)

### Purpose

To compute hyperbolic and exponential discounting for one pair of rewards and find when, and whether, preference reverses.

### Given model

A smaller reward of 100 arrives on day 30; a larger reward of 110 arrives on day 31. Seen from day t, the delays are 30 − t and 31 − t.
Hyperbolic: V = A / (1 + kD), with k = 0.2 per day.
Exponential: V = A × e^(−rD), with r = 0.05 per day.

### Procedure

1) Hyperbolic, seen from day 0: value of each reward. (Check: 14.29 and 15.28; the larger, later reward is preferred.)
2) Hyperbolic, seen from day 30: (Check: 100 and 91.67; the smaller, sooner reward is preferred.)
3) Find the day on which the two hyperbolic values are equal. (Check: day 25.) Sketch both curves, as in Figure 8.5.
4) Exponential: show that the ratio of the larger to the smaller value is 1.1 × e^(−0.05) ≈ 1.046 on every day, so preference never reverses.
5) For hyperbolic discounting, find the smallest k for which preference on day 30 favors the 100 now. (Check: k > 0.1 per day.)
6) Write 6-10 sentences: why a plan made on day 0 fails on day 30, what Kidd and colleagues' reliable and unreliable experimenters imply about what k measures, and one strategy (a commitment device) that a person who knows they discount hyperbolically could use on day 0.

## Lab 8.5 - The Unlucky First Draw (explore or exploit)

### Purpose

To see how a greedy chooser can lock onto the worse option after one unlucky outcome, and how an uncertainty bonus rescues it.

### Given model

Two options. Option A pays, in order: 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 5, 5 (average 5). Option B pays, in order: 4, 9, 8, 7, 6, 9, 8, 7, 6, 8, 7, 7 (average about 7). Each option's estimate is the mean of its own payoffs so far. Play 12 trials. Trial 1 is A; trial 2 is B.
Greedy: from trial 3, choose the option with the higher estimate (ties go to A).
Uncertainty bonus: from trial 3, choose the option with the higher estimate + 2 × square root of (ln t / n), where t is the trial number and n is how many times that option has been chosen.

### Procedure

1) Greedy: list the choices and the total payoff. (Check: A, B, then A on every trial; total 60; B's estimate stays at 4.)
2) Uncertainty bonus: compute both scores on trials 3 to 6 and list all choices. (Check: trial 3, A 8.10 vs B 6.10; trial 4, A 6.67 vs B 6.35; trial 5, A 6.46 vs B 6.54, so B is tried again; trial 6, A 6.55 vs B 8.39. Choices: A, B, A, A, B, B, B, B, B, B, B, B; total 79.)
3) Why does the bonus shrink for an option as it is chosen, and why does it grow slowly for an option that is not chosen?
4) Change the bonus weight from 2 to 0.5 and repeat trials 3 to 6. Does the chooser still discover B? (Check: no; it chooses A from trial 3 to the end and earns 60, like the greedy chooser.) What does the weight represent?
5) Wilson and colleagues found that people explore more when more trials remain. How would you build that into the rule?
6) Write 6-10 sentences: relate the bonus to directed exploration and to norepinephrine's role in Chapter 3, explain why random exploration is cheaper but less efficient, and say what the dorsal anterior cingulate foraging neurons of Hayden and colleagues are computing in this language.

## Lab 8.6 - Goal or Habit? (devaluation in two learners)

### Purpose

To reproduce the logic of the devaluation test: a model-based learner adjusts at once when an outcome loses its value; a model-free learner keeps acting until it has experienced the change.

### Given model

Lever L produces food (value 10); lever R produces water (value 6).
Model-free learner: caches Q(L) and Q(R), each starting at 0, updated after each experience by Q ← Q + 0.5 (outcome value − Q).
Model-based learner: knows which lever produces which outcome and computes each lever's value from the current value of its outcome.
Training: six presses of each lever.

### Procedure

1) Train the model-free learner. (Check: Q(L) = 9.84, Q(R) = 5.91.) Which lever does each learner prefer?
2) Devaluation: food is paired with illness and its value becomes 0. Without any further lever pressing, what does each learner now prefer? (Check: model-based prefers R at once; model-free still prefers L, Q(L) = 9.84.)
3) The model-free learner now presses L four times and receives the devalued food each time. Tabulate Q(L). (Check: 4.92, 2.46, 1.23, 0.62.) After which press does it switch to R?
4) In the real devaluation test no outcome is delivered at all. What does the model-free learner do then, and what does that correspond to in Figure 8.7?
5) Daw, Niv, and Dayan propose that control goes to whichever system is less uncertain. Why would the model-free system become the more reliable one after extended training, and why does that make habits rational?
6) Write 6-10 sentences: which striatal regions correspond to each learner, what de Wit and colleagues' failures mean for the human evidence, and what Gillan's compulsivity result suggests about disorders of control.

## Lab 8.7 - From Evidence to Action (concept map)

### Purpose

To integrate the chapter on one page: how a decision is formed, valued, made, and learned from.

### Procedure

1) Draw the pipeline of Figure 8.1: sensory evidence, accumulation to a bound, valuation (with the body as an input from Chapter 7), selection in the basal ganglia (Chapter 4), action, outcome, and prediction error (Chapter 3).
2) Mark where each uncertainty enters: noisy evidence, uncertain values, unknown probabilities (ambiguity), and the unknown future (delay).
3) Add the bound and the three things that move it: conflict (subthalamic nucleus), urgency, and the cost of errors.
4) Add a confidence readout from the accumulator and an arrow labeled "opt out or change of mind".
5) Draw the two controllers (model-based and model-free) feeding the basal ganglia, with the arbitration rule written beside them, and a third, Pavlovian arrow that can override both.
6) Add an exploration knob on the selection stage, with norepinephrine and the horizon as inputs.
7) Write a 10-14 sentence caption that follows one real choice, such as deciding whether to take an umbrella or which route to drive to work, through every stage, naming the mechanism, the bias it shows, and what would go wrong if one component failed.
