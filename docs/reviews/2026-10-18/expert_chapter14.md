# Expert review: Chapter 14, Implications for Learning, Work, and Technology

File: `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md`

Reviewer role: computational neuroscience and machine learning, with learning science and human–automation interaction. I reviewed the source, `make_figures.py` and the figures, re-ran the two computed models (Figures 14.3 and 14.5), and checked the data figures against their sources. I checked quantitative claims against full texts where I could obtain them (Kuhl et al. 2003; Chang et al. 2015; Dunster et al. 2018; Bastani et al. 2025; Cepeda et al. 2008) and against abstracts (Roediger et al. 2011; Kornell et al. 2009; Wiehler et al. 2022; Bernstein and Turban 2018; Dahmani and Bohbot 2020; Parry 2024), plus the literature for the rest. I checked callbacks against Chapters 1 to 13.

## Overall assessment

Technical accuracy score: **4.5 / 5**

This is a careful applied chapter, and it is notably honest about replication. It takes the right line on every major dispute: learning styles; the Mozart effect; brain training; growth mindset; Ramirez and Beilock; media multitasking; "brain drain"; longhand against laptop notes; ego depletion; the hungry judges; the Google effect; GPS; and the social-media debate, from Orben and Przybylski against Twenge and Haidt to Allcott, Hunt, Braghieri, and Haidt against Odgers.

The numbers I could check are right, often to the decimal:

| Study | Figures checked |
|---|---|
| Kuhl et al. 2003 | 65.7% against 56.7% (SEs 2.40 and 2.29); 12 × 25-minute sessions over four weeks; completers 10 and 11 in Experiment 1, 15 and 13 in Experiment 2 ("about a dozen"); lower attention to the screen (AV 2.79 and audio 1.48 against live 3.53) |
| Cepeda et al. 2008 | 1,354 participants; 20–40% and 5–10% optimal gaps; "a 64% increase in final recall" |
| Chang et al. 2015 | 55% melatonin suppression; about 10 minutes longer to fall asleep |
| Dunster et al. 2018 | 7:50 to 8:45; 34 minutes more sleep; median grade 77.5% to 82% |
| Bastani et al. 2025 | nearly 1,000 students; 48% and 127% in practice; −17% on the exam, and the tutor arm null |
| Bernstein and Turban 2018 | about 70% |
| Dahmani and Bohbot 2020 | 50 drivers, 13 retested |
| Parry 2024 | k = 56; only working memory affected |
| From the literature | Rauscher, Chabris, Owen, Dekker, Newton and Salvi, Pashler, Rohrer (61% against 38%), Kornell and Bjork (61%, 35%, 78%, 78%), Yeager, Hagger, Vohs, Danziger, Woollett, Javadi, Budzyń, Orben, Allcott, Hunt, Braghieri |

Both computed models do what their captions say.

There is no Major error. Four Moderate items:
- one study is described backwards (Kornell, Hays and Bjork);
- the evidence ledger (Figure 14.7) places two claims in boxes that the chapter's own text does not support;
- one figure's axis exaggerates the differences (Figure 14.2);
- one set of classroom numbers I could not confirm (Roediger et al.).

## Major (factually wrong, must fix)

None.

## Moderate

- **Line 52: the Kornell, Hays and Bjork caveat is reversed.** "...found that the failed guesses improved later memory compared with simply studying the answer for the same period, though with time held strictly equal the guessing only matched study."
  - **What is wrong**: In Kornell et al. (2009) the guessing advantage held with time equated, in the word-pair experiments 3 to 6. The "only matched" result runs the other way: in Experiment 2, participants who guessed recalled *as many* items as participants given *more than twice as much time* to study the intact question and answer (as summarized by Hays, Kornell and Bjork). The abstract states plainly that "unsuccessful retrieval attempts enhanced learning with both types of materials."
  - **Fix**: "...found that the failed guesses improved later memory compared with simply studying the answer; in one experiment, guessing did as well as studying the answer for more than twice as long." To keep a caveat, the accurate one is that the benefit is clearest when the guess and the answer are meaningfully related (Grimaldi and Karpicke, 2012).

- **Figure 14.7 (evidence ledger) and lines 68 and 100: two claims are misplaced.**
  - **"A smartphone's mere presence draining the mind" is filed as "Not supported".** The chapter's own text (line 68) says the meta-analysis "found support only for a small effect on working memory". Parry's meta-analysis (k = 56, n ≈ 7,100) reports limited support for a negative effect on working memory, smaller than theorized. That belongs under "Small or disputed", or should be reworded as "a large, general 'brain drain' from a phone's presence".
  - **"AI tutors that guide rather than answer" is filed as "Supported, with caveats".** The evidence is one null exam result (Bastani's tutor arm did no better than controls) and one positive single-institution trial measured immediately after two lessons (Kestin). That is promising but thin. "Small or disputed", or a new "Promising, early" label, is fairer.
  - **Also**: The top box is titled "Strong, including classroom trials" and includes "the cost of switching between tasks", which is a laboratory finding. Either retitle the box "Strong (laboratory and classroom)" or move switching costs into a box with a fitting title.

- **Figure 14.2: the y-axis exaggerates the differences.** The axis starts at 45% (`ax.set_ylim(45, 75)`). With bars, a truncated axis makes the live condition look several times the others. Start at 0 or at 50 (chance, which the caption already marks). Alternatively, switch to points with error bars, which can legitimately use a truncated axis. The values are correct: live 65.7 and English 56.7 are from the text, and the others are approximately as read from the paper.

- **Line 40: the Roediger et al. (2011) numbers need confirming.** "On the chapter exams students got 94 percent of the quizzed material right and 81 percent of the rest, and at the end of the semester 79 percent against 67." The abstract confirms the design and the direction. I could not confirm the four percentages from the sources available to me. Check them against Tables 1 and 2 of the paper; Experiment 1 and Experiment 2 report different values.

## Minor

- **Line 94 (AF447).** "...it fell for more than four minutes into the sea." The BEA timeline runs about 4 minutes 23 seconds from autopilot disconnection to impact, and about 3.5 minutes from the stall onward. Since the sentence follows "entered a stall", use "it fell for three and a half minutes into the sea", or "less than four and a half minutes after the autopilot disconnected, it struck the sea".
- **Line 52 (callback).** "The midbrain region that contains dopamine neurons and ... the hippocampus, the circuit Chapter 3 described": Chapter 3 described dopamine but not the hippocampus–midbrain loop. Use "the dopamine neurons of Chapter 3 and the hippocampus of Chapter 5".
- **Line 54 (Yeager et al.).** "Did nothing for higher achievers": the trial also reported that the intervention increased enrollment in advanced mathematics in the full sample. "Did not raise the grades of higher achievers" is exact.
- **Line 76 (Wiehler et al.).** "Both groups reported feeling equally tired" is consistent with the paper (the fatigue markers in choice and pupil appeared only in the high-demand group). Consider adding "...although only the hard-task group's choices changed", which is the paper's main point.
- **Line 96 (Budzyń).** "Fell from 28.4 percent ... to 22.4 percent" is correct. The authors also note the result needs confirming. "The study was observational and short" covers this.
- **Line 130.** "A budget that Chapter 1 measured in watts" conflates the energy budget with attention. Attention is not measured in watts. Use "a budget whose deepest root, as Chapter 1 described, is energy".
- **Figure 14.3 (spacing model).** The re-run gives optimal gaps of 5.2, 7.5 and 18.4 days for tests at 7, 35 and 350 days, against Cepeda's 3, 8 and 27. The caption's "the model's curve is flatter than the data" is honest. Also say that the squares are Cepeda's *interpolated* optima, as the code comment does.
- **Figure 14.5 (automation model).** The re-run gives skill after one year of 0.96, 0.93, 0.71 and 0.31 for 0, 50, 90 and 99 percent automation, starting from 0.9. "Falls by more than half within a year" at 99 percent is correct. The figure is illustrative and the caption says so.
- **Figure 14.6.** The tutor's exam bar is drawn at 0. The caption correctly says "did not differ significantly". Consider showing the point estimate with its confidence interval rather than a zero bar.

## Copyedit

- **Line 12.** "A week or so later": Kuhl et al. tested after the exposure sessions over a period of days. "Shortly afterward" avoids implying a fixed delay.
- **Line 60.** "The start time moved by 55 minutes but sleep grew by only 34" is correct (7:50 to 8:45). Fine as is; flagged only because a reader may check it.
- **Line 41 (Danziger et al.).** "Almost none just before a break": the paper's figure shows near 0%. Fine.

## Figures

| Figure | Assessment |
|---|---|
| 14.1 (map) | The rows and chapter numbers are consistent with the text. |
| 14.2 (Kuhl) | The values are right; fix the truncated axis (see Moderate). |
| 14.3 (spacing) | Computed correctly and honestly captioned (see Minor). |
| 14.4 (Kornell and Bjork) | 61% against 35%, and 78% against 78%, as in Experiment 1a. Correct. |
| 14.5 (automation) | Computed correctly. |
| 14.6 (Bastani) | 48% and 127% in practice; −17% and null on the exam. Correct (see Minor). |
| 14.7 (ledger) | See Moderate. The groupings are otherwise fair. Teaching to learning styles, transferable brain training and quick-depleting willpower are correctly "Not supported". Growth mindset, exercise and the hippocampus, GPS, and media multitasking are correctly "Small or disputed". |

## Cross-references checked

These are accurate:
- Chapter 1: sensitive periods; the energy budget.
- Chapter 5: the forgetting curve, retrieval, spacing, sleep consolidation.
- Chapter 8: thinking as costly.
- Chapter 9: interleaving and contextual interference; habits; practice specificity.
- Chapter 10: calibration.
- Chapter 12: prediction errors.
- Chapter 13: supernormal stimuli.

These need a small fix:
- the dopamine–hippocampus "circuit Chapter 3 described" (line 52);
- the "watts" phrasing (line 130).

## Fairness on contested topics

The chapter's handling is a model for the book. Each claim gets its best evidence and its best rebuttal:
- the growth-mindset meta-analyses on both sides (line 54);
- Ramirez and Beilock, with the original authors' reply (line 54);
- media multitasking and "brain drain" (lines 68 and 69);
- longhand notes (line 70);
- glutamate fatigue, with Möller's critique (line 74);
- ego depletion, including Vohs's own multi-lab test (line 76);
- the hungry judges, with both critiques (line 76);
- the Google effect (line 86);
- GPS, labeled suggestive (line 88);
- Kosmyna, labeled preprint, small and contested (line 100);
- social media, with Orben against Twenge, the experiments, and Haidt against Odgers, ending in a careful summary (line 110).

The only imbalance is in the ledger figure (see Moderate).

## What would make it a 5

1. Correct the Kornell, Hays and Bjork description (line 52).
2. Move "mere presence" and "AI tutors that guide" to the boxes the text supports, and retitle or re-sort the "Strong" box (Figure 14.7).
3. Fix the truncated axis in Figure 14.2.
4. Confirm the four Roediger et al. percentages against the paper.
5. Correct the AF447 duration.
