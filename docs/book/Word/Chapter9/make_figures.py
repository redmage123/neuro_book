#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 9 (Habits, Skills, and Automaticity). Outputs into ./images.
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


def fig_practice_curve():
    """Figure 9.1: practice curve on linear and log-log axes (illustrative, after Crossman 1959)."""
    floor = 8.0
    T = lambda n: floor + 608 * n ** -0.5
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 3.8))
    na = np.linspace(10, 5e3, 600)
    a.plot(na / 1e3, T(na), color=EXC, lw=2); a.axhline(floor, color=INH, ls="--", lw=1.2)
    a.text(4.95, floor - 9, "machine cycle time", color=INH, ha="right", fontsize=9)
    a.set_xlabel("cigars made (thousands)"); a.set_ylabel("seconds per cigar"); a.set_ylim(-15, 210)
    a.set_yticks([0, 50, 100, 150, 200])
    a.set_title("A  the first 5,000 cigars", loc="left", fontsize=10); clean(a)
    nb = np.logspace(1, 7.3, 300)
    b.loglog(nb, T(nb), color=EXC, lw=2); b.axhline(floor, color=INH, ls="--", lw=1.2)
    x1, x2 = 10.0, 1000.0
    k = np.log(T(x2) / T(x1)) / np.log(x2 / x1)
    nl = np.logspace(1, 5, 50)
    b.loglog(nl, T(x1) * (nl / x1) ** k, color=GRAY, ls=":", lw=1.4)
    b.text(2e3, 60, "dotted: a power function,\na straight line on these axes", color=GRAY, fontsize=9)
    b.text(1.5e7, floor * 0.8, "machine cycle time", color=INH, fontsize=9, ha="right")
    b.set_xlabel("cigars made (log scale)"); b.set_ylabel("seconds per cigar (log scale)")
    b.set_ylim(4, 300); b.set_yticks([5, 10, 20, 50, 100, 200]); b.set_yticklabels(["5", "10", "20", "50", "100", "200"])
    b.set_title("B  the whole record, logarithmic axes", loc="left", fontsize=10); clean(b)
    fig.tight_layout(); save(fig, "fig_practice_curve.png")


def two_rate(pert, Af=0.92, Bf=0.06, As=0.996, Bs=0.015):
    xf = xs = 0.0; F, S, X = [], [], []
    for p in pert:
        x = xf + xs; F.append(xf); S.append(xs); X.append(x)
        if np.isnan(p):          # error clamp: no error information
            e = 0.0
        else:
            e = p - x
        xf = Af * xf + Bf * e; xs = As * xs + Bs * e
    return np.array(F), np.array(S), np.array(X)


def two_rate_schedule():
    """Adapt 300 trials, find the counter-perturbation length that returns output to zero, then clamp 150."""
    best = None
    for k in range(1, 80):
        pert = np.r_[np.ones(300), -np.ones(k)]
        x = two_rate(pert)[2]
        nxt = two_rate(np.r_[pert, np.nan])[2][-1]
        if nxt <= 0:
            best = k; break
    return np.r_[np.ones(300), -np.ones(best), np.full(150, np.nan)], best


def fig_two_rate():
    """Figure 9.2: two-state model of adaptation with spontaneous recovery (simulated)."""
    pert, k = two_rate_schedule()
    F, S, X = two_rate(pert)
    tr = np.arange(len(pert))
    fig, ax = plt.subplots(figsize=(9.2, 3.9))
    p = np.where(np.isnan(pert), np.nan, pert)
    ax.step(tr, p, where="post", color="#bbbbbb", lw=1.2, label="perturbation")
    ax.plot(tr, X, color="black", lw=2.2, label="total adaptation")
    ax.plot(tr, S, color=EXC, lw=1.6, label="slow process")
    ax.plot(tr, F, color=INH, lw=1.6, label="fast process")
    ax.axhline(0, color=GRAY, lw=0.6)
    e = 300 + k
    ax.axvspan(e, len(pert), color=GOLD, alpha=0.12)
    ax.text(e + 75, -0.95, "error-clamp trials\n(error held at zero)", ha="center", color="#8a6d00", fontsize=9)
    ax.annotate("spontaneous\nrecovery", xy=(e + 40, X[e + 40]), xytext=(e + 70, 0.6),
                arrowprops=dict(arrowstyle="-|>", color=GRAY), fontsize=9, ha="center")
    ax.annotate("brief opposite\nperturbation", xy=(300 + k / 2, -1), xytext=(215, -0.75),
                arrowprops=dict(arrowstyle="-|>", color=GRAY), fontsize=9, ha="center")
    ax.set_xlabel("trial"); ax.set_ylabel("adaptation (fraction of perturbation)")
    ax.set_ylim(-1.15, 1.15); ax.legend(loc="upper left", frameon=False, fontsize=8.5, ncol=2); clean(ax)
    fig.tight_layout(); save(fig, "fig_two_rate.png")
    return k


def fig_task_bracketing():
    """Figure 9.3: task-bracketing (illustrative, after Jog et al. 1999; Barnes et al. 2005)."""
    x = np.linspace(0, 1, 400)
    early = 0.55 + 0.12 * np.sin(6 * x) + 0.18 * np.exp(-((x - 0.45) / 0.12) ** 2) + 0.15 * np.exp(-((x - 0.7) / 0.1) ** 2)
    late = 0.15 + 0.95 * np.exp(-((x - 0.06) / 0.05) ** 2) + 0.8 * np.exp(-((x - 0.94) / 0.05) ** 2) + 0.06 * np.exp(-((x - 0.5) / 0.1) ** 2)
    fig, axs = plt.subplots(2, 1, figsize=(9.0, 4.4), sharex=True)
    for ax, y, c, lab in [(axs[0], early, GRAY, "early in training"), (axs[1], late, EXC, "after extended training")]:
        ax.fill_between(x, 0, y, color=c, alpha=0.25); ax.plot(x, y, color=c, lw=2)
        ax.set_ylim(0, 1.25); ax.set_yticks([]); ax.set_ylabel("striatal\nactivity", fontsize=9)
        ax.text(0.99, 1.08, lab, ha="right", fontsize=9.5, color=c, weight="bold"); clean(ax)
    for xv, lab in [(0.06, "start"), (0.33, "tone"), (0.6, "turn"), (0.94, "goal")]:
        for ax in axs: ax.axvline(xv, color="#cccccc", lw=0.8, ls=":")
    axs[1].set_xticks([0.06, 0.33, 0.6, 0.94]); axs[1].set_xticklabels(["start", "tone", "turn", "goal"])
    axs[1].set_xlabel("position in the maze run")
    fig.tight_layout(); save(fig, "fig_task_bracketing.png")


def fig_striatal_loops():
    """Figure 9.4: limbic, associative and sensorimotor loops and the dopamine spiral (after Haber et al. 2000)."""
    fig, ax = plt.subplots(figsize=(9.6, 5.8)); ax.set_xlim(0, 20); ax.set_ylim(-0.6, 11.2); ax.axis("off")
    cols = [(3.4, GREEN, "#1b5e20", "motivation", "orbital and medial\nprefrontal cortex", "ventral striatum\n(limbic)"),
            (10.0, GOLD, "#8a6d00", "goal-directed", "dorsolateral\nprefrontal cortex", "dorsomedial striatum\n(mainly caudate)"),
            (16.6, EXC, EXC, "habitual, automatic", "motor and\npremotor cortex", "dorsolateral striatum\n(posterior putamen)")]
    for x, ec, tc, head, ctx, stri in cols:
        ax.text(x, 10.7, head, ha="center", fontsize=10, weight="bold", color=tc)
        box(ax, x, 9.4, 4.4, 1.2, ctx, ec=ec, color=tc, fs=8.5)
        box(ax, x, 6.5, 4.4, 1.2, stri, ec=ec, color=tc, fs=8.5)
        box(ax, x, 3.7, 4.4, 1.1, "pallidum and SNr,\nthen thalamus", ec=ec, color=tc, fs=8.5)
        box(ax, x, 0.6, 3.6, 1.0, "dopamine neurons", ec=GRAY, color=GRAY, fs=8.5)
        arrow(ax, (x - 0.6, 8.75), (x - 0.6, 7.15), color=ec)
        arrow(ax, (x - 0.6, 5.85), (x - 0.6, 4.3), color=ec)
        arrow(ax, (x - 2.45, 4.0), (x - 2.45, 9.1), color=ec, cs="arc3,rad=0.12")
        arrow(ax, (x + 1.6, 1.15), (x + 2.5, 5.85), color=GRAY, ls="--", cs="arc3,rad=0.15")
    for (x1, _, _, _, _, _), (x2, _, _, _, _, _) in zip(cols[:-1], cols[1:]):
        arrow(ax, (x1 + 1.2, 5.85), (x2 - 1.0, 1.15), color="#7b1fa2", ls=":", lw=1.8)
    ax.text(10.0, -0.45, "dashed: dopamine to its own striatal region;  dotted: striatum to the dopamine neurons of the next loop (the spiral)",
            ha="center", fontsize=8.5, color=GRAY)
    arrow(ax, (5.9, 10.7), (7.6, 10.7), color=GRAY, lw=2.2)
    arrow(ax, (12.4, 10.7), (13.9, 10.7), color=GRAY, lw=2.2)
    save(fig, "fig_striatal_loops.png")


def fig_instance_race():
    """Figure 9.6: Logan's instance race (simulated)."""
    N = np.unique(np.logspace(0, 3, 40).astype(int))
    rng = np.random.default_rng(1); algo, shape, scale = 1.0, 2.0, 4.0
    rt, pr = [], []
    for n in N:
        if n == 1:
            rt.append(algo); pr.append(0.0); continue
        m = scale * rng.weibull(shape, size=(20000, n - 1)).min(axis=1)
        rt.append(np.minimum(m, algo).mean()); pr.append((m < algo).mean())
    rt, pr = np.array(rt), np.array(pr)
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 3.8))
    a.loglog(N, rt, "o-", color=EXC, ms=3.5, lw=1.5)
    a.axhline(algo, color=INH, ls="--", lw=1.2); a.text(1.2, algo * 1.06, "procedure alone", color=INH, fontsize=9)
    a.set_xlabel("practice trials (log scale)"); a.set_ylabel("mean response time, s (log scale)")
    a.set_yticks([0.05, 0.1, 0.2, 0.5, 1]); a.set_yticklabels(["0.05", "0.1", "0.2", "0.5", "1"]); a.set_title("A  response time", loc="left", fontsize=10); clean(a)
    b.semilogx(N, 100 * pr, "o-", color=GOLD, ms=3.5, lw=1.5)
    b.set_ylim(0, 105); b.set_xlabel("practice trials (log scale)"); b.set_ylabel("trials won by memory retrieval (%)")
    b.set_title("B  who wins the race", loc="left", fontsize=10); clean(b)
    fig.tight_layout(); save(fig, "fig_instance_race.png")


def fig_contextual_interference():
    """Figure 9.7: blocked vs random practice (illustrative, after Shea & Morgan 1979)."""
    blocks = np.arange(1, 7)
    blocked = np.array([1350, 1050, 900, 820, 770, 740])
    random_ = np.array([1500, 1250, 1080, 960, 880, 830])
    fig, ax = plt.subplots(figsize=(9.0, 3.9))
    ax.plot(blocks, blocked, "o-", color=EXC, lw=2, label="blocked practice")
    ax.plot(blocks, random_, "s-", color=GOLD, lw=2, label="random practice")
    tests = {"10 min": 8.2, "10 days": 9.4, "new\npattern": 10.6}
    vals = {"10 min": (900, 780), "10 days": (960, 800), "new\npattern": (1050, 900)}
    for lab, x in tests.items():
        bv, rv = vals[lab]
        ax.plot(x - 0.15, bv, "o", color=EXC, ms=7); ax.plot(x + 0.15, rv, "s", color=GOLD, ms=7)
    ax.axvline(7.2, color=GRAY, lw=0.8, ls=":")
    ax.text(3.5, 1560, "acquisition", ha="center", fontsize=9.5, color=GRAY)
    ax.text(9.4, 1560, "tests (random order)", ha="center", fontsize=9.5, color=GRAY)
    ax.set_xticks(list(blocks) + list(tests.values())); ax.set_xticklabels([str(b) for b in blocks] + list(tests.keys()), fontsize=8.5)
    ax.set_ylabel("total time, ms (lower is better)"); ax.set_xlabel("practice block")
    ax.set_ylim(650, 1620); ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, 0.88)); clean(ax)
    fig.tight_layout(); save(fig, "fig_contextual_interference.png")


def fig_song_circuit():
    """Figure 9.5: the songbird learning circuit."""
    fig, ax = plt.subplots(figsize=(9.4, 4.6)); ax.set_xlim(0, 19); ax.set_ylim(0, 9.4); ax.axis("off")
    box(ax, 3.0, 7.6, 3.0, 1.0, "HVC", ec=EXC, color=EXC, fs=10, weight="bold")
    box(ax, 11.0, 7.6, 3.0, 1.0, "RA", ec=EXC, color=EXC, fs=10, weight="bold")
    box(ax, 16.4, 7.6, 3.6, 1.2, "brainstem\n(vocal muscles)", ec=EXC, color=EXC)
    box(ax, 3.0, 3.0, 3.6, 1.2, "Area X\n(basal ganglia)", ec=GOLD, color="#8a6d00")
    box(ax, 7.4, 1.2, 3.0, 1.0, "DLM\n(thalamus)", ec=GOLD, color="#8a6d00", fs=8.5)
    box(ax, 11.0, 3.6, 3.0, 1.0, "LMAN", ec=GOLD, color="#8a6d00", fs=10, weight="bold")
    box(ax, 3.0, 0.9, 3.0, 1.0, "VTA\n(dopamine)", ec=GREEN, color=GREEN, fs=8.5)
    arrow(ax, (4.6, 7.6), (9.4, 7.6), color=EXC, lw=2)
    arrow(ax, (12.6, 7.6), (14.5, 7.6), color=EXC, lw=2)
    arrow(ax, (3.0, 7.0), (3.0, 3.7), color=GOLD)
    arrow(ax, (4.3, 2.5), (5.85, 1.45), color=GOLD)
    arrow(ax, (8.5, 1.6), (10.2, 3.05), color=GOLD)
    arrow(ax, (11.0, 4.2), (11.0, 7.0), color=GOLD, lw=2)
    arrow(ax, (3.0, 1.45), (3.0, 2.35), color=GREEN, ls="--")
    ax.text(7.0, 8.75, "motor pathway: produces the song", ha="center", fontsize=9, color=EXC)
    ax.text(11.3, 5.4, "injects\nvariability", ha="left", fontsize=9, color="#8a6d00")
    ax.text(2.8, 1.9, "better or worse\nthan expected", ha="right", va="center", fontsize=8.5, color=GREEN)
    ax.text(15.9, 3.6, "anterior forebrain pathway:\nvaries the song and learns\nwhich variations to keep", ha="center", fontsize=9, color="#8a6d00")
    save(fig, "fig_song_circuit.png")


if __name__ == "__main__":
    fig_practice_curve(); k = fig_two_rate(); fig_task_bracketing(); fig_striatal_loops()
    fig_instance_race(); fig_contextual_interference(); fig_song_circuit()
    print("counter-perturbation trials:", k)
