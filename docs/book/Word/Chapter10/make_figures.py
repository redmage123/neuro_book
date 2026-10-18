#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 10 (What Artificial Intelligence Gets Right and Wrong). Outputs into ./images.
Requires matplotlib and numpy."""
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


def fig_exchange():
    """Figure 10.1: ideas passing between neuroscience and machine learning."""
    # (year, label, label height, label x)
    neuro = [(1943, "McCulloch and Pitts:\nthe logical neuron", 0.62, 1943), (1949, "Hebb:\ncells that fire together", 1.2, 1947),
             (1962, "Hubel and Wiesel:\nsimple and complex cells", 0.62, 1964),
             (1972, "Rescorla and Wagner:\nlearning from prediction error", 1.2, 1977), (1997, "Schultz, Dayan, Montague:\ndopamine as TD error", 0.62, 1995),
             (2014, "Yamins and colleagues:\nnetworks predict IT", 1.2, 2009), (2020, "Dabney and colleagues:\ndistributional dopamine", 0.62, 2023)]
    ml = [(1958, "Rosenblatt:\nthe perceptron", -0.62, 1956), (1980, "Fukushima:\nthe neocognitron", -0.62, 1975),
          (1986, "Rumelhart, Hinton, Williams:\nbackpropagation", -1.2, 1979), (1988, "Sutton:\ntemporal-difference learning", -1.2, 2001),
          (2012, "Krizhevsky and colleagues:\ndeep convolutional network", -0.62, 2004), (2017, "distributional\nreinforcement learning", -1.2, 2022)]
    links = [(1943, 1958), (1949, 1958), (1962, 1980), (1972, 1988), (1988, 1997), (2012, 2014), (2017, 2020)]
    fig, ax = plt.subplots(figsize=(10.2, 4.6))
    ax.set_xlim(1922, 2033); ax.set_ylim(-1.95, 1.6); ax.axis("off")
    ax.axhline(0, color=GRAY, lw=0.8, xmin=0.17, xmax=0.98)
    ax.text(1923, 0.12, "neuroscience\nand psychology", color=EXC, weight="bold", fontsize=10, va="bottom")
    ax.text(1923, -0.12, "machine\nlearning", color=INH, weight="bold", fontsize=10, va="top")
    for yr in range(1940, 2030, 10):
        ax.plot([yr, yr], [-1.72, -1.66], color=GRAY, lw=0.8)
        ax.text(yr, -1.82, str(yr), ha="center", va="center", fontsize=8, color=GRAY)
    ax.plot([1940, 2020], [-1.69, -1.69], color=GRAY, lw=0.8)
    for yr, t, h, lx in neuro:
        ax.plot([yr, yr, lx], [0.05, h - 0.3, h - 0.18], color=EXC, lw=0.9); ax.plot(yr, 0.05, "o", color=EXC, ms=4)
        ax.text(lx, h, t, ha="center", va="center", fontsize=7.6, color=EXC)
    for yr, t, h, lx in ml:
        ax.plot([yr, yr, lx], [-0.05, h + 0.3, h + 0.18], color=INH, lw=0.9); ax.plot(yr, -0.05, "o", color=INH, ms=4)
        ax.text(lx, h, t, ha="center", va="center", fontsize=7.6, color=INH)
    nyrs = {n[0] for n in neuro}
    for a, b in links:
        ya = 0.05 if a in nyrs else -0.05; yb = 0.05 if b in nyrs else -0.05
        arrow(ax, (a + 0.5, ya), (b - 0.5, yb), color=GOLD, lw=1.6, cs="arc3,rad=%s" % ("-0.35" if ya > yb else "0.35"))
    ax.text(1923, 1.45, "gold arrows: an idea taken\nfrom one field into the other", ha="left", va="top", fontsize=7.5, color=GOLD)
    fig.tight_layout(); save(fig, "fig_exchange.png")


def fig_performance_predictivity():
    """Figure 10.2: better categorization, better prediction of IT, up to a point (illustrative, after Yamins et al. 2014
    and Linsley et al. 2023)."""
    rng = np.random.default_rng(3)
    perf = np.r_[rng.uniform(0.15, 0.45, 22), rng.uniform(0.5, 0.72, 10)]
    pred = 0.08 + 0.52 * perf + rng.normal(0, 0.035, perf.size)
    late = np.array([0.80, 0.83, 0.86, 0.88, 0.90, 0.92]); late_y = np.array([0.45, 0.43, 0.41, 0.40, 0.37, 0.36])
    fig, ax = plt.subplots(figsize=(5.8, 4.2))
    ax.scatter(perf[:22], pred[:22], s=26, color=GRAY, alpha=0.8, label="earlier models")
    ax.scatter(perf[22:], pred[22:], s=34, color=EXC, label="deep networks of 2014")
    ax.scatter(late, late_y, s=34, facecolor="white", edgecolor=INH, lw=1.5, label="later, more accurate networks")
    xs = np.linspace(0.1, 0.75, 10); ax.plot(xs, 0.08 + 0.52 * xs, color=GOLD, lw=1.4, ls="--")
    ax.set_xlabel("object categorization performance")
    ax.set_ylabel("IT responses predicted\n(fraction of explainable variance)")
    ax.set_xlim(0.1, 0.96); ax.set_ylim(0.1, 0.55)
    ax.legend(frameon=False, fontsize=8.5, loc="upper left"); clean(ax)
    fig.tight_layout(); save(fig, "fig_performance_predictivity.png")


# Words or tokens of language (see chapter text for sources).
DATA = [("a child by age five\n(high estimate)", 6.0e7), ("a person by age 20\n(high estimate)", 2.0e8),
        ("GPT-3 (2020)", 3.0e11), ("Llama 3 (2024)", 1.5e13)]


def dotplot(ax, labels, vals, cols, fmt):
    """Values as labeled dots on a log axis: bars on a log axis imply false ratios."""
    y = np.arange(len(vals))[::-1]
    for yi, v, c, l in zip(y, vals, cols, labels):
        ax.plot([ax.get_xlim()[0], v], [yi, yi], color="#dddddd", lw=1, zorder=0)
        ax.plot(v, yi, "o", color=c, ms=9)
        ax.text(v, yi + 0.28, fmt(v), ha="center", fontsize=9)
    ax.set_yticks(y); ax.set_yticklabels(labels); ax.set_ylim(-0.6, len(vals) - 0.3)
    ax.spines[["top", "right", "left"]].set_visible(False); ax.tick_params(axis="y", length=0)


def sci(v):
    e = int(np.floor(np.log10(v))); m = round(v / 10 ** e, 1)
    return (f"{m:g} × " if m != 1 else "") + f"$10^{{{e}}}$"


def fig_data_budget():
    """Figure 10.3: language input to people and to two language models, log scale."""
    fig, ax = plt.subplots(figsize=(7.4, 3.2))
    ax.set_xscale("log"); ax.set_xlim(1e6, 1e14)
    labels = [d[0] for d in DATA]; vals = [d[1] for d in DATA]
    cols = [INH if "GPT" in l or "Llama" in l else EXC for l in labels]
    dotplot(ax, labels, vals, cols, sci)
    ax.set_xlabel("words (people) or tokens (models), log scale")
    fig.tight_layout(); save(fig, "fig_data_budget.png")


def interference(mode, seed, nA=12, nB=12, d=40, h=60, epA=100, epB=100, lr=0.05, replay=6):
    """Two lists with the same cues and different answers (the AB-AC design); list identity is signalled by context units."""
    rng = np.random.default_rng(seed)
    XA = rng.choice([0.0, 1.0], (nA, d)); YA = rng.choice([0.0, 1.0], (nA, 10))
    XA[:, :6] = 1; XA[:, 6:12] = 0
    XB = XA.copy(); XB[:, :6] = 0; XB[:, 6:12] = 1; YB = rng.choice([0.0, 1.0], (nB, 10))
    W1 = rng.normal(0, 0.3, (d, h)); W2 = rng.normal(0, 0.3, (h, 10))
    sig = lambda z: 1 / (1 + np.exp(-z))
    acc = lambda X, Y: np.mean(np.all((sig(sig(X @ W1) @ W2) > 0.5) == (Y > 0.5), 1))

    def epoch(X, Y):
        nonlocal W1, W2
        for i in rng.permutation(len(X)):
            x, y = X[i:i + 1], Y[i:i + 1]; hh = sig(x @ W1); o = sig(hh @ W2)
            do = o - y; dh = (do @ W2.T) * hh * (1 - hh)
            W2 -= lr * hh.T @ do; W1 -= lr * x.T @ dh
    hist = [(acc(XA, YA), acc(XB, YB))]
    for _ in range(epA):
        epoch(XA, YA); hist.append((acc(XA, YA), acc(XB, YB)))
    for _ in range(epB):
        if mode == "seq":
            epoch(XB, YB)
        else:
            idx = rng.choice(nA, replay, replace=False); epoch(np.vstack([XB, XA[idx]]), np.vstack([YB, YA[idx]]))
        hist.append((acc(XA, YA), acc(XB, YB)))
    return np.array(hist)


def fig_interference():
    """Figure 10.5: sequential training erases the first list; replaying a few old items protects it (simulation)."""
    fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.6), sharey=True)
    for ax, mode, title in [(axs[0], "seq", "A  list B trained alone"), (axs[1], "replay", "B  list B trained with a few list-A items replayed")]:
        H = np.mean([interference(mode, s) for s in range(20)], 0) * 100
        ep = np.arange(H.shape[0])
        ax.axvspan(100, 200, color="#f2f2f2", zorder=0)
        ax.plot(ep, H[:, 0], color=EXC, lw=2, label="list A recalled")
        ax.plot(ep, H[:, 1], color=INH, lw=2, ls="--", label="list B recalled")
        ax.set_title(title, loc="left", fontsize=10); ax.set_xlabel("training passes")
        ax.text(50, 106, "training on list A", ha="center", fontsize=8.5, color=GRAY)
        ax.text(150, 106, "training on list B", ha="center", fontsize=8.5, color=GRAY)
        ax.set_ylim(-4, 114); ax.set_yticks([0, 25, 50, 75, 100]); clean(ax)
    axs[0].set_ylabel("items recalled perfectly (%)")
    axs[0].legend(frameon=False, fontsize=8.5, loc="center left", bbox_to_anchor=(0.14, 0.42))
    fig.tight_layout(); save(fig, "fig_interference.png")


# Energy in megawatt-hours (see chapter text for sources).
ENERGY = [("a human brain,\n20 years at 20 W", 20 * 24 * 365.25 * 20 / 1e6), ("training GPT-3\n(estimate)", 1287.0)]


def fig_energy():
    """Figure 10.6: the energy of a brain's first 20 years against one training run, log scale."""
    fig, ax = plt.subplots(figsize=(7.0, 2.3))
    ax.set_xscale("log"); ax.set_xlim(1, 1e4)
    labels = [e[0] for e in ENERGY]; vals = [e[1] for e in ENERGY]
    dotplot(ax, labels, vals, [EXC, INH], lambda v: f"{v:,.1f} MWh" if v < 100 else f"{v:,.0f} MWh")
    ax.set_xlabel("energy (megawatt-hours, log scale)")
    fig.tight_layout(); save(fig, "fig_energy.png")


def fig_lifecycles():
    """Figure 10.4: when learning happens in a typical deployed model and in a brain."""
    fig, (a, b) = plt.subplots(2, 1, figsize=(9.6, 5.0))
    for ax in (a, b):
        ax.set_xlim(0, 10); ax.set_ylim(0, 2.2); ax.axis("off")
    a.text(0, 2.05, "A  a typical deployed language model", fontsize=10, weight="bold", va="top")
    box(a, 2.2, 1.05, 3.4, 0.75, "training\nweights change on fixed data", fc="#e8eef5", ec=EXC, fs=9)
    box(a, 7.0, 1.05, 4.6, 0.75, "use\nweights frozen; recent or retrieved text\nheld in a context window", fc="#f6e9e7", ec=INH, fs=9)
    arrow(a, (3.95, 1.05), (4.65, 1.05), color=GRAY)
    a.text(4.3, 0.4, "knowledge stops here", ha="center", fontsize=8.5, color=INH)
    a.plot([4.3, 4.3], [0.55, 0.65], color=INH, lw=1)
    b.text(0, 2.05, "B  a brain", fontsize=10, weight="bold", va="top")
    box(b, 2.0, 1.25, 2.9, 0.6, "hippocampus\nlearns fast, from one episode", fc="#e8eef5", ec=EXC, fs=8.5)
    box(b, 6.0, 1.25, 2.9, 0.6, "cortex\nlearns slowly, by interleaving", fc="#e8eef5", ec=EXC, fs=8.5)
    arrow(b, (3.5, 1.35), (4.5, 1.35), color=EXC); b.text(4.0, 1.5, "replay", ha="center", fontsize=8, color=EXC)
    arrow(b, (4.5, 1.12), (3.5, 1.12), color=GRAY); b.text(4.0, 0.95, "recall", ha="center", fontsize=8, color=GRAY)
    box(b, 8.9, 1.25, 1.75, 0.6, "neuromodulators\ngate learning", fc="#fbf5e1", ec=GOLD, fs=8.5)
    arrow(b, (8.0, 1.25), (7.5, 1.25), color=GOLD)
    b.annotate("", xy=(9.9, 0.35), xytext=(0.1, 0.35), arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.2))
    b.text(5.0, 0.12, "learning during use, for a lifetime", ha="center", fontsize=8.5, color=GRAY)
    fig.tight_layout(); save(fig, "fig_lifecycles.png")


LEDGER = [
    ("learned, distributed representations", 2), ("error-driven learning", 2), ("prediction as a training signal", 2),
    ("hierarchy of features in vision", 2), ("feedback loops in perception", 1), ("learning from little data", 1),
    ("robustness outside the training data", 1), ("knowing when it does not know", 1),
    ("deciding when to deliberate", 1), ("learning rule available at each synapse", 0),
    ("learning for a lifetime without forgetting", 0), ("values anchored to a body", 0),
    ("energy budget of about 20 W", 0),
]


def fig_ledger():
    """Figure 10.7: a ledger of resemblances and differences."""
    names = {2: "largely shared", 1: "partly shared", 0: "largely absent in current systems"}
    cols = {2: EXC, 1: GOLD, 0: INH}
    fig, ax = plt.subplots(figsize=(7.6, 5.3))
    ax.set_xlim(0, 10); ax.set_ylim(-0.6, len(LEDGER) + 0.2); ax.axis("off")
    for i, (t, s) in enumerate(LEDGER[::-1]):
        ax.add_patch(FancyBboxPatch((0.1, i - 0.36), 0.55, 0.62, boxstyle="round,pad=0.02", fc=cols[s], ec="none"))
        ax.text(0.95, i - 0.05, t, va="center", fontsize=9.5)
        ax.text(9.9, i - 0.05, names[s], va="center", ha="right", fontsize=8.5, color=cols[s])
    ax.text(0.1, len(LEDGER) - 0.1, "property of the brain", fontsize=9, color=GRAY, weight="bold")
    ax.text(9.9, len(LEDGER) - 0.1, "in machine learning today", fontsize=9, color=GRAY, weight="bold", ha="right")
    fig.tight_layout(); save(fig, "fig_ledger.png")


if __name__ == "__main__":
    for f in (fig_exchange, fig_performance_predictivity, fig_data_budget, fig_interference, fig_energy,
              fig_lifecycles, fig_ledger):
        f()
