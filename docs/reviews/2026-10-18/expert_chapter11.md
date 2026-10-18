# Expert review: Chapter 11, Integrating Brain Mechanisms into AI Models: What Machines Could Borrow from Biology

File: `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md`

Reviewer role: computational neuroscience and machine learning (deep learning, RL, LLMs, NeuroAI). I reviewed the source, `make_figures.py`, and all seven figures. I re-ran both simulations from the script: Figure 11.2 over 20 seeds in four conditions, and Figure 11.3 with 200 cues per point. I checked every callback against the Chapter 3, 4, 5, 7, 8, 9 and 10 files.

## Overall assessment

Technical accuracy score: **4 / 5**

This is a strong chapter and a natural sequel to Chapter 10. It is organized around the right question for each borrowing: what the brain does, what has been built, how well it works, and what is missing. Its choice of studies is what a NeuroAI specialist would choose:
- generative and sleep-like replay;
- Benna-Fusi synapses and metaplasticity;
- Masse's context gating;
- RETRO;
- modern Hopfield networks, attention and fast weights;
- Titans;
- differentiable plasticity;
- Horowitz's energy table;
- NorthPole, the IBM analog chip and Hala Point;
- surrogate gradients and e-prop;
- equilibrium propagation and forward-forward;
- Gao's overoptimization curves;
- homeostatic RL;
- curiosity and the noisy TV;
- Vogelsang, Orhan and Lake;
- VOneNets and neural regularization.

The numbers I checked are right:
- **Masse et al.**: EWC 70.8 and SI 82.3 percent, gating alone 61.4, combined 95.4.
- **Human Brain Project**: about €607M in total, €406M of it from the EU.
- **Markram 2015**: about 31,000 neurons in 0.29 mm³.
- **RETRO**: a 2T-token database, 25× fewer parameters.
- **Horowitz**: 0.1, 3.7, 10, 100 and 1,300 to 2,600 pJ.
- **Levy and Calvert**: 35×.
- **Chips**: NorthPole 25× FPS/W; analog chip 35M PCM devices and 12.4 TOPS/W; Hala Point 1,152 chips, 1.15B neurons, 2,600 W.
- **CoastRunners**: about 20 percent above humans.
- **Orhan and Lake**: 200 h of video, 70 percent of the ImageNet-trained model.
- **VOneNets**: 18 percent.
- **Titans**: NeurIPS 2025.

Both simulations reproduce what the text says.

The problems:
- **One Major.** The chapter's central evidence for its thesis, the "borrowed principle" successes, includes three items that were not borrowed: experience replay, attention as memory, and TD learning. Chapters 5 and 10 of this book themselves call replay a convergence, not a borrowing.
- **Moderate items:**
  - The convolution example is unexamined against the bitter-lesson test the chapter itself sets: vision transformers.
  - Two claims about current LLM practice are outdated: "trained from scratch" and "no particular order".
  - Titans is overstated as "the first serious attempt".
  - Some callbacks are inaccurate.
  - The modern-Hopfield capacity comparison needs one sentence of fairness.

## Major (factually wrong, must fix)

- **Lines 16 (Figure 11.1), 24, 30 and 136: replay, attention, and TD learning were not borrowed from the brain.**
  - **Quotes**: "Hippocampal replay became experience replay, which keeps the principle..." (line 24); "Replay is the obvious borrowing" (line 30); "convolution, replay, and temporal-difference learning kept what a part of the brain does and discarded how it does it" (line 136). Figure 11.1 lists "experience replay · temporal-difference learning · context gating · attention as memory" under "borrow the principle", with "record: most of the successes".
  - **What is wrong**:
    - **Replay.** Lin's experience replay (1992) predates the first recording of hippocampal replay (Wilson and McNaughton, 1994). Chapter 5 (line 168) says explicitly that the two "were recognized as analogs only afterward: a convergence, not a borrowing", and Chapter 10 (line 88) says machine learning "had found the same answer independently".
    - **Attention.** Attention came from machine translation (Bahdanau et al., 2015). This chapter's own line 54 presents its link to Hopfield networks and the hippocampus as a convergence: engineers and neuroscientists "arrived at nearly the same mathematics".
    - **TD learning.** As Chapter 10 now says, TD came from psychological models of conditioning, not from the brain. The dopamine link came afterward.
    - **Context gating.** Of the "principle" column, only convolution (Fukushima, explicitly after Hubel and Wiesel) is a clean case of a borrowing from neuroscience that succeeded in deployed systems. Context gating is a genuine borrowing, but by the chapter's own line 40 it is not used in deployed systems.
    - **Effect on the thesis.** The thesis rests on "the borrowings that have worked took a principle". Counting convergences as borrowings inflates the record and contradicts two earlier chapters.
  - **Fix**:
    - Line 24: "...became convolution and pooling, which keep the principle, the same detector repeated across the visual field, and drop the neurons. Other matches came the other way round: experience replay and attention were invented by engineers and only afterward recognized in the hippocampus, which is evidence of a different kind, that the brain and the engineers had found the same solution to the same problem."
    - Line 30: "Replay is the obvious remedy, one that machine learning found for itself and has used for 30 years..."
    - Line 136: "The borrowings and convergences that have worked share that pattern: convolution, replay, and attention keep what a part of the brain does and discard how it does it."
    - Figure 11.1: split the middle column into "borrowed principles" (convolution, context gating, generative replay) and "convergences" (experience replay, attention as associative memory, TD learning), or add a footnote marker to the convergent items. Change "record: most of the successes" to "record: most of the successes, several of them convergences rather than borrowings".

## Moderate (overstated, contested, or misleading)

- **Lines 16 and 24: the flagship borrowing has itself been tested by the bitter lesson, and the chapter does not say so.** "A principle borrowed from the brain must also pass the test that Chapter 10 called the bitter lesson... Few have yet passed it."
  - **What is wrong**: Convolution is the chapter's model success. It is also the best-known case of a brain-inspired inductive bias being overtaken at scale. Vision transformers, which build in no translation-equivariant local filters, match or beat CNNs once pretrained on enough data, although modernized CNNs (ConvNeXt) remain competitive. A specialist will expect the chapter to say this, because it sharpens the thesis: borrowed principles pay most when data are scarce, and may be absorbed or replaced as data grow. That is exactly why the chapter's data-efficiency borrowings (lines 112 to 116) matter.
  - **Fix**: Add after line 24's convolution sentence: "Even this success has been tested by the bitter lesson. Vision transformers, which build in no such assumption, match convolutional networks once they are trained on enough images, and the advantage of the borrowed principle shows mainly when data are scarce. That is a pattern worth expecting of every borrowing in this chapter."
  - **Cite**: Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., & Houlsby, N. (2021). An image is worth 16x16 words: Transformers for image recognition at scale. In *International Conference on Learning Representations*. arXiv:2010.11929 (well known; not re-verified this round).

- **Line 40: "trained from scratch" no longer describes industry practice.** "Large language models are not taught new knowledge by continued training if it can be avoided. ... The industry's answer to the problem of forgetting has been to avoid it, by training each new model from scratch on everything at once."
  - **What is wrong**: By 2025 to 2026, continued pretraining from an earlier checkpoint is common. For example, DeepSeek-V3.1-Base was built from the DeepSeek-V3 checkpoint by a further two-phase extension of about 840 billion tokens (630B + 209B, per the model card). Late-stage "annealing" or mid-training on new data mixes is standard. New knowledge is mostly added through retrieval. The real point stands: when weights are updated, old data are mixed back in (rehearsal at scale) rather than relying on any brain-like protection.
  - **Fix**: "The industry's answer to the problem of forgetting has been to sidestep it: new knowledge is added mostly by retrieval, and when a model's weights are updated, by continued training on a mixture that includes much of the old data, which is replay at enormous scale, or by training a new model altogether."
  - **Cite**: DeepSeek-AI. (2025). *DeepSeek-V3.1-Base* [Model card]. Hugging Face. https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Base (token counts verified from the model card).

- **Line 114: "the largest models are trained on data in no particular order" is wrong.**
  - **What is wrong**: Large-model pretraining schedules change the data mixture during training and end with an annealing phase on the highest-quality data. Llama 3 upsampled high-quality code and mathematics in its final phase, and this improved the 8B model's GSM8K score by 24 points. This is a coarse curriculum, ordered by quality rather than difficulty.
  - **Fix**: "The history since has been mixed: ordering examples by difficulty often helps a little and sometimes not at all. The largest models are trained on a coarser curriculum, a mixture of data that shifts during training and ends on the cleanest text, code, and mathematics."
  - **Cite**: Grattafiori, A., et al. (2024). The Llama 3 herd of models. *arXiv*, 2407.21783, §3.1.3 and §3.4 (annealing verified via secondary summaries of the paper; already in the book's Chapter 10 references).

- **Line 56: Titans is not the first serious attempt, and it is not deployed.** "...it is the first serious attempt to give a deployed model what the hippocampus gives a brain: a memory that learns from use, selectively, without retraining."
  - **What is wrong**: Titans (NeurIPS 2025, verified) is a research architecture, not a deployed one. Memories written at test time have precedents: Memorizing Transformers (2022) and test-time-training layers (2024). The description of Titans' surprise signal is accurate: the gradient of the memory's loss, with momentum and decay.
  - **Fix**: "...it is one of the most developed attempts to give a language model what the hippocampus gives a brain: a memory that learns from use, selectively, without retraining."
  - **Cite** (optional): Wu, Y., Rabe, M. N., Hutchins, D., & Szegedy, C. (2022). Memorizing transformers. In *International Conference on Learning Representations*. arXiv:2203.08913 (not re-verified this round).

- **Lines 50 and Figure 11.3: the capacity comparison needs one sentence of fairness.** "Its capacity grows exponentially with the number of units. ... The classical network fails beyond about 15 patterns; the modern one recalled every pattern tested, up to 3,000."
  - **What is wrong**: Both claims are reproduced exactly by the code. But the modern network in the code (and in Ramsauer's formulation) keeps every stored pattern as a separate vector, P × N numbers that grow with each memory. The classical network packs everything into N × N fixed connections. "Capacity per unit" therefore is not like for like, and a specialist reader will object. The point is not a weakness for the chapter. It *is* the chapter's point about the context window, which also keeps every token.
  - **Fix**: Add after "up to 3,000": "The comparison is not quite like for like: the classical network holds all its memories in one fixed set of connections, while the modern one keeps every stored pattern separately and compares the cue with each, as a context window keeps every word it has been shown."
  - **Also**: "Fails beyond about 15" is loose. The simulation gives 89 percent at 12 patterns, 70 at 14, 43 to 47 at 17, about 25 at 20 and 0 at 30. Say "begins to fail at about 12 patterns and recalls fewer than half by 17". Also note that Amit et al.'s 0.14N is the limit for recall with a small fraction of errors. Exact recall from a noisy cue, as in the figure, fails earlier, which explains why the curve falls before 14.

- **Line 62: the claim about learning rates ignores adaptive optimizers.** "...the step size applied to those errors does not depend on whether this is a good moment to learn."
  - **What is wrong**: Every large model is trained with Adam or a variant. These adapt each parameter's step size to the running statistics of its gradients, a partial and automatic analogue of raising the learning rate when signals are consistent and lowering it when they are noisy. They do not respond to surprise or volatility in the world, so the chapter's contrast survives, but it should be stated precisely.
  - **Fix**: "...a global schedule, high early and lower later, which optimizers such as Adam adjust parameter by parameter according to how consistent each one's recent gradients have been, but nothing in it asks whether the world has just changed or whether this is a moment worth learning from."
  - **Cite**: Kingma, D. P., & Ba, J. (2015). Adam: A method for stochastic optimization. In *International Conference on Learning Representations*. arXiv:1412.6980 (not re-verified this round).

- **Line 98: the claim about capped rewards has no citation and misses the deployed example.** "...some proposals for safer reward functions do exactly that, by capping or balancing rewards rather than letting any one grow without limit."
  - **What is wrong**: There is no citation. The most widely deployed mechanism of this kind is the KL penalty in RLHF. It charges the policy for drifting from its starting distribution, so the proxy reward cannot be pursued past a point without cost. Gao et al. (already cited) studied overoptimization with and without it. That is the closest thing in current practice to "rewards that cannot be pursued past a point without costing something the agent also values".
  - **Fix**: "...and the training of current language models already contains a version of the idea: a penalty for drifting too far from the model's starting behavior, which makes the reward model's score more and more expensive to chase.[^50]" Here footnote 50 is Ouyang et al. (2022), already cited.

## Minor

- **Line 26.** "The rest of this chapter follows the brain's solutions in the order Chapter 10 listed them." Chapter 10's sorting paragraph (line 152) lists lifelong learning, honest confidence, frugality, data appetite, values and local rules. Chapter 11's order is different, with confidence near the end. Say "takes up the brain's solutions that Chapter 10 listed".
- **Line 48.** "...the context window ... which Chapter 10 compared to a working memory" is inaccurate. Chapter 10 (line 84) describes the context window but never calls it working memory. Use "which Chapter 10 described as a memory wiped when the conversation ends".
- **Line 50.** "Chapter 5 described John Hopfield's network of 1982" is inaccurate. Chapter 5 (line 104) describes pattern completion and cites Hopfield only in footnote 28, and Chapter 4 (line 122) describes CA3 pattern completion. Use "Chapter 5 described recall as pattern completion, which John Hopfield modeled in 1982 with a network in which..."
- **Line 84.** "...a rule related to the prospective configuration of Chapter 10" uses a term Chapter 10 never introduces. Chapter 10 (line 102) describes Song and Bogacz's settle-then-learn rule without the name. Use "related to the settle-then-learn rule of Song and Bogacz described in Chapter 10".
- **Line 84.** Wright et al. (2022) trained physical networks by "physics-aware training", running the forward pass in the physical system and backpropagating through a digital model. They did not use the system's "own dynamics for learning". Use "...using the physics as the network, and in some cases its own dynamics for learning" (the Momeni et al. 2025 review covers both).
- **Line 22.** "Having received about 600 million euros" is right (€607M in total, of which €406M was EU funding). Consider saying "about 600 million euros, two-thirds of it from the EU", since the promise was €1 billion.
- **Line 36.** The Figure 11.2 explanation, "because every task needs the same few connections", is broadly right. The five tasks share identical cues and differ only in one context input, so without gating they drive nearly the same hidden activity and must share the same weights. I checked this: raising the protection strength 100-fold leaves task 1 at about 2 percent and blocks the new tasks too. "The same connections", not "the same few", is more accurate. The importance estimate in the code is the squared training-loss gradient at the end of each task, an empirical-Fisher variant weaker than EWC's. The docstring's "in the spirit of" covers this.
- **Line 46.** "On the same plan" overstates RAG's resemblance to the index theory. The index theory stores pointers to cortical patterns, while a retrieval system stores the text itself plus an embedding index. Use "on a similar plan".
- **Repetition of earlier chapters.** These recaps are signposted but could be trimmed by a sentence each:
  - Hassabis et al. 2017 (Chapter 10, line 30).
  - Elastic weight consolidation (Chapters 9 and 10).
  - Wang's meta-RL (Chapters 3 and 10).
  - Mixtures of experts (Chapter 10).
  - Graves's adaptive computation time and MC dropout (Chapter 8's AI section).

  Line 106's "Machine learning has had versions of each part for years" repeats Chapter 8 almost item for item. Its new content is the Kalai scoring fix.
- **Figure numbering.** Figure 11.7 is cited (line 48) and placed (line 58) before Figures 11.4 to 11.6. Renumber it 11.4 and shift the others, or move the citation.

## Figures

- **Figure 11.2 (simulation)**: the code matches the caption and text exactly. Twenty seeds give the following recall of task 1 after each of the five tasks:

  | Condition | After task 1 | 2 | 3 | 4 | 5 |
  |---|---|---|---|---|---|
  | Gating and protection | 100 | 100 | 97.5 | 91.2 | 83.3 |
  | Gating alone | 100 | 77 | 54 | 35 | 25.8 |
  | No protection | 100 | 0 | 0 | 0 | 0 |
  | Protection alone | 100 | 0 | 0 | 0 | 0 |

  "Keep 83 percent" and "the curves ... coincide" are both right. The gate masks are drawn per unit with probability 0.2, so "a fixed random 20 percent" is right on average, which is fine.
- **Figure 11.3 (simulation)**: it is correctly computed (see Moderate). The legend in the lower left sits on the classical curve's tail. Move it to the centre right.
- **Figure 11.4**: Horowitz's values are correctly transcribed, and DRAM at 2,000 pJ is the middle of the 1.3 to 2.6 nJ range, as the caption says.
- **Figure 11.5**: correct. The surrogate (a fast-sigmoid derivative) is a standard choice.
- **Figure 11.6**: correct in form, after Keramati and Gutkin. One caption fix in panel A: the reward is already negative at a pre-meal state of about −1, because the meal of 2 units would carry the state past the set point. Use "becomes negative once the meal would carry the state past the set point". In panel B the homeostatic agent oscillates between about −2 and 0, so "stays near the set point" is right.
- **Figure 11.1**: see Major.
- **Figure 11.7**: defensible as the author's judgment. "Retraining from scratch" in the replay row should change if line 40 changes, for example to "retraining on mixed old and new data; replay in research systems".

## Cross-references checked

These callbacks are accurate:
- Chapter 3: neuromodulators; acetylcholine for encoding against recall; norepinephrine for unexpected uncertainty; Doya; three-factor rule and eligibility traces; the learned neuromodulatory gating that Chapter 3 mentions (line 130); novelty releasing neuromodulators.
- Chapter 5: hippocampal index (Teyler and DiScenna, line 114); slow-wave replay; consolidation and the standard account.
- Chapter 7: Keramati and Gutkin; reward hacking; anchoring limiting drift.
- Chapter 8: confidence (Kepecs, Lak), waiting and conflict.
- Chapter 9: EWC linked to spine stabilization (Kirkpatrick et al. cite Yang et al. 2009); the pianist.
- Chapter 10: the forgetting simulation; Kalai; mixtures of experts; trained networks resembling cortex.

These are inaccurate:
- Replay as a borrowing, which contradicts Chapter 5, line 168, and Chapter 10, line 88.
- The order of Chapter 10's list.
- "Working memory" for the context window (Chapter 10).
- Hopfield's network "described" in Chapter 5.
- "Prospective configuration" (Chapter 10).

## What I verified

- **Against primary sources or abstracts**:
  - Masse et al. 2018: 70.8, 82.3, 61.4 and 95.4 percent (via the authors' patent text, which reproduces the paper's results).
  - Human Brain Project funding and end date.
  - Dapello et al. 2020: 18 percent, and 3 percent over the state of the art.
  - Orhan and Lake 2024: 200 h, 70 percent.
  - Titans: NeurIPS 2025.
  - DeepSeek-V3.1-Base model card: 630B + 209B tokens.
  - Llama 3 annealing.
- **From the literature, consistent with the text**:
  - The Wright letters and the 1901 address; the Feynman blackboard.
  - Markram 2009 and 2015; the 2014 open letter.
  - van de Ven 2020; Tadros 2022; Benna and Fusi; Laborieux; Cichon and Gan.
  - Luo et al.; Biderman et al.; Gekhman et al.; Ambrose et al.; Mattar and Daw; Schaul et al.
  - RAG; RETRO; Amit et al.; Krotov and Hopfield; Ramsauer et al.; Ba et al.; Schlag et al.; Whittington et al.
  - Behrens 2007; Miconi 2018 and 2019; Horowitz; Levy and Calvert; NorthPole; Ambrogio et al.; Hala Point.
  - Neftci et al.; Bellec et al.; Scellier and Bengio; forward-forward; Li et al. (about 3 percent); CoastRunners; Krakovna et al.; Gao et al.; Keramati and Gutkin; Man and Damasio.
  - Pathak; Burda (the noisy TV); Gottlieb and Oudeyer; Kidd and Hayden; Schmidhuber 1991; Kepecs 2008; Botvinick 2001.
  - Graves; PonderNet; Kalai's confidence-threshold proposal; Vogelsang et al.; Elman; Rohde and Plaut; Bengio 2009; Sheybani et al.; Zador et al. 2023; Li et al. 2019; Fong et al.; Safarani et al.
- **Simulations**: I re-ran both simulations. Their numbers are given above.

## What would make it a 5

1. Fix the Major item: distinguish borrowings from convergences in lines 24, 30 and 136 and in Figure 11.1, consistent with Chapters 5 and 10.
2. Put convolution through the chapter's own bitter-lesson test (vision transformers).
3. Update lines 40 and 114 on continued pretraining and data-mixture schedules.
4. Temper the Titans claim, add the fairness sentence to the Hopfield comparison, mention adaptive optimizers at line 62, and cite the KL penalty at line 98.
5. Correct the five callbacks listed above, and renumber Figure 11.7.
