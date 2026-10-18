# Expert review, round 2: Chapter 14, Implications for Learning, Work, and Technology

File: `docs/book/Word/Chapter14/How_the_Brain_Learns_Chapter_14_Implications_for_Learning_Work_and_Technology.md` (revised)

Reviewer role: computational neuroscience and machine learning, with learning science and human–automation interaction. This round is a read-only review of every passage changed since round 1, the regenerated figure code, the footnotes, and the order of figure citations.

## Overall assessment

Technical accuracy score: **5 / 5** (round 1: 4.5)

All round 1 Moderate and Minor items are resolved.

- **Kornell, Hays and Bjork (line 60).** The text now says "failed guesses improved later memory ...; in one experiment, guessing did as well as studying the answer for more than twice as long." That matches the paper's abstract and Hays, Kornell and Bjork's summary of Experiment 2.
- **Figure 14.7 (ledger).** It is re-sorted fairly:
  - "Strong (laboratory and classroom)" now honestly includes switching costs.
  - "A phone's presence (at most a small effect)" and "AI tutors that guide rather than answer (early)" sit under "Small, disputed, or early", consistent with Parry's meta-analysis and with Bastani's null tutor exam effect plus Kestin's short trial.
  - The Mozart effect and "longhand notes beating laptop notes" are correctly "Not supported". The replications found no advantage for longhand.
  - "Infants learning from partners who respond (small studies)" is correctly hedged.
- **Figure 14.1 (Kuhl, renumbered).** The y-axis now starts at 0, with chance marked at 50. The values are unchanged and correct: 65.7 and 56.7 with SEs from the text, the others read approximately.
- **Roediger et al. (2011) (line 46 or thereabouts).** You report that the full text confirms 94% against 81% and 79% against 67% in Experiment 1, and that Experiment 2's advantage over restudy fades by semester's end. Both are consistent with the abstract. Accepted.
- **AF447 (line 108).** "About three and a half minutes" matches the BEA timeline from the stall onward.
- **The remaining fixes are all accurate:**
  - the Chapter 3 and Chapter 5 callback (line 60);
  - Yeager's mindset trial (line 62);
  - the Wiehler clause (line 88);
  - "an effect size of 0.04" (line 90);
  - the "watts" phrasing removed;
  - the Figure 14.3 caption ("interpolated from the data of Cepeda et al.").

The new material is also accurate:
- **Allcott et al. 2020 (line 130).** The framing is correct: willingness to accept was elicited for four weeks of deactivation around the 2018 midterms; participants who would accept $102 or less were randomized; the treatment group was paid to deactivate, and compliance was verified by checking that accounts stayed deactivated. The results that follow are correct: about an hour a day, less polarization, less news knowledge, and about 0.09 SD on subjective well-being.
- **The Sparrow, Liu and Wegner attribution (line 98).** It now correctly separates the search-engine priming claim, which failed in the SSRP replication, from the memory-for-saved-information claims, which were not tested there.
- **The closing sentence of the engagement paragraph (line 126).** It is a fair use of Chapter 13's beetle, framed as a risk rather than a finding.
- **Kuhl in the Central Lesson (line 160).** "Learned from a voice that answered them, and not from the same voice on a screen that could not" is consistent with Kuhl et al. and with the Roseberry and Lytle follow-ups the chapter cites.

## Major (factually wrong, must fix)

None.

## Minor (optional, does not affect the score)

- **Line 160 (Central Lesson).** "From learning styles to brain training to a smartphone's mere presence, have weak or no support" is consistent with the re-sorted ledger, where phone presence now shows "at most a small effect". "Weak" covers it. If you want the two to match exactly, use "...to the idea that a phone's mere presence drains the mind".
- **Line 84 (open offices).** "Perhaps to protect the limited attention this section has described" is a fair, hedged interpretation. Bernstein and Turban themselves describe the result as social withdrawal rather than attention protection, so "perhaps" is the right word.

## What I verified this round

- **Footnotes.** There are 68 markers, numbered monotonically. Every marker has a definition, and there are no unused definitions.
- **Figure citations.** Figures 14.1 to 14.7 are first cited in order (14.1 at line 14, 14.2 at line 24, and so on), and the attribution paragraph matches the new numbering.
- **Figure code.** `fig_kuhl` now uses `set_ylim(0, 80)` with a chance line at 50. The `LEDGER` contents match the text's verdicts. The computed Figures 14.3 and 14.5 are unchanged since my round 1 re-run.
- **Revised sentences.** These were checked against the sources consulted in round 1: Kornell et al. (2009) abstract and Hays et al.'s summary; Kuhl et al. full text; Parry 2024; Bastani et al. full text; Allcott et al. design.

## What would be needed for 5 / 5

Nothing further. The chapter meets the bar.
