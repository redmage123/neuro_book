# Cross-reference audit: How the Brain Learns

Scope checked: every "Chapter N" / "Chapters N and M" mention in the 17 chapter bodies, the front matter, the glossary, and the 16 companion files (about 600 chapter references); every "Figure N.M" reference (all of them resolve to an existing figure, and every panel letter reference, such as 2.7A or 5.4B, matches a panel in the caption); every "# Next Chapter" section (all 16 name the correct next chapter with the exact subtitle used in that chapter's front matter); every "Lab N.M" reference in the companions (all resolve, and the cross-lab references 2.1, 3.5, 5.1, 6.1, and 8.6 point to labs on the stated topic); and unnumbered pointers ("next section", "later chapters", "returns to it").

Format: `path:line | current text | problem | proposed replacement`

## docs/book/Word/Frontispiece/How_the_Brain_Learns_Front_Matter.md

- `docs/book/Word/Frontispiece/How_the_Brain_Learns_Front_Matter.md:49-83` | "Part I --- Physical Foundations ... Chapter 3 Electricity in Living Tissue ... Chapter 20 A Coherent Model of the Human Brain ... Glossary\ References\ Index" | The Contents list still follows the old 20-chapter plan. There is no Chapter 0, Chapters 3 to 20 have the wrong numbers or titles, it leaves out Chapter 16 (NIMCP), and it lists chapters that were never written ("Electricity in Living Tissue", "Action Potentials", "Synapses", "Excitation, Inhibition, and Stability", "How the Brain Decides What to Learn", "Memory Is Not Storage"). It also lists an Index, which does not exist in docs/book (BackMatter holds only the Glossary, and references are given per chapter). The "---" em dashes in the Part headings also break the no-em-dash rule. | Replace lines 49-83 with the following (the Part grouping is a suggestion; the chapter lines are the real titles):
  ```
  **Part I: Physical Foundations**\
  Chapter 0 Foundations: The Physical and Chemical Basis of Life\
  Chapter 1 What the Brain Is (and Is Not)\
  Chapter 2 Neurons: The Brain's Signaling Cells

  **Part II: Chemical Context, Circuits, and Memory**\
  Chapter 3 Neuromodulation: How Chemical Context Shapes Learning and Behavior\
  Chapter 4 Circuits, Networks, and Coordinated Behavior\
  Chapter 5 Plasticity and Memory: How Experience Becomes Structure

  **Part III: Perception, Emotion, Decision, and Skill**\
  Chapter 6 Perception as Inference: How the Brain Sees What It Expects\
  Chapter 7 Emotion and the Body: How Internal States Tell the Brain What Matters\
  Chapter 8 Decision-Making Under Uncertainty: How the Brain Chooses When It Cannot Be Sure\
  Chapter 9 Habits, Skills, and Automaticity: How Practice Turns Choices into Routines

  **Part IV: From Biological Brains to Artificial Systems**\
  Chapter 10 What Artificial Intelligence Gets Right and Wrong: Machine Learning Measured Against the Brain\
  Chapter 11 Integrating Brain Mechanisms into AI Models: What Machines Could Borrow from Biology

  **Part V: Integration and Implications**\
  Chapter 12 The Brain as a Predictive, Adaptive System: Is There One Principle Beneath the Mechanisms?\
  Chapter 13 Why the Brain Works the Way It Does: Constraints, Trade-offs, and the Shape of a Solution\
  Chapter 14 Implications for Learning, Work, and Technology: What the Brain's Design Asks of the World We Have Built\
  Chapter 15 A Coherent Model of the Human Brain: How the Pieces Fit\
  Chapter 16 NIMCP: Building a Brain from the Book's Principles

  Glossary
  ```

## docs/book/Word/Chapter3/How_the_Brain_Learns_Chapter_3_Neuromodulation.md

- `docs/book/Word/Chapter3/How_the_Brain_Learns_Chapter_3_Neuromodulation.md:74` | "Chapters 5 and 6 return to the question." | The question is credit assignment and whether the brain approximates backpropagation. Chapter 6 never discusses it (it has no mention of backpropagation, credit assignment, or Whittington and Bogacz), and Chapter 5 gives it one sentence (line 170). The chapters that actually return to it are Chapter 10 ("Credit Without Backpropagation", lines 96-102) and Chapter 11 ("Local Rules and the Cost of Moving Data", lines 76-96). Chapter 15:122 itself says "a question Chapters 3, 10, and 11 returned to repeatedly". | "Chapters 10 and 11 return to the question."

## docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md

- `docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md:100` | "The two most developed answers were met in Chapters 3 and 6. ... Chapter 6 showed that a network built to correct its own predictions, as cortex may be, can compute nearly the same weight changes that backpropagation does, using only plasticity local to each synapse." | Chapter 6 does not show this. It describes predictive coding as a model of perception, but it never connects predictive coding to backpropagation or weight changes; nothing in Chapter 6 matches "gradient", "backpropagation", "weight change", "Whittington", or "Bogacz". The Chapter 3 half of the sentence is correct (Chapter 3:74 covers random feedback weights and apical bursts). | "The two most developed answers build on Chapters 3 and 6." and "A network built to correct its own predictions, as Chapter 6 proposed cortex may be, can compute nearly the same weight changes that backpropagation does, using only plasticity local to each synapse."

## docs/book/Word/Chapter13/How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md

- `docs/book/Word/Chapter13/How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md:104` | "The basal ganglia, the loops that select actions and that dopamine teaches (Chapters 3, 8, and 9)" | This leaves out the chapter that actually describes the basal ganglia loops. Chapter 4 ("Two Loops for Action", lines 100-108, Figure 4.8) covers selection by disinhibition and dopamine acting on the striatum. Chapter 3 mentions the basal ganglia only in passing, as "the basal ganglia circuit of Chapter 4" (Chapter 3:120). | "(Chapters 3, 4, 8, and 9)"
- `docs/book/Word/Chapter13/How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md:40` | "Chapter 2 described how a voltage spreading passively along a thin fiber fades over a short distance, and how noise added at each point along the way accumulates with it." | Chapter 2 describes the passive fade (line 74, Rall's cable), but it never describes noise building up along the fiber. Its only noise passages are about synaptic release variability (line 58) and channel noise setting a minimum axon diameter (line 126). | "Chapter 2 described how a voltage spreading passively along a thin fiber fades over a short distance, and any noise added at each point along the way accumulates with it."

## docs/companion/Chapter3/Word/How_the_Brain_Learns_Chapter_3_Student_Notes_and_Labs.md

- `docs/companion/Chapter3/Word/How_the_Brain_Learns_Chapter_3_Student_Notes_and_Labs.md:79` | "Chapters 5 and 6 return to this." | Same error as Chapter 3:74. Credit assignment and backpropagation come back in Chapters 10 and 11, not in Chapter 6. | "Chapters 10 and 11 return to this."
- `docs/companion/Chapter3/Word/How_the_Brain_Learns_Chapter_3_Student_Notes_and_Labs.md:10` | "Chapters 1 and 2 gave you a neuron that integrates inputs and sometimes fires." | Chapter 1 has no neuron model. The Chapter 1 companion itself says (line 10) that Chapter 1 "contains almost no neurobiology on purpose", and the book's Chapter 3:12 says "Chapter 2 built a neuron." | "Chapter 2 gave you a neuron that integrates inputs and sometimes fires."

## Checked and found correct (no action)

- All 16 "# Next Chapter" sections (Chapters 0-15) name the right next chapter with its exact subtitle. Chapter 16 correctly has none.
- All Figure N.M references in the book and companions point to figures that exist. The only cross-chapter figure reference (Chapter 11:148, "Figure 10.1") matches its caption ("Eighty years of exchange"). Every panel reference matches a panel in its caption.
- All Lab N.M references in the companions point to labs that exist and are on the stated topic.
- The early chapters (0-2) use the current numbering throughout. No leftovers from the old 20-chapter plan were found anywhere except the front matter Contents.
- Spot checks that passed include Chapter 1:56/82/106 (Chapter 5 on replay and slow learning), Chapter 2:96 (Hodgkin and Huxley in Chapter 1:40), Chapter 8:40 (hyperdirect path in Chapter 4:104), Chapter 8:146 (Frank 2004 in Chapter 3:116), Chapter 10:92 and 11:36 (elastic weight consolidation in Chapter 9:162), Chapter 10:118 (Rubik's cube hand in Chapter 9:160), Chapter 11:70 (plasticity gated by a learned modulatory signal and meta-learning in Chapter 3:130), Chapter 12:80 (Behrens in Chapter 11:66), Chapter 12:106 (savings in Chapter 9:44), Chapter 13:132 (waterfall in Chapter 12), Chapter 15:88 (Powers in Chapter 12:92), Chapter 15:62 (synaptic homeostasis in Chapter 5:126), and Chapter 15:86 (the habit account of addiction disputed in Chapter 9:150).

Total: 7 verified cross-reference errors (1 front matter Contents block, 4 in chapter bodies, 2 in companions).
