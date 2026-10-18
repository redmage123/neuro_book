# Literary Review, Round 2: Chapter 10, "What Artificial Intelligence Gets Right and Wrong: Machine Learning Measured Against the Brain"

Source: `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md` as revised (body lines 10 to 172, about 7,060 words of prose excluding headings, captions, and notes). Line numbers refer to the current file.

## Overall assessment

All seven round-1 Majors are addressed, and most of the Minors are too. The chapter is now the synthesis it was meant to be.

- **The retelling is gone.** "Credit Without Backpropagation" (lines 98 to 102) now opens on callbacks to Chapters 3 and 6. It then spends its words on what is new: Bartunov's test, and Song and Bogacz's prospective configuration. The replay, value, and confidence paragraphs each acknowledge their source chapter in a clause (lines 88, 120, 136).
- **The thesis is delivered.** The sorting paragraph (line 152) takes each of the six differences named at line 18 and places it, and it ends honestly on the one that cannot yet be placed.
- **The handovers land.** Chapter 9's interrupt question is answered at line 140. That paragraph closes on "AlphaGo at move 78 had no such trigger", which ties the section's opening story to Chapter 9's pianist. The Chapter 11 handover is at line 164. The Central Lesson pays off Turing in a way that finally makes the epigraph necessary.
- **The second half now has people in it.** Examples are Lee Sedol's move 78 (line 134), Varley's three men who could not tell who killed the lion but could solve 90 − [(3 + 17) × 3] (line 124), and the reasoning model that writes a dozen solutions to "2 + 3" (line 140). "Knowing What It Does Not Know" has grown from 254 to about 500 words, and the book's long thread on confidence now ends in a story rather than a summary.
- **The callbacks are now accurate.** These are Marr (line 16), the disputed power law (line 56), Chapters 3 and 6 on credit assignment (line 100), and the hippocampal sequences (line 130). The ledger and line 146 now name the same four red rows. Figure 10.7's new rows ("feedback loops in perception", "deciding when to deliberate") match the new paragraphs, and the blue, gold, and red scheme is readable without color.
- **The expert's additions improve the argument rather than burden it.** Linsley's turn (line 40) and the extended Figure 10.2 make "up to a point" visible. Engstrom (line 64) turns a caveat into the point: "changes too slight for the builders of the test set to notice were enough to move every model". The GPT-4 calibration result (line 136) gives the hallucination paragraph evidence instead of assertion. The 2024 retest of the block-stacking problems (line 128) makes "That picture has changed quickly" concrete.
- **Contested findings are stated as contested,** without hedging adverbs: grid cells, infant object expectations, adult neurogenesis, Song and Bogacz, the innateness argument, and human calibration. The house style holds, with no em dashes and no British spellings.

What still keeps prose below 5 is a handful of sentences:

- One transition now points the wrong way after the Linsley addition (line 44).
- One claim outruns its evidence (line 136).
- One passage repeats an earlier one nearly word for word (line 152 against line 102).
- The Turing payoff appears twice.
- One "which" has an ambiguous antecedent (line 102), and one sentence buries its verb (line 28).

The body is also about 60 words over the 7,000 ceiling, and the cuts below fix both. Reader interest is now 5: every section has a story or a turn the reader can follow, and the chapter ends on its strongest sentence.

Prose quality: 4/5. Reader interest: 5/5.

**To reach 5/5 on prose:** make the six Minor fixes below. Together they also bring the body under 7,000 words.

**On the double Turing payoff (coordinator's question):** cut the one at line 80. The paragraph already ends on its best line, "It took the enormous dataset to buy it, much as the child's took evolution." A second aphorism straight after it weakens both. The Central Lesson version is the stronger of the two, and it is the one the epigraph needs, because it closes the book's AI chapter on the epigraph's own terms. Line 152's "by training on a library" then prepares the Central Lesson's "from a library" instead of echoing a line the reader has just read.

## Findings

### Major

None.

### Minor

- **Line 44 (transition now misleads).** "The same story has played out with language" follows two paragraphs about where the vision story broke down (Linsley, Kar). The reader may take it to mean that language models also plateau. Use "Language models have repeated the first part of the story."
- **Line 80 (double payoff).** Cut "Turing's child machine, it turns out, needs either a childhood shaped by evolution or a library." This saves 17 words.
- **Line 102 (ambiguous antecedent).** In "the network first settles its activity on what the outcome should have been and only then changes its synapses, which in their simulations learned faster than backpropagation", it is unclear what "learned". Use "...and only then changes its synapses; in their simulations, networks that learned this way learned faster than with backpropagation and with less interference between tasks."
- **Line 136 (claim outruns its evidence).** "The clearest evidence that training, not the architecture, removes the admission" overstates the result. The GPT-4 result shows that later training worsened calibration; it does not show that training removed admissions of ignorance. Use "The clearest evidence that training can blunt a model's sense of its own reliability comes from OpenAI's report on GPT-4."
- **Line 152 (repeats line 102).** "it may be biology making do without a backward pathway, or, as Song and Bogacz argue, a better way to learn while acting" restates line 102's last sentence nearly word for word, ten lines later in the reader's memory. Use "The local learning rule is the hardest to place: makeshift or improvement, no one yet knows." This saves about 19 words, and the following "No one yet knows." goes.
- **Line 28 (buried verb).** "showed in 1986 that this method, backpropagation, which passes the error ... blame, could train" holds the verb back for 25 words. Use "Backpropagation passes the error at the output backward through the network to assign each weight its share of the blame, and David Rumelhart, Geoffrey Hinton, and Ronald Williams showed in 1986 that it could train networks with hidden layers to discover useful internal representations."

### Copyedits (optional; do not affect the score)

- **Line 30.** "The recordings supported the prediction, and later experiments have extended it.[^11]" is filler after a finished story. Cut it, moving note 11 to the end of the previous sentence (saves 11 words). Figure 10.1 now shows Rescorla and Wagner, but the text does not name them. Change "from models of animal conditioning" to "from the Rescorla-Wagner model of animal conditioning".
- **Line 34.** "end up organized in some respects like the brain inside" stacks its qualifiers. Use "end up organized inside, in some respects, like the brain."
- **Line 118.** To save words, use "Chapter 9's robot hand learned to turn a cube only after training in wildly randomized simulations" (saves about 10 words).
- **Line 140.** "a companion study" is the only unnamed study in the chapter. If the expert confirms it, name the lead author ("Yue Wang and colleagues").
- **Paragraph length.** Line 126 (207 words, three studies) reads more easily split before "Lukas Berglund", and line 124 (194 words) split before "Rosemary Varley". Lines 74, 80, and 88 (186 to 191 words) each hold one line of argument, and I do not ask for further splits.
- **Line 164.** The Chapter 11 handover stands alone as a one-sentence paragraph. Chapter 9 placed its handover at the end of its last point, but here point three is about innateness and the sentence would not fit there, so leaving it alone is acceptable.

Counts: Major 0, Minor 6, Copyedit 6.

## Length and balance

The body is about 7,060 words, roughly 60 over the 6,500 to 7,000 target. The weight is now even across the chapter:

| Section | Words |
|---|---|
| What Is Being Measured | 570 |
| A Shared Ancestry | 504 |
| What the Machines Got Right: Representations | 682 |
| What the Machines Got Right: Error and Prediction | 415 |
| Shortcuts | 418 |
| The Data Gap | 746 |
| Learning That Never Stops | 475 |
| Credit Without Backpropagation | 364 |
| The Energy Bill | 292 |
| Bodies | 369 |
| Fluency and Thought | 612 |
| Knowing What It Does Not Know | 498 |
| What Not to Copy | 492 |
| Implications for Neuroscience | 408 |
| The Central Lesson | 199 |

The first half (through "The Data Gap") and the second half are now roughly equal, as they should be, given that the chapter's title promises both. "Representations" grew by about 170 words with Linsley and Kar, and it earns them, because the section now has an argument (resemblance, then its limits) rather than a list.

The cuts from the Minors and Copyedits total about 60 to 70 words:

- Line 80 Turing (17).
- Line 152 repetition (19).
- Line 30 filler (11).
- Line 118 compression (10).
- Small net savings at lines 28 and 102.

With them the body comes to about 6,990 words, inside the target. I do not recommend further cuts or additions.

**On "Implications for Neuroscience":** the section now works. The opening sentence ties back to Figure 10.1 rather than restating line 14. Point one absorbs the old point four. Point three states the innateness argument as a dispute about measurable numbers, with Piantadosi, the reply, and BabyLM, which is the right way to end on an open question before handing over to Chapter 11.
