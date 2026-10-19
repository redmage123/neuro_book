---
title: "How the Brain Learns"
subtitle: "A Systems-Level Introduction to Neuroscience for Engineers and Technologists"
---

![Santiago Ramón y Cajal (1852--1934), pioneer of modern neuroscience.](images/cajal_portrait.png){width="3in"}

> *"Every man can, if he so desires, become the sculptor of his own brain."*
>
> --- Santiago Ramón y Cajal, *Reglas y consejos sobre investigación científica* (preface to the second edition, 1898)

# Preface

This book is written for readers who are already technically literate but who have never been formally trained in neuroscience. If you are a software engineer, physicist, mathematician, data scientist, or practitioner in a neighboring technical field, you already possess many of the intellectual tools required to understand the brain. What you may lack is not ability, but orientation.

The central aim of this book is to replace metaphor with mechanism. Wherever possible, explanations are grounded in physical processes that occur in living tissue: the movement of ions, the opening and closing of channels, the release of chemicals, and the slow structural changes that follow experience.

Throughout this book, the brain is treated as an adaptive biological control system. It is not a computer in the conventional sense, nor is it a passive information-processing device. Its primary objective is viability: remaining functional under uncertainty.

This perspective has important consequences. Learning is not instantaneous because physical change is slow and metabolically expensive. Forgetting is not a failure of memory, but a necessary feature of a system that must remain flexible.

The book is organized cumulatively, in six parts. Part I lays the foundations: the physics and chemistry that any living system must obey (Chapter 0, which readers comfortable with both may skim), what kind of system the brain is, and how its cells signal. Part II describes the machinery of learning: the chemical signals that decide when learning happens, the circuits in which it happens, and the plasticity that stores it. Part III builds upward to perception, emotion, decision, and habit. Part IV holds the brain up against machine learning, asking what artificial intelligence gets right and wrong and what it could borrow. Part V draws the threads together: whether one principle lies beneath the mechanisms, why the brain is built the way it is, what its design asks of schools, workplaces, and technology, and finally a single model of how the brain learns. Part VI is a case study: an attempt to build a brain from the book's principles, and what its failures teach.

This is not a book about neuroscience as a collection of facts. It is a book about neuroscience as a way of explaining behavior.

If, by the end of this book, you can explain why the brain uses spikes rather than continuous signals and why learning must be regulated, you will have acquired a coherent mental model of how the human brain works.

# How to Use This Book

This book is designed to be read sequentially. Unlike reference manuals or survey texts, its chapters build upon one another in a deliberate order. Later discussions rely on mechanisms, constraints, and distinctions introduced earlier, often implicitly. Skipping ahead may create the impression of understanding while quietly weakening the causal chain that gives the subject coherence.

Neuroscience spans multiple levels of explanation, from molecular processes to behavior and experience. This book moves between those levels repeatedly, but it does so in a controlled way. When a concept is introduced at a higher level, it is eventually anchored to mechanisms at lower levels.

Technically trained readers often bring powerful habits of abstraction to new domains. These habits are an asset, but they can also become a liability if applied too early. Biological systems are constrained in ways that engineered systems are not.

Each chapter is written to be read twice. The first pass should be uninterrupted and relatively quick, with the goal of understanding the narrative arc. The second pass should be slower and more critical, with attention paid to how explanations are grounded in physical processes.

A companion volume, *Student Notes and Labs*, accompanies this text. For each of Chapters 1 to 16 it provides a summary of the chapter's argument and a set of laboratory exercises, most of which can be worked by hand or with a few lines of code; printed check values let you confirm your work as you go. An instructor's answer key gives worked solutions and model answers.

The book does not assume memorization as a primary learning strategy. Terminology is introduced sparingly and reused consistently.

Finally, this book rewards patience. Biological intelligence is not optimized for transparency, and many of its solutions appear indirect when viewed through an engineering lens.

# Contents

Preface\
How to Use This Book\
A Note on Levels of Explanation

**Part I: Foundations**\
Chapter 0. Foundations: The Physical and Chemical Basis of Life\
Chapter 1. What the Brain Is (and Is Not)\
Chapter 2. Neurons: The Brain's Signaling Cells

**Part II: The Machinery of Learning**\
Chapter 3. Neuromodulation: How Chemical Context Shapes Learning and Behavior\
Chapter 4. Circuits, Networks, and Coordinated Behavior\
Chapter 5. Plasticity and Memory: How Experience Becomes Structure

**Part III: Mind and Behavior**\
Chapter 6. Perception as Inference: How the Brain Sees What It Expects\
Chapter 7. Emotion and the Body: How Internal States Tell the Brain What Matters\
Chapter 8. Decision-Making Under Uncertainty: How the Brain Chooses When It Cannot Be Sure\
Chapter 9. Habits, Skills, and Automaticity: How Practice Turns Choices into Routines

**Part IV: Brains and Machines**\
Chapter 10. What Artificial Intelligence Gets Right and Wrong: Machine Learning Measured Against the Brain\
Chapter 11. Integrating Brain Mechanisms into AI Models: What Machines Could Borrow from Biology

**Part V: Synthesis**\
Chapter 12. The Brain as a Predictive, Adaptive System: Is There One Principle Beneath the Mechanisms?\
Chapter 13. Why the Brain Works the Way It Does: Constraints, Trade-offs, and the Shape of a Solution\
Chapter 14. Implications for Learning, Work, and Technology: What the Brain's Design Asks of the World We Have Built\
Chapter 15. A Coherent Model of the Human Brain: How the Pieces Fit

**Part VI: A Case Study**\
Chapter 16. NIMCP: Building a Brain from the Book's Principles

Glossary\
Bibliography\
Index

# A Note on Levels of Explanation

One of the greatest sources of confusion in neuroscience, and in discussions about the brain more generally, comes from a failure to distinguish between different levels of explanation. Intelligent readers often assume that disagreement reflects uncertainty or lack of rigor, when in fact it reflects the fact that different questions are being answered at different levels.

At the most basic level, the brain is a physical system governed by the laws of physics and chemistry. Ions move according to electrochemical gradients. Proteins change shape. Chemical reactions occur with finite speed and nonzero error rates.

At the next level are cells (neurons and glial cells) and their immediate interactions. Here we describe how neurons integrate inputs, generate spikes, and modify their connections in response to activity.

Above the cellular level lies the level of circuits and systems. At this scale, we consider populations of neurons and the patterns of activity they sustain.

At the highest level commonly discussed are cognitive and behavioral descriptions. Here we use terms such as perception, memory, attention, emotion, and decision-making.

Problems arise when levels are mixed without acknowledgment. Explaining a behavioral phenomenon by invoking a neurotransmitter without specifying the circuit in which it operates conflates molecular and systems-level explanations.

This book moves deliberately between levels of explanation, but it does so with care.

Understanding levels of explanation is not a preliminary technicality; it is a foundational skill.
