# Expert review: Chapter 15, A Coherent Model of the Human Brain: How the Pieces Fit

File: `docs/book/Word/Chapter15/How_the_Brain_Learns_Chapter_15_A_Coherent_Model_of_the_Human_Brain.md`

Reviewer role: computational neuroscience and machine learning. I reviewed the source, `make_figures.py` (the `SUPPORT`, `STEPS`, `CONN` and `LEDGER` tables), and all five figures. I checked every callback against the Chapter 0 to 14 files, and the new citations against abstracts (Findling et al. 2025; de Vivo et al. 2017) and the literature.

## Overall assessment

Technical accuracy score: **4.5 / 5**

The synthesis is strong. The eight statements are a fair and well-chosen summary of the book. They are argued as one design rather than a list, and the driving-on-the-left episode is a vivid and accurate way to show the parts working together. The new citations check out:
- **Jonas and Kording 2017:** the 6502, 3,510 transistors, three games, and both quotations.
- **Lazebnik 2002:** fifteen years earlier.
- **Gershman, Blei and Niv 2010:** the latent-cause account.
- **The Marder and Bargmann quotations.**
- **The International Brain Laboratory map:** 621,733 units, 75,708 good neurons, 279 areas, 139 mice, 12 labs.
- **Findling et al.:** "at least 20% to 30% of brain regions ... from early sensory areas ... to motor regions ... loops between areas" (abstract).
- **Crick 1979.**
- **FlyWire:** 139,255 neurons, 54.5 million synapses, 8,453 types.
- **MICrONS:** more than 200,000 cells, about half a billion synapses, about 75,000 neurons imaged.
- **H01:** about 57,000 cells, 150 million synapses, 1.4 PB, glia two to one, up to 50 synapses per connection.
- **Siletti et al.:** 3,313 subclusters.
- **Tang et al.:** 164 trillion synapses.
- **Gidon et al.; Beaulieu-Laroche et al.**
- **de Vivo et al.:** an axon–spine interface about 18% smaller after sleep (abstract).
- **Yang et al. 2014; Adamsky et al. against Agulhon et al.; Langille and Gallistel.**

The footnotes are complete and in order (24 of 24).

There is no Major error. The Minor items are:
- **Figure 15.5:** one placement overstates.
- **Callbacks:** three point to the wrong chapter.
- **Figure 15.2:** the matrix omits two chapter links that the chapter's own text makes.
- **Figure 15.4:** one caption is inaccurate.

## Major (factually wrong, must fix)

None.

## Minor

- **Figure 15.5 and line 110: "prediction and adaptation at every level" is filed as Settled.**
  - **What is wrong**: Adaptation at every level is as settled as anything in this book. Prediction "at every level" as a *mechanism* is not. Chapter 12 concluded that "the evidence for the strategy is strong" but treated predictive coding in cortex as having "a mixed record". That conclusion draws on Walsh et al. and on the Westerberg et al. preprint, which found little predictive suppression in early visual cortex. Filing it as Settled sits uneasily beside Chapter 12's own verdict.
  - **Fix**: Split the item. Keep "adaptation to the statistics of the input, at every level" in Settled. Move "prediction as a general strategy" to Probable, or keep it Settled but restate it as "prediction errors drive learning in many systems (reward, motor, perceptual)". In the text at line 110, change "and prediction and adaptation run through every level" to "and adaptation runs through every level, with prediction as its most general strategy".

- **Line 32: the thirst-neuron example comes from Chapter 12, not Chapter 1 or 7.** "Even the regulation looks ahead: thirst neurons in the mouse fall silent within seconds of drinking..." The statement cites "Chapters 1 and 7", but this example is Zimmerman et al. in Chapter 12 (line 36). Chapter 7 discusses the AgRP hunger neurons and, through Betley, thirst neurons as a teaching signal, but not their silencing by drinking. Add "(Chapter 12)" after the example. Figure 15.2 already links Chapter 12 to statement 1.

- **Line 40: the sea-slug example is in Chapter 1, not Chapter 5.** "The division appears even in a sea slug, whose reflex is strengthened for minutes by one shock and for days by five spaced shocks..." This is Kandel's *Aplysia*, described in Chapter 1 (line 54); Chapter 5 never mentions it. The statement cites "Chapters 5, 9, and 12". Add Chapter 1 to the parenthesis or after the example. Figure 15.2 already links Chapter 1 to statement 5.

- **Figure 15.2: the `SUPPORT` matrix omits two links the chapter itself makes.**
  - **Statement 7 ("built by rules, finished by experience").** The matrix has Chapters 0, 1, 10 and 13. It omits Chapter 6, which line 22 cites, together with Chapter 1, for Hubel and Wiesel's finding that early experience sets cortical wiring, and which covers critical periods and learned priors. Add 6 to statement 7, so that `SUPPORT[6] = [3, 7]`.
  - **Statement 3 ("it predicts").** The matrix has Chapters 3, 6, 9 and 12. Chapter 7 (predictive regulation and interoception) and Chapter 8 (confidence and accumulation as prediction) are central cases of prediction in the book, and Figure 12.1 itself lists them. Consider adding 7 and 8 to statement 3.

  The rest of the matrix agrees with the citations in the eight statements: every chapter each statement cites is filled, and no statement rests on one chapter, as the caption says.

- **Figure 15.4 caption: FlyWire covers the fly's brain, not its whole nervous system.** "...for the complete nervous systems of the nematode worm and the fruit fly..." FlyWire reconstructed the fly's brain without the ventral nerve cord, and the figure's own label correctly says "fruit fly brain". Change to "for the complete nervous system of the nematode worm and the complete brain of the fruit fly". Separately, the whole-human-brain synapse bar is the neocortical count; the legend says so, but the caption should too.

- **Line 84: Parkinson's motor symptoms are not its first effects.** "...and its first effects fall on the selection and vigor of movement." Non-motor symptoms (loss of smell, REM sleep behavior disorder, constipation) often precede the motor signs by years. Use "its defining effects fall on...".

- **Line 116: hedge the replication claim.** "The result has not yet been independently replicated." This is a strong negative claim. Use "has not, so far as we know, been independently replicated in human cortex".

- **Line 12: the Atari chip.** "The chip inside the Apple I, the Commodore 64, and the Atari video game console." The Atari 2600 used the 6507, a reduced-pin version of the 6502, and the Commodore 64 used the 6510. Jonas and Kording use the same loose phrasing, so this is acceptable. "Chips built around the same design" would be exact.

- **Line 66: the savings explanation goes beyond what Chapter 9 says.** "...why a skill relearned after a long break comes back faster than it was first acquired (Chapter 9)." Chapter 9 explains savings partly by a slow process and, after full washout, by remembering an aiming strategy. It does not attribute savings to latent causes. Use "...and it may help explain why a skill relearned after a long break comes back faster (Chapter 9)".

- **The eight statements: one omission.** Chapter 14's synthesis put "learns most from errors in its predictions, and from other people" at the core. Social learning (Kuhl, Roseberry, Lytle) does not appear among the eight. A clause in statement 3 or 6 would close the gap, for example in statement 6: "...and much of what it values and learns comes from other people (Chapter 14)".

## Copyedit

- **Line 92.** "Within five decades the impossible had been done" covers 1979 to 2024–25, which is 45 to 46 years. Fine, though "within half a century" reads more naturally.
- **Line 130.** "(statements one and six)" against "(statement four)": the numbering style is consistent. Fine.

## Figures

- **Figure 15.1 (model).** The diagram matches the eight statements and the caption.
- **Figure 15.2 (matrix).** See Minor. The `SUPPORT` dict is otherwise consistent with the text's chapter citations for each statement:

  | Statement | Chapters in the matrix | Chapters cited in the text |
  |---|---|---|
  | 1 | 1, 7, 12 | 1, 7 |
  | 2 | 0, 1, 2, 13 | 0, 2, 13 |
  | 3 | 3, 6, 9, 12 | 6, 12 |
  | 4 | 2, 3, 5, 10, 11 | 3, 5 |
  | 5 | 1, 5, 9, 10, 11, 12, 14 | 5, 9, 12 |
  | 6 | 3, 4, 7, 8, 9, 14 | 8, 9 |
  | 7 | 0, 1, 10, 13 | 0, 1, 13 |
  | 8 | 1, 3, 4, 13 | 13 |

- **Figure 15.3 (timescales).** The ranges are accurate and the chapter tags are right:
  - dopamine arriving within the eligibility trace at 0.3 to 2 seconds (Yagishita et al., in Chapter 3);
  - early potentiation and cerebellar recalibration over minutes to an hour;
  - protein synthesis over hours;
  - sleep;
  - the shift to habit over weeks;
  - the latent context kept over months to years.
- **Figure 15.4 (connectomes).** The values are correct. H01 shows 16,087 neurons, consistent with about 57,000 cells and glia two to one. MICrONS is shown as cells, as labeled. See Minor for the caption.
- **Figure 15.5 (settled, probable, open).** It is otherwise fair:
  - Engrams are Settled, with the rodent caveat; dopamine RPE, the fast and slow memory systems, energy constraints, and neuromodulators reconfiguring fixed wiring (Marder and Bargmann) are also Settled.
  - Three-factor rules in cortex, sleep consolidation through replay, the shift to habit, and the bodily anchoring of value are Probable. That is appropriately cautious.
  - Credit assignment, single-neuron computation, the sleep and synapses question, glia, molecular storage, and one principle are Open, and each is argued fairly in the text (lines 114 to 124).
  - The only issue is the "prediction" item noted above.

## Cross-references checked

These are accurate:
- Chapter 0: self-organization and the genome.
- Chapter 1: Hodgkin and Huxley; Hubel and Wiesel; McClelland; Helmholtz; Cannon; Ashby; degeneracy; Lennie; *Aplysia*.
- Chapter 2: Waldeyer.
- Chapter 3: Schultz; the third factor; Yagishita's 0.3–2 s window; Parkinson's.
- Chapter 4: place cells; hubs.
- Chapter 5: Bliss and Lømo; CLS; sleep replay; the synaptic homeostasis hypothesis mentioned.
- Chapter 6: Helmholtz; Hubel and Wiesel.
- Chapter 7: Cannon; extinction and renewal; hunger and value; stress and habit.
- Chapter 8: devaluation.
- Chapter 9: force-field adaptation (Shadmehr and Mussa-Ivaldi); chunking; the shift to habit; the addiction dispute.
- Chapter 10: credit assignment.
- Chapter 12: Craik; Powers; free energy.
- Chapter 13: Prinz et al.; mixtures of experts; the genome bottleneck; hubs.
- Chapter 14: taxi drivers; the attention budget.

These need fixing:
- the thirst neurons (line 32, actually Chapter 12);
- the sea slug (line 40, actually Chapter 1);
- the savings attribution (line 66, softer than written).

## What would make it a 5

1. Split "prediction and adaptation at every level" in Figure 15.5 and at line 110.
2. Fix the two misattributed callbacks (lines 32 and 40) and soften line 66.
3. Add Chapter 6 to statement 7, and consider Chapters 7 and 8 for statement 3, in the `SUPPORT` matrix.
4. Correct the Figure 15.4 caption (the fly's brain; the neocortical synapse count).
5. Use "defining" rather than "first" effects for Parkinson's (line 84).
