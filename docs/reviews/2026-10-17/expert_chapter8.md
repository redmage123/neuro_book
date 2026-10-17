# Expert review: Chapter 8, Decision-Making Under Uncertainty: How the Brain Chooses When It Cannot Be Sure

File: `docs/book/Word/Chapter8/How_the_Brain_Learns_Chapter_8_Decision_Making.md`

Reviewer role: decision neuroscience, neuroeconomics, computational reinforcement learning, behavioral economics. Read-only review of the chapter source, `make_figures.py` and all seven figures.

## Overall assessment

Technical accuracy score: **4 / 5**

This is a strong chapter. Its coverage is the one a specialist would choose: perceptual accumulation, value, risk, time, exploration, goal versus habit, effort and computation, social choice, and psychiatry. Most of the specific claims are right, and I checked the ones that carry numbers against abstracts or original tables:
- Roitman and Shadlen 2002: ramps, and a common level about 70 ms before the saccade.
- Newsome, Britten and Movshon 1989; Salzman et al. 1990.
- Kiani and Shadlen 2009: the opt-out "sure target".
- Resulaj et al. 2009.
- Fleming et al. 2010: anterior prefrontal gray matter.
- Latimer et al. 2015: roughly three quarters of neurons fit the stepping model better.
- Katz et al. 2016: LIP inactivation had no effect, MT inactivation impaired.
- Cavanagh et al. 2011: STN DBS reversed the theta-threshold relation and produced impulsive choice.
- Tversky and Kahneman 1981: 72 and 78 percent.
- Tversky and Kahneman 1992: lambda 2.25, alpha 0.88, gamma 0.61.
- Tom et al. 2007.
- De Martino et al. 2006 and 2010 (two patients).
- Hsu et al. 2005.
- McClure et al. 2004; Kable and Glimcher 2007.
- Watts et al. 2018: half the size, reduced by two thirds with controls.
- Kidd et al. 2013: N = 28; about 12 versus 3 minutes, so "about four times" is right.
- Daw et al. 2006; Wilson et al. 2014; Behrens et al. 2007; Hayden, Pearson and Platt 2011; Kolling et al. 2012.
- Daw et al. 2011; Gillan et al. 2016.
- Sanfey et al. 2003.
- Henrich et al. 2001: means from 0.26 to 0.58.
- Frank et al. 2004.
- Weintraub et al. 2010: 13.6 percent and OR 2.72.
- Camille et al. 2011 (GARP violations); Bartra et al. 2013 (206 studies).

The three worked examples are arithmetically correct, and they agree with the figure code:
- **Drift diffusion example, line 52**: with drift 0.582 and unit noise, P(correct) = 1/(1+e^(-2va)) and mean decision time = (a/v)tanh(va). 70 percent needs a = 0.728, with a decision time of 0.50 s. 90 percent needs a = 1.888, with a decision time of 2.60 s. The bound ratio is 2.59 ("about two and a half times") and the time ratio is 5.19 ("about five times"). Because tanh(va) is exactly 0.4 and 0.8 at these accuracies, the time ratio is the bound ratio times two.
- **Coin flip, line 64**: 0.5 × 110 − 0.5 × 100 = 5 dollars. With the 1992 parameters, prospect theory values this gamble at about −32, so it also predicts refusal.
- **Discounting, line 76**: 110/(1+31k) > 100/(1+30k) holds for every k ≥ 0, and 100 > 110/(1+k) holds for k > 0.1 per day. The example works for any sufficiently steep hyperbolic discounter. Figure 8.5 uses k = 0.2, and the curves cross on day 25.

Most contested positions are presented well. The common currency (Levy and Glimcher against Hayden and Niv), one versus two discounting systems (McClure against Kable and Glimcher), the size of loss aversion (Gal and Rucker) and human habits (de Wit et al.) are all given two sides. The dopamine wording follows the book-wide position ("a large population of midbrain dopamine neurons").

The problems are:
- one cited study whose central finding is misdescribed (Padoa-Schioppa and Assad's offer-value neurons are juice-specific);
- two places where the evidence on one side is presented without its strongest counter-evidence:
  - divisive normalization: a preregistered replication failed;
  - LIP: the 2022 to 2024 work answers the stepping and inactivation challenges;
- the human-habit paragraph, which cites Tricomi et al. as a positive result although two of de Wit's five failures were direct replications of it, and which misdescribes Yin et al. 2004;
- the marshmallow and addiction paragraphs, which state as settled two accounts that have each had a key prediction fail;
- an AI section that describes 2017-era systems as current;
- a handful of history and attribution slips.

## Major (factually wrong, must fix)

- **Line 24**: "Many neurons fired in proportion to the value of an offer in the monkey's own exchange rate, whatever the juice, and others to the value of the option the monkey eventually chose."
  - **What is wrong**: Padoa-Schioppa and Assad found three main classes of OFC neurons:
    - "offer value" cells, which encode the value of one particular juice (offer value A or offer value B) and so are juice-specific;
    - "chosen value" cells, which encode the value of whatever was chosen, in a common unit, independent of juice;
    - "taste" cells, which encode the identity of the chosen juice.

    The sentence attaches "whatever the juice" to the offer-value cells, which are the ones that are not juice-independent. The common-scale property that the section rests on comes from the chosen-value cells.
  - **Evidence**: The abstract (PubMed 16633341) says neurons "encode the value of offered and chosen goods" independently of visuospatial and motor factors. In the paper, offer-value responses are defined per juice, and chosen value is the variable expressed in common units (Padoa-Schioppa and Assad 2006, Figs. 2 and 3; also Padoa-Schioppa 2011, Annu. Rev. Neurosci. 34:333).
  - **Suggested rewrite**: "Some neurons fired in proportion to the value of one particular juice on offer. Others fired in proportion to the value of whichever option the monkey chose, whatever the juice, measured in the monkey's own exchange rate: a signal on a common scale. Still others signaled which juice had been chosen."

## Moderate (misleading, outdated, or contested presented as settled; should fix)

- **Line 28**: "Kenway Louie, Mel Khaw, and Glimcher showed that this is divisive normalization ... It helps explain why adding a decoy can change what people choose."
  - **What is wrong**:
    - **Replication failure omitted.** The behavioral distractor effect has failed a preregistered direct replication. Gluth, Kern, Kortmann and Vitali (2020, Nat. Hum. Behav. 4:634, PubMed 32015490) "could not replicate the distractor effect" in two preregistered experiments. They attributed what remains to value-based attention, and the original group replied (Webb, Louie and Glimcher 2020). "Showed that this is" therefore overstates the case.
    - **Wrong source for the neural result.** The shrinking of value signals in neurons comes from LIP recordings (Louie, Grattan and Glimcher 2011, J. Neurosci. 31:10627). The 2013 PNAS paper is mainly modeling plus behavior.
    - **Decoy effect overclaimed.** Simple divisive normalization predicts less consistent choice, not the classic attraction (decoy) effect, in which the target is chosen more often. Explaining that effect needs extensions such as pairwise normalization (Landry and Webb 2021).
  - **Suggested rewrite**: "Kenway Louie, Paul Glimcher and colleagues found that value signals in parietal neurons are divisively normalized, ... and proposed that the same computation makes choices depend on context. Whether an irrelevant third option really makes people less consistent is disputed: a preregistered replication did not find the effect. Variants of normalization have been proposed to explain decoy effects."

- **Line 54 (LIP challenge)**: "Kenneth Latimer and colleagues ... found that many LIP neurons were better described as jumping ... Leor Katz and colleagues silenced LIP ... LIP carries a signal that looks like accumulation, but it may be reading out a decision made elsewhere."
  - **What is wrong**: Only the 2015 and 2016 challenges are given. The replies and newer data are missing, so the paragraph is not two-sided, which the book's standard for contested positions requires:
    - Latimer drew two technical comments in Science (2016, 351:1406).
    - Simultaneous recordings from hundreds of LIP neurons now show a single-trial population signal that combines drift and diffusion and explains choice and RT variability (Steinemann, Stine, Trautmann, Zylberberg, Wolpert and Shadlen 2024, eLife 12:RP90859, PubMed 39422555).
    - LIP inactivation does produce choice and RT deficits that are then compensated within and across sessions (Jeurissen et al. 2022, Neuron 110:1924, PubMed 35421328). This offers a reading of Katz et al. other than "LIP is irrelevant".
  - **Suggested rewrite**: append "Later work has pushed back. Recordings from hundreds of LIP neurons at once show a population signal that drifts and diffuses on single trials as the model requires, and LIP inactivation does impair decisions at first, before other areas compensate. LIP may be one of several areas that hold the running total."

- **Line 100**: "Henry Yin, Barbara Knowlton, and Bernard Balleine found that rats with lesions there stayed goal-directed even after extended training. In people, Elizabeth Tricomi and colleagues found that several days of overtraining made responding insensitive to devaluation ... Sanne de Wit and colleagues reported five attempts that failed".
  - **What is wrong**:
    - **Yin et al. 2004 misdescribed.** The study did not use extended training. It used interval schedules, which produce habits at ordinary training lengths (abstract: "Interval schedules of feedback have been shown to generate habits"; PubMed 14750976).
    - **The replication record is understated.** de Wit et al. included "two independent attempts to replicate the original demonstration", which is Tricomi et al. 2009 (PubMed 29975092). Presenting Tricomi as a positive finding and de Wit as a separate set of failures understates the problem. The one human overtraining result failed to replicate twice, and de Wit et al. argue that devaluation failures in compulsive patients reflect weak goal-directed control rather than strong habits.
    - **"Several days" is generous.** Tricomi compared 1 versus 3 days of training.
  - **Suggested rewrite**: "... rats with lesions there stayed goal-directed even on training schedules that make normal rats habitual. In people, Elizabeth Tricomi and colleagues reported that three days of training made responding insensitive to devaluation and engaged the posterior putamen, but Sanne de Wit and colleagues failed to reproduce this in five experiments, two of them direct replications, so whether overtraining alone produces habits in people is uncertain."

- **Line 102**: "Daw, Yael Niv, and Peter Dayan proposed that the brain runs both and gives control to whichever is less uncertain ..., which is why habits take over with practice".
  - **What is wrong**:
    - **A proposal stated as fact.** The arbitration account is a proposal, but "which is why" turns it into an established explanation.
    - **The habit mapping is contested.** That habits are model-free cached values is disputed. Miller, Shenhav and Ludvig (2019, Psychol. Rev. 126:292, PubMed 30676040) model habits as value-free action repetition, and this accounts for devaluation insensitivity and schedule effects.
    - **The two-step task is contested.** Its signature of model-based control can be produced by sophisticated model-free strategies (Akam, Costa and Dayan 2015, PLoS Comput. Biol. 11:e1004648).
  - **Chapter 9 depends on this.** Chapter 9 is about habits, so this mapping should be flagged as open here.
  - **Suggested rewrite**: "... proposed that the brain runs both and gives control to whichever is less uncertain, which would explain why habits take over with practice. Others argue that habits are not cached values at all but actions strengthened simply by being repeated."

- **Line 82**: "Celeste Kidd, Holly Palmeri, and Richard Aslin showed what waiting depends on. ... Waiting is a decision about how reliable the future is, and in an environment where promises are broken, taking the marshmallow is the rational choice."
  - **What is wrong**:
    - **The study is small and the authors' claim is narrower.** Kidd et al. tested 28 children (14 per group), and their abstract says wait times reflect reliability "in addition to self-control" (PubMed 23063236). "Showed what waiting depends on" and the unqualified last sentence read as if reliability were the whole story.
    - **A larger test found no effect.** A preregistered-scale test in 149 Japanese children found that the experimenter's trustworthiness "did not significantly affect children's wait times" (Yanaoka, Michaelson, Saito and Munakata 2026, Dev. Sci. 29:e70185). Habits of waiting and culture mattered more.
    - **Watts et al. is described too loosely.** The study sampled children of mothers without a college degree (n ≈ 900). Its behavioral outcomes at 15 were "much smaller and rarely statistically significant".
  - **Suggested rewrite**: "Celeste Kidd, Holly Palmeri, and Richard Aslin found, in 28 children, that those who had just seen the experimenter keep a promise waited about four times as long as those who had seen one broken; a larger later study found a weaker role for trust and a larger one for habits of waiting. Waiting is partly a decision about how reliable the future is, and where promises are broken, taking the marshmallow can be the rational choice."

- **Line 120**: "A drug that raises dopamine directly produces a positive error every time ... so the value of drug-seeking grows without limit. The account explains why drug-related habits are so hard to break and is one of several".
  - **What is wrong**: The account's distinctive prediction was tested and failed. If cocaine always produces an uncompensable positive error, Kamin blocking should not occur with cocaine as the reinforcer. Panlilio, Thorndike and Schindler found normal blocking: "contrary to prediction, pre-training with the tone blocked conditioning to the light" (2007, Pharmacol. Biochem. Behav. 86:774, PubMed 17445874). Redish's model also addresses overvaluation of drug-seeking, not habit as such.
  - **Suggested rewrite**: "... so the value of drug-seeking would grow without limit. The idea is elegant but one of several, and one of its clearest predictions, that cues paired with cocaine should escape the normal rules of blocking, failed when tested in rats."

- **Lines 126 to 130 (AI implications)**: "Most deployed models spend the same computation on every input, easy or hard." "Calibrated confidence is scarce." "most systems explore by injecting randomness at a fixed rate."
  - **What is wrong**: As of 2026 these are outdated as general statements:
    - **Adaptive computation is now deployed.** Frontier language models with test-time reasoning spend variable amounts of computation per input, and adaptive computation time, early exit and mixture-of-experts routing are established.
    - **Calibration has improved.** Minderer et al. (2021, NeurIPS, "Revisiting the calibration of modern neural networks") found that recent non-convolutional architectures are well calibrated. Kadavath et al. (2022, "Language models (mostly) know what they know") found pretrained language models reasonably calibrated, with post-training degrading calibration.
    - **Exploration is not fixed.** Epsilon is usually annealed, and count-based and intrinsic-motivation bonuses (Bellemare et al. 2016; Burda et al. 2019) and adaptive exploration schedules (Agent57, Badia et al. 2020) are standard in research systems.
  - **Suggested rewrite**:
    - "Many artificial systems still spend the same computation on every input. The newer reasoning models that think longer about harder problems are a step toward the brain's practice of stopping when it is sure enough, though they rarely set the stopping point by the stakes."
    - For calibration: "Guo and colleagues found that the deep networks of the mid-2010s were systematically overconfident ...; newer architectures are better calibrated, but confidence that is reliable when the input is unlike the training data remains hard to get."
    - For exploration: "most agents explore with randomness on a schedule fixed in advance or add bonuses for novelty".

## Minor (imprecise wording, citation fit)

- **Line 22**: The axiomatic expected-utility theorem appeared in the second edition of *Theory of Games* (1947), not the 1944 first edition. Also, economists did not generally assume expected-utility maximization "since 1738"; it became standard after von Neumann and Morgenstern and Savage. Suggested: "Daniel Bernoulli proposed in 1738 ...; John von Neumann and Oskar Morgenstern proved in 1947 ...".
- **Line 24**: Bartra et al. (2013) found the vmPFC and ventral striatum signal "for both monetary and primary rewards" (PubMed 23507394); social reward was not a category. Drop "or social reward", or cite a social-value study (for example Ruff and Fehr 2014, Nat. Rev. Neurosci. 15:549).
- **Line 32**: Herrnstein's matching is to relative reinforcement rate over sessions, not to "rewards each had recently delivered". The local, recency-weighted version is what Sugrue et al. found, so the contrast is worth keeping. Also, "Newsome" and "LIP" are used here before they are introduced (lines 42 and 44).
- **Line 34 versus Chapter 7**: Chapter 8 says that in Fellows and Farah's variant "the patients' deficit largely disappeared"; Chapter 7 (Ch7 line 168) says it "shrank". Use the same wording in both. "Largely explained by an underlying reversal learning deficit" (abstract) supports either.
- **Line 48**: The optimality of the diffusion model (Bogacz et al.) holds for stationary evidence of known reliability. When difficulty varies from trial to trial, the optimal bound collapses over time (Drugowitsch et al. 2012, J. Neurosci. 32:3612), which is the bridge to the urgency sentence at line 52. Add "when the strength of evidence is fixed".
- **Line 52 (STN)**: Chapter 4 (Ch4 line 104) attributes "stop everything at once" to the hyperdirect path and names the STN only as "a station on" the indirect path (Ch4 line 108). Suggested: "the subthalamic nucleus, the relay of the hyperdirect path that Chapter 4 described as able to stop everything at once". Also, the empirical DBS impulsivity result is Frank, Samanta, Moustafa and Sherman 2007 (Science 318:1309). Frank 2006 is the model.
- **Line 52 (urgency)**: Cisek et al.'s urgency-gating model is an alternative to long integration, not just a falling bound. Large-scale model comparison found that fixed bounds fit most human and monkey data (Hawkins et al. 2015, J. Neurosci. 35:2476, PubMed 25673842). Cite Churchland, Kiani and Shadlen 2008 or Hanks et al. 2014 for an urgency signal in LIP, and say "in some tasks".
- **Line 60**: The changes-of-mind result is about continued accumulation, not confidence; "Confidence also keeps the decision open" is a loose lead-in. Also, "in exactly the cases where" is stronger than the paper: the model explains the frequency and error-dependence of reversals.
- **Line 64**: "They are risk averse for gains and risk seeking for losses" holds for moderate to high probabilities. Prospect theory's fourfold pattern reverses at low probabilities, which is why people buy both lottery tickets and insurance. The sentence immediately after it (overweighting of small probabilities) sets this up. "most people refuse" is uncited; cite Tversky and Kahneman 1992 or Kahneman 2011.
- **Line 70**: Tom et al. found no loss-related increases in amygdala or insula, which is in some tension with the amygdala lesion result that follows. One clause would help. "their loss aversion was gone" should be "was sharply reduced", because the abstract says "dramatic reduction" and n = 2. For the size of λ, the 2024 meta-analysis by Brown, Imai, Vieider and Camerer (J. Econ. Lit. 62:485), with a mean of about 1.97 and a median of about 1.7, supports "a typical finding".
- **Line 72**: Hsu et al.'s orbitofrontal patients were insensitive to both ambiguity and risk (abstract). Add "and to risk".
- **Line 76**: "a person who prefers ... will, 30 days later, prefer 100 dollars now" holds only for k above 0.1 per day, steeper than typical estimates for money. Use "can", or "an impatient enough chooser will". Ainslie popularized dynamic inconsistency; Strotz (1956) described it first. A one-line note that hyperbolic discounting is itself rational when the hazard rate is uncertain (Sozou 1998, Proc. R. Soc. B 265:2015) would fit the chapter's theme.
- **Line 80**: "The serotonin neurons of Chapter 3, whose firing sustained a rat's waiting". Chapter 3 (Ch3 line 106) reports only that the rats' serotonin neurons fired during the wait. The causal evidence is optogenetic activation in mice (Miyazaki et al. 2014, Curr. Biol. 24:2033, PubMed 25155504). Suggested: "whose firing rose while a rat waited, and whose stimulation made mice wait longer".
- **Line 82**: The academic outcomes (SAT) are from Shoda, Mischel and Peake 1990 (Dev. Psychol. 26:978), which Watts et al. replicate. Mischel et al. 1989 is a review. Cite Shoda et al. as well.
- **Line 86**: Gittins and Jones first published the index in 1974. Auer et al.'s UCB guarantees order-optimal regret in the undiscounted frequentist setting; it was not shown to "do almost as well" as the Gittins policy. Suggested: "gave simpler rules ... with guarantees that their losses grow only slowly".
- **Line 90**: Behrens et al. measured learning rate, not exploration, and found the volatility signal in ACC. The norepinephrine link is Yu and Dayan's theory plus later pupil work (Nassar et al. 2012; Browning et al. 2015). Suggested: "How fast to learn should depend on how fast the world is changing ... as the account of norepinephrine ... would predict, although the experiment did not measure norepinephrine".
- **Line 92**: Kolling et al.'s interpretation of dACC as encoding search value is contested. Shenhav, Straccia, Cohen and Botvinick (2014, Nat. Neurosci. 17:1249; 2016, CABN 16:1127) found dACC activity better explained by choice difficulty. One clause would do.
- **Line 104**: Dayan et al. 2006 is a modeling paper; "argued, with models," is more accurate than "showed". The cleanest empirical case is negative automaintenance: pigeons keep pecking a key even when pecking cancels the food (Williams and Williams 1969).
- **Line 108**: Simon coined "satisfice" in 1956 (Psychol. Rev. 63:129); the 1955 paper set out bounded rationality with aspiration levels. Gigerenzer and Goldstein (1996) showed take-the-best matched regression in fitting. The small-data, out-of-sample advantage and the "less prone to fit noise" explanation came later (Czerlinski, Gigerenzer and Goldstein 1999; Gigerenzer and Brighton 2009).
- **Line 114**: Henrich et al. attribute the cross-society variation to "market integration" and "payoffs to cooperation", not "cooperation with strangers". Market integration is close, but name both.
- **Line 118**: Chapter 3 (Ch3 line 116) already describes Frank et al. 2004 in detail. Refer back ("as Chapter 3 described") instead of introducing it as new, and point to Chapter 3 rather than Chapter 4 for dopamine in Parkinson's disease. Weintraub et al.'s odds ratio is 2.72 (95 percent CI 2.08 to 3.54), so "nearly three times the odds" is more accurate than "roughly two and a half".
- **Line 132**: "the first program to beat a professional Go player" should add "on a full board without handicap", since earlier programs beat professionals with handicap stones.

## What an expert would expect and is missing (brief)

- **Rabin's calibration theorem** (Rabin 2000, Econometrica 68:1281). Refusing the 110/100 coin flip at every wealth level implies absurd risk aversion over large stakes under expected utility. This is the standard argument for a reference point and loss aversion rather than a concave utility curve, and the chapter's own example sets it up.
- **The description-experience gap** (Hertwig, Barron, Weber and Erev 2004). When probabilities are learned from outcomes, people underweight rare events, the opposite of prospect theory's overweighting. This is central to a book about learning.
- **Self-control as value modulation**: Hare, Camerer and Rangel 2009 (Science 324:646), where dorsolateral prefrontal cortex modulates vmPFC value in dieters. This is the leading alternative to the two-systems account of line 80.
- **Opportunity cost and vigor**: tonic dopamine as average reward rate (Niv, Daw, Joel and Dayan 2007). This ties the urgency signal, foraging and Parkinsonian slowness together.
- **Replay and planning**: hippocampal replay as model-based evaluation (Mattar and Daw 2018), and the successor representation between model-free and model-based control (Momennejad et al. 2017). Both link back to Chapter 5.
- **The Bayesian link to Chapter 6**: the SPRT sums log-likelihood ratios, which is sequential Bayesian inference. Chapter 6's "a saccade is a decision about where evidence is most needed" (Ch6 line 128) is the natural cross-reference, and the chapter makes none to Chapter 6.

## Citation support check

Checked against PubMed abstracts unless noted.
- **Footnote 2 (Padoa-Schioppa and Assad 2006, 16633341)**: supports OFC value coding; the text misassigns juice-independence (see Major).
- **Footnote 3 (Bartra et al. 2013, 23507394)**: 206 studies, confirmed. "monetary and primary rewards", not social (Minor).
- **Footnote 4 (Camille et al. 2011, 21593337)**: confirmed (GARP violations).
- **Footnote 7 (Louie et al. 2013, 23530203)**: supports a normalization model of choice. The neural shrinkage is from Louie et al. 2011, and the behavioral effect failed preregistered replication (Gluth et al. 2020, 32015490).
- **Footnote 10 (Sugrue et al. 2004, 15205529)**: confirmed.
- **Footnote 11 (Fellows and Farah 2005, 15217900)**: "largely explained by an underlying reversal learning deficit", confirmed.
- **Footnote 12 (Krajbich et al. 2010, 20835253)**: confirmed.
- **Footnote 13 (Hunt et al. 2012)**: consistent with the published MEG and biophysical-model result.
- **Footnote 16 (Roitman and Shadlen 2002, 12417672)**: ramps and threshold, confirmed. The 70 ms figure is in the paper's results.
- **Footnote 18 (Gold and Shadlen 2007)**: Turing's Banburismus as sequential analysis is discussed there, so it supports the claim.
- **Footnote 22 (Cavanagh et al. 2011, 21946325)**: confirmed, "reversed this relationship, resulting in impulsive choice". Frank 2006 is the model; the empirical DBS paper is Frank et al. 2007.
- **Footnote 23 (Cisek et al. 2009)**: supports urgency, but as an alternative to integration (Minor).
- **Footnotes 24 and 25 (Latimer 2015, 26160947; Katz 2016, 27376476)**: confirmed. Counter-evidence is omitted (see Moderate).
- **Footnotes 26 to 28 (Kiani 2009, 19423820; Resulaj 2009, 19693010; Fleming 2010, 20847276)**: confirmed.
- **Footnote 31 (Tversky and Kahneman 1981)**: 72 percent (N = 152) and 78 percent (N = 155), confirmed from the paper.
- **Footnotes 32 to 34 (De Martino 2006, 16888142; Tom 2007, 17255512; De Martino 2010, 20142490)**: confirmed. 2010: two patients, "dramatic reduction".
- **Footnote 37 (Hsu et al. 2005, 16339445)**: confirmed; the patients were insensitive to risk as well (Minor).
- **Footnotes 40 and 41 (McClure 2004; Kable and Glimcher 2007, 17982449)**: confirmed (McClure 2004 checked through McClure et al. 2007's summary of it, 17522323).
- **Footnote 42 (Mischel et al. 1989)**: a review. The academic outcome data are in Shoda et al. 1990 (Minor).
- **Footnote 43 (Watts et al. 2018, 29799765)**: confirmed (half the size; reduced by two thirds).
- **Footnote 44 (Kidd et al. 2013, 23063236)**: confirmed, N = 28, "in addition to self-control" (see Moderate).
- **Footnotes 46 to 48 (Daw 2006, 16778890; Wilson 2014, 25347535; Behrens 2007, 17676057)**: confirmed. Daw also reports intraparietal sulcus. Behrens measured learning rate.
- **Footnote 50 (Hayden 2011, 21642973; Kolling 2012, 22491854)**: confirmed; Kolling is contested (Minor).
- **Footnote 53 (Yin et al. 2004, 14750976)**: interval schedules, not extended training (see Moderate).
- **Footnote 54 (Tricomi et al. 2009, 19490086)**: confirmed as published, but failed two direct replications (de Wit et al. 2018, 29975092).
- **Footnotes 57 and 58 (Daw 2011, 21435563; Gillan 2016, 26928075)**: confirmed.
- **Footnote 67 (Sanfey et al. 2003, 12805551)**: confirmed.
- **Footnote 68 (Henrich et al. 2001)**: the range of means (0.26 Machiguenga to 0.58 Lamalera) and the market-integration and payoffs-to-cooperation explanation are from the paper.
- **Footnote 69 (Frank et al. 2004, 15528409)**: confirmed.
- **Footnote 70 (Weintraub et al. 2010, 20457959)**: 3090 patients, 13.6 percent, OR 2.72, confirmed. "Two and a half" is slightly low (Minor).
- **Footnote 71 (Redish 2004, 15591205)**: the model is as described; its blocking prediction failed (Panlilio et al. 2007, 17445874).
- **Footnotes 74 to 76 (Guo 2017; Gal and Ghahramani 2016; Silver 2016)**: support the claims as of their dates (see Moderate on currency).
- All other footnotes support their sentences as far as I could check from abstracts and standard sources.

## Figures

- **Figure 8.1**: The schematic matches the text and caption. The boxes, arrows and chapter pointers (body state to Chapter 7, basal ganglia to Chapter 4, dopamine prediction error to Chapter 3) are consistent.
- **Figure 8.2**: It is labeled illustrative and shows the right qualitative pattern: an initial dip, coherence-graded ramps, convergence about 70 ms before the saccade, and the motion-aligned fan reversed in the saccade-aligned panel. Two problems of scale:
  - **Ramps too slow.** The 51.2 percent trace in panel A reaches the common level at about 710 ms, implying an RT near 780 ms, whereas Roitman and Shadlen's RTs at that coherence were about 400 to 450 ms. At the slope used for 0 percent, the level would be reached only after about 4 s. Steeper slopes, roughly twice as steep, would match the data.
  - **Artificial plateau.** The flat plateau at the common level in panel A does not occur in motion-aligned averages, which are truncated before the saccade in the original figure.

  Neither problem misleads about the principle.
- **Figure 8.3**: Correct and consistent with the text. Of the 9 traces, 7 reach the correct bound, against an expected 76 percent at a = 1. Panel B's marked points (0.728 for 70 percent in 0.5 s; 1.887 for 90 percent in 2.6 s) are the analytic values.
- **Figure 8.4**: Correct, using λ = 2.25, α = 0.88 and γ = 0.61. The weighting curve crosses the diagonal near p = 0.34. Panel B uses the gain parameter only; the caption could say "for gains" (the loss parameter is 0.69).
- **Figure 8.5**: Correct, with k = 0.2 per day and r = 0.05 per day. The hyperbolic curves cross on day 25, and the exponential ratio is constant (1.046), so those curves never cross, as captioned. The steep k is fine for an illustration.
- **Figure 8.6**: Correct. Panel B is a standard ten-armed testbed (400 runs), and the asymptotes (greedy about 1.05, ε = 0.1 about 1.35, UCB about 1.45) match Sutton and Barto's Fig. 2.2 and 2.4 qualitatively. The bonus is 2·sqrt(ln t / n), a more exploratory constant than UCB1, which is fine. Panel A is schematic; the widths are not 1/sqrt(n), but the caption claims only "very different uncertainty".
- **Figure 8.7**: Labeled illustrative and matches Adams 1982 qualitatively.
- **Attribution block (line 148)**: correctly identifies which figures are illustrative, computed or simulated.

## Cross-chapter consistency

- **Ch8 line 12 versus Ch7 lines 156 to 170**: consistent. The body of Chapter 7 ends on the Iowa gambling task and hands the question to Chapter 8, and "leaves reasoning intact and choice impaired" matches Ch7's "largely intact".
- **Ch8 line 32 versus Ch3 lines 56 and 64**: dopamine wording matches the settled book-wide position.
- **Ch8 line 34 versus Ch7 line 168**: same study, different strength ("largely disappeared" versus "shrank"). Harmonize (Minor).
- **Ch8 line 28 versus Ch4 line 40**: lateral inhibition and winner-take-all, consistent.
- **Ch8 line 52 versus Ch4 lines 104 and 108**: Chapter 4 gives "stop everything at once" to the hyperdirect path and places the STN on the indirect path. Reword (Minor).
- **Ch8 line 60 versus Ch7 line 52**: "accuracy and confidence need not agree", consistent.
- **Ch8 line 70 versus Ch7 line 104**: S.M. described consistently.
- **Ch8 line 80 versus Ch3 line 106 and Ch3 line 130**: the Doya mapping of serotonin to the discount is consistent, but Chapter 3 reports only correlational firing, so Ch8's "sustained" is causal (Minor).
- **Ch8 line 90 versus Ch3 line 104**: Yu and Dayan's norepinephrine and unexpected uncertainty, consistent.
- **Ch8 line 118 versus Ch3 line 116**: Frank et al. 2004 is described in Chapter 3. Chapter 8 re-introduces it and cites Chapter 4 for dopamine loss (Minor).
- **Ch8 line 120 versus Ch7 line 178**: "addiction is a form of reward hacking" and Redish's account are consistent.
- **Ch8 line 130 versus Ch3 line 130 and Ch7 line 180**: neuromodulators setting exploration, consistent.
- **Ch8 versus Ch6**: no explicit cross-reference. The SPRT and Bayesian-inference link and the active-sensing sentence (Ch6 line 128) are natural ones to add (see Missing). Nothing in Chapter 8 contradicts Chapter 6. Chapter 8 uses "prediction error" only in the dopamine, scalar-value sense, which respects the distinction drawn at Ch6 line 64 and Ch3 line 64.

## Sources consulted

- PubMed E-utilities abstracts: 16633341, 23507394, 21593337, 23530203, 32015490, 32929204, 15205529, 15217900, 20835253, 12417672, 21946325, 26160947, 27376476, 39422555 (Steinemann et al. 2024), 35421328 (Jeurissen et al. 2022), 19423820, 19693010, 20847276, 17255512, 20142490, 16888142, 16339445, 17522323, 17982449, 29799765, 23063236, 41949069 (Yanaoka et al. 2026), 16778890, 25347535, 17676057, 21642973, 22491854, 27580609 (Shenhav et al. 2016), 14750976, 19490086, 29975092, 26928075, 21435563, 12805551, 20457959, 15528409, 25155504, 15591205, 17445874 (Panlilio et al. 2007), 25673842 (Hawkins et al. 2015), 30676040 (Miller et al. 2019), 15381028.
- Arithmetic checks: the closed-form DDM accuracy and mean decision time, the prospect-theory valuation of the coin flip, and the hyperbolic crossing point, computed by hand and checked against `make_figures.py` (V = 0.582, bounds 0.728 and 1.887; k = 0.2, crossing at day 25).
