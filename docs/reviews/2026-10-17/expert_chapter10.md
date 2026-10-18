# Expert review: Chapter 10, What Artificial Intelligence Gets Right and Wrong: Machine Learning Measured Against the Brain

File: `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md`

Reviewer role: computational neuroscience and machine learning (deep learning, RL, LLMs, NeuroAI). I reviewed the source, `make_figures.py` (and re-ran the Figure 10.5 simulation: 20 seeds, same code), all seven figures, and the "Implications for Artificial Intelligence" sections of Chapters 1 to 9 and the front matter for the callbacks.

## Overall assessment

Technical accuracy score: **4 / 5**

This is a well-judged synthesis. The structure is right: representations, error and prediction, shortcuts, data, continual learning, credit assignment, energy, embodiment, fluency versus thought, metacognition, and the Bitter Lesson as the case against. The chapter uses the strongest primary studies in each area and mostly characterizes them accurately. I checked the numbers that carry the argument against the sources, and they are right:
- Krizhevsky: 26 to 15 percent error.
- Chinchilla: 70B parameters on 1.4T tokens.
- Frank: 10^6 words a month, 6 × 10^7 by age 5, 2 × 10^8 by age 20.
- Vong: 61 h of recording, 22 words, 61.6 against 66.7 percent.
- Zech: three hospital systems; tokens identify the site.
- Recht: 11 to 14 points.
- Patterson: 1,287 MWh.
- TrueNorth: 63 mW.
- McCoy: 51 against 13 percent.
- Berglund: 79 against 33 percent.
- Valmeekam: about 34 percent of plans, and 0.2 to 4 percent once disguised.
- Dohare, DreamerV3 and DeepSeek-R1: correctly described.

The chapter hedges its own resemblance claims, through Schaeffer, Bowers and Caucheteux, which a specialist will appreciate.

The problems:
- **Two callbacks are wrong.** The front matter does not describe Marr's levels, and Chapter 6 did not say adversarial images fool no person.
- **One developmental claim is wrong.** Newborns do not show object permanence.
- **The text misdescribes the book's own simulation.** List A takes about 20 passes to be forgotten, not "a few".
- **Several claims are stated more firmly than the evidence allows.** These are the TD-as-engineering history, "trained only to perform a task ... organized like the brain" without the post-2020 plateau, the Recht result, next-token prediction as "the objective Chapter 6 attributed to cortex", "before 2014 ... filters chosen by hand", and human metacognition as the contrast case.
- **The LLM-reasoning section is dated for late 2026.** All three failure studies are of GPT-4 in 2023.

None of this undermines the argument.

## Major (factually wrong, must fix)

- **Line 16: the front matter does not describe Marr's levels, and performance/representation/mechanism is not Marr's scheme.** "The front matter of this book described these as levels of explanation, after David Marr..."
  - **What is wrong**: The front matter's "A Note on Levels of Explanation" (Front Matter, lines 85 to 101) describes levels of *scale*: physical/molecular, cellular, circuit/systems, and cognitive/behavioral. It does not mention Marr. Marr's three levels are computational (what is computed and why), algorithmic/representational, and implementational. "Performance" is not the computational level. A learning procedure such as backpropagation sits at the algorithmic level, not under "mechanism" as implementation.
  - **Fix**: "Measuring needs a scale, and there are three. A system can match the brain in performance, doing what a person does as well as a person does it. It can match in representation, organizing information inside it as the brain does. Or it can match in mechanism, getting there by the same means. The distinction echoes, loosely, the levels of analysis that David Marr proposed for vision (what is computed, by what algorithm and representation, and in what hardware), and it matters here because current machine learning scores very differently on the three.[^2]"

- **Line 68: newborns do not "expect objects to persist when hidden".** "...a newborn human prefers faces and expects objects to persist when hidden."
  - **What is wrong**: Newborn face preference is well established. Expectations of object persistence have been shown by violation-of-expectation methods at 3.5 to 5 months, not at birth, and even those results are debated (Bogartz et al., 2000).
  - **Fix**: "A colt walks within hours of birth; a newborn human prefers to look at faces, and by three or four months infants look longer when a hidden object seems to have vanished, as if they expected it to persist."
  - **Cite**: Baillargeon, R., Spelke, E. S., & Wasserman, S. (1985). Object permanence in five-month-old infants. *Cognition*, 20(3), 191–208. https://doi.org/10.1016/0010-0277(85)90008-3 (the paper and pages are verified; the DOI is from memory and not verified). Spelke and Kinzler (2007), already cited, covers the general point.

- **Line 80: the text misdescribes Figure 10.5's simulation.** "...the network forgets the first list almost completely within a few passes."
  - **What is wrong**: I re-ran `interference()` for seeds 0 to 19:
    - Perfect recall of list A is 100 percent at pass 100.
    - It is 54 percent after 3 passes on list B, 25 percent after 10, and 17.5 percent after 12.
    - It falls below 5 percent only after about 21 passes and below 1 percent after about 35.

    The striking feature in the code's output is that list A is lost much faster than list B is learned. B is still below 20 percent at pass 12, when A has fallen to 17.5 percent.
  - **Fix**: "...the network loses half of the first list within a few passes and nearly all of it within about twenty, well before it has finished learning the second."

## Moderate (overstated, contested, or misleading)

- **Line 14: the Chapter 6 callback contradicts Chapter 6.** "Chapter 6, why it is fooled by images no person would mistake."
  - **What is wrong**: Chapter 6 (its AI section) explicitly says that "humans given only a brief glimpse of such images can be fooled by them too" (Elsayed et al., 2018) and rejects the simple framing.
  - **Fix**: "Chapter 6, why an imperceptible change to an image can make it confidently wrong."

- **Line 28: TD learning was not devised purely as engineering.** "...temporal-difference learning, devised as an engineering method for learning predictions, turned out to describe the firing of dopamine neurons..."
  - **What is wrong**: Sutton and Barto developed the TD family from 1981 onward explicitly as a model of animal classical conditioning, extending Rescorla-Wagner to real time. The 1988 paper generalized it as a prediction method. Chapter 3's footnote 16 itself calls Rescorla-Wagner "the trial-level ancestor" of TD. The round trip is therefore psychology to engineering to neurophysiology, which strengthens the chapter's theme. Figure 10.1 inherits the problem: TD appears as a pure ML origin.
  - **Fix**: "Chapter 3 told how Richard Sutton's temporal-difference learning, which he and Andrew Barto had developed from models of animal conditioning and then generalized into an engineering method for learning predictions, turned out to describe the firing of dopamine neurons..."
  - **Cite**: Sutton, R. S., & Barto, A. G. (1981). Toward a modern theory of adaptive networks: Expectation and prediction. *Psychological Review*, 88(2), 135–170. https://doi.org/10.1037/0033-295X.88.2.135 (journal, volume, pages and PMID 7291377 verified; DOI not verified).

- **Line 28: "then biology confirmed" is too strong for Dabney et al. (2020).** "An idea had gone from biology to engineering and come back with a prediction that biology then confirmed."
  - **What is wrong**: The 2020 result was a reanalysis of existing recordings, consistent with the prediction, and alternative accounts of the diversity of reversal points have been debated. The strongest later support is Sousa et al. (2025).
  - **Fix**: "...come back with a prediction that the recordings supported, and that later experiments have extended."
  - **Cite**: Sousa, M., Bujalski, P., Cruz, B. F., Louie, K., McNamee, D. C., & Paton, J. J. (2025). A multidimensional distributional map of future reward in dopamine neurons. *Nature*, 642(8068). https://doi.org/10.1038/s41586-025-09089-6 (title, journal, volume, issue and DOI verified; author list and pages not verified).

- **Lines 22 and 26: the backpropagation history is simplified to the point of error.** "Multilayer networks could compute it, but no one knew how to train them" (line 22). "The method of training such a network came from engineering. ... Rumelhart, Hinton, and Williams showed in 1986..." (line 26).
  - **What is wrong**: Gradient training of multilayer networks predates 1986. Amari trained multilayer perceptrons by stochastic gradient descent in 1967, Linnainmaa published reverse-mode differentiation in 1970, and Werbos proposed applying it to neural networks in 1974. Rumelhart was a cognitive psychologist, and the 1986 contribution was showing that the method discovers useful hidden representations.
  - **Fix**, line 22: "...but there was no practical, widely known way to train them." Line 26: "The method of training such a network came from mathematics and control engineering, where the reverse-mode calculation of gradients had been worked out in the 1970s; David Rumelhart, Geoffrey Hinton, and Ronald Williams showed in 1986 that this backpropagation ... could train networks with hidden layers to discover useful internal representations."

- **Lines 32 to 36 and Figure 10.2: the performance-predictivity relation has since broken down, and the chapter does not say so.** "The networks that were better at recognizing objects were better at predicting the responses..."
  - **What is wrong**: The finding is accurate for 2014. However, as ImageNet accuracy rose past about 70 percent, IT predictivity plateaued and then declined, and this is now a central NeuroAI result. Without it, line 32 ("trained only to perform a task, end up organized like the brain") and Figure 10.2's ever-rising line overstate the case. In addition, Yamins et al. predicted multi-unit IT recording sites, not "individual IT neurons".
  - **Fix**: Replace "individual IT neurons" with "sites in IT". After the Khaligh-Razavi sentence add: "The relation did not hold indefinitely. As networks grew more accurate than those of 2014, their ability to predict IT stopped improving and then began to fall, because the most accurate networks came to rely on features that IT does not use."
  - **Cite**: Linsley, D., Rodriguez, I. F., Fel, T., Arcaro, M., Sharma, S., Livingstone, M., & Serre, T. (2023). Performance-optimized deep neural networks are evolving into worse models of inferotemporal visual cortex. In *Advances in Neural Information Processing Systems 36* (pp. 28873–28891). arXiv:2306.03779 (verified).

- **Line 48: next-token prediction is not the objective Chapter 6 attributed to cortex.** "A language model's training objective is the one Chapter 6 attributed to cortex, reduced to text."
  - **What is wrong**: Chapter 6's predictive coding is hierarchical. Each level predicts the activity of the level below, and error units correct it during inference. An autoregressive LM predicts only its next input, at the output, and is trained by backpropagation with no inference-time error correction; Chapter 6's own AI section says standard networks have "no error signal at inference time". The sentence also ignores post-training. As of 2026, frontier models spend a substantial and growing share of compute on reinforcement learning from human preferences and verifiable rewards, which is labeled or reward-driven.
  - **Fix**: "A language model's training objective shares the aim that Chapter 6 attributed to cortex, predicting what comes next, though not its hierarchical form, and it is reduced to text. (The final stages of training add a different signal: rewards from human preferences or from checking answers.)"

- **Line 58: the Recht result is weaker evidence of brittleness than presented.** "...found that the accuracy of every model they tested dropped, by roughly 11 to 14 percentage points, although the new images looked to people like the old ones."
  - **What is wrong**: Recht et al. did not test whether people saw the images as alike. Engstrom et al. (2020) showed that most of the drop came from bias in how the replication matched the annotators' selection frequencies: only about 3.6 of the 11.7 points remains unexplained. Model rankings were also preserved.
  - **Fix**: "...found that the accuracy of every model they tested dropped by roughly 11 to 14 percentage points. Later analysis traced much of the drop to subtle differences in how the new images had been selected, which is itself the point: changes too slight for the builders of the test set to notice were enough to move every model."
  - **Cite**: Engstrom, L., Ilyas, A., Santurkar, S., Tsipras, D., Steinhardt, J., & Madry, A. (2020). Identifying statistical bias in dataset replication. In *Proceedings of the 37th International Conference on Machine Learning* (PMLR 119, pp. 2922–2932) (finding and venue verified; author list and pages from memory).

- **Line 90: the Chapter 3 and Chapter 6 callback does not match what follows.** "Chapter 3 and Chapter 6 described two lines of attack..."
  - **What is wrong**: Chapter 3 described feedback alignment. Chapter 6's line was predictive-coding networks approximating backpropagation (Chapter 6, AI section, fifth point). Line 90 then describes feedback alignment, NGRADs and dendritic schemes, and never mentions predictive coding, so the reader cannot find Chapter 6's line.
  - **Fix**: Insert after the Lillicrap sentence: "Chapter 6's line was predictive coding. James Whittington and Rafal Bogacz showed that a predictive-coding network with purely local Hebbian plasticity can, under some conditions, compute the same weight changes as backpropagation."
  - **Also**: For the last sentence, add evidence of the scaling gap.
  - **Cite**: Whittington, J. C. R., & Bogacz, R. (2017). An approximation of the error backpropagation algorithm in a predictive coding network with local Hebbian synaptic plasticity. *Neural Computation*, 29(5), 1229–1262. https://doi.org/10.1162/NECO_a_00949 (verified). Bartunov, S., Santoro, A., Richards, B. A., Marris, L., Hinton, G. E., & Lillicrap, T. P. (2018). Assessing the scalability of biologically-motivated deep learning algorithms and architectures. In *Advances in Neural Information Processing Systems 31*. arXiv:1807.04587 (verified).

- **Line 92: a specialist would expect the strongest "something different" proposal.** "Whether that combination amounts to an approximation of the gradient or to something different and perhaps better suited to learning all the time..."
  - **Fix**: Add: "Yuhang Song, Bogacz, and their colleagues have argued for the second: in their models, the brain first settles its activity on what the outcome should have been and only then changes its synapses, which in their simulations learns faster than backpropagation and with less interference."
  - **Cite**: Song, Y., Millidge, B., Salvatori, T., Lukasiewicz, T., Xu, Z., & Bogacz, R. (2024). Inferring neural activity before plasticity as a foundation for learning beyond backpropagation. *Nature Neuroscience*, 27(2), 348–358. https://doi.org/10.1038/s41593-023-01514-1 (authors, title, journal and DOI verified; volume and pages from memory).

- **Line 96: the inference claim is uncited, and the 700 W figure is dated.** "...a widely used model spends more energy answering queries over its life than it did learning, and a single current data-center processor can draw 700 watts, as much as 35 brains.[^43]"
  - **What is wrong**: Footnote 43 is the H100 spec sheet only. The inference claim needs a source. The H100 (2022) is no longer "current" in late 2026: Blackwell-generation accelerators are rated at about 1,000 W and above.
  - **Fix**: "...At Google, about three-fifths of the energy used for machine learning went to answering queries rather than training. A single data-center processor of the mid-2020s draws 700 to 1,000 watts or more, as much as 35 to 50 brains."
  - **Cite**: Patterson, D., Gonzalez, J., Hölzle, U., Le, Q., Liang, C., Munguia, L.-M., Rothchild, D., So, D. R., Texier, M., & Dean, J. (2022). The carbon footprint of machine learning training will plateau, then shrink. *Computer*, 55(7), 18–28. https://doi.org/10.1109/MC.2022.3148714 (the "about ⅗ of ML energy use is for inference" sentence is verified in arXiv:2204.05149; the journal DOI and pages are from memory).
  - **Optional**: GPT-3 (2020) is now an old comparison. Meta's Llama 3.1 model card reports about 31 million H100 GPU-hours for the 405B model, which is roughly 20 GWh at rated power, or about 6,000 brain-twenties. Check that figure against the model card before use.

- **Lines 114 to 116: the reasoning evidence is dated for a late-2026 book.** McCoy, Berglund and Valmeekam all tested GPT-4 in 2023, and line 116 says only that "that picture is changing".
  - **What is wrong**: The same Valmeekam group later found that a reasoning model, o1-preview, solved 97.8 percent of Blocksworld problems and 52.8 percent of the disguised "Mystery" versions, against GPT-4's 34.6 and 0.2 percent. That is the concrete evidence line 116 needs, and it keeps the honest residue: the disguised problems remain much harder.
  - **Fix**: After the DeepSeek-R1 sentence add: "When Valmeekam's group retested its block-stacking problems on one such model in 2024, it solved nearly all of the plain problems and about half of the disguised ones, where GPT-4 had solved almost none."
  - **Cite**: Valmeekam, K., Stechly, K., & Kambhampati, S. (2024). LLMs still can't plan; can LRMs? A preliminary evaluation of OpenAI's o1 on PlanBench. *arXiv*, 2409.13373 (numbers verified from the paper's Tables 1 and 2; author list from memory).

- **Lines 120 to 122 and 148: the human side of the metacognition contrast is overstated, and the model side omits the clearest evidence.** "A person's confidence is calibrated by consequences..." (line 122). "...knows when to say it does not know because being wrong costs it something" (line 148).
  - **What is wrong**:
    - People are often miscalibrated: they are overconfident on general-knowledge questions, they confabulate reasons, and patients with anosognosia deny deficits. Chapter 8's opt-out animals are trained with explicit reward for opting out.
    - "Because being wrong costs it something" is a hypothesis about cause, not a finding.
    - On the model side, the evidence a specialist would cite is that pretrained LLMs are well calibrated and preference-based post-training degrades calibration. This supports Kalai's point that the training reward, not the architecture, removes "I don't know".
  - **Fix**, line 122: "A person's confidence is shaped, imperfectly, by consequences: people are often overconfident and sometimes invent reasons for what they did, but being wrong has costs that tend to pull confidence back toward accuracy. A model is rewarded for what its designers chose to reward. When OpenAI measured GPT-4, the model as first trained on text was well calibrated, and the later training that made it a helpful assistant made it markedly less so." Line 148: "...and is pushed toward knowing when it does not know by the cost of being wrong."
  - **Cite**: OpenAI. (2023). GPT-4 technical report. *arXiv*, 2303.08774 (the calibration figure, about 0.007 to 0.074 expected calibration error before and after post-training, is confirmed by secondary sources; check against the report's Figure 8).

- **Line 138: "before 2014" overstates.** "Before 2014 a model of visual cortex was a set of filters chosen by hand..."
  - **What is wrong**: Chapter 6 itself describes Olshausen and Field (1996) learning V1 receptive fields from natural images. HMAX-style models also learned some stages.
  - **Fix**: "Before 2014 most models of higher visual cortex were built largely by hand, with learning confined to a stage or two; now..."

- **Line 148: "evolution has already done most of the work" contradicts the chapter's own lines 68 to 70.** Lines 68 to 70 give two parts to the explanation, innate structure *and* rich, embodied, chosen experience.
  - **Fix**: "A brain learns from little data because evolution has built in much of the structure and because its experience is rich, embodied, and chosen..."

## Minor

- **Line 12**: The 1958 demonstration ran on an IBM 704, so "a room-sized computer" is right. The hardware Mark I Perceptron came in 1960, so do not let an editor merge the two.
- **Line 34**: "the best of them predicted about half" is right (about 48 percent of explainable variance for multi-unit sites).
- **Line 40**: The Schaeffer et al. count is "more than 11,000 networks" (verified in the paper), so "thousands" is fine. The authors also found that the grid-like units, where they appeared, lacked key properties of real grid cells, such as multiple modules. Consider adding "and the grids that did appear lacked key properties of real ones". Their conclusion has been disputed by groups who see the needed conditions as principled. A clause, "a conclusion others have disputed", would be fair.
- **Line 64**: "GPT-3, the language model that in 2020 first wrote convincing prose" ignores GPT-2 (2019). Use "...that in 2020 made convincing prose routine". Llama 3's 15 trillion is fine for 2024. For late 2026, note that open models trained in 2025 used over 30 trillion tokens (the Qwen3 technical report states 36 trillion, arXiv:2505.09388, not verified here).
- **Line 70: Vong et al.** The model was trained on video frames paired with *transcribed* utterances, not raw audio. Say "61 hours of video and transcribed speech". "Learned nothing of grammar" should be "was not tested on grammar". It was a contrastive word-image model that could not have learned syntax, but the paper does not test it.
- **Line 70 or 142: the BabyLM omission.** A specialist would expect the BabyLM Challenge, which trains language models on a child-sized budget of 10 to 100 million words, in the data-gap or innateness discussion. One sentence at line 142 would do: "Language models trained on 100 million words, about what a child hears by 12, learn much of English grammar but still fall short of models trained on trillions."
  - **Cite**: Warstadt, A., Mueller, A., Choshen, L., Wilcox, E., Zhuang, C., Ciro, J., Mosquera, R., Paranjape, B., Williams, A., Linzen, T., & Cotterell, R. (2023). Findings of the BabyLM Challenge: Sample-efficient pretraining on developmentally plausible corpora. In *Proceedings of the BabyLM Challenge at the 27th Conference on Computational Natural Language Learning* (pp. 1–34). https://doi.org/10.18653/v1/2023.conll-babylm.1 (verified). Note that the winning small-data systems beat some models trained on far more data on the challenge's benchmarks; check the wording before relying on that point.
- **Line 76: retrieval and persistent memory.** "A language model knows nothing of events after its training data were collected unless it is told about them or retrained." In 2026 most deployed assistants routinely search the web and keep persistent memories outside the weights. Add: "...unless it is told about them, looks them up, or is retrained; the memories some assistants now keep between conversations are stored as text and fed back in, not learned into the weights."
- **Line 80**: Cite McClelland, McNaughton and O'Reilly (1995) for CLS alongside Kumaran et al. (2016). Chapter 5 already does.
- **Line 84: adult human neurogenesis is contested.** Say "...in many mammals, though whether it continues in adult humans is disputed."
- **Line 88**: The weight-transport problem was named by Grossberg (1987). Crick's 1989 essay is a fine citation for a popular book.
- **Line 116: Chapter 5 does not describe route simulation.** "...the way Chapter 5's hippocampus appears to simulate routes before an animal takes them." Chapter 5 describes replay after experience (sleep and waking, forward and reverse), not sequences that depict future paths. Either say "the way the hippocampal sequences of Chapter 5 appear, in some experiments, to sketch routes before an animal takes them" and cite: Pfeiffer, B. E., & Foster, D. J. (2013). Hippocampal place-cell sequences depict future paths to remembered goals. *Nature*, 497(7447), 74–79. https://doi.org/10.1038/nature12112 (verified). Or drop the callback.
- **Line 128 and Figure 10.7 disagree.** The text says the listed problems are those "on which Figure 10.7 marks current machine learning as weakest". The figure marks "learning from little data" and "knowing when it does not know" as *partly shared* (gold). Say "weak or weakest".
- **Line 140: Ponce et al.** "...the images evolved toward shapes resembling faces and body parts that no one had predicted" is ambiguous, since faces were expected for face-selective sites. Use "...toward images that often contained parts of faces or bodies, or objects familiar to the monkeys, combined in ways no one had predicted."
- **Line 142**: "A system with no built-in grammar" should add "though with architectural biases of its own and thousands of times more text".
- **Footnote 46**: AlphaGo Lee is described in Silver et al. (2017). For the program itself, Silver et al. (2016), *Nature*, 529(7587), 484–489, is the standard citation. Chapter 8 presumably already cites it.
- **Reference list**: Krizhevsky et al. (2012) lacks pages (1097–1105).

## Figures

- **Figure 10.5 (simulation): the code matches the caption, but the text does not match the output.**
  - The code does what the caption says:
    - Two lists of 12 items share 28 random cue bits.
    - List membership is coded by 6 + 6 context units.
    - The network is a 40-60-10 sigmoid network trained by online backpropagation, 100 passes per list.
    - The replay condition adds 6 list-A items, *drawn afresh at random each pass*.
    - The results are averages over 20 seeds.
  - See Major item 3 for the text at line 80.
  - Caption: say "replaying six list-A items, chosen at random on each pass, alongside list B". Also say that "recalled" means all ten output bits correct, which explains the steep curves.
  - In panel A the legend sits on the rising list-A curve (passes 0 to 30, around 50 percent). Move it into the empty lower-left region of panel A after pass 30, or into panel B's empty band around 40 percent.
  - In panel B, list A dips to about 83 percent before recovering. The caption's "protects list A" is fair.
  - In `make_figures.py` the docstrings misnumber the figures: `fig_interference` says 10.4, `fig_energy` 10.5 and `fig_lifecycles` 10.6, where the chapter has 10.5, 10.6 and 10.4. This is harmless, but fix it for maintainers.
- **Figure 10.1**:
  - The TD point needs the psychology origin (see Moderate, line 28). Add a neuroscience/psychology point, "Rescorla and Wagner (1972): learning from prediction error", with a gold arrow to Sutton 1988, or label Sutton "TD learning (from models of conditioning)".
  - The Hebb point has no arrow. Either link it to Rosenblatt or drop it.
  - The 2012→2014 arrow is barely visible.
- **Figure 10.2**: As drawn, the monotonic line invites the reader to extrapolate. Add to the caption: "Later, more accurate networks did not continue the trend (see text)". Better still, add a few grey "recent high-accuracy models" points at x ≈ 0.8 with falling y, labeled illustrative, after Linsley et al. (2023).
- **Figure 10.3**: The numbers are correct and the axis label honestly flags words against tokens. Optionally add a 2025 bar at about 3.6 × 10^13.
- **Figure 10.4**: Panel A could add a thin dashed arrow from "use" labeled "retrieval / tools (no weight change)" so the figure is not dated by 2026 assistants. Panel B is a fair schematic of CLS plus neuromodulatory gating.
- **Figure 10.6**: The arithmetic is correct (3.5 MWh; 1,287 MWh). See the optional modern data point above.
- **Figure 10.7**: The judgments are defensible and the caption labels them as the author's. One suggestion: "prediction as a training signal: largely shared" is fair. But "error-driven learning: largely shared" sits uneasily beside "learning rule available at each synapse: largely absent". Consider "error-driven learning (the principle)" to separate the principle from its implementation.

## Cross-references checked

These callbacks are accurate:
- Chapter 1: 20 W; constraints that silicon does not share.
- Chapter 2: McCulloch-Pitts; XOR in a human cortical neuron via Gidon et al.; all-or-none spikes.
- Chapter 3: deciding when to learn; random feedback weights; dopamine RPE; meta-RL in prefrontal cortex.
- Chapter 5: McCloskey and Cohen; CLS; experience replay as a convergence; STDP and the third factor.
- Chapter 6: Hubel and Wiesel to the neocognitron; texture bias; predictive coding; forward models.
- Chapter 7: value anchored to the body; the anchoring limits drift.
- Chapter 8: AlphaGo; opt-out confidence; accumulation to a bound.
- Chapter 9: power law of practice; varied practice; EWC; spines; the robot hand.

These are inaccurate:
- The front matter and Marr (line 16).
- Chapter 6 on adversarial images (line 14).
- Chapter 3 and Chapter 6 as two lines of attack on backpropagation (line 90).
- Chapter 5 on route simulation (line 116).
- The TD framing (line 28): it is consistent with Chapter 3's text but historically incomplete.

## What I verified

- **Against primary sources or abstracts**:
  - Frank 2023: the monthly, age-5 and age-20 figures.
  - Zech et al. 2018: NIH, MSH and IU; prevalence 34.2 against 1.2 percent; hospital identified with more than 99.9 percent accuracy; metal laterality tokens.
  - McCoy et al. 2024: 51 against 13 percent.
  - Valmeekam et al. 2023 and 2024: Blocksworld and Mystery figures; o1-preview at 97.8 and 52.8 percent.
  - Schaeffer et al. 2022: more than 11,000 networks.
  - Engstrom et al. 2020: 3.6 of 11.7 points unexplained.
  - Linsley et al. 2023.
  - Patterson et al. 2022: about ⅗ of ML energy goes to inference.
  - Song et al. 2024, Whittington and Bogacz 2017, Bartunov et al. 2018, Pfeiffer and Foster 2013, Baillargeon et al. 1985, BabyLM 2023, DeepSeek-R1 in *Nature* 645, Sousa et al. 2025.
- **From the literature, consistent with the text**:
  - Rosenblatt and the 1958 NYT report.
  - Krizhevsky (15.3 against 26.2 percent).
  - Kaplan; Chinchilla.
  - Yamins (about 48 percent explainable variance); Khaligh-Razavi; Schrimpf; Goldstein; Caucheteux and King.
  - Banino; Bowers; Geirhos 2020 and 2021.
  - Vong (61.6 against 66.7 percent, 22 words, 61 h, about 1 percent of waking hours).
  - Lake 2015; Wang 2018; Mnih 2015 (49 games, hippocampal parallel noted); Lin 1992.
  - Dohare 2024; Crick 1989; Lillicrap 2016 and 2020; Sacramento; Payeur.
  - Patterson 2021 (1,287 MWh); TrueNorth (63 mW); Moravec (p. 15); Lee Sedol 4–1 and Aja Huang placing stones.
  - Mahowald; Fedorenko et al. 2024; Berglund (79 against 33 percent); Kalai et al. 2025; Kadavath 2022; Bashivan 2019; Ponce 2019; the Bitter Lesson (13 March 2019).
- **Simulation**: I re-ran `interference()` for seeds 0 to 19 in both conditions. The figure is correctly computed and the caption is accurate; the line 80 text is not.
- **Arithmetic**: 20 W × 20 yr = 3.51 MWh; 1,287 / 3.5 ≈ 367 brains; 3 × 10^11 / 6 × 10^7 = 5,000; 1.5 × 10^13 / 6 × 10^7 = 250,000. All consistent with the text.

## What would make it a 5

1. Fix the three Major items: the Marr and front-matter callback, newborn object permanence, and the line 80 description of the simulation.
2. Correct the Chapter 6 (line 14), Chapter 3/6 (line 90) and Chapter 5 (line 116) callbacks.
3. Add the post-2020 breakdown of the performance-predictivity relation (text and Figure 10.2 caption).
4. Reframe TD's origin and soften "confirmed" for distributional dopamine.
5. Qualify the Recht result, the next-token "same objective" claim, and "before 2014 ... by hand".
6. Update the reasoning section with the 2024 o1 PlanBench result, the energy paragraph with a source for inference and a current accelerator figure, and line 76 with retrieval and memory.
7. Rebalance the metacognition contrast (human miscalibration; post-training degrades LLM calibration) and the Central Lesson's "evolution has done most of the work".
8. Add Whittington and Bogacz, and Song et al. (prospective configuration), to the credit-assignment section.
