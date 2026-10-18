# Literary Review: Chapter 11, "Integrating Brain Mechanisms into AI Models: What Machines Could Borrow from Biology"

Source: `docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md` (body lines 10 to 140, about 6,370 words of prose by my count, excluding headings, captions, and notes; the coordinator counts about 6,450). It has 7 figures and about 73 footnotes.

## Overall assessment

What works:

- **The opening.** The Wrights and the buzzards is the best opening since Rosenblatt's perceptron. Wilbur twisting an inner-tube box in the bicycle shop (line 10) is a scene the reader can see. His own sentence, that watching a bird flap is "a very small part of its mental labor" (line 12), states the chapter's argument before the chapter makes it. "The bird showed that a thing could be done and suggested one principle for doing it. The engineering was their own" is the thesis in two sentences, and Hassabis's "validating ... and suggesting an algorithm" (line 24) then confirms it in the field's own words.
- **The frame closes.** "The Wrights did not build a bird" (line 136) returns to the opening. Feynman's blackboard is paid off in "What Building Teaches Biology", whose last sentence is the chapter's best: "building has become a way of asking the brain questions."
- **Many passages have real narrative force:**
  - Markram's ten-year promise and the open letter (line 22).
  - "The industry's answer to the problem of forgetting has been to avoid it" (line 40).
  - "Engineers looking for a better memory and neuroscientists looking for a model of the hippocampus arrived at nearly the same mathematics" (line 54).
  - Horowitz's energy table and Levy and Calvert's finding that even the brain pays most of its energy to move information (lines 72 to 76).
  - The CoastRunners boat circling its lagoon on fire, paid off at line 94: "the hundredth target would have been worth nothing."
  - Burda's noisy television and "Children do not stare at static for long" (line 100).
  - The cataract children (line 112).
- **The house style holds.** There are no em dashes and no British spellings, and numbers follow the house rule. The figures are clean, and each is cited.

What does not work:

1. **The chapter's central examples of successful borrowing contradict Chapters 5 and 10.** Line 24 says "Hippocampal replay became experience replay". Figure 11.1 and the Central Lesson (line 136) list replay and temporal-difference learning as principles taken from the brain. But Chapter 5 says experience replay was invented in 1992, before hippocampal replay was recorded: "a convergence, not a borrowing". Chapter 10 says machine learning found it "independently" and traces temporal-difference learning to the psychology of conditioning. The thesis rests on these examples, so the claim must be made accurately.
2. **"Knowing When to Stop and Think" (lines 102 to 108) is a recap.** It repeats Kepecs and Graves (Chapter 8's AI section), uncertainty from disagreement and dropout (Chapter 8), and Kalai (twice in Chapter 10), and it has no story. Only Kalai's scoring fix and the closing proposal are new. The section offers a "small, fast monitor", yet there is no experiment showing such a monitor in a person.
3. **"Borrowing the Data" (lines 118 to 124) is a catalogue.** It runs four studies through one 207-word paragraph, and the reader pictures none of them.
4. **The Central Lesson has three problems.**
   - It carries the replay and temporal-difference error from point 1.
   - It drops the third way of borrowing that Figure 11.1 introduced.
   - It ends on the Chapter 12 handover. Chapters 9 and 10 put the handover at the end of the closing applied section, so that the Central Lesson ends on a lesson.

Smaller issues:

- **Inaccurate statements.** Line 26 says the chapter follows Chapter 10's order, but it does not. Line 50 sends the reader to a Hopfield network that Chapter 5 mentions only in a note. Line 56 calls a 2025 memory module "the first serious attempt".
- **Figure numbering.** Figure 11.7 is cited and placed between Figures 11.3 and 11.4.
- **Paragraph length.** Nine paragraphs run past 175 words.

Prose quality: 4/5. Reader interest: 4/5.

**To reach 5/5 on prose:**

- Correct the replay and temporal-difference claim in its three places.
- Fix the false or loose callbacks (lines 26, 50, 116, 130).
- Untangle the run-on sentences (lines 36, 40).
- Renumber Figure 11.7.
- Split the paragraphs flagged below.

**To reach 5/5 on reader interest:**

- Give "Knowing When to Stop and Think" a story of its own. I propose Logan and Crump's typists, whose fingers slowed after an error the screen had secretly corrected; it is a human "small, fast monitor", and it extends Chapter 9's pianist.
- Rebuild "Borrowing the Data" around one experiment (Dapello's V1 front end).
- Make Behrens's volatility experiment concrete.
- Rewrite the Central Lesson as below.

The changes add about 150 words net and keep the body well under the 7,000 ceiling.

**On "What Building Teaches Biology" as the closing section:** it works, and it is the right replacement for the usual AI section. Feynman's sentence earns its place there. It does not repeat Chapter 10's "Implications for Neuroscience", which was about networks as models and as tools of control; this section is about building as a test of theory. The section should carry the Chapter 12 handover.

**On the Next Chapter line:** it works. The handover's "whether a single principle lies beneath them" sets it up exactly. Keep the hedge in the final subtitle. "One Principle Beneath the Mechanisms" promises an answer that the free-energy and predictive-processing literature, which is contested, may not deliver. A question form ("Is There One Principle Beneath the Mechanisms?") or "A Principle Beneath the Mechanisms" would match the handover.

## Findings

### Major

- **Lines 24, 136, and Figure 11.1 (replay and temporal-difference learning presented as borrowings).** These contradict Chapter 5 ("a convergence, not a borrowing") and Chapter 10 ("found the same answer independently"; temporal-difference learning came "from the Rescorla-Wagner model of animal conditioning").
  - **Rewrite line 24's replay sentence:** "Replay is the instructive exception: machine learning invented experience replay before hippocampal replay was recorded, as Chapter 5 noted, and the two were recognized as the same principle, relearning old experience interleaved with new, only afterward. Since then each field has used the other's version to sharpen its own."
  - **In Figure 11.1,** remove "experience replay" from the "borrow the principle" box, or mark it "(found independently)". Change the caption's "as convolution, replay, and gating did" to "as convolution and gating did".
  - **In the Central Lesson,** see the rewrite in the last Major finding.

- **Lines 102 to 108 ("Knowing When to Stop and Think" recaps Chapters 8 and 10 and has no story).** Chapter 8 described Kepecs's rats, Graves's adaptive computation time, and uncertainty from switching off units. Chapter 10 cited Kalai twice.
  - **Compress line 104's two experiments** to one acknowledging sentence: "Chapter 8 found confidence computed alongside every decision, in rats as in people, and Chapter 9 a signal of conflict or error that hands control from habit to deliberation."
  - **Compress line 106's first two sentences** to: "Machine learning has had versions of each part for years, from networks that learn how long to compute to ensembles whose disagreement measures their uncertainty, as Chapter 8 described.[^60][^61]"
  - **Add before line 108** (about 110 words; expert to verify against Logan and Crump, *Science* 2010): "The brain's monitor is faster than thought, and it can be caught working on its own. Gordon Logan and Matthew Crump had skilled typists copy words while the program secretly altered what appeared on the screen. When it silently corrected a typist's mistake, the typist's fingers still slowed on the next keystroke, as they do after any error, though the typist then took credit for the correct word on the screen. When it inserted an error the typist had not made, the fingers did not slow, though the typist accepted the blame. The hands had an error signal of their own, faster than the eye and independent of what the typist believed."
  - Then line 108 can begin "The brain's monitor is cheap, fast, and always on ...". The pianist sentence stays, and it now has company.

- **Lines 120 to 124 ("Borrowing the Data" is a catalogue).** Line 122 runs four studies through 207 words.
  - **Lead with Dapello and tell it as an experiment** (about 90 words): what the front end was (filters measured in monkey V1, plus their noise), what was attacked, and what changed. The expert should supply one concrete detail, for example that the gain came largely from the added neural noise.
  - **Compress Li, Fong, and Safarani** into one sentence: "Other groups have made networks resemble mouse visual cortex, weighted training images by how strongly they drove the human visual system, or trained networks to predict monkey V1 alongside recognizing objects, and each found modest gains in robustness or accuracy.[^70][^72][^73]"
  - Keep line 124, which is the section's best paragraph.

- **Line 136 (Central Lesson).** It repeats the replay and temporal-difference claim, omits borrowing the data, puts curiosity under "trusted" rather than under learning, and ends on the handover. **Rewrite:** "The Wrights did not build a bird. They took one principle from the buzzard, controlling roll by changing the lift on each wing, and built it with cloth, wire, and an engine. The borrowings from the brain that have worked share that pattern: convolution kept what the repeated detectors of visual cortex do and discarded the neurons, and replay, found independently on both sides, turned out to be one principle in two materials. The brain's remaining lessons are of the same kind. A learner that must keep learning while it is used needs a fast memory that learns from use, a way to choose what to replay and what to protect, signals that decide when learning is worth doing, and curiosity about what it can learn. A learner limited by energy needs to compute where its memory is, by rules that need no global traffic. A learner that must be trusted needs rewards that saturate and a cheap alarm that tells it when its fast answer is wrong. Where no one yet knows the principle, a recording of the brain may carry it anyway. Each of these has been built in some form; few have been built at scale, and none has yet passed the test that would make it a lesson rather than a suggestion."
  - **Move the last two sentences of the current line 136** ("Building them is also how neuroscience ..." and the Chapter 12 handover) to the end of line 132, where they follow "a way of asking the brain questions" naturally.

### Minor

- **Line 10 (no section heading).** Chapters 8 to 10 open under a heading ("The Problem Decision Solves", "What Practice Changes", "What Is Being Measured"). Add one, for example "# What the Wrights Took from the Buzzard".
- **Line 26 (false and one sentence long).** The chapter does not follow the order of Chapter 10's sorting paragraph, which runs lifelong learning, confidence, frugality, data, values, local rules. Use "The rest of this chapter takes the borrowable solutions in turn." Or cut the line, since line 14 already lists them.
- **Line 30.** Experience replay dates from 1992. Change "for 30 years" to "for more than 30 years".
- **Line 36 (203 words).** "networks protected by weight protection alone" doubles the noun; use "networks with weight protection alone". Split before "Figure 11.2 reproduces the effect".
- **Line 40.** The second sentence chains two studies and three clauses. **Rewrite:** "Fine-tuning a trained model on a sequence of new tasks degrades what it knew before, and in one study of models of one to seven billion parameters the forgetting grew worse with size. The cheap method most often used to adapt large models, which trains a small set of added weights, learns less than full fine-tuning and forgets less, as if learning and forgetting were two sides of the same change."
- **Line 42.** "doing it continually, offline, while the system is otherwise in use" contradicts itself. Use "doing it continually, in the pauses of use, as the brain does in rest and sleep."
- **Line 48 and Figure 11.7 (numbering).** Figure 11.7 is cited at line 48 and placed at line 58, before Figure 11.4. Renumber it 11.4 and shift the later figures (11.4 to 11.6 become 11.5 to 11.7), or move it and its citation to the end of "Learning When to Learn", whose last row it also illustrates. If it moves, keep the number 11.7 only if it comes last.
- **Line 50 (callback).** Chapter 5's body describes pattern completion but names Hopfield only in a note. Use "Chapter 5 described pattern completion, in which a fragment of a memory settles into the whole. John Hopfield's network of 1982 is the classic model of it: memories are stored in the connections among units, ..."
- **Line 54.** The paragraph runs three studies at the same weight. Trim Ba and colleagues to a clause ("Hinton's group had proposed 'fast weights' in 2016, connections that change in seconds to hold the recent past"), and keep Schlag and Whittington.
- **Line 56.** "A team at Google" is the only unnamed group in the chapter; name its lead author (Ali Behrouz). "the first serious attempt" overclaims, since memory-augmented networks go back at least to the Neural Turing Machine. Use "one of the most serious attempts to give a language model what the hippocampus gives a brain".
- **Line 62 (Doya repeated; Behrens abstract).** Doya's correspondence is in the AI sections of both Chapter 3 and Chapter 7. Use "Kenji Doya's proposal, met in Chapter 3, maps the four main neuromodulators onto the settings a learning machine needs." Make Behrens visible (expert to confirm): "Timothy Behrens and his colleagues had people choose between a blue and a green option whose chances of paying off sometimes held steady for long stretches and sometimes reversed every few dozen trials. People raised their learning rate in the volatile stretches and lowered it in the stable ones, as an ideal learner would, and activity in the anterior cingulate cortex tracked the volatility." Split the paragraph before "Kenji Doya".
- **Line 78.** Three chips at the same weight make a catalogue in the chapter's longest section. Hala Point is a scale record without a result. Cut it, or reduce it to "Intel's spiking chips now run a billion simulated neurons on a few kilowatts", which saves about 25 words.
- **Line 80 (186 words).** Split before "Guillaume Bellec".
- **Line 84.** "Some groups train physical systems" is vague. Name one, for example Logan Wright, Peter McMahon, and their colleagues' physical neural networks (Nature 2022), or cut the sentence.
- **Line 98.** "some proposals for safer reward functions do exactly that" is uncited and reads as hand-waving at the section's key moment. Name a concrete instance (expert to supply). One candidate is the penalty used in training language models for drifting too far from the original model, which caps how far any one reward can be pursued.
- **Line 100 (206 words).** Put the history first: move the Schmidhuber sentence to open the paragraph ("Jürgen Schmidhuber proposed curious machines in 1991, rewarded by what their own model of the world failed to predict, and saw at once the problem of unlearnable noise."). Then Pathak, then Burda's television. Split before "Jacqueline Gottlieb".
- **Line 112.** The cataract children are the chapter's only human patients. Give them one sentence of place and scale (expert to verify): "Many of them were treated through Sinha's Project Prakash in India, which finds and treats children blind from birth."
- **Line 116.** The topic sentence says the child "chooses" its curriculum, but the evidence that follows concerns developmental order (Sheybani) and quantity (Orhan and Lake). Use "What the child's curriculum has that an engineered one lacks is that development orders it and the child chooses it." If the expert confirms it, note that Orhan and Lake's video comes from the same kind of head-camera record that Chapter 10 described with Vong and Lake.
- **Line 130.** "Masse's gating worked, which makes the context-dependent activity of prefrontal neurons look less like a curiosity" introduces prefrontal context activity that the chapter never described; line 36 motivated gating with dendritic branches. Use "which makes the separation of tasks onto different dendritic branches look less like a curiosity and more like a solution".
- **Lines 10, 22, 24 (176 to 195 words each).** They hold. Line 10 is a single scene, and lines 22 and 24 are each one argument. I do not ask for splits.

### Copyedits

- Line 16: "Few have yet passed it" and line 136's "none has yet passed the test" can read as a contradiction. Line 16 means principles generally (convolution passed), and line 136 means the remaining lessons. Change line 16 to "Few principles have yet passed it".
- Line 36: "and by gating alone 61 percent" should be "and with gating alone, 61 percent".
- Line 72: "multiplying two 32-bit floating-point numbers about 4" should be "about 4 picojoules", for clarity at first use of the unit. Alternatively, put "picojoules" after "a tenth".
- Line 104: "Adam Kepecs, Zachary Mainen, and their colleagues" should become "Adam Kepecs and his colleagues" if the paragraph is compressed as proposed.
- Figure 11.6 caption: "becomes negative past the set point" does not match panel A, where the reward turns negative at about −1, when the meal would carry the store past the set point. Use "becomes negative when the meal would carry the store past the set point".

Counts: Major 4, Minor 20, Copyedit 5.

## Length and balance

The body is about 6,370 words by my count (about 6,450 by the coordinator's), comfortably under the 7,000 ceiling.

| Section | Words |
|---|---|
| Opening (unheaded) | 538 |
| Copying and Borrowing | 387 |
| Learning Without Forgetting | 881 |
| A Memory That Learns in Use | 725 |
| Learning When to Learn | 423 |
| Local Rules and the Cost of Moving Data | 939 |
| Values That Cannot Be Rewritten | 723 |
| Knowing When to Stop and Think | 379 |
| Growing Up | 465 |
| Borrowing the Data | 343 |
| What Building Teaches Biology | 318 |
| The Central Lesson | 231 |

The balance tilts toward the first half. "Local Rules" (939) and "Learning Without Forgetting" (881) together hold more than a quarter of the body. "Knowing When to Stop and Think" (379) and "Borrowing the Data" (343) are the thinnest, and they are also the sections without a story. "Learning Without Forgetting" earns its length with Figure 11.2 and the Gekhman result. "Local Rules" earns most of its length but carries a catalogue in lines 78 and 84.

Cuts (about 190 words):

- Line 104 and the first half of line 106, Chapter 8 recaps (85).
- Line 122 compressed (50).
- Line 78 Hala Point (25).
- Line 54 Ba trimmed (15).
- Line 62 Doya (15).

Additions (about 340 words):

- Logan and Crump (110).
- Dapello told as an experiment (45 net).
- Behrens made concrete (35).
- Replay correction (30).
- Project Prakash (25).
- Opening heading and the line 26 fix (5).
- The other Minor rewrites (about 60 net).
- Central Lesson rewrite (about 30 net).

The result is about 6,520 words by my count (about 6,600 by the coordinator's), with "Knowing When to Stop and Think" at about 400 words and now built around an experiment, "Borrowing the Data" at about 340 and built around one, and "Local Rules" at about 900. I do not recommend further expansion. The chapter's strength is that each section asks the same four questions briefly.
