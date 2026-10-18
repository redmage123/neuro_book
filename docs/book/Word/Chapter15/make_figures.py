#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 15 (A Coherent Model of the Human Brain). Outputs into ./images.
Requires matplotlib and numpy. Figure 15.4 plots published counts; the others are schematic."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).parent / "images"; OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
EXC, INH, GRAY, GOLD, GREEN = "#1f4e79", "#b03a2e", "#555555", "#c9a227", "#2e7d32"


def arrow(ax, a, b, color=GRAY, lw=1.5, style="-|>", ls="-", cs=None):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, color=color, lw=lw, linestyle=ls, mutation_scale=12,
                                 shrinkA=0, shrinkB=0, connectionstyle=cs or "arc3,rad=0"))


def box(ax, x, y, w, h, text, fc="white", ec=GRAY, color="black", fs=9, weight="normal"):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.08", fc=fc, ec=ec, lw=1.2))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=color, weight=weight)


def save(fig, name):
    fig.savefig(OUT / name, dpi=200, bbox_inches="tight", facecolor="white"); plt.close(fig)


def clean(ax):
    ax.spines[["top", "right"]].set_visible(False)


def fig_model():
    fig, ax = plt.subplots(figsize=(10, 6.6)); ax.set_xlim(0, 10); ax.set_ylim(0, 6.85); ax.axis("off")
    box(ax, 5.6, 6.45, 8.4, 0.5, "history: parts inherited from ancestors that solved other problems (Ch. 13)", fc="#f6efd6", ec=GOLD, fs=9)
    box(ax, 0.55, 3.55, 0.8, 5.0, "constraints\n\nenergy\n\nspace\nand\nwire\n\ntime\n\nnoise\n\ngenome\n(Ch. 1, 2, 13)", fc="#f3f3f3", ec=GRAY, fs=8.2)
    box(ax, 5.6, 0.55, 8.4, 0.55, "a body in a world: needs, set points, actions and their consequences (Ch. 1, 7)", fc="#eeeeee", ec=GRAY, fs=9.2)
    box(ax, 2.9, 2.0, 2.5, 0.8, "prediction meets input\n(Ch. 6, 12)", fc="#e8eef5", ec=EXC)
    box(ax, 2.9, 3.6, 2.5, 0.8, "errors of several kinds:\nsurprise, reward, movement", fc="#e8eef5", ec=EXC)
    box(ax, 2.9, 5.3, 2.5, 0.9, "neuromodulators broadcast\nand set the learning rate\n(Ch. 3)", fc="#f7e6e4", ec=INH)
    box(ax, 6.0, 5.3, 2.4, 0.9, "local plasticity, kept\nonly when gated\n(three factors; Ch. 3, 5)", fc="#f7e6e4", ec=INH)
    box(ax, 6.0, 3.6, 2.4, 1.0, "fast store (hippocampus)\n⇅ replay in sleep\nslow cortex (Ch. 5)", fc="white", ec=GRAY)
    box(ax, 8.65, 3.6, 2.0, 1.0, "value → choice\n→ habit\n(Ch. 8, 9)", fc="white", ec=GRAY)
    box(ax, 8.65, 2.0, 2.0, 0.8, "action\n(Ch. 4, 9)", fc="white", ec=GRAY)
    arrow(ax, (2.9, 0.85), (2.9, 1.55), color=GRAY); ax.text(2.0, 1.15, "input", fontsize=8.5, color=GRAY)
    arrow(ax, (2.9, 2.42), (2.9, 3.17), color=EXC)
    arrow(ax, (2.9, 4.02), (2.9, 4.82), color=EXC)
    arrow(ax, (4.2, 5.3), (4.75, 5.3), color=INH)
    arrow(ax, (6.0, 4.82), (6.0, 4.13), color=INH)
    arrow(ax, (7.25, 3.6), (7.62, 3.6), color=GRAY)
    arrow(ax, (8.65, 3.07), (8.65, 2.42), color=GRAY)
    arrow(ax, (8.65, 1.58), (8.65, 0.85), color=GRAY)
    arrow(ax, (4.75, 3.45), (4.18, 2.2), color=EXC, ls="--"); ax.text(4.95, 2.45, "memories shape\nthe next prediction", fontsize=7.8, color=EXC, ha="left")
    arrow(ax, (7.7, 0.85), (7.7, 3.0), color=GRAY, ls="--", cs="arc3,rad=0.0"); ax.text(7.55, 1.3, "the body sets\nwhat is valuable", fontsize=7.8, color=GRAY, ha="right")
    fig.tight_layout(); save(fig, "fig_model.png")


STATEMENTS = ["1. a controller of a body", "2. slow, noisy, costly parts", "3. it predicts", "4. local change, global gating",
              "5. several memory systems", "6. value, choice, habit", "7. built by rules, finished by experience",
              "8. compromise and inheritance"]
SUPPORT = {0: [2, 7], 1: [1, 2, 5, 7, 8], 2: [2, 4], 3: [3, 4, 6, 8], 4: [8, 6], 5: [4, 5], 6: [3, 7], 7: [1, 3, 6],
           8: [3, 6], 9: [5, 6, 3], 10: [4, 5, 7], 11: [4, 5], 12: [3, 5, 1], 13: [2, 7, 8], 14: [5, 6]}


def fig_matrix():
    fig, ax = plt.subplots(figsize=(9.6, 4.6))
    M = np.zeros((8, 15))
    for ch, sts in SUPPORT.items():
        for s in sts: M[s - 1, ch] = 1
    for i in range(8):
        for j in range(15):
            ax.add_patch(plt.Rectangle((j, 7 - i), 0.9, 0.85, fc=EXC if M[i, j] else "#eeeeee", ec="white"))
    ax.set_xlim(-0.1, 15); ax.set_ylim(-0.1, 8)
    ax.set_xticks(np.arange(15) + 0.45); ax.set_xticklabels([str(c) for c in range(15)])
    ax.set_yticks(np.arange(8) + 0.42); ax.set_yticklabels(STATEMENTS[::-1])
    ax.set_xlabel("chapter"); ax.tick_params(length=0)
    for s in ax.spines.values(): s.set_visible(False)
    fig.tight_layout(); save(fig, "fig_matrix.png")


STEPS = [(1e-3, 1e-1, "spikes and prediction errors", "2, 6"),
         (0.3, 2, "dopamine arrives within the eligibility trace", "3"),
         (60, 3600, "cerebellar recalibration; early potentiation", "5, 9"),
         (3600, 3 * 3600, "new proteins make changes last", "5"),
         (6 * 3600, 9 * 3600, "sleep: replay to the cortex", "5"),
         (7 * 86400, 60 * 86400, "control shifts to habit; chunking", "9"),
         (90 * 86400, 5 * 365 * 86400, "the old habit kept as a latent context;\nsavings on relearning", "7, 9, 12")]


def fig_timescales():
    fig, ax = plt.subplots(figsize=(9.8, 4.6))
    for i, (a, b, lab, ch) in enumerate(STEPS):
        y = len(STEPS) - i
        ax.plot([a, b], [y, y], color=EXC, lw=7, solid_capstyle="round")
        ax.text(b * 1.8, y, f"{lab}  (Ch. {ch})", va="center", fontsize=8.8)
    ax.set_xscale("log"); ax.set_xlim(5e-4, 5e11); ax.set_yticks([]); ax.set_ylim(0.3, len(STEPS) + 0.7)
    ticks = [1e-3, 1, 60, 3600, 86400, 30 * 86400, 365 * 86400]
    ax.set_xticks(ticks); ax.set_xticklabels(["1 ms", "1 s", "1 min", "1 h", "1 day", "1 month", "1 year"])
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.set_xlabel("time after the first attempt (log scale)")
    fig.tight_layout(); save(fig, "fig_timescales.png")


CONN = [("nematode worm\n(whole)", 302, 7e3),
        ("fruit fly brain\n(FlyWire)", 139255, 54.5e6),
        ("1 mm³ mouse cortex\n(MICrONS; cells)", 200000, 0.5e9),
        ("1 mm³ human cortex\n(H01)", 16087, 149.9e6),
        ("whole human brain\n(estimates)", 86e9, 1.64e14)]


def fig_connectomes():
    fig, ax = plt.subplots(figsize=(9.0, 4.4))
    x = np.arange(len(CONN)); w = 0.38
    n = [c[1] for c in CONN]; s = [c[2] for c in CONN]
    ax.bar(x - w / 2, n, w, color=EXC, label="neurons (cells, for the mouse sample)", log=True)
    ax.bar(x + w / 2, s, w, color=GOLD, label="synapses (neocortex only, for the whole brain)", log=True)
    nl = ["302", "139,255", "over 200,000", "16,087", "86 billion"]
    sl = ["about 7,000", "54.5 million", "about 0.5 billion", "150 million", "164 trillion"]
    for xi, v, lab in zip(x - w / 2, n, nl):
        ax.text(xi, v * 1.6, lab, ha="center", fontsize=7.8, rotation=90, va="bottom")
    for xi, v, lab in zip(x + w / 2, s, sl):
        ax.text(xi, v * 1.6, lab, ha="center", fontsize=7.8, rotation=90, va="bottom")
    ax.set_xticks(x); ax.set_xticklabels([c[0] for c in CONN], fontsize=8.5)
    ax.set_ylim(10, 1e19); ax.set_ylabel("count (log scale)"); clean(ax)
    ax.legend(frameon=False, fontsize=8.5, loc="upper left")
    fig.tight_layout(); save(fig, "fig_connectomes.png")


LEDGER = [("Settled", EXC, ["memories stored in changes among particular cells\n   (mostly from work in rodents)",
                            "dopamine neurons signal reward prediction errors",
                            "a fast memory system and a slow one",
                            "energy constrains how the brain codes and wires",
                            "adaptation to the input at every level",
                            "neuromodulators reconfigure fixed wiring\n   (shown mainly in small circuits)"]),
          ("Probable", GRAY, ["prediction as a general strategy of the cortex",
                              "three-factor learning rules throughout the cortex",
                              "sleep consolidates memories through replay",
                              "practice shifts control toward habit circuits",
                              "value is anchored to the body's state"]),
          ("Open", GOLD, ["how the cortex assigns credit",
                          "how much single neurons compute",
                          "what sleep does to synapses",
                          "the role of glia in learning",
                          "whether memories also live in molecules",
                          "whether one principle lies beneath it all"]),
          ("Beyond this book", INH, ["how any of this gives rise to conscious experience"])]


def fig_settled():
    fig, ax = plt.subplots(figsize=(9.8, 6.4)); ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    pos = [(0.15, 9.8, 4.75, 5.0), (5.1, 9.8, 4.75, 5.0), (0.15, 4.6, 4.75, 4.5), (5.1, 4.6, 4.75, 4.5)]
    for (title, c, items), (x0, y0, w, h) in zip(LEDGER, pos):
        ax.add_patch(FancyBboxPatch((x0, y0 - h), w, h, boxstyle="round,pad=0.05", fc="white", ec=c, lw=1.8))
        ax.text(x0 + 0.2, y0 - 0.4, title, fontsize=11, weight="bold", color=c, va="center")
        for j, it in enumerate(items):
            ax.text(x0 + 0.25, y0 - 1.05 - j * 0.62, "• " + it, fontsize=8.6, va="center")
    fig.tight_layout(); save(fig, "fig_settled.png")


if __name__ == "__main__":
    fig_model(); fig_matrix(); fig_timescales(); fig_connectomes(); fig_settled()
