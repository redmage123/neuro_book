# Cross-chapter consistency audit: recurring numbers and facts

Scope: docs/book/Word/Chapter0..16/*.md and docs/companion/Chapter1..16/Word/*.md (read-only).
Line numbers are physical line numbers in the .md file (footnotes included).
Abbreviations: B4 = docs/book/Word/Chapter4/How_the_Brain_Learns_Chapter_4_Circuits.md, C16 = docs/companion/Chapter16/Word/How_the_Brain_Learns_Chapter_16_Student_Notes_and_Labs.md, etc.

Severity: HIGH = a reader will see two different numbers for the same thing, or a number contradicts the cited source; MED = numbers are each defensible but read as contradictory; LOW = citation/name formatting.

Total findings: 11 (2 HIGH, 4 MED, 5 LOW groups).

---

## 1. NIMCP spiking-network size: 2.0 million (chapter) vs 2.2 million (companion + figure)  [HIGH]

Canonical value: about 2.0 million neurons (1.8 million hierarchical SNN + about 200,000 language/sensorimotor), as B16:28 says.
Evidence: NIMCP source, include/core/brain/nimcp_brain.h:2003 `#define NIMCP_DEFAULT_SNN_NEURONS 1800000 /**< 1.8M hierarchical SNN (+200K language/sensorymotor on top) */`; scripts/brain_daemon.py:93 `DEFAULT_SNN_NEURONS = 1_800_000`; docs/architecture/20_snn.md:33. Nothing in the source gives 2.2 million. With 1.5 billion synapses, synapses per neuron = 750, not 682.

| location | current text | problem | proposed replacement |
|---|---|---|---|
| C16:116 | `NIMCP's spiking network: 2.2 million neurons, about 682 synapses per neuron.` | contradicts B16:28 (roughly 2 million) | `NIMCP's spiking network: about 2 million neurons, about 750 synapses per neuron.` |
| C16:118 (Lab 16.2 step 1 check) | `(Check: about 3.9 × 10^10^ and 1.25 × 10^12^.)` | unchanged (total synapses × rate does not depend on N) | no change needed |
| C16:150 | `NIMCP: 2.2 million neurons, 1.5 billion synapses.` | same | `NIMCP: about 2 million neurons, 1.5 billion synapses.` |
| C16:154 | `(Check: about 682, 391, and 10,061.)` | follows from 2.2 M | `(Check: about 750, 391, and 10,061.)` |
| C16:156 | `(Check: about 2.2 × 10^10^ synapses; about 265 GB.)` | follows from 2.2 M | `(Check: about 2.0 × 10^10^ synapses; about 241 GB.)` (2.0e6 × 10,061 = 2.01e10; × 12 bytes = 2.41e11 bytes) |
| docs/book/Word/Chapter16/make_figures.py:140 (drives Figure 16.5) | `("NIMCP\nspiking\nnetwork", 2.2e6, 1.5e9)` | figure plots 2.2 M against text's 2 M | `("NIMCP\nspiking\nnetwork", 2.0e6, 1.5e9)` then regenerate fig_scale.png |

Optional related nit, C16:121: `bring 834 down to about 28 spikes a second, a factor of 30? (Check: about 168 steps.)` The chapter's early rate is 26 (B16:42, B16:76, C16:116). For consistency: `bring 834 down to the early rate of 26 spikes a second, a factor of about 32? (Check: about 172 steps.)` (ln(834/26)/ln(1/0.98) = 171.6).

---

## 2. Neocortical synapse count: 150 trillion (Ch4) vs 164 trillion (Ch13, Ch15, Ch16, companions, figures)  [HIGH]

Both numbers are real but from different papers from the same Danish stereology group: Pakkenberg et al. (2003, Exp. Gerontol. 38:95) give 0.15 × 10^15 for young adults; Tang et al. (2001, Synapse 41:258) give 164 × 10^12. The book uses 164 trillion in B13:118, B15:98, B15 Fig 15.4 (make_figures.py:109, 119), B16 Fig 16.5 (make_figures.py:141), C15:123, C16:150, and Ch16's lab checks depend on it (10,061 per neuron). Ch4 is the only outlier. Canonical: 164 trillion (Tang et al. 2001), since it carries the most downstream arithmetic.

| location | current text | problem | proposed replacement |
|---|---|---|---|
| B4:16 | `The human brain contains on the order of 86 billion neurons and, in the neocortex alone, roughly 150 trillion synapses.[^1]` | different figure for the same quantity than Ch13/15/16 | `The human brain contains about 86 billion neurons and, in the neocortex alone, about 164 trillion synapses.[^1]` |
| B4:382 (footnote [^1], tail) | `Azevedo and colleagues count the neurons; Pakkenberg and colleagues estimate about 150 trillion synapses in the neocortex of young adults.` | must match | append Tang to the footnote's citation list: `...; Tang, Y., Nyengaard, J. R., De Groot, D. M. G., & Gundersen, H. J. G. (2001). Total regional and global number of synapses in the human brain neocortex. *Synapse*, 41(3), 258–273.` and change the tail to `Azevedo and colleagues count the neurons; Tang and colleagues count about 164 trillion synapses in the neocortex, and Pakkenberg and colleagues give a similar figure of about 150 trillion for young adults.` (also add the Tang entry to Ch4's reference list) |

Related, MED: whole-brain figure "on the order of a hundred trillion" (B1:28, C1:33) sits below the neocortex-only 164 trillion given later. "On the order of" technically covers it, and B13:118 explicitly calls Zador's 100 trillion a round number, but a reader comparing Ch1 with Ch4/Ch13 sees the part exceed the whole.

| location | current text | proposed replacement |
|---|---|---|
| B1:28 | `and the neurons are joined by on the order of a hundred trillion synapses, the junctions` | `and the neurons are joined by well over a hundred trillion synapses, the junctions` |
| C1:33 | `about 86 billion neurons and on the order of a hundred trillion synapses;` | `about 86 billion neurons and well over a hundred trillion synapses;` |

---

## 3. Fraction of cortical neurons the energy budget allows to be active: "one in a hundred" (Ch1, Ch15, C1, C16) vs "no more than about fifteen percent" (Ch2)  [MED]

Both are correctly sourced: Attwell and Laughlin (2001, J Cereb Blood Flow Metab 21:1133) conclude that the budget favors codes with at most about 15 percent of neurons simultaneously active (abstract, confirmed via PubMed 11598490); Lennie (2003, Curr Biol 13:493) gives about 1 percent. But B2:126 states the 15 percent as the cortex's limit without mentioning the stricter figure that Ch1, Ch15 (B15:34), Ch16 (B16:84) and C16:122 treat as the book's number, so the reader sees two different "what the cortex can afford" figures.

| location | current text | proposed replacement |
|---|---|---|
| B2:126 | `their budget predicts that a cortex paying these costs can afford to have no more than about fifteen percent of its neurons active at the same time.[^43]` | `their budget predicts that a cortex paying these costs can afford to have no more than about fifteen percent of its neurons active at the same time, and Peter Lennie's later calculation, described in Chapter 1, puts the affordable fraction nearer one in a hundred.[^43]` (add Lennie, P. (2003). The cost of cortical computation. *Current Biology*, 13(6), 493–497 to footnote [^43] and Ch2's reference list) |

---

## 4. Brain power: 20 watts (Ch1, Ch10, Ch13 opening, C1, C10) vs 500 kilocalories a day (Ch13, C13)  [MED]

B13:24 says "Chapter 1 gave the brain's budget, about 20 watts", and B13:88 then says the brain's neurons cost about 500 kcal a day (C13:240 check: 516 kcal). 516 kcal/day = 2.16 MJ / 86,400 s = 25 W; 20 W = 413 kcal/day. Both are sourced (20 W from Sterling and Laughlin 2015 / Mink et al. 1981 at about 20 percent of ~100 W; 516 kcal/day from Herculano-Houzel 2012 PNAS 109 suppl. 1:10661), but a reader who converts will find a 25 percent mismatch within one chapter.

| location | current text | proposed replacement |
|---|---|---|
| B13:88 | `so that the human brain's 86 billion neurons cost about 500 kilocalories a day.[^33]` | `so that the human brain's 86 billion neurons cost about 500 kilocalories a day, or about 25 watts, a little above the round 20 watts of Chapter 1, which comes from a different method of estimation.[^33]` |

(Optionally add a one-line "Why is 516 kcal more than 20 W?" note after C13:240.)

---

## 5. "How much slower is the brain": about a million times (Ch1, C1) vs ten million times (Ch2, C2)  [MED]

B1:30 and C1:33: transistors "switch in picoseconds" and "the brain is about a million times slower" (comparison against a processor clock cycle of several GHz, ~0.3 ns, gives about 3 million). B2:126, B2:128 (Fig 2.9 caption) and C2:113: a 1 ms spike versus a 100 ps transistor switch, "ten million times". Different comparisons, but both are framed as "transistor switches in picoseconds", so they read as contradictory.

| location | current text | proposed replacement |
|---|---|---|
| B1:30 | `Measured step for step, the brain is about a million times slower than a laptop.` | `Measured step for step against a processor's clock, the brain is about a million times slower than a laptop.` |
| C1:33 | `The brain is roughly a million times slower per step,` | `Against a processor's clock, the brain is roughly a million times slower per step,` |

(Ch2's "ten million times faster" is correct for a single 100 ps transistor switch and can stay.)

---

## 6. H.M.: extent of hippocampal removal (note, single-chapter but fact-checkable)  [MED]

B5:156: `after most of both hippocampi and the medial temporal cortex around them were removed`. Corkin et al. (1997, J Neurosci 17:3964), which Ch5 itself cites (B5:236), found by MRI that roughly the posterior half of the hippocampal body was spared bilaterally (the resection removed about the anterior 5 cm of medial temporal lobe, and the remaining hippocampal tissue was atrophic).
Proposed: `after the front part of both hippocampi and the medial temporal cortex around them were removed` (or `after much of both hippocampi ...`).
Also spelling: C5:99 `Patient H. M.` vs `H.M.` everywhere else (B5, B9, C5:72, C5:74, C9:34). Replace with `Patient H.M.`

---

## 7. Name spelling: Kording vs Körding in running text  [LOW]

Same person (Konrad Paul Kording). References correctly follow each paper's byline (Körding 2007 in B12:244; Kording 2017/2019 in B15, B10, B9). Running text differs: B12:106 `Konrad Körding` vs B15:12 `Konrad Kording`, B15:144 `Kording's`; companion C12:61 `(Körding 2007)` vs C15:21 `(Jonas and Kording 2017)`.
Proposed: standardize running text on his current spelling: B12:106 `Konrad Körding, Joshua Tenenbaum` -> `Konrad Kording, Joshua Tenenbaum`; C12:61 `(Körding 2007)` -> `(Kording 2007)`; keep reference-list bylines as published. (Alternatively standardize on Körding in all running text; just pick one.)

---

## 8. Same reference, different journal title form  [LOW]

| work | variant A (keep) | variant B (change) |
|---|---|---|
| Hodgkin & Huxley (1952), J Physiol 117(4), 500–544 | `*Journal of Physiology*` in B0:176, B0:286, B1:164, B1:244, B2:224, B2:350 | B13:232 and B13:340 `*The Journal of Physiology*` -> `*Journal of Physiology*` |
| Hubel & Wiesel (1962), J Physiol 160(1), 106–154 | `*Journal of Physiology*` in B4:278, B4:422, B6:260, B6:392 | B10:254 and B10:404 `*The Journal of Physiology*` -> `*Journal of Physiology*` |

## 9. Same reference, missing issue number  [LOW]

Thorpe, Fize & Marlot (1996): B1:204, B1:236, B2:284, B2:362 give `*Nature*, 381(6582), 520–522.`; B6:344 and B6:396 give `*Nature*, 381, 520–522`. Replace in B6 with `*Nature*, 381(6582), 520–522`.

## 10. Same reference, different title punctuation  [LOW]

Martin, Keating, Goodkin, Bastian & Thach (1996), *Brain* 119(4), 1183–1198. Published title: "Throwing while looking through prisms. I. Focal olivocerebellar lesions impair adaptation." B6:294 matches; B9:308 (and its footnote copy) has `Throwing while looking through prisms: I. Focal` -> `Throwing while looking through prisms. I. Focal`.

## 11. Same reference, different conference/author-list style  [LOW]

| work | locations | variants | proposed |
|---|---|---|---|
| Miconi et al. (2019) Backpropamine | B3:264, B3:400 vs B11:286, B11:422 | `*International Conference on Learning Representations (ICLR)*.` vs `In *International Conference on Learning Representations*.` | use `In *International Conference on Learning Representations*.` in B3 |
| Schaul et al. (2016) Prioritized experience replay | B7:386, B7:634 vs B11:310, B11:390 | `*International Conference on Learning Representations*. arXiv:1511.05952.` vs `In *International Conference on Learning Representations*.` | use B7 form in B11 (keeps the arXiv locator), or vice versa |
| Gal & Ghahramani (2016) | B8:250, B8:604 vs B11:218, B11:472 | `*Proceedings of the 33rd International Conference on Machine Learning*, PMLR 48, 1050–1059.` vs `In *Proceedings of the 33rd International Conference on Machine Learning* (pp. 1050–1059). PMLR.` | use the B8 form (has volume 48) in B11 |
| Kadavath et al. (2022) | B8:296, B8:602 vs B10:258, B10:540 | `Perez, E., … Kaplan, J. (2022)` vs `Perez, E., Schiefer, N., Hatfield-Dodds, Z., DasSarma, N., Tran-Johnson, E., et al. (2022)` | use B8 form (APA 7 style, first 19 … last) in B10 |
| Hebb (1949) | B0:170, B0:302 vs B2, B5, B10 | `New York: Wiley` vs `Wiley` | B0 uses place-of-publication style for all its older books (Carnot, Galvani, Helmholtz), so this is chapter-internal style; harmonize only if the book wants one style throughout |

---

## Checked and consistent (no action)

- Neurons in the brain: 86 billion everywhere (B0:86, B1:28, B4:16, B4:110, B13:88, B13:116, B15:98, C1:33, C13:234), Azevedo et al. 2009 (86.1 billion; 84.6 billion non-neuronal). Glia/non-neuronal "similar"/"roughly equal" (B0, B1); "glia outnumbered neurons two to one" (B15:98, B15:128) refers explicitly to the H01 sample, which is correct (16,087 neurons, ~32,000 glia).
- Cerebral cortex: about 16 billion (B3:42, B3:324, C3:51, C3:121), 16.3 billion neocortex (C15:123, C16:150), 19 percent of neurons (B1:230). Cerebellum about 69 billion (B4:110, B4:434). Consistent.
- Brain 2 percent of body mass, 20 percent of resting energy, 20 W: B0:62, B1:46, B2:126, B2:128, C1:45, C2:113, B10, C10. Consistent. 3.5 MWh over 20 years at 20 W is arithmetically correct.
- Attwell and Laughlin budget 47/34/13 percent: B1:46 and C1:45 agree (note: later work, e.g. Harris and Attwell 2012/Engl et al., revised the action-potential share down; not a consistency issue).
- Conduction speeds: fastest myelinated about 100 m/s, thin unmyelinated about 1 m/s (B1:30, B2:102, C2:89); squid axon 476 µm, 21.2 m/s measured, 18.8 computed (B1:40, B1:244, B13:46, B13:52, C1:43, C13); Hursh 6 m/s per µm. Consistent. Squid axon "up to a millimeter" (B0:78) vs "about half a millimeter" (B1:40) is compatible.
- Membrane: rest −70 mV, threshold about 15 mV above (−55), peak +40 mV, cleft 20 nm, membrane 5 nm: consistent across B0, B2, B3, C2, C3, B16.
- Inputs per neuron: CA1 ~30,000 + 1,700; Purkinje ~200,000 (B2:34, B4:110, C1:103, C2:25); cortical ~10,000 (B16:28, C16 lab 10,061). Consistent.
- Dates and people: Hodgkin and Huxley 1939 first intracellular recording, 1952 model, Nobel 1963 with Eccles (B0, B1, B2, B13, B15, C1); Bliss and Lømo 1973, anesthetized rabbit (B2:116, B5:54, B15:22, C2:109, C5:43); Hebb 1949; Wiesel and Hubel 1963 deprivation, Hubel and Wiesel 1962 receptive fields, "1960s" (B1:62, B6:136, B15:22, C1:65); Schultz from the 1980s, 1998 review; Montague, Dayan, Sejnowski 1996 and Schultz, Dayan, Montague 1997 (B3:58, C3:63, C8:52); Sutton TD 1988; Loewi 1921 (B2:42, C2:39); Katz and Miledi 1965; Fatt and Katz 1952; Adrian and Zotterman 1926; Sherrington 1897 "synapse", 1906 "interoceptive"; Thorndike 1911; Helmholtz 1867; Craik 1943 (died 1945 aged 31); McCulloch and Pitts 1943; Rumelhart, Hinton, Williams 1986; Fukushima 1980; McCloskey and Cohen 1989; Hopfield 1982, Nobel 2024; Ebbinghaus 1885; Lashley 1951; Scoville and Milner 1957; H.M. retrograde gap about eleven years (B5:114, C5:72). All consistent.
- Thorpe 1996 / 150 ms (B1:30, B6:54, C1:33); saccades three (or three to four) per second (B6, B12, C6, C12). Consistent.
- Connectomes: worm 302 neurons / ~7,000 synapses; FlyWire 139,255 / 54.5 million; H01 ~57,000 cells, 16,087 neurons, ~150 million synapses, 1.4 PB; MICrONS >200,000 cells, ~0.5 billion synapses: consistent across B13, B15, C13, C15, C16 and both figure scripts.
- MOS 6502, 3,510 transistors (Jonas and Kording 2017): appears only in B15:12 and C15:21; matches the paper. Minor accuracy nit, not a consistency issue: the Commodore 64 used the 6510 and the Atari 2600 the 6507, both 6502 variants; B15:12 could read `the MOS 6502, the chip inside the Apple I, near-identical versions of which ran the Commodore 64 and the Atari video game console,`.
- Reference lists: across all 17 chapter files, no work is cited with different years or different author sets; only the formatting variants in sections 8 to 11 differ.

Sources consulted beyond the book: NIMCP source tree (/home/bbrelin/nimcp, files named above); Attwell and Laughlin 2001 abstract (https://pubmed.ncbi.nlm.nih.gov/11598490/); Tang et al. 2001 and Pakkenberg et al. 2003 as cited in the book's own footnotes; Herculano-Houzel 2012 (cited B13:376).
