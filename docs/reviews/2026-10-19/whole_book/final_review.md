# Final copy-and-fact review: How the Brain Learns

Scope: all uncommitted `*.md` hunks (34 files, about 2,300 diff lines), the new glossary (237 entries, now 236 after one merge), and a scan of the Instructor's Answer Key for internal references.

## Summary

- Problems found: 22
- Fixed directly: 14 (3 in chapters, 1 in a companion file, 5 in the answer key, 5 in the glossary, some of them covering several entries)
- Left for the author: 8
- `check_footnotes.py` was run on both edited chapters (3 and 10). It reported no problems.

## Verified and correct (no action)

Every callback added in this round was checked by grepping the target chapter. All of the following point to the right chapter:

- Ch1 "Chapters 3 and 6"; Ch2 Golgi, Attwell and Laughlin, Lennie, Thorpe, and Sterling and Laughlin all point to Ch1
- Ch5 synaptic scaling points to Ch1 homeostatic plasticity
- Ch6 Hubel and Wiesel and the sensitive period point to Ch1; Ch6 "local sense, argued in Chapter 3" (Ch3 line 84)
- Ch8 deep brain stimulation of the subthalamic nucleus points to Ch3
- Ch8 "section on the cost of thinking" points to "Thinking Is Costly", which gives the adversarial and changing-world reasons
- Ch10 "Chapters 1 and 5" for McCloskey and Cohen
- Ch11 Behrens points to Ch8, and Doya points to Chs 3 and 7
- Ch12 Yu and Dayan point to Ch6 (footnote 32 there); thermodynamic free energy points to Ch0; Behrens points to Chs 8 and 11
- Ch13 synaptic failures point to Chs 1 and 2; basal ganglia point to Chs 3, 4, 8, and 9; "round 20 watts of Chapter 1"
- Ch14 Bainbridge's "last irony" (the antecedent is in the same chapter); attention points to Ch6
- Ch15 Bliss and Lømo point to Ch2
- Ch16 elastic weight consolidation points to Chs 9 and 11

Other items confirmed:

- New numbers are consistent:
  - well over 100 trillion synapses (Ch1), 164 trillion in the neocortex (Ch4, Tang 2001)
  - homeostatic scaling "a day or more" (Ch1) and "a day or two" (Ch5)
  - early LTP "an hour or two" (Chs 5 and 15)
  - eligibility trace "seconds to minutes" (Chs 3 and 16)
  - 516 kcal is about 25 W (Ch13 and Lab 13.6)
- These lab checks were recomputed and are correct:
  - Lab 1.4: 30.7 and 45.95; 1.82, 2.345, and 1.0; break-even at 29.5
  - Lab 13.2: 2,657 µm; ten crossings give 167 ms
  - Lab 13.4: insect ordering
  - Lab 13.5: w = 1.5 gives F, D, B (w = 1 gives an F/H tie, so the change was right)
  - Lab 14.1: R = 0.375
  - Lab 8.x: d = 10 gives 0.105, 0.137, 0.152, and 0.151
  - Lab 9.x: 0.499
  - Lab 16.2: 750 synapses per neuron, 3.9e10 and 1.25e12, 172 steps
  - Lab 16.4: 2.0e10 synapses, 241 GB
- House style: no em dashes and no British spellings in any added line or in the glossary.
- Front matter: Contents titles match every chapter's `subtitle`.

## Problems fixed

1. **Ch10, The two most developed answers.** After the rewrite, "with bursts at the apical dendrites ... carrying the error" made burst-dependent error signaling look like part of the random-feedback (feedback alignment) mechanism. These are two separate proposals. Changed to: "One is Chapter 3's: a backward pathway with random, fixed weights ... and bursts at the apical dendrites ... that carry the error ...".
2. **Ch10, Sorted this way.** In "an honest estimate of what it knows", the antecedent of "it" was lost in the cut. Changed to "what one knows".
3. **Ch3, acetylcholine paragraph.** "Chapter 5" appeared twice in one clause ("the deep stage of sleep that Chapter 5 describes, favors recall ... that Chapter 5 connects"). Removed the first.
4. **Ch3 and companion Ch3, credit assignment.** The callback was changed from "Chapters 5 and 6" to "Chapters 10 and 11", but Ch6 does return to the question: its predictive coding versus backprop passage at line 162, which Ch10 also cites. Changed to "Chapters 6, 10, and 11" in both files.
5. **Answer key: internal revision language removed.**
   - "Design note (not an erratum):"
   - "the lab now applies"
   - "(script check: ...)"
   - "(matches the corrected check)"
   - "as the lab now states"
   - "Instructor notes (not check errors):"
   - "as the lab now specifies"

   No "audit", "this edition", or script filenames remain. The Lab 16.5 title "Auditing a Mechanism" is legitimate content.
6. **Glossary, Action potential.** It was cited to Chapter 1, but the mechanism and propagation are explained in Ch2. Changed to Chapter 2.
7. **Glossary, Homeostatic plasticity.** It said "over hours and days", which contradicts Ch1 as revised ("over a day or more"). Aligned it with Ch1.
8. **Glossary, duplicate entries.** "Genome bottleneck" (Ch13) and "Genomic bottleneck" (Ch10) were two entries for one concept. Merged them into "Genomic bottleneck (genome bottleneck)" (Chapters 10 and 13).
9. **Glossary, near-duplicate names.** "Prediction error (sensory)" (Ch6, predictive coding) and "Sensory prediction error" (Ch9, motor) meant different things under nearly the same name. Renamed the Ch9 entry "Sensory prediction error (in motor adaptation)" and added a cross-reference.
10. **Glossary, Transfer.** "Large studies ... found no transfer, even to closely related tasks" contradicted Ch14's Simons review ("less on closely related ones"), which is also quoted in the Brain training entry. Reworded to separate the single study (Owen) from the review.
11. **Glossary, missing chapter tags.** Eight entries held over from the old front-matter glossary had none, although the glossary header promises a chapter for every entry. Added:
    - Axon, Dendrite, Neuron, Threshold, and Excitation: Ch2
    - Circuit and Inhibition: Ch4
    - Prediction: Ch12

## Left for the author

1. **Ch3 epigraph (Henry Dale).** The title, date (12 December 1936), and the gist of the opening ("first became an experimental reality in 1921", crediting Loewi) are confirmed by a search summary. nobelprize.org returned 403, so I could not confirm the quoted sentence word for word, including the comma after "impulses". Check it against the printed lecture.
2. **Front-matter Cajal epigraph source.** The new attribution reads *Reglas y consejos sobre investigación científica* (preface to the second edition, 1898). Early editions carried the title *... investigación biológica*, and the dating of the second edition (1898 or 1899) should be checked against the edition you cite.
3. **Contents lists "Bibliography" and "Index".** Neither exists in `docs/book/Word`; each chapter has its own references. Either add them or drop the lines.
4. **Glossary, entries still without a chapter tag.** Behavior, Cognition, and Stability have no single obvious home chapter, so I left them for you to assign.
5. **Ch3, "Little changes for long unless the context says it should."** This is grammatical but awkward. It is quoted verbatim in companion Lab 3.4 step 7, so changing it means changing both files.
6. **Ch14, attention.** "Attention, which Chapter 6 described as the weighting of evidence by its reliability" states as fact what Ch6 presents as the predictive-coding proposal. The companion was hedged in this round. Consider "which Chapter 6 treated as".
7. **Minor style points.**
   - Ch7 "only three of 12 healthy volunteers" mixes a spelled-out number and a numeral. It follows the one-to-ten rule, but some editors keep both numerals in a direct comparison.
   - Prose now spells "Kording" while some reference entries keep "Körding" as published. That is fine, but the choice is now deliberate.
8. **Other items.**
   - The glossary `.docx` and other `.docx`/`.pdf` builds need regenerating from the edited markdown. I did not touch them.
   - The glossary cites LTP to Ch2, where it is introduced; Ch5 explains it most fully. This is your choice under the header's "introduced or most fully explained".
