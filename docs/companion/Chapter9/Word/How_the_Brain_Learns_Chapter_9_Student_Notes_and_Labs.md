---
title: "Chapter 9 Student Notes and Labs"
subtitle: "Habits, Skills, and Automaticity: How Practice Turns Choices into Routines"
---

# Student Notes

## What this chapter is for

Chapter 8 closed on habits that have outlived their reasons. Chapter 9 asks what practice does to an action, in which circuits, and at what price: how a choice becomes a routine and a clumsy movement becomes a skill.

If you come from software or machine learning, the chapter is designed to correct three instincts:
1) treating "learning a skill" as one process, rather than several (recalibration, chunking and handover, cortical rewiring) running in different circuits with different teaching signals,
2) treating automaticity as a faster algorithm, rather than as the replacement of computation by retrieval, with the brittleness that implies, and
3) treating motor variability as noise to be minimized, rather than as exploration that a reinforcement signal can select from.

Your goal is to be able to explain the shape of practice curves, the difference between a habit and a skill, how adaptation works and why it is not skill, what a chunk is and how the striatum marks one, how control moves from associative to sensorimotor circuits, what changes in motor cortex, what is and is not known about offline gains, what automaticity buys and costs, how practice should be scheduled, and what each of these implies for artificial systems.

## What practice changes

- Crossman's cigar-machine operators kept getting faster for years, over millions of cigars, until they approached the machine's cycle time (Crossman 1959).
- Whitehead: operations of thought are like cavalry charges, limited and costly; the economy of Chapter 8's "Thinking Is Costly".
- Thesis: practice (1) recalibrates movements (cerebellum, Chapter 4), (2) binds actions into units and hands their control to circuits that execute (basal ganglia and dopamine, Chapter 3), with dopamine grading the variations practice produces, and (3) builds and protects new connections in cortex. The result, automaticity, is fast, consistent, cheap in attention, and hard to inspect or change.

## The shape of practice

- On log-log axes, time per trial often falls along a straight line until it meets a floor: the power law of practice (Newell and Rosenbloom 1981) (Figure 9.1). Each doubling of practice buys about the same proportional gain.
- Averaging across people can manufacture a power function; individual curves are often exponential (Heathcote, Brown and Mewhort 2000).
- Stages: cognitive, associative, autonomous (Fitts and Posner 1967); telegraphers' "hierarchy of habits" from letters to words to phrases (Bryan and Harter 1899).

## Habits and skills

- Habit: triggered by a situation, insensitive to devaluation (Chapter 8). Skill: a shift of the whole speed-accuracy curve, faster at the same accuracy or more accurate at the same speed (Reis 2009; Shmuelof 2012; Krakauer 2019).
- Both are procedural memory and survive amnesia: H.M. improved at rotary pursuit (Corkin 1968). Amnesic patients learned the weather prediction task, at least early in training, while Parkinson's patients remembered the sessions and failed to learn (Knowlton, Mangels and Squire 1996); amnesic patients learn a hidden repeating sequence (Nissen and Bullemer 1987; Reber and Squire 1994).

## Recalibration

- Force-field reaching: errors shrink with practice; switching the field off produces a mirror-image aftereffect (Shadmehr and Mussa-Ivaldi 1994).
- Prism throwing: cerebellar and inferior-olive patients fail to adapt (Martin 1996).
- Adaptation is driven by sensory prediction error, not task failure (Tseng 2007). Mazzoni and Krakauer (2006): an explicit aiming strategy works at once, but implicit recalibration keeps correcting and drives the cursor off target. Explicit strategy carries the fast part, implicit recalibration the slow part (Taylor, Krakauer and Ivry 2014).
- Two-state model: fast process (learns and forgets quickly) plus slow process (learns slowly, holds on) explains spontaneous recovery after brief counter-adaptation in error-clamp trials (Smith, Ghazizadeh and Shadmehr 2006) (Figure 9.2). It explains some savings, but not savings after full washout, which depend partly on recalling an explicit strategy (Zarahn 2008; Haith 2015).
- Other teachers: use-dependent learning, a bias toward repeated movements (Diedrichsen 2010); reward-based learning, which cerebellar patients can still use (Therrien, Wolpert and Bastian 2016).
- Adaptation returns performance to baseline under new conditions; skill is new capability, a slower process (Krakauer 2019; Diedrichsen and Kornysheva 2015).

## Chunking

- Lashley's problem of serial order: sequences are too fast to be chains of reflexes; they are planned as wholes (Lashley 1951).
- Chunks in memory: about seven items (Miller 1956), nearer four on later estimates (Cowan 2001). Chess masters recall real positions, not random ones (Chase and Simon 1973). A runner raised his digit span from 7 to 79 by coding digits as running times, after more than 230 hours; his letter span stayed near six (Ericsson, Chase and Faloon 1980).
- Motor chunks: people spontaneously group key-press sequences, and breaking their own chunks hurts most (Sakai, Kitaguchi and Hikosaka 2003). Over three days, sensorimotor putamen activity rose with chunk concatenation and frontoparietal cortex with segmentation (Wymbs 2012).
- Task-bracketing: with extended training, striatal activity concentrates at the start and end of a maze run (Jog 1999; Barnes 2005) (Figure 9.3), tied to the onset of devaluation insensitivity (Smith and Graybiel 2013). Start/stop signals in striatum and substantia nigra emerge during sequence learning (Jin and Costa 2010); the direct and indirect pathways divide parsing and concatenation (Jin, Tecuapetla and Costa 2014). Habits as chunked sequences (Dezfouli and Balleine 2012). A chunk is cheap to select and cannot be revised in the middle.

## From planning circuits to doing circuits

- Rotarod skill: dorsomedial striatum engaged early, dorsolateral later; late potentiation in dorsolateral indirect-pathway neurons; DMS lesions impair early sessions only, DLS lesions throughout (Yin 2009).
- In people, activity moves from the associative striatum to the posterior putamen over weeks (Lehéricy 2005).
- Dopamine depletion in dorsolateral striatum prevents habit formation (Faure 2005). The striatonigrostriatal spiral links ventral, associative, and sensorimotor loops (Haber, Fudge and McFarland 2000) (Figure 9.4).
- Silencing infralimbic cortex releases a habit; after a new habit forms, silencing it restores the old one (Smith 2012): habits are continuously permitted.
- Motor cortex lesions after training spare a learned lever-press skill; before training they prevent learning (Kawai 2015). The sensorimotor striatum controls the learned kinematics without cortical input (Dhawale 2021; Wolff 2022).
- Debate: the striatum trains cortex, and automatic performance is cortico-cortical (Ashby, Turner and Horvitz 2010), against cortex training subcortical circuits. Shared principle: the circuits that learn a skill are not the circuits that run it.

## Variability as exploration

- People with more task-relevant variability learned faster (Wu 2014), not consistently replicated for error-based learning (He 2016).
- Songbirds: silencing LMAN removes juvenile song variability (Ölveczky, Andalman and Fee 2005); adult Bengalese finches shift a syllable's pitch away from noise within hours (Tumer and Brainard 2007); VTA dopamine neurons projecting to Area X signal whether a rendition was better or worse than expected (Gadagkar 2016). A reinforcement-learning loop: vary, evaluate, bias (Fee and Goldberg 2011) (Figure 9.5).

## The cortex rewires

- Motor maps: finger representation expands in squirrel monkeys learning pellet retrieval (Nudo 1996); five days of piano practice enlarge TMS maps, and imagined practice does too, less (Pascual-Leone 1995); string players' left-hand finger representation in somatosensory cortex is enlarged (Elbert 1995).
- Spines: new spines form within an hour of reach training and a fraction persist for months (Xu 2009) or for life (Yang, Pan and Gan 2009); shrinking learning-induced spines with light disrupts the skill (Hayashi-Takagi 2015).
- Caution: controlling for speed, little change in human primary motor cortex after five weeks, clearer change in premotor and parietal cortex (Berlot, Popp and Diedrichsen 2020).

## Learning between sessions

- About 20 percent overnight gain in finger tapping after sleep (Walker 2002), largely explained by fatigue, time of day, and averaging (Rickard 2008; Brawn 2010; Pan and Rickard 2015).
- Micro-offline gains: early improvement happens in ten-second rests (Bönstrup 2019), with compressed replay in hippocampus and sensorimotor cortex (Buch 2021); or recovery from short-lived fatigue (Gupta and Rickard 2022). Unresolved.

## Automaticity

- James (1890): habit diminishes conscious attention.
- Consistent mapping produces automatic detection; varied mapping stays effortful; reversed roles interfere for a long time (Schneider and Shiffrin 1977; Shiffrin and Schneider 1977). Stroop interference (Stroop 1935).
- Logan's instance theory: a race between the procedure and retrieval of stored instances; under simple assumptions it predicts the power law and shrinking variability (Logan 1988, 1992) (Figure 9.6). Automaticity replaces computing with remembering.
- Attending to an automatic skill hurts experts and helps novices (Beilock 2002); choking (Beilock and Carr 2001); implicitly learned putting survives pressure (Masters 1992); prefrontal activity declines as dual-task cost vanishes (Poldrack 2005).

## How practice should be practiced

- About 10,000 hours of solitary practice among the best violinists (Ericsson, Krampe and Tesch-Römer 1993), popularized as a rule (Gladwell 2008); meta-analysis: about 12 percent of variance (Macnamara, Hambrick and Oswald 2014); a double-blind replication found a smaller effect (Macnamara and Maitra 2019).
- Contextual interference: random practice is worse during acquisition and better at retention and transfer (Shea and Morgan 1979) (Figure 9.7); desirable difficulties (Schmidt and Bjork 1992); smaller in applied settings (Brady 2004).
- Varied warm-up beat specific warm-up at the specific distance (Kerr and Booth 1978); schema theory (Schmidt 1975).

## Habits in daily life

- About 43 percent of daily actions are repeated almost daily in the same place (Wood, Quinn and Kashy 2002).
- New habits: 18 to 254 days to reach 95 percent of the plateau, median 66; a missed day matters little (Lally 2010).
- Habitual cinema-goers eat stale popcorn as readily as fresh, only in the cinema and only with the dominant hand (Neal 2011). Overtraining alone has often failed to produce habits in people (de Wit 2018). Changing context opens a window for change (Wood and Rünger 2016; Verplanken and Wood 2006).

## When routines go wrong

- Parkinson's disease: earliest dopamine loss in the posterior putamen; loss of automatic control (Redgrave 2010); automaticity possible with more training and activity (Wu and Hallett 2005); floor markers normalize stride (Morris 1996).
- Musician's dystonia: about 1 percent of professional musicians (Altenmüller and Jabusch 2010); Leon Fleisher (Fleisher and Midgette 2010); repetitive squeezing in monkeys blurs finger maps (Byl, Merzenich and Jenkins 1996).
- Addiction as habit (Everitt and Robbins 2005, 2016) against addiction as excessive goal-directed choice (Hogarth 2020).

## Implications for artificial intelligence

1) Search turned into reflex: AlphaGo Zero's network learns to reproduce its own search (Silver 2017); expert iteration (Anthony, Tian and Barber 2017); distilling reasoning into direct answers (Deng 2023).
2) Cached answers are brittle when the goal changes, like habits after devaluation.
3) Varied practice generalizes: domain randomization (Tobin 2017; OpenAI 2019), as Kerr and Booth's beanbags.
4) Skills accumulate in the brain with limited interference (Brashers-Krug 1996); networks forget catastrophically without protection (Kirkpatrick 2017).
5) The slow system interrupts the fast one; machines rarely decide for themselves when to switch.

## Practical summary

- Practice curves are steep then shallow and keep improving long after it feels finished.
- Adaptation recalibrates through sensory prediction error in the cerebellum; skill is a shifted speed-accuracy curve.
- The striatum chunks sequences and brackets them; control moves from associative to sensorimotor loops, with dopamine.
- Motor cortex tutors learning and builds a few lasting synapses; it may not be needed to execute.
- Automaticity is retrieval replacing computation; it frees attention and resists change.
- Varied and interleaved practice is harder and teaches more.
- Habits are cued by context and permitted continuously by cortex.

# Labs

## Lab Notes: how to succeed in these labs

These labs turn the chapter's models into short calculations: the law of practice, adaptation at two timescales, automaticity as a race between computing and remembering, chunking in a timed sequence, skill as a shift in the speed-accuracy trade-off, and habit strength surviving devaluation. Each isolates one idea. The arithmetic is light; the point is to watch the rule behave and to ask what the learner gains and loses by it.

General rules:
1) Write every intermediate value, rounded to two decimal places unless told otherwise. Where a lab carries values forward from row to row, keep three decimals while computing; your answers may then differ from the check values by 0.01.
2) Draw the process or curve before computing.
3) End with an interpretation: what would change if a parameter changed, and what does the learner gain or lose?

### What to hand in for every lab

- A table of values.
- A diagram or sketch where requested (a photo of a hand drawing is fine).
- A short interpretation (6-12 sentences).

## Lab 9.1 - The Law of Practice (power functions on log axes)

### Purpose

To see why practice curves look like plateaus on ordinary axes and like straight lines on logarithmic ones, and what a floor does to the line.

### Given model

Time per trial after N trials of practice: T(N) = 20 × N^(−0.4) seconds.
A second learner has a floor: T(N) = 2 + 18 × N^(−0.5) seconds.

### Procedure

1) Compute T for the first learner at N = 1, 10, 100, 1000. (Check: 20.00, 7.96, 3.17, 1.26 s.)
2) Plot the four points on ordinary axes, then plot log10(T) against log10(N). What is the slope of the second plot? (Check: −0.4, the exponent.)
3) By what factor does T shrink each time practice doubles? (Check: 2^(−0.4) = 0.758, about a quarter faster per doubling, at any stage.) How many trials does it take to fall from 20 s to 10 s, and from 20 s to 5 s? (Check: about 5.7 and 32 trials.)
4) Compute the second learner's T at N = 1, 10, 100, 1000, 10000. (Check: 20.00, 7.69, 3.80, 2.57, 2.18 s.) Plot it on log-log axes. Where does it stop being straight, and why?
5) Heathcote, Brown, and Mewhort showed that averaging different individual curves can produce a power function. Sketch two exponential curves with different rates and their average, and explain in two sentences why the average flattens more slowly than either.
6) Write 6-10 sentences: what Crossman's cigar makers show about when learning stops, what the floor represents for them, and what it would mean for a skill to have a floor set by the body rather than by a machine.

## Lab 9.2 - Two Timescales of Adaptation (savings and spontaneous recovery)

### Purpose

To run the two-state model of Smith, Ghazizadeh, and Shadmehr by hand and watch spontaneous recovery appear.

### Given model

On each trial the movement output is x = xf + xs, the sum of a fast and a slow process. The error is e = p − x, where p is the perturbation (+1 or −1). When feedback is withheld (an error-clamp trial), e = 0.
After each trial: xf ← 0.5 × xf + 0.4 × e and xs ← 0.95 × xs + 0.1 × e. Both start at 0.
Schedule: trials 1-10, p = +1; trials 11-12, p = −1; trials 13-16, no feedback (e = 0).

### Procedure

1) Tabulate trial, p, xf, xs, x, and e for all 16 trials (values at the start of each trial). (Check: trial 2: xf = 0.40, xs = 0.10, x = 0.50; trial 10: xf = 0.30, xs = 0.34, x = 0.65.)
2) Which process carries most of the adaptation early, and which late? At which trial does the slow process overtake the fast one? (Check: trial 9.)
3) After the two opposite trials, what is the output at the start of trial 13? (Check: xf = −0.52, xs = 0.10, x = −0.42.)
4) Continue through the four no-feedback trials. (Check: x = −0.42, −0.16, −0.04, 0.02, and 0.05 after trial 16.) Explain why the output drifts back toward the first adaptation even though nothing is being learned.
5) Savings: if the +1 perturbation is now reintroduced, would this learner relearn faster than at trial 1? Use the value of xs to explain.
6) Write 6-10 sentences: which brain structure is thought to do this learning, what kind of error drives it (Tseng; Mazzoni and Krakauer), and why adaptation, which returns performance to where it was, is not the same as learning a new skill.

## Lab 9.3 - Remembering Instead of Computing (Logan's instance race)

### Purpose

To derive the power law of practice from instance theory, and to see when memory takes over from the procedure.

### Given model

The procedure always takes 1 second. Each stored instance can be retrieved in a random time that is exponentially distributed with mean 4 seconds. With n instances stored, the fastest retrieval is exponential with mean 4/n seconds. The response is given by whichever finishes first.
Probability that retrieval wins: P = 1 − e^(−n/4).
Mean response time: RT = (1 − e^(−n/4)) / (n/4) seconds.

### Procedure

1) Compute P and RT for n = 1, 2, 4, 8, 16, 32, 64. (Check: P = 0.22, 0.39, 0.63, 0.86, 0.98, 1.00, 1.00; RT = 0.89, 0.79, 0.63, 0.43, 0.25, 0.13, 0.06 s.)
2) For each doubling of n, compute the ratio RT(2n)/RT(n). (Check: 0.89, 0.80, 0.68, 0.57, 0.51, 0.50.) What does the ratio settle at, and what power function does that imply? (Check: 0.5 per doubling, so RT is proportional to n^(−1) once retrieval always wins.)
3) Plot log RT against log n. Where is the curve straight, and why is it curved at first?
4) The race model says nothing about whether the answer retrieved is correct. Suppose the rule of the task changes (for example, a key that meant "yes" now means "no"). What happens on the first trials after the change, and how does this relate to Shiffrin and Schneider's reversal experiment and to the Stroop effect?
5) Explain in two sentences why a child who knows that seven and five make twelve no longer counts.
6) Write 6-10 sentences: how instance theory relates to AlphaGo Zero's network learning to reproduce the moves of its own search, and what both gain and lose by replacing computation with retrieval.

## Lab 9.4 - Finding the Chunks (pauses in a learned sequence)

### Purpose

To identify chunks from the timing of a practiced sequence, as Sakai, Kitaguchi, and Hikosaka did.

### Given model

A person types a 12-key sequence. The 11 intervals between successive presses, in milliseconds, are:
Early in practice: 420, 410, 430, 415, 425, 420, 410, 430, 420, 415, 425
After practice: 150, 140, 145, 380, 150, 135, 140, 390, 145, 150, 140

### Procedure

1) Compute the total time for the 11 intervals early and late. (Check: 4,620 ms and 2,065 ms.)
2) In the late sequence, mark every interval longer than 300 ms. Where are the chunk boundaries, and how many keys does each chunk contain? (Check: boundaries after keys 4 and 8; three chunks of four keys.)
3) Compute the mean interval within chunks and between chunks. (Check: 143.9 ms and 385 ms.)
4) Graybiel's task-bracketing predicts striatal activity at the start and end of each unit. Sketch where activity would appear across the 12 presses early and late.
5) If the sequence were rearranged to keep the three chunks intact but change their order, would you expect performance to suffer more or less than if it were rearranged to split each chunk? Why?
6) Write 6-10 sentences: what Lashley's problem of serial order says about how the late sequence must be represented, what a chunk buys (speed, cheap selection), and what it costs (no revision in the middle).

## Lab 9.5 - Skill Shifts the Curve (Fitts's law)

### Purpose

To define skill as a change in the speed-accuracy trade-off rather than as speed alone.

### Given model

Fitts's law: movement time MT = a + b × log2(2D/W) seconds, where D is the distance to a target and W its width. The quantity log2(2D/W) is the index of difficulty, in bits.
Before practice: a = 0.20 s, b = 0.15 s per bit. After practice: a = 0.15 s, b = 0.10 s per bit. The distance is D = 16 cm.

### Procedure

1) Compute the index of difficulty for W = 4, 2, 1, and 0.5 cm. (Check: 3, 4, 5, 6 bits.)
2) Compute MT before and after practice for each width. (Check: before 0.65, 0.80, 0.95, 1.10 s; after 0.45, 0.55, 0.65, 0.75 s.)
3) Plot MT against target width for both, on the same axes. Is the improvement the same at every width?
4) Suppose a movement must be completed in 0.8 s. What is the smallest target that can be hit reliably before and after practice? (Check: index 4.0 bits, W = 2.0 cm before; index 6.5 bits, W = 0.35 cm after.)
5) Someone who simply moved faster after practice, with no change in a or b, would hit fewer targets. Explain why that is not skill in the sense of Reis and Krakauer.
6) Write 6-10 sentences: which circuits change when the curve shifts (motor cortex spines, striatum, cerebellum), and why a measure of speed alone could mistake a reckless learner for a skilled one.

## Lab 9.6 - When Does an Action Become a Habit? (habit strength and devaluation)

### Purpose

To reproduce Adams's result, that devaluation stops moderately trained responding but not extensively trained responding, with a model in which habits are strengthened by repetition alone (Miller, Shenhav, and Ludvig).

### Given model

Each press of lever L strengthens its habit: H ← H + 0.3 × (1 − H), starting at H = 0, so after n presses H = 1 − 0.7^n.
The drive to press a lever is its goal value plus 0.6 × its habit strength.
Before devaluation, L leads to food with goal value 1; an alternative action R (for example, exploring the cage) has goal value 0.5 and no habit.
After devaluation, the food's goal value is 0, and the animal knows it (a goal-directed system updates at once).

### Procedure

1) Compute H after n = 1 to 12 presses. (Check: 0.30, 0.51, 0.66, 0.76, 0.83, 0.88, 0.92, 0.94, 0.96, 0.97, 0.98, 0.99.)
2) After devaluation, the drive for L is 0.6 × H. For moderate training (n = 3) and extended training (n = 12), compute the drive for L and compare it with R's 0.5. (Check: 0.39 against 0.5, so the animal switches to R; 0.59 against 0.5, so it keeps pressing L.)
3) Find the smallest amount of training after which the habit alone outweighs the alternative. (Check: six presses, where 0.6 × H = 0.53; at five it is 0.50, a tie.)
4) Change the habit weight from 0.6 to 0.4. Can any amount of training now produce a habit that survives devaluation? (Check: no, because 0.4 × H never exceeds 0.4.) What might the habit weight correspond to in the brain (think of the infralimbic experiments of Smith and Graybiel)?
5) Compare this model with the model-free learner of Lab 8.6, in which habits are cached values. Which predicts that a habit can persist even when the animal has experienced the devalued outcome?
6) Write 6-10 sentences: which striatal region carries H, what the popcorn experiment of Neal and Wood adds about context, and why the failures to produce habits by overtraining in people (de Wit) might mean the human habit weight builds over months rather than hours.

## Lab 9.7 - From Choice to Routine (concept map)

### Purpose

To integrate the chapter on one page: what practice changes, where, and at what cost.

### Procedure

1) Draw three columns labeled recalibration, chunking and habit, and cortical change. Under each, name the main structure (cerebellum; striatum with dopamine; motor and premotor cortex), the learning signal (sensory prediction error; reward prediction error and repetition; use-dependent plasticity), and one experiment from the chapter.
2) Add the shift of Figure 9.4 from the associative loop to the sensorimotor loop, with the dopamine spiral, and mark where the infralimbic cortex can switch a habit off.
3) Add Logan's race: a procedure arrow and a retrieval arrow converging on the response, with the number of instances growing over practice.
4) Add the songbird loop as an inset: variation from LMAN, evaluation by dopamine, selection in Area X.
5) Mark three failure points: Parkinson's disease (loss of the sensorimotor striatum's dopamine), musician's dystonia (overlapping finger maps), and the habit account of addiction (with Hogarth's objection written beside it).
6) Write a 10-14 sentence caption that follows one real skill, such as learning to type, ride a bicycle, or play a scale, from its first deliberate attempt to automatic performance, naming the mechanism at each stage and what would be lost if that mechanism failed.
