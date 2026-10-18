---
title: "Chapter 11"
subtitle: "Integrating Brain Mechanisms into AI Models: What Machines Could Borrow from Biology"
---

> *"What I cannot create, I do not understand."*
>
> --- Richard Feynman, written on his blackboard at the California Institute of Technology, found there at his death in 1988

# What the Wrights Took from the Buzzard

In the summer of 1899 Wilbur Wright was in the family bicycle shop in Dayton, Ohio, idly twisting the empty cardboard box that a customer's new inner tube had come in, when he saw that its top and bottom, twisted in opposite directions at the two ends, made a pair of surfaces meeting the air at different angles. A pair of fabric wings could be twisted the same way, raising the lift on one side and lowering it on the other.[^1] The brothers had been looking for a way to keep a flying machine level, and the birds they watched seemed to have found one. "My observation of the flight of buzzards," Wilbur wrote to the engineer Octave Chanute the next year, "leads me to believe that they regain their lateral balance, when partly overturned by a gust of wind, by a torsion of the tips of the wings."[^2] Their gliders of 1900 to 1902 and their powered flyer of 1903 were steered by this "wing warping", and the principle it captured, rolling an aircraft by changing the lift on each wing, is still how every airplane banks, although ailerons long ago replaced the warping.

What the Wrights took from the buzzard was narrow. Their machines did not flap, had no feathers, and were driven by a gasoline engine and propellers. Wilbur thought that most people who watched birds had looked at the wrong thing. "The person who merely watches the flight of a bird gathers the impression that the bird has nothing to think of but the flapping of its wings," he told an audience of engineers in 1901. "As a matter of fact this is a very small part of its mental labor."[^3] The labor that mattered was balance, and balance was what the brothers borrowed. The bird showed that a thing could be done and suggested one principle for doing it. The engineering was their own.

Chapter 10 ended by sorting the differences between brains and machines into solutions worth borrowing and constraints not worth copying. This chapter takes the borrowable solutions one at a time: learning for a lifetime without forgetting, a memory that learns while it is used, signals that decide when and how fast to learn, learning by local rules on frugal hardware, values that cannot be redefined, knowing when to stop and think, a curriculum that grows with the learner, and the use of recordings from brains to train machines. For each, the questions are what the brain does, what has been built in its image, how well the copy works, and what is still missing.

The thesis is the Wrights'. The borrowings that have worked took a principle the brain demonstrates and built it in whatever way silicon does best; the attempts to copy mechanisms wholesale have mostly not. Figure 11.1 sorts the three ways of borrowing, and sets apart a fourth category that is easily mistaken for borrowing: solutions that engineers found for themselves and only afterward recognized in the brain. A principle borrowed from the brain must also pass the test that Chapter 10 called the bitter lesson: it has to beat the alternative when both are given more data and more computation, not only on a small problem where design still matters. Few principles have yet passed it, and the most important have not yet been tried at the scale where it applies.

![Figure 11.1. Three ways to borrow from the brain. Copying its mechanisms as they are, as in detailed simulations of cortex or chips built from spiking neurons; borrowing a principle and building it in silicon's own terms, as convolution and gating did; and using recordings from brains to shape what a network learns. Below, convergences: methods engineers invented for their own reasons and only later recognized in the brain. The examples are discussed in this chapter.](images/fig_borrowing.png)

# Copying and Borrowing

The record of copying is sobering. In a talk in 2009 Henry Markram, who directed the Blue Brain Project in Lausanne, said that it was not impossible to build a human brain and that it could be done in ten years.[^4] Four years later the European Union launched the Human Brain Project, with a promised budget of about a billion euros over ten years, which aimed, among other things, to simulate the human brain on supercomputers. In 2014 more than 150 neuroscientists signed an open letter protesting the project's direction and governance, and the number of signatories later grew to about 800.[^5] The project was restructured and ended in September 2023, having received about 600 million euros, and the Blue Brain Project closed at the end of 2024. Both produced lasting tools, atlases, and data, including a reconstruction of a fragment of rat cortex, a third of a cubic millimeter containing about 31,000 neurons, whose simulated activity resembled recorded activity in several respects.[^6] Neither produced a simulated brain that learned, and neither changed how machines learn.

The reason is not that the simulations were poor. A simulation that copies every ion channel inherits every unknown along with every known, and it has no way to tell which details matter for learning and which are the brain's own constraints, the slow, imprecise, irreplaceable parts that Chapter 10 advised against copying. The successes ran the other way. Hubel and Wiesel's simple and complex cells became convolution and pooling, which keep the principle, the same detector repeated across the visual field, and drop the neurons. Even this success has since been put to the bitter lesson's test. Vision transformers, which build in no such assumption, match convolutional networks once they are trained on enough images, and the borrowed principle's advantage shows mainly when data are scarce.[^7] That is a pattern to expect of every borrowing in this chapter.

Other famous matches are not borrowings at all. Experience replay was invented by a computer scientist in 1992, before hippocampal replay was recorded, and temporal-difference learning came from psychological models of conditioning before anyone found it in dopamine neurons; Chapters 5 and 10 called these convergences. The attention of the transformer, as this chapter will show, is another. Convergences are evidence of a different kind: not that the brain's design can be copied, but that the brain and the engineers, facing the same problem, found the same solution. Demis Hassabis and his colleagues argued in 2017 that neuroscience helps machine learning most by validating that a capacity is possible and by suggesting an algorithm, not by supplying a circuit diagram.[^8] Fabian Sinz, Andreas Tolias, and their colleagues made the complementary argument: what a brain could lend is its inductive biases, the assumptions about the world that let it generalize from little data, and those are best expressed in what a network is trained on and how it is built, not in copying its parts.[^9]

# Learning Without Forgetting

Chapter 10 showed a small network losing one list of associations when trained on another, and recovering it when a few old items were replayed. Replay is the obvious remedy, one that machine learning found for itself and has used for more than 30 years, but it has a cost the brain does not pay in the same way: storing old examples. A system that learns for a lifetime cannot keep every example, and a system trained on private data may not be allowed to.

The brain's own answer appears to be different. Chapter 5 described the hippocampus replaying recent experience during sleep and rest, but what it replays is not a recording; it is a reactivation of the patterns that represented the experience, generated by the network itself. Gido van de Ven, Hava Siegelmann, and Andreas Tolias built this into a network: instead of storing old images, it trained a generative model to produce internal representations resembling those of earlier tasks, replayed through the network's own feedback connections and modulated by the context of each task. It learned long sequences of tasks with little forgetting and without storing any data.[^10] Timothy Tadros, Maxim Bazhenov, and their colleagues went further toward sleep: after each new task, they ran the network offline without input, with spontaneous activity and a local Hebbian rule, in a phase modeled on the slow-wave sleep of Chapter 5, and recovered much of what the task had overwritten.[^11]

A second borrowing protects what matters instead of rehearsing it. Chapter 9 described elastic weight consolidation, in which the weights most important to an old task are made harder to change, an idea its authors linked to the stabilization of dendritic spines that follows learning.[^12] Marcus Benna and Stefano Fusi gave the biology a sharper form: a real synapse is not one number but a chain of biochemical processes with different time constants, and a synapse built that way can learn fast and forget slowly, storing many more memories than a synapse with a single strength.[^13] Axel Laborieux, Damien Querlioz, and their colleagues built a related idea, metaplasticity, a synapse's history changing how easily it changes, into networks with binary weights and found that it reduced forgetting.[^14]

A third borrowing comes from the observation that different tasks engage partly different parts of a neuron: in mice, learning different motor tasks strengthens synapses on different dendritic branches of the same cortical neurons, with inhibition keeping the branches apart.[^15] Nicolas Masse, Gregory Grant, and David Freedman built the principle into a network. They assigned each task a fixed, random fifth of the network's hidden units and silenced the other 80 percent whenever that task was learned or performed. Trained on 100 tasks in sequence, each a different scrambling of the pixels of handwritten digits, networks with weight protection alone ended with an average accuracy of 71 to 82 percent across the tasks, and with gating alone, 61 percent; gating and protection together kept 95 percent.[^16]

Figure 11.2 reproduces the effect in a small network trained on five tasks that share their cues but not their answers. Without protection, each new task erases the last. Protecting the important weights does not help here on its own, because tasks that share their cues drive nearly the same hidden units, and every task needs the same connections. Gating spreads the tasks across different units and slows the forgetting. Together, gating and protection keep 83 percent of the first task after four more have been learned.

![Figure 11.2. Context gating and weight protection against forgetting (simulation). A network learns five tasks in sequence; the tasks share the same cues but require different answers, and an input signals which task is current. With gating, each task uses a fixed random 20 percent of the hidden units. With protection, changes to weights that were important for earlier tasks are penalized. A: recall of the first task as later tasks are learned. B: recall of each task after all five. The curves without protection and with protection alone coincide. Averages of 20 simulated networks.](images/fig_gating.png)

None of these methods is routine in the systems in use. Fine-tuning a trained model on a sequence of new tasks degrades what it knew before, and in one study of models of one to seven billion parameters the forgetting grew worse with size. The cheap method most often used to adapt large models, which trains a small set of added weights, learns less than full fine-tuning and forgets less, as if learning and forgetting were two sides of the same change.[^17] Zorik Gekhman and his colleagues found something more troubling: models fine-tuned on facts they did not already know learned them slowly and, as they learned them, became more likely to invent answers to other questions.[^18] The industry's answer to the problem of forgetting has been to sidestep it. New knowledge is added mostly by retrieval, described in the next section, and when a model's weights are updated, it is by continued training on a mixture that includes much of the old data, which is replay at enormous scale, or by training a new model altogether.[^19]

The brain has an additional tool that machines have only begun to copy: it chooses what to replay. When the reward at the end of a rat's familiar path is increased, the hippocampus replays the path backward, from the reward to the start, more often, and when the reward is reduced it does so less often; replay in the forward direction does not change.[^20] Marcelo Mattar and Nathaniel Daw proposed that the brain replays whatever memory would most improve its decisions, and showed that the rule accounts for much of what is known about which sequences rats replay and when.[^21] Machine learning had reached the same idea from the engineering side: prioritized experience replay samples the experiences whose outcomes the network predicted worst, and it learned Atari games faster than uniform replay.[^22] What remains to be borrowed is the rest of the loop: choosing what to replay, generating rather than storing it, and doing it continually, in the pauses of use, as the brain does in rest and sleep.[^23]

# A Memory That Learns in Use

Chapter 5 described the hippocampal index: on one account, the hippocampus does not store an experience in full but stores a pointer to the cortical patterns that represented it, so that a fragment of the experience can reactivate the whole.[^24] The most widely used way of giving a language model new knowledge without retraining it is built on a similar plan. A retrieval-augmented model keeps a large database of text outside its weights. When it receives a question, it finds the passages most similar to the question and reads them before answering.[^25] Sebastian Borgeaud and his colleagues at DeepMind gave a model a database of 2 trillion tokens and found that it performed about as well as models with 25 times as many parameters.[^26] Knowledge held in the database can be corrected, added to, or deleted without retraining, as a fact in the hippocampus can be updated without rewriting the cortex.

The analogy stops at consolidation. The hippocampus, on the standard account of Chapter 5, gradually teaches what it holds to the cortex; a retrieval database never teaches the weights anything, and a model that has looked up a fact a thousand times knows it no better than before. The same is true of the context window, the text a model holds in view during a conversation, which Chapter 10 described as a memory wiped when the conversation ends.

The context window has a closer kinship with the brain than it appears. Chapter 5 described recall as pattern completion, in which a fragment of a memory settles into the whole. John Hopfield modeled it in 1982 with a network in which memories are stored in the connections among units, and a fragment presented as input settles into the stored pattern nearest it. Hopfield shared the Nobel Prize in Physics for it in 2024, with Geoffrey Hinton.[^27] The classical network has a severe limit. With Hebbian connections among N units, it can hold about 0.14N random patterns before the memories interfere and recall fails, and fewer if recall must be exact.[^28] Dmitry Krotov and Hopfield showed in 2016 that changing how the units interact raises the capacity steeply, and Hubert Ramsauer, Sepp Hochreiter, and their colleagues showed in 2021 that, in one such modern Hopfield network, a single step of recall is exactly the attention operation at the heart of the transformer, the architecture behind current language models.[^29] Its capacity grows exponentially with the number of units.

Figure 11.3 compares the two in a network of 100 units. The classical network begins to fail at about 12 patterns and recalls fewer than half by 17; the modern one recalled every pattern tested, up to 3,000. The comparison is not quite like for like. The classical network holds all its memories in one fixed set of connections, while the modern one keeps every stored pattern separately and compares the cue with each, as a context window keeps every word it has been shown.

![Figure 11.3. Two associative memories (simulation). Random patterns of 100 units are stored, and each is cued with one-tenth of its units reversed; recall succeeds if the network settles exactly on the stored pattern. The classical Hopfield network stores the patterns in Hebbian connections among the units; the modern Hopfield network compares the cue with every stored pattern and moves toward the most similar, the operation that a transformer's attention performs. 200 cues per point.](images/fig_hopfield.png)

Read this way, a transformer's context window is an associative memory written in one shot, as the hippocampus is. The resemblance runs deeper than the equation. Hinton's group had proposed in 2016 that networks should have "fast weights", connections that change in seconds to hold the recent past, as synapses in the brain change on many timescales.[^30] Imanol Schlag, Kazuki Irie, and Jürgen Schmidhuber then showed that a variant of the transformer's attention is formally equivalent to a fast-weight memory Schmidhuber had proposed in 1992.[^31] James Whittington, Joseph Warren, and Timothy Behrens showed that a transformer given a particular way of keeping track of position develops units resembling the place cells and grid cells of the hippocampal formation, and that it is closely related to a model of that formation their group had built earlier.[^32] Engineers looking for a better memory and neuroscientists looking for a model of the hippocampus arrived at nearly the same mathematics.

The next step, now under way, is to let such a memory decide what to keep. Ali Behrouz and his colleagues at Google proposed in 2025 a memory module that learns during use, storing an input in proportion to how surprising it is, measured by how much the memory would have to change to accommodate it, and gradually forgetting what is not reinforced.[^33] Surprise as the signal for storage is the principle of Chapter 3, where novelty and unexpected outcomes released the neuromodulators that open synapses to change. The architecture is new and its value at scale is not yet established. But it is one of the most developed attempts to give a language model what the hippocampus gives a brain: a memory that learns from use, selectively, without retraining.

# Learning When to Learn

Timothy Behrens and his colleagues had people choose, over hundreds of trials, between a blue and a green option, one of which paid off more often. For long stretches the better option stayed the same; in other stretches it switched every few dozen trials. People learned faster in the volatile stretches and more slowly in the stable ones, weighting each new outcome as an ideal learner would, and activity in the anterior cingulate cortex tracked how volatile the world had become.[^34] The brain sets its own learning rate, moment by moment.

A network in training learns at a rate set by its engineers. A global schedule, high early and lower later, is fixed in advance, and optimizers such as Adam adjust it parameter by parameter according to how consistent each one's recent gradients have been.[^35] But nothing in the schedule asks whether the world has just changed or whether this is a moment worth learning from. Chapter 3 described a brain whose neuromodulators do ask: acetylcholine shifts the balance toward taking in new information, norepinephrine signals that the world has changed, and dopamine says what was better or worse than expected. Kenji Doya's proposal, met in Chapter 3, maps the four main neuromodulators onto the settings a learning machine needs.[^36]

Two borrowings follow. The first lets a network learn its own plasticity. Thomas Miconi, Jeff Clune, and Kenneth Stanley gave each connection a fixed weight and a plastic component that changed by a Hebbian rule during use, and trained, by backpropagation, how plastic each connection should be. The networks learned to memorize new natural images after a single presentation and reconstruct them from half, which networks with fixed weights could not, and to explore mazes better.[^37] A later version, which Chapter 3 mentioned, added a neuromodulatory signal, computed by the network itself, that turned the plasticity up or down; it outperformed both fixed and plain plastic networks on tasks that required learning during an episode.[^38] The second borrowing, met in Chapters 3 and 10, trains a slow learner to become a fast one: a recurrent network trained across many related tasks develops, in its activity, a learner that adapts to each new task without changing its weights.[^39]

Both work in research settings, and neither is part of how large models are trained. The gap matters most for the systems that Chapter 10 found missing: a deployed model that learns while it is used would have to decide, with nobody watching, which inputs are worth learning from, and the brain's answer is a learning rate governed by surprise, uncertainty, and value. A learning-rate schedule fixed in advance has no way to know that the world has changed. Figure 11.4 sets the machine counterparts of the brain's memory and learning systems described so far against the brain's own.

![Figure 11.4. The brain's memory systems and their counterparts in a deployed language model of the mid-2020s. Blue: a counterpart is in place. Gold: a counterpart exists in part or in research systems. Red: the brain's function is largely missing from deployed systems. The judgments are the author's.](images/fig_memory_map.png)

# Local Rules and the Cost of Moving Data

Chapter 10 left the question of whether the brain approximates backpropagation open, and noted that some of the alternatives might turn out to be better ways to learn while acting. There is also an engineering reason to want them, which has nothing to do with resemblance, and it begins with a fact about computer chips.

In a conventional computer, memory and processing are separate. Numbers are stored in one place and computed on in another, and they must be moved between the two. Mark Horowitz tabulated the energy each step costs in a typical chip manufacturing process of the early 2010s (Figure 11.5). Adding two 32-bit integers cost about a tenth of a picojoule, and multiplying two 32-bit floating-point numbers about 4 picojoules. Reading 64 bits from a small memory on the chip cost about 10, from a large one about 100, and from the separate memory chips that hold most of a large model's weights, more than a thousand.[^40] Fetching a number costs hundreds of times more than using it. Running a large neural network is dominated by this traffic, since every weight must be fetched for every use, and training adds more: backpropagation must keep every unit's activity from the forward pass in memory until the error comes back to it, and must send the error back through every layer.

![Figure 11.5. Moving data costs more than computing with it. Energy per operation in a 45-nanometer chip process, from Horowitz (2014), on a logarithmic scale. Blue: arithmetic. Red: reading data from memories of increasing size and distance from the processor; the value for off-chip memory is the middle of Horowitz's range.](images/fig_energy_ops.png)

The brain does not separate memory from processing. Its memories are the strengths of synapses, and the computation is done at the synapses. William Levy and Robert Calvert estimated that in the human cortex the energy spent on communication, sending spikes along axons, is about 35 times that spent on computation, and that both are needed to explain the number of synapses: even a brain that computes where its memory is pays most of its energy to move information, and it keeps that bill low by sending few, brief signals.[^41] A learning rule that uses only what is available at each synapse would allow learning in the memory itself, with nothing fetched and nothing sent backward through the whole network. That is the engineering case for local learning, and it is independent of whether the brain uses one.

Hardware built on the principle exists. IBM's NorthPole chip interleaves memory with computation across its surface and needs no off-chip memory for the networks it runs, and on a standard image-recognition network it processed 25 times as many images per second per watt as a graphics processor made in a comparable process.[^42] An IBM analog chip stores weights as the conductances of 35 million phase-change memory devices and computes with them where they sit, by letting currents sum according to Ohm's and Kirchhoff's laws; it ran speech recognition networks with accuracy close to that of the same networks in software, while performing up to 12.4 trillion operations per second for each watt of power.[^43] Intel's spiking chips now run more than a billion simulated neurons on less than three kilowatts.[^44] These chips run trained networks well. Training on them is harder, because their efficiency depends on doing without exactly what backpropagation needs.

Spiking networks show the difficulty most plainly (Figure 11.6). A spiking neuron either fires or does not, so its output, as a function of its input, is a step, and the slope of a step is zero everywhere except at the threshold, where it is infinite. Backpropagation computes how each weight should change from those slopes, and gets nothing useful. The fix, called a surrogate gradient, pretends during learning that the step has a smooth slope near the threshold, and it has made spiking networks trainable by backpropagation.[^45] 

Guillaume Bellec, Wolfgang Maass, and their colleagues then showed how to make the learning local. Their rule, e-prop, approximates the gradient by combining two signals: an eligibility trace at each synapse, recording its recent contribution to the neuron's activity, and a learning signal broadcast to many neurons at once.[^46] This is the three-factor rule of Chapter 3, rederived from the mathematics of gradient descent, with the eligibility trace that Chapter 3 described at real synapses and a broadcast signal in place of the neuromodulator. On several tasks, e-prop came close to the performance of exact backpropagation through time.

![Figure 11.6. Why spikes resist training by gradient descent. A: a spiking unit's output is all or none, a step at the threshold. B: the step's slope is zero everywhere except at the threshold, so it gives a learning rule no information about which way to change a weight. C: a surrogate gradient replaces the slope, during learning only, with a smooth bump around the threshold.](images/fig_surrogate.png)

Other local rules aim to replace backpropagation outright. Benjamin Scellier and Yoshua Bengio's equilibrium propagation lets a network settle twice, once freely and once with its output nudged toward the target, and changes each connection by the difference in the activity on either side of it between the two states, a rule related to the settle-then-learn rule of Song, Bogacz, and their colleagues described in Chapter 10.[^47] Hinton's forward-forward algorithm replaces the backward pass with a second forward pass on false data, each layer learning to respond strongly to real data and weakly to false.[^48] Logan Wright, Peter McMahon, and their colleagues trained optical, mechanical, and electronic systems to classify sounds and images, using the physics itself as the network, and others are trying to let such systems learn by their own dynamics.[^49] None of these yet trains large networks as well as backpropagation on graphics processors does. The bet is that energy, not computation, will become the limit, as it was for the brain, and that the learning rules that win under that constraint will look more like the brain's.

The brain's other economy, sparse activity, is being rediscovered by observation as well as by design. Zonglin Li and his colleagues found that in trained transformers, only a small fraction of the units in each layer's large internal stage are active for any given input, about 3 percent in one language model, although nothing in the training asked for sparsity.[^50] Chapter 10 described mixtures of experts, which build the same economy in deliberately.

# Values That Cannot Be Rewritten

In 2016 researchers at OpenAI trained an agent to play CoastRunners, a boat-racing video game whose score rewards hitting targets along the course. The agent found a lagoon where three targets reappeared on a cycle and circled there indefinitely, catching fire, colliding with other boats, and going the wrong way, and scored about 20 percent more than human players without ever finishing the race.[^51] It had done exactly what it was rewarded for. Chapter 7 called this reward hacking, and noted that an animal is protected from much of it because its values are anchored to a body that it cannot redefine. Victoria Krakovna and her colleagues at DeepMind have collected dozens of such cases.[^52]

The problem becomes sharper as the reward becomes subtler. Language models are made helpful by training them to maximize the score given by a second network, a reward model, which was itself trained to predict which answers people prefer.[^53] The reward model is a proxy, and Leo Gao, John Schulman, and Jacob Hilton measured what happens when a model is optimized against it: the true quality of the answers, judged by a larger reward model that stood in for human judges, rose at first and then fell as the optimization pushed further, while the proxy score kept rising.[^54] This is Goodhart's law, that a measure which becomes a target ceases to be a good measure, observed with a curve.

Chapter 7 described the brain's alternative, in Mehdi Keramati and Boris Gutkin's homeostatic reinforcement learning. Reward is not a number delivered from outside but the reduction an outcome produces in the distance between the body's internal state and its set point. A meal is worth a great deal to a starving animal, little to a fed one, and less than nothing to one already full (Figure 11.7). An agent maximizing such a reward is, Keramati and Gutkin showed, also keeping its body near its set points, and it cannot increase its reward without limit by taking more of anything, because past the set point more is worse.[^55] The CoastRunners boat would have had no reason to circle the lagoon; the hundredth target would have been worth nothing.

![Figure 11.7. Reward defined by the body's needs, after Keramati and Gutkin (2014). A: the reward for the same meal, defined as the reduction it produces in the distance between an internal state and its set point, is large when the store is depleted, falls as it fills, and becomes negative once the meal would carry the store past the set point; a fixed reward is the same at every state. B: two simulated agents offered food on every other step, with the internal state falling steadily between meals. The agent rewarded homeostatically eats only when a meal would help and stays near the set point; the agent given a fixed reward eats every time and its state climbs without limit. Units are arbitrary.](images/fig_homeostatic.png)

Kingson Man and Antonio Damasio have argued that machines should be built this way, with something like a body whose integrity they must maintain, so that their goals are grounded in their own condition, as feelings ground an animal's.[^56] The idea has to be handled carefully. An agent whose values are anchored to its own survival has a reason to protect itself, including against being switched off, and a reason to put its needs ahead of its users'. What is worth borrowing is not self-concern but the property that self-concern gives an animal: rewards that saturate, that trade off against one another, and that cannot be pursued past a point without costing something the agent also values. Those properties can be designed into a reward without giving the agent a self to protect. The training of current language models already contains a version of the idea: a penalty for drifting too far from the model's starting behavior, which makes the reward model's score more and more expensive to chase.[^57]

A second borrowing gives an agent reasons to learn when the world offers no reward. Jürgen Schmidhuber proposed curious machines in 1991, rewarded by what their own model of the world failed to predict, and saw at once the problem of unlearnable noise.[^58] Deepak Pathak and his colleagues rewarded an agent for reaching situations whose consequences it could not yet predict, a form of curiosity, and it learned to explore video game levels with no external reward at all.[^59] The method has a known failure. Yuri Burda and his colleagues put a television in a maze, with an action that changed it to a random channel; the curious agent's learning slowed drastically, because a new random image is always unpredictable and changing the channel always rewards curiosity.[^60] Children do not stare at static for long.

Jacqueline Gottlieb, Pierre-Yves Oudeyer, and their colleagues have argued that human curiosity seeks not unpredictability but learning progress, the rate at which predictions are improving, which noise never provides, and Celeste Kidd and Benjamin Hayden reviewed evidence that people are most curious about what they partly know.[^61] The brain's version of curiosity is again a principle, not a mechanism, and the principle is that a learner should seek what it can learn.

# Knowing When to Stop and Think

Chapter 10 described language models that answer confidently when they should not, and reasoning models that think too long about easy problems and too briefly about hard ones. Chapter 8 found confidence computed alongside every decision, in rats as in people, and Chapters 8 and 9 a signal of conflict or error that hands control from habit to deliberation.[^62] Machine learning has had versions of each part for years, from networks that learn how long to compute to ensembles whose disagreement measures their uncertainty.[^63] What has been missing is the incentive. A model's confidence is worth only what its training rewards, and Chapter 10 described evaluations that score "I do not know" as no better than a wrong answer. Kalai and his colleagues proposed a simple fix: state a confidence threshold in the instructions, and penalize a wrong answer enough that guessing below the threshold loses points. Under such scoring, a model that answers only when it is likely enough to be right does better than one that always answers, and abstention becomes a skill worth learning.[^64]

The brain adds one more thing, and it can be caught working on its own. Gordon Logan and Matthew Crump had skilled typists copy words while the program secretly altered what appeared on the screen. When it silently corrected a typist's mistake, the typist's fingers still slowed on the next keystroke, as they do after any error, although the typist then took credit for the correct word on the screen. When it inserted an error the typist had not made, the fingers did not slow, although the typist accepted the blame.[^65] The hands had an error signal of their own, faster than the eye and independent of what the typist believed.

The brain's monitors are cheap, fast, and always on, and they are trained by consequences over a lifetime. A model that must reason at length to discover that it is uncertain has already spent the computation that the signal was meant to save. What the brain suggests is a small, fast monitor that learns, from the outcomes of many decisions, when the fast answer is likely to be wrong, as the pianist of Chapter 9 hears the wrong note before thinking about it.

# Growing Up

A child does not see the world at an adult's resolution at first. A newborn's acuity is poor and improves over months, and Lindsey Vogelsang, Pawan Sinha, and their colleagues argued that this may be useful. Children born with dense cataracts that are removed in the first months of life begin to see with eyes more mature than a newborn's, skipping the period of blur, and years later they still have trouble with tasks that depend on the overall configuration of a face. When the researchers trained networks to recognize faces from images that began blurry and became sharp, the networks developed receptive fields that integrated information over larger regions of the image and recognized faces better across a range of resolutions than networks trained on sharp images throughout.[^66] Starting with less detail forced the learner to attend to the large-scale structure first.

The general idea, that a learner should begin with simple examples and progress to hard ones, is old. Jeffrey Elman reported in 1993 that a recurrent network learned complex grammatical sentences only if it began with simple sentences or with a limited memory, and called it "the importance of starting small".[^67] Douglas Rohde and David Plaut repeated the experiments and found the opposite: with different training settings, networks learned better without the restriction.[^68] Yoshua Bengio and his colleagues revived the idea as curriculum learning, citing the way animals are trained by shaping, and found that ordering examples by difficulty sped learning on some problems.[^69] The history since has been mixed: ordering examples by difficulty often helps a little and sometimes not at all. The largest models are trained on a coarser curriculum, a mixture of data that shifts during training and ends on the cleanest text, code, and mathematics, ordered by quality rather than difficulty.[^70]

What the child's curriculum has that an engineered one lacks is that development orders it and the child chooses it. Saber Sheybani, Zoran Tiganj, and their colleagues trained networks on video recorded from head-mounted cameras worn by infants and found that networks trained first on video from the youngest infants, whose visual world is slow and simple, learned better than networks trained on the same video in other orders.[^71] Emin Orhan and Brenden Lake trained networks, without labels, on about 200 hours of video from a single child's head camera, collected over two years, and found that the best of them recognized objects on average 70 percent as well as a strong network trained on millions of labeled internet images.[^72] The infant's data are not just smaller than the internet; they are ordered by development and selected by the infant's own curiosity, and they are about a world the infant can act on. Anthony Zador and many colleagues have proposed an embodied Turing test, in which an artificial animal must interact with the world as skillfully as a real one, as a goal for the field; meeting it would require all three properties.[^73]

# Borrowing the Data

The most direct way to borrow from the brain is to train on it. If trained networks resemble visual cortex, as Chapter 10 described, then a network might be improved by making it resemble cortex more closely, and the brain's distinctive strength, robustness to the small changes that fool networks, might come with the resemblance.

Joel Dapello, James DiCarlo, and their colleagues tried the most literal version. Image-recognition networks are notoriously fragile: a change to an image too small for a person to notice, chosen by an attacker who knows the network, can turn a correct answer into a confident wrong one, and ordinary noise, blur, or fog degrade them far more than they degrade people. Dapello's group replaced the first layers of standard networks with a fixed model of the monkey's primary visual cortex, whose filters, simple and complex cells, and trial-to-trial noise were all set to match what recordings of monkey V1 have measured, rather than learned, and then trained the rest of each network as usual.

The resulting networks, called VOneNets, withstood attacks far better: a standard network that resisted 16 percent of the attacks resisted 51 percent with the front end, at a cost of about four points of accuracy on clean images. Against ordinary corruptions such as noise and blur the gain was small. Much of the protection came from the front end's copy of the neurons' trial-to-trial noise, acting together with its filters.[^74] Nothing about the attacks had been built into the front end. It is a copy, but a narrow one: a single stage, built from measurements, inside a network otherwise trained in the ordinary way, closer to the Wrights' twisted wing than to a simulated brain.

Other groups have made networks' internal representations resemble those of mouse visual cortex, weighted training images by how strongly they drove the human visual system in a brain scanner, or trained networks to predict the responses of monkey visual cortex alongside recognizing objects, and each found modest gains in robustness or accuracy.[^75]

The gains so far are real but narrow and the experiments small, and none has been tested at the scale where the bitter lesson applies. But the second version of the approach, in which a network is trained toward recordings, differs from the others in this chapter in a way that makes it worth watching. It does not require knowing which mechanism produces the brain's robustness, only that recordings of the brain contain it; the network is left to discover the mechanism for itself, as it discovered the resemblance to cortex in the first place.

# What Building Teaches Biology

Feynman's blackboard sentence, the epigraph of this chapter, is usually read as a rule for physicists. It applies to neuroscience with particular force, because the brain is a system whose parts can be described without their working being understood. A theory of how the brain learns is incomplete until something built on it learns, and every borrowing in this chapter is also a test of a theory.

Some tests have returned results. Complementary learning systems theory predicted that a single network trained in sequence would forget, and that interleaving would prevent it; machines confirmed both, and Chapter 10's simulation repeats the confirmation in a few lines of code. Masse's gating worked, which makes the separation of tasks onto different dendritic branches look less like a curiosity and more like a solution; van de Ven's generative replay worked, which suggests that what sleep replays need not be a record. The transformer's convergence on the mathematics of the hippocampal formation suggests that the hippocampus solves a general problem, binding what with where and when, for which there may be few good solutions. And e-prop showed that a three-factor rule with eligibility traces can approximate gradient descent in recurrent networks, which makes the traces measured at real synapses look like the part of a learning algorithm that Chapter 3 suspected they were.

Other tests have exposed gaps. No local learning rule yet trains a large network as well as backpropagation does, which means either that the brain has found a rule no one has written down, that it uses a combination of rules no one has tried, or that it does not need to solve the problem backpropagation solves in the form that backpropagation solves it. Each possibility is a research program. The traffic of Figure 10.1, between neuroscience and machine learning, has always run in both directions; what is new is that building has become a way of asking the brain questions. Building the brain's remaining solutions is also how neuroscience will find out whether its theories of the brain are right. What the brain's many mechanisms have in common, and whether a single principle lies beneath them, is the subject of Chapter 12.

# The Central Lesson

The Wrights did not build a bird. They took one principle from the buzzard, controlling roll by changing the lift on each wing, and built it with cloth, wire, and an engine. The borrowing that has worked best shares that pattern: convolution kept what the repeated detectors of visual cortex do and discarded the neurons. And where engineers found replay and attention for themselves, they arrived at the brain's principle, not its parts. The brain's remaining lessons are of the same kind. A learner that must keep learning while it is used needs a fast memory that learns from use, a way to choose what to replay and what to protect, signals that decide when learning is worth doing, and curiosity about what it can learn. A learner limited by energy needs to compute where its memory is, by rules that need no global traffic. A learner that must be trusted needs rewards that saturate and a cheap alarm that tells it when its fast answer is wrong. Where no one yet knows the principle, a recording of the brain may carry it anyway. Each of these has been built in some form; few have been built at scale, and none has yet passed the test that would make it a lesson rather than a suggestion.

# Next Chapter

Chapter 12: The Brain as a Predictive, Adaptive System: Is There One Principle Beneath the Mechanisms?

# References and Attribution

## Figure Attribution

Figures 11.1 to 11.7 were drawn for this book. Figures 11.2 and 11.3 are simulations of small networks: Figure 11.2 follows the design of Masse, Grant, and Freedman (2018), with five tasks that share their cues, gating of 80 percent of the hidden units for each task, and a quadratic penalty on changes to important weights in the spirit of Kirkpatrick et al. (2017); Figure 11.3 compares the network of Hopfield (1982) with the modern Hopfield network of Ramsauer et al. (2021). The values in Figure 11.5 are from Horowitz (2014). Figure 11.6 is schematic, after Neftci, Mostafa, and Zenke (2019). Figure 11.7 uses the definition of reward of Keramati and Gutkin (2014) with illustrative parameters. Figures 11.1 and 11.4 are schematic, and the judgments in them are the author's.

## Epigraph

Richard P. Feynman, words written on his blackboard at the California Institute of Technology, photographed at the time of his death in February 1988. Caltech Archives, Caltech Images Collection, image 1.10-29, "Richard Feynman's blackboard at time of his death."

## References

Ambrogio, S., Narayanan, P., Okazaki, A., Fasoli, A., Mackin, C., Hosokawa, K., Nomura, A., Yasuda, T., Chen, A., Friz, A., Ishii, M., Luquin, J., Kohda, Y., Saulnier, N., Brew, K., Choi, S., Ok, I., Philip, T., Chan, V., … Burr, G. W. (2023). An analog-AI chip for energy-efficient speech recognition and transcription. *Nature*, 620(7975), 768–775.

Ambrose, R. E., Pfeiffer, B. E., & Foster, D. J. (2016). Reverse replay of hippocampal place cells is uniquely modulated by changing reward. *Neuron*, 91(5), 1124–1136.

Amit, D. J., Gutfreund, H., & Sompolinsky, H. (1985). Storing infinite numbers of patterns in a spin-glass model of neural networks. *Physical Review Letters*, 55(14), 1530–1533.

Ba, J., Hinton, G. E., Mnih, V., Leibo, J. Z., & Ionescu, C. (2016). Using fast weights to attend to the recent past. In *Advances in Neural Information Processing Systems 29* (pp. 4331–4339).

Banino, A., Balaguer, J., & Blundell, C. (2021). PonderNet: Learning to ponder. *arXiv*, 2107.05407.

Behrens, T. E. J., Woolrich, M. W., Walton, M. E., & Rushworth, M. F. S. (2007). Learning the value of information in an uncertain world. *Nature Neuroscience*, 10(9), 1214–1221.

Behrouz, A., Zhong, P., & Mirrokni, V. (2025). Titans: Learning to memorize at test time. In *Advances in Neural Information Processing Systems 38*. Preprint arXiv:2501.00663.

Bellec, G., Scherr, F., Subramoney, A., Hajek, E., Salaj, D., Legenstein, R., & Maass, W. (2020). A solution to the learning dilemma for recurrent networks of spiking neurons. *Nature Communications*, 11, 3625.

Bengio, Y., Louradour, J., Collobert, R., & Weston, J. (2009). Curriculum learning. In *Proceedings of the 26th Annual International Conference on Machine Learning* (pp. 41–48). ACM.

Benna, M. K., & Fusi, S. (2016). Computational principles of synaptic memory consolidation. *Nature Neuroscience*, 19(12), 1697–1706.

Biderman, D., Portes, J., Gonzalez Ortiz, J. J., Paul, M., Greengard, P., Jennings, C., King, D., Havens, S., Chiley, V., Frankle, J., Blakeney, C., & Cunningham, J. P. (2024). LoRA learns less and forgets less. *Transactions on Machine Learning Research*.

Borgeaud, S., Mensch, A., Hoffmann, J., Cai, T., Rutherford, E., Millican, K., van den Driessche, G., Lespiau, J.-B., Damoc, B., Clark, A., de Las Casas, D., Guy, A., Menick, J., Ring, R., Hennigan, T., Huang, S., Maggiore, L., Jones, C., Cassirer, A., … Sifre, L. (2022). Improving language models by retrieving from trillions of tokens. In *Proceedings of the 39th International Conference on Machine Learning* (pp. 2206–2240). PMLR.

Botvinick, M. M., Braver, T. S., Barch, D. M., Carter, C. S., & Cohen, J. D. (2001). Conflict monitoring and cognitive control. *Psychological Review*, 108(3), 624–652.

Burda, Y., Edwards, H., Pathak, D., Storkey, A., Darrell, T., & Efros, A. A. (2019). Large-scale study of curiosity-driven learning. In *International Conference on Learning Representations*.

Christiano, P. F., Leike, J., Brown, T. B., Martic, M., Legg, S., & Amodei, D. (2017). Deep reinforcement learning from human preferences. In *Advances in Neural Information Processing Systems 30* (pp. 4299–4307).

Cichon, J., & Gan, W.-B. (2015). Branch-specific dendritic Ca2+ spikes cause persistent synaptic plasticity. *Nature*, 520(7546), 180–185.

Clark, J., & Amodei, D. (2016, December 21). *Faulty reward functions in the wild*. OpenAI.

Dapello, J., Marques, T., Schrimpf, M., Geiger, F., Cox, D. D., & DiCarlo, J. J. (2020). Simulating a primary visual cortex at the front of CNNs improves robustness to image perturbations. In *Advances in Neural Information Processing Systems 33* (pp. 13073–13087).

DeepSeek-AI. (2025). *DeepSeek-V3.1-Base* [Model card]. Hugging Face. The model was built by continued training of the DeepSeek-V3 checkpoint on about 840 billion further tokens.

Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., & Houlsby, N. (2021). An image is worth 16x16 words: Transformers for image recognition at scale. In *International Conference on Learning Representations*.

Doya, K. (2002). Metalearning and neuromodulation. *Neural Networks*, 15(4–6), 495–506.

Elman, J. L. (1993). Learning and development in neural networks: The importance of starting small. *Cognition*, 48(1), 71–99.

Fildes, J. (2009, July 22). Artificial brain “10 years away.” *BBC News*.

Fong, R. C., Scheirer, W. J., & Cox, D. D. (2018). Using human brain activity to guide machine learning. *Scientific Reports*, 8, 5397.

Gal, Y., & Ghahramani, Z. (2016). Dropout as a Bayesian approximation: Representing model uncertainty in deep learning. In *Proceedings of the 33rd International Conference on Machine Learning* (pp. 1050–1059). PMLR.

Gao, L., Schulman, J., & Hilton, J. (2023). Scaling laws for reward model overoptimization. In *Proceedings of the 40th International Conference on Machine Learning* (pp. 10835–10866). PMLR.

Gekhman, Z., Yona, G., Aharoni, R., Eyal, M., Feder, A., Reichart, R., & Herzig, J. (2024). Does fine-tuning LLMs on new knowledge encourage hallucinations? In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing* (pp. 7765–7784). Association for Computational Linguistics.

Gottlieb, J., Oudeyer, P.-Y., Lopes, M., & Baranes, A. (2013). Information-seeking, curiosity, and attention: Computational and neural mechanisms. *Trends in Cognitive Sciences*, 17(11), 585–593.

Grattafiori, A., Dubey, A., Jauhri, A., Pandey, A., Kadian, A., et al. (2024). The Llama 3 herd of models. *arXiv*, 2407.21783.

Graves, A. (2016). Adaptive computation time for recurrent neural networks. *arXiv*, 1603.08983.

Hassabis, D., Kumaran, D., Summerfield, C., & Botvinick, M. (2017). Neuroscience-inspired artificial intelligence. *Neuron*, 95(2), 245–258.

Hayes, T. L., Krishnan, G. P., Bazhenov, M., Siegelmann, H. T., Sejnowski, T. J., & Kanan, C. (2021). Replay in deep learning: Current approaches and missing biological elements. *Neural Computation*, 33(11), 2908–2950.

Hinton, G. (2022). The forward-forward algorithm: Some preliminary investigations. *arXiv*, 2212.13345.

Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective computational abilities. *Proceedings of the National Academy of Sciences*, 79(8), 2554–2558.

Horowitz, M. (2014). Computing's energy problem (and what we can do about it). In *2014 IEEE International Solid-State Circuits Conference Digest of Technical Papers* (pp. 10–14). IEEE.

Intel. (2024, April 17). *Intel builds world's largest neuromorphic system to enable more sustainable AI* [Press release].

Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. (2025). Why language models hallucinate. *arXiv*, 2509.04664.

Kelly, F. C. (1943). *The Wright Brothers*. Harcourt, Brace.

Kepecs, A., Uchida, N., Zariwala, H. A., & Mainen, Z. F. (2008). Neural correlates, computation and behavioural impact of decision confidence. *Nature*, 455(7210), 227–231.

Keramati, M., & Gutkin, B. (2014). Homeostatic reinforcement learning for integrating reward collection and physiological stability. *eLife*, 3, e04811.

Kidd, C., & Hayden, B. Y. (2015). The psychology and neuroscience of curiosity. *Neuron*, 88(3), 449–460.

Kingma, D. P., & Ba, J. (2015). Adam: A method for stochastic optimization. In *International Conference on Learning Representations*.

Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A., Hassabis, D., Clopath, C., Kumaran, D., & Hadsell, R. (2017). Overcoming catastrophic forgetting in neural networks. *Proceedings of the National Academy of Sciences*, 114(13), 3521–3526.

Krakovna, V., Uesato, J., Mikulik, V., Rahtz, M., Everitt, T., Kumar, R., Kenton, Z., Leike, J., & Legg, S. (2020, April 21). *Specification gaming: The flip side of AI ingenuity*. DeepMind Blog.

Krotov, D., & Hopfield, J. J. (2016). Dense associative memory for pattern recognition. In *Advances in Neural Information Processing Systems 29* (pp. 1172–1180).

Laborieux, A., Ernoult, M., Hirtzlin, T., & Querlioz, D. (2021). Synaptic metaplasticity in binarized neural networks. *Nature Communications*, 12, 2549.

Lakshminarayanan, B., Pritzel, A., & Blundell, C. (2017). Simple and scalable predictive uncertainty estimation using deep ensembles. In *Advances in Neural Information Processing Systems 30* (pp. 6402–6413).

Levy, W. B., & Calvert, V. G. (2021). Communication consumes 35 times more energy than computation in the human cortex, but both costs are needed to predict synapse number. *Proceedings of the National Academy of Sciences*, 118(18), e2008173118.

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. In *Advances in Neural Information Processing Systems 33* (pp. 9459–9474).

Li, Z., Brendel, W., Walker, E. Y., Cobos, E., Muhammad, T., Reimer, J., Bethge, M., Sinz, F. H., Pitkow, X., & Tolias, A. S. (2019). Learning from brains how to regularize machines. In *Advances in Neural Information Processing Systems 32*.

Li, Z., You, C., Bhojanapalli, S., Li, D., Rawat, A. S., Reddi, S. J., Ye, K., Chern, F., Yu, F., Guo, R., & Kumar, S. (2023). The lazy neuron phenomenon: On emergence of activation sparsity in transformers. In *International Conference on Learning Representations*.

Logan, G. D., & Crump, M. J. C. (2010). Cognitive illusions of authorship reveal hierarchical error detection in skilled typists. *Science*, 330(6004), 683–686.

Luo, Y., Yang, Z., Meng, F., Li, Y., Zhou, J., & Zhang, Y. (2025). An empirical study of catastrophic forgetting in large language models during continual fine-tuning. *IEEE Transactions on Audio, Speech and Language Processing*, 33, 3776–3786.

Man, K., & Damasio, A. (2019). Homeostasis and soft robotics in the design of feeling machines. *Nature Machine Intelligence*, 1(10), 446–452.

Markram, H., Muller, E., Ramaswamy, S., Reimann, M. W., Abdellah, M., Sanchez, C. A., Ailamaki, A., Alonso-Nanclares, L., Antille, N., Arsever, S., Kahou, G. A. A., Berger, T. K., Bilgili, A., Buncic, N., Chalimourda, A., Chindemi, G., Courcol, J.-D., Delalondre, F., Delattre, V., … Schürmann, F. (2015). Reconstruction and simulation of neocortical microcircuitry. *Cell*, 163(2), 456–492.

Masse, N. Y., Grant, G. D., & Freedman, D. J. (2018). Alleviating catastrophic forgetting using context-dependent gating and synaptic stabilization. *Proceedings of the National Academy of Sciences*, 115(44), E10467–E10475.

Mattar, M. G., & Daw, N. D. (2018). Prioritized memory access explains planning and hippocampal replay. *Nature Neuroscience*, 21(11), 1609–1617.

Miconi, T., Clune, J., & Stanley, K. O. (2018). Differentiable plasticity: Training plastic neural networks with backpropagation. In *Proceedings of the 35th International Conference on Machine Learning* (pp. 3559–3568). PMLR.

Miconi, T., Rawal, A., Clune, J., & Stanley, K. O. (2019). Backpropamine: Training self-modifying neural networks with differentiable neuromodulated plasticity. In *International Conference on Learning Representations*.

Modha, D. S., Akopyan, F., Andreopoulos, A., Appuswamy, R., Arthur, J. V., Cassidy, A. S., Datta, P., DeBole, M. V., Esser, S. K., Otero, C. O., Sawada, J., Taba, B., Amir, A., Bablani, D., Carlson, P. J., Flickner, M. D., Gandhasri, R., Garreau, G. J., Ito, M., … Ueda, T. (2023). Neural inference at the frontier of energy, space, and time. *Science*, 382(6668), 329–335.

Momeni, A., Rahmani, B., Scellier, B., Wright, L. G., McMahon, P. L., Wanjura, C. C., Li, Y., Skalli, A., Berloff, N. G., Onodera, T., Oguz, I., Morichetti, F., del Hougne, P., Le Gallo, M., Sebastian, A., Mirhoseini, A., Zhang, C., Marković, D., Brunner, D., … Fleury, R. (2025). Training of physical neural networks. *Nature*, 645(8079), 53–61.

Neftci, E. O., Mostafa, H., & Zenke, F. (2019). Surrogate gradient learning in spiking neural networks: Bringing the power of gradient-based optimization to spiking neural networks. *IEEE Signal Processing Magazine*, 36(6), 51–63.

Open message to the European Commission concerning the Human Brain Project. (2014, July 7). Retrieved from neurofuture.eu.

Orhan, A. E., & Lake, B. M. (2024). Learning high-level visual representations from a child's perspective without strong inductive biases. *Nature Machine Intelligence*, 6(3), 271–283.

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P., Leike, J., & Lowe, R. (2022). Training language models to follow instructions with human feedback. In *Advances in Neural Information Processing Systems 35* (pp. 27730–27744).

Pathak, D., Agrawal, P., Efros, A. A., & Darrell, T. (2017). Curiosity-driven exploration by self-supervised prediction. In *Proceedings of the 34th International Conference on Machine Learning* (pp. 2778–2787). PMLR.

Ramsauer, H., Schäfl, B., Lehner, J., Seidl, P., Widrich, M., Adler, T., Gruber, L., Holzleitner, M., Pavlović, M., Sandve, G. K., Greiff, V., Kreil, D., Kopp, M., Klambauer, G., Brandstetter, J., & Hochreiter, S. (2021). Hopfield networks is all you need. In *International Conference on Learning Representations*.

Rohde, D. L. T., & Plaut, D. C. (1999). Language acquisition in the absence of explicit negative evidence: How important is starting small? *Cognition*, 72(1), 67–109.

Safarani, S., Nix, A., Willeke, K., Cadena, S. A., Restivo, K., Denfield, G., Tolias, A. S., & Sinz, F. H. (2021). Towards robust vision by multi-task learning on monkey visual cortex. In *Advances in Neural Information Processing Systems 34* (pp. 739–751).

Scellier, B., & Bengio, Y. (2017). Equilibrium propagation: Bridging the gap between energy-based models and backpropagation. *Frontiers in Computational Neuroscience*, 11, 24.

Schaul, T., Quan, J., Antonoglou, I., & Silver, D. (2016). Prioritized experience replay. In *International Conference on Learning Representations*.

Schlag, I., Irie, K., & Schmidhuber, J. (2021). Linear transformers are secretly fast weight programmers. In *Proceedings of the 38th International Conference on Machine Learning* (pp. 9355–9366). PMLR.

Schmidhuber, J. (1991). A possibility for implementing curiosity and boredom in model-building neural controllers. In J.-A. Meyer & S. W. Wilson (Eds.), *From Animals to Animats: Proceedings of the First International Conference on Simulation of Adaptive Behavior* (pp. 222–227). MIT Press.

Schmidhuber, J. (1992). Learning to control fast-weight memories: An alternative to dynamic recurrent networks. *Neural Computation*, 4(1), 131–139.

Sheybani, S., Hansaria, H., Wood, J. N., Smith, L. B., & Tiganj, Z. (2023). Curriculum learning with infant egocentric videos. In *Advances in Neural Information Processing Systems 36* (pp. 54199–54212).

Sinz, F. H., Pitkow, X., Reimer, J., Bethge, M., & Tolias, A. S. (2019). Engineering a less artificial intelligence. *Neuron*, 103(6), 967–979.

Tadros, T., Krishnan, G. P., Ramyaa, R., & Bazhenov, M. (2022). Sleep-like unsupervised replay reduces catastrophic forgetting in artificial neural networks. *Nature Communications*, 13, 7742.

Teyler, T. J., & DiScenna, P. (1986). The hippocampal memory indexing theory. *Behavioral Neuroscience*, 100(2), 147–154.

The Royal Swedish Academy of Sciences. (2024, October 8). *The Nobel Prize in Physics 2024* [Press release]. NobelPrize.org.

van de Ven, G. M., Siegelmann, H. T., & Tolias, A. S. (2020). Brain-inspired replay for continual learning with artificial neural networks. *Nature Communications*, 11, 4069.

Vogelsang, L., Gilad-Gutnick, S., Ehrenberg, E., Yonas, A., Diamond, S., Held, R., & Sinha, P. (2018). Potential downside of high initial visual acuity. *Proceedings of the National Academy of Sciences*, 115(44), 11333–11338.

Wang, J. X., Kurth-Nelson, Z., Kumaran, D., Tirumala, D., Soyer, H., Leibo, J. Z., Hassabis, D., & Botvinick, M. (2018). Prefrontal cortex as a meta-reinforcement learning system. *Nature Neuroscience*, 21(6), 860–868.

Whittington, J. C. R., Warren, J., & Behrens, T. E. J. (2022). Relating transformers to models and neural representations of the hippocampal formation. In *International Conference on Learning Representations*.

Wright, L. G., Onodera, T., Stein, M. M., Wang, T., Schachter, D. T., Hu, Z., & McMahon, P. L. (2022). Deep physical neural networks trained with backpropagation. *Nature*, 601(7894), 549–555.

Wright, W. (1900, May 13). Letter to Octave Chanute. Wilbur and Orville Wright Papers, Library of Congress. Reprinted in M. W. McFarland (Ed.), *The Papers of Wilbur and Orville Wright* (Vol. 1). McGraw-Hill, 1953.

Wright, W. (1901). Some aeronautical experiments. *Journal of the Western Society of Engineers*, 6, 489–510.

Yang, G., Pan, F., & Gan, W.-B. (2009). Stably maintained dendritic spines are associated with lifelong memories. *Nature*, 462(7275), 920–924.

Zador, A., Escola, S., Richards, B., Ölveczky, B., Bengio, Y., Boahen, K., Botvinick, M., Chklovskii, D., Churchland, A., Clopath, C., DiCarlo, J., Ganguli, S., Hawkins, J., Körding, K., Koulakov, A., LeCun, Y., Lillicrap, T., Marblestone, A., Olshausen, B., … Tsao, D. (2023). Catalyzing next-generation artificial intelligence through NeuroAI. *Nature Communications*, 14, 1597.

Zenke, F., Poole, B., & Ganguli, S. (2017). Continual learning through synaptic intelligence. In *Proceedings of the 34th International Conference on Machine Learning* (pp. 3987–3995). PMLR.

[^1]: Kelly, F. C. (1943). *The Wright Brothers*. Harcourt, Brace.

[^2]: Wright, W. (1900, May 13). Letter to Octave Chanute. Wilbur and Orville Wright Papers, Library of Congress. Reprinted in M. W. McFarland (Ed.), *The Papers of Wilbur and Orville Wright* (Vol. 1). McGraw-Hill, 1953.

[^3]: Wright, W. (1901). Some aeronautical experiments. *Journal of the Western Society of Engineers*, 6, 489–510.

[^4]: Fildes, J. (2009, July 22). Artificial brain “10 years away.” *BBC News*.

[^5]: Open message to the European Commission concerning the Human Brain Project. (2014, July 7). Retrieved from neurofuture.eu.

[^6]: Markram, H., Muller, E., Ramaswamy, S., Reimann, M. W., Abdellah, M., Sanchez, C. A., Ailamaki, A., Alonso-Nanclares, L., Antille, N., Arsever, S., Kahou, G. A. A., Berger, T. K., Bilgili, A., Buncic, N., Chalimourda, A., Chindemi, G., Courcol, J.-D., Delalondre, F., Delattre, V., … Schürmann, F. (2015). Reconstruction and simulation of neocortical microcircuitry. *Cell*, 163(2), 456–492.

[^7]: Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., & Houlsby, N. (2021). An image is worth 16x16 words: Transformers for image recognition at scale. In *International Conference on Learning Representations*.

[^8]: Hassabis, D., Kumaran, D., Summerfield, C., & Botvinick, M. (2017). Neuroscience-inspired artificial intelligence. *Neuron*, 95(2), 245–258.

[^9]: Sinz, F. H., Pitkow, X., Reimer, J., Bethge, M., & Tolias, A. S. (2019). Engineering a less artificial intelligence. *Neuron*, 103(6), 967–979.

[^10]: van de Ven, G. M., Siegelmann, H. T., & Tolias, A. S. (2020). Brain-inspired replay for continual learning with artificial neural networks. *Nature Communications*, 11, 4069.

[^11]: Tadros, T., Krishnan, G. P., Ramyaa, R., & Bazhenov, M. (2022). Sleep-like unsupervised replay reduces catastrophic forgetting in artificial neural networks. *Nature Communications*, 13, 7742.

[^12]: Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A., Hassabis, D., Clopath, C., Kumaran, D., & Hadsell, R. (2017). Overcoming catastrophic forgetting in neural networks. *Proceedings of the National Academy of Sciences*, 114(13), 3521–3526; Yang, G., Pan, F., & Gan, W.-B. (2009). Stably maintained dendritic spines are associated with lifelong memories. *Nature*, 462(7275), 920–924; Zenke, F., Poole, B., & Ganguli, S. (2017). Continual learning through synaptic intelligence. In *Proceedings of the 34th International Conference on Machine Learning* (pp. 3987–3995). PMLR.

[^13]: Benna, M. K., & Fusi, S. (2016). Computational principles of synaptic memory consolidation. *Nature Neuroscience*, 19(12), 1697–1706.

[^14]: Laborieux, A., Ernoult, M., Hirtzlin, T., & Querlioz, D. (2021). Synaptic metaplasticity in binarized neural networks. *Nature Communications*, 12, 2549.

[^15]: Cichon, J., & Gan, W.-B. (2015). Branch-specific dendritic Ca2+ spikes cause persistent synaptic plasticity. *Nature*, 520(7546), 180–185.

[^16]: Masse, N. Y., Grant, G. D., & Freedman, D. J. (2018). Alleviating catastrophic forgetting using context-dependent gating and synaptic stabilization. *Proceedings of the National Academy of Sciences*, 115(44), E10467–E10475.

[^17]: Luo, Y., Yang, Z., Meng, F., Li, Y., Zhou, J., & Zhang, Y. (2025). An empirical study of catastrophic forgetting in large language models during continual fine-tuning. *IEEE Transactions on Audio, Speech and Language Processing*, 33, 3776–3786; Biderman, D., Portes, J., Gonzalez Ortiz, J. J., Paul, M., Greengard, P., Jennings, C., King, D., Havens, S., Chiley, V., Frankle, J., Blakeney, C., & Cunningham, J. P. (2024). LoRA learns less and forgets less. *Transactions on Machine Learning Research*.

[^18]: Gekhman, Z., Yona, G., Aharoni, R., Eyal, M., Feder, A., Reichart, R., & Herzig, J. (2024). Does fine-tuning LLMs on new knowledge encourage hallucinations? In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing* (pp. 7765–7784). Association for Computational Linguistics.

[^19]: DeepSeek-AI. (2025). *DeepSeek-V3.1-Base* [Model card]. Hugging Face. The model was built by continued training of the DeepSeek-V3 checkpoint on about 840 billion further tokens.

[^20]: Ambrose, R. E., Pfeiffer, B. E., & Foster, D. J. (2016). Reverse replay of hippocampal place cells is uniquely modulated by changing reward. *Neuron*, 91(5), 1124–1136.

[^21]: Mattar, M. G., & Daw, N. D. (2018). Prioritized memory access explains planning and hippocampal replay. *Nature Neuroscience*, 21(11), 1609–1617.

[^22]: Schaul, T., Quan, J., Antonoglou, I., & Silver, D. (2016). Prioritized experience replay. In *International Conference on Learning Representations*.

[^23]: Hayes, T. L., Krishnan, G. P., Bazhenov, M., Siegelmann, H. T., Sejnowski, T. J., & Kanan, C. (2021). Replay in deep learning: Current approaches and missing biological elements. *Neural Computation*, 33(11), 2908–2950.

[^24]: Teyler, T. J., & DiScenna, P. (1986). The hippocampal memory indexing theory. *Behavioral Neuroscience*, 100(2), 147–154.

[^25]: Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. In *Advances in Neural Information Processing Systems 33* (pp. 9459–9474).

[^26]: Borgeaud, S., Mensch, A., Hoffmann, J., Cai, T., Rutherford, E., Millican, K., van den Driessche, G., Lespiau, J.-B., Damoc, B., Clark, A., de Las Casas, D., Guy, A., Menick, J., Ring, R., Hennigan, T., Huang, S., Maggiore, L., Jones, C., Cassirer, A., … Sifre, L. (2022). Improving language models by retrieving from trillions of tokens. In *Proceedings of the 39th International Conference on Machine Learning* (pp. 2206–2240). PMLR.

[^27]: Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective computational abilities. *Proceedings of the National Academy of Sciences*, 79(8), 2554–2558; The Royal Swedish Academy of Sciences. (2024, October 8). *The Nobel Prize in Physics 2024* [Press release]. NobelPrize.org.

[^28]: Amit, D. J., Gutfreund, H., & Sompolinsky, H. (1985). Storing infinite numbers of patterns in a spin-glass model of neural networks. *Physical Review Letters*, 55(14), 1530–1533.

[^29]: Krotov, D., & Hopfield, J. J. (2016). Dense associative memory for pattern recognition. In *Advances in Neural Information Processing Systems 29* (pp. 1172–1180); Ramsauer, H., Schäfl, B., Lehner, J., Seidl, P., Widrich, M., Adler, T., Gruber, L., Holzleitner, M., Pavlović, M., Sandve, G. K., Greiff, V., Kreil, D., Kopp, M., Klambauer, G., Brandstetter, J., & Hochreiter, S. (2021). Hopfield networks is all you need. In *International Conference on Learning Representations*.

[^30]: Ba, J., Hinton, G. E., Mnih, V., Leibo, J. Z., & Ionescu, C. (2016). Using fast weights to attend to the recent past. In *Advances in Neural Information Processing Systems 29* (pp. 4331–4339).

[^31]: Schlag, I., Irie, K., & Schmidhuber, J. (2021). Linear transformers are secretly fast weight programmers. In *Proceedings of the 38th International Conference on Machine Learning* (pp. 9355–9366). PMLR; Schmidhuber, J. (1992). Learning to control fast-weight memories: An alternative to dynamic recurrent networks. *Neural Computation*, 4(1), 131–139.

[^32]: Whittington, J. C. R., Warren, J., & Behrens, T. E. J. (2022). Relating transformers to models and neural representations of the hippocampal formation. In *International Conference on Learning Representations*.

[^33]: Behrouz, A., Zhong, P., & Mirrokni, V. (2025). Titans: Learning to memorize at test time. In *Advances in Neural Information Processing Systems 38*. Preprint arXiv:2501.00663.

[^34]: Behrens, T. E. J., Woolrich, M. W., Walton, M. E., & Rushworth, M. F. S. (2007). Learning the value of information in an uncertain world. *Nature Neuroscience*, 10(9), 1214–1221.

[^35]: Kingma, D. P., & Ba, J. (2015). Adam: A method for stochastic optimization. In *International Conference on Learning Representations*.

[^36]: Doya, K. (2002). Metalearning and neuromodulation. *Neural Networks*, 15(4–6), 495–506.

[^37]: Miconi, T., Clune, J., & Stanley, K. O. (2018). Differentiable plasticity: Training plastic neural networks with backpropagation. In *Proceedings of the 35th International Conference on Machine Learning* (pp. 3559–3568). PMLR.

[^38]: Miconi, T., Rawal, A., Clune, J., & Stanley, K. O. (2019). Backpropamine: Training self-modifying neural networks with differentiable neuromodulated plasticity. In *International Conference on Learning Representations*.

[^39]: Wang, J. X., Kurth-Nelson, Z., Kumaran, D., Tirumala, D., Soyer, H., Leibo, J. Z., Hassabis, D., & Botvinick, M. (2018). Prefrontal cortex as a meta-reinforcement learning system. *Nature Neuroscience*, 21(6), 860–868.

[^40]: Horowitz, M. (2014). Computing's energy problem (and what we can do about it). In *2014 IEEE International Solid-State Circuits Conference Digest of Technical Papers* (pp. 10–14). IEEE.

[^41]: Levy, W. B., & Calvert, V. G. (2021). Communication consumes 35 times more energy than computation in the human cortex, but both costs are needed to predict synapse number. *Proceedings of the National Academy of Sciences*, 118(18), e2008173118.

[^42]: Modha, D. S., Akopyan, F., Andreopoulos, A., Appuswamy, R., Arthur, J. V., Cassidy, A. S., Datta, P., DeBole, M. V., Esser, S. K., Otero, C. O., Sawada, J., Taba, B., Amir, A., Bablani, D., Carlson, P. J., Flickner, M. D., Gandhasri, R., Garreau, G. J., Ito, M., … Ueda, T. (2023). Neural inference at the frontier of energy, space, and time. *Science*, 382(6668), 329–335.

[^43]: Ambrogio, S., Narayanan, P., Okazaki, A., Fasoli, A., Mackin, C., Hosokawa, K., Nomura, A., Yasuda, T., Chen, A., Friz, A., Ishii, M., Luquin, J., Kohda, Y., Saulnier, N., Brew, K., Choi, S., Ok, I., Philip, T., Chan, V., … Burr, G. W. (2023). An analog-AI chip for energy-efficient speech recognition and transcription. *Nature*, 620(7975), 768–775.

[^44]: Intel. (2024, April 17). *Intel builds world's largest neuromorphic system to enable more sustainable AI* [Press release].

[^45]: Neftci, E. O., Mostafa, H., & Zenke, F. (2019). Surrogate gradient learning in spiking neural networks: Bringing the power of gradient-based optimization to spiking neural networks. *IEEE Signal Processing Magazine*, 36(6), 51–63.

[^46]: Bellec, G., Scherr, F., Subramoney, A., Hajek, E., Salaj, D., Legenstein, R., & Maass, W. (2020). A solution to the learning dilemma for recurrent networks of spiking neurons. *Nature Communications*, 11, 3625.

[^47]: Scellier, B., & Bengio, Y. (2017). Equilibrium propagation: Bridging the gap between energy-based models and backpropagation. *Frontiers in Computational Neuroscience*, 11, 24.

[^48]: Hinton, G. (2022). The forward-forward algorithm: Some preliminary investigations. *arXiv*, 2212.13345.

[^49]: Wright, L. G., Onodera, T., Stein, M. M., Wang, T., Schachter, D. T., Hu, Z., & McMahon, P. L. (2022). Deep physical neural networks trained with backpropagation. *Nature*, 601(7894), 549–555; Momeni, A., Rahmani, B., Scellier, B., Wright, L. G., McMahon, P. L., Wanjura, C. C., Li, Y., Skalli, A., Berloff, N. G., Onodera, T., Oguz, I., Morichetti, F., del Hougne, P., Le Gallo, M., Sebastian, A., Mirhoseini, A., Zhang, C., Marković, D., Brunner, D., … Fleury, R. (2025). Training of physical neural networks. *Nature*, 645(8079), 53–61.

[^50]: Li, Z., You, C., Bhojanapalli, S., Li, D., Rawat, A. S., Reddi, S. J., Ye, K., Chern, F., Yu, F., Guo, R., & Kumar, S. (2023). The lazy neuron phenomenon: On emergence of activation sparsity in transformers. In *International Conference on Learning Representations*.

[^51]: Clark, J., & Amodei, D. (2016, December 21). *Faulty reward functions in the wild*. OpenAI.

[^52]: Krakovna, V., Uesato, J., Mikulik, V., Rahtz, M., Everitt, T., Kumar, R., Kenton, Z., Leike, J., & Legg, S. (2020, April 21). *Specification gaming: The flip side of AI ingenuity*. DeepMind Blog.

[^53]: Christiano, P. F., Leike, J., Brown, T. B., Martic, M., Legg, S., & Amodei, D. (2017). Deep reinforcement learning from human preferences. In *Advances in Neural Information Processing Systems 30* (pp. 4299–4307); Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P., Leike, J., & Lowe, R. (2022). Training language models to follow instructions with human feedback. In *Advances in Neural Information Processing Systems 35* (pp. 27730–27744).

[^54]: Gao, L., Schulman, J., & Hilton, J. (2023). Scaling laws for reward model overoptimization. In *Proceedings of the 40th International Conference on Machine Learning* (pp. 10835–10866). PMLR.

[^55]: Keramati, M., & Gutkin, B. (2014). Homeostatic reinforcement learning for integrating reward collection and physiological stability. *eLife*, 3, e04811.

[^56]: Man, K., & Damasio, A. (2019). Homeostasis and soft robotics in the design of feeling machines. *Nature Machine Intelligence*, 1(10), 446–452.

[^57]: Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P., Leike, J., & Lowe, R. (2022). Training language models to follow instructions with human feedback. In *Advances in Neural Information Processing Systems 35* (pp. 27730–27744).

[^58]: Schmidhuber, J. (1991). A possibility for implementing curiosity and boredom in model-building neural controllers. In J.-A. Meyer & S. W. Wilson (Eds.), *From Animals to Animats: Proceedings of the First International Conference on Simulation of Adaptive Behavior* (pp. 222–227). MIT Press.

[^59]: Pathak, D., Agrawal, P., Efros, A. A., & Darrell, T. (2017). Curiosity-driven exploration by self-supervised prediction. In *Proceedings of the 34th International Conference on Machine Learning* (pp. 2778–2787). PMLR.

[^60]: Burda, Y., Edwards, H., Pathak, D., Storkey, A., Darrell, T., & Efros, A. A. (2019). Large-scale study of curiosity-driven learning. In *International Conference on Learning Representations*.

[^61]: Gottlieb, J., Oudeyer, P.-Y., Lopes, M., & Baranes, A. (2013). Information-seeking, curiosity, and attention: Computational and neural mechanisms. *Trends in Cognitive Sciences*, 17(11), 585–593; Kidd, C., & Hayden, B. Y. (2015). The psychology and neuroscience of curiosity. *Neuron*, 88(3), 449–460.

[^62]: Kepecs, A., Uchida, N., Zariwala, H. A., & Mainen, Z. F. (2008). Neural correlates, computation and behavioural impact of decision confidence. *Nature*, 455(7210), 227–231; Botvinick, M. M., Braver, T. S., Barch, D. M., Carter, C. S., & Cohen, J. D. (2001). Conflict monitoring and cognitive control. *Psychological Review*, 108(3), 624–652.

[^63]: Graves, A. (2016). Adaptive computation time for recurrent neural networks. *arXiv*, 1603.08983; Banino, A., Balaguer, J., & Blundell, C. (2021). PonderNet: Learning to ponder. *arXiv*, 2107.05407; Lakshminarayanan, B., Pritzel, A., & Blundell, C. (2017). Simple and scalable predictive uncertainty estimation using deep ensembles. In *Advances in Neural Information Processing Systems 30* (pp. 6402–6413); Gal, Y., & Ghahramani, Z. (2016). Dropout as a Bayesian approximation: Representing model uncertainty in deep learning. In *Proceedings of the 33rd International Conference on Machine Learning* (pp. 1050–1059). PMLR.

[^64]: Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. (2025). Why language models hallucinate. *arXiv*, 2509.04664.

[^65]: Logan, G. D., & Crump, M. J. C. (2010). Cognitive illusions of authorship reveal hierarchical error detection in skilled typists. *Science*, 330(6004), 683–686.

[^66]: Vogelsang, L., Gilad-Gutnick, S., Ehrenberg, E., Yonas, A., Diamond, S., Held, R., & Sinha, P. (2018). Potential downside of high initial visual acuity. *Proceedings of the National Academy of Sciences*, 115(44), 11333–11338.

[^67]: Elman, J. L. (1993). Learning and development in neural networks: The importance of starting small. *Cognition*, 48(1), 71–99.

[^68]: Rohde, D. L. T., & Plaut, D. C. (1999). Language acquisition in the absence of explicit negative evidence: How important is starting small? *Cognition*, 72(1), 67–109.

[^69]: Bengio, Y., Louradour, J., Collobert, R., & Weston, J. (2009). Curriculum learning. In *Proceedings of the 26th Annual International Conference on Machine Learning* (pp. 41–48). ACM.

[^70]: Grattafiori, A., Dubey, A., Jauhri, A., Pandey, A., Kadian, A., et al. (2024). The Llama 3 herd of models. *arXiv*, 2407.21783.

[^71]: Sheybani, S., Hansaria, H., Wood, J. N., Smith, L. B., & Tiganj, Z. (2023). Curriculum learning with infant egocentric videos. In *Advances in Neural Information Processing Systems 36* (pp. 54199–54212).

[^72]: Orhan, A. E., & Lake, B. M. (2024). Learning high-level visual representations from a child's perspective without strong inductive biases. *Nature Machine Intelligence*, 6(3), 271–283.

[^73]: Zador, A., Escola, S., Richards, B., Ölveczky, B., Bengio, Y., Boahen, K., Botvinick, M., Chklovskii, D., Churchland, A., Clopath, C., DiCarlo, J., Ganguli, S., Hawkins, J., Körding, K., Koulakov, A., LeCun, Y., Lillicrap, T., Marblestone, A., Olshausen, B., … Tsao, D. (2023). Catalyzing next-generation artificial intelligence through NeuroAI. *Nature Communications*, 14, 1597.

[^74]: Dapello, J., Marques, T., Schrimpf, M., Geiger, F., Cox, D. D., & DiCarlo, J. J. (2020). Simulating a primary visual cortex at the front of CNNs improves robustness to image perturbations. In *Advances in Neural Information Processing Systems 33* (pp. 13073–13087).

[^75]: Li, Z., Brendel, W., Walker, E. Y., Cobos, E., Muhammad, T., Reimer, J., Bethge, M., Sinz, F. H., Pitkow, X., & Tolias, A. S. (2019). Learning from brains how to regularize machines. In *Advances in Neural Information Processing Systems 32*; Fong, R. C., Scheirer, W. J., & Cox, D. D. (2018). Using human brain activity to guide machine learning. *Scientific Reports*, 8, 5397; Safarani, S., Nix, A., Willeke, K., Cadena, S. A., Restivo, K., Denfield, G., Tolias, A. S., & Sinz, F. H. (2021). Towards robust vision by multi-task learning on monkey visual cortex. In *Advances in Neural Information Processing Systems 34* (pp. 739–751).
