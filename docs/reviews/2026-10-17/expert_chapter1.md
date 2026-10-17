# Expert review: Chapter 1, What the Brain Is (and Is Not)

File: `docs/book/Word/Chapter1/How_the_Brain_Learns_Chapter_1_What_the_Brain_Is.md`

## Overall assessment

Technical accuracy score: **4 / 5**

This is a framing chapter with few checkable claims, and the ones it makes are mostly right and well cited (von Neumann 1945, Hodgkin and Huxley, Allen and Stevens on synaptic failure, Shadlen and Newsome on variability, Jacob on tinkering, McClelland et al. on slow cortical learning). The one substantive problem is a causal claim about why learning is slow that the biology does not support and that Chapter 5 later contradicts. The remaining issues are attribution and hedging.

## Major (factually wrong, must fix)

- None.

## Moderate (misleading or outdated, should fix)

- **Line 46**: "Learning is slow because molecular change is slow." The molecular events of plasticity are fast: NMDA-receptor-dependent LTP is induced by one second of stimulation and is expressed within a minute or two; AMPA receptor insertion takes minutes (Malinow and Malenka 2002, cited in Chapter 5); one-trial fear conditioning and one-shot hippocampal learning exist. Chapter 5 (lines 158 to 160) gives the correct reason: slow cortical learning is a design requirement to avoid interference, and fast learning is quarantined in the hippocampus. Suggested: "Learning that must not disturb what is already stored is slow, because ...". As written the sentence is wrong and the book contradicts it later.
- **Line 14 and footnote 2 (line 176)**: "Over the last seventy years, the language of computation has become the dominant way of speaking about minds" with Dartmouth 1955 as the origin. The computational vocabulary for the brain predates Dartmouth: McCulloch and Pitts 1943 ("A logical calculus of the ideas immanent in nervous activity"), Wiener's Cybernetics 1948, Turing 1950, and von Neumann's 1945 EDVAC report itself (which borrows "neurons" from McCulloch and Pitts). The footnote should name McCulloch and Pitts as the start of the vocabulary; Dartmouth is the start of "artificial intelligence" as a field.

## Minor (imprecise wording)

- **Line 24**: "Noise is an enemy to be suppressed." True of engineered digital logic, but von Neumann himself (1956, "Probabilistic logics and the synthesis of reliable organisms from unreliable components") designed for noisy components, and the brain-versus-computer contrast is softer than the paragraph implies. A clause acknowledging this would strengthen rather than weaken the argument.
- **Line 48 and footnote 10**: "Plasticity compensates for damage.[^10]" cites Turrigiano and Nelson 2004, a review of homeostatic plasticity in development. It does not address compensation for injury. A better source would be a review of post-lesion plasticity (for example Nudo 2013, Front. Hum. Neurosci. 7:887) or Murphy and Corbett 2009, Nat. Rev. Neurosci. 10:861.
- **Line 74 and footnote 15**: "the objective of this system is not truth in the abstract. It is viability.[^15]" cites Friston 2010 (free-energy principle). The free-energy principle is contested as a theory and is not primarily a claim about viability over truth; Ashby 1952 and Maturana and Varela (autopoiesis) are the sources for the viability framing. Footnote 13 already cites Ashby; move the viability claim there.
- **Line 82**: "Synapses sometimes fail to transmit." Correct, and the footnote at line 48 (Allen and Stevens 1994) is the right source; here the claim is cited to Shadlen and Newsome 1998, which is about spike-count variability, not synaptic failure. Consider citing Allen and Stevens at both places.
- **Line 88, Figure 1.3 caption / line 112 attribution**: Caption says Cajal's drawings "established neurons as discrete, branching cells"; the attribution identifies the drawing as a Purkinje cell from human cerebellum (1899). Both are correct; the image shows the Cajal Institute stamp. Consider adding "(Golgi stain)" since the chapter has not yet explained how such drawings were possible.
- **Line 102**: "Chapter 2: Neurons --- The Brain's Signaling Cells" matches Chapter 2's subtitle. (Chapter 2's own "Next Chapter" line does not match Chapter 3's subtitle; see the Chapter 2 report.)

## Citation support check

Footnotes 1, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17 and 18 support the sentences they are attached to. Footnote 2 (origin of computational vocabulary), footnote 10 (damage compensation) and footnote 15 (viability) are weak fits, as noted.

## Figures

Figure 1.1 (von Neumann architecture) and Figure 1.2 (midsagittal MRI) are correctly described. No simulated data in this chapter.
