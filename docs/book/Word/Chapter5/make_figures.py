#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 5 (Plasticity and Memory). Outputs into ./images.
Requires matplotlib and numpy."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle, Ellipse

OUT = Path(__file__).parent / "images"; OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
EXC, INH, GRAY, GOLD, GREEN = "#1f4e79", "#b03a2e", "#555555", "#c9a227", "#2e7d32"


def fig_nmda():
    """Figure 5.1: the NMDA receptor as a coincidence detector."""
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.6))
    for ax, t, depol in zip(axes, ["A. Glutamate alone: NMDA channel blocked", "B. Glutamate + depolarization: calcium enters"], [False, True]):
        ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.set_aspect("equal"); ax.axis("off"); ax.set_title(t, fontsize=9.5, loc="left")
        ax.add_patch(Rectangle((0.5, 4.8), 9, 0.5, fc="#ddd", ec="none")); ax.add_patch(Rectangle((0.5, 2.5), 9, 0.5, fc="#ddd", ec="none"))
        ax.text(0.6, 5.55, "presynaptic terminal", fontsize=8, color=GRAY); ax.text(0.6, 1.9, "postsynaptic spine", fontsize=8, color=GRAY)
        for x in np.linspace(2, 8, 7):
            ax.add_patch(Circle((x + np.random.default_rng(int(x * 10)).uniform(-0.2, 0.2), 4.1), 0.12, fc=GOLD, ec=GOLD))
        ax.text(9.2, 4.0, "glutamate", fontsize=7.5, color=GOLD, ha="right")
        # AMPA receptor
        ax.add_patch(Rectangle((2.3, 2.2), 1.2, 1.1, fc="white", ec=EXC, lw=2)); ax.text(2.9, 1.6, "AMPA", fontsize=8, color=EXC, ha="center")
        ax.annotate("", xy=(2.9, 0.9), xytext=(2.9, 2.2), arrowprops=dict(arrowstyle="-|>", color=EXC, lw=1.5)); ax.text(3.3, 1.1, "Na$^+$", fontsize=8, color=EXC)
        # NMDA receptor
        ax.add_patch(Rectangle((6.0, 2.2), 1.4, 1.1, fc="white", ec=INH, lw=2)); ax.text(6.7, 1.6, "NMDA", fontsize=8, color=INH, ha="center")
        if not depol:
            ax.add_patch(Circle((6.7, 2.45), 0.22, fc=GRAY, ec=GRAY)); ax.text(7.5, 2.3, "Mg$^{2+}$ plug", fontsize=7.5, color=GRAY)
            ax.text(5, 0.6, "membrane near rest: the magnesium ion sits in the pore;\nglutamate is bound but nothing passes", fontsize=7.5, color=GRAY, ha="center")
        else:
            ax.add_patch(Circle((8.3, 1.3), 0.22, fc=GRAY, ec=GRAY)); ax.annotate("", xy=(8.1, 1.4), xytext=(6.9, 2.3), arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1, ls="--"))
            ax.annotate("", xy=(6.7, 0.9), xytext=(6.7, 2.2), arrowprops=dict(arrowstyle="-|>", color=INH, lw=2)); ax.text(5.6, 1.0, "Ca$^{2+}$", fontsize=9, color=INH, fontweight="bold")
            ax.text(5, 0.3, "membrane depolarized (many AMPA inputs, or a back-propagating spike):\nmagnesium is expelled, calcium enters, plasticity machinery starts", fontsize=7.5, color=GRAY, ha="center")
    fig.tight_layout(); fig.savefig(OUT / "fig_nmda.png", dpi=200); plt.close(fig)


def fig_ltp_ltd():
    """Figure 5.2: calcium level decides the direction; time courses of LTP and LTD."""
    fig = plt.figure(figsize=(9, 3.3)); gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.3])
    ax = fig.add_subplot(gs[0]); ca = np.linspace(0, 3, 300)
    dw = np.where(ca < 0.5, 0, np.where(ca < 1.4, -0.6 * np.sin(np.pi * (ca - 0.5) / 0.9), 1.0 * np.sin(np.pi * np.clip((ca - 1.4) / 1.6, 0, 1)) ** 0.7))
    ax.plot(ca, dw, color=EXC, lw=2); ax.axhline(0, color=GRAY, lw=0.8); ax.axvspan(0.5, 1.4, color=INH, alpha=0.08); ax.axvspan(1.4, 3, color=EXC, alpha=0.08)
    ax.text(0.95, -0.72, "moderate, prolonged\nCa$^{2+}$: LTD", ha="center", fontsize=8, color=INH); ax.text(2.2, 0.55, "high, brief\nCa$^{2+}$: LTP", ha="center", fontsize=8, color=EXC)
    ax.set_xlabel("postsynaptic calcium"); ax.set_ylabel("change in synaptic strength"); ax.set_title("A. One signal, two directions", fontsize=9.5, loc="left"); ax.set_xticks([]); ax.set_yticks([-0.5, 0, 0.5, 1]); ax.set_ylim(-0.9, 1.2)
    ax2 = fig.add_subplot(gs[1]); t = np.arange(-10, 60, 0.25); rng = np.random.default_rng(1)
    ltp = np.where(t < 0, 100, 100 + 80 * np.exp(-np.clip(t, 0, None) / 40) * 0 + 70 * (1 - np.exp(-np.clip(t, 0, None) / 2)) * (0.75 + 0.25 * np.exp(-np.clip(t, 0, None) / 15))) + rng.normal(0, 3, t.size)
    ltd = np.where(t < 0, 100, 100 - 35 * (1 - np.exp(-np.clip(t, 0, None) / 4))) + rng.normal(0, 3, t.size)
    ax2.scatter(t, ltp, s=6, color=EXC, label="after 1 s at 100 Hz (LTP)"); ax2.scatter(t, ltd, s=6, color=INH, label="after 15 min at 1 Hz (LTD)")
    ax2.axvline(0, color=GRAY, ls="--", lw=1); ax2.text(1, 185, "induction", fontsize=8, color=GRAY); ax2.axhline(100, color=GRAY, lw=0.8, ls=":")
    ax2.set_xlabel("time (min)"); ax2.set_ylabel("synaptic response (% of baseline)"); ax2.set_ylim(40, 200); ax2.legend(frameon=False, fontsize=8, loc="upper right")
    ax2.set_title("B. The same synapse, strengthened or weakened", fontsize=9.5, loc="left")
    fig.tight_layout(); fig.savefig(OUT / "fig_ltp_ltd.png", dpi=200); plt.close(fig)


def fig_stdp():
    """Figure 5.3: the spike-timing-dependent plasticity window."""
    fig, ax = plt.subplots(figsize=(7, 3.4)); dt = np.linspace(-80, 80, 400)
    win = np.where(dt > 0, 1.0 * np.exp(-dt / 17), -0.5 * np.exp(dt / 34))
    ax.plot(dt, win, color=EXC, lw=2); ax.axhline(0, color=GRAY, lw=0.8); ax.axvline(0, color=GRAY, lw=0.8)
    rng = np.random.default_rng(4); pts = rng.uniform(-70, 70, 50); ax.scatter(pts, np.where(pts > 0, np.exp(-pts / 17), -0.5 * np.exp(pts / 34)) + rng.normal(0, 0.08, 50), s=12, color=GRAY, alpha=0.6)
    ax.fill_between(dt, win, 0, where=dt > 0, color=EXC, alpha=0.1); ax.fill_between(dt, win, 0, where=dt < 0, color=INH, alpha=0.1)
    ax.text(40, 0.75, "pre before post:\n'I helped cause the spike'\nstrengthen", fontsize=8.5, color=EXC, ha="center"); ax.text(-45, 0.55, "post before pre:\n'I arrived too late'\nweaken", fontsize=8.5, color=INH, ha="center")
    ax.set_xlabel("spike timing  $t_{post} - t_{pre}$  (ms)"); ax.set_ylabel("change in strength"); ax.set_ylim(-0.8, 1.2); ax.set_title("Spike-timing-dependent plasticity", fontsize=9.5, loc="left")
    fig.tight_layout(); fig.savefig(OUT / "fig_stdp.png", dpi=200); plt.close(fig)


def fig_homeostasis():
    """Figure 5.4: sliding threshold (BCM) and synaptic scaling."""
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.2))
    ax = axes[0]; x = np.linspace(0, 3, 300)
    for th, c, lab in ((0.8, INH, "after a quiet period (low threshold)"), (1.6, EXC, "after intense activity (high threshold)")):
        y = x * (x - th) * 0.6; ax.plot(x, y, color=c, lw=2, label=lab); ax.plot([th], [0], "o", color=c)
    ax.axhline(0, color=GRAY, lw=0.8); ax.set_ylim(-0.8, 2.2); ax.set_xlabel("postsynaptic activity"); ax.set_ylabel("change in strength"); ax.legend(frameon=False, fontsize=7.5, loc="upper left")
    ax.set_title("A. Sliding threshold: the LTP/LTD crossover moves", fontsize=9.5, loc="left"); ax.set_xticks([]); ax.set_yticks([])
    ax = axes[1]; w = np.array([0.2, 0.5, 0.9, 1.4, 0.7]); idx = np.arange(5)
    ax.bar(idx - 0.2, w, 0.4, color=EXC, label="before"); ax.bar(idx + 0.2, w * 0.6, 0.4, color=GOLD, label="after scaling (x0.6)")
    ax.set_xticks(idx); ax.set_xticklabels([f"S{i + 1}" for i in idx]); ax.set_ylabel("synaptic strength"); ax.legend(frameon=False, fontsize=8)
    ax.set_title("B. Synaptic scaling: all inputs shrink, ratios survive", fontsize=9.5, loc="left")
    fig.tight_layout(); fig.savefig(OUT / "fig_homeostasis.png", dpi=200); plt.close(fig)


def fig_engram():
    """Figure 5.5: a memory as a sparse ensemble that can be reactivated from a partial cue."""
    rng = np.random.default_rng(7); n = 60; pos = rng.uniform(0, 10, (n, 2)); eng = rng.choice(n, 9, replace=False)
    fig, axes = plt.subplots(1, 3, figsize=(9, 3.2))
    titles = ["A. Encoding: a sparse set of cells\nstrengthens its mutual connections", "B. Partial cue: three of them fire", "C. Completion: the whole ensemble returns"]
    for k, (ax, t) in enumerate(zip(axes, titles)):
        ax.set_xlim(-0.5, 10.5); ax.set_ylim(-0.5, 10.5); ax.set_aspect("equal"); ax.axis("off"); ax.set_title(t, fontsize=8.5, loc="left")
        for i in range(n):
            for j in range(i + 1, n):
                if np.hypot(*(pos[i] - pos[j])) < 1.6 and rng.random() < 0.5: ax.plot(*zip(pos[i], pos[j]), color="#ccc", lw=0.6, zorder=1)
        for a in eng:
            for b in eng:
                if a < b: ax.plot(*zip(pos[a], pos[b]), color=EXC if k != 1 else "#9bb3c9", lw=1.4 if k == 0 else 1.0, zorder=2)
        active = set(eng) if k != 1 else set(eng[:3])
        for i in range(n):
            on = i in active; ax.add_patch(Circle(pos[i], 0.25, fc=INH if on else "white", ec=INH if (i in eng) else "#999", lw=1.4 if i in eng else 0.8, zorder=3))
    fig.tight_layout(); fig.savefig(OUT / "fig_engram.png", dpi=200); plt.close(fig)


def fig_consolidation():
    """Figure 5.7: two clocks of consolidation and the complementary learning systems."""
    fig = plt.figure(figsize=(9, 3.6)); gs = fig.add_gridspec(1, 2, width_ratios=[1.2, 1])
    ax = fig.add_subplot(gs[0]); ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off"); ax.set_title("A. Two clocks", fontsize=9.5, loc="left")
    ax.add_patch(FancyBboxPatch((0.3, 3.5), 9.4, 2.1, boxstyle="round,pad=0.05", fc="#eef3f8", ec=EXC, lw=1.5)); ax.text(0.5, 5.3, "Synaptic consolidation (minutes to hours)", fontsize=9, color=EXC, fontweight="bold")
    ax.text(0.5, 5.0, "early LTP (existing proteins)  ->  gene expression, new protein\n->  late LTP, enlarged spines\nlabile for about an hour; blocked by protein-synthesis inhibitors", fontsize=7.5, color=GRAY, va="top", linespacing=1.4)
    ax.add_patch(FancyBboxPatch((0.3, 0.2), 9.4, 2.9, boxstyle="round,pad=0.05", fc="#fbf3ee", ec=INH, lw=1.5)); ax.text(0.5, 2.8, "Systems consolidation (weeks to years)", fontsize=9, color=INH, fontweight="bold")
    ax.text(0.5, 2.5, "hippocampus holds the index and replays it (sharp-wave ripples)\neach replay nudges cortical synapses a little\nover weeks to years the cortex can retrieve the memory\nwithout the hippocampus; what remains is the gist,\ninterleaved with what the cortex already knew", fontsize=7.5, color=GRAY, va="top", linespacing=1.4)
    ax2 = fig.add_subplot(gs[1]); ax2.set_xlim(0, 10); ax2.set_ylim(0, 6); ax2.axis("off"); ax2.set_title("B. Complementary learning systems", fontsize=9.5, loc="left")
    ax2.add_patch(FancyBboxPatch((0.4, 3.6), 3.4, 1.7, boxstyle="round,pad=0.05", fc="white", ec=INH, lw=2)); ax2.text(2.1, 4.45, "Hippocampus\nfast, sparse,\none-shot", ha="center", va="center", fontsize=8, color=INH)
    ax2.add_patch(FancyBboxPatch((6.2, 3.6), 3.4, 1.7, boxstyle="round,pad=0.05", fc="white", ec=EXC, lw=2)); ax2.text(7.9, 4.45, "Neocortex\nslow, overlapping,\nstatistical", ha="center", va="center", fontsize=8, color=EXC)
    ax2.add_patch(FancyArrowPatch((3.8, 4.8), (6.2, 4.8), arrowstyle="-|>", mutation_scale=14, lw=1.8, color=INH)); ax2.text(5.0, 5.5, "replay (sleep, quiet rest)", fontsize=7.5, color=INH, ha="center")
    ax2.add_patch(FancyArrowPatch((6.2, 4.0), (3.8, 4.0), arrowstyle="-|>", mutation_scale=14, lw=1.2, color=EXC)); ax2.text(5.0, 3.55, "cues", fontsize=7.5, color=EXC, ha="center")
    ax2.add_patch(FancyArrowPatch((2.1, 1.4), (2.1, 3.6), arrowstyle="-|>", mutation_scale=14, lw=1.8, color=GRAY)); ax2.text(2.1, 0.8, "today's experience", fontsize=8, color=GRAY, ha="center")
    ax2.text(7.9, 1.9, "A fast learner would overwrite\nitself; a slow learner would\nmiss the day. Two systems, two\nrates, and replay to interleave.", fontsize=7.5, color=GRAY, ha="center", va="center")
    fig.tight_layout(); fig.savefig(OUT / "fig_consolidation.png", dpi=200); plt.close(fig)


def fig_forgetting():
    """Figure 5.9: forgetting, and what spaced retrieval does to it."""
    fig, ax = plt.subplots(figsize=(7, 3.3)); t = np.linspace(0, 30, 600)
    ax.plot(t, 100 * np.exp(-t / 6), color=GRAY, lw=2, label="single exposure")
    s = 6; r = np.zeros_like(t); last = 0; strength = 100; cur = 6
    reviews = [1, 4, 10, 20]; y = []; k = 0
    for ti in t:
        if k < len(reviews) and ti >= reviews[k]:
            last = reviews[k]; cur *= 1.9; k += 1
        y.append(100 * np.exp(-(ti - last) / cur))
    ax.plot(t, y, color=EXC, lw=2, label="retrieved at days 1, 4, 10, 20")
    for rv in reviews: ax.axvline(rv, color=EXC, lw=0.8, ls=":")
    ax.set_xlabel("days since learning"); ax.set_ylabel("retention (%)"); ax.set_ylim(0, 105); ax.legend(frameon=False, fontsize=8)
    ax.set_title("Forgetting is fast; each successful retrieval slows the next decay", fontsize=9.5, loc="left")
    fig.tight_layout(); fig.savefig(OUT / "fig_forgetting.png", dpi=200); plt.close(fig)


def fig_systems():
    """Figure 5.10: kinds of memory map onto different circuits and mechanisms."""
    fig, ax = plt.subplots(figsize=(9, 3.4)); ax.set_xlim(0, 12); ax.set_ylim(0, 6); ax.axis("off")
    cols = [("Episodic and semantic\n(facts, events)", "hippocampus,\nmedial temporal lobe,\nthen neocortex", "synaptic change,\nreplay and systems\nconsolidation", INH),
            ("Procedural\n(skills, habits)", "basal ganglia,\ncerebellum,\nmotor cortex", "dopamine-gated\nstriatal plasticity;\nclimbing-fiber LTD", EXC),
            ("Emotional\n(fear, value)", "amygdala", "fast, durable\nLTP; hard to erase,\neasy to suppress", GOLD),
            ("Working\n(the next few seconds)", "prefrontal and\nparietal cortex", "persistent activity\nand short-term synaptic\nfacilitation, not\nstructural change", GREEN)]
    for i, (kind, where, how, c) in enumerate(cols):
        x = 0.3 + i * 2.95
        ax.add_patch(FancyBboxPatch((x, 4.3), 2.7, 1.4, boxstyle="round,pad=0.05", fc="white", ec=c, lw=2)); ax.text(x + 1.35, 5.0, kind, ha="center", va="center", fontsize=8.5, color=c, fontweight="bold")
        ax.text(x + 1.35, 3.1, where, ha="center", va="center", fontsize=8, color=GRAY); ax.text(x + 1.35, 1.2, how, ha="center", va="center", fontsize=7.5, color=GRAY)
    ax.text(-0.1, 3.1, "where", fontsize=8, color=GRAY, rotation=90, va="center"); ax.text(-0.1, 1.2, "how", fontsize=8, color=GRAY, rotation=90, va="center")
    fig.tight_layout(); fig.savefig(OUT / "fig_systems.png", dpi=200); plt.close(fig)


if __name__ == "__main__":
    fig_nmda(); fig_ltp_ltd(); fig_stdp(); fig_homeostasis(); fig_engram(); fig_consolidation(); fig_forgetting(); fig_systems()
    print("done:", sorted(p.name for p in OUT.glob("fig_*.png")))
