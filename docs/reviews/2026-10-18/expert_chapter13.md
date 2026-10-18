# Expert review: Chapter 13, Why the Brain Works the Way It Does: Constraints, Trade-offs, and the Shape of a Solution

File: `docs/book/Word/Chapter13/How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md`

Reviewer role: computational neuroscience and machine learning (neural energetics, information theory, comparative and evolutionary neuroscience, network science, NeuroAI). I reviewed the source, `make_figures.py`, and all seven figures, and I re-ran the five computed figures. I checked quantitative claims against primary sources where full text was available: Europe PMC full text for Niven, Harris, Kaiser, Shuvaev and Zador, and PubMed abstracts for Moran, Wang, Kuzawa, Olkowicz, Cornélio, Cordey, Levy and Baxter (2002) and Hartline. I checked callbacks against the Chapter 0 to 12 files.

## Overall assessment

Technical accuracy score: **4.5 / 5**

This is a strong closing chapter for the explanatory arc. Tinbergen's four questions frame it, and the argument (hard constraints, Pareto trade-offs, history, and convergence as the test that separates them) is sound and carefully hedged. The quantitative backbone is right, and I could verify most of it to the decimal:

| Source | What I checked |
|---|---|
| Moran et al. | 15% of resting metabolism at 1 g, 5% at 8.5 g |
| Niven et al., full text | Calliphora 955 ± 70 bits/s; *D. melanogaster* 197 ± 31; "five times more information", "ten times more energy to code the same quantity" |
| Harris et al., full text | 4-fold more information possible with a stronger synapse; the physiological strength maximizes bits per ATP |
| Wang et al. 2008 | 14 species; fastest fibers 1–5 ms across neocortex; average 7 ± 2 Hz |
| Kaiser and Hilgetag, full text | 48% and 32% |
| Kuzawa et al. | 66% of resting metabolic rate; 43% of daily energy requirements |
| Shuvaev et al., full text | 322-fold compression and 94% initial accuracy; BeamRider 492-fold |
| Zador, full text | "about 1 GB ... an hour or so of streaming video"; "at least six orders of magnitude" |
| Cordey et al. | the energetic threshold rests on 12 women; it was exceeded in a third of studies |
| Others, from the literature | Hodgkin and Huxley (476 µm, 21.2 m/s); Hursh (6 m/s per µm); Zhang and Sejnowski (4/3 and 1.23); Cherniak (11! arrangements); Olkowicz (raven 1.2 billion and macaw 1.9 billion pallial neurons); DeepSeek-V3 (671B parameters, 37B active) |

All five computed figures reproduce the numbers in the text.

The contested claims are treated fairly on the whole: the cavefish, cooking, expensive tissue, the obstetric dilemma against EGG, Ringo, bird convergence, and the Levy–Baxter optimum. The exception is the inverted retina, where the chapter takes the "bad design" side of a live debate as settled.

There are no Major errors. The Minor items are:
- one density figure that should follow the source's own summary;
- two callbacks to things earlier chapters do not contain;
- a slight internal inconsistency in the genome arithmetic;
- three AI-section wordings that would be more exact with a clause each;
- a few numbers I could not confirm from the sources available to me, which should be checked before press.

## Major (factually wrong, must fix)

None.

## Minor (accuracy, fairness, callbacks)

- **Line 104: the inverted retina is presented as settled bad design.** "The compensation does not make the inversion a good design. It shows what a tinkerer does with a design it cannot discard."
  - **What is wrong**: The history-over-constraint reading is the standard one, and the octopus contrast is apt. But the chapter's own test for separating history from constraint invites the reply, made in recent work, that inversion has functional benefits. It puts photoreceptors in direct contact with the pigment epithelium and choroid, which regenerate photopigment, supply the highest metabolic demand in the body, and remove heat. Some authors therefore argue it is not a defect at all. A specialist will expect one sentence of the other side, especially in a chapter that is otherwise scrupulous about contested claims.
  - **Fix**: "...onto the cones. Some researchers argue that the arrangement is not a defect at all, since it puts the photoreceptors, the most energy-hungry cells in the body, against the tissue that feeds them and renews their pigment. Even so, the blind spot and the light-scattering layers are costs that the octopus does not pay, and the compensation shows what a tinkerer does with a design it cannot discard."
  - **Cite**: Baden, T., & Nilsson, D.-E. (2022). Is our retina really upside down? *Current Biology*, 32(7), R300–R303. https://doi.org/10.1016/j.cub.2022.02.065 (from memory, not re-verified this round).

- **Line 100: use the source's own density summary.** "...parrots and songbirds pack their forebrain neurons three to four times more densely than primates."
  - **What is wrong**: The Olkowicz et al. abstract says the brains of parrots and songbirds "contain on average twice as many neurons as primate brains of the same mass", with corvids and parrots putting a larger fraction of them in the pallium. Some pallial density ratios in the paper's tables may reach three to four times. As written, though, the claim is stronger than the paper's own summary.
  - **Fix**: "...found that parrot and songbird brains hold on average twice as many neurons as primate brains of the same mass, and put a larger share of them in the forebrain." The raven and macaw figures that follow are correct.

- **Line 78: the ion-channel callback points to a passage that does not exist.** "...and Chapter 5 described how many different mixtures of ion channels can give a neuron the same pattern of firing."
  - **What is wrong**: Chapter 5 mentions only that channel densities change with activity (line 26). No chapter describes the many-mixtures result. Chapter 1's degeneracy passage (line 84) is general.
  - **Fix**: Introduce it here: "...and the clearest case is in single neurons and small circuits: Astrid Prinz, Dirk Bucher, and Eve Marder found that very different combinations of ion channels and synapses produce nearly the same rhythm in a model of a crustacean circuit."
  - **Cite**: Prinz, A. A., Bucher, D., & Marder, E. (2004). Similar network activity from disparate circuit parameters. *Nature Neuroscience*, 7(12), 1345–1352. https://doi.org/10.1038/nn1352 (from memory, not re-verified this round).

- **Line 126: the dopamine-vigor callback is uncited in the book.** "...dopamine sets how vigorously the animal acts and how much effort it will spend."
  - **What is wrong**: Chapter 8 lists Niv et al. (2007) on vigor in its references, but no chapter's body describes vigor. Either cite Niv directly here (footnote: Niv, Daw, Joel, and Dayan 2007, *Psychopharmacology*, 191(3), 507–520, already in Chapter 8's reference list), or attach the clause to a chapter that discusses it.

- **Line 34: the squid sodium figure is not in Chapter 1.** "The textbook squid axon of Chapter 1 lets in about four times as much sodium as the minimum..."
  - **What is wrong**: Chapter 1 (line 40) describes the squid axon and Hodgkin and Huxley, but not the fourfold sodium figure.
  - **Fix**: "The squid axon of Chapter 1, it turns out, lets in about four times..." Add a source for the fourfold figure; Alle et al. (2009) review it in their introduction.

- **Line 108 and Figure 13.6: the genome arithmetic is slightly inconsistent.** The text quotes Zador's "at least six orders of magnitude", while the figure's own computation, with the same assumptions, gives a factor of about 600,000 (5.8 orders). Both are fine as round numbers, but side by side they read as a contradiction.
  - **Fix**: Add after the quotation: "(on the round numbers used here, a factor of more than half a million)".
  - **Also**: Line 108 uses Zador's 100 billion neurons, while line 84 uses 86 billion. Add "in round numbers".

- **Line 28: the source of the 10 to 20 Hz optimum needs checking.** "Their later estimates put the most efficient rate at about 10 to 20 spikes a second for a cortical neuron, against about 200 for the rate that would maximize information alone."
  - **What is wrong**: Footnote 6 cites Levy and Baxter (2002). Its abstract concerns the optimal *failure rate* given an average firing rate, not the optimal firing rate itself. Confirm that the 10 to 20 Hz figure is stated in that paper; it may instead come from Levy and Baxter (1996) with their cost ratios. The "about 200" assumes a bin of about 2.5 ms; say so, or write "hundreds".

- **Line 32: two Harris et al. details I could not confirm.**
  - "Only about one retinal spike in five triggered a spike in the relay cell": I could not confirm this figure in the full text.
  - "The synapse's natural strength instead maximized the information transmitted for each molecule of ATP": the paper reports that the maximum was at the physiological conductance in six of ten cells and within 0.5 to 3 times it in three more. "In most cells" would be exact.

- **Lines 85 and 49: further figures to confirm.**
  - "Five or six hours a day of raw food would be enough" (Cornélio et al.): the abstract says only that foraging efficiency matters more than body mass. Confirm the hours in the paper.
  - "By several hundredfold on their estimate" (Hartline and Colman): the abstract gives no figure. Confirm it.
  - "Around the age of four" (Kuzawa et al.): the paper's peak glucose-to-resting-metabolic-rate ratio falls at about age five, and the ratio to daily energy requirements at about age four. "Around the age of four or five" covers both.

- **Line 142: "a convergence, not a borrowing" is too strong for mixtures of experts.** The earliest mixture-of-experts work was partly motivated by the brain's modular "what" and "where" streams (Jacobs, Jordan and Barto, 1991). Today's sparse MoE is motivated by compute, not energy as such. Use: "It is largely a convergence: the modern versions were built to save computation, not to imitate the brain, and like the convergences of Chapter 11 they suggest that the constraint is doing the work."

- **Line 144: the spike argument is itself a convergence.** "Spikes solve the problem of sending a signal over a long, noisy fiber, and a digital chip already transmits signals without loss." The chip does so by restoring its signal to discrete levels at every gate, which is Sarpeshkar's point at line 40: the same answer to the same constraint. A clause would turn this into a second convergence example: "...already restores its signals to clean digital levels at every step, the same answer the axon found."

- **Line 146: "no counterpart" is slightly overstated.** "The genome bottleneck has no counterpart in machine learning." Hypernetworks and other weight-generating networks do compress weights through a small generator; Shuvaev et al. build on that idea. Use "has no counterpart in how large models are trained".

- **Line 148: the callback should name both chapters.** "The systems of Chapter 11 that decide how long to think" should be "Chapters 10 and 11". Reasoning models that allot computation were discussed in Chapter 10 (lines 128 and 144), and adaptive computation time in Chapter 11.

## Copyedit

- **Lines 12 and 14.** "Cave fish" (line 12) against "cavefish" (line 14): pick one. "Cavefish" is standard.
- **Line 108.** "3.7 × 10^15" will typeset with a literal caret. Use a superscript (10<sup>15</sup>) or the house convention.
- **Line 14.** "The previous twelve": the book has Chapters 0 to 12, so the previous chapters number thirteen. Use "the earlier chapters".
- **Line 48.** "Imagine yourself with a 100-fold thicker spinal cord!" is a quotation ending in an exclamation mark inside running text. Confirm the wording against Hartline and Colman.

## Figures

All computed figures were re-run:

| Figure | Re-run result | Matches |
|---|---|---|
| 13.2 | optimal spike probability 0.033, 0.155 and 0.382 for rest costs of 1%, 10% and 100% of a spike | the caption's claim that cheaper rest gives a lower peak |
| 13.3 | 3.53 µm; cross-section ratio about 18,150 | text's "about 3.5 µm" and "about 18,000" |
| 13.4 | path 9.07 at local wiring; wire 1.26 and path 5.99 at 5%; 1.52 and 4.92 at 10%; 5.82 and 3.69 at 100% | lines 64 to 66 exactly |
| 13.5 | 706 non-dominated designs filling the triangle | the caption |
| 13.6 | worm genome about 3,470 times its wiring list; human wiring list about 589,000 times the genome | the caption's "thousands" and "about 600,000" |

- **Figure 13.4**: The caption says "the red line marks the best available trade-offs: no network does better on both counts", which is a correct description of the non-dominated set.
- **Figure 13.1**: The chapter numbers are mostly right. "Sensitive periods" under the genome constraint points to Chapter 1, which is correct (Wiesel and Hubel, Chapter 1, line 62).
- **Figure 13.7**: The rows and chapter numbers are accurate.

## Cross-references checked

These are accurate:
- Chapter 0: self-organization (line 94).
- Chapter 1: the 20 W budget, Lennie, Allen and Stevens, Jacob's tinkerer, degeneracy, sensitive periods.
- Chapter 2: passive decay; myelin; Faisal et al.'s axon floor (line 126).
- Chapter 4: small-world networks; hubs and the 26 disorders (line 150); central pattern generators.
- Chapter 6: the blind spot.
- Chapter 7: stress shifting control toward habit (Arnsten, Figure 7.6).
- Chapters 8 and 9: speed against accuracy, exploration, habit.
- Chapter 10: Zador.
- Chapter 11: Horowitz (0.9 and 3.7 pJ, 1.3 to 2.6 nJ, consistent with Chapter 11) and convergences.
- Chapter 12: adaptation, the waterfall illusion, norepinephrine and the learning rate.

These are inaccurate:
- Chapter 5 on ion-channel mixtures (line 78).
- Chapter 1 on the fourfold sodium figure (line 34).
- Dopamine vigor (line 126), which appears in no chapter body.

## Fairness of the contested claims

| Topic | Line | Assessment |
|---|---|---|
| Cavefish | 12 | Hedged appropriately. |
| Cooking | 85 | Both sides given (Fonseca-Azevedo and Herculano-Houzel against Cornélio). |
| Expensive tissue | 88 | Aiello and Wheeler, then Navarrete's null result, then Pontzer's "raise the budget" account. Fair and current. |
| Obstetric dilemma against EGG | 90 | Both sides, with Cordey et al.'s critique of the energetic ceiling. Fair. "Many pregnant women exceed it" could be stated precisely: the threshold was exceeded in a third of the 12 studies. |
| Ringo | 54 | Labeled a conjecture. Fair. |
| Bird pallium | 100 | Convergence is supported by the 2025 developmental studies. Fair; fix only the density figure. |
| Levy and Baxter | 28 to 32 | Fair; confirm the source of the 10 to 20 Hz figure. |
| Müller cells and the inverted retina | 104 | The one place where the chapter takes a side on a live question without acknowledging the other (see Minor). |

## What would make it a 5

1. Add one sentence on the functional case for the inverted retina (line 104).
2. Align the bird-density claim with Olkowicz et al.'s summary (line 100).
3. Fix the three inaccurate callbacks (lines 34, 78 and 126).
4. Reconcile the genome numbers (line 108 and Figure 13.6).
5. Confirm the handful of figures not verifiable from the sources available to me: Levy and Baxter's 10 to 20 Hz, Harris et al.'s one in five, Cornélio's hours, and Hartline and Colman's "several hundredfold".
6. Add the three one-clause refinements to the AI section (lines 142 to 146).
