# Literary Review: Chapter 13, "Why the Brain Works the Way It Does: Constraints, Trade-offs, and the Shape of a Solution"

Source: `docs/book/Word/Chapter13/How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md` (body lines 10 to 158, about 6,690 words of prose by my count, excluding headings, captions, and notes). It has 7 figures and 57 footnotes.

## Overall assessment

What works:

- **The opening.** The eyeless cavefish is the best opening in Part VI: a measured bill (15 percent of a small fish's resting metabolism) for an organ that is no longer needed, stated with the right caution about whether the saving explains the loss (line 12).
- **The thesis.** Tinbergen's four questions (line 16) give the chapter a clear job, and the thesis is precise: "the brain's form is where a few hard physical constraints meet a history that could only modify what already existed". Tinbergen returns as the experimenter of supernormal stimuli (line 132) and in the Central Lesson's last sentences, which makes a satisfying frame.
- **The chapter writes in sentences a reader will keep:**
  - "Sparse firing is not a shortage of activity; it is what an efficient code looks like when spikes are dear" (line 28).
  - "The spike is what long distances cost" (line 42).
  - "Imagine yourself with a 100-fold thicker spinal cord!" (line 48).
  - "the compromise is the design" (line 74).
  - "It shows what a tinkerer does with a design it cannot discard" (line 104).
  - "It is the only way a brain of this size can be finished" (line 112).
  - "The brain is not the best possible brain, and it is not a botched one" (line 154).
- **The stories are many and well chosen:**
  - The squid's half-millimeter axon.
  - The gel brain that folds in minutes.
  - Cherniak's worm, whose layout is the best of 39,916,800.
  - Darwin's finches in their triangle.
  - Cooking and the nine-hour day.
  - The wasp whose neurons discard their nuclei.
  - Ravens and macaws with more neurons than monkeys.
  - The octopus.
  - The inverted retina rescued by Müller cells.
  - The gull chicks, the oystercatcher, and the beetle courting a beer bottle.
- **Contested claims are stated as contested:** the cavefish saving, the cooking arithmetic, the expensive-tissue hypothesis, the obstetric dilemma, Ringo's conjecture, mismatch, and bird-mammal convergence.
- **The house style holds,** with no em dashes and no British spellings.
- **The figures earn their places.** Figure 13.3 shows the cost of speed in space at a glance. Figure 13.4 makes "a few long connections buy most of the gain" visible. Figure 13.6 makes the genome bottleneck a picture.

What does not work:

1. **The chapter promises to answer Chapter 12's questions and answers only two of them.** Line 14 restates Chapter 12's four: why spikes, why a hierarchy of areas, why a fast memory beside a slow one, and why the brain spends its energy as it does. Spikes and energy get full sections. The hierarchy is never explained. The fast and slow memories appear only as a restatement of Chapter 5 (line 122), not as the answer to a constraint.
2. **The front of the chapter is the least pictured.** "The Price of a Bit" (835 words, the longest section) is a run of measurements on flies, synapses, and axons, with no scene a reader can see. It comes right after the cavefish. It also reintroduces material from Chapters 1 and 2 (Lennie, Allen and Stevens, the squid axon).
3. **The AI section's first point restates Chapters 10 and 11.** Horowitz's energy table, with its numbers, is Figure 11.5. Mixtures of experts appear in both Chapter 10 and Chapter 11. This leaves a 243-word paragraph (line 142) whose only new facts are DeepSeek's ratio and the link to Levy and Baxter.

The smaller issues are these:

- **One callback has no source.** Line 78 sends the reader to Chapter 5 for degenerate ion-channel mixtures that no chapter describes.
- **Two numbers disagree.** The brain has 86 billion neurons at line 84 but 100 billion at line 108. Zador's "at least six orders of magnitude" (line 108) is contradicted by Figure 13.6's "factor of about 600,000".
- **One surname is missing its first name** ("Cordey", line 90).
- **Six paragraphs run past 200 words,** each with two strands.

Prose quality: 4/5. Reader interest: 4/5.

**To reach 5/5 on prose:** make the three Major fixes, correct the callback and the numbers, and split the long paragraphs.

**To reach 5/5 on reader interest:** give "The Price of a Bit" a picture, and use the hierarchy addition to bring in a vivid, concrete experiment: Clune's evolved networks, which became modular and hierarchical once connections had a cost. Add Prinz and Marder's millions of simulated lobster circuits to "Many Jobs at Once", the shortest of the argument sections. The changes leave the body at about 6,750 words.

## Findings

### Major

- **Line 14 against the body (two of Chapter 12's four questions unanswered).**
  - **The hierarchy.** In "Placing the Parts", after line 66, add about 120 words (expert to verify): "Wire cost may also explain why the brain is organized into modules and a hierarchy of areas. Jeff Clune, Jean-Baptiste Mouret, and Hod Lipson evolved networks in a computer to perform tasks, once with connections free and once with a cost for each connection. The networks that paid for their wiring evolved separate modules, each handling part of the problem, and performed as well or better; in a follow-up, Henok Mengistu, Joost Huizinga, Mouret, and Clune found that the same cost also produced hierarchy, modules built from modules. A brain that pays for every axon is pushed toward the arrangement of areas the earlier chapters described."
  - **The two memories.** In line 122, add one sentence that names the constraint: "The constraint here is statistical rather than physical: a single network that learns fast enough to capture one experience will overwrite what it knew, so two learners at different rates are the economical answer."
  - Alternatively, if neither addition is wanted, narrow line 14's list to the questions the chapter answers.

- **Lines 20 to 34 ("The Price of a Bit": long, unpictured, and partly retold).**
  - Open the section with the contrast in Niven's flies, put as a picture before the arithmetic. For example: "A blowfly patrolling a sunlit carcass and a fruit fly drifting over a bowl of fruit have eyes of the same plan but very different budgets." Then give the bits and the energy (line 26).
  - Compress the reintroductions. In line 22, Chapter 1's budget can be one clause. In line 32, use "the synaptic failures that Chapter 1 described, more than half of all impulses at a hippocampal synapse" in place of re-naming Allen and Stevens.
  - Split line 32 before "An experiment by Julia Harris".
  - These changes save about 40 words and give the reader something to see before the information theory.

- **Line 142 (AI point one restates Chapters 10 and 11).** Replace the Horowitz numbers and the mixture-of-experts history with callbacks, and keep what is new. **Rewrite:** "First, the constraints of silicon are different, and where they coincide with the brain's, engineers have arrived at the brain's solutions without copying them. Chapter 11 described Horowitz's table: fetching a number from memory costs far more than computing with it. One response, met in Chapters 10 and 11, is the mixture of experts, in which each word is sent to only a few of a model's many subnetworks. DeepSeek-V3, released at the end of 2024, has 671 billion parameters, of which 37 billion, about one in eighteen, are used for each word it processes.[^57] This is the economy Levy and Baxter described: a large population of which only a small fraction is active at once, because activity is what costs. It is a convergence, not a borrowing, and like the convergences of Chapter 11 it suggests that the constraint is doing the work." This saves about 110 words. Notes 55 and 56 can be cut or folded.

### Minor

- **Line 48 (202 words).** Split before "Figure 13.3 shows the two scaling rules". "37°C" should be "37 degrees Celsius", matching Chapter 12's "37 degrees".
- **Line 78 (callback without source).** No chapter describes "how many different mixtures of ion channels can give a neuron the same pattern of firing". Replace the Chapter 5 clause with a story of its own (about 60 words; expert to verify): "Astrid Prinz, Dirk Bucher, and Eve Marder simulated millions of versions of the small circuit that drives a lobster's stomach and found that widely different combinations of ion channels and synaptic strengths produced nearly the same rhythm." This also gives "Many Jobs at Once", at 392 words the shortest argument section, a second scene.
- **Line 84 against line 108 (86 against 100 billion neurons).** At line 108, use "The brain has about 86 billion neurons, which Zador rounds to 100 billion, each with more than a thousand synapses."
- **Line 86.** The expert should confirm the age at which brain glucose use peaks in Kuzawa's data. I recall it as about five years rather than four.
- **Line 90.** "Cordey and her colleagues" needs a first name, as everywhere else in the book.
- **Line 92 (214 words, four stories).** Split before "A honeybee, with fewer than a million neurons".
- **Line 100 (200 words).** Split before "Martin Stacho, Onur Güntürkün". "Studies of cell types and development published in 2025" is the only unnamed group in the section; name a lead author.
- **Line 108 (Zador against Figure 13.6).** The quoted "at least six orders of magnitude" conflicts with the computed shortfall of about 600,000, which is under six orders. Use "it would fall short by a factor of about 600,000, nearly six orders of magnitude", or keep Zador's words and say that his estimate assumes more bits per connection. Either way, the text and the figure should agree.
- **Line 122.** "which is why, as Chapter 12 described, a waterfall can make a still rock face appear to drift". Good callback; keep it.
- **Line 150.** "in classrooms, offices, and in front of screens" breaks the parallel. Use "in classrooms, in offices, and in front of screens".
- **Line 154 (optional).** The Central Lesson returns to Tinbergen but not to the cavefish. A closing clause would complete the frame, for example after "It is a set of compromises struck under a few hard constraints": "the cavefish's lost eyes are one such compromise, struck again when the world changed."

### Copyedits

- Line 12: "a small silvery fish" is fine. The coordinator's brief and the heading call it a cavefish, while the text says "cave fish" (two words) at lines 12 and 14. Standardize on "cavefish", as line 14 already does once.
- Line 54: "would be prohibitively slow" adds an adverb the sentence does not need; "would be too slow" is stronger.
- Line 74: "an 'archetype,'" puts the comma inside the quotation marks, which is American style and correct. Line 100's "pallium, the region corresponding to the cortex," is fine.
- Figure 13.1: the history box says "basal ganglia kept for 500 million years", but line 98 says the lineages split "about 560 million years ago". Harmonize them.
- Figure 13.6: the green bars are the only green in Part VI, since Chapter 10's ledger was moved to blue, gold, and red. Consider blue for the genome bars, for consistency and for readers with red-green color blindness.

Counts: Major 3, Minor 11, Copyedit 5.

## Length and balance

The body is about 6,690 words by my count, inside the 6,500 to 7,000 target.

| Section | Words |
|---|---|
| The Fish That Gave Up Its Eyes | 478 |
| The Price of a Bit | 835 |
| Why Spikes | 366 |
| Speed Costs Space | 812 |
| Placing the Parts | 418 |
| Many Jobs at Once | 392 |
| How Big a Brain | 797 |
| Different Histories, Same Answers | 611 |
| The Bottleneck of the Genome | 433 |
| Trade-offs That Cannot Be Escaped | 350 |
| Built for a Different World | 388 |
| Implications for Artificial Intelligence | 590 |
| The Central Lesson | 199 |

**Structure and pacing.** The order is sound. It runs from the cost of a single signal (bits, spikes, speed), through the layout of the whole (wire, compromise, size), to history (convergence, the genome), synthesis (trade-offs), and misfit (supernormal stimuli). The weakness is at the start. The three physical sections run about 2,000 words with only the squid and the gel brain as scenes, and "The Price of a Bit" carries the heaviest arithmetic with no picture at all. "Trade-offs That Cannot Be Escaped" (350) is a synthesis without a story, which is acceptable because Figure 13.7 carries it and the section is brief.

**Repetition with earlier chapters:**

- Chapter 1's budget, tinkerer, degeneracy, and sensitive periods are acknowledged as callbacks.
- Chapter 2's passive spread, myelin, and the floor on axon width are acknowledged as callbacks.
- Chapter 4's small-world networks and hubs are acknowledged and extended with new data (Kaiser and Hilgetag, Figure 13.4).
- The two places that retell rather than recall are Allen and Stevens (line 32, already in Chapters 1 and 2) and the AI section's Horowitz and mixtures of experts (Chapters 10 and 11). Both are covered above.

**Proposed changes:**

- Cuts (about 150 words): line 142 (110), and lines 22 and 32 (40).
- Additions (about 220 words): the hierarchy experiment (120), the memory sentence (35), Prinz and Marder (60), and minor clauses.

The result is about 6,760 words, within the target, with "Placing the Parts" (about 540) and "Many Jobs at Once" (about 450) brought closer to their neighbors and the AI section at about 480.
