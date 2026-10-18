# Expert review, round 2: Chapter 12, The Brain as a Predictive, Adaptive System

File: `docs/book/Word/Chapter12/How_the_Brain_Learns_Chapter_12_The_Brain_as_a_Predictive_Adaptive_System.md` (revised)

Reviewer role: computational neuroscience and machine learning (predictive coding, efficient coding, RL, Bayesian models, the free-energy literature). This round I re-read the whole revised chapter and verified each newly introduced study against its abstract or full text where I could obtain it. I also checked the regenerated Figures 12.1 and 12.6 against the code and checked the footnote apparatus.

## Overall assessment

Technical accuracy score: **5 / 5** (round 1: 4.5)

All six round 1 Moderate items are fixed, and each is now accurate:

- **Powers et al. (line 90).** The paper now gets a tone-responsive auditory region plus an insula/ACC network resembling the clinical hallucination regions, which is consistent with the paper's circuit description (see Minor for one check).
- **Active inference and epistemic value (line 132).** This is now stated fairly (Friston et al. 2015). The Millidge et al. (2021) critique is accurately softened: expected free energy "cannot simply be derived ... as the free energy of the future, and its exploratory part does not follow directly". That is their argument.
- **Isomura et al. (line 124).** The Hebbian caveat is there.
- **Körding et al. (line 104).** The savings claim now matches Chapter 9 (line 44).
- **Light from above (line 106).** The Chapter 6 repeat is now a one-clause callback, and the slow-speed prior replaces it. Snowden et al. 1998, Stocker and Simoncelli 2006 and Sotiropoulos et al. 2011 are correctly described, and the Pretto et al. 2012 realistic-fog caveat is a nice touch. Vallortigara et al. is kept.
- **N400 (line 66).** The prediction-against-integration debate is now stated, with Nieuwland et al. 2018 (nine labs, 334 participants, noun cloze effect replicated, article effect not).

The round 1 Minor items are also fixed:
- **Line 112.** "Computable" upper bound.
- **Line 122.** Westerberg is set against Keller ("the evidence may depend on the kind of prediction that is violated"), which is a fair reading.
- **Callbacks, all now accurate:**
  - place cells in Chapter 4 (line 56);
  - Chapters 5 and 10 (line 14);
  - synaptic scaling in Chapter 5 (line 100);
  - the delta rule beneath Chapter 3's TD (line 74);
  - Yu and Dayan as Chapter 3's account (line 78);
  - Sterling's allostasis in Chapter 7 (line 36).
- **Figure 12.5 caption.** It now says the learner knows the hazard rate and the noise, and "best fixed rate" is right: my round 1 grid search gave 23.1 at rates 0.5 to 0.6.
- **Figure 12.6.** The sensory-adaptation bar now runs from 10 ms to about 5 min.
- **Figure 12.1.** The hippocampus error cell is softened to "departure from the expected path (proposed)".

The substantive additions I asked for are in and accurate:
- **Palmer et al. 2015 (line 50).** This matches the abstract: "nearly every cell in the retina participates in a group of cells for which this predictive information is close to the physical limit".
- **Chalk et al. 2018.** Accurate.
- **Bowers and Davis 2012, with Griffiths et al.'s reply (line 84).** The paragraph's judgment that the adaptive learning rate "survives the critique better than most, because it predicts something a fixed-rate learner does not" is exactly the right standard.
- **Momennejad et al. 2017.** The reward- against transition-revaluation asymmetry and the hybrid conclusion are right.
- **Garvert et al. 2017.** Accurate.
- **Stahl and Feigenson 2015 (line 132).** Eleven-month-olds; the ball through the wall, which they banged, and the unsupported car, which they dropped. Accurate.

The literary additions are also accurate:
- **Land and McLeod 2000 (line 28).** Three batsmen of differing skill, a predictive saccade to the bounce point, and the latency of the first saccade distinguishing good from poor batsmen.
- **McGuire et al. 2014.** Surprise and uncertainty influences on learning rate in separable regions.
- **Stoffregen et al. 2013 (line 98).** A Caribbean voyage (Bahamas to Dominica); stance changed within the first hours. 19 of 24 participants (79%) reported mal de débarquement for 30 minutes or less, and 5 (21%) for 120 minutes or more. The long-duration group had swayed more at sea. "About one in five" is exact.

At about 6,570 words the chapter is now in the book's range, and the length was added where it was needed: on both sides of the "one principle?" question.

## Major (factually wrong, must fix)

None.

## Moderate (overstated, contested, or misleading)

None.

## Minor (optional, does not affect the score)

- **Line 76 (chronology).** "In a later version of the task ... [McGuire 2014] ... In a later study the same group found that the size of people's pupils..." The pupil study (Nassar et al., 2012) predates McGuire et al. (2014). Reorder the two sentences, or change the second to "In an earlier study...".
- **Line 28.** "Followed it for a fifth of a second after it landed": the abstract gives 100 to 200 ms. "For up to a fifth of a second" is exact.
- **Line 106 (Pretto).** "Real fog hides distant objects more than near ones and has the opposite effect, so that drivers in it slow down." Pretto et al. tested *simulated* fog that reduced contrast with distance as real fog does, not drivers in real fog. Use "Fog that, like real fog, hides distant objects more than near ones has the opposite effect in the simulator..."
- **Line 106 (Sotiropoulos).** "Trained people for five days": I could not confirm the number of sessions from the supplementary material. It reports learning across sessions, with the shifted prior persisting for at least a week afterward. Check the count against the main text, or use "over several sessions".
- **Line 90 (Powers).** "Raised activity in the auditory regions that responded to real tones": the abstract describes only "a brain circuit that mediated the conditioned hallucinations". Confirm against the paper's Figure 3 that the overlap with tone-responsive auditory cortex is reported as such. If it is not, use "raised activity in auditory cortex, along with a network...".
- **Line 148 (fourth AI point).** "A large model is trained on one loss, with a second, for human preferences, added at the end" simplifies. Current pretraining often adds auxiliary losses, such as load balancing in mixtures of experts and multi-token prediction, and post-training now includes reinforcement learning on verifiable rewards as well as preferences. Use "...is trained mostly on one loss, with a few others added for particular purposes, chiefly at the end". The question the paragraph poses is good.

## Figures

- **Figure 12.1**: The rows match the chapters, and the hippocampus error cell is now marked "(proposed)".
- **Figures 12.2 to 12.5**: The code is unchanged since my round 1 re-run (ratio 5.3; 3.32 against 2.32 bits; fields extend backward under one-way running; RMS errors 35.8, 23.1 and 20.3). The captions match.
- **Figure 12.6**: The sensory-adaptation bar is extended to about 5 minutes, consistent with line 46 (rate adaptation over a minute, power-law tails).
- **Figure 12.7**: Unchanged and correct.

## Cross-references checked this round

All callbacks are now accurate:
- Chapter 1: Ashby.
- Chapter 3: delta and TD; Yu and Dayan; norepinephrine.
- Chapter 4: place cells.
- Chapters 5 and 10: replay and forward sequences.
- Chapter 5: synaptic scaling.
- Chapter 6: predictive coding; light from above; the clinical accounts; efference copy.
- Chapter 7: allostasis; anticipatory regulation.
- Chapter 8: confidence.
- Chapter 9: fast and slow processes; savings.
- Chapter 10: language models; DreamerV3; the forgetting network.
- Chapter 11: Behrens; curiosity.

Chapter 6 overlap is now limited to deliberate one-line callbacks.

## What I verified this round

- **Footnotes.** There are 62 markers, numbered monotonically. Every marker has a definition, and there are no unused definitions.
- **Against abstracts or full text**:
  - Palmer et al. 2015.
  - Powers et al. 2017 (abstract).
  - Stoffregen et al. 2013 (full text: 19/24 and 5/24, sway greater in the long-duration group).
  - Land and McLeod 2000 (abstract via secondary sources).
  - McGuire et al. 2014 (abstract).
  - Stahl and Feigenson 2015.
  - Sotiropoulos et al. 2011 (supplementary material).
- **From the literature, consistent with the text**:
  - Chalk et al. 2018.
  - Momennejad et al. 2017.
  - Garvert et al. 2017.
  - Nieuwland et al. 2018.
  - Bowers and Davis 2012, and Griffiths et al. 2012.
  - Snowden et al. 1998, and Pretto et al. 2012.
  - Stocker and Simoncelli 2006.
  - Friston et al. 2015, and Millidge et al. 2021.

## What would be needed for 5 / 5

Nothing further. The chapter meets the bar. The Minor items are small accuracy refinements, and two of them are checks against the source text (Sotiropoulos's session count, Powers's Figure 3).
