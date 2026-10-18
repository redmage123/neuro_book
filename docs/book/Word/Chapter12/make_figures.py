#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 12 (The Brain as a Predictive, Adaptive System). Outputs into ./images.
Requires matplotlib and numpy. Figures 12.2 to 12.5 are computed."""
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


MAP = [("dopamine neurons", "reward to come", "one number: better or\nworse than expected", "values of states\nand actions", "3, 8"),
       ("hippocampus", "where the animal\nwill be next", "departure from the\nexpected path (proposed)", "a predictive map\nof space and events", "5"),
       ("sensory cortex", "the input from\nthe level below", "a pattern of errors,\nfeature by feature", "a hierarchical model\nof the world", "6"),
       ("body-regulating\nbrain (hypothalamus,\ninsula)", "the body's needs", "interoceptive error", "set points and\nanticipatory responses", "7"),
       ("cerebellum", "the sensory result\nof a movement", "climbing-fiber error", "a forward model\nof the body", "9"),
       ("frontal and\ncingulate cortex", "how reliable the\nworld is", "surprise about\nsurprise", "the learning rate itself", "8, 11")]


def fig_map():
    """Figure 12.1: prediction across the book."""
    heads = ["system", "predicts", "error signal", "what learns", "chapter"]
    xs = [1.25, 3.55, 5.95, 8.35, 10.2]; ws = [2.1, 2.1, 2.3, 2.1, 0.9]
    fig, ax = plt.subplots(figsize=(10.2, 6.2))
    ax.set_xlim(0, 10.8); ax.set_ylim(-0.6, len(MAP) + 0.4); ax.axis("off")
    for x, h in zip(xs, heads):
        ax.text(x, len(MAP) - 0.05, h, ha="center", fontsize=10, weight="bold", color=GRAY)
    for i, row in enumerate(MAP[::-1]):
        for j, (x, w, t) in enumerate(zip(xs, ws, row)):
            ec = [EXC, GRAY, INH, GOLD, GRAY][j]
            box(ax, x, i, w, 0.78, t, ec=ec, fs=8.3)
    fig.tight_layout(); save(fig, "fig_prediction_map.png")


def pink_noise(n, rng, alpha=1.0):
    f = np.fft.rfftfreq(n); f[0] = f[1]
    spec = (rng.normal(size=f.size) + 1j * rng.normal(size=f.size)) / f ** (alpha / 2)
    x = np.fft.irfft(spec, n); return (x - x.mean()) / x.std()


def fig_retina():
    """Figure 12.2: predictive coding in the retina (after Srinivasan, Laughlin and Dubs 1982)."""
    rng = np.random.default_rng(3)
    x = pink_noise(8192, rng, alpha=1.0) + 0.05 * rng.normal(size=8192)  # power falls as 1/f, as along a line through a natural image
    pred = 0.5 * (np.roll(x, 1) + np.roll(x, -1))  # the surround predicts the center
    err = x - pred
    ratio = x.var() / err.var()
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.5), gridspec_kw={"width_ratios": [1.5, 1]})
    seg = slice(2000, 2200)
    t = np.arange(200)
    axs[0].plot(t, x[seg], color=EXC, lw=1.8, label="intensity along a row of photoreceptors")
    axs[0].plot(t, err[seg] - 3.2, color=INH, lw=1.4, label="minus the surround's prediction")
    axs[0].set_yticks([]); axs[0].set_xlabel("position along the row"); clean(axs[0])
    axs[0].spines["left"].set_visible(False)
    axs[0].legend(frameon=False, fontsize=8.5, loc="lower left", bbox_to_anchor=(0.04, 1.0), ncol=2)
    axs[0].text(-0.02, 1.04, "A", transform=axs[0].transAxes, fontsize=10)
    bins = np.linspace(-4, 4, 81)
    axs[1].hist(x, bins=bins, color=EXC, alpha=0.55, density=True, label="raw signal")
    axs[1].hist(err, bins=bins, color=INH, alpha=0.65, density=True, label="error sent onward")
    axs[1].set_xlabel("value (in units of the raw\nsignal's standard deviation)"); axs[1].set_yticks([])
    axs[1].text(0.97, 0.62, f"variance\n{ratio:.0f} times smaller", transform=axs[1].transAxes, ha="right", fontsize=9, color=INH)
    axs[1].legend(frameon=False, fontsize=8.5, loc="upper right"); clean(axs[1]); axs[1].spines["left"].set_visible(False)
    axs[1].set_title("B", loc="left", fontsize=10)
    fig.tight_layout(); save(fig, "fig_retina.png")
    return ratio


def fig_equalize():
    """Figure 12.3: matching the response curve to the statistics of the input (after Laughlin 1981)."""
    rng = np.random.default_rng(4)
    c = rng.laplace(0, 0.18, 220000); c = c[np.abs(c) < 1][:200000]  # illustrative distribution of contrasts
    grid = np.linspace(-1, 1, 401)
    cdf = np.searchsorted(np.sort(c), grid) / c.size
    linear = np.clip(0.5 + grid / 2, 0, 1)
    def bits(resp, levels=10):
        r = np.clip((resp * levels).astype(int), 0, levels - 1); p = np.bincount(r, minlength=levels) / r.size
        p = p[p > 0]; return -(p * np.log2(p)).sum()
    b_eq = bits(np.interp(c, grid, cdf)); b_lin = bits(np.interp(c, grid, linear))
    fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.6))
    axs[0].hist(c, bins=np.linspace(-1, 1, 81), color=GRAY, density=True)
    axs[0].set_xlabel("contrast"); axs[0].set_ylabel("how often it occurs"); axs[0].set_yticks([])
    axs[0].set_title("A  contrasts in the scene", loc="left", fontsize=10); clean(axs[0])
    axs[1].plot(grid, cdf, color=EXC, lw=2.2, label=f"matched to the scene: {b_eq:.1f} bits")
    axs[1].plot(grid, linear, color=INH, lw=2, ls="--", label=f"linear: {b_lin:.1f} bits")
    axs[1].set_xlabel("contrast"); axs[1].set_ylabel("response (fraction of maximum)")
    axs[1].set_title("B  two response curves, ten response levels", loc="left", fontsize=10)
    axs[1].legend(frameon=False, fontsize=8.5, loc="upper left"); clean(axs[1])
    fig.tight_layout(); save(fig, "fig_equalize.png")
    return b_eq, b_lin


def fig_successor():
    """Figure 12.4: a predictive map on a linear track (successor representation)."""
    n, g = 40, 0.85
    T_r = np.zeros((n, n)); T_w = np.zeros((n, n))
    for s in range(n):
        T_r[s, min(s + 1, n - 1)] += 0.9; T_r[s, s] += 0.1                 # mostly runs rightward
        T_w[s, max(s - 1, 0)] += 0.5; T_w[s, min(s + 1, n - 1)] += 0.5     # wanders either way
    fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.4), sharey=True)
    for ax, T, title in [(axs[0], T_w, "A  wandering in both directions"), (axs[1], T_r, "B  running one way, left to right")]:
        M = np.linalg.inv(np.eye(n) - g * T)
        for j, c in [(14, EXC), (24, INH)]:
            f = M[:, j] / M[:, j].max()
            ax.plot(np.arange(n), f, color=c, lw=2); ax.axvline(j, color=c, lw=0.8, ls=":")
        ax.set_title(title, loc="left", fontsize=10); ax.set_xlabel("animal's position on the track"); clean(ax)
    axs[0].set_ylabel("activity of a cell for\none location (normalized)")
    axs[1].annotate("field extends backward,\nagainst the direction of travel", (20.5, 0.5), (27, 0.55), fontsize=8.5, color=GRAY,
                    arrowprops=dict(arrowstyle="->", color=GRAY))
    fig.tight_layout(); save(fig, "fig_successor.png")


def changepoint_run(seed=2, n=300, H=0.03, sigma=20.0, slow=0.1, fast=0.6):
    """Observations from a mean that jumps at random change-points; three learners track it.
    The adaptive learner is the approximately Bayesian delta rule of Nassar et al. (2010)."""
    rng = np.random.default_rng(seed)
    mu = np.empty(n); m = 150.0
    for t in range(n):
        if t > 0 and rng.random() < H: m = rng.uniform(20, 280)
        mu[t] = m
    x = mu + rng.normal(0, sigma, n)
    est = {"slow": np.empty(n), "fast": np.empty(n), "adaptive": np.empty(n)}; lr = np.empty(n)
    b = {"slow": 150.0, "fast": 150.0, "adaptive": 150.0}; r = 1.0
    for t in range(n):
        for k in b: est[k][t] = b[k]
        d = x[t] - b["adaptive"]; var = sigma ** 2 * (1 + 1 / r)
        like_cp = H / 300.0; like_same = (1 - H) * np.exp(-d * d / (2 * var)) / np.sqrt(2 * np.pi * var)
        om = like_cp / (like_cp + like_same); a = om + (1 - om) / (r + 1)
        lr[t] = a; b["adaptive"] += a * d; r = (1 - om) * (r + 1) + om
        b["slow"] += slow * (x[t] - b["slow"]); b["fast"] += fast * (x[t] - b["fast"])
    return mu, x, est, lr


def fig_learning_rate():
    """Figure 12.5: an adaptive learning rate (after Nassar et al. 2010)."""
    runs = [changepoint_run(seed=s) for s in range(100)]
    err = {k: np.mean([np.sqrt(np.mean((r[2][k] - r[0]) ** 2)) for r in runs]) for k in ("slow", "fast", "adaptive")}
    mu, x, est, lr = changepoint_run(seed=5)
    fig, axs = plt.subplots(2, 1, figsize=(9.4, 5.2), sharex=True, gridspec_kw={"height_ratios": [2.2, 1]})
    t = np.arange(len(mu))
    axs[0].plot(t, x, ".", color="#bbbbbb", ms=3, label="observations")
    axs[0].plot(t, mu, color="black", lw=1.2, label="hidden mean")
    axs[0].plot(t, est["slow"], color=GOLD, lw=1.6, ls="--", label="fixed rate 0.1")
    axs[0].plot(t, est["fast"], color=GRAY, lw=1.2, ls=":", label="fixed rate 0.6")
    axs[0].plot(t, est["adaptive"], color=INH, lw=1.8, label="adaptive rate")
    axs[0].set_ylabel("value"); axs[0].legend(frameon=False, fontsize=8, loc="upper left", ncol=2, bbox_to_anchor=(0, 1.22))
    clean(axs[0]); axs[0].set_title("A", loc="left", fontsize=10, pad=34)
    axs[1].plot(t, lr, color=INH, lw=1.6); axs[1].set_ylim(0, 1.05)
    axs[1].set_ylabel("adaptive\nlearning rate"); axs[1].set_xlabel("trial"); clean(axs[1])
    axs[1].set_title("B", loc="left", fontsize=10)
    fig.tight_layout(); save(fig, "fig_learning_rate.png")
    return err


LADDER = [("sensory adaptation", 1e-2, 3e2, EXC), ("short-term synaptic plasticity", 1e-2, 1e1, EXC),
          ("neuromodulatory change in learning rate", 1e0, 1e3, GOLD), ("dark adaptation of the eye", 6e1, 2.4e3, EXC),
          ("motor adaptation", 6e1, 1e5, GOLD), ("long-term potentiation and consolidation", 3.6e3, 3e8, INH),
          ("synaptic scaling", 3.6e4, 3e5, INH), ("development and critical periods", 3e6, 6e8, INH),
          ("evolution of innate priors", 3e12, 3e16, GRAY)]


def fig_timescales():
    """Figure 12.6: adaptation on every timescale (schematic; ranges approximate)."""
    fig, ax = plt.subplots(figsize=(9.4, 4.2))
    for i, (lab, a, b, c) in enumerate(LADDER[::-1]):
        ax.plot([a, b], [i, i], color=c, lw=7, solid_capstyle="butt")
        ax.text(a / 1.4, i, lab, ha="right", va="center", fontsize=8.8)
    ticks = [1e-2, 1, 60, 3600, 86400, 3.15e7, 3.15e9, 3.15e12, 3.15e15]
    labs = ["10 ms", "1 s", "1 min", "1 h", "1 day", "1 year", "100 years", "100,000\nyears", "100 million\nyears"]
    ax.set_xscale("log"); ax.set_xticks(ticks); ax.set_xticklabels(labs, fontsize=8)
    ax.set_xlim(1e-8, 1e17); ax.set_yticks([]); ax.set_ylim(-0.8, len(LADDER) - 0.2)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.set_xlabel("timescale (logarithmic)")
    fig.tight_layout(); save(fig, "fig_timescales.png")


def fig_two_ways():
    """Figure 12.7: two ways to reduce a prediction error."""
    fig, ax = plt.subplots(figsize=(8.6, 4.0))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    box(ax, 2, 2.5, 2.6, 1.1, "the brain's model\n(predictions)", ec=EXC, color=EXC, fs=9.5, weight="bold")
    box(ax, 8, 2.5, 2.6, 1.1, "the world\nand the body", ec=GRAY, fs=9.5, weight="bold")
    box(ax, 5, 2.5, 1.9, 0.8, "prediction\nerror", ec=INH, color=INH, fs=9.5)
    arrow(ax, (3.35, 2.5), (4.0, 2.5), color=EXC); arrow(ax, (6.65, 2.5), (6.0, 2.5), color=GRAY)
    arrow(ax, (5, 3.0), (2.4, 3.15), color=INH, lw=1.8, cs="arc3,rad=0.35")
    ax.text(3.6, 3.95, "1. change the model:\nperceive and learn", ha="center", fontsize=9, color=INH)
    arrow(ax, (5, 2.0), (7.6, 1.85), color=GOLD, lw=1.8, cs="arc3,rad=0.35")
    ax.text(6.4, 0.95, "2. change the world:\nact", ha="center", fontsize=9, color=GOLD)
    fig.tight_layout(); save(fig, "fig_two_ways.png")


if __name__ == "__main__":
    fig_map()
    print("retina variance ratio", round(fig_retina(), 1))
    print("bits", [round(v, 2) for v in fig_equalize()])
    fig_successor()
    print("rms errors", {k: round(v, 1) for k, v in fig_learning_rate().items()})
    fig_timescales(); fig_two_ways()
