# Expert review, round 2: Chapter 9, Habits, Skills, and Automaticity

File: `docs/book/Word/Chapter9/How_the_Brain_Learns_Chapter_9_Habits_Skills_and_Automaticity.md` (revised)

Reviewer role: motor learning, basal ganglia and cerebellum, habit formation, skill acquisition, computational RL. Read-only review of the revised body, all new and changed footnotes, `make_figures.py` and all seven figures.

## Overall assessment

Technical accuracy score: **4.5 / 5** (round 1: 4)

Every round 1 Major and Moderate finding has been addressed, and the fixes are accurate:
- **Two-state model (line 44).** It is now scoped to spontaneous recovery and to some savings. Washout savings are attributed partly to explicit strategy, citing Zarahn 2008 and Haith 2015. Error-clamp trials are described correctly in the text and in Figure 9.2.
- **Wymbs (line 58).** Now three days, with concatenation in the putamen and segmentation in frontoparietal cortex. This matches the abstract.
- **Kerr and Booth (line 130).** The warm-up throws around the twelve-week program are now right, and Schmidt 1975 is added.
- **Yin 2009 (line 68).** Lesions before training; DMS impaired early and then caught up; DLS impaired throughout. The striatopallidal potentiation is included, and it matches the abstract ("preferentially expressed in striatopallidal neurons").
- **Hedges.** Instance theory (line 112, with Logan 1992), Wu and He (line 82), interference (line 156, Brashers-Krug), and Macnamara (line 124) are all hedged appropriately.
- **Smaller fixes.** Bengalese finches, implicit chain of thought, the Rubik's solver, the Knowlton caveat, and Chapter 8's framing at line 12 are all fixed.
- **New material is accurate.** Use-dependent learning (Diedrichsen 2010), Therrien 2016 (abstract checked), and Faure 2005 are correctly described.
- **Figure 9.4** now has three loops, the pallidum/SNr, and Haber's spiral drawn correctly: each striatal region projects to the dopamine neurons that serve the next loop.
- **Figure 9.1** reaches the machine floor and is labelled illustrative.
- **Figure 9.7** now says total time and random-order tests. **Figure 9.6** has readable y ticks and says "a fixed time".

Two sentences added in this revision misdescribe their sources (Jin 2014 at line 64, Smith and Graybiel 2013 at line 60). Fixing these two is all that separates the chapter from 5/5.

## Major (factually wrong, must fix)

- **Line 60: the citation now credits the striatum with what Smith and Graybiel found in cortex.** The text says: "later work tied the bracketing pattern to the point at which the run became insensitive to devaluation."
  - **What is wrong**: Smith and Graybiel (2013) found the opposite for the striatum. The abstract says the striatum "rapidly acquired an action-bracketing activity pattern insensitive to reward devaluation but sensitive to running automaticity". A similar pattern in the upper layers of the infralimbic cortex "formed only late during overtraining and closely tracked habit states". So striatal bracketing comes before the habit and does not mark it. The cortical bracketing is what coincides with devaluation insensitivity.
  - **Fix**: "Later work found that the striatal pattern forms early, before the behavior becomes insensitive to devaluation, and tracks how automatic the running is; a similar pattern appears in the infralimbic cortex only late in overtraining, just as the habit sets in." This also links neatly to the infralimbic paragraph at line 74.

- **Line 64: Jin, Tecuapetla and Costa did not find a division of labor between the two pathways.** The text says: "The two output pathways of the striatum ... appear to divide the work, one more involved in the elements within a sequence and the other in marking where a sequence begins and ends."
  - **What is wrong**: The abstract says the direct and indirect pathways "were concomitantly active during sequence initiation, but behaved differently during sequence performance, revealing a more complex functional organization of these circuits than previously postulated". The distinction the paper actually draws is between kinds of neuron, not between pathways:
    - start/stop neurons, which parse the sequence;
    - neurons with sustained or inhibited activity throughout the sequence, whose activity covaried with the rate of execution of its elements (concatenation).
  - **Fix**: "Jin, Fatuel Tecuapetla, and Costa later found, alongside the start and stop neurons, others whose activity stayed up or stayed down for the whole of a sequence, as if binding its elements together; both of the striatum's output pathways were active as a sequence began, and they differed only in how they behaved while it ran."

## Minor

- **Line 142 (Fleisher).** The facts check out against standard accounts and the memoir:
  - onset in 1964, at age 36;
  - the fourth and fifth fingers of the right hand;
  - roughly three decades of left-hand repertoire, teaching and conducting;
  - botulinum toxin and Rolfing in the 1990s;
  - *Two Hands* (Vanguard Classics, 2004) as his first two-handed album in about 40 years.

  One nuance: his recovery was partial and depended on continuing injections. "Did he begin to play with both hands again" is accurate as written; adding "though he still needed regular injections" would forestall the impression of a cure. (This is from secondary accounts; I have not checked the memoir's page text.)
- **Line 142, last sentence: a hypothesis stated as fact.** "The plasticity that enlarges a string player's finger map can, pushed further, merge the maps..." is the Byl–Merzenich hypothesis, and musician's dystonia also involves reduced cortical inhibition and a heritable predisposition. Say "may, pushed further, merge the maps".
- **Line 112: "correctly" is slightly strong.** Logan (1992) found the predicted joint power-law reduction of the mean and the standard deviation largely held, but later tests were mixed. Prefer "and in Logan's own tests it did".
- **Figure 9.1: the starting value is high.** It begins at 200 s per cigar, a 25-fold improvement to an 8 s cycle. That is high for Crossman's operators, but the figure is labelled illustrative and its shape now matches the text and caption. Acceptable as it stands.
- **Figure 9.4: one optional addition.** Haber's spiral also includes each striatal region's reciprocal projection to the dopamine neurons that serve it; the dashed arrows show only dopamine going to its own region. This is optional, because the caption describes what is drawn.

## What I verified this round

- **Against PubMed abstracts**:
  - Smith & Graybiel 2013: the source of the line 60 finding.
  - Jin, Tecuapetla & Costa 2014: the source of the line 64 finding.
  - Therrien, Wolpert & Bastian 2016: reward-based learning in cerebellar patients, fully retained. The text matches.
  - Faure et al. 2005: the citation details match. The description fits the paper as I know it, but I did not retrieve its abstract text.
  - Yin et al. 2009 (striatopallidal), Wymbs et al. 2012, Zarahn et al. 2008, Haith et al. 2015, He et al. 2016 and Brashers-Krug et al. 1996: all were checked in round 1 and are consistent with the revised wording.
- **References confirmed to exist and fit their sentences**: Diedrichsen et al. 2010, Logan 1992, Cowan 2001, Schmidt 1975, Gladwell 2008, and Fleisher & Midgette 2010.
- **Cross-references**:
  - Chapter 3: reward prediction error.
  - Chapter 4: climbing fibers, the two output pathways, basal ganglia selection.
  - Chapter 5: H.M., procedural memory, sleep, waking replay, catastrophic interference.
  - Chapter 6: prediction error in perception.
  - Chapter 8: TMS, explore/exploit, AlphaGo, arbitration, cost of thinking, de Wit.

  All point to content those chapters contain. The removed studies leave no dangling references in the text.
- **Figures**: all seven regenerated PNGs were viewed. Captions and figure numbers (9.5 song circuit, 9.6 instance race, 9.7 contextual interference) match the text.

## What would be needed for 5 / 5

1. Rewrite line 60 so that the devaluation-linked bracketing is attributed to the infralimbic cortex, not the striatum.
2. Rewrite line 64 so it describes Jin et al. 2014's sustained and inhibited "concatenation" neurons, without assigning parsing and concatenation to separate pathways.

The Minor items are optional and do not affect the score.
