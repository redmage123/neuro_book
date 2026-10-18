#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 11 (Integrating Brain Mechanisms into AI Models). Outputs into ./images.
Requires matplotlib and numpy. Figures 11.2 and 11.3 are simulations and take a minute or two."""
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


def fig_borrowing():
    """Figure 11.1: three ways to borrow from the brain."""
    cols = [("copy the mechanism", "build the brain's parts\nas they are",
             "detailed simulation of cortex\nspiking neuromorphic chips", "costly; few wins so far\noutside energy use", INH),
            ("borrow the principle", "keep what a part does,\nbuild it in silicon's terms",
             "convolution  ·  context gating\ngenerated replay  ·  learned plasticity\nhomeostatic reward", "convolution in wide use;\nmost others in research systems", EXC),
            ("borrow the data", "use recordings from brains\nto shape what a network learns",
             "networks regularized toward\nneural responses in visual cortex", "modest gains in robustness;\nearly days", GOLD)]
    fig, ax = plt.subplots(figsize=(9.6, 5.3))
    ax.set_xlim(0, 12); ax.set_ylim(-1.45, 6.4); ax.axis("off")
    box(ax, 6, 5.85, 3.2, 0.6, "the brain", fc="#eef3f8", ec=EXC, fs=10.5, weight="bold", color=EXC)
    for i, (head, how, ex, rec, c) in enumerate(cols):
        x = 2 + 4 * i
        arrow(ax, (6 + (i - 1) * 0.9, 5.45), (x, 4.75), color=c, lw=1.8)
        box(ax, x, 4.35, 3.5, 0.6, head, ec=c, color=c, fs=10, weight="bold")
        ax.text(x, 3.45, how, ha="center", va="center", fontsize=8.8, color=GRAY, style="italic")
        box(ax, x, 2.15, 3.5, 1.15, ex, fs=8.6)
        ax.text(x, 0.95, "record: " + rec, ha="center", va="center", fontsize=8.6, color=c)
    ax.add_patch(FancyBboxPatch((0.25, -1.3), 11.5, 1.05, boxstyle="round,pad=0.08", fc="#f4f4f4", ec=GRAY, lw=1.0, ls="--"))
    ax.text(6, -0.45, "not borrowed: convergences", ha="center", va="center", fontsize=9.5, color=GRAY, weight="bold")
    ax.text(6, -0.95, "experience replay  ·  temporal-difference learning  ·  attention as associative memory\n"
            "invented by engineers or psychologists, recognized in the brain afterward", ha="center", va="center", fontsize=8.3, color=GRAY)
    fig.tight_layout(); save(fig, "fig_borrowing.png")


def gating_run(mode, seed=0, T=5, n=12, d=40, h=200, keep=0.2, passes=150, lr=0.05, lam=10.0):
    """Five tasks that share their cues but not their answers. A context unit signals the task.
    'gate': each task uses a fixed random 20% of hidden units (after Masse, Grant and Freedman 2018).
    'stab': changes to weights important for earlier tasks are penalized (in the spirit of
    elastic weight consolidation). Returns R[t, s], the fraction of task-s items recalled perfectly
    after training on task t."""
    rng = np.random.default_rng(seed)
    sig = lambda z: 1 / (1 + np.exp(-z))
    X = rng.choice([0., 1.], (n, d))
    Ys = [rng.choice([0., 1.], (n, 10)) for _ in range(T)]
    gate, stab = "gate" in mode, "stab" in mode
    masks = [(rng.random(h) < keep).astype(float) if gate else np.ones(h) for _ in range(T)]
    W1 = rng.normal(0, 0.3, (d + T, h)); W2 = rng.normal(0, 0.3, (h, 10))
    F1, F2, A1, A2 = np.zeros_like(W1), np.zeros_like(W2), W1.copy(), W2.copy()

    def inp(t):
        c = np.zeros((n, T)); c[:, t] = 1; return np.hstack([X, c])

    def grads(t, i):
        x = inp(t)[i:i + 1]; hh = sig(x @ W1) * masks[t]; o = sig(hh @ W2)
        do = o - Ys[t][i:i + 1]; dh = (do @ W2.T) * hh * (1 - hh)
        return x.T @ dh, hh.T @ do

    def acc(t):
        o = sig((sig(inp(t) @ W1) * masks[t]) @ W2); return np.mean(np.all((o > 0.5) == (Ys[t] > 0.5), 1))

    R = np.full((T, T), np.nan)
    for t in range(T):
        for _ in range(passes):
            for i in rng.permutation(n):
                g1, g2 = grads(t, i)
                if stab: g1 = g1 + lam * F1 * (W1 - A1); g2 = g2 + lam * F2 * (W2 - A2)
                W1 -= lr * g1; W2 -= lr * g2
        if stab:  # importance of each weight to the task just learned: its mean squared gradient
            for i in range(n):
                g1, g2 = grads(t, i); F1 += 50 * g1 ** 2 / n; F2 += 50 * g2 ** 2 / n
            A1, A2 = W1.copy(), W2.copy()
        for s in range(t + 1): R[t, s] = acc(s)
    return R


def fig_gating():
    """Figure 11.2: context gating and weight protection against forgetting (simulation)."""
    conds = [("plain", "no protection", GRAY, ":"), ("stab", "weights protected", GOLD, "-."),
             ("gate", "units gated by context", EXC, "--"), ("gate+stab", "gated and protected", INH, "-")]
    res = {m: np.mean([gating_run(m, s) for s in range(20)], 0) * 100 for m, *_ in conds}
    fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.7), sharey=True)
    for m, lab, c, ls in conds:
        axs[0].plot(range(1, 6), res[m][:, 0], color=c, ls=ls, lw=2, marker="o", ms=4, label=lab)
        axs[1].plot(range(1, 6), res[m][-1], color=c, ls=ls, lw=2, marker="o", ms=4)
    axs[0].set_title("A  task 1, recalled after each new task", loc="left", fontsize=10)
    axs[0].set_xlabel("tasks learned so far"); axs[0].set_ylabel("items recalled perfectly (%)")
    axs[1].set_title("B  every task, recalled after all five", loc="left", fontsize=10)
    axs[1].set_xlabel("task")
    for ax in axs: ax.set_xticks(range(1, 6)); ax.set_ylim(-4, 106); clean(ax)
    fig.legend(*axs[0].get_legend_handles_labels(), frameon=False, fontsize=8.5, loc="lower center", ncol=4, bbox_to_anchor=(0.5, -0.02))
    fig.tight_layout(rect=(0, 0.07, 1, 1)); save(fig, "fig_gating.png")


def hopfield_trial(P, kind, rng, N=100, flip=0.1, beta=0.5, steps=10):
    """Store P random patterns of N units; cue with one pattern with 10% of its units flipped;
    succeed if the network settles on the stored pattern exactly."""
    xi = rng.choice([-1., 1.], (P, N)); mu = rng.integers(P); x = xi[mu].copy()
    x[rng.choice(N, int(flip * N), replace=False)] *= -1
    if kind == "classic":  # Hopfield (1982): Hebbian weights, one unit at a time
        W = xi.T @ xi / N; np.fill_diagonal(W, 0)
        for _ in range(steps):
            for i in rng.permutation(N): x[i] = 1. if W[i] @ x >= 0 else -1.
    else:  # modern Hopfield network: a softmax over stored patterns, the update used by attention
        for _ in range(steps):
            a = beta * (xi @ x); a -= a.max(); p = np.exp(a); p /= p.sum()
            x = np.where(p @ xi >= 0, 1., -1.)
    return np.all(x == xi[mu])


def fig_hopfield():
    """Figure 11.3: capacity of a classical and a modern Hopfield network (simulation)."""
    rng = np.random.default_rng(1)
    Ps = [2, 4, 6, 8, 10, 12, 14, 17, 20, 25, 30, 40, 60, 100, 200, 400, 1000, 3000]
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    for kind, lab, c, ls in [("classic", "classical (1982): Hebbian weights", EXC, "-"),
                             ("modern", "modern: attention over stored patterns", INH, "--")]:
        r = [100 * np.mean([hopfield_trial(P, kind, rng) for _ in range(200 if P < 500 else 60)]) for P in Ps]
        ax.plot(Ps, r, color=c, ls=ls, lw=2, marker="o", ms=3.5, label=lab)
    ax.axvline(100, color=GRAY, lw=0.8, ls=":")
    ax.text(110, 55, "as many patterns\nas units", fontsize=8.5, color=GRAY, va="center")
    ax.set_xscale("log"); ax.set_ylim(-4, 106)
    ax.set_xticks([2, 10, 100, 1000]); ax.set_xticklabels(["2", "10", "100", "1,000"])
    ax.set_xlabel("patterns stored in a network of 100 units"); ax.set_ylabel("cued patterns recalled exactly (%)")
    ax.legend(frameon=False, fontsize=8.5, loc="center right", bbox_to_anchor=(1.0, 0.3)); clean(ax)
    fig.tight_layout(); save(fig, "fig_hopfield.png")


# Energy per operation at 45 nm, picojoules (Horowitz 2014).
OPS = [("add two 32-bit integers", 0.1), ("multiply two 32-bit floating-point numbers", 3.7),
       ("read 64 bits from a small on-chip memory (8 KB)", 10.0), ("read 64 bits from a large on-chip memory (1 MB)", 100.0),
       ("read 64 bits from off-chip memory (DRAM)", 2000.0)]


def fig_energy_ops():
    """Figure 11.5: moving data costs more than computing with it."""
    fig, ax = plt.subplots(figsize=(8.0, 3.2))
    for i, (lab, v) in enumerate(OPS[::-1]):
        c = INH if "read" in lab else EXC
        ax.plot([0.03, v], [i, i], color="#dddddd", lw=1, zorder=0); ax.plot(v, i, "o", color=c, ms=8)
        ax.text(v * 1.5, i, f"{v:g} pJ", va="center", fontsize=9, color=c)
    ax.set_yticks(range(len(OPS))); ax.set_yticklabels([o[0] for o in OPS[::-1]], fontsize=9)
    ax.set_xscale("log"); ax.set_xlim(0.03, 2e4); ax.set_ylim(-0.6, len(OPS) - 0.4)
    ax.set_xlabel("energy per operation (picojoules, logarithmic scale)"); clean(ax)
    fig.tight_layout(); save(fig, "fig_energy_ops.png")


def fig_surrogate():
    """Figure 11.6: why spikes resist gradient training, and the surrogate gradient."""
    v = np.linspace(-2, 2, 801); th = 0
    fig, axs = plt.subplots(1, 3, figsize=(9.6, 2.9))
    axs[0].plot(v, (v >= th).astype(float), color=EXC, lw=2)
    axs[0].set_title("A  spike or no spike", loc="left", fontsize=10); axs[0].set_ylabel("output")
    axs[1].plot(v, np.zeros_like(v), color=INH, lw=2); axs[1].annotate("", (0, 1.0), (0, 0), arrowprops=dict(arrowstyle="-|>", color=INH, lw=2))
    axs[1].text(0.15, 0.85, "infinite at\nthreshold", fontsize=8.5, color=INH)
    axs[1].set_title("B  its true slope", loc="left", fontsize=10)
    axs[2].plot(v, 1 / (1 + 4 * np.abs(v)) ** 2, color=GOLD, lw=2)
    axs[2].set_title("C  the surrogate slope", loc="left", fontsize=10)
    for ax in axs:
        ax.set_xlabel("membrane potential\nrelative to threshold"); ax.set_ylim(-0.08, 1.12); ax.set_xticks([-2, 0, 2]); ax.set_yticks([0, 1]); clean(ax)
    axs[1].set_yticks([0]); axs[2].set_yticks([0, 1])
    fig.tight_layout(); save(fig, "fig_surrogate.png")


def fig_homeostatic():
    """Figure 11.7: reward defined by the body's needs (after Keramati and Gutkin 2014)."""
    def drive(h): return np.abs(h) ** 1.5  # distance of the internal state from its set point (0)
    h = np.linspace(-10, 6, 400); K = 2.0
    fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.6))
    ax = axs[0]
    ax.plot(h, drive(h) - drive(h + K), color=EXC, lw=2, label="homeostatic reward")
    ax.axhline(4, color=INH, lw=2, ls="--", label="fixed reward")
    ax.axhline(0, color=GRAY, lw=0.6); ax.axvline(0, color=GRAY, lw=0.6, ls=":")
    ax.text(0.2, -7.6, "set point", fontsize=8.5, color=GRAY)
    ax.set_xlabel("internal state before eating\n(energy store relative to its set point)"); ax.set_ylabel("reward for one meal")
    ax.set_title("A  the value of the same meal", loc="left", fontsize=10); ax.legend(frameon=False, fontsize=8.5, loc="upper right")
    clean(ax)
    ax = axs[1]
    T = 60; cost = 1.0
    for kind, c, ls, lab in [("homeo", EXC, "-", "eats when the meal is rewarding"), ("fixed", INH, "--", "eats whenever food is offered")]:
        s = -6.0; tr = []
        for t in range(T):
            offered = t % 2 == 0
            eat = offered and (drive(s) - drive(s + K) > 0 if kind == "homeo" else True)
            s = s + (K if eat else 0) - cost * 0.6; tr.append(s)
        ax.plot(range(T), tr, color=c, ls=ls, lw=2, label=lab)
    ax.axhline(0, color=GRAY, lw=0.6, ls=":")
    ax.set_xlabel("time"); ax.set_ylabel("internal state")
    ax.set_title("B  two agents offered food every other step", loc="left", fontsize=10)
    ax.legend(frameon=False, fontsize=8.5, loc="upper left"); clean(ax)
    fig.tight_layout(); save(fig, "fig_homeostatic.png")


MEM = [("knowledge spread across synapses\n(slow, in cortex)", "trained weights", 2),
       ("a fast store of episodes\n(hippocampus)", "context window, retrieval database,\nfast weights", 1),
       ("protection of what matters\n(synaptic consolidation, gating)", "weight protection, gating\n(research systems)", 1),
       ("consolidation by replay\n(in sleep and rest)", "retraining on mixed old and new data;\nreplay in research systems", 0),
       ("neuromodulators set when\nand how fast to learn", "a learning-rate schedule\nfixed in advance", 0)]


def fig_memory_map():
    """Figure 11.4: the brain's memory systems and their machine counterparts."""
    cols = {2: EXC, 1: GOLD, 0: INH}; names = {2: "in place", 1: "partly built", 0: "largely missing"}
    fig, ax = plt.subplots(figsize=(9.4, 5.0))
    ax.set_xlim(0, 12); ax.set_ylim(-0.7, len(MEM) + 0.3); ax.axis("off")
    ax.text(2.4, len(MEM) - 0.05, "in the brain", ha="center", fontsize=10, weight="bold", color=GRAY)
    ax.text(9.4, len(MEM) - 0.05, "in a deployed language model", ha="center", fontsize=10, weight="bold", color=GRAY)
    for i, (b, m, s) in enumerate(MEM[::-1]):
        box(ax, 2.4, i, 4.2, 0.72, b, fs=8.8)
        box(ax, 9.4, i, 4.0, 0.72, m, ec=cols[s], fs=8.8)
        arrow(ax, (4.65, i), (7.2, i), color=cols[s], lw=2)
        ax.text(5.92, i + 0.17, names[s], ha="center", fontsize=8.3, color=cols[s])
    fig.tight_layout(); save(fig, "fig_memory_map.png")


if __name__ == "__main__":
    for f in (fig_borrowing, fig_gating, fig_hopfield, fig_energy_ops, fig_surrogate, fig_homeostatic, fig_memory_map):
        f()
