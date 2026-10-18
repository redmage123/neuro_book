# Literary Review: Chapter 10, "What Artificial Intelligence Gets Right and Wrong: Machine Learning Measured Against the Brain"

Source: `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md` (body lines 10 to 152, about 6,035 words of prose excluding headings, captions, and notes; 7 figures; 63 footnotes).

## Overall assessment

What works: the chapter has the best opening in the book since Chapter 8. Rosenblatt's perceptron, which the Navy expected to "reproduce itself" and "be conscious of its existence", ends on "It came from the brain" (line 12). That line states the chapter's debt in five words. The three scales of performance, representation, and mechanism (line 16) give the reader a ruler. The thesis (line 18) sets two lists side by side: brains learn from little data, all their lives, on 20 watts, while machines learn from enormous data, once, on megawatts. That is the clearest thesis statement in the book. The best passages are these:

- Zech's pneumonia network that learned to recognize hospitals (line 56).
- Vong and Lake's network trained on one child's camera (line 70).
- "It took the enormous dataset to buy it, much as the child's took evolution" (line 72).
- Aja Huang placing AlphaGo's stones by hand (line 104).
- Kalai's multiple-choice student who never leaves a blank (line 120).
- Bashivan's and Ponce's images designed to drive neurons (line 140).

The house style holds: there are no em dashes, the spelling is American, and numbers follow the house rule. Every figure is cited.

What does not work:

1. **The chapter repeats instead of synthesizing.** It is meant to synthesize the AI sections of Chapters 1 to 9, but in four places it retells them.
   - "Credit Without Backpropagation" (lines 88 to 90) introduces Crick's 1989 objection, random feedback weights, and apical bursts as if they were new. All three are in Chapter 3, line 74.
   - The replay paragraph (line 80) retells Chapter 5's AI section.
   - The value paragraph (line 108) retells Chapter 7's.
   - The confidence paragraph (line 120) retells Chapter 8's.
2. **The thesis promises a sorting that the chapter never delivers.** Line 18 says some differences are failures to repair and others are constraints not to copy, and calls "telling the two apart" the purpose of the chapter. "What Not to Copy" (line 132) then sorts four different traits (slow neurons, imprecision, wiring cost, no reset), none of which is among the six differences the thesis named.
3. **Two handovers are dropped.** Chapter 9 ends by giving this chapter a specific question: when should a fast system hand control back to a slow one? Line 14 restates it, and the chapter never returns to it. Turing's child-machine epigraph is never paid off either.
4. **Four callbacks are inaccurate.**
   - Line 16 sends Marr to the front matter, but he is in Chapter 1.
   - Line 50 cites Chapter 9's power law as settled, though Chapter 9 states it as contested.
   - Line 90 credits Chapter 6 with two lines of attack that are both Chapter 3's.
   - Line 116 refers to a route-simulating hippocampus that Chapter 5 never describes.
5. **The text and the ledger disagree.** Line 128 says Figure 10.7 marks "little data" and "an honest estimate" as weakest, but the figure colors both partly shared.
6. **The second half thins out and the chapter is short.** After "Bodies", no story holds the page. "Knowing What It Does Not Know" is the shortest content section (254 words) on the question the book has built toward since Chapter 8. At about 6,035 words the body falls below the 6,500 to 7,000 target.

Prose quality: 4/5. Reader interest: 3/5.

**To reach 5/5 on prose:** correct the four callbacks and the ledger sentence. Fix the sentences that must be read twice (lines 58, 84, 106, 122). Split the five overlong paragraphs (lines 26, 70, 100, 114, 116). State the two uncited or uncontested claims (lines 68, 142) with their evidence and dispute.

**To reach 5/5 on reader interest:** compress each retold argument to one acknowledging clause, and spend the words saved on what only this chapter can do:

- Sort the six differences, as the thesis promises.
- Answer Chapter 9's interrupt question.
- Add Chapter 6's missing loops, with Kar's recurrence experiment.
- Give the confidence section a story: Lee Sedol's move 78, after which AlphaGo went on believing it was winning.
- Name a human case for the aphasia evidence.
- Pay off Turing.
- Hand over to Chapter 11.

These additions bring the body into the target range.

**On "Implications for Neuroscience":** the reversal works, and it is the right ending for the book's AI chapter. Points one and two are strong, and Bashivan and Ponce are among the chapter's most vivid experiments. Three things weaken it. The opening sentence restates line 14. Point three makes an uncited claim about innateness that is one of the most disputed in cognitive science, and states it as settled. Point four restates line 92. The section also needs to carry the handover to Chapter 11, as Chapter 9's AI section carried the handover to this one.

## Findings

### Major

- **Lines 88 to 90 (credit assignment retold from Chapter 3).** Chapter 3, line 74 already gives Crick's 1989 objection, random feedback weights, apical bursts, and Lillicrap's 2020 argument, and says "Chapters 5 and 6 return to the question." Line 88 reintroduces Crick as news. Line 90 then says "Chapter 3 and Chapter 6 described two lines of attack" and describes two lines that both come from Chapter 3. Chapter 6's contribution, predictive coding as an approximation of backpropagation (Whittington and Bogacz, Chapter 6 note 62), is missing.
  - **Rewrite line 88's second sentence:** "Chapter 3 recounted Francis Crick's objection of 1989: axons carry signals one way, and a synapse has no evident means of learning the strength of a synapse somewhere downstream.[^39]"
  - **Rewrite line 90's first two sentences:** "The question has not been settled, and the two most developed answers were met in Chapters 3 and 6. Chapter 3 showed that a backward pathway with random, fixed weights is enough, because the forward weights come to align with it, and that bursts arriving at the apical dendrites of pyramidal neurons could hold an error apart from the cell's main output; Chapter 6 showed that a network built to correct its predictions, as cortex may be, can compute nearly the same weight changes that backpropagation does.[^40]"
  - Keep Sacramento and Payeur, which are new, and keep the closing sentence. This saves about 60 words.

- **Lines 18 and 124 to 132 (the promised sorting is never done).** The thesis names six differences and says telling the failures from the constraints is "the purpose of the comparison". Line 132 sorts a different list. **Add after line 132** a paragraph of about 150 words: "Sorted this way, the differences named at the start of this chapter fall on both sides. Learning all its life without forgetting, and an honest estimate of what it knows, are solutions to problems that every system meets once it is put to use, and machines lack them to their cost. The brain's frugality is also a solution, forced by a constraint that now binds silicon too. Its small appetite for data is partly evolution's gift, which a machine can buy back, expensively, by pretraining. Values anchored to a body are a constraint a machine need not share, although what the anchoring buys, a limit on how far goals can drift, is something machines still need by other means. The local learning rule is the hardest to place: it may be biology making do without a backward pathway, or it may be a better way to learn while acting. No one yet knows, and that question is where Chapter 11 begins." Then cut "The task is to separate the solutions from the constraints that produced them" at the end of line 132, which the new paragraph replaces.

- **Lines 14 and 118 to 122 (Chapter 9's handover is dropped, and the confidence section is thin).** Chapter 9 ends: "Whether machines can learn it [when to switch from fast to slow], and what else they lack, is the question of Chapter 10." Line 14 echoes it, and nothing answers it. "Knowing What It Does Not Know" is 254 words, and its first paragraph retells Chapter 8's point that models "can estimate fairly well" whether they are right.
  - **Open the section with a story** that follows on from line 104 (about 80 words; expert to verify the details against Metz, note 47): "Lee Sedol won one game of the five. In the fourth, his 78th move was one that AlphaGo had judged about one chance in 10,000 for a human player to find, and for several moves afterward the program went on estimating that it was winning while its play fell apart; Hassabis said afterward that it recognized its mistake only around move 87. A system that had learned its confidence from its own games met a position unlike them and did not know it."
  - **Compress line 120's Chapter 8 material** to "Models can be trained to estimate whether their own answers are right, as Chapter 8 noted, and do it fairly well within the range of their training.[^59]"
  - **Add a closing paragraph** (about 90 words): "Chapter 9 ended on a related question: when a fast system should hand control back to a slow one. A pianist plays automatically until a wrong note, and the wrong note is the signal. Language models that reason at length have begun to make this decision for themselves, spending more reasoning on problems they judge harder, but the judgment is learned from whatever training rewarded and is often poorly matched to difficulty. The brain's trigger is simpler and more reliable: an expected outcome that fails to arrive." The expert should supply one study for the miscalibration claim, for example on reasoning models that overthink easy problems, or the sentence should be softened.

- **Line 128 and Figure 10.7 (the text contradicts the ledger).** The text lists "from little data" and "with an honest estimate of what it knows" as the weakest areas, but the figure colors both partly shared, and it colors the local learning rule and bodily values red, which the text omits. **Rewrite the final sentence:** "Learning for a lifetime without forgetting, by rules available at each synapse, on a small energy budget, with values anchored to something it cannot redefine: these are the rows Figure 10.7 marks as largely absent, and they are among the problems the brain was shaped by." If the loops paragraph below is added, add the row "feedback and recurrence in perception: partly shared". If the Chapter 9 paragraph is added, add "deciding when to deliberate: partly shared".

- **Lines 30 to 42 (Chapter 6's "loops" are missing).** Chapter 6's AI section says the feedforward sweep has been reproduced and "the loops have not been". This chapter's case for representations rests entirely on feedforward results and never revisits that verdict. **Add before "The fair conclusion" in line 42** (about 80 words; expert to verify): "Chapter 6 noted that the networks had copied the brain's first sweep through the visual hierarchy but not its loops, and the gap shows in timing. Kohitij Kar, DiCarlo, and their colleagues found images that monkeys recognized and feedforward networks did not. For those images the object's identity appeared in IT tens of milliseconds later than for easy ones, as if it had needed a second pass, and networks with recurrent connections predicted the late responses better.[^new: Kar, Kubilius, Schmidt, Issa, and DiCarlo, *Nature Neuroscience* 2019]"

- **Line 142 (innateness stated as settled, without citation).** "A system with no built-in grammar learned to produce grammatical language ... it narrows what has to be innate." This is the poverty-of-the-stimulus debate, and both halves are contested. **Rewrite:** "Third, machine learning has reopened an old argument about how much of the mind must be innate. Systems with no built-in grammar now produce grammatical language from text alone, and Steven Piantadosi has argued that this undermines the case for an innate universal grammar.[^new] Others reply that the models need thousands of times more language than a child hears, so that they show what can be learned from text in bulk, not what a child learns from what it hears. The disagreement is now about numbers that can be measured, which is progress."

- **Lines 146 to 148 (Central Lesson: the epigraph is never paid off and half the thesis is missing).** The paragraph restates what machines took and lacked, but it omits the thesis's second half (what not to copy). It also ends on "where the next comparisons will be made", which is flat. **Rewrite:** "Machine learning took one idea from the brain, that knowledge can be learned into the strengths of many connections by correcting errors of prediction, and proved it more powerful than its inventors could: trained at scale, networks match people at tasks once thought to need a mind, and arrive at representations like those of a cortex they were never shown. What they did not take are the conditions under which a brain learns. A brain learns from little data because evolution has done much of the work, learns all its life because it replays what it knows and keeps its synapses changeable, and runs on 20 watts because it computes sparsely where its memory is. Some of those conditions are constraints a machine is right to ignore; the rest are answers to problems that every learner meets once it leaves the laboratory. Turing proposed in 1950 to build a machine that learns like a child. Seventy-six years later the machines learn, but not like children: they learn once, from a library, at great cost, and then stop. The child's way is still the harder one to build." At the end of "Implications for Neuroscience", add the handover: "What the brain could still lend to machines, and how its mechanisms might be built into them, is the subject of Chapter 11."

### Minor

- **Line 14.** The roll call skips Chapters 1, 2, 4, and 7, although Chapter 7's question returns at line 108. Add "Chapter 7, what a machine can value when it has no body;" after the Chapter 6 clause.
- **Line 16 (Marr misattributed).** The front matter's levels are physical, cellular, circuit, and cognitive. Marr is in Chapter 1, line 34, and the three scales here are not Marr's levels. **Rewrite:** "Chapter 1 kept apart, after David Marr, what a system computes, the procedure it uses, and the hardware that runs it, and the three scales borrow that discipline. The distinction matters here because current machine learning scores very differently on them.[^2]"
- **Line 22 and Figure 10.1.** Hebb appears in the figure, with an arrow into the perceptron, but not in the text. Change "weights that changed with experience" to "weights that changed with experience, as Donald Hebb had proposed in 1949 that synapses do".
- **Line 26 (188 words).** Split before "The method of training such a network came from engineering."
- **Line 34.** "IT" is used before it is defined. Change it to "inferior temporal cortex (IT)".
- **Line 50 (power law stated as settled).** Chapter 9 states the power law of practice as contested. Change "A power law of improvement with experience is the shape that Chapter 9 found for human practice" to "A power law is also the shape often fitted to human practice, as Chapter 9 described, though there the fit is disputed". Optionally cut the Chinchilla numbers ("with 70 billion parameters trained on 1.4 trillion tokens") to save about 10 words.
- **Line 58.** Habits are cached answers that outlive their reasons, while shortcuts are spurious cues, so the analogy is loose. "Even small changes of context can expose a network that has not" has an unclear antecedent. **Rewrite:** "The brain is not free of shortcuts: Chapter 9's habits go on producing yesterday's answer after the reason for it has gone. But a person ... the ones that matter. A network trained on one collection of images has had no such schooling, and even small changes can expose it."
- **Line 64.** "the language model that in 2020 first wrote convincing prose" makes a priority claim that is easily disputed. Use "the language model that in 2020 made fluent machine prose familiar".
- **Line 68 (contested infant finding).** "a newborn human ... expects objects to persist when hidden" is not established for newborns. The classic evidence (Baillargeon) is from infants a few months old, and its interpretation is disputed. Use "a newborn turns toward faces, and infants a few months old look longer when a hidden object seems to have vanished" (expert to confirm).
- **Line 70 (190 words).** Split before "The result shows". If the source allows, add one concrete image of the child wearing the camera; it is the chapter's only child on the page.
- **Line 72.** Pay off the epigraph here or in the Central Lesson, not both. If the Central Lesson rewrite is not taken, end line 72 with: "Turing's child-machine, it turns out, needs either a childhood of evolution or a library."
- **Line 80.** Chapter 5's AI section already makes the replay point and calls it "a convergence, not a borrowing". Acknowledge it: "Machine learning had found the same answer independently, as Chapter 5 noted, and Volodymyr Mnih ..."
- **Line 80 and Figure 10.5.** "forgets the first list almost completely within a few passes" does not match the figure: list A is still about half recalled after five passes and reaches zero after about 25. Use "within about 25 passes, fewer than it took to learn it".
- **Line 84.** "It keeps making new synapses and removing unused ones, Chapter 9's motor cortex grows spines ..., and the hippocampus adds new neurons in many mammals" runs three unlike clauses together. Adult neurogenesis in humans is also disputed. **Rewrite:** "The brain does something that looks similar. It keeps making new synapses and removing unused ones, as Chapter 9's motor cortex did for a new skill, and in many mammals the hippocampus adds new neurons throughout life, although whether adult humans do so is disputed."
- **Line 100 (197 words).** Split before "Machine learning has begun to rediscover parts of this."
- **Line 106.** "What the child has, and Chapters 6 and 9 described, are forward models" is ungrammatical. Use "What the child has are the forward models of Chapters 6 and 9: predictions of ..."
- **Line 108.** This retells Chapter 7's AI section. Compress the first two sentences to "Chapter 7 argued that value in the brain is anchored to the state of the body, which limits how far an animal's goals can drift."
- **Line 112.** The aphasia evidence has no person in it. Name one study (expert to supply), for example Rosemary Varley and colleagues' men with severe agrammatic aphasia who could no longer understand "John loves Mary" but could still solve arithmetic problems of similar structure.
- **Line 114 (237 words, three studies).** Split after the McCoy result. Cut the 51 versus 13 percent sentence, since the cipher shift already makes the point. That saves about 30 words.
- **Line 116.** "This is Chapter 8's accumulation to a bound in a new form" repeats Chapter 8's own AI section. Use "Chapter 8 saw in this an echo of accumulation to a bound." "the way Chapter 5's hippocampus appears to simulate routes before an animal takes them" has no source in Chapter 5, which describes replay of past runs, not simulation of future ones. Use "the way Chapter 8's planning system consults a model of the world before it acts". Split before "Other systems learn models".
- **Line 122.** "The brain's version of this depends on what the last section described" points to "Fluency and Thought", but the body was discussed two sections back. Use "The brain's version of this depends on the body." "The brain, on the evidence of this book, cares about being right because being wrong has cost it something" is a proposal, not a finding. Use "One reason the brain may care about being right is that being wrong has cost it something."
- **Line 126.** Name the essay; many readers know it by its title. Use "wrote in 2019, in an essay called 'The Bitter Lesson', that ..."
- **Line 136.** This restates line 14. Use "The traffic of Figure 10.1 runs both ways, and in the last decade the return direction has been the busier one: machine learning has changed neuroscience as much as neuroscience changed it."
- **Line 138.** "Before 2014 a model of visual cortex was a set of filters chosen by hand" overstates the case, since HMAX and its relatives learned some of their features. Use "Until the mid-2010s, models of visual cortex were built largely from filters chosen by hand".
- **Line 144 (point four restates line 92).** Either merge it into point one as a closing sentence ("Describing the brain this way has made old questions precise: what its objectives are, whether it approximates the gradient, and how it keeps its plasticity.") or cut it.
- **Figures 10.3 and 10.6.** These are bar charts on a log axis with an arbitrary baseline (10^6 words, 0.1 MWh), so the bar lengths suggest ratios that are false: the child's bar looks about a fifth of Llama 3's. Use dots with labels on the log axis, or note the baseline in the caption.
- **Figure 10.7.** Red and green carry the categories. The text labels make it readable for color-blind readers, but a blue and orange scheme would be safer and would match Figures 10.3 and 10.6.

### Copyedits

- Line 72: "and argued, with colleagues, that" should be "and, with colleagues, argued that".
- Line 96: "a single current data-center processor" will date. Use "a single data-center processor of 2024".
- Note 46: it cites AlphaGo Zero (Silver et al. 2017) for the 2016 match against Lee Sedol. The expert should check whether Silver et al. 2016 ("Mastering the game of Go with deep neural networks and tree search") or a match report is the intended source.
- Figure 10.3: "a child by age 5" should be "a child by age five", to match the text's house style.
- Line 26: "from 26 percent to 15" should be "from 26 percent to 15 percent", for parallelism.

Counts: Major 7, Minor 27, Copyedit 5.

## Length and balance

The body is about 6,035 words, roughly 465 below the bottom of the 6,500 to 7,000 target. The weight falls well in the first half and thins in the second:

| Section | Words |
|---|---|
| What Is Being Measured | 545 |
| A Shared Ancestry | 449 |
| What the Machines Got Right: Representations | 514 |
| What the Machines Got Right: Error and Prediction | 382 |
| Shortcuts | 350 |
| The Data Gap | 650 |
| Learning That Never Stops | 422 |
| Credit Without Backpropagation | 339 |
| The Energy Bill | 283 |
| Bodies | 390 |
| Fluency and Thought | 555 |
| Knowing What It Does Not Know | 254 |
| What Not to Copy | 381 |
| Implications for Neuroscience | 351 |
| The Central Lesson | 156 |

"The Data Gap" is the longest section and earns it. "Knowing What It Does Not Know" carries the question the book has built toward since Chapter 8, yet it is the shortest content section. "Credit Without Backpropagation" spends about half its words on Chapter 3.

Cuts (about 185 words):

- Line 88 to 90 Chapter 3 retelling (60).
- Line 114 cipher percentages (30).
- Line 108 Chapter 7 retelling (25).
- Line 120 Chapter 8 retelling (25).
- Line 144 point four merged (30).
- Line 50 Chinchilla numbers (10).
- Line 136 opener (5).

Additions (about 700 words):

- Line 42, Kar's recurrence paragraph (80).
- Line 112, the aphasia case (50).
- Knowing section, Lee Sedol's move 78 (80) and the Chapter 9 interrupt paragraph (90).
- Line 132, the sorting paragraph (150).
- Line 142, the innateness point restated as contested (50 net).
- Central Lesson rewrite (35 net).
- Chapter 11 handover (25).
- Line 14 Chapter 7 clause (10).
- Line 22 Hebb (15).
- Line 126 "The Bitter Lesson" (5).
- The other minor rewrites (about 110 net).

The result is about 6,550 words, inside the target. "Knowing What It Does Not Know" grows to about 470 words and "What Not to Copy" to about 530, so the second half carries weight equal to the first.
