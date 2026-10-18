#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 13 (Why the Brain Works the Way It Does). Outputs into ./images.
Requires matplotlib, numpy, and networkx. Figures 13.2 to 13.6 are computed."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
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


def H2(p):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return -(p * np.log2(p) + (1 - p) * np.log2(1 - p))


def fig_efficiency():
    """Levy and Baxter (1996): bits per unit energy for a binary neuron that fires with probability p
    in each time bin, when a bin costs r (rest) plus 1 if a spike is fired."""
    p = np.linspace(0.001, 0.999, 4000)
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.8))
    a.plot(p, H2(p), color=EXC, lw=2)
    a.set_xlabel("probability of a spike in each time bin"); a.set_ylabel("information per bin (bits)")
    a.set_title("A. Information alone peaks at one half", fontsize=10, loc="left"); clean(a)
    a.axvline(0.5, color=GRAY, ls=":", lw=1)
    opt = {}
    for r, c in [(0.01, INH), (0.1, GOLD), (1.0, EXC)]:
        eff = H2(p) / (r + p); i = eff.argmax(); opt[r] = p[i]
        b.plot(p, eff / eff.max(), color=c, lw=2, label=f"rest costs {r:g} of a spike")
        b.plot(p[i], 1.0, "o", color=c, ms=6)
    b.set_xscale("log"); b.set_xlim(1e-3, 1)
    b.set_xlabel("probability of a spike in each time bin (log scale)"); b.set_ylabel("bits per unit energy (relative)")
    b.set_title("B. Bits per unit energy peak far lower", fontsize=10, loc="left"); clean(b)
    b.legend(frameon=False, fontsize=8.5, loc="lower center")
    fig.tight_layout(); save(fig, "fig_efficiency.png")
    return opt


def wiring_networks(n=100, k=6, fracs=np.linspace(0, 1, 21), seeds=range(12)):
    rows = []
    for s in seeds:
        rng = np.random.default_rng(s)
        pos = rng.random((n, 2))
        d = np.linalg.norm(pos[:, None] - pos[None], axis=2)
        near = np.argsort(d, axis=1)[:, 1:k // 2 + 1]
        base = {tuple(sorted((i, j))) for i in range(n) for j in near[i]}
        base = sorted(base)
        for f in fracs:
            m = len(base); nrew = int(round(f * m))
            idx = rng.permutation(m)[:nrew]
            edges = set(base)
            for t in idx:
                edges.discard(base[t])
            while len(edges) < m:
                i, j = rng.choice(n, 2, replace=False); edges.add(tuple(sorted((i, j))))
            G = nx.Graph(); G.add_nodes_from(range(n)); G.add_edges_from(edges)
            if not nx.is_connected(G):
                continue
            wire = sum(d[i, j] for i, j in edges)
            rows.append((f, wire, nx.average_shortest_path_length(G)))
    return np.array(rows)


def pareto_mask(costs):
    m = np.ones(len(costs), bool)
    for i, c in enumerate(costs):
        if m[i]:
            dominated = np.all(costs >= c, axis=1) & np.any(costs > c, axis=1)
            m[dominated] = False
    return m


def fig_wiring():
    R = wiring_networks()
    wire = R[:, 1] / R[R[:, 0] == 0, 1].mean()
    fig, ax = plt.subplots(figsize=(6.6, 4.4))
    sc = ax.scatter(wire, R[:, 2], c=R[:, 0], cmap="viridis", s=16, alpha=0.85)
    m = pareto_mask(np.c_[wire, R[:, 2]]); o = np.argsort(wire[m])
    ax.plot(wire[m][o], R[m, 2][o], color=INH, lw=1.8, label="best available trade-offs")
    cb = fig.colorbar(sc, ax=ax); cb.set_label("fraction of connections that are long-range")
    ax.set_xlabel("total wire length (relative to all-local wiring)"); ax.set_ylabel("average steps between two neurons")
    ax.legend(frameon=False, loc="upper right"); clean(ax)
    fig.tight_layout(); save(fig, "fig_wiring.png")
    out = {}
    for f in (0.0, 0.05, 0.1, 1.0):
        sel = np.isclose(R[:, 0], f)
        out[f] = (round(wire[sel].mean(), 2), round(R[sel, 2].mean(), 2))
    return out


def fig_pareto():
    """Shoval et al. (2012): three tasks, each best served by one archetype; performance falls with distance."""
    rng = np.random.default_rng(3)
    A = np.array([[0.15, 0.2], [0.85, 0.25], [0.45, 0.85]])
    names = ["speed", "economy", "precision"]
    X = rng.random((3000, 2))
    # A design is dominated if some other design is closer to all three archetypes; test against a dense grid.
    g = np.stack(np.meshgrid(np.linspace(0, 1, 241), np.linspace(0, 1, 241)), -1).reshape(-1, 2)
    dg = np.linalg.norm(g[:, None] - A[None], axis=2)
    dX = np.linalg.norm(X[:, None] - A[None], axis=2)
    m = np.array([not np.any(np.all(dg < dx, axis=1)) for dx in dX])
    fig, ax = plt.subplots(figsize=(5.6, 4.8))
    ax.scatter(X[~m, 0], X[~m, 1], s=5, color="#cccccc", label="possible designs")
    ax.scatter(X[m, 0], X[m, 1], s=7, color=EXC, label="designs no other beats at every task")
    ax.fill(A[:, 0], A[:, 1], fc="none", ec=INH, lw=1.5, ls="--")
    for (x, y), nm in zip(A, names):
        ax.plot(x, y, "o", color=INH, ms=8)
        ax.annotate(f"best for {nm}", (x, y), xytext=(0, 9 if y > 0.5 else -15), textcoords="offset points",
                    ha="center", color=INH, fontsize=9.5)
    ax.set_xlabel("trait 1"); ax.set_ylabel("trait 2"); ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlim(-0.02, 1.02); ax.set_ylim(-0.02, 1.02)
    ax.legend(frameon=False, fontsize=8.5, loc="upper right", bbox_to_anchor=(1.0, 1.12), ncol=1)
    fig.tight_layout(); save(fig, "fig_pareto.png")
    return int(m.sum())


K_UNMY = 21.2 / np.sqrt(476.0)   # squid giant axon: 476 um, 21.2 m/s at 18.5 C (Hodgkin and Huxley 1952)
K_MY = 6.0                         # myelinated: about 6 m/s per um of outer fiber diameter (Hursh 1939, cat)


def fig_conduction():
    d = np.logspace(-1, 3, 400)
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.8, 3.9))
    a.loglog(d, K_UNMY * np.sqrt(d), color=INH, lw=2, label="bare axon (speed grows as\nthe square root of width)")
    dm = d[(d >= 1) & (d <= 20)]   # real myelinated fibers span roughly 1 to 20 um
    a.loglog(dm, K_MY * dm, color=EXC, lw=2, label="myelinated fiber (speed grows\nin proportion to width)")
    a.plot(476, 21.2, "o", color=INH); a.annotate("squid giant axon", (476, 21.2), xytext=(-8, 10), textcoords="offset points", ha="right", fontsize=8.5, color=INH)
    dsame = 21.2 / K_MY
    a.plot(dsame, 21.2, "o", color=EXC); a.annotate(f"myelinated fiber\nof {dsame:.1f} µm", (dsame, 21.2), xytext=(-6, 8), textcoords="offset points", ha="right", fontsize=8.5, color=EXC)
    a.axhline(21.2, color=GRAY, ls=":", lw=1)
    a.set_xlabel("fiber diameter (µm)"); a.set_ylabel("conduction speed (m/s)")
    a.set_title("A. Two ways to go fast", fontsize=10, loc="left"); a.legend(frameon=False, fontsize=8, loc="lower right"); clean(a)
    v = np.logspace(0, 2, 200)
    ratio = ((v / K_UNMY) ** 2 / (v / K_MY)) ** 2
    b.loglog(v, ratio, color=GOLD, lw=2)
    for vv in (10, 21.2, 50):
        r = ((vv / K_UNMY) ** 2 / (vv / K_MY)) ** 2; b.plot(vv, r, "o", color=GOLD)
        b.annotate(f"about {float(f'{r:.2g}'):,.0f}×", (vv, r), xytext=(-4, 8), textcoords="offset points", ha="right", fontsize=8.5)
    b.set_xlabel("required conduction speed (m/s)"); b.set_ylabel("cross-section of a bare axon\n÷ cross-section of a myelinated fiber")
    b.set_title("B. What the bare axon pays in space", fontsize=10, loc="left"); clean(b)
    fig.tight_layout(); save(fig, "fig_conduction.png")
    return dsame, ((21.2 / K_UNMY) ** 2 / dsame) ** 2

def fig_genome():
    """Zador (2019): bits needed to list every connection versus the information a genome can hold."""
    human_genome = 3.1e9 * 2                 # base pairs x 2 bits
    human_wiring = 1e14 * np.log2(1e11)      # Zador: 10^14 connections x ~37 bits each
    worm_genome = 1.0e8 * 2                  # C. elegans genome, about 100 million base pairs
    worm_wiring = 7000 * np.log2(302)        # about 7,000 synapses among 302 neurons
    fig, ax = plt.subplots(figsize=(7.4, 4.0))
    xs = np.array([0, 1, 3, 4]); vals = [worm_genome, worm_wiring, human_genome, human_wiring]
    cols = [EXC, GOLD, EXC, GOLD]
    ax.bar(xs, vals, color=cols, width=0.8, log=True)
    for x, v in zip(xs, vals):
        e = int(np.floor(np.log10(v))); m = v / 10 ** e
        ax.text(x, v * 1.6, f"{m:.1f} × 10$^{{{e}}}$ bits", ha="center", fontsize=9)
    ax.set_xticks(xs); ax.set_xticklabels(["genome", "list of every\nconnection", "genome", "list of every\nconnection"])
    ax.text(0.5, 5e20, "nematode worm\n(302 neurons)", ha="center", va="top", fontsize=10, weight="bold")
    ax.text(3.5, 5e20, "human\n(about 10$^{11}$ neurons)", ha="center", va="top", fontsize=10, weight="bold")
    ax.axvline(2.0, color="#dddddd", lw=1, ymax=0.75)
    ax.set_ylim(1e0, 1e21); ax.set_ylabel("information (bits, log scale)"); clean(ax)
    ax.set_xlim(-0.7, 4.7)
    fig.tight_layout(); save(fig, "fig_genome.png")
    return worm_genome / worm_wiring, human_wiring / human_genome


TRADE = [("hold what is known", "learn what is new", "fast and slow memory stores; sleep", "forgetting, or interference", "5"),
         ("trust expectation", "trust the input", "precision; acetylcholine, norepinephrine", "illusion, or hallucination", "6, 12"),
         ("sensitivity", "range", "adaptation to the input's statistics", "aftereffects; lost absolute level", "12"),
         ("speed", "accuracy", "decision threshold", "hasty errors, or paralysis", "8"),
         ("exploit", "explore", "uncertainty; norepinephrine", "rigidity, or restlessness", "8"),
         ("flexibility", "economy of effort", "goal-directed and habitual control", "slips, or compulsions", "9"),
         ("information", "energy", "sparse firing; unreliable synapses", "lost detail", "1, 13"),
         ("short paths", "short wires", "local clusters with a few long links", "vulnerable hubs", "4, 13")]


def fig_tradeoffs():
    fig, ax = plt.subplots(figsize=(10.4, 5.4)); ax.set_xlim(0, 10.4); ax.set_ylim(0, len(TRADE) + 1.1); ax.axis("off")
    hdr = [(1.05, "one goal"), (3.3, "the other"), (5.75, "how the brain sets the balance"), (8.4, "failure when it is wrong"), (10.05, "ch.")]
    y0 = len(TRADE) + 0.55
    for x, t in hdr:
        ax.text(x, y0, t, ha="center", fontsize=9.5, weight="bold", color=GRAY)
    for i, (a, b, how, fail, ch) in enumerate(TRADE):
        y = len(TRADE) - i - 0.25
        box(ax, 1.05, y, 1.75, 0.62, a, fc="#e8eef5", ec=EXC, fs=8.8)
        box(ax, 3.3, y, 1.75, 0.62, b, fc="#f7e6e4", ec=INH, fs=8.8)
        arrow(ax, (2.02, y), (2.33, y), color=GRAY, style="<|-|>")
        ax.text(5.75, y, how, ha="center", va="center", fontsize=8.8)
        ax.text(8.4, y, fail, ha="center", va="center", fontsize=8.8, color=INH)
        ax.text(10.05, y, ch, ha="center", va="center", fontsize=8.8, color=GRAY)
    fig.tight_layout(); save(fig, "fig_tradeoffs.png")


CONSTRAINTS = [("energy", "sparse firing; unreliable synapses;\nprediction that cancels the expected", "1, 2, 6, 12"),
               ("space and wire", "myelin for a few fast lines; local clusters\nwith long links; modules and hierarchy; folding", "2, 4, 13"),
               ("time", "prediction to beat delays; one\nhemisphere for time-critical skills", "9, 12, 13"),
               ("noise", "spikes over distance; populations\nthat vote; a floor on axon width", "1, 2"),
               ("the genome's capacity", "rules of growth, then learning;\nsensitive periods", "0, 1, 5"),
               ("many tasks at once", "compromises among goals;\nneuromodulators to shift them", "3, 8, 9")]


def fig_map():
    fig, ax = plt.subplots(figsize=(9.6, 6.2)); ax.set_xlim(0, 10); ax.set_ylim(-0.6, 7.2); ax.axis("off")
    ax.text(1.6, 6.85, "constraint", ha="center", fontsize=10, weight="bold", color=GRAY)
    ax.text(6.1, 6.85, "features it helps explain", ha="center", fontsize=10, weight="bold", color=GRAY)
    ax.text(9.35, 6.85, "chapters", ha="center", fontsize=10, weight="bold", color=GRAY)
    for i, (c, f, ch) in enumerate(CONSTRAINTS):
        y = 6.0 - i * 0.98
        box(ax, 1.6, y, 2.4, 0.66, c, fc="#e8eef5", ec=EXC, fs=9.5, weight="bold")
        arrow(ax, (2.9, y), (3.85, y), color=EXC)
        box(ax, 6.1, y, 4.2, 0.74, f, fs=8.8)
        ax.text(9.35, y, ch, ha="center", va="center", fontsize=9, color=GRAY)
    box(ax, 5.0, -0.25, 9.4, 0.5, "history: a tinkerer modifying what already existed (basal ganglia kept for more than 500 million years; an inverted retina)",
        fc="#f6efd6", ec=GOLD, fs=8.8)
    fig.tight_layout(); save(fig, "fig_map.png")


if __name__ == "__main__":
    fig_map(); fig_tradeoffs()
    print("genome ratios", fig_genome())
    print("conduction", fig_conduction())
    print("optimal p", {k: round(v, 3) for k, v in fig_efficiency().items()})
    print("wiring", fig_wiring())
    print("pareto points", fig_pareto())
