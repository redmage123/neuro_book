#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 16 (NIMCP). Outputs into ./images.
Requires matplotlib and numpy. Figure 16.3 is computed; Figures 16.4 and 16.5 plot measurements and published
counts; Figures 16.1 and 16.2 are schematic summaries of the NIMCP source code as surveyed in October 2026."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).parent / "images"; OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
EXC, INH, GRAY, GOLD = "#1f4e79", "#b03a2e", "#555555", "#c9a227"


def arrow(ax, a, b, color=GRAY, lw=1.5, style="-|>", ls="-"):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, color=color, lw=lw, linestyle=ls, mutation_scale=12, shrinkA=0, shrinkB=0))


def box(ax, x, y, w, h, text, fc="white", ec=GRAY, fs=8.8, weight="normal"):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.08", fc=fc, ec=ec, lw=1.2))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, weight=weight)


def save(fig, name):
    fig.savefig(OUT / name, dpi=200, bbox_inches="tight", facecolor="white"); plt.close(fig)


def clean(ax):
    ax.spines[["top", "right"]].set_visible(False)


def fig_architecture():
    fig, ax = plt.subplots(figsize=(10, 5.4)); ax.set_xlim(0, 10); ax.set_ylim(1.0, 6.6); ax.axis("off")
    box(ax, 1.4, 5.7, 2.4, 0.8, "pretrained encoders\n(sentence embeddings;\nimage and audio networks)", fc="#f3f3f3")
    box(ax, 1.4, 4.4, 2.4, 0.8, "curriculum and \"parent\"\n(scripted stages;\nan LLM as teacher)", fc="#f3f3f3")
    box(ax, 5.0, 5.7, 3.6, 0.8, "gradient-trained networks\n(150,000-unit ANN and others;\nbackpropagation, AdamW)", fc="#e8eef5", ec=EXC)
    box(ax, 5.0, 3.55, 3.6, 1.5, "spiking substrate\n~2 million LIF neurons, ~1.5 billion synapses\n8-tier hierarchy, AMPA/NMDA/GABA,\nPV/SOM/VIP interneurons, Broca and Wernicke\npopulations; reward-gated Hebbian rule;\nfiring-rate homeostasis", fc="#e8eef5", ec=EXC)
    box(ax, 8.6, 5.0, 2.4, 1.2, "algorithmic \"regions\"\nhippocampus, amygdala,\nbasal ganglia, VTA,\nhypothalamus, etc.", fc="#f7e6e4", ec=INH)
    box(ax, 8.6, 3.2, 2.4, 1.0, "six neuromodulators\n(set mainly from\ntraining loss)", fc="#f7e6e4", ec=INH)
    box(ax, 5.0, 1.55, 3.6, 0.8, "sleep: prioritized replay, REM blends,\nsurprise-gated memory store", fc="white")
    box(ax, 8.6, 1.55, 2.4, 0.8, "safety: locked rules,\nlocked drive set points,\naudit log, watchdog", fc="#f6efd6", ec=GOLD)
    box(ax, 1.4, 2.4, 2.4, 1.0, "output: grounded lexicon,\nrule-based grammar\ncorrection (a separate\nLLM in some interfaces)", fc="#f3f3f3")
    arrow(ax, (2.62, 5.7), (3.18, 5.7)); arrow(ax, (2.62, 4.4), (3.18, 5.4))
    arrow(ax, (5.0, 5.28), (5.0, 4.32), style="<|-|>", color=EXC); ax.text(5.1, 4.8, "rate-spike bridges", fontsize=8, color=EXC)
    arrow(ax, (7.38, 5.0), (6.82, 4.1), style="<|-|>", color=INH); arrow(ax, (7.38, 3.2), (6.82, 3.4), color=INH)
    arrow(ax, (5.0, 2.78), (5.0, 1.97), style="<|-|>"); arrow(ax, (3.18, 3.0), (2.62, 2.6))
    ax.text(0.2, 6.4, "gray: borrowed or scripted components    blue: learning networks    red: modules and modulators", fontsize=8, color=GRAY)
    fig.tight_layout(); save(fig, "fig_architecture.png")


ROWS = [("1. serves a body", "hypothalamic drives with set points; no simulated body", "partial"),
        ("2. built from poor parts", "conductance-based LIF neurons; sparse, noisy spiking", "running"),
        ("3. predicts", "predictive-coding hierarchy; world-model trainer disconnected", "partial"),
        ("4. learns locally, keeps globally", "reward-gated Hebbian rule; eligibility traces not reaching\nthe large network; most learning by backpropagation", "partial"),
        ("5. remembers on several clocks", "surprise-gated store, sleep replay, REM blends; one network,\nnot fast and slow systems; EWC not connected", "partial"),
        ("6. value, action, habit", "basal ganglia module registers habits during training\nbut never selects the system's actions", "partial"),
        ("7. grown, not specified", "staged curriculum with an LLM as parent; generic random\nhierarchy as the starting point", "partial"),
        ("8. compromise and inheritance", "no evolutionary prior; constraints are GPU memory and\nhost memory, not energy", "absent")]
COL = {"running": EXC, "partial": GOLD, "present, not wired": "#d98c5f", "absent": INH}


def fig_status():
    fig, ax = plt.subplots(figsize=(10.2, 5.6)); ax.set_xlim(0, 10.2); ax.set_ylim(0, len(ROWS) + 0.9); ax.axis("off")
    for x, t in [(1.35, "statement (Chapter 15)"), (5.6, "what NIMCP contains"), (9.35, "status")]:
        ax.text(x, len(ROWS) + 0.45, t, ha="center", fontsize=9.5, weight="bold", color=GRAY)
    for i, (s, what, st) in enumerate(ROWS):
        y = len(ROWS) - i - 0.3
        ax.text(0.05, y, s, va="center", fontsize=9)
        ax.text(2.9, y, what, va="center", fontsize=8.5)
        ax.add_patch(FancyBboxPatch((8.6, y - 0.28), 1.5, 0.56, boxstyle="round,pad=0.04", fc=COL[st], ec="none", alpha=0.85))
        ax.text(9.35, y, st, ha="center", va="center", fontsize=8.3, color="white", weight="bold")
    fig.tight_layout(); save(fig, "fig_status.png")


def credit_sim(delay, rule, n=20, cue_len=3, trials=300, p_bg=0.05, tau=8.0, seed=0):
    """Toy credit assignment. On each trial one cue synapse (index 0 is the cue that predicts reward) is active
    for cue_len steps together with the action neuron; reward arrives `delay` steps after cue onset. Other synapses
    fire at random (p_bg). Coincidence rule: weights change only for synapses active at the reward step.
    Trace rule: each synapse keeps a trace that decays with time constant tau; reward multiplies the trace."""
    rng = np.random.default_rng(seed)
    w = np.zeros(n)
    for _ in range(trials):
        steps = max(delay, cue_len) + 1
        act = rng.random((steps, n)) < p_bg
        act[:cue_len, 0] = True
        e = np.zeros(n)
        for t in range(steps):
            e = e * np.exp(-1.0 / tau) + act[t]
            if t == delay:
                if rule == "coincidence":
                    w += 0.01 * act[t]
                else:
                    w += 0.01 * e
    return w[0] / max(w[1:].mean(), 1e-9), w[0]


def fig_credit():
    delays = np.arange(0, 21)
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.8, 3.8))
    res = {}
    for rule, c, lab in [("coincidence", INH, "coincidence rule (pre and post active\nwhen reward arrives)"), ("trace", EXC, "eligibility trace (τ = 8 steps)")]:
        sel = []; raw = []
        for d in delays:
            s, r = credit_sim(d, rule); sel.append(s); raw.append(r)
        res[rule] = (sel, raw)
        a.plot(delays, raw, "o-", color=c, ms=4, label=lab)
        b.semilogy(delays, sel, "o-", color=c, ms=4, label=lab)
    for ax in (a, b):
        ax.set_xticks(range(0, 21, 2)); ax.axvline(2.5, color=GRAY, ls=":", lw=1); ax.set_xlabel("delay from cue onset to reward (steps)"); clean(ax)
    a.text(2.8, max(res["trace"][1]) * 0.95, "cue ends", fontsize=8, color=GRAY)
    a.set_ylabel("weight of the predictive synapse"); a.set_title("A. Credit reaching the right synapse", fontsize=10, loc="left")
    b.set_ylabel("right synapse ÷ average other synapse"); b.set_title("B. Selectivity of the credit", fontsize=10, loc="left")
    b.axhline(1, color=GRAY, lw=0.8)
    a.legend(frameon=False, fontsize=8, loc="upper right")
    fig.tight_layout(); save(fig, "fig_credit.png")
    return {k: (round(v[0][0], 1), round(v[0][5], 2), round(v[0][10], 2)) for k, v in res.items()}


EVALS = [("step 1,250\n(May 5)", 20), ("stage 1,\nstep 10,500", 2), ("stage 2,\nstep 3,350", 19), ("stage 2,\nsteps 3,900-4,000", 1),
         ("stage 2,\nstep 4,050", 33), ("stage 2,\nstep 4,500", 21)]


def fig_measurements():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.2, 3.9), gridspec_kw={"width_ratios": [1.6, 1]})
    x = np.arange(len(EVALS))
    a.bar(x, [v for _, v in EVALS], color=EXC, width=0.6)
    a.axhline(50, color=GRAY, ls=":", lw=1); a.text(len(EVALS) - 0.6, 51, "50 prompts", fontsize=8, color=GRAY, ha="right")
    a.set_xticks(x); a.set_xticklabels([l for l, _ in EVALS], fontsize=7.8); a.set_ylim(0, 56)
    a.set_ylabel("different answers to 50 prompts"); a.set_title("A. Variety of answers (May 2026 evaluations)", fontsize=10, loc="left"); clean(a)
    runs = ["probe 1", "probe 2", "before\npruning", "after\npruning"]
    b.bar(np.arange(4), [1, 1, 1, 1], color=INH, width=0.6)
    b.axhline(20, color=GRAY, ls=":", lw=1); b.text(3.4, 18.6, "perfect: 20", fontsize=8, color=GRAY, ha="right")
    b.set_xticks(np.arange(4)); b.set_xticklabels(runs, fontsize=8); b.set_ylim(0, 22)
    b.set_ylabel("intended word produced (of 20)"); b.set_title("B. Saying the intended word (May 29)", fontsize=10, loc="left"); clean(b)
    fig.tight_layout(); save(fig, "fig_measurements.png")


SCALE = [("honeybee\n(under a\nmillion)", 1e6, None), ("fruit fly\nbrain", 139255, 54.5e6), ("NIMCP\nspiking\nnetwork", 2.2e6, 1.5e9),
         ("1 mm\u00b3 of\nhuman\ncortex", 16087, 149.9e6), ("human\nneocortex", 16.3e9, 1.64e14), ("whole\nhuman\nbrain", 86e9, None)]


def fig_scale():
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.9))
    x = np.arange(len(SCALE))
    cols = [GRAY, GRAY, GOLD, GRAY, GRAY, GRAY]
    a.bar(x, [s[1] for s in SCALE], color=cols, log=True, width=0.6)
    a.set_xticks(x); a.set_xticklabels([s[0] for s in SCALE], fontsize=7.8); a.set_ylabel("neurons (log scale)")
    a.set_title("A. Neurons", fontsize=10, loc="left"); clean(a)
    spn = [(s[0], s[2] / s[1]) for s in SCALE if s[2]]
    xb = np.arange(len(spn))
    b.bar(xb, [v for _, v in spn], color=[GOLD if 'NIMCP' in n else GRAY for n, _ in spn], width=0.6)
    for xi, (_, v) in zip(xb, spn):
        b.text(xi, v * 1.03, f"{v:,.0f}", ha="center", fontsize=8.5)
    b.set_xticks(xb); b.set_xticklabels([s for s, _ in spn], fontsize=7.8); b.set_ylabel("synapses per neuron")
    b.set_title("B. Connections per neuron", fontsize=10, loc="left"); clean(b)
    fig.tight_layout(); save(fig, "fig_scale.png")


if __name__ == "__main__":
    fig_architecture(); fig_status(); fig_measurements(); fig_scale()
    print("credit", fig_credit())
