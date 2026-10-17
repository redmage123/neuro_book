# Literary Review: Chapter 5, "Plasticity and Memory: How Experience Becomes Structure"

Source: `docs/book/Word/Chapter5/How_the_Brain_Learns_Chapter_5_Plasticity_and_Memory.md` (558 lines; body ends at line 182, about 6,500 words of body text, 10 figures)

## Overall assessment

What works: this is the strongest chapter in the manuscript. The argument climbs from a single protein (the NMDA receptor as a molecular AND gate) through synapse, whole cell, ensemble, two consolidation systems, sleep, reconsolidation and forgetting, and at every level there is an experiment, a date and a number. It pays off promises made in Chapters 1-4 explicitly (the "same door" opening at line 12; "no reset button" at line 160; Chapter 4's deferred hippocampal plasticity; Chapter 3's third factor), and the complementary-learning-systems section says outright that it is "the most important idea in this chapter for readers from machine learning" and then proves it. The sentences have snap: "Memory is not something the brain has. It is something the brain's tissue has become"; "A record that changes when read is a bad database. It is a good adaptive system"; "Nothing is stored. Everything is rebuilt." The AI section's five points are each distinct and each anchored in the biology just described.

What does not work: only small things. One historical date sentence is wrong or at best ambiguous, one relative clause does not agree with its antecedent, one anatomical figure is never cited from the text, one forward reference depends on a term Chapter 3 never actually uses, the opening roll-call omits Chapter 0, one phrase date-stamps the book, and two spellings disagree with Chapter 6. At 6,500 words of body it is the longest chapter and earns the length, though the "Kinds of Memory" paragraph and the STDP mechanism sentence would both benefit from being split. Prose quality: 5/5. Reader interest: 5/5.

## Findings

### Major (must fix before publication)

- **Line 54.** "LTP was first measured in the hippocampus in 1973; LTD was established in the cerebellum in 1982 and in the hippocampus a decade after LTP." Read literally, "a decade after LTP" is 1983; hippocampal LTD was established in 1992 (Dudek & Bear; Mulkey & Malenka, both in the references), two decades after LTP. Rewrite: "LTD was established in the cerebellum in 1982 and in the hippocampus a decade after that, in 1992."
- **Line 90.** "Chapter 3 described a three-factor rule: a synapse changes when it was recently active, when its neuron fired, and when a neuromodulatory signal arrives" Chapter 3's body text never uses the term; it occurs only in the caption of Figure 3.8. Fix in Chapter 3 (see that report). If Chapter 3 is not changed, rewrite here: "Chapter 3 described, without naming it, a three-factor rule".

### Minor (should fix)

- **Line 12.** "Every chapter so far has ended at the same door. Chapter 1 said ... Chapter 2 said ... Chapter 3 said ... Chapter 4 said ..." Chapter 0 is omitted. Either add "Chapter 0 said that a cell is a membrane doing continuous work" or accept, with the book-level decision, that Chapter 0 is a primer outside the sequence.
- **Line 20.** "Seventy-five years later the list of things that can change is long." Dates the book to 2024. "Three quarters of a century later".
- **Line 44.** "Most fast excitatory transmission uses AMPA receptors: glutamate binds..." Neither AMPA nor NMDA is glossed. Add one clause: "two kinds of glutamate receptor, each named for the laboratory chemical that activates it".
- **Line 72.** "The window is set by the kinetics of the NMDA receptor: a back-propagating spike that arrives while glutamate is still bound expels the magnesium and admits a large calcium pulse; one that arrives before the glutamate finds the receptor closed, and the glutamate that follows meets a membrane that has already repolarized, producing only a small, slow calcium signal." Seventy words. Split after "calcium pulse." and begin the second sentence "A spike that arrives before the glutamate finds the receptor closed; the glutamate that follows then meets a membrane that has already repolarized and produces only a small, slow calcium signal."
- **Line 84.** "Because the scaling is multiplicative, the ratios between synapses, which is where the learned information lives, are preserved" The relative clause does not agree with "ratios". Rewrite: "Because the scaling is multiplicative, the ratios between synapses are preserved, and the ratios are where the learned information lives."
- **Line 100.** "Neurons that are active during a learning event can be labeled genetically and later made to fire with light." Name the technique; this readership will know the word: "made to fire with light, a technique called optogenetics."
- **Line 104 (Figure 5.6).** The limbic-anatomy figure is never referenced in the text. Add "(Figure 5.6)" at line 96 after "in the hippocampus and amygdala", or cut the figure.
- **Line 116.** "The fast one trains the slow one gradually, by replaying its contents interleaved with everything else" "Everything else" is vague. "interleaved with the cortex's existing knowledge".
- **Line 140 (caption).** "Retention after a single exposure (gray)" Chapter 6 uses "grey" three times (lines 14, 76, 78). Standardize to American "gray" book-wide.
- **Line 152.** The paragraph from "Episodic and semantic memory" to "leaves no structural trace" is 130 words covering four memory systems. Split after "...without any episode being recalled."
- **Line 158.** "Chapter 1 promised that learning is slow because physical change is slow." Chapter 1 line 46 says "molecular change is slow". Quote it accurately: "because molecular change is slow".
- **Line 172.** "Artificial systems mostly have no equivalent to deliberate, selective forgetting." There is a literature on machine unlearning and on pruning. Hedge: "Artificial systems have only crude equivalents of deliberate, selective forgetting."

### Nit (optional)

- **Line 36.** "which the first computational models exposed in the 1970s" The references cited are Oja (1982) and Bienenstock, Cooper & Munro (1982); von der Malsburg (1973) is not listed. Either add the 1973 reference or write "in the early 1980s".
- **Line 62.** "This is the first of the chapter's two consolidation clocks." Good foreshadowing; keep.
- **Line 102.** "Recall is a dynamical event, not a lookup." Good; keep.
- **Line 134.** "A record that changes when read is a bad database. It is a good adaptive system" Good; keep.
- **Line 154.** "The amnesic patient H. M." with a space; the references use "H.M." Choose one.
- **Line 160.** "Slowness is the price of not overwriting yourself, which, for a system without a reset button, is the price of staying coherent." Good callback to Chapter 1 line 56; keep.
- **Line 182.** "Chapter 6: Perception as Inference --- How the Brain Sees What It Expects" matches Chapter 6's subtitle; no change.

Counts: Major 2, Minor 12, Nit 7.
