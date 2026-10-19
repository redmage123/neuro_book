# Applied changes: Chapter 0 (no companion)

File: docs/book/Word/Chapter0/How_the_Brain_Learns_Chapter_0_Foundations.md

## Changes
1. Line 78: deleted "Their model explained in quantitative detail how the opening and closing of sodium and potassium channels generate the electrical impulse." Cross-chapter repetition of Hodgkin and Huxley (audit_repetition.md A2, Chapter 0; aud/cuts.py OTHER (0,78)). The next sentence (Figure 0.7) shows the same thing, and Ch1:40 and Ch2:96 tell it in full. No footnote marker in the cut sentence; [^31] stays on the paragraph's last sentence.
2. Footnotes: check_footnotes.py reports no problems (43 footnotes, 43 definitions, 49 references); ran --write (no renumbering needed beyond a re-sort).

## Skipped / no action
- audit_numbers.md 11 (Hebb 1949 "New York: Wiley" vs "Wiley"): the report calls it chapter-internal style (Chapter 0 uses place of publication for all its older books); harmonize only if the book wants one style throughout. Left as is.
- audit_repetition.md A3 item 7 ("Further trimming of Ch0 is possible if Figure 0.7 stays"): not proposed as a specific cut; the remaining Ch0 telling is short and carries the Figure 0.7 explanation.
- audit_terms.md B5 (two meanings of "free energy"): the fix belongs in Ch12; Chapter 0's thermodynamic definition is the canonical one and needs no change.
- House style scan: no em dashes in prose (only the "> ---" epigraph attribution, house format), no British spellings, no bare numerals one to ten in prose. Nothing to fix.
- No within-chapter redundancy worth cutting found (the twenty-nanometer gap appears at lines 50 and 92 in different contexts: diffusion time and synaptic addressing).

## Build
python3 docs/build.py Chapter0/ succeeded (docx and pdf).

## Word count (body above "# References and Attribution", excluding image lines)
Before: 3398. After: 3378 (-20).
# Applied changes: Chapter 1 and its companion

Files: docs/book/Word/Chapter1/How_the_Brain_Learns_Chapter_1_What_the_Brain_Is.md; docs/companion/Chapter1/Word/How_the_Brain_Learns_Chapter_1_Student_Notes_and_Labs.md; scratchpad key_ch1.md

## Chapter changes
1. Line 86: replaced the 70-word "Nor is it true that the brain optimizes nothing ... that Chapter 6 also describes." with "Nor does the brain optimize nothing: it has no single global objective, but Chapters 3 and 6 show many of its circuits minimizing a local error or cost." Cross-chapter repetition (audit_repetition.md A2 Chapter 1; aud/cuts.py OTHER (1,86); home Ch3:84). Lightly reworded from the proposed text ("Chapters 3 and 6 show circuits that minimize a local error or cost, though no single global objective") for smoother syntax. This also removes the repeated "large population of dopamine neurons" formula (A3 item 2) and makes audit_terms.md C7 (gloss "gradient descent" at ch1:86) moot, since the phrase is gone. No footnote in the cut text.
2. Line 28: "on the order of a hundred trillion synapses" -> "well over a hundred trillion synapses" (audit_numbers.md 2 MED; audit_terms.md related item): the whole-brain figure no longer sits below the neocortex-only 164 trillion of later chapters.
3. Line 30: "Measured step for step, the brain is about a million times slower" -> "Measured step for step against a processor's clock, ..." (audit_numbers.md 5): separates this comparison from Ch2's "ten million times" per transistor switch.
4. Line 34: "keeping those levels apart" -> "keeping those levels of analysis apart (a different axis from the levels of biological organization in the front matter)" (audit_terms.md C6).
5. Line 82: homeostatic plasticity "over hours and days" -> "over a day or more" (audit_terms.md B6, optional timescale agreement with Ch5's synaptic scaling "a day or two"; applied because it is a consistency fix, not a cut of unique material).
6. Footnotes: check_footnotes.py reports no problems (36 footnotes, 36 definitions, 43 references); ran --write.

## Companion changes
7. Line 33: "on the order of a hundred trillion synapses" -> "well over a hundred trillion synapses" and "The brain is roughly a million times slower per step" -> "Against a processor's clock, the brain is roughly a million times slower per step" (audit_numbers.md 2 and 5, C1:33).
8. Line 39: "Marr's three levels" -> "Marr's three levels of analysis" (matches chapter change 4, audit_terms.md C6).
9. Line 94: homeostatic plasticity "over hours and days" -> "over a day or more" (matches chapter change 5).
10. Line 99: rewrote the "Nor does the brain optimize nothing" sentence to match the cut chapter text (dropped gradient descent, the dopamine-population hedge, and cue combination, which the chapter no longer mentions there; kept the Chapter 3 and Chapter 6 examples).
11. Lab 1.4 Part B (lab_errata.md Chapter 1): delay cost raised from 2 to 40 units so the intended speed-over-accuracy lesson appears; step 5 now states that the 30 and 5 percent rates are wrong-action rates and that the delay cost is added to the outcome; step 7 now compares acting now, waiting, and Part A's always-flee rule and asks for the break-even delay cost. Check values recomputed (keywork/ch1/lab14.py): true predator 30.7 vs 45.95; combined 1.82 (act now), 2.345 (wait), 1.0 (always flee); break-even 29.5 units. Step 8 ("why reflexes trade accuracy for speed") now matches the numbers.
12. key_ch1.md: Lab 1.4 steps 5-7 rewritten for the new numbers (removed the old instructor note); errata section now says "Fixed in this edition: ..." for Lab 1.4 and keeps the Lab 1.2 design note.

## Skipped / no action
- audit_terms.md A3 (learning/memory), B1 (sensitive period), C4 (plasticity): Chapter 1 is the canonical wording; fixes belong to the glossary and other chapters.
- audit_terms.md C7 (gloss gradient descent at ch1:86): moot after the line 86 cut.
- audit_repetition.md A3 item 33 (Simon/Gigerenzer at Ch1:74 vs Ch8:132): report proposes no cut; both carry footnotes.
- audit_repetition.md A3 item 10 ("energy will become the binding constraint" at Ch1:102): Ch1 is kept; the cut is in Ch4.
- audit_xref.md: no Chapter 1 errors (Ch1:56/82/106 spot checks passed). The Ch3 companion's "Chapters 1 and 2 gave you a neuron" is in another chapter's file.
- Companion line 110 (Lin 1992 vs hippocampal replay 1994): not in the chapter body but not contradicted by it; left.
- House style scan (chapter and companion): no em dashes in prose, no British spellings, no bare numerals one to ten in prose (lab step numbers and model values are exempt). Nothing to fix.
- No further within-chapter redundancy cut: the closing "If there is one idea to carry forward" (line 96) overlaps the Central Lesson but frames the transition to Chapter 2; left for the author.

## Build
python3 docs/build.py Chapter1/ succeeded (chapter and companion, docx and pdf).

## Word count (body above "# References and Attribution", excluding image lines)
Before: 5193. After: 5161 (-32).
# Applied changes: Chapter 2 (Neurons) and its companion

## Chapter body (docs/book/Word/Chapter2/How_the_Brain_Learns_Chapter_2_Neurons.md)
1. Golgi stain retelling shortened to a callback: "with Camillo Golgi's silver method (Chapter 1) and drew" (audit_repetition A2 Ch2, cuts.py (2,14)). Footnote [^1] unaffected.
2. Attwell and Laughlin budget sentence shortened to "By Attwell and Laughlin's estimate in Chapter 1, most of the energy budget goes to pumping back the ions that signaling lets through.[^4]" (A2 Ch2, (2,24)). Marker [^4] kept.
3. Deleted "Nothing travels the length of the axon except causation." (A2 Ch2, (2,98), within-chapter redundancy with the preceding sentence).
4. Thorpe experiment shortened to a callback to Chapter 1, [^38] kept (A2 Ch2, (2,112)).
5. Sterling and Laughlin near-verbatim repeat of Ch1 shortened, [^44] kept (A2 Ch2, (2,130)).
6. Energy section: added "and Peter Lennie's later calculation, described in Chapter 1, puts the affordable fraction nearer one in a hundred" after the fifteen percent figure (audit_numbers #3); Lennie (2003) appended to footnote [^43] and added to the References list.
7. "noradrenaline" -> "norepinephrine" in "A Neuron in Context" (audit_terms B2).
8. Footnotes checked and renumbered with check_footnotes.py (48 footnotes, 48 definitions, 58 references, no problems).

## Companion (docs/companion/Chapter2/Word/How_the_Brain_Learns_Chapter_2_Student_Notes_and_Labs.md)
9. "noradrenaline" -> "norepinephrine" in "A neuron in context" (audit_terms B2, co2:117).
10. Lab errata (lab_errata Ch2): removed the unused "Time step: 5 ms" parameter from Labs 2.1 and 2.2; added Lab 2.1 Part D (steps 14-16) in which the cell reaches threshold (75 simultaneous Branch A inputs; two bursts 10 ms apart need 50 per burst, 100 in all; values computed in keywork/ch23 and keywork/ch2/labs.py logic); stated in Lab 2.1 "What to record" and in Lab 2.2 Purpose that Parts A to C measure distance from threshold.
11. House style (numbers one to ten as words in lab prose): "Place four ... four ... and four", "Place ten / six", "fire all ten EPSPs", "fire six IPSPs", "three-column table", "at least eight rows", "four synapses: two excitatory, two inhibitory".
12. Answer key key_ch2.md: added answers for Lab 2.1 steps 14-16; errata section replaced with "Fixed in this edition: ...".

## Skipped / not changed
- Epigraph kept exactly as published ("brightly coloured", "some day—who knows?—"), per instructions and epigraphs.md (audit_repetition B1 / C in-quotation note).
- Optional Spanish-original addition to the Epigraph note (epigraphs.md item 1): not an audit finding; left to the author.
- audit_numbers #5 ("ten million times" vs Ch1's "a million times"): the report says Ch2's figure is correct and stays; no Ch2 change.
- audit_xref Ch13:40 (noise along a fiber attributed to Ch2): the fix belongs in Chapter 13, not Chapter 2.
- Companion sentence "Nothing travels the length of the axon except causation." kept: it is a study-note summary, not a factual mismatch with the chapter (the chapter still says what travels is a pattern of channel openings).
- No em dashes, British spellings, or stray numerals found in Chapter 2 body prose (references keep published titles such as "grey matter", "fibre", "anaesthetized").

## Word count (body above "# References and Attribution", image lines excluded)
- Before: 5483
- After: 5439 (-44)
# Applied changes: Chapter 3 (Neuromodulation) and its companion

(The Henry Dale epigraph and its Epigraph note were already in place and were left untouched.)

## Chapter body (docs/book/Word/Chapter3/How_the_Brain_Learns_Chapter_3_Neuromodulation.md)
1. "Chapters 5 and 6 return to the question." -> "Chapters 10 and 11 return to the question." (audit_xref, Ch3:74).
2. Three-factor rule: "A synapse changes only when three things coincide within the lifetime of the trace:" -> "A change that lasts requires three things to coincide within the lifetime of the trace:" (audit_terms A1).
3. "synaptic tagging and capture, the molecular form of the trace" -> "a slower relative of the trace" (audit_terms A2).
4. "whose job is not to carry information" -> "whose job is not to carry detailed content" (audit_terms C5).
5. Striatum glossed at first use: "project to the striatum, the input stage of the basal ganglia described in Chapter 4, and to the prefrontal cortex" (audit_terms C7).
6. Slow-wave sleep glossed at first use: "as during slow-wave sleep, the deep stage of sleep that Chapter 5 describes," (audit_terms C7).
7. Repetition cut: the two-prediction-errors passage shortened to "Second, the error in question is a single number about value; Chapter 6 introduces a different, high-dimensional prediction error about sensory content, and the two should not be confused." (audit_repetition A2 Ch3, cuts.py (3,64)).
8. Repetition cut: "No loss function is handed to the brain. It has many local errors, the temporal-difference error among them, and it reduces them under" -> "The brain reduces its many local errors under", [^48] kept (A2 Ch3, (3,134)).
9. Own within-chapter consistency fix following audit_terms A1: in the AI section, "Nothing changes unless the context says it should." -> "Little changes for long unless the context says it should." (the absolute version contradicted the chapter's own statement that activity alone induces plasticity and modulators decide whether it is kept). Lab 3.4 step 7 and key_ch3.md quote updated to match.
10. Miconi et al. (2019) reference and footnote [^46]: "*International Conference on Learning Representations (ICLR)*" -> "In *International Conference on Learning Representations*" (audit_numbers #11).
11. Footnotes checked and renumbered with check_footnotes.py (48 footnotes, 48 definitions, 77 references, no problems).

## Companion (docs/companion/Chapter3/Word/How_the_Brain_Learns_Chapter_3_Student_Notes_and_Labs.md)
12. "Chapters 1 and 2 gave you a neuron" -> "Chapter 2 gave you a neuron" (audit_xref; lab_errata Ch3).
13. "Chapters 5 and 6 return to this." -> "Chapters 10 and 11 return to this." (audit_xref; lab_errata Ch3).
14. "Chapter 5 describes its molecular form, synaptic tagging and capture." -> "Chapter 5 describes a slower relative, synaptic tagging and capture, which works over hours." (audit_terms A2, co3:91).
15. Eligibility-trace note: "nothing happens" -> "nothing lasting happens" (matches chapter wording, audit_terms A1).
16. Two-prediction-errors note: added "and should not be confused" to match the shortened chapter sentence.
17. "The chapter's rewritten Clinical Evidence section" -> "The chapter's Clinical Evidence section" (stray edition-history word).
18. Lab 3.2 step 3: "below 0.01" -> "at or below 0.01" (lab_errata Ch3; at 3 s delta_w = 0.0100 exactly).
19. Lab 3.4 step 7 quotation updated to "little changes for long unless the context says it should" (follows item 9).
20. House style numbers: "for eight trials", "for four trials", "Over ten trials", "the ten trials" (three places).
21. Answer key key_ch3.md: Lab 3.2 step 3 answer aligned with "at or below 0.01" (threshold 3 s); Lab 3.4 quotation updated; errata items replaced with "Fixed in this edition: ..." lines.

## Skipped / not changed
- audit_terms C4 (ch3:32 "Synaptic plasticity, the lasting change in the strength of a connection" -> "the capacity of a connection to change its strength lastingly"): skipped, because the sentence continues "can be induced by presynaptic and postsynaptic activity alone", and a capacity being "induced" reads worse than the current wording.
- audit_terms C8 / B9 (add Yu and Dayan to Ch3, or change co3:104 to "(Chapter 6)"): skipped, because the premise is wrong: Chapter 3 already presents Yu and Dayan's account in "Norepinephrine, Serotonin, and Acetylcholine" (with footnote [^34]), so co3:104 has a chapter source.
- audit_terms C7 for ch3:32 ("consolidated"): the report itself says no change is required.
- audit_repetition B1 (duplicated Cajal epigraph): already resolved before this pass (Dale epigraph); left as is.
- No em dashes, British spellings, or stray numerals one to ten found in Chapter 3 body prose after the edits.

## Word count (body above "# References and Attribution", image lines excluded)
- Before: 5383 (counted after the epigraph replacement, which preceded this pass)
- After: 5357 (-26)
# Applied changes: Chapter 4 (Circuits, Networks, and Coordinated Behavior)

Files: docs/book/Word/Chapter4/How_the_Brain_Learns_Chapter_4_Circuits.md; docs/companion/Chapter4/Word/How_the_Brain_Learns_Chapter_4_Student_Notes_and_Labs.md; key_ch4.md.

## Chapter
1. Line 16: "on the order of 86 billion neurons ... roughly 150 trillion synapses" -> "about 86 billion neurons ... about 164 trillion synapses" (audit_numbers #2; canonical 164 trillion, Tang et al. 2001, as used in Ch13/15/16).
2. Footnote [^1]: added Tang, Nyengaard, De Groot & Gundersen (2001) to the citation list and changed the tail to "Tang and colleagues count about 164 trillion synapses in the neocortex, and Pakkenberg and colleagues give a similar figure of about 150 trillion for young adults." (audit_numbers #2).
3. References: added the Tang et al. (2001) *Synapse* 41(3), 258–273 entry (audit_numbers #2).
4. Line 42: "the basis of working memory and of pattern completion" -> "the basis of working memory, the holding of information in mind for seconds, and of pattern completion, described below" (audit_terms C7; terms used before definition).
5. Line 170: cut "As energy becomes the binding constraint on large models, the brain's economies are worth studying." (audit_repetition A2 Ch4 / aud/cuts.py; motif's home is Ch10:112; paragraph ends cleanly on "adds up").
6. Footnotes checked and renumbered with check_footnotes.py (48 footnotes, 48 definitions, 87 references, no problems).

## Companion
7. Lab 4.1 Given parameters: added the no-reset convention ("spike" means V at or above threshold on that step; V followed onward after a crossing) (lab_errata Ch4).
8. Lab 4.3 step 4: "What happens to the period, and does the rhythm survive?" -> "Does the rhythm survive? If it does, what happens to its period; if it does not, what state does the circuit settle into?" (lab_errata Ch4; with fatigue 0.2 the rhythm stops, L settles at x = 0.5).
9. Lab 4.3 optional extension: stone moved from step 150 to step 140 ("after computing that step"), plus a request to try step 150 and a warning that a stone early in a burst can lock the synchronous model into a symmetric two-step cycle (both at 0.474, then both at 0) (lab_errata Ch4). Verified with keywork/hco4.py: lock occurs for stone steps 136-139 and 150-153; step 140 recovers; the feedback term (D + 0.1 for the more fatigued side) recovers for every step 130-159.
   - Deviation from the errata's suggestion: step 145 was NOT used, because x is already 0 at steps 143-147, so a stone there changes nothing (verified by running the model).
10. Student Notes checked against the edited chapter: no synapse count, no energy-constraint sentence, figure numbers and terms unchanged; no further edit needed.

## Answer key (key_ch4.md)
11. Lab 4.3 optional-extension note rewritten for the step-140 stone and the step-150 warning.
12. Errata section: Lab 4.3 extension, Lab 4.3 step 4, and Lab 4.1 no-reset items replaced by "Fixed in this edition: ..." entries. Lab 4.5 step 4 averaging note (2.27 vs 2.33) kept: it is not in lab_errata.md and the lab is correct as instructed.

## Skipped / no action
- audit_terms B3 (reward prediction error at ch4:108): already canonical; no change.
- audit_repetition A3 index items naming Ch4 (reward prediction error hedge at Ch4:108, Golgi at Ch4:86, place cells at Ch4:138, Ch1 slogan quoted at Ch4:82): all marked "keep" or "acceptable"; the optional cut of the slogan is in Ch6, not Ch4.
- audit_xref Ch13:104 (add Chapter 4 to the basal ganglia citation) and audit_terms C8 co6:246 concern other chapters' files.
- House style: no em dashes in prose (only the "> ---" epigraph attribution and YAML), no British spellings, no stray numerals one to ten in prose; numerals in lab values left as is.
- No further within-chapter redundancy cuts found that would not remove unique content.

## Word count (body above "# References and Attribution", image lines excluded)
Before: 4,197. After: 4,189.

Build: `python3 docs/build.py Chapter4/` succeeded (book and companion docx and pdf).
# Applied changes: Chapter 5 (Plasticity and Memory)

Files: docs/book/Word/Chapter5/How_the_Brain_Learns_Chapter_5_Plasticity_and_Memory.md; docs/companion/Chapter5/Word/How_the_Brain_Learns_Chapter_5_Student_Notes_and_Labs.md; key_ch5.md.

## Chapter
1. "The Third Factor": "a synapse changes when it was recently active" -> "a synapse changes lastingly when it was recently active" (audit_terms A1; removes the contradiction with the next sentence that activity alone induces change).
2. "The Third Factor": "and it is the eligibility trace of Chapter 3 seen at the level of molecules" -> "a slower, molecular relative of Chapter 3's eligibility trace that works over hours rather than seconds" (audit_terms A2; trace = seconds to minutes, tag = one to two hours).
3. "Keeping the Whole Neuron Stable": "This synaptic scaling is slow" -> "This synaptic scaling, the form of homeostatic plasticity that Chapter 1 introduced, is slow" (audit_terms B6).
4. "Two Clocks": named the theory: "two systems, called complementary learning systems, was set out in 1995" (audit_terms B7).
5. "Why Learning Is Slow": "Early LTP takes minutes;" -> "Early LTP forms in minutes and lasts an hour or two;" (audit_terms C1).
6. "Kinds of Memory": H.M. "after most of both hippocampi" -> "after the front part of both hippocampi" (audit_numbers #6; Corkin et al. 1997 MRI found the posterior hippocampal body spared).
7. Within-chapter redundancy (own finding): cut the paragraph "Figure 5.1 shows the two states. In the first, ... a cascade of enzymes begins that can last for hours." It restated the Figure 5.1 caption and the preceding paragraph (figure already cited at the magnesium plug). Next section's opening "The two outcomes of that cascade" -> "The two outcomes of the enzyme cascade that calcium sets off" so the antecedent survives.
8. Footnotes checked and renumbered with check_footnotes.py (61 footnotes, 61 definitions, 138 references, no problems). No footnote markers were removed.

## Companion
9. Student Notes, "The third factor": "a synapse changes when" -> "a synapse changes lastingly when" (audit_terms A1, co5:60).
10. Student Notes: "This is synaptic tagging and capture: Chapter 3's eligibility trace at the level of molecules." -> "..., a slower, molecular relative of Chapter 3's eligibility trace that works over hours rather than seconds." (audit_terms A2, co5:62).
11. Student Notes, "Why learning is slow": "Minutes for early LTP," -> "Minutes to form early LTP, which lasts an hour or two;" with the list punctuation made consistent (audit_terms C1, co5:103).
12. Student Notes: "Patient H. M." -> "Patient H.M." (audit_numbers #6 spelling).
13. Student Notes, synaptic scaling bullet: added "the form of homeostatic plasticity introduced in Chapter 1", and "Timescale about a day" -> "Timescale a day or two" to match the chapter (audit_terms B6; companion had drifted from the chapter).
14. Student Notes, "Two clocks": "Why two systems (McClelland, ...)" -> "Why two systems, the complementary learning systems theory (McClelland, ...)" (audit_terms B7, to match chapter edit 4).
15. Lab 5.3 window: added "if dt = 0 (both spikes at the same moment), no change" (lab_errata Ch5).
16. Lab 5.5 step 3 check: w = (0.476, -0.223) -> (0.477, -0.223) (lab_errata Ch5; recomputed: w1 = 0.47671).

## Answer key (key_ch5.md)
17. Lab 5.3 step 5 answer now cites the lab's stated dt = 0 convention instead of "undefined at zero (score it as no change)".
18. Lab 5.5 step 3 answer: "rounds to 0.477, not 0.476 (see Errata)" -> "rounds to 0.477 (matches the corrected check)".
19. Errata section replaced with "Fixed in this edition" entries for Lab 5.5 step 3 and Lab 5.3 dt = 0.

## Skipped / no action
- audit_terms A3 (glossary Learning/Memory vs ch5:14): the fix is to the front-matter glossary, not Chapter 5; ch5:14 is the canonical physical framing.
- audit_repetition A3 items with home in Ch5 (complementary learning systems, H.M., replay convergence, Hebb, forgetting curve): Ch5 is the home; all cuts fall in other chapters.
- audit_repetition index #8 (Bliss and Lomo named only in Ch2; Ch5:54 gives 1973 without names): the report proposes no Ch5 change, only a Ch15 cross-reference fix.
- House style: no em dashes in prose (only the "> ---" epigraph attribution and YAML), no British spellings, no stray numerals one to ten in prose; lab numerals left as computed values.

## Word count (body above "# References and Attribution", image lines excluded)
Before: 4,617. After: 4,605.

Build: `python3 docs/build.py Chapter5/` succeeded (book and companion docx and pdf).
# Chapter 6: changes applied

## Chapter (docs/book/Word/Chapter6/How_the_Brain_Learns_Chapter_6_Perception_as_Inference.md)
1. Line ~36 (Bayes): defined precision at first technical use, "relative precision, the inverse of a distribution's variance (the narrower the curve, the more precise)". audit_terms C2 (used "variance" rather than the proposed "spread" to match the companion's 1/s² and the glossary's "inverse of its variance").
2. Line ~110 (Ernst and Banks): repetition cut "Sense in which the brain optimizes (home: Ch3 line 84)", exact replacement from aud/cuts.py. This also removes "the dopamine error of that chapter", resolving audit_terms B3 for the chapter.
3. Line ~118 (Perception Is Active): deleted the second quotation of the Chapter 1 slogan (cuts.py, "Ch1 slogan quoted a second time"); paragraph now opens "The account so far has treated the brain...".
4. Line ~136 (Learning the Priors): repetition cut "Hubel and Wiesel monocular deprivation (home: Ch1 line 62)" merged with audit_terms B1. Text now: "The window is the one Hubel and Wiesel found in kittens with one eye closed (Chapter 1).[^45] This critical period, the strict form of the sensitive periods introduced there, closes, in the cat, ...". Footnote [^45] kept on the surviving claim. (Used B1's "strict form of the sensitive periods" wording instead of the cut's parenthetical "(the sensitive period of Chapter 1)", which would have equated the two terms.)
5. Footnotes: check_footnotes.py reports 63 footnotes, 63 definitions, 93 references, no problems; --write run (no renumbering needed; no footnote or reference removed).

## Companion (docs/companion/Chapter6/Word/How_the_Brain_Learns_Chapter_6_Student_Notes_and_Labs.md)
6. Misconception 3: "treating attention only as a spotlight that selects, rather than also as a gain..." (audit_terms A5).
7. Practical summary: "On the predictive coding proposal, attention is precision: gain on errors..." (audit_terms A5).
8. Goals paragraph: "why attention is precision" -> "why attention can be treated as precision" (A5, same hedge, matches the chapter's "proposal").
9. Lab 6.2 step 6: "the chapter's claim that attention is precision" -> "proposal" (A5).
10. Combining the senses note: "the dopamine error of Chapter 3" -> "the reward prediction error of Chapter 3" (audit_terms B3) and "the local sense ... (Chapter 3)" to match the trimmed chapter sentence.
11. Learning the priors bullet: "Critical period (Hubel and Wiesel; the strict form of Chapter 1's sensitive period)" (audit_terms B1, matches chapter edit 4).
12. Lab 6.5 step 4: "(Chapter 4)" -> "(Chapters 4 and 6)" for the forward model (audit_terms C8).
13. House style: "cancelling" -> "canceling" (Lab Notes); "about 1 million ganglion-cell axons" -> "one million"; Lab 6.4 "5 times more likely" -> "five times".
14. key_ch6.md: errata section notes the wording-only lab fixes; no check values changed (lab_errata.md has no Chapter 6 items; key already reported none).

## Skipped / not applicable
- audit_xref items on Ch3:74, Ch10:100, co3:79 mention Chapter 6 but live in other chapters' files; not touched. (Note for the editor: audit_xref says Ch6 never mentions backpropagation, but Ch6 line ~162 does discuss predictive-coding networks approximating backpropagation, citing [^62]; the Ch10:100 claim is therefore partly supported.)
- audit_terms A5 ch14 and B1 ch1/ch12, B3 ch8/co13/co15, C8 co3: other chapters.
- Optional cuts in aud/optional.py: none for Chapter 6.
- House-style scan: no em dashes or British spellings in chapter prose ("modelling" occurs only in cited-work titles in References, kept); epigraph "> ---" attribution kept per house format; no stray numerals one to ten in chapter prose.
- Companion figure numbers and facts re-checked against the chapter: unchanged (Figures 6.1 to 6.10 untouched).

## Build
python3 docs/build.py Chapter6/ succeeded (book and companion docx + pdf).

## Word count (chapter body above "# References and Attribution", excluding image lines)
Before: 5739. After: 5674 (-65).
# Chapter 7: applied audit changes

## Chapter (docs/book/Word/Chapter7/How_the_Brain_Learns_Chapter_7_Emotion_and_the_Body.md)
1. Line 12: cut "A model of the world is not yet a reason to do anything." (audit_repetition A1, Opening: same point made three ways).
2. Line 34: Figure 7.1 text merged into one sentence (A1, Figure 7.1 described twice).
3. Line 54: cut "Body signals do not only report a state; they reset the animal's priorities." (A1, Sickness behavior).
4. Line 78: cut "And every position agrees on the part this chapter needs: ..." (A1, Thesis restated).
5. Line 86: RPE callback shortened to "The reward prediction error of Chapter 3 is computed ...: a drop of juice ..." (A1 cross-chapter, RPE home Ch3).
6. Line 112: "which is why the fear can return and why, as Chapter 5 noted" -> "which is why, as Chapter 5 noted" (A1, Fear returns after extinction).
7. Line 140: "common language" sentence folded into the correlational sentence (A1, Disorders as errors of estimation).
8. Line 106: "only 3 of 12" -> "only three of 12" (audit_repetition C1).
9. Line 180: inserted after the Doya sentence "Later work, described in Chapter 12, suggests that they divide the learning rate between them: norepinephrine raises it when the world has changed, and acetylcholine weights incoming evidence when the world is noisy but stable." (audit_terms A4; "suggests" added because Ch12:80 itself says "Who sets the rate in the brain is less clear").
10. Line 64 (actual first use; audit said 70): "an injection of adrenaline, the adrenal hormone that American physiologists call epinephrine and a close chemical relative ..." -> "an injection of epinephrine (also called adrenaline), the adrenal hormone and a close chemical relative ..." (audit_terms B2).
11. Lines 70, 118, 120 (Figure 7.5 caption), 140, 146 (x2): "adrenaline" -> "epinephrine" (audit_terms B2).
12. Figure 7.5 (make_figures.py, fig_stress_axes): box label "adrenaline: ..." -> "epinephrine: ..."; figure regenerated and checked visually (B2, to match caption/text).
13. Footnotes: no cut carried a marker; check_footnotes.py clean (107 footnotes, 107 definitions, 110 references), --write run.

## Companion (docs/companion/Chapter7/Word/How_the_Brain_Learns_Chapter_7_Student_Notes_and_Labs.md)
14. Line 51: Cannon bullet "adrenaline injections" -> "epinephrine injections"; gloss -> "(Epinephrine, also called adrenaline, is a close relative of Chapter 3's norepinephrine.)" (B2).
15. Lines 54, 88, 97, 98, 286 (Lab 7.6 step 3), 322 (capstone step 3): "adrenaline" -> "epinephrine" (B2).
16. Line 74: "and all agree that emotional states carry ..." -> "and all can accept the chapter's thesis that ..." (chapter sentence it summarized was cut in item 4; thesis survives at chapter line 16).
17. Line 84: RPE bullet shortened to "The reward prediction error of Chapter 3 is computed ..." to match item 5.
18. Line 85: grammar slip "separating wanting (...) differs from liking" -> "separating wanting (...) from liking" (found while checking notes).
19. Line 125: Doya bullet gets the Chapter 12 division-of-labor sentence (match item 9).

## Answer key (key_ch7.md)
20. "adrenaline" -> "epinephrine" in capstone answers (4 places); errata section adds "Fixed in this edition: ..." for items 14-18. No lab check values changed (lab_errata.md has no Chapter 7 items), so no recomputation needed.

## Skipped
- Optional cuts (Dutton and Aron bridge, BNST, hand-holding, flashbulb memories): unique material, left to the author per brief.
- audit_terms B3 (reward prediction error): Chapter 7 already uses the canonical term; nothing to change.
- No em dashes, British spellings, or numerals one to ten in prose found beyond item 8 (epigraph "> ---" attribution is house format; en dashes in reference page ranges are not prose).

## Word count (body above "# References and Attribution", excluding image lines)
Before: 6873. After: 6812 (-61). Build: python3 docs/build.py Chapter7/ succeeded (docx + pdf for chapter and companion).
# Chapter 8: applied audit changes

Files edited: docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md, docs/companion/Chapter8/Word/How_the_Brain_Learns_Chapter_8_Student_Notes_and_Labs.md, scratchpad key_ch8.md.

## Chapter changes
1. Line 16, roadmap paragraph condensed to the audit's replacement (audit_repetition A1 Ch8, within-chapter; each clause is restated in its section and the Central Lesson).
2. Line 32, deleted "Chapter 6's eye movements are decisions of the same kind, each a choice of where to sample next." (A1 Ch8, Wald item; Ch6:128 already says it).
3. Line 40, deep brain stimulation gloss replaced by "of the subthalamic nucleus (Chapter 3)" (A1 Ch8, cross-chapter; verified that Ch3:120 and Figure 3.9 describe the electrode and STN).
4. Line 68, reward prediction error restatement shortened to "learned from outcomes by the reward prediction error of Chapter 3, which adjusts ..." (A1 Ch8, home Ch3; footnote [^29] kept).
5. Line 70, Iowa/Fellows and Farah sentence condensed per A1 Ch8, with one wording change: "traced largely to" instead of "traced to", to keep the original hedge ("largely explained"). Footnote [^32] kept.
6. Line 124, "through the dopamine prediction error of Chapter 3" -> "through the reward prediction error of Chapter 3" (audit_terms B3 canonical term).
7. Line 154, deleted "The brain spends time in proportion to difficulty, stops when it is sure enough, and raises the bound when errors are expensive." (A1 Ch8, within-chapter).
8. Line 162, "Fifth" paragraph shortened to the audit's replacement pointing back to the cost-of-thinking section (A1 Ch8, within-chapter).
9. Footnotes: no footnote markers were removed; check_footnotes.py clean (98 footnotes, 98 definitions); --write run (renumbering produced no textual change).

## Companion and key
10. Lab 8.2 step 4 check: "best at a = 1.5 or 2.0, which are nearly tied at 0.152" -> "0.105, 0.137, 0.152, 0.151; a = 1.5 is marginally best, with a = 2.0 nearly tied." Recomputed with keywork/lab82.py (0.1047, 0.1366, 0.1521, 0.1515). Source: rounding note in key_ch8.md errata (not in lab_errata.md; small and verified, so applied).
11. key_ch8.md: errata rounding note replaced with "Fixed in this edition: ..."; Lab 8.7 required node "dopamine prediction error" -> "reward prediction error (dopamine)" (B3).
12. Companion Student Notes rechecked against the edited chapter: all facts still present in the chapter (cuts removed only restatements); figure numbers unchanged (8.1 to 8.7); "dopamine reward prediction error" in Notes already uses the canonical term (audit_terms B3 lists co8:52 as canonical). No change needed.

## Skipped
- Optional unique-material cuts (A1 "Author's call": collapsing bounds Ch8:42, divisive normalization Ch8:64, marshmallow trust studies Ch8:102, Henrich Ch8:142): left to the author per brief.
- audit_terms B9 analogue (Ch8:110 and Ch8:158 cite Chapter 3 for the norepinephrine/unexpected-uncertainty account): not a problem; Ch3:104 now states Yu and Dayan's account explicitly, so the reference is correct.
- key_ch8 clarity note on Lab 8.1 step 5 (doubling samples equals halving the bound): left in the key as a teaching note; the lab question is answerable as written and the key already gives the distinction.
- audit_numbers LOW items naming B8 (Gal and Ghahramani; Kadavath) use the Ch8 form as canonical; no Ch8 change.
- House style: no em dashes, British spellings, or numerals one to ten in prose found in chapter or companion (en dashes only in reference page ranges; "5 dollars" kept as a numeral with unit, matching "110 dollars" in the same sentence).

## Word count (body above "# References and Attribution", image lines excluded)
Before: 6856. After: 6673 (-183).

Build: python3 docs/build.py Chapter8/ succeeded (docx + pdf for chapter and companion).
# Chapter 9: applied audit changes

## Chapter (docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md)
1. Line 18 roadmap: rewrote "practice does three things ..." (which then listed four) as one sentence naming the cerebellum, basal ganglia/dopamine, and cortex. Kept "out of true" for voice. (audit_repetition A1 Ch9:18; C content slip)
2. Line 22: deleted "The tenth hour helps less than the first, but the thousandth still helps." (A1 Ch9:22, within-chapter repetition)
3. Line 32: "insensitivity to devaluation: the habitual rat keeps pressing ..." -> "insensitivity to devaluation." (A1 Ch9:32)
4. Line 34: tightened the H.M. callback; footnote [^8] kept. (A1 Ch9:34, home Ch5)
5. Line 70: folded the Chapter 8 recap of dorsomedial/dorsolateral control into one sentence. (A1 Ch9:70, home Ch8:122)
6. Line 86: "Chapter 8 described the dilemma ... exploration means" -> "For a movement, the exploration of Chapter 8 means". (A1 Ch9:86)
7. Line 164: "Practice adds a twist to Chapter 8's arbitration between planning and habit: ..." (A1 Ch9:164, tightening)
8. Line 50: removed the second definition of adaptation as recalibration. (A1 Ch9:50)
9. Line 158: removed "like the habitual rat" from the cached-network sentence. (A1 Ch9:158)
10. References and footnote [^12]: Martin et al. 1996 title "prisms: I." -> "prisms. I." (two places). (audit_numbers item 10)
- Footnotes: no footnote markers were removed by the cuts; check_footnotes.py reports 96 footnotes / 96 definitions, no problems; --write made no further changes.

## Companion (docs/companion/Chapter9/Word/How_the_Brain_Learns_Chapter_9_Student_Notes_and_Labs.md)
11. Lab 9.6 step 3 check: "at five it is 0.50, a tie" -> "at five it is 0.499, just short of 0.5, so R still narrowly wins." Recomputed: 0.6 x (1 - 0.7^5) = 0.4992; at six, 0.5294. (lab_errata Ch9)
- Student Notes rechecked against the edited chapter: the thesis bullet (three numbered roles) and other facts, figure numbers 9.1 to 9.7, and terms all still match. No other changes needed.

## Answer key (key_ch9.md)
12. Lab 9.6 step 3 answer updated to match the new check; errata section now reads "Fixed in this edition: ...".

## House style
- No em dashes, British spellings (outside quotations), or numerals one to ten found in prose in the chapter or companion. The epigraph "> ---" attribution line is the house format and stays.

## Skipped
- Optional cuts (Ericsson/Chase/Faloon digit-span runner Ch9:58; Leon Fleisher Ch9:146; musician's dystonia/Byl Ch9:148): unique material left to the author, per the brief.
- audit_terms B8 (EWC attribution) and D (Ch16:46): the occurrences are in Chapters 10, 11, and 16, not this chapter's files.
- No further within-chapter cuts: the remaining overlaps (Central Lesson recap, rat at lines 12, 140, 168) are deliberate framing/callbacks.

## Word count (body above "# References and Attribution", excluding image lines)
- Before: 7123
- After: 7014 (-109)
# Applied audit changes: Chapter 10

## Chapter (docs/book/Word/Chapter10/How_the_Brain_Learns_Chapter_10_What_AI_Gets_Right_and_Wrong.md)
1. Line 26: Hubel and Wiesel to neocognitron history cut to one sentence (audit_repetition A, Ch10:26; home Ch6:54). Footnote [^5] kept.
2. Line 52: recap of Chapters 3, 5, 6 compressed to parenthetical chapter cites (audit_repetition A, Ch10:52). Kept "In every case learning is driven by error..." as a separate sentence instead of the proposed colon join, for flow; wording on the third factor kept neutral (consistent with audit_terms A1).
3. Line 88: "the one McCloskey and Cohen found in 1989 and Chapter 5 described: ..." -> "the catastrophic interference that ... found in 1989 (Chapters 1 and 5)" (audit_repetition A Ch10:88 and D cross-reference fix; they are named in Ch1:56, the phenomenon is described in Ch5:116).
4. Line 88: complementary learning systems restatement shortened to "the complementary learning systems of Chapter 5: a fast hippocampal learner that replays episodes into slow cortex" (audit_repetition A, Ch10:88; wording slightly adjusted from the proposal for grammar). [^40] kept.
5. Line 94: deleted "Plasticity in the brain is not a phase but a maintained state, and it is maintained at a cost." (audit_repetition A, Ch10:94, in cuts.py).
6. Line 100: feedback alignment / bursts / predictive coding passage tightened (audit_repetition A, Ch10:100) and reworded so Chapter 6 is credited with what it claims (audit_xref Ch10:100, as corrected by the coordinator: Ch6:162 states that predictive-coding networks can approximate backpropagation, citing Whittington and Bogacz; cortex-as-predictive-coding stays a hedge "as cortex may be"). Now: "The two most developed answers were met in Chapters 3 and 6. One is Chapter 3's backward pathway ... [^46] The other is Chapter 6's predictive coding: a network built to correct its own predictions, as cortex may be, can compute nearly the same weight changes ... [^47]". Both footnotes kept.
7. Line 144: deleted the pianist sentence (audit_repetition A, Ch10:144; home Ch9:164).
8. Line 156: "Learning all its life without forgetting ... are solutions to problems that every system meets once it is put to use, and machines lack them to their cost" -> "Lifelong learning without forgetting ... are solutions machines lack to their cost" (audit_repetition A, Ch10:156).
9. Line 172: "Seventy-six years later" -> "Three-quarters of a century later" (audit_repetition C6, time-anchored phrasing).
10. References + footnote [^5]: Hubel & Wiesel 1962 "*The Journal of Physiology*" -> "*Journal of Physiology*" (audit_numbers 8).
11. References + footnote [^73]: Kadavath et al. 2022 author list changed to the Ch8 form "Perez, E., … Kaplan, J. (2022)" (audit_numbers 11).
- Footnote check: 81 footnotes, 81 definitions, no problems; --write produced no changes (no footnotes removed by the cuts).

## Companion (docs/companion/Chapter10/Word/How_the_Brain_Learns_Chapter_10_Student_Notes_and_Labs.md)
12. Lab 10.7 step 1: "eleven properties" -> "thirteen properties" (lab_errata Ch10; verified against LEDGER in make_figures.py: 13 rows).
13. Student Notes, Bodies: "AlphaGo beat Lee Sedol 4 to 1" -> "four games to one" (house style numbers; matches chapter wording).
14. Lab 10.1 step 1: "by age 5, 10, and 20" -> "by ages five, ten, and 20" (house style numbers). Check values unchanged.
- Student Notes reviewed against chapter edits: no figure numbers, facts or terms changed by the chapter edits needed updating.

## Answer key (key_ch10.md)
15. Errata entry replaced with "Fixed in this edition: ..." and the Lab 10.7 note updated. No check values changed (none of the labs' numbers changed).

## Skipped
- Optional cuts of unique material (grid cells Ch10:46, Recht/Engstrom Ch10:64, Piantadosi Ch10:166): left to the author per brief.
- audit_xref's proposed "build on Chapters 3 and 6" / "as Chapter 6 proposed cortex may be": not used, since Ch6:162 does make the predictive-coding-approximates-backprop claim (coordinator correction); wording adjusted instead (item 6).
- audit_numbers 11 Hebb "New York: Wiley" vs "Wiley": the report leaves it as chapter-internal style; Ch10 already uses "Wiley", no change.
- audit_numbers 7 Kording/Körding: Ch10 only has the byline "Kording, K. P." in references (as published); no running-text use; no change.
- audit_repetition C: "programme" in the Turing epigraph is original spelling, kept; "> ---" epigraph attribution is house format, kept.
- Other house-style scans (em dashes, British spellings, numerals one to ten in prose) found nothing else in the chapter. In the companion, given-data numerals in Lab 10.6 ("10 of the non-cow photographs", beside 50 and 100) and lab ranks/sentence ranges were left as lab values.

## Word count (body above "# References and Attribution", excluding image lines)
Before: 7182. After: 7049 (−133).
# Chapter 11: applied audit changes

## Chapter (docs/book/Word/Chapter11/How_the_Brain_Learns_Chapter_11_Integrating_Brain_Mechanisms_into_AI.md)
1. Line 16 roadmap list of eight borrowings cut to one sentence (audit_repetition A, Ch11 "Roadmap list"; section heads and Central Lesson name them).
2. Line 32 "small network losing a list" opener replaced by a replay callback (A, cross-chapter, home Ch10:88). Modified the proposed wording slightly: "the remedy for forgetting that Chapter 10 demonstrated", so the section's first sentence still names forgetting.
3. Line 54 pattern completion: dropped the second definition ("in which a fragment of a memory settles into the whole") (A, within-chapter).
4. Line 66 Behrens retold as a pointer to Chapter 8 with all facts and [^34] kept (A, cross-chapter, home Ch8:110; verified Ch8:110 tells it).
5. Line 68 neuromodulator roles and Doya shortened, "met in Chapters 3 and 7" (A; verified Doya at Ch3:130 and Ch7:180). Changed the proposed "maps the four of them" to "maps the four main ones" because the count is no longer introduced. [^36] kept.
6. Line 72 deleted "A learning-rate schedule fixed in advance has no way to know that the world has changed." (A, within-chapter, restates line 68).
7. Line 90 dropped the doubled eligibility-trace callback (A).
8. Line 104 Keramati and Gutkin definition merged into one sentence (A).
9. Line 120 dropped the pianist simile, third use of the image (A, home Ch9:164).
10. Line 146 complementary-learning confirmation condensed (A, within-chapter).
11. Line 148 deleted "Building the brain's remaining solutions is also how neuroscience will find out..." (A, within-chapter, restates line 144).
12. Line 50 "2 trillion tokens" -> "two trillion tokens" (audit_repetition C2, house style).
- Footnotes: no markers lost; check_footnotes.py reports 75 footnotes, 75 definitions, no problems; --write run (renumber/sort, no orphans).

## Companion (docs/companion/Chapter11/Word/How_the_Brain_Learns_Chapter_11_Student_Notes_and_Labs.md)
13. Student Notes figure numbers fixed (lab_errata Ch11): memory map 11.7 -> 11.4; Horowitz 11.4 -> 11.5; surrogate gradients 11.5 -> 11.6; homeostatic reward 11.6 -> 11.7. Verified against chapter captions.
14. Lab 11.1 Purpose Figure 11.4 -> 11.5; Lab 11.4 Purpose Figure 11.6 -> 11.7 (lab_errata Ch11).
15. Student Notes "RETRO's 2-trillion-token database" -> "two-trillion-token" (house style, to match chapter change 12).
- No lab check values changed, so no recomputation needed. Student Notes otherwise still match the edited chapter (Behrens, Doya, e-prop notes unaffected).

## Answer key (key_ch11.md)
16. Figure-number erratum replaced with "Fixed in this edition: ..." line; answers already cited the correct figure numbers (11.4 memory map, 11.7 homeostatic), no other change.

## Skipped
- Optional cuts of unique material (Ch11:60 Whittington transformer grid cells; Ch11:138 other brain-data studies): left to author per brief.
- audit_terms B8 (EWC attribution) and B7 (complementary learning systems naming): fixes are in Ch16/Ch5, not Ch11; Ch11:36 already says "Chapter 9 described elastic weight consolidation".
- audit_xref: no finding requires a Ch11 change (Ch11 references verified as correct there).
- audit_numbers: no Ch11 items.
- Epigraph attribution "> --- Richard Feynman" kept (house format).
- House-style scan: no em dashes in prose, no British spellings, no other bare numerals one to ten in prose in chapter or companion.

## Word count (body above "# References and Attribution", excluding image lines)
- Before: 6917. After: 6697 (220 words cut).

Build: `python3 docs/build.py Chapter11/` succeeded (docx + pdf for chapter and companion).
# Chapter 12: applied audit changes

Chapter: docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md
Companion: docs/companion/Chapter12/Word/How_the_Brain_Learns_Chapter_12_Student_Notes_and_Labs.md
Edit script: keywork/ch12/apply.py

## Changes (chapter)
1. Line 14: cut the Chapters 3-9 recap to one sentence, and "previous eleven chapters" became "previous chapters". (audit_repetition A1, Ch12:14; C4, stale count)
2. Line 36: cut the reactive vs predictive controller sentences; the paragraph now goes straight to Sterling. Footnote [^9] kept. (A1, Ch12:36; home Ch7:34)
3. Line 72: condensed the two-kinds-of-error restatement. I kept "a single number about value" in place of the proposed "scalar error about value", because "scalar" is not glossed for lay readers. (A1, Ch12:72; A3 item 3)
4. Line 80: replaced "As Chapter 11 described with Behrens's..." with "(Chapters 8 and 11)", and replaced "the neuromodulatory account of Chapter 3" with "(Chapter 6)". (A1 Ch12:80; D, Behrens first told in Ch8; audit_terms B9, Yu and Dayan are in Ch6 and not in the Ch3 body.) I used Chapter 6 rather than the cut text's "(Chapter 3)" because B9 checked the Ch3 body. I partly declined the A1 trim: I kept the glosses "of a noisy but stable world" and "of one that has changed", because Ch13:136 says "Norepinephrine raises the learning rate when the world has changed, as Chapter 12 described" and needs this sentence to support it (audit_terms A4 canonical).
5. Line 106: cut the savings caveat. (A1, Ch12:106; home Ch9:44)
6. Line 106: "Konrad Körding" became "Konrad Kording" in the running text. The reference byline is unchanged. (audit_numbers 7)
7. Line 112: condensed the fast and slow learners paragraph. (A1, Ch12:112; A3 item 1)
8. Line 116: free energy is now glossed as an information-theoretic quantity distinct from the thermodynamic free energy of Chapter 0. I checked that Ch0:30-34 uses the thermodynamic sense. (audit_terms B5)
9. Line 126: "compatible with predictive processing" became "compatible with predictive coding and its relatives, often grouped as predictive processing". (audit_terms B4)
10. Line 156: the fourth AI point now refers back to the kinds of error "described above". (A1, Ch12:156, within-chapter)
11. Line 158: tightened the Chapter 13 bridge sentence. (A1, Ch12:158)

## Changes (companion and key)
12. Companion line 61: "(Körding 2007)" became "(Kording 2007)". (audit_numbers 7)
13. key_ch12.md: "Körding" became "Kording" in the Lab 12.7 answer, and the errata section now notes that no lab values changed. lab_errata.md has no Chapter 12 items, so there were no lab or check-value changes and nothing to recompute.

## Skipped / no action
- The optional cuts in audit_repetition (flash-lag, the slow-speed prior and fog, Isomura, Kagan): left to the author, as the brief instructs.
- audit_terms B1 (ch12:102 "critical periods") and B6 (ch12:102 "over a day or two"): no Ch12 change was proposed, and both already agree with the canonical terms.
- audit_terms A4: the fix belongs in Ch7. Ch12 already states the canonical split, which item 4 keeps.
- audit_repetition B (the Craik epigraph is also the opening anecdote): flagged as a deliberate callback, so no action.
- House style: the chapter and companion have no em dashes in prose (only the "> ---" epigraph line and the YAML fences), no British spellings outside reference titles (for example "Behaviour" in a journal title), and no numerals one to ten in prose.
- Companion Student Notes: they still match the chapter. The figure numbers are unchanged (12.1 to 12.7), and every fact cited in the notes survives the cuts. The flash-lag, Yu and Dayan, and Körding (2007) citations all remain in the chapter.
- Footnotes: no footnote markers were removed. check_footnotes reports 62 footnotes, 62 definitions, and 70 references with no problems. Running --write produced no changes.

## Build
python3 docs/build.py Chapter12/ succeeded. It built the docx and pdf for both the chapter and the companion.

## Word count (body above "# References and Attribution", image lines excluded)
Before: 6621. After: 6423 (-198).
# Chapter 13: applied changes

## Chapter (How_the_Brain_Learns_Chapter_13_Why_the_Brain_Works_the_Way_It_Does.md)
1. Line 14: cut the book recap before Ch12's closing questions ("The earlier chapters described what the brain does, and Chapter 12 closed with questions...") (audit_repetition A1, Ch13:14; A3 item 40).
2. Line 30: synaptic failures sentence shortened to "the synaptic failures of Chapters 1 and 2" (audit_repetition A1, Ch13:30; A3 item 15, third statement of Allen and Stevens).
3. Line 72: deleted closing restatement "But a brain that pays for every axon is pushed toward..." (audit_repetition A1, Ch13:72, within-chapter).
4. Line 128: deleted re-definition clause "because improving one side worsens the other" (audit_repetition A1, Ch13:128).
5. Line 132: complementary-learning argument cut to "Here the constraint is statistical rather than physical." (audit_repetition A1, Ch13:132; A3 item 1).
6. Line 136: deleted "A fixed design must choose one compromise... different compromise for each." (audit_repetition A1, Ch13:136, within-chapter).
7. Line 104: basal ganglia cross-reference "(Chapters 3, 8, and 9)" -> "(Chapters 3, 4, 8, and 9)" (audit_xref, Ch13:104; Chapter 4 describes the loops).
8. Line 40: "and how noise added ... accumulates" -> "and any noise added ... accumulates" (audit_xref, Ch13:40; Chapter 2 never describes noise accumulating along a fiber).
9. Line 88: added "or about 25 watts, a little above the round 20 watts of Chapter 1, which comes from a different method of estimation" after the 500 kcal figure (audit_numbers item 4).
10. Footnotes: no markers lost in the cuts; check_footnotes.py clean (60/60), renumbered and references sorted with --write.

## Companion (How_the_Brain_Learns_Chapter_13_Student_Notes_and_Labs.md)
11. Lab 13.2 step 1 check: 2,648 -> 2,657 µm (lab_errata; (50/0.97)^2 = 2,657).
12. Lab 13.2 step 4: "ten passes back and forth" -> "ten one-way crossings", added check "about 167 ms" (lab_errata).
13. Lab 13.4 step 3 check reordered: "2.8 × 10^8 against 1.7 × 10^8" (genome then list, as in steps 1-2) (lab_errata).
14. Lab 13.5 step 4: w = 1 -> w = 1.5 so F is the unique best (F 92, E/H 91); checks F, D, B unchanged (lab_errata).
15. Lab 13.6 step 1: added conversion to watts and the question why 516 kcal (about 25 W) exceeds Chapter 1's 20 W; check "516 kcal; about 25 W" (audit_numbers item 4, optional companion note).
Recomputed in keywork/ch13/checks13.py. Student Notes checked against the edited chapter: no figure numbers, facts, or terms changed by the cuts.

## Answer key (key_ch13.md)
16. Updated Lab 13.2 steps 1 and 4, Lab 13.4 step 3, Lab 13.5 step 4 (w = 1.5; added H and F ranges to the w sweep), Lab 13.6 step 1 (watts and explanation); errata section replaced with "Fixed in this edition" lines.

## Skipped / no change needed
- audit_numbers item 2 (164 trillion synapses): Ch13 already uses the canonical figure.
- audit_terms A4 (norepinephrine vs acetylcholine for learning rate): the fix is in Ch7; Ch13:136 already matches the canonical synthesis.
- audit_terms B1 (sensitive period): Ch13 already uses the canonical term.
- audit_terms C2 (precision, everyday sense at Ch13:164): the replacement is in Ch6 only.
- audit_repetition A3 item 19 (Yu and Dayan at Ch13:136) and item 10 (20 watts at Ch13:24): marked keep.
- Ch13:160 bridge sentence: the duplicate is cut in Ch14, not here.
- Optional author's-call cuts (Ch13:94 obstetric dilemma, Ch13:96 elephantnose fish/Megaphragma): not taken, per brief.
- House style: no em dashes, British spellings (only "Behaviour"/"modelling" in cited titles), or bare numerals one to ten found in prose of either file; no changes needed.

## Word count (body above "# References and Attribution", excluding image lines)
Before: 7,091. After: 6,990 (-101).
# Chapter 14: applied audit changes

Chapter file: docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md
Companion: docs/companion/Chapter14/Word/How_the_Brain_Learns_Chapter_14_Student_Notes_and_Labs.md

## Chapter changes
1. Line 20: cut bridge sentence repeating Ch13:160; now "This chapter asks what those constraints imply for classrooms, offices, and screens." (audit_repetition A1; also A40)
2. Line 22: cut Bruer restatement ("A fact about synapses does not become a lesson plan ..."); kept "The evidence that matters most in this chapter is of that kind." (A1, within-chapter)
3. Line 40: "three things that slow it, retrieval, spacing, and sleep" -> "how spaced retrieval and sleep slow it" (A1; fixes factual mismatch with Ch5:140, audit D)
4. Line 48: removed the "much as Chapter 12's prediction errors ..." analogy, which line 58 repeats (A1)
5. Line 66: cut the hippocampus-to-cortex replay recap of Ch5 sleep consolidation (A1)
6. Line 74: "Attention is the means ..." -> "Attention, which Chapter 6 described as the weighting of evidence by its reliability, is also the means ..." (audit_terms A5, links capacity view to Ch6 precision view)
7. Line 90: cut self-control summary sentence restating lines 86-88 (A1)
8. Line 124: compressed recap of Chapters 3, 9, 13 to "The dopamine teaching signal of Chapter 3, the context-cued habits of Chapter 9, and the supernormal stimuli of Chapter 13 have all been applied, ..." (A1; slightly reworded from the proposal for flow)
9. Line 144: deleted the Bastani/Kestin restatement (A1; also removes the inaccurate "did the opposite", audit D)
10. Line 146: Bainbridge restatement shortened to "Second, automation should leave its users practiced, as Bainbridge's last irony warns." (A1)
11. Line 152: bridge to Ch15 shortened to "Putting these pieces together into one model of how the brain learns is the task of Chapter 15." (A1; fixes last-chapter phrasing, audit C5 and A40)
- No footnote markers were in any cut text; check_footnotes.py reports 68/68, no problems; --write run (no renumbering change needed).
- House style scan: no em dashes in prose (epigraph attribution kept), no British spellings outside quotations and reference titles, no numerals one to ten in prose.
- Figures unchanged (no optional cut taken, so Figure 14.7 rows stand).

## Companion changes (lab_errata.md)
12. Lab 14.1 step 1 check: 0.37 -> 0.375 (exact value; recomputed in keywork/lab14_1.py, other checks unchanged: S2 2.0/5.9/18.5/91.5, retention 0.34/0.60/0.83/0.96, expected 0.34/0.58/0.69/0.57).
13. Lab 14.2 step 3: "If the two 78 percent groups ... were independent" -> "Knowing nothing about how the two 78 percent groups ... overlap" (answer 56 percent stands).
14. Lab 14.7 step 2: "use Figure 14.1" -> "use Figure 14.2".
- Student Notes checked against the edited chapter: figure numbers, facts, and terms still match; no change needed.
- key_ch14.md: answers for Labs 14.1, 14.2, 14.7 updated to match; errata section replaced with "Fixed in this edition" entries.

## Skipped
- Author's-call optional cuts (left/right brain, Ramirez and Beilock, tablet light, Kosmyna): unique material, left to the author per brief.
- Lab 14.5 given values ("4 interruptions a day", "1 second") left as numerals: they are given quantities with units in a lab calculation.

## Word count (body above "# References and Attribution", excluding image lines)
Before: 6380. After: 6196 (-184, 2.9%).

Build: python3 docs/build.py Chapter14/ succeeded (docx and pdf for chapter and companion).
# Applied: Chapter 15 (A Coherent Model of the Human Brain)

Files: docs/book/Word/Chapter15/How_the_Brain_Learns_Chapter_15_A_Coherent_Model_of_the_Human_Brain.md; docs/companion/Chapter15/Word/How_the_Brain_Learns_Chapter_15_Student_Notes_and_Labs.md; key_ch15.md.

## Changes (chapter)
1. Line 12: "the chip inside the Apple I and the Commodore 64, a near-identical version of which ran the Atari" -> "the chip inside the Apple I, near-identical versions of which ran the Commodore 64 and the Atari video game console" (audit_numbers "checked and consistent" accuracy nit: the C64 used the 6510, a 6502 variant).
2. Line 22: Bliss and Lømo "(Chapter 5)" -> "(Chapters 2 and 5)" (audit_repetition A3 item 8 and D; they are named only in Ch2).
3. Line 24: "Helmholtz's inference became the predictions of Chapter 12" -> "became the inference of Chapter 6 and the predictions of Chapter 12" (audit_terms B11).
4. Line 58: "(Chapters 6, 9, and 12)" -> "(Chapters 6, 8, 9, and 12)" for the circuits of choice (audit_terms B10).
5. Line 58: "a lorry behind" -> "a truck behind" (audit_terms, American usage note).
6. Line 60: early LTP "for the next few hours" -> "for the next hour or two" (audit_terms C1).
7. check_footnotes.py: no problems; --write run (26 footnotes, 31 references; renumber/sort only).

## Changes (companion and key)
8. Companion Student Notes, "What is settled": "dopamine prediction errors" -> "reward prediction errors" (audit_terms B3).
9. key_ch15.md: same term change in the Lab 15.6 answers (two places) to match the companion and Figure 15.5. Errata section unchanged (no Chapter 15 lab errata in lab_errata.md; "None found" stands).

## Skipped / no action
- audit_numbers 2 (164 trillion) and 3 (one in a hundred): Ch15 already carries the canonical values; fixes are in Ch4/Ch2.
- audit_numbers 7 (Kording vs Körding): Ch15 and C15 already use "Kording", the proposed canonical form.
- audit_terms A1 (three-factor rule): Ch15:38 is the canonical wording; no change. A4 (norepinephrine and learning rate): Ch15:58 is the canonical synthesis; fix is in Ch7.
- audit_repetition A: no cuts proposed for Ch15 (its recaps at 20-24, 38, 40, 44 are marked "keep"); Ch14:152 bridge cut belongs to Ch14. No within-chapter redundancy worth cutting found.
- audit_repetition C: "millimetre" in the Crick quotation (line 94) kept (original spelling). Epigraph "> ---" line is house format. No em dashes, British spellings, or bare numerals one to ten in prose found.
- audit_xref: nothing for Ch15 (its cross-references pass spot checks).

## Build
`python3 docs/build.py Chapter15/` succeeded (docx and pdf for chapter and companion).

## Word count (body above "# References and Attribution", excluding image lines)
Before: 5,099. After: 5,108.
# Applied: Chapter 16 (NIMCP)

Files: docs/book/Word/Chapter16/How_the_Brain_Learns_Chapter_16_NIMCP.md; docs/book/Word/Chapter16/make_figures.py and images/fig_scale.png; docs/companion/Chapter16/Word/How_the_Brain_Learns_Chapter_16_Student_Notes_and_Labs.md; key_ch16.md.

## Changes (chapter)
1. Line 18 (disclosure paragraph), extra task (a): date stamp. Now reads "... the chapter follows the code. It describes NIMCP as it stood in October 2026, at commit 4693efd of the project's repository (18 October 2026), and later versions may differ; the questions it raises will outlast the details." The earlier "as they stood in October 2026" and "The project will have changed by the time this is read; the account describes it as it stood" were folded into this sentence to avoid saying it twice. Commit and date verified read-only in /home/bbrelin/nimcp (4693efd32, 2026-10-18, also HEAD).
2. Extra task (b): every NIMCP repository citation (12 References entries, 17 occurrences in 16 footnotes, including the two compound footnotes) now ends "NIMCP source repository (unpublished; examined 19 October 2026). Repository commit 4693efd, 18 October 2026." Footnotes and references changed by the same replacement, so they still match.
3. Note on Sources: "as they stood on 19 October 2026" -> "as they stood at commit 4693efd of the project's repository (18 October 2026), examined on 19 October 2026" (consistency with 1 and 2).
4. Line 28: "for roughly 2 million in all" -> "for roughly two million in all" (audit_repetition C3).
5. Line 46: elastic weight consolidation "that Chapter 11 described" -> "that Chapters 9 and 11 described" (audit_terms B8; audit_repetition A3 item 27 and D).
6. Line 54: the book's rule holds the change "for a second or so" -> "for seconds to minutes" in an eligibility trace (audit_terms A2; Ch3 defines the trace as seconds to minutes). The sentence describes the book's rule, not NIMCP's, so the change applies.
7. Line 92: NIMCP neurons have "about a tenth" -> "less than a tenth" of a cortical neuron's connections (lab_errata Ch16; 750 / 10,061 = 0.075).
8. make_figures.py:140: NIMCP spiking network 2.2e6 -> 2.0e6 (audit_numbers 1; lab_errata Ch16); regenerated fig_scale.png only (Figure 16.5 panel B now shows 750) and viewed it.
9. check_footnotes.py: no problems; --write run (18 footnotes, 19 references).

## Changes (companion)
10. Notes, disclosure bullet: "The account follows the code as of October 2026 (repository commit 4693efd, 18 October 2026); later versions may differ." (extra task (a), carried into the companion).
11. Notes: "About 2 million neurons" -> "About two million neurons" (house style); "intended word produced 1 of 20 times" -> "once in 20 tries" (house style).
12. Lab 16.1 step 3: states the background starts at step 0, as in Figure 16.3's simulation, asks for each delay, and adds "(Check: about 0.13, 0.22, and 0.32.)" (lab_errata Ch16, third item).
13. Lab 16.2 given values: "2.2 million neurons, about 682 synapses per neuron" -> "about 2.0 million neurons, about 750 synapses per neuron" (audit_numbers 1). Step 1 check unchanged (independent of N).
14. Lab 16.2 step 2: target rate 28 -> the chapter's early rate of 26, "a factor of about 32? (Check: about 172 steps.)" (audit_numbers 1 optional nit; lab_errata). ln(834/26)/-ln(0.98) = 171.7.
15. Lab 16.4 given values: "about 2.0 million neurons"; step 1 check "about 750, 391, and 10,061"; step 3 check "about 2.0 × 10^10 synapses; about 241 GB" (2.0e6 × 10,061.35 × 12 bytes = 241.5 GB).
Recomputation script: keywork/ch15_16b/calc16.py.

## Key
16. key_ch16.md: Lab 16.1 step 3 rewritten for the stated assumption (0.13, 0.22, 0.32; ratios 20.0, 8.15, 3.08; infinite-history answer accepted with assumption stated); Lab 16.2 steps 1 and 2 (2.0 million × 750; factor 32.08, 172 steps) and step 3 note (0.75 percent of 2.0 million); Lab 16.4 steps 1 and 3 (750; 1.9 times the fly; about a thirteenth, chapter says "less than a tenth"; 2.01 × 10^10; 241.5 GB). Errata section replaced with "Fixed in this edition: ..." and the remaining instructor notes; the "about a tenth" wording point removed (fixed).

## Skipped / no action
- audit_terms A1 (three-factor rule): Ch16:54 already uses the canonical "decides whether the change is kept".
- audit_numbers 2 and 3: Ch16 already uses 164 trillion and one in a hundred.
- audit_repetition A: no cuts proposed for Ch16 (A3 marks 54-62 and 90 as "keep, diagnostic"). No within-chapter cuts made.
- House style: no em dashes in prose, no British spellings; remaining numerals (2 percent, 3 to 5 percent, "a scale where 1 would be identical") are measurements/values. Epigraph attribution line kept (house format).
- Figure 16.1 caption and box already say "about two million"/"~2 million": no change. Figure Attribution "as examined in October 2026" left as is (the commit is given in the Note on Sources directly below).

## Build
`python3 docs/build.py Chapter16/` succeeded (docx and pdf for chapter and companion).

## Word count (body above "# References and Attribution", excluding image lines)
Before: 4,610. After: 4,611.
