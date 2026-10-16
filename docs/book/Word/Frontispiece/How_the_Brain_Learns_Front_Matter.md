---
title: "How the Brain Learns"
subtitle: "A Systems-Level Introduction to Neuroscience for Engineers and Technologists"
---

![Santiago Ramón y Cajal (1852--1934), pioneer of modern neuroscience.](images/cajal_portrait.png){width="3in"}

> *"Every man can, if he so desires, become the sculptor of his own brain."*
>
> --- Santiago Ramón y Cajal

# Preface

This book is written for readers who are already technically literate but who have never been formally trained in neuroscience. If you are a software engineer, physicist, mathematician, data scientist, or practitioner in a neighboring technical field, you already possess many of the intellectual tools required to understand the brain. What you may lack is not ability, but orientation.

The central aim of this book is to replace metaphor with mechanism. Wherever possible, explanations are grounded in physical processes that occur in living tissue: the movement of ions, the opening and closing of channels, the release of chemicals, and the slow structural changes that follow experience.

Throughout this book, the brain is treated as an adaptive biological control system. It is not a computer in the conventional sense, nor is it a passive information-processing device. Its primary objective is viability---remaining functional under uncertainty.

This perspective has important consequences. Learning is not instantaneous because physical change is slow and metabolically expensive. Forgetting is not a failure of memory, but a necessary feature of a system that must remain flexible.

The book is organized cumulatively, beginning with the physical foundations of neural signaling and building toward cognition and intelligence.

This is not a book about neuroscience as a collection of facts. It is a book about neuroscience as a way of explaining behavior.

If, by the end of this book, you can explain why the brain uses spikes rather than continuous signals and why learning must be regulated, you will have acquired a coherent mental model of how the human brain works.

# How to Use This Book

This book is designed to be read sequentially. Unlike reference manuals or survey texts, its chapters build upon one another in a deliberate order. Later discussions rely on mechanisms, constraints, and distinctions introduced earlier, often implicitly. Skipping ahead may create the impression of understanding while quietly weakening the causal chain that gives the subject coherence.

Neuroscience spans multiple levels of explanation, from molecular processes to behavior and experience. This book moves between those levels repeatedly, but it does so in a controlled way. When a concept is introduced at a higher level, it is eventually anchored to mechanisms at lower levels.

Technically trained readers often bring powerful habits of abstraction to new domains. These habits are an asset, but they can also become a liability if applied too early. Biological systems are constrained in ways that engineered systems are not.

Each chapter is written to be read twice. The first pass should be uninterrupted and relatively quick, with the goal of understanding the narrative arc. The second pass should be slower and more critical, with attention paid to how explanations are grounded in physical processes.

A companion volume, *Student Notes and Laboratory Exercises for How the Brain Learns*, accompanies this text. The companion volume provides summaries, annotated diagrams, and laboratory-style exercises to reinforce understanding.

The book does not assume memorization as a primary learning strategy. Terminology is introduced sparingly and reused consistently.

Finally, this book rewards patience. Biological intelligence is not optimized for transparency, and many of its solutions appear indirect when viewed through an engineering lens.

# Contents

Preface\
How to Use This Book

**Part I --- Physical Foundations of Neural Computation**\
Chapter 1 What the Brain Is (and Is Not)\
Chapter 2 Neurons: The Brain's Signaling Cells\
Chapter 3 Electricity in Living Tissue\
Chapter 4 Action Potentials: How Neurons Signal

**Part II --- Chemical Communication and the Regulation of Learning**\
Chapter 5 Synapses: Where Neurons Communicate\
Chapter 6 Excitation, Inhibition, and Stability\
Chapter 7 Neuromodulators: The Brain's Control Signals\
Chapter 8 How the Brain Decides What to Learn

**Part III --- Plasticity and Memory**\
Chapter 9 Plasticity: How Experience Changes the Brain\
Chapter 10 Memory Is Not Storage\
Chapter 11 Habits, Skills, and Automaticity

**Part IV --- Perception, Emotion, and Decision-Making**\
Chapter 12 Perception as Inference\
Chapter 13 Emotion as a Regulatory System\
Chapter 14 Decision-Making Under Uncertainty

**Part V --- From Biological Brains to Artificial Systems**\
Chapter 15 What Artificial Intelligence Gets Right---and Wrong\
Chapter 16 Integrating Brain Mechanisms into AI Models

**Part VI --- Integration and Implications**\
Chapter 17 The Brain as a Predictive, Adaptive System\
Chapter 18 Why the Brain Works the Way It Does\
Chapter 19 Implications for Learning, Work, and Technology\
Chapter 20 A Coherent Model of the Human Brain

Glossary\
References\
Index

# A Note on Levels of Explanation

One of the greatest sources of confusion in neuroscience---and in discussions about the brain more generally---comes from a failure to distinguish between different levels of explanation. Intelligent readers often assume that disagreement reflects uncertainty or lack of rigor, when in fact it reflects the fact that different questions are being answered at different levels.

At the most basic level, the brain is a physical system governed by the laws of physics and chemistry. Ions move according to electrochemical gradients. Proteins change shape. Chemical reactions occur with finite speed and nonzero error rates.

At the next level are cells---neurons and glial cells---and their immediate interactions. Here we describe how neurons integrate inputs, generate spikes, and modify their connections in response to activity.

Above the cellular level lies the level of circuits and systems. At this scale, we consider populations of neurons and the patterns of activity they sustain.

At the highest level commonly discussed are cognitive and behavioral descriptions. Here we use terms such as perception, memory, attention, emotion, and decision-making.

Problems arise when levels are mixed without acknowledgment. Explaining a behavioral phenomenon by invoking a neurotransmitter without specifying the circuit in which it operates conflates molecular and systems-level explanations.

This book moves deliberately between levels of explanation, but it does so with care.

Understanding levels of explanation is not a preliminary technicality; it is a foundational skill.

# Glossary

Action potential (spike)

:   A brief, all-or-none electrical event generated by a neuron when its membrane voltage crosses a critical threshold. Action potentials propagate along axons and serve as the primary means by which neurons transmit signals over long distances. Information is carried not by the size of the spike, but by its timing and pattern.

Axon

:   A long, slender projection of a neuron specialized for transmitting action potentials to other neurons or target cells.

Behavior

:   Observable actions or responses of an organism to internal or external conditions.

Circuit

:   A group of interconnected neurons whose collective activity performs a specific transformation or regulatory function.

Cognition

:   Processes such as perception, memory, reasoning, and decision-making, treated here as emergent descriptions of neural dynamics.

Dendrite

:   Branching extensions of a neuron specialized for receiving synaptic input.

Excitation

:   Neural processes that increase the likelihood that a neuron will fire an action potential.

Inhibition

:   Neural processes that decrease the likelihood that a neuron will fire, essential for stability and selectivity.

Learning

:   A lasting physical change in neural structure or function that alters future behavior as a result of experience.

Memory

:   The capacity of a system to behave differently because of past experience.

Neuron

:   A specialized cell that processes and transmits information using electrical and chemical signals.

Neuromodulator

:   A chemical signal that alters circuit state and regulates when and how learning occurs.

Plasticity

:   Biological mechanisms that enable learning by changing synaptic strength, excitability, or structure.

Prediction

:   The brain's use of prior experience to anticipate future sensory input or outcomes.

Representation

:   An explanatory description summarizing regularities in neural activity, not a physical stored object.

Stability

:   The ability of a neural system to maintain functional operation despite noise and perturbation.

Synapse

:   The specialized junction through which one neuron communicates with another.

Threshold

:   The membrane voltage at which a neuron generates an action potential.
