# Expert review: Chapter 16, NIMCP: Building a Brain from the Book's Principles

File: `docs/book/Word/Chapter16/How_the_Brain_Learns_Chapter_16_NIMCP.md`

Reviewer role: computational neuroscience and machine learning (spiking networks, plasticity rules, NeuroAI). I reviewed the chapter, `make_figures.py` and the figures, and re-ran the Figure 16.3 simulation. I spot-checked the chapter's claims against the NIMCP repository, read-only, at `/home/bbrelin/nimcp`: nothing was built, run or modified. I read the source files named in the brief, the evaluation JSONs, the probe and cosine logs, `monitoring.log`, `sync_checkpoint.log` and `logs/brain_daemon.log`, and the design notes in `docs/claude/`.

## Overall assessment

Technical accuracy score: **4 / 5**

This is an unusual and valuable chapter: an author holding his own system to the book's standard, with disclosure, code-first sourcing, and a diagnosis organized by the book's own model. The tone is right. It is neither promotional nor harsh, it credits what is faithful to biology, and it proposes concrete tests.

Most factual claims about NIMCP check out exactly against the repository:

| Claim | Verified against |
|---|---|
| 1.8M neurons in 46 populations | `TIER_DEFS` in `nimcp_snn_hierarchical.c`: 46 populations, 1,800,000 neurons |
| Connectivity of 0.02–0.5% | the same table: 0.0002 to 0.005 |
| About 1.5 billion synapses | my estimate from the tier table is about 1.44 billion, before interneuron and skip connections |
| 20 ms membrane time constant; threshold 15 mV above rest | `tau_mem = 20`, `SNN_V_GAP 15` |
| AMPA, NMDA and GABA receptors; PV, SST and VIP classes with a disinhibition chain | the hierarchical SNN code |
| The substrate "has no concept of 'region'" | quotation verified |
| Hypothalamus set points of 37 °C and 90 mg/dL; "Setpoints ARE the reward function" | the hypothalamus source |
| The Claude parent prompt, "a loving, warm parent raising a child" | `immerse_athena.py:4428` |
| The Phi-3 decoder | `scripts/phi3_decoder.py` |
| The 150,000-unit conventional network | `DEFAULT_ANN_NEURONS` |
| The 768-neuron network at 26 Hz with 67% silent | `EMERGENT_SPIKING_DYNAMICS.md` |
| 1 to 33 distinct answers to 50 questions in May; "grand gel telephotography..." | the eval JSONs: 2, 19, 1, 1, 1, 22, 33, 21, 21 across checkpoints |
| Intent fidelity of 1/20 in every probe; "INTENT-MISS COLLAPSE" | all four 29 May probe logs |
| Within-category similarity below between-category; "reset recommended" | `cosines_1836.log`: +0.014 against +0.031 |
| Ethics harm estimated from confidence | `nimcp_brain_part_core.c`: `predicted_harm = confidence < 0.5 ? 0.5 : 0` |
| The LGSS rules are symbolic and hash-locked | `LGSS_core_rules.json` and `nimcp_lgss.c` |

Figure 16.3 reproduces its caption: selectivity of about 21 at short delays for both rules; about 1 for the coincidence rule beyond the cue; 8.95 and 4.07 for the trace rule at delays of 5 and 10.

There is one Major item: the chapter's central diagnosis cites the project's own "ambient domination" note as describing a credit-assignment failure, but the note describes something else. Several Moderate items concern the learning-rule description and the evidence for runaway firing.

## Major (factually wrong, must fix)

- **Line 80: the "ambient domination" note is misattributed to credit assignment.** "The collapse of the network's output onto a few phrases is the failure of credit assignment that Figure 16.3 illustrates. ... The project's own design notes describe exactly this, under the heading of 'ambient domination'..."
  - **What is wrong**: `docs/claude/snn-language-generation-design.md` defines ambient domination as a *readout* failure: "the full net's ~15k spikes/step swamp the seed's ~8-neuron projection; a fixed set of high-ambient pops ('thoriated', 'urbanized', 'anisotropy') wins regardless of prompt." That is a signal-to-noise problem at decode time, driven by excessive ambient activity. It is far closer to the chapter's runaway-firing diagnosis (Chapter 4 inhibition, Chapter 5 homeostasis) than to the learning rule.
  - **A second problem**: the chapter itself says (line 54) that the biological rule runs only every tenth step, at a small learning rate, and is switched off when the gradient trainer is active, and that "most of the learning ... is done by backpropagation". It is therefore not safe to attribute output collapse mainly to the SNN's coincidence rule.
  - **Fix**: "The collapse of the network's output onto a few phrases has at least two plausible causes in the book's terms. The project's own design notes trace it to what they call 'ambient domination': the activity of the whole network, some 15,000 spikes in each step, swamps the few neurons that carry the prompt, so that a fixed set of highly active populations wins whatever was asked. That is the runaway excitation of the previous paragraph, seen at the output. The credit-assignment problem of Figure 16.3 may add to it: a rule that strengthens whatever is active when reward arrives will tend to strengthen the most active patterns further. The notes add two problems of a different kind: the system has no mechanism for sequencing words, and 'word order is not encoded anywhere.'"
  - **Also**: Change the Central Lesson (line 108) to match: "collapsed output is what happens when the activity of the whole network drowns the signal it is meant to carry, and credit assigned without eligibility traces may make it worse."

## Moderate

- **Line 52: the learning rule is described incompletely, in a way that matters for the diagnosis.** "A synapse is strengthened only when the neurons on both sides spike in the same time step, by an amount proportional to how much better the current reward is than its running average, and all weights decay slightly."
  - **What is wrong**: In `snn_rstdp_apply` (`nimcp_snn_training.c`, about lines 890 to 965):
    - The decay term (`decay_rate = 1e-5`) is applied only to synapses that were co-active, not to all weights.
    - Inhibitory synapses that are co-active become *more* inhibitory under positive reward (`delta = -scale - decay·w`).
    - There is rate-dependent inhibitory strengthening: inhibitory synapses onto a neuron whose rate EMA exceeds 0.10 are pushed more negative (`delta -= 0.1·(rate - 0.10)`).
    - Weights are clipped to [−4, 2].

    The last point is a local inhibitory-plasticity brake, beyond the homeostatic scaling mentioned at line 78. The runaway diagnosis should acknowledge that it exists and still did not contain the activity. Note too that `brain_daemon.log` (2 June) records "SNN runaway protection (natural saturation) IS NOT ACTIVE", which supports the diagnosis.
  - **Fix**: "...by an amount proportional to how much better the current reward is than its running average, and those synapses also decay slightly; inhibitory synapses are strengthened by the same signal, and more strongly onto neurons that are firing too fast."
  - **Also**: At line 78 add: "...NIMCP has homeostatic scaling and a local rule that strengthens inhibition onto over-active neurons, but..."

- **Line 70: the evidence for runaway firing needs restating.** "Monitoring logs recorded tens of thousands of alerts that the spiking network's firing rate was far too high, with rates between 100 and more than 900 spikes a second..."
  - **What is wrong**: In the repository, `monitoring.log` contains 4,008 such alerts (5 to 19 October), and every one reports the same value, 834.2 Hz, while the step counter stays at 60,718 to 60,719. They are repeated readings of one stale status, not thousands of independent measurements. The "tens of thousands" figure and the 100 to 900 Hz range may come from logs on the remote machine or older rotated logs. If so, cite them. If not, rewrite.
  - **Fix** (if no other source): "Monitoring logs repeatedly reported a firing rate of over 800 spikes a second in the network's last saved state, against the 26 of the early small network, and a June log records that the network's protection against runaway excitation was not active."

- **Line 40: the 26 Hz network was trained by backpropagation.** "...an early version of the spiking network, with 768 neurons, settled on its own into firing about 26 times a second among its active neurons..."
  - **What is wrong**: `EMERGENT_SPIKING_DYNAMICS.md` reports that this network was "trained via backpropagation through time (BPTT) with surrogate gradients" alongside five other networks. "On its own" is fair (there was no rate regularizer). But the sparsity emerged under gradient training, not under the biological rules, and that matters for statement 2.
  - **Also**: 26 Hz among the active third is well above typical cortical mean rates. Chapter 1's "one in a hundred" concerns how many neurons are active at once, not rate.
  - **Fix**: "...settled, without any term in its training asking for it, into firing about 26 times a second among its active neurons, with about two-thirds silent at any moment. That sparsity resembles cortex, although it arose under gradient training rather than the biological rules."

- **Line 84: hedge the scale conclusion.** "Scale is not the obstacle; organization is." This is the chapter's inference, not a measured result. The chapter's own figures show 1.5 billion synapses against the neocortex's 164 trillion, and about 700 synapses per neuron against about 10,000. "Scale alone is probably not the obstacle; the bee shows how much a small, well-organized brain can do" is better supported.

- **Line 44 and Figure 16.2: the basal ganglia are partly wired.** "...a basal ganglia module ... It is never called when the system makes a decision." The decision claim is consistent with what I found: no external caller of action selection. But `nimcp_training_integration.c` (about lines 143 to 610) does call `basal_ganglia_register_habit`, `check_habit`, `get_habit_strength`, `strengthen_habit`, `get_rpe` and `get_dopamine` during training, to register and strengthen per-domain habits. Figure 16.2's "present, not wired" is therefore slightly too strong. Use "partial (habits recorded during training; not used to select actions)", or add that clause to the text.

## Minor

- **Line 22: the 10% variability applies to pyramidal neurons only.** "Neurons differ from one another by about 10 percent in their time constants and thresholds." The code applies σ = 0.10 to pyramidal tier populations only; PV, SOM, VIP and TRN interneurons have σ = 0 (`nimcp_snn_hierarchical.c`, about lines 334 to 340). Use "Pyramidal neurons differ...".
- **Lines 26 and 72: the README still makes the claim.** "...the 'trillions' that the project's introductory material once claimed." `README.md` (lines 8 and 77) still says "trillions". Use "claims".
- **Line 70: "unreachable" may be inaccurate.** "Training stopped in late June 2026, when the remote machine on which it ran became unreachable." `sync_checkpoint.log` shows that from 26 June onward the checkpoint was "not found on RunPod — skipping", which implies the machine answered but the file was gone. Use "when the run on the remote machine ended and its checkpoint disappeared", unless another log shows the host was unreachable.
- **Line 70: two claims I could not find in the repository.** "...repeatedly killed for exceeding the machine's memory, the 39th time on 18 October" and "more than 26,000 registered tests ... fewer than 200 ... nearly half failing". I found no log with an OOM count or the 39th kill (`monitoring.log` and `sync_checkpoint.log` contain no kill records), and no test-run log. The `test/` CMake files contain about 1,500 `add_test` calls, though tests may be registered in other ways. Cite the files these came from (the logs on the remote machine or the CTest output), or soften.
- **Line 40: "about 21 gigabytes".** I did not find this figure in the files I read. Cite the source (a checkpoint size or memory log).
- **Line 54: the tenth-step cadence needs a citation.** "The biological rules run alongside, every tenth step..." I found a `% 10` cadence at `immerse_athena.py:4973` (interaction count). Confirm that this is the cadence of the biological rules and cite it in the footnote.
- **Line 60.** "What the parent cannot supply is contingency" is a fair use of Roseberry et al. and Lytle et al. (Chapter 14). Since the parent's narrations are pre-generated, "cannot" is right for those; the scripted critic does respond, in a rule-based way. Consider "can supply only rule-based contingency".
- **Line 108.** As well as the Major fix, "slow learning from a random start is what happens without the structure that evolution and development supply" is reasonable as framed by Chapters 10 and 13, but it is stated as established. Use "...is what the book would predict without...".

## Copyedit

- **Line 14.** The "Neuro-Inspired Modular Control Protocol" expansion: confirm against the README, which I did not see expanded in the lines I read.
- **Line 38.** "Blood glucose of 90 milligrams per deciliter": correct. The code also has an oxygen-saturation set point of 98%, which you could mention for completeness.

## Figures

- **Figure 16.1 (architecture).** It is consistent with the text and the code: the hybrid of the spiking network and the conventional networks, the bridges, the algorithmic "regions", and the LLM parent and Phi-3.
- **Figure 16.2 (status).** See the basal ganglia item. The other rows match the text.
- **Figure 16.3 (credit toy).** The code matches the caption. The re-run selectivity values are below.

  | Delay (steps) | Coincidence rule | Trace rule |
  |---|---|---|
  | 0 | 21.1 | 21.1 |
  | 1 | 20.7 | 20.9 |
  | 2 | 21.5 | 21.1 |
  | 3 | 0.8 | 14.4 |
  | 4 | 0.7 | 10.9 |
  | 5 | 1.3 | 9.0 |
  | 7 | 1.0 | 6.1 |
  | 10 | 1.4 | 4.1 |

  The text's "factor of nine after five steps and four after ten" is exact. One nuance: in NIMCP the reward is computed per training step from the loss, while spikes are per SNN time step, so the real "delay" is many SNN steps. That strengthens the figure's point.
- **Figure 16.4 (measurements).** Panel A's distinct-answer counts match the eval JSONs. Panel B's 1/20 matches all four probes. Consider noting in the caption that the probes also report outputs that were *diverse* (16 to 19 unique out of 20) but unrelated to the intent, which is a different failure from panel A's collapse.
- **Figure 16.5 (scale).** The counts are consistent with Chapters 13 and 15. Synapses per neuron:

  | System | Synapses per neuron |
  |---|---|
  | Fly | about 390 |
  | NIMCP | about 680 (1.5 billion over 2.2 million) |
  | H01 | about 9,300 |
  | Human neocortex | about 10,000 |

  "About a tenth of the connections of a cortical neuron" (line 84) is right to within the rounding; it is closer to a fifteenth. The honeybee count of 1 million is shown as a neuron count only, which is fine.

## Fairness

The chapter is fair to the project:
- It credits genuine biological fidelity: conductance synapses with Mg-block NMDA, the interneuron motif, and homeostasis.
- It quotes the author's own candor ("I don't know if this approach is better than scaling transformers").
- It treats the safety architecture as structurally right but thin, with specific and verifiable reasons.
- It proposes small, decisive experiments rather than verdicts.

The one fairness problem runs in a surprising direction. The chapter's diagnosis is more confident and more neatly mapped onto the book's model than the evidence allows: the ambient-domination misattribution, "scale is not the obstacle", and the Central Lesson's "is what happens when". Hedging these makes the chapter's argument, that failures cluster where the theory predicts, more credible, not less.

## What would make it a 5

1. Correct the "ambient domination" attribution and the Central Lesson's corresponding sentence (lines 80 and 108).
2. Describe the actual R-STDP rule, including inhibitory strengthening and the rate brake, and acknowledge it in the runaway diagnosis (lines 52 and 78).
3. Re-source or rewrite the firing-alert claim (line 70). In the repository it is 4,008 repeats of one stale value.
4. Note that the 26 Hz result came from backpropagation through time (line 40), and mark the basal ganglia as partial (Figure 16.2).
5. Cite or soften the unverified operational figures: the 39th OOM kill, the test counts, 21 GB, and "unreachable".
