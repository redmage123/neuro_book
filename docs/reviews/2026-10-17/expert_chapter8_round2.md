# Expert review, round 2: Chapter 8, Decision-Making Under Uncertainty

File: `docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md` (598 lines, revised)

Reviewer role: decision neuroscience, neuroeconomics, computational reinforcement learning, behavioral economics. Read-only review of the whole revised chapter, all 98 footnotes, `make_figures.py` and the seven figures.

## Overall assessment

Technical accuracy score: **5 / 5**

Every Major and Moderate finding from round 1 has been fixed, and the fixes are accurate.

- **Padoa-Schioppa and Assad (line 56).** Offer-value cells are now juice-specific, chosen-value cells are on a common scale, and taste cells are mentioned.
- **Normalization (line 62).** The neural result is cited to Louie, Grattan and Glimcher 2011. The behavioral claim is attributed as a proposal, the Gluth 2020 replication failure is given, and the decoy claim is gone.
- **LIP (line 42).** The paragraph is now two-sided, citing Steinemann 2024 and Jeurissen 2022.
- **Human habits (line 114).** Yin is described with interval schedules. Tricomi is given as three days, and de Wit's two direct replications are stated.
- **Arbitration (lines 116 to 118).** The account is now hedged, with Miller et al. 2019 and Akam et al. 2015.
- **Marshmallow test (line 96).** Kidd's n = 28 is given, Yanaoka 2026 is added, and the Watts sample is described.
- **Redish (line 140).** The account is followed by Panlilio 2007.
- **AI section (lines 146 to 150).** Updated with Graves, Minderer, Kadavath and Bellemare.

The round 1 Minor findings are also fixed. The cross-chapter wording now matches Ch3, Ch4 and Ch7, and Chapter 6 is linked through the SPRT as sequential Bayesian inference and through Ch6's saccades.

I checked the new material against primary sources, and it is accurate:
- **Rabin 2000.** Refusing −100/+110 at every wealth level implies refusing −1,000/+any amount. This is the paper's headline example.
- **Brown et al. 2024.** Their mean λ is 1.955 (95 percent interval 1.82 to 2.10) and the unadjusted median is 1.69, so "somewhat below two" is right.
- **Hertwig et al. 2004** (PubMed 15270998), **Hare et al. 2009** (19407204), **Niv et al. 2007** (17031711), **Williams and Williams 1969** (16811370) and **Frank et al. 2007** (17962524, "actually sped up their decisions under high-conflict conditions"): confirmed.
- **Lak et al. 2014** (25242219): "OFC inactivation disrupts waiting-based confidence reports without affecting decision accuracy". Confirmed.
- **Knoch et al. 2006** (17023614): right but not left DLPFC rTMS reduced rejection of unfair offers, and subjects "still judge such offers as very unfair". Confirmed.
- **Louie et al. 2011** (21775606) and **Churchland et al. 2008** (18488024), the latter for a "time-dependent rise in firing rates that may impose a deadline": confirmed.
- **Drugowitsch et al. 2012** and **Hawkins et al. 2015** (25673842): used as described.
- **Sozou 1998** and **Strotz 1955**: described correctly.
- **Pascal and Fermat, 1654**: correct.

The worked numbers are unchanged and still correct. The drift diffusion example gives a bound ratio of 2.59 and a time ratio of 5.19. The coin flip is worth 5 dollars on average, and prospect theory values it at about −32. The discounting reversal holds for k above 0.1 per day.

The remaining findings below are Minor. None affects the score.

## Major

None.

## Moderate

None.

## Minor

- **Line 124, recognition heuristic**: "About two thirds of the Americans, who knew both cities, answered correctly; every one of the Germans did".
  - **Figure.** The commonly cited figure from Goldstein and Gigerenzer (2002) is 62 percent of American students (University of Chicago) against 100 percent of German students. I confirmed this from secondary reproductions of the paper's figures; the publisher PDF was not retrievable. "About three in five" or "62 percent" is more exact than "about two thirds".
  - **Census.** San Antonio has since overtaken San Diego (2020 census: about 1.43 million against 1.39 million).
  - **Fix**: "About 62 percent of the Americans ... answered correctly (San Diego was then the larger city)".
- **Line 20 and footnote 1**: Devlin 2008 supports the Pascal and Fermat letters. The claim that the wager is "often called the first argument in decision theory" traces to Ian Hacking (1972, "The logic of Pascal's wager", *American Philosophical Quarterly* 9:186; also *The Emergence of Probability*, 1975). Add Hacking to the footnote.
- **Figure 8.2**: The figure still has the round 1 problems of scale; it is labeled illustrative, so this is optional.
  - **Ramps too slow.** The 51.2 percent ramp reaches the common level at about 710 ms, implying an RT near 780 ms against about 400 to 450 ms in Roitman and Shadlen. Doubling the slope term (`12 + 160 * c` to about `25 + 320 * c`) would fix it.
  - **Plateau.** Panel A plateaus at the common level, which motion-aligned averages do not do.
- **Figure 8.4 caption**: Panel B uses the gain parameter (γ = 0.61). Add "(for gains)" after "decision weights".

## What an expert would expect and is missing

Nothing essential. The round 1 list (Rabin, the description-experience gap, Hare et al., Niv et al., the Bayesian link to Ch6) has been added.

## Citation support check (new or changed footnotes)

- **Footnote 1 (Devlin 2008)**: supports the Pascal and Fermat letters; add Hacking for the wager (Minor).
- **Footnote 10 (Frank et al. 2007; Cavanagh et al. 2011)**: confirmed.
- **Footnote 11 (Drugowitsch et al. 2012; Churchland et al. 2008)**: supports the falling optimal bound and the LIP urgency signal.
- **Footnote 12 (Hawkins et al. 2015)**: supports "fixed bounds fit most ... as well or better".
- **Footnote 15 (Steinemann et al. 2024; Jeurissen et al. 2022)**: confirmed.
- **Footnote 17 (Lak et al. 2014)**: confirmed.
- **Footnotes 20, 21 and 26 to 28 (von Neumann and Morgenstern 1947; Padoa-Schioppa and Assad; Louie 2011 and 2013; Gluth et al.)**: confirmed.
- **Footnotes 35 and 36 (Tversky and Kahneman 1992; Rabin 2000)**: confirmed.
- **Footnotes 41 to 45 (Tom; De Martino 2010; Gal and Rucker; Brown et al. 2024; Hertwig et al. 2004)**: confirmed.
- **Footnotes 49, 50, 53 and 54 (Strotz and Ainslie; Sozou; Hare et al.; Miyazaki et al. 2014)**: confirmed.
- **Footnotes 55 to 58 (Mischel and Shoda; Watts et al.; Kidd et al.; Yanaoka et al. 2026)**: confirmed.
- **Footnotes 64 and 65 (Hayden, Kolling and Shenhav; Niv et al. 2007)**: confirmed.
- **Footnotes 68 to 73 (Yin; Tricomi and de Wit; Daw 2005; Miller et al.; Daw 2011 and Akam; Gillan)**: confirmed.
- **Footnotes 75 and 76 (Williams and Williams 1969; Dayan et al. 2006)**: confirmed.
- **Footnotes 77 to 79 (Simon 1955 and 1956; Goldstein and Gigerenzer 2002; Gigerenzer and Goldstein 1996)**: confirmed except the percentage (Minor).
- **Footnote 85 (Knoch et al. 2006)**: confirmed.
- **Footnote 90 (Panlilio et al. 2007)**: confirmed, and the gloss of blocking is correct.
- **Footnotes 93 to 97 (Graves; Guo; Minderer and Kadavath; Gal and Ghahramani; Bellemare)**: the bibliographic details are correct and the citations support the sentences.
- All other footnotes are unchanged from round 1 and support their sentences.

## Figures

- **Figure 8.6**: The revised caption ("an option tried 40 times and one tried twice") matches the panel A legend.
- **Figures 8.1, 8.3, 8.5 and 8.7**: correct, as in round 1.
- **Figures 8.2 and 8.4**: see Minor.

## Cross-chapter consistency

- **Ch8 line 40 versus Ch4 lines 104 and 108**: the STN is now "the relay of the hyperdirect path". Consistent.
- **Ch8 line 68 versus Ch7 line 168**: Fellows and Farah, "largely explained by a failure to reverse". Consistent.
- **Ch8 line 94 versus Ch3 line 106**: Ch8 gives the correlational firing in rats from Ch3 and the causal stimulation in mice separately. Consistent.
- **Ch8 line 138 versus Ch3 line 116**: Frank 2004 is now referred back to Chapter 3.
- **Ch8 line 140 versus Ch7 line 178**: the reward-hacking link is explicit and consistent.
- **Ch8 line 32 versus Ch6 line 128**: the link from the SPRT to Bayesian inference and saccades is correct and consistent.
- **Dopamine wording (line 66)**: matches the book-wide position.

## Sources consulted

- PubMed E-utilities: 25242219, 17023614, 21775606, 19407204, 17962524, 15270998, 17031711, 16811370, 11863042, 18488024, plus the round 1 set.
- Brown et al. 2024: https://www.aeaweb.org/doi/10.1257/jel.20221698 and https://healthcare-economist.com/2024/06/26/empirical-estimates-of-loss-aversion
- Recognition heuristic figures: https://www.slideshare.net/slideshow/gigerenzer/1449915 (reproduces Goldstein and Gigerenzer 2002); https://dlab.sauder.ubc.ca/sjdm/journal/11/rh15/rh15.html
