# Lab errata found while writing the answer key (apply to the companion file of the chapter; then update scratchpad key_chN.md to match)

Chapter 1
- Lab 1.4 Part B: with the given numbers, waiting is cheaper (expected cost 0.445 vs 1.82 act-now vs 1.0 always-flee), contradicting the intended "reflexes trade accuracy for speed" lesson; waiting stops paying only for delay cost above about 29.5 units. Adjust the numbers (e.g., delay cost) so that the intended trade-off appears, recompute, and give check values. See key_ch1.md errata.
Chapter 2
- Labs 2.1/2.2: no scenario reaches threshold (best -68.0 mV), so every spike question answers "no spike"; the "time step 5 ms" parameter is unused. Either add a scenario that does cross threshold (e.g., many synchronous inputs) or make explicit that the lesson is how far single inputs are from threshold; remove or use the unused parameter. Recompute any check values.
Chapter 3
- Lab 3.2 step 3: "below 0.01" -> "at or below 0.01" (at 3 s delta_w is exactly 0.0100).
- Companion line ~10 "Chapters 1 and 2 gave you a neuron" -> "Chapter 2 gave you a neuron" (see audit_xref.md); companion ~79 "Chapters 5 and 6 return" -> "Chapters 10 and 11 return".
Chapter 4
- Lab 4.3 optional code extension: stone at step 150 makes the symmetric model lock into a two-step cycle; move the stone to step 145 (verify by running the model) or warn about lockup.
- Lab 4.3 step 4: with fatigue 0.2 the rhythm stops (L settles at x = 0.5); rephrase the question so it does not presume the rhythm survives ("does the rhythm survive?" is ok; make sure no wording implies only the period changes).
- Lab 4.1: state that the model has no reset after a spike ("spike" = threshold crossing).
Chapter 5
- Lab 5.5 step 3: check w = (0.476, -0.223) -> (0.477, -0.223).
- Lab 5.3 step 5: STDP window undefined at dt = 0; state the convention (no change at dt = 0).
Chapter 9
- Lab 9.6 step 3: at five presses habit drive is 0.499, so R narrowly wins rather than ties; adjust wording if it says tie.
Chapter 10
- Lab 10.7 step 1: "eleven properties in Figure 10.7" -> "thirteen properties".
Chapter 11
- Companion figure numbers wrong: chapter has 11.4 = memory-systems map, 11.5 = Horowitz energy chart, 11.6 = surrogate gradients, 11.7 = homeostatic reward. Fix Student Notes (Horowitz 11.4->11.5; surrogate 11.5->11.6; homeostatic 11.6->11.7; memory map 11.7->11.4) and Lab 11.1 Purpose (11.4->11.5), Lab 11.4 Purpose (11.6->11.7). Verify against chapter captions.
Chapter 13
- Lab 13.5 step 4: at w = 1, F and H tie at 96; change to w = 1.5 (F alone at 92) or state the tie; recompute checks.
- Lab 13.2 step 1: bare axon at 50 m/s with coefficient 0.97 needs 2,657 µm, not 2,648 (fix check).
- Lab 13.2 step 4: "ten passes back and forth" ambiguous; say "ten one-way crossings" (167 ms) and keep the comparison with 200 ms.
- Lab 13.4 step 3: check lists values in reverse order of steps 1-2; reorder.
Chapter 14
- Lab 14.2 step 3: "If the two ... groups were independent" is wrong; reword: "Knowing nothing about how the two 78 percent groups overlap, what is the smallest possible share..." (answer 56 percent stands).
- Lab 14.7 step 2: "use Figure 14.1" -> "use Figure 14.2".
- Lab 14.1 step 1: R at 30 days is 0.375 -> print 0.38 (or 0.375).
Chapter 16
- Network size: NIMCP is about 2.0 million neurons (1.8M + 200K), not 2.2 million (companion lines ~116, ~150; Figure 16.5 in Chapter16/make_figures.py plots 2.2e6: change to 2.0e6 and regenerate the figure, view the PNG). Synapses per neuron about 750 (1.5e9 / 2.0e6), not 682. Lab 16.3 answers become "about 750, 391, and 10,061" and "about 2.0 x 10^10 synapses; about 241 GB" (recompute). Companion ~121 uses 28 spikes/s where the chapter's early rate is 26; align.
- Chapter 16 text line ~92 "about a tenth of the connections of a cortical neuron": with 750 vs 10,061 that is about a thirteenth; change to "less than a tenth".
- Lab 16.1 step 3: expected background trace depends on assumed history; state the assumption in the lab (background firing from step 0) or accept ranges; align with key.
