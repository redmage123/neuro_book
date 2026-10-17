#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 8 (Decision-Making Under Uncertainty). Outputs into ./images.
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


def fig_decision_overview():
    """Figure 8.1: the parts of a decision."""
    fig, ax = plt.subplots(figsize=(9.4, 4.8)); ax.set_xlim(0, 19); ax.set_ylim(-0.4, 9.2); ax.axis("off")
    box(ax, 2.3, 6.8, 4.1, 1.3, "sensory evidence\n(noisy, arrives over time)", fc="#f6f6f6")
    box(ax, 2.3, 2.4, 4.1, 1.3, "state of the body\n(Chapter 7)", fc="#f6f6f6")
    box(ax, 7.7, 6.8, 4.6, 1.3, "accumulate to a bound\n(parietal and frontal cortex)", ec=EXC, color=EXC)
    box(ax, 7.7, 2.4, 5.0, 1.8, "value the options\n(orbitofrontal and ventromedial\nprefrontal cortex, striatum)", ec=GOLD, color="#8a6d00", fs=8.5)
    box(ax, 13.1, 4.6, 4.4, 1.3, "select one action\n(basal ganglia, Chapter 4)", ec=GREEN, color=GREEN)
    box(ax, 17.4, 4.6, 2.2, 1.1, "act", fc="#f6f6f6", fs=10, weight="bold")
    box(ax, 13.9, 0.5, 7.4, 1.0, "outcome: prediction error (dopamine, Chapter 3)", ec=INH, color=INH, fs=8.5)
    arrow(ax, (4.45, 6.8), (5.3, 6.8)); arrow(ax, (4.45, 2.4), (5.3, 2.4))
    arrow(ax, (10.1, 6.5), (11.4, 5.35), color=EXC); arrow(ax, (10.3, 2.7), (11.4, 3.85), color="#8a6d00")
    arrow(ax, (15.35, 4.6), (16.25, 4.6), color=GREEN)
    arrow(ax, (17.4, 4.0), (16.5, 1.1), color=INH, cs="arc3,rad=-0.15")
    arrow(ax, (10.15, 0.5), (7.7, 1.45), color=INH, cs="arc3,rad=-0.25"); ax.text(8.0, 0.05, "updates values", fontsize=8, color=INH, style="italic", ha="center")
    arrow(ax, (7.7, 3.35), (7.7, 6.1), color=GRAY, ls="--", style="<|-|>")
    ax.text(7.95, 4.7, "value and evidence\ninteract", fontsize=8, color=GRAY, style="italic", va="center")
    ax.text(7.7, 7.85, "how sure? (confidence)", fontsize=8.5, color=EXC, ha="center", style="italic")
    ax.text(13.0, 6.0, "explore or exploit?\nplan or repeat?", fontsize=8.5, color=GREEN, ha="center", style="italic")
    save(fig, "fig_decision_overview.png")


def fig_lip_ramps():
    """Figure 8.2: LIP ramps by coherence (illustrative)."""
    cohs = [0.512, 0.256, 0.128, 0.064, 0.0]
    cols = [EXC, "#3b6ea0", "#6f97bf", "#a3bcd6", GRAY]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9, 3.6), sharey=True)
    t = np.linspace(0, 0.8, 200)
    for c, col in zip(cohs, cols):
        r = 20 + np.where(t > 0.2, (t - 0.2) * (25 + 320 * c), 0) - np.where(t < 0.2, 5 * np.sin(t / 0.2 * np.pi), 0)
        a1.plot(t * 1000, np.where(r <= 68, r, np.nan), color=col, lw=2, label=f"{c * 100:.1f}%")
        rt = np.linspace(-0.6, 0.0, 240)
        slope = 25 + 320 * c
        ramp = 68 + slope * (rt + 0.07)                      # reaches the common level 70 ms before the movement
        burst = 68 + (rt + 0.07) / 0.07 * 10                 # shared presaccadic rise after the level is reached
        y = np.where(rt < -0.07, ramp, burst)
        a2.plot(rt * 1000, np.where(y >= 20, y, np.nan), color=col, lw=2)   # start each trace at the motion-onset level
    a1.set_xlabel("time from motion onset (ms)"); a1.set_ylabel("firing rate (spikes/s)")
    a1.legend(title="motion strength", frameon=False, fontsize=8, title_fontsize=8, loc="upper left")
    a2.axhline(68, color=GRAY, ls=":", lw=1); a2.text(-590, 70, "common level", fontsize=8, color=GRAY); a2.set_ylim(10, 82)
    a2.axvline(-70, color=GOLD, lw=1); a2.text(-75, 25, "about 70 ms\nbefore the\neye moves", fontsize=8, color="#8a6d00", ha="right")
    a2.set_xlabel("time to eye movement (ms)")
    a1.set_ylim(10, 84); a1.set_title("A", loc="left", weight="bold"); a2.set_title("B", loc="left", weight="bold")
    clean(a1); clean(a2)
    fig.tight_layout(); save(fig, "fig_lip_ramps.png")


V = 0.582  # drift for the "weak evidence" example in the text (70 percent correct in 0.5 s)


def fig_drift_diffusion():
    """Figure 8.3: drift diffusion traces and the speed-accuracy trade-off."""
    rng = np.random.default_rng(3)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.4, 3.9), gridspec_kw={"width_ratios": [1.25, 1]})
    a, dt = 1.0, 0.002
    for k in range(9):
        x, xs = 0.0, [0.0]
        while abs(x) < a and len(xs) < 3000:
            x += V * dt + np.sqrt(dt) * rng.normal(); xs.append(x)
        tt = np.arange(len(xs)) * dt
        col = EXC if x >= a else INH
        a1.plot(tt, np.clip(xs, -a, a), color=col, lw=1.2, alpha=0.85)
    a1.axhline(a, color=EXC, lw=2); a1.axhline(-a, color=INH, lw=2)
    a1.text(0.02, a + 0.06, "bound: choose the correct option", color=EXC, fontsize=8.5)
    a1.text(0.02, -a - 0.17, "bound: choose the wrong option", color=INH, fontsize=8.5)
    a1.set_ylim(-1.35, 1.35); a1.set_xlabel("time (s)"); a1.set_ylabel("accumulated evidence"); a1.set_title("A", loc="left", weight="bold")
    clean(a1)
    bounds = np.linspace(0.1, 2.5, 200)
    acc = 1 / (1 + np.exp(-2 * V * bounds)); mdt = bounds / V * np.tanh(bounds * V)
    a2.plot(bounds, acc * 100, color=EXC, lw=2.2); a2.set_ylabel("percent correct", color=EXC); a2.set_ylim(50, 100)
    a2.set_xlabel("height of the bound"); a2.set_title("B", loc="left", weight="bold")
    b2 = a2.twinx(); b2.plot(bounds, mdt, color=GOLD, lw=2.2, ls="--"); b2.set_ylabel("mean decision time (s)", color="#8a6d00")
    for bb, lab in [(0.728, "70% correct, 0.5 s"), (1.887, "90% correct, 2.6 s")]:
        a2.plot([bb], [100 / (1 + np.exp(-2 * V * bb))], "o", color=EXC); a2.annotate(lab, (bb, 100 / (1 + np.exp(-2 * V * bb))), xytext=(-12, 10), textcoords="offset points", fontsize=8, color=EXC, ha="right")
    a2.spines[["top"]].set_visible(False); b2.spines[["top"]].set_visible(False)
    fig.tight_layout(); save(fig, "fig_drift_diffusion.png")


def fig_prospect_theory():
    """Figure 8.4: Tversky and Kahneman (1992) value and weighting functions."""
    alpha, lam, gamma = 0.88, 2.25, 0.61
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9, 3.9))
    x = np.linspace(-100, 100, 401)
    v = np.where(x >= 0, np.abs(x) ** alpha, -lam * np.abs(x) ** alpha)
    a1.plot(x, v, color=EXC, lw=2.4); a1.axhline(0, color=GRAY, lw=0.8); a1.axvline(0, color=GRAY, lw=0.8)
    a1.set_xlabel("outcome relative to reference point"); a1.set_ylabel("subjective value")
    a1.text(62, 12, "gains", color=GREEN, fontsize=9); a1.text(12, -120, "losses loom about\ntwice as large\nas equal gains", color=INH, fontsize=9)
    a1.set_xticks([-100, -50, 0, 50, 100]); a1.set_yticks([]); a1.set_title("A", loc="left", weight="bold"); clean(a1)
    p = np.linspace(0.0001, 0.9999, 400)
    w = p ** gamma / (p ** gamma + (1 - p) ** gamma) ** (1 / gamma)
    a2.plot(p, w, color=EXC, lw=2.4, label="decision weight"); a2.plot([0, 1], [0, 1], color=GRAY, ls=":", lw=1.2, label="probability itself")
    a2.set_xlabel("probability"); a2.set_ylabel("decision weight"); a2.legend(frameon=False, fontsize=8.5, loc="upper left")
    a2.annotate("small chances\noverweighted", (0.05, p[20] ** gamma / (p[20] ** gamma + (1 - p[20]) ** gamma) ** (1 / gamma)), xytext=(0.22, 0.08), fontsize=8, color=GRAY, arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.8))
    a2.annotate("large chances\nunderweighted", (0.85, 0.85 ** gamma / (0.85 ** gamma + 0.15 ** gamma) ** (1 / gamma)), xytext=(0.55, 0.88), fontsize=8, color=GRAY, arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.8))
    a2.set_title("B", loc="left", weight="bold"); clean(a2)
    fig.tight_layout(); save(fig, "fig_prospect_theory.png")


def fig_discounting():
    """Figure 8.5: hyperbolic vs exponential discounting and preference reversal (illustrative)."""
    k = 0.2; r = 0.05
    t = np.linspace(0, 30.999, 600)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.2, 3.8), sharey=True)
    for ax, kind in [(a1, "hyperbolic"), (a2, "exponential")]:
        if kind == "hyperbolic":
            vs = np.where(t <= 30, 100 / (1 + k * (30 - t)), np.nan); vl = 110 / (1 + k * (31 - t))
        else:
            vs = np.where(t <= 30, 100 * np.exp(-r * (30 - t)), np.nan); vl = 110 * np.exp(-r * (31 - t))
        ax.plot(t, vs, color=INH, lw=2.2, label="100 dollars on day 30")
        ax.plot(t, vl, color=EXC, lw=2.2, label="110 dollars on day 31")
        ax.set_xlabel("today's date (day)"); ax.set_xlim(0, 31); clean(ax)
        ax.set_title(("A" if kind == "hyperbolic" else "B") + f": {kind}", loc="left", weight="bold")
    a1.set_ylabel("value seen from today"); a1.legend(frameon=False, fontsize=8.5, loc="upper left")
    k_cross = 30 - (110 - 100) / (k * 10) / 1.0  # crossing day for hyperbolic: 100(1+k(31-t)) = 110(1+k(30-t))
    tc = (100 * (1 + 31 * k) - 110 * (1 + 30 * k)) / (100 * k - 110 * k)
    a1.axvline(tc, color=GOLD, lw=1.2, ls="--"); a1.text(tc - 0.5, 92, "preference\nreverses", ha="right", fontsize=8.5, color="#8a6d00")
    a2.text(2, 80, "the curves never cross", fontsize=8.5, color=GRAY)
    fig.tight_layout(); save(fig, "fig_discounting.png")


def fig_explore_exploit():
    """Figure 8.6: uncertainty and a ten-armed bandit (simulated)."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.4, 3.9), gridspec_kw={"width_ratios": [1, 1.3]})
    x = np.linspace(-3, 5, 400)
    g = lambda m, s: np.exp(-0.5 * ((x - m) / s) ** 2) / (s * np.sqrt(2 * np.pi))
    a1.plot(x, g(1.0, 0.25), color=EXC, lw=2.2, label="tried 40 times"); a1.fill_between(x, g(1.0, 0.25), color=EXC, alpha=0.12)
    a1.plot(x, g(0.8, 1.1), color=GOLD, lw=2.2, label="tried twice"); a1.fill_between(x, g(0.8, 1.1), color=GOLD, alpha=0.15)
    a1.set_xlabel("estimated value of the option"); a1.set_yticks([]); a1.set_ylabel("belief")
    a1.legend(frameon=False, fontsize=8.5); a1.set_title("A", loc="left", weight="bold"); clean(a1)
    rng = np.random.default_rng(7); runs, steps, K = 400, 1000, 10
    res = {"always exploit": np.zeros(steps), "explore at random (10%)": np.zeros(steps), "explore where uncertain": np.zeros(steps)}
    for _ in range(runs):
        q = rng.normal(0, 1, K)
        for name in res:
            est = np.zeros(K); n = np.zeros(K)
            for s in range(steps):
                if name == "always exploit":
                    a = int(np.argmax(est + 1e-6 * rng.random(K)))
                elif name.startswith("explore at random"):
                    a = int(rng.integers(K)) if rng.random() < 0.1 else int(np.argmax(est + 1e-6 * rng.random(K)))
                else:
                    a = int(np.argmin(n)) if n.min() == 0 else int(np.argmax(est + 2 * np.sqrt(np.log(s + 1) / n)))
                rwd = q[a] + rng.normal(); n[a] += 1; est[a] += (rwd - est[a]) / n[a]; res[name][s] += rwd
    for (name, v), col, ls in zip(res.items(), [GRAY, INH, EXC], ["-", "--", "-"]):
        sm = np.convolve(v / runs, np.ones(20) / 20, mode="valid")
        a2.plot(np.arange(len(sm)) + 10, sm, color=col, lw=2, ls=ls, label=name)
    a2.set_xlabel("trial"); a2.set_ylabel("average reward"); a2.legend(frameon=False, fontsize=8.5, loc="lower right")
    a2.set_title("B", loc="left", weight="bold"); clean(a2)
    fig.tight_layout(); save(fig, "fig_explore_exploit.png")


def fig_devaluation():
    """Figure 8.7: devaluation after moderate vs extended training (illustrative)."""
    fig, ax = plt.subplots(figsize=(7, 3.8))
    xs = np.array([0, 1]); w = 0.34
    control = [10, 10.5]; deval = [4.5, 9.8]
    ax.bar(xs - w / 2, control, w, color=EXC, label="outcome still valued")
    ax.bar(xs + w / 2, deval, w, color=INH, label="outcome devalued")
    ax.set_xticks(xs); ax.set_xticklabels(["moderate training", "extended training"])
    ax.set_ylabel("lever presses per minute\n(test, no outcome delivered)"); ax.set_yticks([])
    ax.text(0, 11.6, "goal-directed:\nchecks the outcome", ha="center", fontsize=9, color=GRAY)
    ax.text(1, 11.6, "habit:\nrepeats the action", ha="center", fontsize=9, color=GRAY)
    ax.set_ylim(0, 14.5); ax.legend(frameon=False, fontsize=8.5, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2); clean(ax)
    save(fig, "fig_devaluation.png")


if __name__ == "__main__":
    for f in (fig_decision_overview, fig_lip_ramps, fig_drift_diffusion, fig_prospect_theory, fig_discounting,
              fig_explore_exploit, fig_devaluation):
        f()
    print("figures written to", OUT)
