# Expert review, round 2: Chapter 16, NIMCP: Building a Brain from the Book's Principles

File: `docs/book/Word/Chapter16/How_the_Brain_Learns_Chapter_16_NIMCP.md` (revised)

Reviewer role: computational neuroscience and machine learning. This round is a read-only review of the passages changed since round 1, re-checked against the NIMCP repository. That included `TRAINING_ALERT.txt`, commit 4693efd32, `checkpoints/snapshot_prod_full_20260505` and its `chat_eval_log.jsonl`. Nothing was built, run or modified.

## Overall assessment

Technical accuracy score: **5 / 5** (round 1: 4)

The round 1 Major item is fixed, and every Moderate and Minor item is resolved and checks out against the repository.

- **"Ambient domination" (line 86).** It is now presented as the design notes present it: a readout problem in which the background of about 15,000 spikes per step swamps the neurons carrying the prompt. It is tied to the runaway-firing excess, to sparse coding and attentional gain control (Chapter 6), and to the missing sequencing mechanism (Chapter 9). Credit assignment is now a separate, correctly scoped paragraph (line 88): it limits what the spiking core can learn, while backpropagation on borrowed targets does most of the learning. The Central Lesson is consistent with this.
- **The learning rule (lines 54 and 84).** The decay applies to co-active synapses only, reward strengthens co-active inhibition, and the runaway paragraph now names both brakes: reward-driven strengthening of inhibition onto overactive neurons, and homeostatic scaling capped at 2% per step. This matches `snn_rstdp_apply`.
- **Firing alerts (line 76).** You were right that my round 1 count missed the main source. `TRAINING_ALERT.txt` has 38,090 "firing rate very high" lines, ranging from 100.1 to 908.6 Hz. Of these, 32,986 are the stale 834.2 Hz value, and the first is 877.3 Hz on 25 April. "Roughly 800 to 900 spikes a second ... after late June the same reading simply repeated, a stale value" is accurate. My 4,008 came from `monitoring.log`, which covers only October.
- **The remote machine (line 76).** `TRAINING_ALERT.txt` records "[CRITICAL] Pod ... unreachable" from 26 June 17:40 onward (32,979 lines), so "became unreachable" is supported.
- **Out-of-memory kills (line 76).** The message of commit 4693efd32 (18 October) says "Batch size 12 still OOM'd on 56GB pod (kill #39)". "Killed dozens of times" is accurate and appropriately general.
- **21 GB (line 42).** `du` gives 21 GB for `checkpoints/snapshot_prod_full_20260505`.
- **The opening scene (line 12).** It is verified. The `chat_eval_log.jsonl` entry timestamped 5 May 2026 records "What color is the sky?" → "ball beside eye Look! The ball is beside the eye. ...", with a mean similarity of 0.0245, which supports the "0.02" at line 72. "At other checkpoints that month ... the same string of words to every one" matches the three May evaluations with one distinct answer.
- **Other round 1 items.**
  - The 26 Hz network is now credited to a variant of backpropagation (line 42).
  - "Pyramidal neurons" for the 10% variability (line 24).
  - The README "claims" (present tense).
  - "Scale is probably not the main obstacle" (line 92).
  - The basal ganglia are "partial", with the precise wording about habits registered during training (line 48 and Figure 16.2).
  - The test-suite sentence is removed.
- **The new closing paragraph (line 118).** The microprocessor mirror is apt, and the Box epigraph is correctly sourced: *Empirical Model-Building and Response Surfaces*, p. 424.

## Major (factually wrong, must fix)

None.

## Minor (optional, does not affect the score)

- **Line 12.** The logged response continues after "The ball is beside the eye.": "A round bouncy ball you can throw and catch and an eye that sees the world in all its color and detail." Add an ellipsis to the quotation ("...The ball is beside the eye. ...") so the truncation is marked. The continuation is itself informative, since it is a lexicon gloss, the kind of output the chapter attributes to borrowed components (line 32).
- **Line 88.** "The spiking network can learn little that is specific to any task" is still stated as a finding; it is an inference from the rule's structure. "Can probably learn little..." or "is unlikely to learn much..." would match the chapter's hedging elsewhere.

## What I verified this round

- **`TRAINING_ALERT.txt`.** Firing-alert count, range and stale value; the "unreachable" lines.
- **Commit 4693efd32.** The message records kill #39.
- **The checkpoint directory.** Its size.
- **`chat_eval_log.jsonl`.** The opening exchange and the mean similarity.
- **The revised rule description.** Re-read against `nimcp_snn_training.c`, about lines 890 to 965.
- **The ambient-domination paragraph.** Checked against `docs/claude/snn-language-generation-design.md`.

## What would be needed for 5 / 5

Nothing further. The chapter meets the bar.
