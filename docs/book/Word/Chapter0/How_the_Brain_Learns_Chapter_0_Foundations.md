---
title: "Chapter 0"
subtitle: "Foundations: The Physical and Chemical Basis of Life"
---

> *"What an organism feeds upon is negative entropy. Or, to put it less paradoxically, the essential thing in metabolism is that the organism succeeds in freeing itself from all the entropy it cannot help producing while alive."*
>
> --- Erwin Schrödinger, *What Is Life?* (1944)

Neurons are cells before they are anything else, and the brain's capabilities and limits follow from the physics and chemistry of the matter it is made of. This chapter supplies that background: what a cell is, what energy and entropy demand of it, how charge and diffusion behave in salt water, what proteins and the other large molecules do, and how one cell becomes a nervous system. Readers who have studied biology can skim it. Readers who have not will find here every term the later chapters assume, defined once and then used without apology.

# What a Cell Is

Every living thing on Earth is made of cells. A bacterium is one cell; an adult human body is on the order of 30 trillion of them, the classic estimate being 37 trillion and a recent recount giving about 36 trillion for a reference man and 28 trillion for a reference woman.[^1] Across that range of scale, all cells share the features that define being alive.[^2]

A cell is a compartment bounded by a membrane. Inside the membrane is a crowded chemical environment where thousands of reactions run at once; outside is whatever the world happens to be. The membrane separates the controlled interior from the uncontrolled exterior, and without that boundary there is no chemistry a cell could call its own. Figure 0.1 shows the standard inventory of an animal cell: a nucleus that holds the DNA, mitochondria that produce most of the cell's usable energy, a system of internal membranes that makes and sorts proteins, and a skeleton of filaments that gives the cell its shape. A neuron has every one of these parts.

Cells are not passive containers. They maintain their internal environment, resist degradation, harvest energy from their surroundings, respond to signals, and reproduce. Each of these activities is work, and a cell that stops doing the work dies.

![Figure 0.1. The parts of an animal cell. A membrane bounds the cell; the nucleus holds the DNA; mitochondria supply most of the cell's usable energy; the endoplasmic reticulum and Golgi apparatus make and sort proteins; filaments give the cell its shape. Every one of these parts is present in a neuron.](images/figure_0_1.png)

Cells come in two kinds. Prokaryotes, the bacteria and archaea, are small and structurally simple: they have no nucleus, and their DNA lies loose in the cell interior. Despite that simplicity they dominated the planet for more than two billion years and remain its most numerous organisms.[^3] Eukaryotes, which include plants, animals, fungi, and the single-celled protists, are larger and more elaborate. Their DNA is enclosed in a membrane-bound nucleus, and their interior is divided into organelles, specialized compartments that each perform a particular job. All neurons are eukaryotic cells, and the distinction matters because eukaryotic machinery is what made multicellular organisms, specialized cell types, and eventually nervous systems possible.[^4]

# Energy and Order

Cells obey the same physical laws as everything else. There is no vital force and no exemption for living matter, and the laws that matter most for a neuron are the two laws of thermodynamics.[^5]

The first law says that energy is neither created nor destroyed, only transformed. When a cell breaks down glucose, the chemical energy in the sugar becomes other forms: some is captured as useful work, the rest leaves as heat, and the total is unchanged. The second law says that in any spontaneous process the total entropy of the universe increases. Entropy is a measure of disorder, or more precisely of the number of microscopic arrangements compatible with what we can see, and left alone, ordered things become disordered. A cell deprived of fuel does not pause; it dissolves.

It follows that maintaining the organized structure of a cell requires constant work. Figure 0.2 shows the arrangement. The cell takes in molecules of low entropy and high free energy (glucose and oxygen), uses them to keep its own structure in order, and exports entropy to its surroundings as heat and as small, disordered waste molecules such as carbon dioxide and water. The cell's own entropy stays steady, the entropy of the surroundings rises by more than the cell's would otherwise have risen, and the second law is satisfied. Schrödinger's phrase for this, in the epigraph, is that the organism feeds on negative entropy; he added in a note to the same chapter that, writing for physicists alone, he would have said it feeds on free energy, the portion of energy that is available to do work.[^6]

![Figure 0.2. How a cell keeps its order. (A) Glucose and oxygen enter with low entropy and high free energy; the cell spends that free energy to maintain ion gradients, folded proteins, and intact membranes, and exports entropy as heat and waste. (B) The cell's entropy holds steady while the entropy of its surroundings, and so of the universe, rises. An illustrative diagram.](images/fig_cell_energy_entropy.png)

The currency in which cells spend free energy is a small molecule called adenosine triphosphate, or ATP. Mitochondria make most of it by oxidizing the breakdown products of glucose, and nearly every energy-requiring process in a cell, from pumping ions to building proteins, is paid for by splitting ATP into adenosine diphosphate and phosphate. It is tempting to say that the energy is "stored in the phosphate bond" and released when the bond breaks, but that is a misconception: breaking any bond costs energy. ATP hydrolysis releases free energy because the products are more stable than the reactant, through relief of the repulsion among the closely packed negative charges, better solvation of the products by water, and resonance stabilization of the released phosphate.[^7] The distinction is worth keeping in mind, because the brain spends much of its ATP on one task, keeping ions on the correct sides of neuronal membranes.

# Charge and Gradients

Neurons are electrical devices, but their electricity is not the electricity in a wire. In a wire, electrons move through a metal; in a neuron, ions move through water and across membranes, which is far slower and is why the brain's signals look nothing like a circuit board's. Understanding the difference means understanding electrochemistry.

Ions are atoms or molecules that carry an electric charge because they have lost or gained electrons. The ions that matter most for a neuron are sodium, potassium, and calcium, all positively charged (calcium carries two charges), and chloride, which is negative.[^8] When ions are distributed unequally across a barrier, two tendencies act on them. One is the concentration gradient: molecules spread from where they are concentrated to where they are scarce, because spreading out is the more probable arrangement, which is the second law again in different clothes. The other is the electrical gradient: opposite charges attract, like charges repel, and a positive ion is drawn toward a negatively charged region. The sum of the two is the electrochemical gradient, and it is what every neural signal runs on.

A membrane with unequal ions on its two sides is a charged battery, and neurons discharge it to signal.[^9] Figure 0.3 shows how the battery is charged. A protein in the membrane, the sodium-potassium pump, uses the energy of one ATP to push three sodium ions out of the cell and pull two potassium ions in, so that potassium ends up concentrated inside and sodium outside.[^10] A second class of membrane protein, the ion channel, forms a pore that lets one kind of ion through and no other, and opens and closes in response to voltage or to a chemical. When a channel opens, ions run down their gradient and the membrane voltage changes. The pumps charge the battery slowly and continuously; the channels discharge it in milliseconds. Chapter 2 builds the neuron's signal from exactly these two parts.

![Figure 0.3. The sodium-potassium pump charges the membrane. Each cycle spends one ATP to move three sodium ions out and two potassium ions in, so the cell ends with potassium concentrated inside and sodium outside. The bars at the right show the two gradients the pump maintains.](images/figure_0_3.png)

# Diffusion

Molecules in solution are in constant random motion because of thermal energy. That motion carries substances from regions of high concentration to regions of low concentration, a process called diffusion.[^11] Diffusion is fundamental to cell biology: neurotransmitters diffuse across synaptic gaps, oxygen diffuses from blood into tissue, and waste diffuses away from cells. No energy is spent on it; the molecules simply wander, and wandering evens things out.[^12]

Diffusion has one property that shapes the whole design of the nervous system. The time a diffusing molecule takes to cover a distance grows with the square of the distance.[^13] A small molecule such as a neurotransmitter crosses the twenty-nanometer gap of a synapse in a fraction of a microsecond and drifts across a micrometer-sized dendritic spine in under a millisecond, but the same molecule would take years to diffuse the length of a meter-long axon. This is why neurons evolved a different mechanism for long-distance signaling, the electrical impulse that Chapter 2 describes, and why chemistry is reserved for the short hop across the synapse.

# Molecules and Bonds

Atoms join into molecules by sharing or transferring electrons, and the forces that hold them together are chemical bonds.[^14] The point that matters for a neuron is that bonds come in two strengths. Covalent bonds, in which two atoms share a pair of electrons, are strong and stable; they hold the atoms of a water molecule together and form the backbone of every protein and every strand of DNA. The weak interactions are the interesting ones. Ionic attractions between opposite charges, and hydrogen bonds, which form when a hydrogen atom bonded to oxygen or nitrogen is drawn toward another oxygen or nitrogen, are each a small fraction of the strength of a covalent bond, and they can be made and broken at body temperature. That is what lets a protein fold into a shape, change its shape when something binds to it, and change back. An ion channel opens because weak bonds rearrange; the two strands of DNA separate for copying because hydrogen bonds let go.[^15] Figure 0.4 shows the three kinds.

![Figure 0.4. Three kinds of chemical bond. (A) A covalent bond shares a pair of electrons and is strong. (B) An ionic bond is the attraction between a positive and a negative ion. (C) A hydrogen bond is a weak attraction between partial charges on neighboring molecules; many together shape proteins and hold the two strands of DNA.](images/figure_0_4.png)

# The Molecules of Life

Four classes of large molecules do most of the work in a cell, and Figure 0.5 sketches them. Proteins are the machines. They catalyze reactions, form structural elements, transport materials, send and receive signals, and perform mechanical work. A protein is a chain of amino acids folded into a specific three-dimensional shape, and the shape determines the function: Christian Anfinsen showed in the 1960s that a protein unfolded in the test tube refolds into its working shape on its own, so the sequence of amino acids contains the instructions for the shape.[^16] Ion channels are proteins. Neurotransmitter receptors are proteins. The machinery that releases neurotransmitter from vesicles, the small membrane-bound packets in which a neuron stores it, consists of proteins.

Nucleic acids store and transmit the genetic information. DNA holds the instructions for building proteins, and RNA carries those instructions from the DNA to the protein-building machinery.[^17] Carbohydrates, the sugars, store energy and form structural materials; glucose is the brain's primary fuel, and the brain, at about two percent of body mass, consumes about a fifth of the body's glucose-derived energy at rest.[^18] Lipids, the fats, form membranes, store energy, and act as signaling molecules. The membrane around every cell and every organelle is a double layer of lipids with water-loving heads facing outward and water-fearing tails facing inward, a structure first inferred in 1925 from the observation that the lipid extracted from red blood cells covers twice the cells' surface area.[^19]

![Figure 0.5. The four kinds of large molecule. Proteins are chains of amino acids folded into machines; nucleic acids are sequences of nucleotides that store instructions; carbohydrates are sugars used for fuel and structure; lipids have water-loving heads and water-fearing tails and form membranes.](images/figure_0_5.png)

# Enzymes

Most of the reactions in a cell would run far too slowly to support life without help. Enzymes are proteins that accelerate specific reactions, by factors of a million in ordinary cases and by up to a hundred thousand trillion in the most extreme case measured, an enzyme called OMP decarboxylase whose reaction would otherwise take 78 million years to run halfway.[^20] An enzyme works by holding the reacting molecules together in the right orientation and chemical surroundings. It is not used up; a single enzyme molecule can process thousands of molecules per second.[^21] And it is specific: each enzyme typically catalyzes one reaction or a small family of related ones, the fit between enzyme and substrate being, in Emil Fischer's image of 1894, that of a lock and key.[^22] Specificity is what lets a cell decide which reactions happen, when, and where. Neural signaling depends on enzymes at every step: synthesizing neurotransmitters, breaking them down, making and consuming ATP, and modifying ion channels.

# How These Laws Were Discovered

In 1665, Robert Hooke looked at a sliver of cork through a microscope and saw small compartments he called cells, from the Latin *cella*, a small room. He was looking at the walls of dead plant cells, but the name stuck, and his drawing, reproduced in Figure 0.6, is the first published description of a cell.[^23] Over the next 170 years microscopes improved and observations accumulated, until in 1838 and 1839 Matthias Schleiden and Theodor Schwann proposed the cell theory: all living organisms are composed of cells, and the cell is the basic unit of life.[^24] Rudolf Virchow later popularized the principle, first stated by François-Vincent Raspail, that every cell arises from a pre-existing cell.[^25] Whatever the apparent diversity of life, trees, mushrooms, fish, and humans share a common structural basis.

![Figure 0.6. Hooke's drawing of cork (1665). The first published description of cells, from *Micrographia*; what Hooke saw were the walls of dead plant cells.](images/figure_0_6.png)

The laws of thermodynamics emerged from a practical concern with steam engines. Sadi Carnot in 1824 asked how much work a given quantity of heat could yield; Rudolf Clausius, by 1865, had given the answer its general form and had coined the word entropy.[^26] Eduard Buchner's demonstration in 1897 that yeast extract with no living cells in it still ferments sugar was the turning point for biology, because it showed that the chemistry of life could be taken out of the cell and studied as chemistry.[^27] Vitalism, the belief that life needs a special non-physical force, did not die at once; Hans Driesch defended it into the twentieth century. But by the middle of that century, when Schrödinger wrote the book quoted at the head of this chapter, the laws of physics had been applied to living matter without finding any exemption, and vitalism had no scientific case left.[^28]

Around 1780, Luigi Galvani found that electrical stimulation made a frog's leg twitch, the first demonstration that electricity has a role in living tissue.[^29] His contemporary Alessandro Volta, arguing with him about what the experiment meant, invented the battery.[^30] In the century and a half that followed, scientists worked out how cells use ions and gradients, and the culmination came in 1952, when Alan Hodgkin and Andrew Huxley published a mathematical model of the action potential in the squid giant axon, an axon so large (up to a millimeter across) that electrodes could be threaded inside it. Their model explained in quantitative detail how the opening and closing of sodium and potassium channels generate the electrical impulse. Figure 0.7 shows one impulse computed from their equations: the sodium conductance rises first and fast and drives the voltage up, the potassium conductance rises later and more slowly and drives it back down, and the brief undershoot at the end is the potassium channels still open. Hodgkin and Huxley received the Nobel Prize for this work in 1963.[^31]

![Figure 0.7. One action potential from the Hodgkin and Huxley equations (a simulation). (A) The membrane potential of a model squid giant axon after a one-millisecond stimulus: a rise to about +40 mV, a fall, and a brief undershoot. (B) The sodium conductance opens first and fast; the potassium conductance opens later and closes slowly. Both panels are computed from the 1952 model, not recorded.](images/fig_hodgkin_huxley_simulation.png)

The twentieth century then brought the structure of DNA in 1953, the genetic code in the 1960s,[^32] the mechanisms of protein synthesis, and the details of the metabolic pathways. That work continues as structural biology, proteomics, and systems biology.

# From One Cell to a Brain

A single cell is remarkable, but a brain is not a single cell. The human brain contains approximately 86 billion neurons and a similar number of non-neuronal cells, most of them glia, the support cells that insulate axons, regulate the chemistry around synapses, and clear debris, all organized into precise structures.[^33] How does that organization arise?

Every human begins as one fertilized egg. Through repeated division, differentiation, and migration, that one cell becomes tens of trillions organized into tissues, organs, and systems, and Figure 0.8 shows the first weeks of the process.[^34] The sequence is not random. Cells follow genetic programs inherited from their parent cells that specify when to divide, when to differentiate into a specialized type, where to migrate, and how to connect. Development is a cascade in which early events constrain later possibilities: a cell that has committed to the nervous system cannot later become a liver cell, and a neuron that has migrated to the cortex cannot relocate to the spinal cord. Conrad Waddington's image for this was a ball rolling down a landscape of branching valleys, each fork closing off the valleys not taken.[^35] This is why early development is so critical and why errors in it propagate forward.

![Figure 0.8. The first weeks of a human embryo. From the fertilized egg (top left), repeated division produces a ball of cells, which implants in the uterine wall and organizes into the layers from which every tissue, including the nervous system, will form.](images/figure_0_8.png)

Cells do not develop in isolation. They constantly send and receive chemical signals that coordinate their behavior, and biologists sort the signals by how far they travel. Autocrine signals act on the cell that produced them. Paracrine signals act on nearby cells. Endocrine signals, the hormones, travel through the bloodstream to act on distant cells. Synaptic signaling is treated as a category of its own: a neuron releases a chemical across a gap of about twenty nanometers onto one particular target cell, which makes it a chemical signal with the addressing precision of a wire.[^36] These signals let cells coordinate during development, maintain tissue organization in adults, and respond to changing conditions. The nervous system is, in one sense, an elaboration of cell signaling specialized for speed and precision.

# Self-Organization

Complex organization can emerge from simple rules followed by many agents without any agent knowing the plan. This principle, called self-organization, operates throughout biology; Alan Turing showed in 1952 that two chemicals reacting and diffusing at different rates can produce stripes and spots from a uniform start.[^37]

The wiring of the visual system shows how the brain uses it, and Figure 0.9 shows the two stages. Axons from the retina grow to their targets in the thalamus and the superior colliculus (not directly to the cortex), and they arrive in rough order: an axon from the temporal side of the retina stops near the front of the target, and an axon from the nasal side runs to the back. The ordering is chemical. Roger Sperry proposed in 1963 that growing axons and their targets carry matching chemical labels, and the labels turned out to be graded: the target expresses a molecule, ephrin-A, in a gradient from front to back, temporal axons carry more of its receptor than nasal axons do, and the more receptor an axon carries the sooner the gradient repels it and stops it.[^38] The result is a coarse map, with each axon's terminal arbor spread over a wide region. The second stage sharpens it. Before the eyes open, the retina generates spontaneous waves of activity that sweep across it, so that neighboring retinal cells fire together and distant ones do not; after birth, vision supplies the same correlations. Connections between cells that fire together are strengthened and the rest are pruned, by the rule the book returns to in Chapter 5, Donald Hebb's rule that neurons which fire together wire together, and each arbor shrinks to one position.[^39] Blocking the retinal waves leaves the coarse map in place but prevents the sharpening.[^40]

![Figure 0.9. Two stages in the wiring of the visual map. (A) Axons from the temporal (top) to nasal (bottom) retina terminate in order along the target because a gradient of ephrin-A repels temporal axons sooner; each arbor is still broad. (B) Correlated activity, from spontaneous retinal waves and then from vision, prunes each arbor to a single position. An illustrative diagram.](images/fig_axon_guidance_refinement.png)

No central controller directs either stage. No blueprint specifies where each connection goes. A gradient and a local rule, applied by a million axons at once, produce a map, and the same combination of chemical cues and activity-dependent refinement builds circuits throughout the brain.[^41] The result is structure that looks designed but was never designed. It evolved, and then it developed.

# Why This Foundation Matters

Everything that follows depends on what this chapter has covered. Neurons are cells. They obey thermodynamics and electrochemistry. They are built from proteins, lipids, and the other molecules of life, they develop according to genetic programs, and they wire themselves up by self-organization. When later chapters describe an action potential, they are describing a physical event governed by ion gradients and channels. When they describe learning, they are describing physical changes in synapses governed by molecular biology. When they describe memory, they are describing physical traces left in neural tissue.

How such mechanisms relate to subjective experience, the felt quality of seeing red or tasting coffee, is a question this book does not try to answer.[^42] Neuroscience has explained specific functions of specific circuits in some detail, how the retina encodes an image, for instance, and it has not explained that.[^43] This book stays with what can be explained: the physical mechanisms of learning, memory, perception, and action, which are remarkable enough to warrant careful study on their own. The brain is not a metaphor. It is matter, and matter is enough.

# Next Chapter

Chapter 1: What the Brain Is (and Is Not)

# References and Attribution

## Figure Attribution

Figures 0.2, 0.4, 0.5, 0.7, and 0.9 were drawn for this book. The traces in Figure 0.7 are a simulation computed from the Hodgkin and Huxley (1952) equations with squid giant axon parameters at 6.3 degrees Celsius, not recorded data. Figures 0.2 and 0.9 are illustrative diagrams.

Figure 0.1: "Animal cell structure en.svg" by Mariana Ruiz Villarreal (LadyofHats), public domain, via Wikimedia Commons. Figure 0.3: "Scheme sodium-potassium pump-en.svg" by Mariana Ruiz Villarreal (LadyofHats), public domain, via Wikimedia Commons. Figure 0.6: Robert Hooke, *Micrographia* (1665), Observation XVIII, public domain. Figure 0.8: "HumanEmbryogenesis.svg" by Wikimedia Commons user Zephyris, CC BY-SA 3.0, via Wikimedia Commons.

## Epigraph

Erwin Schrödinger, *What Is Life? The Physical Aspect of the Living Cell* (Cambridge University Press, 1944), chapter 6, "Order, Disorder and Entropy."

## References

Alberts, B., Heald, R., Johnson, A., Morgan, D., Raff, M., Roberts, K., & Walter, P. (2022). *Molecular Biology of the Cell* (7th ed.). W. W. Norton.

Anfinsen, C. B. (1973). Principles that govern the folding of protein chains. *Science*, 181(4096), 223–230.

Azevedo, F. A. C., Carvalho, L. R. B., Grinberg, L. T., Farfel, J. M., Ferretti, R. E. L., Leite, R. E. P., Jacob Filho, W., Lent, R., & Herculano-Houzel, S. (2009). Equal numbers of neuronal and nonneuronal cells make the human brain an isometrically scaled-up primate brain. *Journal of Comparative Neurology*, 513(5), 532–541.

Barresi, M. J. F., & Gilbert, S. F. (2019). *Developmental Biology* (12th ed.). Sinauer Associates.

Berg, H. C. (1993). *Random Walks in Biology* (expanded ed.). Princeton University Press.

Bianconi, E., Piovesan, A., Facchin, F., Beraudi, A., Casadei, R., Frabetti, F., Vitale, L., Pelleri, M. C., Tassani, S., Piva, F., Perez-Amodio, S., Strippoli, P., & Canaider, S. (2013). An estimation of the number of cells in the human body. *Annals of Human Biology*, 40(6), 463–471.

Buchner, E. (1897). Alkoholische Gährung ohne Hefezellen. *Berichte der deutschen chemischen Gesellschaft*, 30(1), 117–124.

Camazine, S., Deneubourg, J.-L., Franks, N. R., Sneyd, J., Theraulaz, G., & Bonabeau, E. (2001). *Self-Organization in Biological Systems*. Princeton University Press.

Cang, J., & Feldheim, D. A. (2013). Developmental mechanisms of topographic map formation and alignment. *Annual Review of Neuroscience*, 36, 51–77.

Carnot, S. (1824). *Réflexions sur la puissance motrice du feu et sur les machines propres à développer cette puissance*. Paris: Bachelier.

Chalmers, D. J. (1995). Facing up to the problem of consciousness. *Journal of Consciousness Studies*, 2(3), 200–219.

Clausius, R. (1865). Ueber verschiedene für die Anwendung bequeme Formen der Hauptgleichungen der mechanischen Wärmetheorie. *Annalen der Physik und Chemie*, 125, 353–400.

Crick, F. (1970). Central dogma of molecular biology. *Nature*, 227, 561–563.

Crick, F. H. C., Barnett, L., Brenner, S., & Watts-Tobin, R. J. (1961). General nature of the genetic code for proteins. *Nature*, 192, 1227–1232.

Einstein, A. (1905). Über die von der molekularkinetischen Theorie der Wärme geforderte Bewegung von in ruhenden Flüssigkeiten suspendierten Teilchen. *Annalen der Physik*, 322(8), 549–560.

Fick, A. (1855). Ueber Diffusion. *Annalen der Physik und Chemie*, 94, 59–86.

Fischer, E. (1894). Einfluss der Configuration auf die Wirkung der Enzyme. *Berichte der deutschen chemischen Gesellschaft*, 27(3), 2985–2993.

Galvani, L. (1791). *De viribus electricitatis in motu musculari commentarius*. Bologna: Ex Typographia Instituti Scientiarum.

Goldman, D. E. (1943). Potential, impedance, and rectification in membranes. *Journal of General Physiology*, 27(1), 37–60.

Gorter, E., & Grendel, F. (1925). On bimolecular layers of lipoids on the chromocytes of the blood. *Journal of Experimental Medicine*, 41(4), 439–443.

Hatton, I. A., Galbraith, E. D., Merleau, N. S. C., Miettinen, T. P., Smith, B. M., & Shander, J. A. (2023). The human cell count and size distribution. *Proceedings of the National Academy of Sciences*, 120(39), e2303077120.

Hebb, D. O. (1949). *The Organization of Behavior: A Neuropsychological Theory*. New York: Wiley.

Helmholtz, H. von (1847). *Über die Erhaltung der Kraft*. Berlin: Reimer.

Hille, B. (2001). *Ion Channels of Excitable Membranes* (3rd ed.). Sinauer Associates.

Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. *Journal of Physiology*, 117(4), 500–544.

Hooke, R. (1665). *Micrographia: or Some Physiological Descriptions of Minute Bodies Made by Magnifying Glasses*. London: J. Martyn and J. Allestry, for the Royal Society.

Kandel, E. R., Koester, J. D., Mack, S. H., & Siegelbaum, S. A. (Eds.). (2021). *Principles of Neural Science* (6th ed.). McGraw-Hill.

Katz, L. C., & Shatz, C. J. (1996). Synaptic activity and the construction of cortical circuits. *Science*, 274(5290), 1133–1138.

Levine, J. (1983). Materialism and qualia: The explanatory gap. *Pacific Philosophical Quarterly*, 64(4), 354–361.

Mergenthaler, P., Lindauer, U., Dienel, G. A., & Meisel, A. (2013). Sugar for the brain: The role of glucose in physiological and pathological brain function. *Trends in Neurosciences*, 36(10), 587–597.

Nelson, D. L., & Cox, M. M. (2021). *Lehninger Principles of Biochemistry* (8th ed.). W. H. Freeman.

Nernst, W. (1889). Die elektromotorische Wirksamkeit der Ionen. *Zeitschrift für physikalische Chemie*, 4, 129–181.

Nirenberg, M. W., & Matthaei, J. H. (1961). The dependence of cell-free protein synthesis in E. coli upon naturally occurring or synthetic polyribonucleotides. *Proceedings of the National Academy of Sciences*, 47(10), 1588–1602.

Pauling, L. (1960). *The Nature of the Chemical Bond* (3rd ed.). Cornell University Press.

Purves, D., Augustine, G. J., Fitzpatrick, D., Hall, W. C., LaMantia, A.-S., Mooney, R. D., Platt, M. L., & White, L. E. (Eds.). (2018). *Neuroscience* (6th ed.). Sinauer Associates.

Radzicka, A., & Wolfenden, R. (1995). A proficient enzyme. *Science*, 267(5194), 90–93.

Schleiden, M. J. (1838). Beiträge zur Phytogenesis. *Archiv für Anatomie, Physiologie und wissenschaftliche Medicin*, 5, 137–176.

Schrödinger, E. (1944). *What Is Life? The Physical Aspect of the Living Cell*. Cambridge University Press.

Schwann, T. (1839). *Mikroskopische Untersuchungen über die Uebereinstimmung in der Structur und dem Wachsthum der Thiere und Pflanzen*. Berlin: Sander. English translation by H. Smith, *Microscopical Researches into the Accordance in the Structure and Growth of Animals and Plants* (Sydenham Society, 1847).

Singer, S. J., & Nicolson, G. L. (1972). The fluid mosaic model of the structure of cell membranes. *Science*, 175(4023), 720–731.

Skou, J. C. (1957). The influence of some cations on an adenosine triphosphatase from peripheral nerves. *Biochimica et Biophysica Acta*, 23, 394–401.

Sperry, R. W. (1963). Chemoaffinity in the orderly growth of nerve fiber patterns and connections. *Proceedings of the National Academy of Sciences*, 50(4), 703–710.

Tessier-Lavigne, M., & Goodman, C. S. (1996). The molecular biology of axon guidance. *Science*, 274(5290), 1123–1133.

Turing, A. M. (1952). The chemical basis of morphogenesis. *Philosophical Transactions of the Royal Society B*, 237(641), 37–72.

Virchow, R. (1858). *Die Cellularpathologie in ihrer Begründung auf physiologische und pathologische Gewebelehre*. Berlin: Hirschwald.

Volta, A. (1800). On the electricity excited by the mere contact of conducting substances of different kinds. *Philosophical Transactions of the Royal Society of London*, 90, 403–431.

Waddington, C. H. (1957). *The Strategy of the Genes*. London: Allen & Unwin.

Watson, J. D., & Crick, F. H. C. (1953). Molecular structure of nucleic acids: A structure for deoxyribose nucleic acid. *Nature*, 171, 737–738.

Whitman, W. B., Coleman, D. C., & Wiebe, W. J. (1998). Prokaryotes: The unseen majority. *Proceedings of the National Academy of Sciences*, 95(12), 6578–6583.

[^1]: Bianconi, E., Piovesan, A., Facchin, F., Beraudi, A., Casadei, R., Frabetti, F., Vitale, L., Pelleri, M. C., Tassani, S., Piva, F., Perez-Amodio, S., Strippoli, P., & Canaider, S. (2013). An estimation of the number of cells in the human body. *Annals of Human Biology*, 40(6), 463–471; Hatton, I. A., Galbraith, E. D., Merleau, N. S. C., Miettinen, T. P., Smith, B. M., & Shander, J. A. (2023). The human cell count and size distribution. *Proceedings of the National Academy of Sciences*, 120(39), e2303077120. Bianconi and colleagues gave the 37 trillion estimate; Hatton and colleagues the 36 trillion and 28 trillion figures.

[^2]: Alberts, B., Heald, R., Johnson, A., Morgan, D., Raff, M., Roberts, K., & Walter, P. (2022). *Molecular Biology of the Cell* (7th ed.). W. W. Norton. Chapter 1.

[^3]: Whitman, W. B., Coleman, D. C., & Wiebe, W. J. (1998). Prokaryotes: The unseen majority. *Proceedings of the National Academy of Sciences*, 95(12), 6578–6583.

[^4]: Alberts, B., Heald, R., Johnson, A., Morgan, D., Raff, M., Roberts, K., & Walter, P. (2022). *Molecular Biology of the Cell* (7th ed.). W. W. Norton. Chapter 1 gives the prokaryote and eukaryote comparison.

[^5]: Helmholtz, H. von (1847). *Über die Erhaltung der Kraft*. Berlin: Reimer; Clausius, R. (1865). Ueber verschiedene für die Anwendung bequeme Formen der Hauptgleichungen der mechanischen Wärmetheorie. *Annalen der Physik und Chemie*, 125, 353–400. Helmholtz gave energy conservation its general form, after earlier statements by Julius Robert Mayer and James Prescott Joule, with physiology among his examples; Clausius named entropy and stated the second law in the form used here.

[^6]: Schrödinger, E. (1944). *What Is Life? The Physical Aspect of the Living Cell*. Cambridge University Press. Chapter 6, "Order, Disorder and Entropy," and its appended note, where Schrödinger says that for physicists he would have let the discussion turn on free energy.

[^7]: Nelson, D. L., & Cox, M. M. (2021). *Lehninger Principles of Biochemistry* (8th ed.). W. H. Freeman. Chapter 13, on the free energy of ATP hydrolysis and why "high-energy bond" is a misnomer.

[^8]: Hille, B. (2001). *Ion Channels of Excitable Membranes* (3rd ed.). Sinauer Associates. Chapter 1 for the ions of excitable membranes and their typical concentrations.

[^9]: Nernst, W. (1889). Die elektromotorische Wirksamkeit der Ionen. *Zeitschrift für physikalische Chemie*, 4, 129–181; Goldman, D. E. (1943). Potential, impedance, and rectification in membranes. *Journal of General Physiology*, 27(1), 37–60. Nernst gave the equilibrium potential for a single ion; Goldman the voltage set by several ions with different permeabilities.

[^10]: Skou, J. C. (1957). The influence of some cations on an adenosine triphosphatase from peripheral nerves. *Biochimica et Biophysica Acta*, 23, 394–401; Hille, B. (2001). *Ion Channels of Excitable Membranes* (3rd ed.). Sinauer Associates. Skou discovered the sodium-potassium pump; Hille gives its three-to-two stoichiometry and the distinction between pumps and channels.

[^11]: Fick, A. (1855). Ueber Diffusion. *Annalen der Physik und Chemie*, 94, 59–86; Einstein, A. (1905). Über die von der molekularkinetischen Theorie der Wärme geforderte Bewegung von in ruhenden Flüssigkeiten suspendierten Teilchen. *Annalen der Physik*, 322(8), 549–560. Fick's law describes the flux; Einstein derived it from random molecular motion.

[^12]: Berg, H. C. (1993). *Random Walks in Biology* (expanded ed.). Princeton University Press.

[^13]: Berg, H. C. (1993). *Random Walks in Biology* (expanded ed.). Princeton University Press. Chapter 1. For a small molecule in water the diffusion coefficient is of the order of one billionth of a square meter per second, which gives roughly a fifth of a microsecond for 20 nanometers, half a millisecond for a micrometer, and about fifteen years for a meter.

[^14]: Pauling, L. (1960). *The Nature of the Chemical Bond* (3rd ed.). Cornell University Press.

[^15]: Watson, J. D., & Crick, F. H. C. (1953). Molecular structure of nucleic acids: A structure for deoxyribose nucleic acid. *Nature*, 171, 737–738; Nelson, D. L., & Cox, M. M. (2021). *Lehninger Principles of Biochemistry* (8th ed.). W. H. Freeman.

[^16]: Anfinsen, C. B. (1973). Principles that govern the folding of protein chains. *Science*, 181(4096), 223–230. Anfinsen's Nobel lecture, summarizing the refolding experiments on ribonuclease.

[^17]: Crick, F. (1970). Central dogma of molecular biology. *Nature*, 227, 561–563.

[^18]: Mergenthaler, P., Lindauer, U., Dienel, G. A., & Meisel, A. (2013). Sugar for the brain: The role of glucose in physiological and pathological brain function. *Trends in Neurosciences*, 36(10), 587–597.

[^19]: Gorter, E., & Grendel, F. (1925). On bimolecular layers of lipoids on the chromocytes of the blood. *Journal of Experimental Medicine*, 41(4), 439–443; Singer, S. J., & Nicolson, G. L. (1972). The fluid mosaic model of the structure of cell membranes. *Science*, 175(4023), 720–731.

[^20]: Radzicka, A., & Wolfenden, R. (1995). A proficient enzyme. *Science*, 267(5194), 90–93. Orotidine 5'-phosphate decarboxylase accelerates its reaction by a factor of about 10^17; the uncatalyzed half-life is 78 million years.

[^21]: Nelson, D. L., & Cox, M. M. (2021). *Lehninger Principles of Biochemistry* (8th ed.). W. H. Freeman. Chapter 6, on enzyme kinetics and turnover numbers.

[^22]: Fischer, E. (1894). Einfluss der Configuration auf die Wirkung der Enzyme. *Berichte der deutschen chemischen Gesellschaft*, 27(3), 2985–2993. The "lock and key" account of specificity.

[^23]: Hooke, R. (1665). *Micrographia: or Some Physiological Descriptions of Minute Bodies Made by Magnifying Glasses*. London: J. Martyn and J. Allestry, for the Royal Society. Observation XVIII, "Of the Schematisme or Texture of Cork."

[^24]: Schleiden, M. J. (1838). Beiträge zur Phytogenesis. *Archiv für Anatomie, Physiologie und wissenschaftliche Medicin*, 5, 137–176; Schwann, T. (1839). *Mikroskopische Untersuchungen über die Uebereinstimmung in der Structur und dem Wachsthum der Thiere und Pflanzen*. Berlin: Sander. English translation by H. Smith, *Microscopical Researches into the Accordance in the Structure and Growth of Animals and Plants* (Sydenham Society, 1847).

[^25]: Virchow, R. (1858). *Die Cellularpathologie in ihrer Begründung auf physiologische und pathologische Gewebelehre*. Berlin: Hirschwald. The maxim *omnis cellula e cellula*, which Virchow popularized from 1855, had been stated by Raspail in 1825.

[^26]: Carnot, S. (1824). *Réflexions sur la puissance motrice du feu et sur les machines propres à développer cette puissance*. Paris: Bachelier; Clausius, R. (1865). Ueber verschiedene für die Anwendung bequeme Formen der Hauptgleichungen der mechanischen Wärmetheorie. *Annalen der Physik und Chemie*, 125, 353–400.

[^27]: Buchner, E. (1897). Alkoholische Gährung ohne Hefezellen. *Berichte der deutschen chemischen Gesellschaft*, 30(1), 117–124.

[^28]: Schrödinger, E. (1944). *What Is Life? The Physical Aspect of the Living Cell*. Cambridge University Press. Schrödinger's book is the classic mid-century statement that living matter obeys the known laws of physics.

[^29]: Galvani, L. (1791). *De viribus electricitatis in motu musculari commentarius*. Bologna: Ex Typographia Instituti Scientiarum. Galvani's experiments began around 1780; the full account was published in 1791.

[^30]: Volta, A. (1800). On the electricity excited by the mere contact of conducting substances of different kinds. *Philosophical Transactions of the Royal Society of London*, 90, 403–431.

[^31]: Hodgkin, A. L., & Huxley, A. F. (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. *Journal of Physiology*, 117(4), 500–544; Hille, B. (2001). *Ion Channels of Excitable Membranes* (3rd ed.). Sinauer Associates. The 1963 Nobel Prize in Physiology or Medicine was shared with John Eccles. Hille, Chapter 2, describes the squid giant axon preparation.

[^32]: Watson, J. D., & Crick, F. H. C. (1953). Molecular structure of nucleic acids: A structure for deoxyribose nucleic acid. *Nature*, 171, 737–738; Nirenberg, M. W., & Matthaei, J. H. (1961). The dependence of cell-free protein synthesis in E. coli upon naturally occurring or synthetic polyribonucleotides. *Proceedings of the National Academy of Sciences*, 47(10), 1588–1602; Crick, F. H. C., Barnett, L., Brenner, S., & Watts-Tobin, R. J. (1961). General nature of the genetic code for proteins. *Nature*, 192, 1227–1232.

[^33]: Azevedo, F. A. C., Carvalho, L. R. B., Grinberg, L. T., Farfel, J. M., Ferretti, R. E. L., Leite, R. E. P., Jacob Filho, W., Lent, R., & Herculano-Houzel, S. (2009). Equal numbers of neuronal and nonneuronal cells make the human brain an isometrically scaled-up primate brain. *Journal of Comparative Neurology*, 513(5), 532–541; Kandel, E. R., Koester, J. D., Mack, S. H., & Siegelbaum, S. A. (Eds.). (2021). *Principles of Neural Science* (6th ed.). McGraw-Hill. Kandel and colleagues, Chapter 7, for the functions of glia.

[^34]: Barresi, M. J. F., & Gilbert, S. F. (2019). *Developmental Biology* (12th ed.). Sinauer Associates.

[^35]: Waddington, C. H. (1957). *The Strategy of the Genes*. London: Allen & Unwin. Waddington's "epigenetic landscape" is the standard image of progressively restricted cell fate.

[^36]: Alberts, B., Heald, R., Johnson, A., Morgan, D., Raff, M., Roberts, K., & Walter, P. (2022). *Molecular Biology of the Cell* (7th ed.). W. W. Norton. Chapter 15 classifies contact-dependent, paracrine, synaptic, and endocrine signaling as separate modes.

[^37]: Turing, A. M. (1952). The chemical basis of morphogenesis. *Philosophical Transactions of the Royal Society B*, 237(641), 37–72; Camazine, S., Deneubourg, J.-L., Franks, N. R., Sneyd, J., Theraulaz, G., & Bonabeau, E. (2001). *Self-Organization in Biological Systems*. Princeton University Press.

[^38]: Sperry, R. W. (1963). Chemoaffinity in the orderly growth of nerve fiber patterns and connections. *Proceedings of the National Academy of Sciences*, 50(4), 703–710; Cang, J., & Feldheim, D. A. (2013). Developmental mechanisms of topographic map formation and alignment. *Annual Review of Neuroscience*, 36, 51–77. Sperry's chemoaffinity hypothesis; Cang and Feldheim review the Eph receptor and ephrin gradients that implement it.

[^39]: Hebb, D. O. (1949). *The Organization of Behavior: A Neuropsychological Theory*. New York: Wiley; Katz, L. C., & Shatz, C. J. (1996). Synaptic activity and the construction of cortical circuits. *Science*, 274(5290), 1133–1138. "Fire together, wire together" paraphrases Hebb's postulate; Katz and Shatz review spontaneous retinal waves and activity-dependent refinement.

[^40]: Cang, J., & Feldheim, D. A. (2013). Developmental mechanisms of topographic map formation and alignment. *Annual Review of Neuroscience*, 36, 51–77. Mice lacking normal retinal waves form a coarse map whose arbors fail to refine.

[^41]: Tessier-Lavigne, M., & Goodman, C. S. (1996). The molecular biology of axon guidance. *Science*, 274(5290), 1123–1133; Katz, L. C., & Shatz, C. J. (1996). Synaptic activity and the construction of cortical circuits. *Science*, 274(5290), 1133–1138.

[^42]: Levine, J. (1983). Materialism and qualia: The explanatory gap. *Pacific Philosophical Quarterly*, 64(4), 354–361; Chalmers, D. J. (1995). Facing up to the problem of consciousness. *Journal of Consciousness Studies*, 2(3), 200–219.

[^43]: Kandel, E. R., Koester, J. D., Mack, S. H., & Siegelbaum, S. A. (Eds.). (2021). *Principles of Neural Science* (6th ed.). McGraw-Hill; Purves, D., Augustine, G. J., Fitzpatrick, D., Hall, W. C., LaMantia, A.-S., Mooney, R. D., Platt, M. L., & White, L. E. (Eds.). (2018). *Neuroscience* (6th ed.). Sinauer Associates.
