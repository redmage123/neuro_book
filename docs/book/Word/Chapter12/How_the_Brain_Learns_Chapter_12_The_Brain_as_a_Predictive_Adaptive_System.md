---
title: "Chapter 12"
subtitle: "The Brain as a Predictive, Adaptive System: Is There One Principle Beneath the Mechanisms?"
---

> *"If the organism carries a 'small-scale model' of external reality and of its own possible actions within its head, it is able to try out various alternatives, conclude which is the best of them, react to future situations before they arise."*
>
> --- Kenneth Craik, *The Nature of Explanation* (1943)

# A Model in the Head

In 1943 a young Cambridge psychologist named Kenneth Craik published a book arguing that thinking is the manipulation of a model. A nervous system, he wrote, could carry a working model of the world and of its own possible actions, run it forward to see what would happen, and act on the result before the world had a chance to deliver it. Craik did not know how a brain could build such a model; nobody did. He spent the two years left to him on the problem, during the war, on questions as practical as how gunners track a moving target. On 7 May 1945, the day before the war in Europe ended, a car struck his bicycle on King's Parade in Cambridge, and he died the next day, at the age of 31.[^1] Craik's book is slight, and much of what these chapters have described can be read as a footnote to it.

The previous chapters met prediction everywhere: in dopamine neurons (Chapter 3), hippocampal replay (Chapters 5 and 10), sensory cortex (Chapter 6), the regulation of the body (Chapter 7), choice (Chapter 8), and movement (Chapter 9). Figure 12.1 collects these.

![Figure 12.1. Prediction across the book. Each row is a system described in an earlier chapter: what it predicts, the error signal that reports the mismatch, and what that error teaches. The rows differ in their signals, their speeds, and their cells; what they share is the comparison of an expectation with an outcome.](images/fig_prediction_map.png)

The list invites a question that this chapter takes seriously. Is prediction one principle of brain function, beneath all these mechanisms, or a word that happens to fit many different things? Some theorists, most ambitiously Karl Friston, have argued for the first: that everything the brain does, perceiving, acting, learning, and regulating, is the minimization of a single quantity. Others regard that claim as too general to be tested, or as true only in a sense that explains nothing.

The thesis of this chapter is that prediction is the brain's most general strategy, and adaptation, the continual revision of the predictions, is its counterpart; together they are as close to a principle as the brain offers. But they are a strategy implemented by many mechanisms, each shaped by the constraints of energy, time, and a body, and not a single mechanism repeated everywhere. The evidence for the strategy is strong. The evidence that one equation captures it is, so far, weak.

# Why Predict?

There are at least three reasons a brain would predict, and each would apply to any system in the brain's position.

The first is delay. Nerve signals are slow, and every stage of processing adds time. The first responses to a visual stimulus reach the primary visual cortex of a monkey about 60 to 70 milliseconds after the stimulus appears, and the later stages of the visual hierarchy respond later still.[^2] A brain that acted only on what it had already processed would be acting, always, on a world that had moved on. A ball traveling at 30 meters per second covers two meters in that time. One sign that the brain compensates is the flash-lag effect: when a flash appears beside a moving object at the same place, people see the moving object as ahead of the flash, as if the brain were projecting the motion forward to the present.[^3] Whether the effect reflects extrapolation or other mechanisms is still argued over, but the problem it addresses is not.

The clearest demonstrations come from sport. Michael Land and Peter McLeod recorded the eye movements of three cricket batsmen, from a professional to a weekend amateur, facing balls from a bowling machine. The batsmen watched the ball leave the machine and then, without tracking it, jumped their eyes to the spot on the pitch where they expected it to bounce, waited there for it, and followed it for up to a fifth of a second after it landed; what distinguished the good batsmen from the poor one was how soon after release that first jump came.[^4] They were not watching the ball so much as checking a prediction of it. A brain that must act in real time on delayed information must predict.

Delay matters most for the brain's own movements, which change its input faster than the input can be processed. The eyes jump three or four times a second, and each jump sweeps the image across the retina. Jean-René Duhamel, Carol Colby, and Michael Goldberg found that some neurons in the monkey's parietal cortex shift their receptive fields just before an eye movement, responding to a stimulus that the coming movement will bring into view before the eye has moved, and that nearly all of them respond when a movement brings into their field the place where a stimulus had been flashed, even though the stimulus is already gone.[^5] The cells update their map of space from the movement the brain has commanded, the efference copy of Chapter 6, rather than waiting for the retina to report.

The second reason is economy. Most of the world is predictable from its surroundings. Adjacent points in a natural scene usually have similar brightness, and successive moments usually resemble one another. A neuron that transmitted the raw signal would spend most of its spikes repeating what the next neuron could have guessed. In 1982 Mandyam Srinivasan, Simon Laughlin, and Ahron Dubs proposed that this is what lateral inhibition in the retina is for, borrowing a term from communications engineering, predictive coding: each point's signal is reduced by an estimate of it made from its neighbors and from its own recent past, and what is passed on is the error, the part that could not be predicted.[^6] Figure 12.2 shows the effect on a signal with the statistics of a line through a natural image. Subtracting the average of each point's two neighbors leaves an error whose variance is about five times smaller than the signal's; the same information can be sent with a smaller range of responses, and therefore more precisely, with the same noisy neurons. This was 17 years before predictive coding was proposed for the cortex, in the model that Chapter 6 described.[^7]

![Figure 12.2. Predictive coding in the retina, after Srinivasan, Laughlin, and Dubs (1982) (simulation). A: a fluctuating intensity along a row of photoreceptors, with the statistics of a line through a natural image (blue), and the same signal after each point's two neighbors' average has been subtracted (red), the part a neighbor could not predict. B: the distribution of each. The error has about one-fifth of the signal's variance, so it can be transmitted with a narrower range of responses.](images/fig_retina.png)

The third reason is regulation. Chapter 7 described a body regulated ahead of need: insulin released at the sight of food, breathing raised at the start of exercise, hunger neurons quieted by the sight of a meal not yet eaten. The same laboratory that found the hunger neurons found that thirst neurons in the mouse brain fall silent within seconds of drinking, long before the water could have changed the blood, and are activated by eating, in anticipation of the salt and water balance the meal will soon disturb.[^8] Peter Sterling, whose allostasis Chapter 7 described, has argued that this, predictive regulation rather than reaction, is the main business of the brain.[^9]

# Matching the World's Statistics

To predict a signal, a system must know its statistics, and the best evidence that neurons do comes from a fly. In 1981 Laughlin measured the contrasts in natural scenes of the kind a blowfly sees and found how often each level of contrast occurred. He then recorded from the large monopolar cells, the neurons that receive the fly's photoreceptor signals, and measured how their responses grew with contrast. The two curves matched. The neurons' response to each contrast was the cumulative frequency of that contrast in the fly's world, so that each of the neurons' response levels was used about equally often.[^10]

This is the design that a communications engineer would choose. A neuron has a limited range of firing rates and is noisy within it. If its response were a straight line of contrast, most of its range would be spent on contrasts that rarely occur, and the common small contrasts would be crowded into a few response levels. Matching the response curve to the distribution spreads the common contrasts across the range, and Figure 12.3 shows the gain. With ten distinguishable response levels, the matched curve carries 3.3 bits about each contrast and a straight line 2.3. Horace Barlow had proposed in 1961 that sensory neurons are organized to remove redundancy in this way, and Laughlin's fly was the first direct confirmation.[^11]

![Figure 12.3. Matching a response curve to the world, after Laughlin (1981) (simulation). A: an illustrative distribution of contrasts, in which small contrasts are common and large ones rare. B: a response curve shaped like the cumulative distribution (blue) uses all ten response levels equally and carries 3.3 bits per contrast; a linear response (red) carries 2.3, because most contrasts fall in a few of its levels.](images/fig_equalize.png)

A fixed match would be fragile, because the world's statistics change, and the brain's match changes with them. Naama Brenner, William Bialek, and Rob de Ruyter van Steveninck recorded from H1, a motion-sensitive neuron in the fly, while the visual motion it saw changed in strength. When the motion became more variable, the neuron's input-output curve stretched to cover the new range; when the motion calmed, it contracted, so that the cell kept using its full range of responses.[^12] Adrienne Fairhall and the same group then found that after a change the information the neuron carried recovered within about a tenth of a second, while its firing rate went on adjusting for a minute, as if the neuron were estimating the statistics of its input on several timescales at once.[^13] Adaptation of this kind is not fatigue. It is the continual revision of a prediction about what the next input will be like. Over longer periods, adaptation often follows a power law in time, the signature of many timescales operating at once, sometimes within a single neuron.[^14]

Adaptation shows itself most plainly when a prediction outlives the world it was fitted to. In 1834 Robert Addams described what he saw at the Falls of Foyers, on the shore of Loch Ness. Having looked for a few seconds at the cascade and then turned his eyes to the rock face beside it, he "saw the rocky surface as if in motion upwards, and with an apparent velocity equal to that of the descending water." He blamed an involuntary movement of the eyeball. The motion aftereffect, as it is now called, is the classic case of a sensory system adjusted to a sustained input. Neurons tuned to the direction of the falling water reduce their responses, and when the motion stops, the balance between neurons tuned to opposite directions tips the other way.[^15] The rocks are not moving; the brain has recalibrated its expectation of motion to a world that has changed.

The fly's neurons are matched to the present statistics of their input. A stronger claim is that early sensory neurons encode the future. Stephanie Palmer, Olivier Marre, Michael Berry, and Bialek recorded from dozens of ganglion cells in a salamander's retina while a bar moved in a jittery but partly predictable way. Nearly every cell belonged to some small group whose spikes carried almost as much information about where the bar would be next as any code could, given how much the bar's past revealed about its future.[^16] Matthew Chalk, Marre, and Gašper Tkačik then brought efficient coding and coding for the future into one framework, in which whether a neuron should decorrelate its input, or respond sparsely, depends on the statistics of the input and on whether the code is for recovering the past or predicting what comes next.[^17] That is this chapter's thesis in miniature: one strategy, with its implementation tuned to circumstance.

# Prediction at Every Level

The same strategy appears wherever the brain has been examined closely enough, and three examples not yet met in this book show how far it reaches.

The first is the hippocampus. Chapter 4 described place cells, each active when an animal is in one part of its environment. Mayank Mehta, Carol Barnes, and Bruce McNaughton recorded place cells while rats ran repeatedly in one direction along a track and found that each cell's field grew backward, against the direction of travel, over the first laps of each session: a cell that had fired only at one spot came to fire earlier, as the rat approached it.[^18] Kimberly Stachenfeld, Matthew Botvinick, and Samuel Gershman explained the asymmetry by proposing that the hippocampus encodes not where the animal is but where it is likely to go: a predictive map in which each location is represented by the locations expected to follow it, a construction from reinforcement learning called the successor representation.[^19]

Figure 12.4 shows why such a map produces the backward growth. If the animal always runs one way, a location is predicted by the places just before it, and a cell for that location becomes active as the animal approaches. The same theory accounts for some features of grid cells, and it unites the hippocampus's two roles, in memory and in navigation, as two uses of one model of what follows what.

![Figure 12.4. A predictive map on a linear track (computed). Each curve shows the activity, at every position, of a cell representing one location (dotted line) in a successor representation: how strongly the animal's current position predicts a future visit to that location. A: an animal that wanders in both directions; the fields are symmetric. B: an animal that runs from left to right; each field extends backward, toward the places from which the location is reached, as Mehta and colleagues observed in rats.](images/fig_successor.png)

People appear to use such maps too. Ida Momennejad, Gershman, and their colleagues taught people sequences of states that led to rewards and then changed either the rewards or the sequences. People adjusted to changed rewards more readily than to changed sequences, the asymmetry a predictive map produces, since a map of what follows what must be relearned when the sequence changes but not when only the rewards do. Yet people did adjust to changed sequences, if less well, and the authors concluded that they combine such a map with deliberate planning.[^20] Mona Garvert, Raymond Dolan, and Behrens showed people a stream of objects whose order followed hidden rules, and found that the hippocampus and entorhinal cortex represented each object according to which objects were likely to follow it, a structure the participants could not report.[^21]

The second is the cortex of a running mouse. Georg Keller, Tobias Bonhoeffer, and Mark Hübener placed mice on a ball in front of screens that showed a corridor moving past as the mouse ran, so that the visual flow was coupled to the mouse's own movement. Occasionally they stopped the flow for a moment while the mouse kept running. Many neurons in the primary visual cortex responded strongly to these halts, which were not stimuli at all but the absence of the motion that the running predicted.[^22] Alexander Attinger, Bo Wang, and Keller then raised mice in darkness and gave them visual experience only in a virtual world, in which the flow either followed their running or moved independently of it. Strong mismatch responses developed only in the mice whose world had moved with them.[^23] The prediction that visual flow follows running is not built into visual cortex. It is learned, from the coupling between movement and sight, as the infant's world teaches it.

The third is language. In 1980 Marta Kutas and Steven Hillyard recorded electrical activity from the scalps of people reading sentences one word at a time. When a sentence ended with a word that made no sense, as in "he spread the warm bread with socks", a negative wave peaked about 400 milliseconds after the word, which they called the N400.[^24] More than 40 years of work since have shown that the wave tracks not nonsense as such but expectation: it is smaller for any word that the preceding words made probable and larger for one they made improbable, even when both are perfectly sensible.[^25] Whether that reflects a word predicted before it arrives or one more easily fitted in after it does has been argued over for decades; a replication in nine laboratories with 334 participants confirmed the effect of how expected a noun is but not the best-known evidence that readers anticipate the word itself, a change in the wave at the article "a" or "an" that precedes an expected noun.[^26] Either way, the brain's sensitivity to how expected each word is was found a generation before the language models of Chapter 10, which are trained on nothing else.

In each case the prediction is learned from experience, compared with what arrives, and revised when it fails. The three examples differ in almost everything else: the cells, the timescales, the content of the prediction, and the signal that reports its failure.

# Many Errors, One Form

The errors of Figure 12.1 are not one signal. Chapter 6 distinguished the dopamine neuron's error, a single number about value, from the feature-by-feature errors of sensory cortex, and the cerebellum's error arrives on climbing fibers, one to each Purkinje cell, and says which movement went wrong.

What they share is a form. Each compares a prediction with an outcome and changes something in proportion to the difference. The simplest learning rule of this kind, the error-correcting rule beneath Chapter 3's temporal-difference learning, is called the delta rule: the new estimate is the old one plus a fraction of the error. The fraction, the learning rate, is the interesting part. If the world is stable and the observations are noisy, the learning rate should be small, so that each noisy observation moves the estimate only a little. If the world has just changed, it should be large, so that the old estimate is abandoned quickly. No fixed rate can do both.

The solution, worked out for engineering problems by Rudolf Kalman in 1960, is to make the learning rate depend on uncertainty: large when the learner is unsure of its estimate relative to the noise in its observations, small when it is sure.[^27] Matthew Nassar, Joshua Gold, and their colleagues asked people to predict where the next of a series of numbers would fall, while the numbers' average jumped from time to time without warning. People's learning rates rose after a jump and then fell as the new average was confirmed, as an approximately optimal learner's would.[^28] The same group also found that the size of people's pupils, which reflects arousal systems including the noradrenergic system of Chapter 3, tracked the model's estimates of how likely a change had been and how uncertain the current estimate was, and together these pupil measures predicted each trial's learning rate.[^29] In a later version of the task, people placed a bucket to catch bags dropped from a helicopter hidden behind clouds, which now and then moved without warning; separate brain regions tracked the influence of surprise and of uncertainty on how much each bag changed where people put the bucket.[^30]

Figure 12.5 shows such a learner. It tracks the jumps almost as quickly as a learner with a high fixed rate and holds steady between them almost as well as one with a low rate; over 100 simulated runs its average error was 20, against 23 for the best fixed rate.

Who sets the rate in the brain is less clear. People adjust their learning rate to the volatility of the world (Chapters 8 and 11), and on Angela Yu and Peter Dayan's account (Chapter 6) acetylcholine reports the expected uncertainty of a noisy but stable world and norepinephrine the unexpected uncertainty of one that has changed.[^31] Christoph Mathys and his colleagues built a hierarchy of such learners, each level estimating how fast the level below is changing, so that the volatility of the world is itself learned.[^32]

![Figure 12.5. An adaptive learning rate, after Nassar and colleagues (2010) (simulation). A: noisy observations (gray dots) of a hidden mean (black) that jumps at random. A learner with a low fixed rate (gold) is precise but slow to follow jumps; one with a high fixed rate (gray) follows quickly but is buffeted by noise. A learner that knows how often the mean jumps and how noisy the observations are, and whose rate rises when an observation is improbable under its current estimate (red), does both. B: the adaptive learner's rate, which spikes after each jump and decays as the new mean is confirmed. Over 100 simulated runs, root-mean-square errors were 36 (rate 0.1), 23 (rate 0.6), and 20 (adaptive).](images/fig_learning_rate.png)

A learning rate set by uncertainty is the clearest single candidate for what all the brain's error signals have in common. It is an idea about how to learn from prediction errors, not about what to predict, and it applies whatever the cells and signals that implement it.

The claim that the brain learns as an ideal learner would deserves the same scrutiny this chapter will give the free-energy principle. Jeffrey Bowers and Colin Davis argued that Bayesian models in psychology and neuroscience are too easily adjusted: the priors, likelihoods, and costs can be chosen after the data are in, so that almost any behavior can be described as optimal, and the models rarely predict better than simpler ones. Thomas Griffiths and his colleagues replied that the models are tools for asking what problem the brain is solving, not claims that it solves it perfectly.[^33] The adaptive learning rate survives the critique better than most such claims, because it predicts something a fixed-rate learner does not, a rise in learning after surprise, and people's learning rates and pupils show it. But "approximately optimal" should be read as a description of what the brain manages, not a guarantee.

# When the Learning Rate Goes Wrong

If learning well depends on weighting new evidence correctly against old beliefs, some disorders might be failures of the weighting. Chapter 6 described accounts of psychosis and autism in which priors are weighted too heavily or too lightly. Two experiments since have measured the weighting directly, using the hierarchical learner just described.

Albert Powers, Mathys, and Philip Corlett played people a faint tone at the same time as they showed a checkerboard, many times, until the two were associated. As the experiment went on, the tone was made fainter and, on more and more trials, left out altogether. Everyone sometimes reported hearing a tone that had not been played, a hallucination produced by conditioning. People who heard voices in daily life reported these conditioned hallucinations more often and with more confidence, whether they had a diagnosis of psychotic illness or not; one group of voice-hearers without a diagnosis attributed their voices to spiritual sources. Fitted to each person's responses, the model showed that the voice-hearers gave more weight to what they expected relative to what they heard. In brain scans, the conditioned hallucinations raised activity in the auditory regions that responded to real tones, along with a network including the insula and the anterior cingulate cortex that resembles the regions active when patients hallucinate.[^34]

Rebecca Lawson, Mathys, and Geraint Rees gave autistic and non-autistic adults a task in which a tone predicted whether a face or a house would appear, with a reliability that changed without warning from block to block. The autistic adults were less surprised when the tone's prediction was violated, and the model fitted to their choices showed why: they judged the world to be more volatile than it was, so that each violation seemed less informative about whether anything had changed, and those who did this most had the most severe symptoms.[^35]

Both studies are small, and neither establishes a cause. But they show what a predictive account adds to the description of a disorder. Instead of a vague claim that prediction has failed, it offers a quantity, how much weight a brain gives to what it believes against what it is told and how fast it thinks the world changes, that can be estimated in each person and compared.

# Adaptation on Every Timescale

Anyone who has spent a few days at sea knows the feeling of stepping ashore and finding the land rocking. Thomas Stoffregen and his colleagues measured it aboard a ship crossing the Caribbean. Within the first hours of the voyage, passengers new to the sea had widened their stance and changed how they swayed. On their first day back on land, most felt the ground move for half an hour or less, but about one in five felt it for two hours or more, and these were the people who had swayed most at sea.[^36] Balance had been relearned for a moving deck within hours, and unlearning it took hours more: the brain had built a prediction of the ground's motion and could not discard it at once.

Sea legs are one timescale among many. Prediction requires a model, and a model of a changing world must change. The brain revises its predictions on every timescale it has been examined at (Figure 12.6). Sensory neurons rescale their responses within a fraction of a second, as the fly's H1 did. Synapses strengthen and weaken from moment to moment through short-term plasticity, and over hours to years through the long-term changes of Chapter 5. The eye's sensitivity to light recovers over half an hour or more in the dark.[^37] Motor adaptation, Chapter 9 showed, has a fast process that learns and forgets quickly and a slow one that learns and forgets slowly. Synaptic scaling, which Chapter 5 described, adjusts all of a neuron's synapses over a day or two to keep its activity within bounds.[^38] Development opens critical periods in which a circuit takes on the statistics of its early environment, and then closes them.[^39] Evolution, on the longest scale, has built some predictions in before experience begins.

![Figure 12.6. Adaptation on every timescale (schematic; ranges approximate). Each bar shows the timescale over which a process revises the brain's predictions. Faster processes track the moment; slower ones accumulate what is reliably true; the slowest, evolution, sets the starting point for the rest.](images/fig_timescales.png)

Why so many timescales? Konrad Kording, Joshua Tenenbaum, and Reza Shadmehr gave an answer for motor adaptation that generalizes. The disturbances a body meets have different durations: fatigue lasts minutes, an injury weeks, growth years. A learner that does not know which kind of disturbance it faces should estimate all of them at once, attributing a new error mostly to the fast, likely causes and only gradually to the slow ones. They showed that such a learner reproduces spontaneous recovery, the return of an old adaptation after a new one fades, and some forms of savings, the faster relearning of an adaptation met before; Chapter 9 described both.[^40] On this view, the many timescales of plasticity are not a collection of accidents but an inference about the timescales on which the world changes.

Even long-held priors can be revised. People assume, other things being equal, that objects move slowly, which is usually true, and the assumption shows when the evidence weakens: a faint pattern looks slower than a clear one moving at the same speed. Robert Snowden and his colleagues found that drivers in a simulator whose whole scene had been reduced in contrast, as if by a uniform fog, judged their speed to be lower than it was and drove faster. Fog simulated more realistically, hiding distant objects more than near ones, has the opposite effect, and drivers in it slow down; the uniform version isolated the prior.[^41] Alan Stocker and Eero Simoncelli showed that misjudgments of speed at low contrast are what an observer with a prior favoring slow speeds would make.[^42] Grigorios Sotiropoulos, Aaron Seitz, and Peggy Seriès trained people for five days on faint patterns that moved fast, and the prior itself shifted toward faster speeds, as a change in how they judged the direction of faint moving lines revealed.[^43]

Chapter 6's light from above, which training can rotate and which chicks reared under light from below still assume, makes the same point. Chicks hatched and kept in darkness, shown moving patterns of light points for the first time, approach a pattern made by a walking animal rather than one made by random motion, whether the animal is a hen or a cat, as if they arrive expecting living things to move as living things do.[^44] Evolution sets the prior; experience can move it, within limits.

The timescales also answer the problem of Chapters 5 and 10, the balance between learning and remembering: layering fast processes on slow ones lets the brain follow the moment without losing what is reliably true.

# One Principle? The Free-Energy Principle

The most ambitious attempt to turn all this into a single principle is Karl Friston's. In a series of papers since 2005, Friston has argued that any system that keeps itself in a limited set of states, as a living thing must, can be described as minimizing variational free energy, an information-theoretic quantity distinct from the thermodynamic free energy of Chapter 0, which it can compute from its sensations and its own model and which sets an upper bound on surprise, the improbability of its sensory states under that model.[^45] Minimizing it can be done in two ways (Figure 12.7). The system can change its model so that its sensations become less surprising, which is perception and learning; or it can change its sensations so that they match its model, which is action. Friston called the second active inference. On this account, a creature moves its eyes to find what it expects, reaches for a cup to make the predicted sensation of holding it come true, and keeps its body temperature near 37 degrees because it predicts it will be there.

![Figure 12.7. Two ways to reduce a prediction error. A mismatch between the brain's predictions and what arrives from the world and the body can be reduced by changing the model, which is perception and learning, or by acting to change what arrives. The free-energy principle treats both as the minimization of one quantity.](images/fig_two_ways.png)

The attraction is obvious. One formulation covers perception, action, learning, attention (as the weighting of errors by their reliability, Chapter 6's precision), and homeostasis, and it echoes the cybernetics of W. Ross Ashby that Chapter 1 described. Andy Clark and Jakob Hohwy have built a broad philosophy of mind on it.[^46]

The objections are as serious. The first is the dark-room problem. If a creature's goal is to minimize surprise, why does it not find a dark, quiet room and stay there, where nothing surprising can happen? Friston, Christopher Thornton, and Clark replied that a creature like us expects to be fed, warm, and among others, so that a dark room, in which it would starve, is exactly what its model predicts it will avoid.[^47] The reply works, but at a price: the creature's goals must be written into its model as expectations about the states it will occupy, and the theory then explains goal-directed behavior by assuming the goals.

The second objection is that the principle, as a principle, cannot be tested. Friston has said as much: "Like Hamilton's Principle of Stationary Action, it cannot be falsified," whereas hypotheses derived from it, such as predictive coding, "may or may not be supported by empirical evidence."[^48] Mel Andrews argued that the formalism is a modeling framework, not a hypothesis about the brain, and Samuel Gershman that it is so flexible that almost any behavior can be described as minimizing free energy under some model.[^49] Jelle Bruineberg and his colleagues showed that its central device, the "Markov blanket" that separates a system from its surroundings, is used in two senses, a tool of statistics and a claim about what an organism is.[^50]

What can be tested are the specific process theories built under it, and the most specific, predictive coding in cortex, has had a mixed record. Laurence Aitchison and Máté Lengyel showed that a brain could do Bayesian inference without predictive coding and could use predictive coding without doing Bayesian inference, so evidence for one is not evidence for the other.[^51] Kevin Walsh, Redmond O'Connell, and their colleagues reviewed the neurophysiological evidence and found much of it compatible with predictive coding and its relatives, often grouped as predictive processing, but rarely decisive against alternatives.[^52] A large study recording from many visual areas at once in mice and monkeys, so far reported only as a preprint, found that responses to violations of a learned pattern appeared mainly in higher areas, not in early visual cortex, and found little sign of the suppression of predicted input that the theory requires.[^53] Yet the mismatch between movement and sight in Keller's mice does evoke responses in early visual cortex; the evidence may depend on the kind of prediction that is violated.

The principle has had direct tests, with results that show both its reach and its limits. Takuya Isomura, Friston, and their colleagues grew rat cortical neurons on arrays of electrodes and stimulated them with mixtures of two hidden signals. Over 100 sessions the cultured neurons came to respond selectively to one source or the other, separating the mixture, and a free-energy model fitted to the first ten sessions predicted how their responses and connections would change over the remaining 90.[^54] The same separation is predicted by simpler learning rules of the Hebbian kind, which the free-energy model can be read as restating; the study shows that the principle can describe what the neurons did, not that a rival account could not.

Brett Kagan and his colleagues connected cultures of mouse or human cortical neurons, hundreds of thousands of cells on each array, to a simulated game of Pong, delivering predictable stimulation when the paddle hit the ball and unpredictable stimulation when it missed, and reported that the cultures' rallies lengthened within five minutes of play, as the free-energy account predicted they would if neurons act to make their input predictable.[^55] A group of neuroscientists objected that the improvement was modest and that the paper's claim of "sentience" stretched the word beyond use.[^56] Both studies show something real: that networks of neurons, with nothing but their own plasticity, learn in ways that reduce the unpredictability of their input. Neither shows that this is all a brain does.

# What Prediction Leaves Out

A strategy that explains everything explains nothing, and it is worth being clear about what prediction does not obviously explain.

It does not say what to want. A model can predict a meal or a predator equally well; which one to seek is a matter of value, and in the free-energy account value is reintroduced as prior expectations about preferred states. Chapter 7 argued that value is anchored to a body; the anchoring is a fact about the organism, not a consequence of predicting well.

It does not say why to explore. A learner that wanted only to make its input predictable would stay where it is, but animals and children seek out what they do not yet understand. Aimee Stahl and Lisa Feigenson showed 11-month-old infants a ball that seemed to roll through a solid wall, or a toy car pushed off a ledge that seemed to hover in midair. The infants learned more about an object that had broken their expectations than about one that had not, and when they were given it to play with, they tested the expectation it had broken: they banged the ball on the table, and tended to drop the car.[^57] The surprise told them where to look; the drive to explore was their own.

Chapter 11 described the most promising account of that drive, curiosity as the pursuit of learning progress, a preference for improving predictions rather than for having good ones already. In active inference, a drive to resolve uncertainty appears as an "epistemic" part of the quantity an agent minimizes when it plans, the free energy it expects in the future.[^58] Beren Millidge and his colleagues have argued that this expected free energy cannot simply be derived from the principle as the free energy of the future, and that its exploratory part does not follow directly from it, so that exploration is assumed rather than explained.[^59]

It may not even describe the brain's evolutionary priority. Paul Cisek has argued that brains evolved as controllers, loops that keep an animal's relation to its world within useful bounds, elaborated over hundreds of millions of years, and that dividing behavior into perception, prediction, and action imposes an engineer's diagram on a system that never had one.[^60] On his view, prediction is one of the things control loops came to use, as an animal's interactions grew more complex, not the foundation they were built on.

And prediction does not explain the brain's particular form. Why it uses spikes, why it is organized in a hierarchy of areas, why it keeps a fast memory beside a slow one, and why it spends its energy as it does are questions about the constraints under which it was built, and they need answers of a different kind.

# Implications for Artificial Intelligence

The most successful artificial systems of the 2020s are predictors. A large language model is trained to predict the next word, and Chapter 10 noted how much follows from that single objective. In one sense the brain's strategy has been vindicated at enormous scale. In four senses it has not yet been copied.

First, the brain predicts the consequences of its own actions, and learns most from the mismatches its own movements create, as Keller's mice did. A language model is trained mostly to predict text it had no part in producing. The systems that learn world models of their own actions, such as the DreamerV3 agent of Chapter 10, are closer to the brain's arrangement, and Yann LeCun has proposed that machines should predict not raw data but abstract representations of it, so that they model what matters rather than every pixel, as the levels of the cortical hierarchy predict the level below rather than the retina.[^61]

Second, the brain's learning rate is governed by its uncertainty, moment by moment, as Figure 12.5 showed; a trained model's is set on a schedule, and once deployed it does not learn at all. The idea of letting each connection learn its own learning rate from the history of its errors is old in machine learning; Richard Sutton proposed one version in 1992.[^62] But it has not become part of how large models learn.

Third, the brain adapts on many timescales at once, with fast processes riding on slow ones. A deployed model has, in effect, two: the slow learning of its training, frozen, and the fast, unretained adaptation of its context window. What it lacks is everything in between, the hours, days, and years over which a brain consolidates what it has learned in use. Chapter 11 described the attempts to supply it.

Fourth, the brain learns from many errors at once, of the different kinds described above. A large model is trained mainly on one loss, next-word prediction, with further objectives, for human preferences and for correct answers, added at the end. Whether many local objectives, each fitted to its own part of the problem, would learn faster or more robustly than one global objective is a question the brain's arrangement poses directly.

The constraints under which the brain evolved, which prediction leaves unexplained, are the subject of Chapter 13.

# The Central Lesson

Craik guessed in 1943 that a brain carries a model of the world and runs it ahead of time. Eighty years of evidence has filled in his sketch. Neurons in the retina transmit what their neighbors cannot predict; neurons in the fly match their responses to the statistics of the world and rescale them as it changes; dopamine neurons, cortical neurons, the hippocampus, the cerebellum, and the circuits that regulate the body all compare what they expect with what arrives and learn from the difference, at rates set by how uncertain they are and on timescales from milliseconds to lifetimes, with evolution setting the starting point. That is as close to a single principle as the brain offers: predict, compare, and revise, with a confidence that matches the world's reliability. It is a strategy, not a mechanism, carried out by different cells with different signals for different purposes. The attempt to compress it into one equation has produced a framework that describes almost anything and a few real tests, but the strategy does not depend on the equation.

# Next Chapter

Chapter 13: Why the Brain Works the Way It Does: Constraints, Trade-offs, and the Shape of a Solution

# References and Attribution

## Figure Attribution

Figures 12.1 to 12.7 were drawn for this book. Figures 12.2 to 12.5 are computed: Figure 12.2 applies the lateral-inhibition scheme of Srinivasan, Laughlin, and Dubs (1982) to a simulated signal whose power falls in inverse proportion to frequency; Figure 12.3 applies the principle of Laughlin (1981) to an illustrative distribution of contrasts; Figure 12.4 computes the successor representation of Stachenfeld, Botvinick, and Gershman (2017) on a linear track; Figure 12.5 simulates the approximately Bayesian learner of Nassar et al. (2010) beside learners with fixed rates. Figures 12.1, 12.6, and 12.7 are schematic; the timescales in Figure 12.6 are approximate.

## Epigraph

Kenneth J. W. Craik, *The Nature of Explanation* (Cambridge University Press, 1943), chapter 5, "Hypothesis on the Nature of Thought," p. 61.

## References

Addams, R. (1834). An account of a peculiar optical phænomenon seen after having looked at a moving body. *London and Edinburgh Philosophical Magazine and Journal of Science*, 5(29), 373–374.

Aitchison, L., & Lengyel, M. (2017). With or without you: Predictive coding and Bayesian inference in the brain. *Current Opinion in Neurobiology*, 46, 219–227.

Andrews, M. (2021). The math is not the territory: Navigating the free energy principle. *Biology & Philosophy*, 36(3), 30.

Attinger, A., Wang, B., & Keller, G. B. (2017). Visuomotor coupling shapes the functional development of mouse visual cortex. *Cell*, 169(7), 1291–1302.

Balci, F., Ben Hamed, S., Boraud, T., Bouret, S., Brochier, T., Brun, C., Cohen, J. Y., Coutureau, E., Deffains, M., Doyère, V., Gregoriou, G. G., Heimel, J. A., Kilavik, B. E., Lee, D., Leuthardt, E. C., Mainen, Z. F., Mathis, M., Monosov, I. E., Naudé, J., … Zimmermann, J. (2023). A response to claims of emergent intelligence and sentience in a dish. *Neuron*, 111(5), 604–605.

Barlow, H. B. (1961). Possible principles underlying the transformations of sensory messages. In W. A. Rosenblith (Ed.), *Sensory Communication* (pp. 217–234). MIT Press.

Bowers, J. S., & Davis, C. J. (2012). Bayesian just-so stories in psychology and neuroscience. *Psychological Bulletin*, 138(3), 389–414.

Brenner, N., Bialek, W., & de Ruyter van Steveninck, R. (2000). Adaptive rescaling maximizes information transmission. *Neuron*, 26(3), 695–702.

Bruineberg, J., Dołęga, K., Dewhurst, J., & Baltieri, M. (2022). The emperor's new Markov blankets. *Behavioral and Brain Sciences*, 45, e183.

Chalk, M., Marre, O., & Tkačik, G. (2018). Toward a unified theory of efficient, predictive, and sparse coding. *Proceedings of the National Academy of Sciences*, 115(1), 186–191.

Cisek, P. (2019). Resynthesizing behavior through phylogenetic refinement. *Attention, Perception, & Psychophysics*, 81(7), 2265–2287.

Clark, A. (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behavioral and Brain Sciences*, 36(3), 181–204.

Craik, K. J. W. (1943). *The Nature of Explanation*. Cambridge University Press.

Dayan, P., Kakade, S., & Montague, P. R. (2000). Learning and selective attention. *Nature Neuroscience*, 3(Suppl.), 1218–1223.

Duhamel, J.-R., Colby, C. L., & Goldberg, M. E. (1992). The updating of the representation of visual space in parietal cortex by intended eye movements. *Science*, 255(5040), 90–92.

Fairhall, A. L., Lewen, G. D., Bialek, W., & de Ruyter van Steveninck, R. R. (2001). Efficiency and ambiguity in an adaptive neural code. *Nature*, 412(6849), 787–792.

Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.

Friston, K., Fortier, M., & Friedman, D. A. (2018). Of woodlice and men: A Bayesian account of cognition, life and consciousness. An interview with Karl Friston. *ALIUS Bulletin*, 2, 17–43.

Friston, K., Kilner, J., & Harrison, L. (2006). A free energy principle for the brain. *Journal of Physiology-Paris*, 100(1–3), 70–87.

Friston, K., Rigoli, F., Ognibene, D., Mathys, C., Fitzgerald, T., & Pezzulo, G. (2015). Active inference and epistemic value. *Cognitive Neuroscience*, 6(4), 187–214.

Friston, K., Thornton, C., & Clark, A. (2012). Free-energy minimization and the dark-room problem. *Frontiers in Psychology*, 3, 130.

Garvert, M. M., Dolan, R. J., & Behrens, T. E. J. (2017). A map of abstract relational knowledge in the human hippocampal–entorhinal cortex. *eLife*, 6, e17086.

Gershman, S. J. (2019). What does the free energy principle tell us about the brain? *Neurons, Behavior, Data Analysis, and Theory*, 2(3).

Griffiths, T. L., Chater, N., Norris, D., & Pouget, A. (2012). How the Bayesians got their beliefs (and what those beliefs actually are): Comment on Bowers and Davis (2012). *Psychological Bulletin*, 138(3), 415–422.

Hensch, T. K. (2005). Critical period plasticity in local cortical circuits. *Nature Reviews Neuroscience*, 6(11), 877–888.

Hohwy, J. (2013). *The Predictive Mind*. Oxford University Press.

Isomura, T., Kotani, K., Jimbo, Y., & Friston, K. J. (2023). Experimental validation of the free-energy principle with in vitro neural networks. *Nature Communications*, 14, 4547.

Kagan, B. J., Kitchen, A. C., Tran, N. T., Habibollahi, F., Khajehnejad, M., Parker, B. J., Bhat, A., Rollo, B., Razi, A., & Friston, K. J. (2022). In vitro neurons learn and exhibit sentience when embodied in a simulated game-world. *Neuron*, 110(23), 3952–3969.

Kalman, R. E. (1960). A new approach to linear filtering and prediction problems. *Journal of Basic Engineering*, 82(1), 35–45.

Keller, G. B., Bonhoeffer, T., & Hübener, M. (2012). Sensorimotor mismatch signals in primary visual cortex of the behaving mouse. *Neuron*, 74(5), 809–815.

Kutas, M., & Federmeier, K. D. (2011). Thirty years and counting: Finding meaning in the N400 component of the event-related brain potential (ERP). *Annual Review of Psychology*, 62, 621–647.

Kutas, M., & Hillyard, S. A. (1980). Reading senseless sentences: Brain potentials reflect semantic incongruity. *Science*, 207(4427), 203–205.

Körding, K. P., Tenenbaum, J. B., & Shadmehr, R. (2007). The dynamics of memory as a consequence of optimal adaptation to a changing body. *Nature Neuroscience*, 10(6), 779–786.

Lamb, T. D., & Pugh, E. N., Jr. (2004). Dark adaptation and the retinoid cycle of vision. *Progress in Retinal and Eye Research*, 23(3), 307–380.

Land, M. F., & McLeod, P. (2000). From eye movements to actions: How batsmen hit the ball. *Nature Neuroscience*, 3(12), 1340–1345.

Laughlin, S. (1981). A simple coding procedure enhances a neuron's information capacity. *Zeitschrift für Naturforschung C*, 36(9–10), 910–912.

Lawson, R. P., Mathys, C., & Rees, G. (2017). Adults with autism overestimate the volatility of the sensory environment. *Nature Neuroscience*, 20(9), 1293–1299.

LeCun, Y. (2022). *A path towards autonomous machine intelligence* (Version 0.9.2). OpenReview.

Mather, G., Verstraten, F., & Anstis, S. (Eds.). (1998). *The Motion Aftereffect: A Modern Perspective*. MIT Press.

Mathys, C., Daunizeau, J., Friston, K. J., & Stephan, K. E. (2011). A Bayesian foundation for individual learning under uncertainty. *Frontiers in Human Neuroscience*, 5, 39.

McGuire, J. T., Nassar, M. R., Gold, J. I., & Kable, J. W. (2014). Functionally dissociable influences on learning rate in a dynamic environment. *Neuron*, 84(4), 870–881.

Mehta, M. R., Barnes, C. A., & McNaughton, B. L. (1997). Experience-dependent, asymmetric expansion of hippocampal place fields. *Proceedings of the National Academy of Sciences*, 94(16), 8918–8921.

Millidge, B., Tschantz, A., & Buckley, C. L. (2021). Whence the expected free energy? *Neural Computation*, 33(2), 447–482.

Momennejad, I., Russek, E. M., Cheong, J. H., Botvinick, M. M., Daw, N. D., & Gershman, S. J. (2017). The successor representation in human reinforcement learning. *Nature Human Behaviour*, 1(9), 680–692.

Nassar, M. R., Rumsey, K. M., Wilson, R. C., Parikh, K., Heasly, B., & Gold, J. I. (2012). Rational regulation of learning dynamics by pupil-linked arousal systems. *Nature Neuroscience*, 15(7), 1040–1046.

Nassar, M. R., Wilson, R. C., Heasly, B., & Gold, J. I. (2010). An approximately Bayesian delta-rule model explains the dynamics of belief updating in a changing environment. *Journal of Neuroscience*, 30(37), 12366–12378.

Nieuwland, M. S., Politzer-Ahles, S., Heyselaar, E., Segaert, K., Darley, E., Kazanina, N., Von Grebmer Zu Wolfsthurn, S., Bartolozzi, F., Kogan, V., Ito, A., Mézière, D., Barr, D. J., Rousselet, G. A., Ferguson, H. J., Busch-Moreno, S., Fu, X., Tuomainen, J., Kulakova, E., Husband, E. M., … Huettig, F. (2018). Large-scale replication study reveals a limit on probabilistic prediction in language comprehension. *eLife*, 7, e33468.

Nijhawan, R. (1994). Motion extrapolation in catching. *Nature*, 370(6487), 256–257.

Palmer, S. E., Marre, O., Berry, M. J., II, & Bialek, W. (2015). Predictive information in a sensory population. *Proceedings of the National Academy of Sciences*, 112(22), 6908–6913.

Powers, A. R., Mathys, C., & Corlett, P. R. (2017). Pavlovian conditioning–induced hallucinations result from overweighting of perceptual priors. *Science*, 357(6351), 596–600.

Pretto, P., Bresciani, J.-P., Rainer, G., & Bülthoff, H. H. (2012). Foggy perception slows us down. *eLife*, 1, e00031.

Rao, R. P. N., & Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience*, 2(1), 79–87.

Schmolesky, M. T., Wang, Y., Hanes, D. P., Thompson, K. G., Leutgeb, S., Schall, J. D., & Leventhal, A. G. (1998). Signal timing across the macaque visual system. *Journal of Neurophysiology*, 79(6), 3272–3278.

Snowden, R. J., Stimpson, N., & Ruddle, R. A. (1998). Speed perception fogs up as visibility drops. *Nature*, 392(6675), 450.

Sotiropoulos, G., Seitz, A. R., & Seriès, P. (2011). Changing expectations about speed alters perceived motion direction. *Current Biology*, 21(21), R883–R884.

Srinivasan, M. V., Laughlin, S. B., & Dubs, A. (1982). Predictive coding: A fresh view of inhibition in the retina. *Proceedings of the Royal Society of London. Series B, Biological Sciences*, 216(1205), 427–459.

Stachenfeld, K. L., Botvinick, M. M., & Gershman, S. J. (2017). The hippocampus as a predictive map. *Nature Neuroscience*, 20(11), 1643–1653.

Stahl, A. E., & Feigenson, L. (2015). Observing the unexpected enhances infants' learning and exploration. *Science*, 348(6230), 91–94.

Sterling, P. (2012). Allostasis: A model of predictive regulation. *Physiology & Behavior*, 106(1), 5–15.

Stocker, A. A., & Simoncelli, E. P. (2006). Noise characteristics and prior expectations in human visual speed perception. *Nature Neuroscience*, 9(4), 578–585.

Stoffregen, T. A., Chen, F.-C., Varlet, M., Alcantara, C., & Bardy, B. G. (2013). Getting your sea legs. *PLoS ONE*, 8(6), e66949.

Sutton, R. S. (1992). Adapting bias by gradient descent: An incremental version of delta-bar-delta. In *Proceedings of the Tenth National Conference on Artificial Intelligence* (pp. 171–176). AAAI Press.

Turrigiano, G. G., Leslie, K. R., Desai, N. S., Rutherford, L. C., & Nelson, S. B. (1998). Activity-dependent scaling of quantal amplitude in neocortical neurons. *Nature*, 391(6670), 892–896.

Vallortigara, G., Regolin, L., & Marconato, F. (2005). Visually inexperienced chicks exhibit spontaneous preference for biological motion patterns. *PLoS Biology*, 3(7), e208.

Walsh, K. S., McGovern, D. P., Clark, A., & O'Connell, R. G. (2020). Evaluating the neurophysiological evidence for predictive processing as a model of perception. *Annals of the New York Academy of Sciences*, 1464(1), 242–268.

Wark, B., Lundstrom, B. N., & Fairhall, A. (2007). Sensory adaptation. *Current Opinion in Neurobiology*, 17(4), 423–429.

Westerberg, J. A., Xiong, Y. S., Sennesh, E., Nejat, H., Ricci, D., Durand, S., et al., & Bastos, A. M. (2025). *Hierarchical substrates of prediction in visual cortical spiking* [Preprint]. bioRxiv.

Yu, A. J., & Dayan, P. (2005). Uncertainty, neuromodulation, and attention. *Neuron*, 46(4), 681–692.

Zangwill, O. L. (1980). Kenneth Craik: The man and his work. *British Journal of Psychology*, 71(1), 1–16.

Zimmerman, C. A., Lin, Y.-C., Leib, D. E., Guo, L., Huey, E. L., Daly, G. E., Chen, Y., & Knight, Z. A. (2016). Thirst neurons anticipate the homeostatic consequences of eating and drinking. *Nature*, 537(7622), 680–684.

[^1]: Craik, K. J. W. (1943). *The Nature of Explanation*. Cambridge University Press; Zangwill, O. L. (1980). Kenneth Craik: The man and his work. *British Journal of Psychology*, 71(1), 1–16.

[^2]: Schmolesky, M. T., Wang, Y., Hanes, D. P., Thompson, K. G., Leutgeb, S., Schall, J. D., & Leventhal, A. G. (1998). Signal timing across the macaque visual system. *Journal of Neurophysiology*, 79(6), 3272–3278.

[^3]: Nijhawan, R. (1994). Motion extrapolation in catching. *Nature*, 370(6487), 256–257.

[^4]: Land, M. F., & McLeod, P. (2000). From eye movements to actions: How batsmen hit the ball. *Nature Neuroscience*, 3(12), 1340–1345.

[^5]: Duhamel, J.-R., Colby, C. L., & Goldberg, M. E. (1992). The updating of the representation of visual space in parietal cortex by intended eye movements. *Science*, 255(5040), 90–92.

[^6]: Srinivasan, M. V., Laughlin, S. B., & Dubs, A. (1982). Predictive coding: A fresh view of inhibition in the retina. *Proceedings of the Royal Society of London. Series B, Biological Sciences*, 216(1205), 427–459.

[^7]: Rao, R. P. N., & Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience*, 2(1), 79–87.

[^8]: Zimmerman, C. A., Lin, Y.-C., Leib, D. E., Guo, L., Huey, E. L., Daly, G. E., Chen, Y., & Knight, Z. A. (2016). Thirst neurons anticipate the homeostatic consequences of eating and drinking. *Nature*, 537(7622), 680–684.

[^9]: Sterling, P. (2012). Allostasis: A model of predictive regulation. *Physiology & Behavior*, 106(1), 5–15.

[^10]: Laughlin, S. (1981). A simple coding procedure enhances a neuron's information capacity. *Zeitschrift für Naturforschung C*, 36(9–10), 910–912.

[^11]: Barlow, H. B. (1961). Possible principles underlying the transformations of sensory messages. In W. A. Rosenblith (Ed.), *Sensory Communication* (pp. 217–234). MIT Press.

[^12]: Brenner, N., Bialek, W., & de Ruyter van Steveninck, R. (2000). Adaptive rescaling maximizes information transmission. *Neuron*, 26(3), 695–702.

[^13]: Fairhall, A. L., Lewen, G. D., Bialek, W., & de Ruyter van Steveninck, R. R. (2001). Efficiency and ambiguity in an adaptive neural code. *Nature*, 412(6849), 787–792.

[^14]: Wark, B., Lundstrom, B. N., & Fairhall, A. (2007). Sensory adaptation. *Current Opinion in Neurobiology*, 17(4), 423–429.

[^15]: Addams, R. (1834). An account of a peculiar optical phænomenon seen after having looked at a moving body. *London and Edinburgh Philosophical Magazine and Journal of Science*, 5(29), 373–374; Mather, G., Verstraten, F., & Anstis, S. (Eds.). (1998). *The Motion Aftereffect: A Modern Perspective*. MIT Press.

[^16]: Palmer, S. E., Marre, O., Berry, M. J., II, & Bialek, W. (2015). Predictive information in a sensory population. *Proceedings of the National Academy of Sciences*, 112(22), 6908–6913.

[^17]: Chalk, M., Marre, O., & Tkačik, G. (2018). Toward a unified theory of efficient, predictive, and sparse coding. *Proceedings of the National Academy of Sciences*, 115(1), 186–191.

[^18]: Mehta, M. R., Barnes, C. A., & McNaughton, B. L. (1997). Experience-dependent, asymmetric expansion of hippocampal place fields. *Proceedings of the National Academy of Sciences*, 94(16), 8918–8921.

[^19]: Stachenfeld, K. L., Botvinick, M. M., & Gershman, S. J. (2017). The hippocampus as a predictive map. *Nature Neuroscience*, 20(11), 1643–1653.

[^20]: Momennejad, I., Russek, E. M., Cheong, J. H., Botvinick, M. M., Daw, N. D., & Gershman, S. J. (2017). The successor representation in human reinforcement learning. *Nature Human Behaviour*, 1(9), 680–692.

[^21]: Garvert, M. M., Dolan, R. J., & Behrens, T. E. J. (2017). A map of abstract relational knowledge in the human hippocampal–entorhinal cortex. *eLife*, 6, e17086.

[^22]: Keller, G. B., Bonhoeffer, T., & Hübener, M. (2012). Sensorimotor mismatch signals in primary visual cortex of the behaving mouse. *Neuron*, 74(5), 809–815.

[^23]: Attinger, A., Wang, B., & Keller, G. B. (2017). Visuomotor coupling shapes the functional development of mouse visual cortex. *Cell*, 169(7), 1291–1302.

[^24]: Kutas, M., & Hillyard, S. A. (1980). Reading senseless sentences: Brain potentials reflect semantic incongruity. *Science*, 207(4427), 203–205.

[^25]: Kutas, M., & Federmeier, K. D. (2011). Thirty years and counting: Finding meaning in the N400 component of the event-related brain potential (ERP). *Annual Review of Psychology*, 62, 621–647.

[^26]: Nieuwland, M. S., Politzer-Ahles, S., Heyselaar, E., Segaert, K., Darley, E., Kazanina, N., Von Grebmer Zu Wolfsthurn, S., Bartolozzi, F., Kogan, V., Ito, A., Mézière, D., Barr, D. J., Rousselet, G. A., Ferguson, H. J., Busch-Moreno, S., Fu, X., Tuomainen, J., Kulakova, E., Husband, E. M., … Huettig, F. (2018). Large-scale replication study reveals a limit on probabilistic prediction in language comprehension. *eLife*, 7, e33468.

[^27]: Kalman, R. E. (1960). A new approach to linear filtering and prediction problems. *Journal of Basic Engineering*, 82(1), 35–45; Dayan, P., Kakade, S., & Montague, P. R. (2000). Learning and selective attention. *Nature Neuroscience*, 3(Suppl.), 1218–1223.

[^28]: Nassar, M. R., Wilson, R. C., Heasly, B., & Gold, J. I. (2010). An approximately Bayesian delta-rule model explains the dynamics of belief updating in a changing environment. *Journal of Neuroscience*, 30(37), 12366–12378.

[^29]: Nassar, M. R., Rumsey, K. M., Wilson, R. C., Parikh, K., Heasly, B., & Gold, J. I. (2012). Rational regulation of learning dynamics by pupil-linked arousal systems. *Nature Neuroscience*, 15(7), 1040–1046.

[^30]: McGuire, J. T., Nassar, M. R., Gold, J. I., & Kable, J. W. (2014). Functionally dissociable influences on learning rate in a dynamic environment. *Neuron*, 84(4), 870–881.

[^31]: Yu, A. J., & Dayan, P. (2005). Uncertainty, neuromodulation, and attention. *Neuron*, 46(4), 681–692.

[^32]: Mathys, C., Daunizeau, J., Friston, K. J., & Stephan, K. E. (2011). A Bayesian foundation for individual learning under uncertainty. *Frontiers in Human Neuroscience*, 5, 39.

[^33]: Bowers, J. S., & Davis, C. J. (2012). Bayesian just-so stories in psychology and neuroscience. *Psychological Bulletin*, 138(3), 389–414; Griffiths, T. L., Chater, N., Norris, D., & Pouget, A. (2012). How the Bayesians got their beliefs (and what those beliefs actually are): Comment on Bowers and Davis (2012). *Psychological Bulletin*, 138(3), 415–422.

[^34]: Powers, A. R., Mathys, C., & Corlett, P. R. (2017). Pavlovian conditioning–induced hallucinations result from overweighting of perceptual priors. *Science*, 357(6351), 596–600.

[^35]: Lawson, R. P., Mathys, C., & Rees, G. (2017). Adults with autism overestimate the volatility of the sensory environment. *Nature Neuroscience*, 20(9), 1293–1299.

[^36]: Stoffregen, T. A., Chen, F.-C., Varlet, M., Alcantara, C., & Bardy, B. G. (2013). Getting your sea legs. *PLoS ONE*, 8(6), e66949.

[^37]: Lamb, T. D., & Pugh, E. N., Jr. (2004). Dark adaptation and the retinoid cycle of vision. *Progress in Retinal and Eye Research*, 23(3), 307–380.

[^38]: Turrigiano, G. G., Leslie, K. R., Desai, N. S., Rutherford, L. C., & Nelson, S. B. (1998). Activity-dependent scaling of quantal amplitude in neocortical neurons. *Nature*, 391(6670), 892–896.

[^39]: Hensch, T. K. (2005). Critical period plasticity in local cortical circuits. *Nature Reviews Neuroscience*, 6(11), 877–888.

[^40]: Körding, K. P., Tenenbaum, J. B., & Shadmehr, R. (2007). The dynamics of memory as a consequence of optimal adaptation to a changing body. *Nature Neuroscience*, 10(6), 779–786.

[^41]: Snowden, R. J., Stimpson, N., & Ruddle, R. A. (1998). Speed perception fogs up as visibility drops. *Nature*, 392(6675), 450; Pretto, P., Bresciani, J.-P., Rainer, G., & Bülthoff, H. H. (2012). Foggy perception slows us down. *eLife*, 1, e00031.

[^42]: Stocker, A. A., & Simoncelli, E. P. (2006). Noise characteristics and prior expectations in human visual speed perception. *Nature Neuroscience*, 9(4), 578–585.

[^43]: Sotiropoulos, G., Seitz, A. R., & Seriès, P. (2011). Changing expectations about speed alters perceived motion direction. *Current Biology*, 21(21), R883–R884.

[^44]: Vallortigara, G., Regolin, L., & Marconato, F. (2005). Visually inexperienced chicks exhibit spontaneous preference for biological motion patterns. *PLoS Biology*, 3(7), e208.

[^45]: Friston, K., Kilner, J., & Harrison, L. (2006). A free energy principle for the brain. *Journal of Physiology-Paris*, 100(1–3), 70–87; Friston, K. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.

[^46]: Clark, A. (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behavioral and Brain Sciences*, 36(3), 181–204; Hohwy, J. (2013). *The Predictive Mind*. Oxford University Press.

[^47]: Friston, K., Thornton, C., & Clark, A. (2012). Free-energy minimization and the dark-room problem. *Frontiers in Psychology*, 3, 130.

[^48]: Friston, K., Fortier, M., & Friedman, D. A. (2018). Of woodlice and men: A Bayesian account of cognition, life and consciousness. An interview with Karl Friston. *ALIUS Bulletin*, 2, 17–43.

[^49]: Andrews, M. (2021). The math is not the territory: Navigating the free energy principle. *Biology & Philosophy*, 36(3), 30; Gershman, S. J. (2019). What does the free energy principle tell us about the brain? *Neurons, Behavior, Data Analysis, and Theory*, 2(3).

[^50]: Bruineberg, J., Dołęga, K., Dewhurst, J., & Baltieri, M. (2022). The emperor's new Markov blankets. *Behavioral and Brain Sciences*, 45, e183.

[^51]: Aitchison, L., & Lengyel, M. (2017). With or without you: Predictive coding and Bayesian inference in the brain. *Current Opinion in Neurobiology*, 46, 219–227.

[^52]: Walsh, K. S., McGovern, D. P., Clark, A., & O'Connell, R. G. (2020). Evaluating the neurophysiological evidence for predictive processing as a model of perception. *Annals of the New York Academy of Sciences*, 1464(1), 242–268.

[^53]: Westerberg, J. A., Xiong, Y. S., Sennesh, E., Nejat, H., Ricci, D., Durand, S., et al., & Bastos, A. M. (2025). *Hierarchical substrates of prediction in visual cortical spiking* [Preprint]. bioRxiv.

[^54]: Isomura, T., Kotani, K., Jimbo, Y., & Friston, K. J. (2023). Experimental validation of the free-energy principle with in vitro neural networks. *Nature Communications*, 14, 4547.

[^55]: Kagan, B. J., Kitchen, A. C., Tran, N. T., Habibollahi, F., Khajehnejad, M., Parker, B. J., Bhat, A., Rollo, B., Razi, A., & Friston, K. J. (2022). In vitro neurons learn and exhibit sentience when embodied in a simulated game-world. *Neuron*, 110(23), 3952–3969.

[^56]: Balci, F., Ben Hamed, S., Boraud, T., Bouret, S., Brochier, T., Brun, C., Cohen, J. Y., Coutureau, E., Deffains, M., Doyère, V., Gregoriou, G. G., Heimel, J. A., Kilavik, B. E., Lee, D., Leuthardt, E. C., Mainen, Z. F., Mathis, M., Monosov, I. E., Naudé, J., … Zimmermann, J. (2023). A response to claims of emergent intelligence and sentience in a dish. *Neuron*, 111(5), 604–605.

[^57]: Stahl, A. E., & Feigenson, L. (2015). Observing the unexpected enhances infants' learning and exploration. *Science*, 348(6230), 91–94.

[^58]: Friston, K., Rigoli, F., Ognibene, D., Mathys, C., Fitzgerald, T., & Pezzulo, G. (2015). Active inference and epistemic value. *Cognitive Neuroscience*, 6(4), 187–214.

[^59]: Millidge, B., Tschantz, A., & Buckley, C. L. (2021). Whence the expected free energy? *Neural Computation*, 33(2), 447–482.

[^60]: Cisek, P. (2019). Resynthesizing behavior through phylogenetic refinement. *Attention, Perception, & Psychophysics*, 81(7), 2265–2287.

[^61]: LeCun, Y. (2022). *A path towards autonomous machine intelligence* (Version 0.9.2). OpenReview.

[^62]: Sutton, R. S. (1992). Adapting bias by gradient descent: An incremental version of delta-bar-delta. In *Proceedings of the Tenth National Conference on Artificial Intelligence* (pp. 171–176). AAAI Press.
