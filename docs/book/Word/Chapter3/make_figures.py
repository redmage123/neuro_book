#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 3 (Neuromodulation). Outputs into ./images.
Requires matplotlib and numpy. Rasters and curves are illustrative simulations, not data."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, FancyBboxPatch, Rectangle, Polygon

OUT = Path(__file__).parent / "images"; OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
EXC, INH, GRAY, GOLD, GREEN = "#1f4e79", "#b03a2e", "#555555", "#c9a227", "#2e7d32"
LIGHT = "#f2f2f2"


def arrow(ax, a, b, color=GRAY, lw=1.5, style="-|>", ls="-", shrink=0, cs=None, ms=12):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, color=color, lw=lw, linestyle=ls, mutation_scale=ms,
                                 shrinkA=shrink, shrinkB=shrink, connectionstyle=cs or "arc3,rad=0", zorder=5))


def vesicles(ax, pts, r=0.13, color=GOLD):
    for p in pts:
        ax.add_patch(Circle(p, r, fc="white", ec=color, lw=1.2))
        ax.add_patch(Circle(p, r * 0.45, fc=color, ec="none", alpha=0.7))


# ----------------------------------------------------------------------------------------------
def fig_transmission():
    """Figure 3.1: synaptic (point-to-point) versus volume transmission."""
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.6))
    # --- A synaptic
    ax = axes[0]; ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_aspect("equal"); ax.axis("off")
    ax.text(0.2, 9.6, "A  synaptic transmission", fontsize=11, weight="bold", color=EXC, va="top")
    # presynaptic terminal: axon from the top widening into a bouton
    bouton = [(4.2, 9.0), (5.8, 9.0), (6.1, 7.6), (7.3, 6.4), (7.0, 5.1), (5.0, 4.75), (3.0, 5.1), (2.7, 6.4), (3.9, 7.6)]
    ax.add_patch(Polygon(bouton, closed=True, fc=LIGHT, ec=GRAY, lw=1.4))
    vesicles(ax, [(4.0, 7.2), (4.9, 7.6), (5.9, 7.1), (4.4, 6.3), (5.4, 6.5), (6.3, 6.1), (3.7, 5.7), (5.0, 5.6), (6.0, 5.4)], r=0.26)
    vesicles(ax, [(4.6, 5.05), (5.5, 5.05)], r=0.26)  # docked at the active zone
    ax.text(5.0, 8.4, "presynaptic\nterminal", ha="center", va="center", fontsize=9, color=GRAY)
    ax.text(7.5, 7.4, "vesicles", fontsize=8.5, color=GOLD, ha="left")
    # released transmitter in the cleft
    rng = np.random.default_rng(3)
    for x, y in zip(rng.uniform(3.6, 6.4, 40), rng.uniform(4.3, 4.72, 40)):
        ax.plot(x, y, ".", color=GOLD, ms=3)
    # postsynaptic spine head with receptors
    spine = [(3.0, 4.35), (7.0, 4.35), (7.3, 3.4), (6.0, 2.4), (5.6, 1.0), (4.4, 1.0), (4.0, 2.4), (2.7, 3.4)]
    ax.add_patch(Polygon(spine, closed=True, fc=LIGHT, ec=GRAY, lw=1.4))
    for x in np.linspace(3.9, 6.1, 7):
        ax.add_patch(Rectangle((x - 0.1, 4.2), 0.2, 0.32, fc=INH, ec="none"))
    ax.plot([3.6, 6.4], [4.05, 4.05], color=INH, lw=3, solid_capstyle="round")
    ax.text(5.0, 3.1, "postsynaptic\nspine", ha="center", va="center", fontsize=9, color=GRAY)
    ax.text(7.6, 4.45, "receptors", fontsize=8.5, color=INH, ha="left", va="center")
    ax.text(2.3, 4.55, "cleft\n~20 nm", fontsize=8, color=GRAY, ha="right", va="center")
    ax.text(5.0, 0.35, "one sender, one receiver\nsub-millisecond, local", ha="center", va="center", fontsize=8.5, color=EXC)
    # --- B volume
    ax = axes[1]; ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_aspect("equal"); ax.axis("off")
    ax.text(0.2, 9.6, "B  volume transmission", fontsize=11, weight="bold", color=EXC, va="top")
    # neuromodulatory axon crossing the field with a varicosity
    xs = np.linspace(0.3, 9.7, 200); yc = 6.2 + 0.25 * np.sin(xs * 1.1)
    width = 0.22 + 0.75 * np.exp(-((xs - 5.0) ** 2) / 1.3)
    ax.fill_between(xs, yc - width, yc + width, fc=LIGHT, ec=GRAY, lw=1.4)
    vesicles(ax, [(4.4, 6.5), (5.0, 6.2), (5.6, 6.55), (4.8, 5.75), (5.5, 5.9)], r=0.2)
    ax.text(5.0, 7.75, "varicosity on a\nneuromodulatory axon", ha="center", va="center", fontsize=9, color=GRAY)
    # diffusing transmitter: concentric fading rings and scattered dots
    for r, a in [(0.9, 0.35), (1.6, 0.22), (2.4, 0.13), (3.2, 0.07)]:
        ax.add_patch(Circle((5.0, 5.9), r, fc=GOLD, ec="none", alpha=a))
    rng = np.random.default_rng(7)
    rr = rng.uniform(0.5, 3.3, 90); th = rng.uniform(0, 2 * np.pi, 90)
    ax.plot(5.0 + rr * np.cos(th), 5.9 + rr * np.sin(th), ".", color=GOLD, ms=2.5, alpha=0.8)
    # several targets: dendrites and synapses at various distances, receptors on them
    targets = [((1.3, 3.0), 0.0), ((3.4, 2.1), 0.3), ((6.5, 2.2), -0.3), ((8.6, 3.3), 0.0), ((8.3, 7.9), 0.2), ((1.6, 8.0), -0.2)]
    for (cx, cy), tilt in targets:
        ax.add_patch(Ellipse((cx, cy), 1.6, 0.9, angle=np.degrees(tilt), fc=LIGHT, ec=GRAY, lw=1.2))
        for k in range(3):
            ang = np.pi / 2 + tilt + (k - 1) * 0.5
            px, py = cx + 0.78 * np.cos(ang) * 0.62, cy + 0.45 * np.sin(ang) * 1.0
            ax.add_patch(Rectangle((px - 0.07, py - 0.07), 0.14, 0.14, fc=INH, ec="none"))
    ax.text(1.2, 1.7, "receptors on many\ncells and synapses", ha="center", va="top", fontsize=8.5, color=INH)
    ax.text(5.0, 0.35, "one sender, thousands of receivers\nseconds to minutes, micrometres", ha="center", va="center", fontsize=8.5, color=EXC)
    fig.tight_layout(); fig.savefig(OUT / "fig_transmission.png", dpi=200); plt.close(fig)


# ----------------------------------------------------------------------------------------------
def synapse_pair(ax, x0, y0, modulator_level, label):
    """Draw pre and post elements at (x0,y0) with a neuromodulatory axon above and a cloud of modulator."""
    # modulator cloud
    n = int(8 + 110 * modulator_level); rng = np.random.default_rng(int(10 * modulator_level) + 1)
    if modulator_level > 0.05:
        ax.add_patch(Circle((x0 + 2.0, y0 + 1.1), 1.75, fc=GOLD, ec="none", alpha=0.08 + 0.22 * modulator_level))
    rr = rng.uniform(0, 1.7, n); th = rng.uniform(0, 2 * np.pi, n)
    ax.plot(x0 + 2.0 + rr * np.cos(th), y0 + 1.1 + rr * 0.95 * np.sin(th), ".", color=GOLD, ms=3)
    # neuromodulatory axon above with a varicosity
    xs = np.linspace(x0 - 0.5, x0 + 4.5, 100); yc = np.full_like(xs, y0 + 3.0)
    w = 0.12 + 0.28 * np.exp(-((xs - (x0 + 2.0)) ** 2) / 0.4)
    ax.fill_between(xs, yc - w, yc + w, fc=LIGHT, ec=GRAY, lw=1.1)
    ax.text(x0 + 2.0, y0 + 3.55, "neuromodulatory axon", ha="center", fontsize=8, color=GRAY)
    # pre bouton and post spine
    ax.add_patch(Polygon([(x0 - 0.5, y0 + 1.5), (x0 + 1.2, y0 + 1.5), (x0 + 1.7, y0 + 1.1), (x0 + 1.7, y0 + 0.9), (x0 + 1.2, y0 + 0.5), (x0 - 0.5, y0 + 0.5)],
                         closed=True, fc=LIGHT, ec=GRAY, lw=1.3))
    vesicles(ax, [(x0 + 0.5, y0 + 1.15), (x0 + 1.1, y0 + 0.8), (x0 + 0.6, y0 + 0.7)], r=0.14)
    ax.add_patch(Polygon([(x0 + 4.5, y0 + 1.5), (x0 + 2.8, y0 + 1.5), (x0 + 2.3, y0 + 1.1), (x0 + 2.3, y0 + 0.9), (x0 + 2.8, y0 + 0.5), (x0 + 4.5, y0 + 0.5)],
                         closed=True, fc=LIGHT, ec=GRAY, lw=1.3))
    for yy in (y0 + 0.85, y0 + 1.0, y0 + 1.15):
        ax.add_patch(Rectangle((x0 + 2.25, yy - 0.05), 0.22, 0.1, fc=INH, ec="none"))
    ax.text(x0 + 0.3, y0 + 1.0, "pre", ha="center", va="center", fontsize=9, color=EXC)
    ax.text(x0 + 3.7, y0 + 1.0, "post", ha="center", va="center", fontsize=9, color=EXC)
    ax.text(x0 + 2.0, y0 - 0.75, label, ha="center", va="top", fontsize=9.5, color=GOLD, weight="bold")


def fig_context():
    """Figure 3.2: the same synapse behaves differently under low and high neuromodulator levels."""
    fig = plt.figure(figsize=(9.5, 4.8))
    gs = fig.add_gridspec(2, 2, height_ratios=[2.3, 1.0], hspace=0.05, wspace=0.12)
    for col, (level, label, gain, title) in enumerate([(0.05, "low modulator", 1.0, "same input"), (0.9, "high modulator", 2.2, "same input")]):
        ax = fig.add_subplot(gs[0, col]); ax.set_xlim(-1, 5); ax.set_ylim(-1.3, 4.1); ax.set_aspect("equal"); ax.axis("off")
        synapse_pair(ax, 0, 0, level, label)
        ax2 = fig.add_subplot(gs[1, col]); ax2.set_xlim(0, 100); ax2.set_ylim(-0.5, 2.8)
        for s in ("top", "right"): ax2.spines[s].set_visible(False)
        ax2.set_yticks([]); ax2.set_xlabel("time (ms)", fontsize=8.5); ax2.tick_params(labelsize=8)
        t = np.linspace(0, 100, 600); v = np.zeros_like(t)
        for t0 in (10, 30, 50):
            m = t > t0; v[m] += gain * (np.exp(-(t[m] - t0) / 12) - np.exp(-(t[m] - t0) / 2))
        ax2.plot(t, v, color=EXC, lw=1.6)
        for t0 in (10, 30, 50): ax2.plot([t0, t0], [-0.45, -0.15], color=GRAY, lw=1.2)
        ax2.text(60, -0.3, "presynaptic spikes", fontsize=7.5, color=GRAY, va="center")
        ax2.text(62, 1.9, f"postsynaptic response ×{gain:.1f}" if gain > 1 else "postsynaptic response", fontsize=8, color=EXC)
        if col == 1:
            ax2.text(2, 2.6, "larger response, and the synapse\nis now permitted to change", fontsize=8, color=GOLD, ha="left", va="top")
    fig.savefig(OUT / "fig_context.png", dpi=200, bbox_inches="tight"); plt.close(fig)


# ----------------------------------------------------------------------------------------------
def brain_outline(ax):
    """Schematic midsagittal brain: front at left. Returns nothing; draws cerebrum, cerebellum, brainstem."""
    # brainstem (drawn first, behind)
    ax.add_patch(Polygon([(5.5, 3.0), (6.7, 3.0), (6.9, 1.9), (6.6, 0.3), (5.9, 0.3), (5.5, 1.9)], closed=True, fc="#e9e9e9", ec=GRAY, lw=1.3))
    # cerebrum: smooth blob
    th = np.linspace(0, 2 * np.pi, 400)
    x = 5.0 + 4.6 * np.cos(th); y = 4.4 + 2.5 * np.sin(th) * (1 - 0.18 * np.cos(th)) + 0.25 * np.cos(th)  # rounder front, lower back
    ax.fill(x, y, fc=LIGHT, ec=GRAY, lw=1.4, zorder=2)
    # cerebellum
    ax.add_patch(Ellipse((8.0, 1.7), 2.6, 1.6, angle=15, fc="#e4e4e4", ec=GRAY, lw=1.3, zorder=3))
    # corpus callosum arc for orientation
    tc = np.linspace(np.pi * 0.08, np.pi * 0.92, 100)
    ax.plot(5.0 + 2.2 * np.cos(tc), 4.6 + 1.0 * np.sin(tc), color="#bbbbbb", lw=3, zorder=3)
    ax.text(0.5, 7.2, "front", fontsize=8.5, color=GRAY, style="italic"); ax.text(9.6, 7.2, "back", fontsize=8.5, color=GRAY, style="italic", ha="right")


def nucleus(ax, p, color, size=90):
    ax.scatter([p[0]], [p[1]], s=size, color=color, zorder=6, edgecolors="white", linewidths=1.0)


def fig_systems():
    """Figure 3.3: the four major neuromodulatory systems on a schematic midsagittal brain."""
    fig, ax = plt.subplots(figsize=(9.5, 6.4)); ax.set_xlim(-0.2, 11.2); ax.set_ylim(-0.3, 7.6); ax.set_aspect("equal"); ax.axis("off")
    brain_outline(ax)
    colors = {"dopamine": INH, "norepinephrine": EXC, "serotonin": GREEN, "acetylcholine": GOLD}
    # targets (approximate positions in the schematic)
    cortex = [(1.8, 5.6), (3.4, 6.5), (5.2, 6.8), (7.0, 6.4), (8.6, 5.3)]
    striatum, prefrontal, hippo, thal = (4.0, 4.1), (1.4, 4.4), (7.2, 3.3), (5.6, 4.1)
    # dopamine: VTA and SNc
    vta, snc = (5.95, 1.9), (6.4, 2.0)
    for s in (vta, snc): nucleus(ax, s, colors["dopamine"])
    arrow(ax, vta, striatum, colors["dopamine"], cs="arc3,rad=0.25"); arrow(ax, vta, prefrontal, colors["dopamine"], cs="arc3,rad=0.35")
    arrow(ax, snc, (4.4, 4.5), colors["dopamine"], cs="arc3,rad=0.15")
    # norepinephrine: locus coeruleus to whole cortex, hippocampus, cerebellum
    lc = (6.9, 1.25); nucleus(ax, lc, colors["norepinephrine"])
    for tgt, rad in [(cortex[0], 0.45), (cortex[2], 0.35), (cortex[4], 0.2), (hippo, 0.1), ((8.3, 1.8), -0.3)]:
        arrow(ax, lc, tgt, colors["norepinephrine"], cs=f"arc3,rad={rad}", lw=1.3)
    # serotonin: raphe nuclei to cortex and hippocampus
    raphe = (6.15, 0.95); nucleus(ax, raphe, colors["serotonin"])
    for tgt, rad in [(cortex[1], 0.5), (cortex[3], 0.15), (hippo, 0.3), (striatum, 0.2)]:
        arrow(ax, raphe, tgt, colors["serotonin"], cs=f"arc3,rad={rad}", lw=1.3)
    # acetylcholine: basal forebrain to cortex and hippocampus; PPN/LDT to thalamus
    bf, ppn = (3.6, 3.1), (6.8, 1.65)
    for s in (bf, ppn): nucleus(ax, s, colors["acetylcholine"])
    for tgt, rad in [(cortex[0], -0.3), (cortex[1], -0.25), (cortex[2], -0.2), (hippo, 0.2)]:
        arrow(ax, bf, tgt, colors["acetylcholine"], cs=f"arc3,rad={rad}", lw=1.3)
    arrow(ax, ppn, thal, colors["acetylcholine"], cs="arc3,rad=-0.2", lw=1.3)
    # labels for nuclei (leader lines kept short)
    lab = [("VTA, substantia nigra\n(dopamine)", vta, (4.1, 1.45), INH), ("locus coeruleus\n(norepinephrine)", lc, (7.9, -0.05), EXC),
           ("raphe nuclei\n(serotonin)", raphe, (3.6, 0.25), GREEN), ("basal forebrain\n(acetylcholine)", bf, (1.3, 2.3), GOLD),
           ("pedunculopontine nucleus\n(acetylcholine)", ppn, (9.7, 0.85), GOLD)]
    for text, p, q, c in lab:
        ax.annotate(text, xy=p, xytext=q, fontsize=8, color=c, ha="center", va="center",
                    arrowprops=dict(arrowstyle="-", color=c, lw=0.8, shrinkB=5), zorder=7)
    for name, p in [("striatum", striatum), ("thalamus", thal), ("hippocampus", hippo), ("prefrontal\ncortex", prefrontal)]:
        ax.text(p[0], p[1] + 0.22, name, fontsize=7.5, color=GRAY, ha="center", va="bottom", zorder=7)
    ax.text(5.0, 7.45, "cortex", fontsize=8.5, color=GRAY, ha="center")
    # legend
    for k, (name, c) in enumerate(colors.items()):
        ax.plot([0.2, 0.7], [0.75 - k * 0.3] * 2, color=c, lw=2.2); ax.text(0.85, 0.75 - k * 0.3, name, fontsize=8.5, color=c, va="center")
    fig.tight_layout(); fig.savefig(OUT / "fig_systems.png", dpi=200); plt.close(fig)


def fig_cholinergic():
    """Figure 3.4: the cholinergic system alone."""
    fig, ax = plt.subplots(figsize=(9.5, 6.0)); ax.set_xlim(-0.2, 10.6); ax.set_ylim(-0.3, 7.6); ax.set_aspect("equal"); ax.axis("off")
    brain_outline(ax)
    cortex = [(1.5, 5.3), (2.6, 6.3), (4.0, 6.75), (5.4, 6.8), (6.8, 6.5), (8.2, 5.7)]
    hippo, thal = (6.9, 3.6), (5.6, 4.1)
    septum, nbm, ppn = (3.3, 3.5), (4.2, 2.9), (6.6, 2.0)
    for s in (septum, nbm, ppn): nucleus(ax, s, GOLD, 110)
    for tgt, rad in [(cortex[0], -0.35), (cortex[1], -0.3), (cortex[2], -0.25), (cortex[3], -0.2), (cortex[4], -0.15), (cortex[5], -0.1)]:
        arrow(ax, nbm, tgt, GOLD, cs=f"arc3,rad={rad}", lw=1.4)
    arrow(ax, septum, hippo, GOLD, cs="arc3,rad=0.35", lw=1.4)
    arrow(ax, ppn, thal, GOLD, cs="arc3,rad=-0.25", lw=1.4)
    ax.scatter([hippo[0]], [hippo[1]], s=60, color=GRAY, zorder=5); ax.scatter([thal[0]], [thal[1]], s=60, color=GRAY, zorder=5)
    ax.text(hippo[0] + 0.25, hippo[1] - 0.05, "hippocampus", fontsize=8.5, color=GRAY, va="top")
    ax.text(thal[0] - 0.25, thal[1] + 0.15, "thalamus", fontsize=8.5, color=GRAY, ha="right")
    ax.text(5.0, 7.45, "neocortex", fontsize=9, color=GRAY, ha="center")
    ax.annotate("nucleus basalis of Meynert\n(basal forebrain): to all of neocortex", xy=nbm, xytext=(2.6, 1.0), fontsize=8.5, color=GOLD, ha="center",
                arrowprops=dict(arrowstyle="-", color=GOLD, lw=0.8, shrinkB=6))
    ax.annotate("medial septum:\nto hippocampus", xy=septum, xytext=(1.2, 3.9), fontsize=8.5, color=GOLD, ha="center",
                arrowprops=dict(arrowstyle="-", color=GOLD, lw=0.8, shrinkB=6))
    ax.annotate("pedunculopontine and laterodorsal\ntegmental nuclei (brainstem): to thalamus", xy=ppn, xytext=(8.2, -0.05), fontsize=8.5, color=GOLD, ha="center",
                arrowprops=dict(arrowstyle="-", color=GOLD, lw=0.8, shrinkB=6))
    ax.text(0.1, 0.1, "a few thousand cells reach the whole cortex", fontsize=8.5, color=EXC, style="italic")
    fig.tight_layout(); fig.savefig(OUT / "fig_cholinergic.png", dpi=200); plt.close(fig)


# ----------------------------------------------------------------------------------------------
def fig_rpe():
    """Figure 3.5: simulated dopamine-neuron rasters and histograms in the three Schultz conditions."""
    rng = np.random.default_rng(42)
    t0, t1, dt = -0.5, 1.8, 0.001; t = np.arange(t0, t1, dt)
    cue, rew = 0.0, 1.0
    base = 5.0

    def rate(cond):
        r = np.full_like(t, base)
        burst = lambda c: 45.0 * np.exp(-((t - (c + 0.09)) ** 2) / (2 * 0.04 ** 2))
        if cond == 0: r += burst(rew)
        if cond == 1: r += burst(cue)
        if cond == 2:
            r += burst(cue); r = np.where((t > rew + 0.05) & (t < rew + 0.35), 0.3, r)
        return r
    titles = ["A  unpredicted reward", "B  predicted reward (after learning)", "C  predicted reward omitted"]
    fig, axes = plt.subplots(2, 3, figsize=(9.5, 4.6), gridspec_kw=dict(height_ratios=[1.6, 1.0]), sharex=True)
    ntr = 14
    for c in range(3):
        r = rate(c); axr, axh = axes[0, c], axes[1, c]
        spikes = []
        for k in range(ntr):
            s = t[rng.random(len(t)) < r * dt]; spikes.append(s)
            axr.vlines(s, k + 0.1, k + 0.9, color=EXC, lw=0.8)
        axr.set_ylim(0, ntr); axr.set_yticks([]); axr.set_title(titles[c], fontsize=9.5, loc="left", color=EXC, weight="bold", pad=16)
        if c == 0: axr.set_ylabel("trials", fontsize=9)
        bins = np.arange(t0, t1 + 0.05, 0.05); allsp = np.concatenate(spikes)
        h, _ = np.histogram(allsp, bins); axh.bar(bins[:-1], h / ntr / 0.05, width=0.05, align="edge", color=EXC, alpha=0.85)
        axh.axhline(base, color=GRAY, lw=0.7, ls=":")
        axh.set_ylim(0, 50); axh.set_xlim(t0, t1); axh.tick_params(labelsize=8)
        if c == 0: axh.set_ylabel("spikes / s", fontsize=9)
        axh.set_xlabel("time (s)", fontsize=9)
        for ax in (axr, axh):
            for s in ("top", "right"): ax.spines[s].set_visible(False)
            if c != 0: ax.axvline(cue, color=GOLD, lw=1.2, ls="--")
            ax.axvline(rew, color=GREEN if c != 2 else INH, lw=1.2, ls="--")
        axr.text(cue, ntr + 0.3, "cue" if c else "", color=GOLD, fontsize=8, ha="center")
        axr.text(rew, ntr + 0.3, "reward" if c != 2 else "no reward", color=GREEN if c != 2 else INH, fontsize=8, ha="center")
    fig.tight_layout(); fig.savefig(OUT / "fig_rpe.png", dpi=200); plt.close(fig)


def fig_td():
    """Figure 3.6: temporal-difference learning moves the prediction error from the reward to the cue."""
    T, cue_t, rew_t, alpha, gamma, ntrials = 12, 2, 8, 0.15, 1.0, 150
    V = np.zeros(T + 1); d_cue, d_rew, profiles = [], [], {}
    for trial in range(1, ntrials + 1):
        delta = np.zeros(T)
        for s in range(T):
            r = 1.0 if s == rew_t else 0.0
            nxt = V[s + 1] if (s + 1 >= cue_t) else 0.0
            cur = V[s] if s >= cue_t else 0.0
            delta[s] = r + gamma * nxt - cur
            if s >= cue_t: V[s] += alpha * delta[s]
        d_cue.append(delta[cue_t - 1]); d_rew.append(delta[rew_t])
        if trial in (1, 10, 40, 150): profiles[trial] = delta.copy()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 3.6), gridspec_kw=dict(width_ratios=[1.1, 1.0]))
    offs = {1: 3.75, 10: 2.5, 40: 1.25, 150: 0.0}
    for tr, prof in profiles.items():
        ax1.step(np.arange(T), prof + offs[tr], where="mid", color=EXC, lw=1.5)
        ax1.axhline(offs[tr], color="#cccccc", lw=0.6)
        ax1.text(-0.4, offs[tr] + 0.5, f"trial {tr}", fontsize=8.5, color=GRAY, ha="right", va="center")
    ax1.axvline(cue_t - 1, color=GOLD, lw=1.2, ls="--"); ax1.axvline(rew_t, color=GREEN, lw=1.2, ls="--")
    ax1.text(cue_t - 1, 4.95, "cue", color=GOLD, fontsize=8.5, ha="center"); ax1.text(rew_t, 4.95, "reward", color=GREEN, fontsize=8.5, ha="center")
    ax1.set_xlim(-1.8, T - 0.5); ax1.set_ylim(-0.3, 5.15); ax1.set_yticks([]); ax1.set_xlabel("time step within a trial", fontsize=9)
    ax1.set_title("A  prediction error δ within a trial", fontsize=9.5, loc="left", color=EXC, weight="bold")
    for s in ("top", "right", "left"): ax1.spines[s].set_visible(False)
    ax1.tick_params(labelsize=8)
    tr = np.arange(1, ntrials + 1)
    ax2.plot(tr, d_rew, color=GREEN, lw=1.8, label="δ at reward"); ax2.plot(tr, d_cue, color=GOLD, lw=1.8, label="δ at cue")
    ax2.set_xlabel("trial", fontsize=9); ax2.set_ylabel("prediction error δ", fontsize=9); ax2.set_ylim(-0.05, 1.05)
    ax2.legend(fontsize=8.5, frameon=False, loc="center right"); ax2.tick_params(labelsize=8)
    ax2.set_title("B  the signal migrates to the cue", fontsize=9.5, loc="left", color=EXC, weight="bold")
    for s in ("top", "right"): ax2.spines[s].set_visible(False)
    fig.tight_layout(); fig.savefig(OUT / "fig_td.png", dpi=200); plt.close(fig)
    return d_cue, d_rew


# ----------------------------------------------------------------------------------------------
def fig_eligibility():
    """Figure 3.7: an eligibility trace bridges the gap between a spike pair and a delayed dopamine pulse."""
    t = np.linspace(0, 8, 4000); tau = 1.5; t_pair = 1.0
    e = np.where(t >= t_pair, np.exp(-(t - t_pair) / tau), 0.0)
    fig, axes = plt.subplots(4, 2, figsize=(9.5, 5.2), sharex=True, gridspec_kw=dict(height_ratios=[0.7, 1, 0.8, 1]))
    for col, (t_da, title) in enumerate([(2.5, "A  dopamine arrives while the trace persists"), (6.5, "B  dopamine arrives after the trace has decayed")]):
        da = np.exp(-((t - t_da) ** 2) / (2 * 0.08 ** 2))
        w = 1.0 + 0.6 * np.cumsum(e * da) * (t[1] - t[0]) / 0.2
        w = 1.0 + 0.6 * (np.cumsum(e * da) / np.cumsum(e * da)[-1]) * (e[np.argmin(abs(t - t_da))] / 1.0)
        a0, a1, a2, a3 = axes[:, col]
        a0.vlines([t_pair], 0.1, 0.9, color=EXC, lw=2); a0.vlines([t_pair + 0.08], 0.1, 0.9, color=INH, lw=2)
        a0.text(t_pair + 0.25, 0.5, "pre spike, then post spike", fontsize=8, va="center", color=GRAY)
        a0.set_ylim(0, 1); a0.set_yticks([]); a0.set_ylabel("spikes", fontsize=8)
        a0.set_title(title, fontsize=9.5, loc="left", color=EXC, weight="bold")
        a1.plot(t, e, color=GOLD, lw=1.8); a1.fill_between(t, 0, e, color=GOLD, alpha=0.15)
        a1.set_ylim(0, 1.15); a1.set_yticks([]); a1.set_ylabel("eligibility\ntrace e(t)", fontsize=8)
        a1.text(t_pair + tau + 0.3, 0.55, "decays over seconds", fontsize=8, color=GOLD)
        a2.plot(t, da, color=GREEN, lw=1.8); a2.set_ylim(0, 1.3); a2.set_yticks([]); a2.set_ylabel("dopamine\nδ(t)", fontsize=8)
        a2.text(t_da + 0.2, 0.75, "pulse", fontsize=8, color=GREEN)
        a3.plot(t, w, color=EXC, lw=1.8); a3.set_ylim(0.9, 1.75); a3.set_yticks([1.0, 1.5]); a3.set_ylabel("synaptic\nweight w", fontsize=8)
        a3.tick_params(labelsize=8); a3.set_xlabel("time (s)", fontsize=9)
        a3.text(t_da + 0.2, 1.38 if col == 0 else 1.12, "weight increases" if col == 0 else "no change", fontsize=8.5, color=EXC)
        for a in (a0, a1, a2, a3):
            for s in ("top", "right"): a.spines[s].set_visible(False)
            a.axvline(t_da, color=GREEN, lw=0.8, ls=":")
    fig.tight_layout(); fig.savefig(OUT / "fig_eligibility.png", dpi=200); plt.close(fig)


def fig_math():
    """Figure 3.8: the three-factor rule written out, with the curves it produces."""
    fig = plt.figure(figsize=(9.5, 4.4))
    gs = fig.add_gridspec(2, 3, height_ratios=[0.85, 1.0], hspace=0.55, wspace=0.35)
    ax = fig.add_subplot(gs[0, :]); ax.axis("off")
    ax.text(0.0, 0.95, "A three-factor learning rule", fontsize=10.5, color=EXC, weight="bold", va="top")
    ax.text(0.02, 0.58, r"$\dfrac{de}{dt} = -\dfrac{e}{\tau_e} + \mathrm{STDP}(\Delta t)\;\delta(t - t_{\mathrm{pair}})$", fontsize=13, va="center")
    ax.text(0.55, 0.58, r"$\dfrac{dw}{dt} = \eta\; e(t)\; \delta_{\mathrm{DA}}(t)$", fontsize=13, va="center")
    ax.text(0.02, 0.12, "eligibility e rises when pre and post spikes pair (factors 1 and 2), decays with time constant τ;\n"
                        "the weight w changes only while both e and the dopamine signal δ (factor 3) are present.",
            fontsize=8.5, color=GRAY, va="center")
    # STDP window
    a = fig.add_subplot(gs[1, 0]); dt = np.linspace(-80, 80, 400)
    stdp = np.where(dt > 0, np.exp(-dt / 20), -0.6 * np.exp(dt / 20))
    a.plot(dt, stdp, color=EXC, lw=1.6); a.axhline(0, color=GRAY, lw=0.6); a.axvline(0, color=GRAY, lw=0.6)
    a.set_xlabel("Δt = t$_{post}$ − t$_{pre}$ (ms)", fontsize=8.5); a.set_ylabel("STDP(Δt)", fontsize=8.5); a.tick_params(labelsize=7.5)
    a.set_title("B  pairing sets the sign and size", fontsize=9, loc="left", color=EXC, weight="bold")
    # e and delta
    b = fig.add_subplot(gs[1, 1]); t = np.linspace(0, 8, 2000)
    e = np.where(t >= 1, np.exp(-(t - 1) / 1.5), 0); d = np.exp(-((t - 3.0) ** 2) / (2 * 0.1 ** 2))
    b.plot(t, e, color=GOLD, lw=1.6, label="e(t)"); b.plot(t, d, color=GREEN, lw=1.6, label="δ$_{DA}$(t)")
    b.legend(fontsize=8, frameon=False); b.set_xlabel("time (s)", fontsize=8.5); b.tick_params(labelsize=7.5); b.set_yticks([])
    b.set_title("C  trace and dopamine overlap", fontsize=9, loc="left", color=EXC, weight="bold")
    # w
    c = fig.add_subplot(gs[1, 2]); w = 1 + 0.5 * np.cumsum(e * d) / np.sum(e * d)
    c.plot(t, w, color=EXC, lw=1.6); c.set_xlabel("time (s)", fontsize=8.5); c.set_ylabel("w", fontsize=8.5); c.tick_params(labelsize=7.5)
    c.set_ylim(0.9, 1.6); c.set_title("D  the product drives the change", fontsize=9, loc="left", color=EXC, weight="bold")
    for ax_ in (a, b, c):
        for s in ("top", "right"): ax_.spines[s].set_visible(False)
    fig.savefig(OUT / "fig_math.png", dpi=200, bbox_inches="tight"); plt.close(fig)


# ----------------------------------------------------------------------------------------------
def fig_dbs():
    """Figure 3.9: deep brain stimulation hardware in place, head and upper torso in profile."""
    fig, ax = plt.subplots(figsize=(6.5, 7.2)); ax.set_xlim(0, 9); ax.set_ylim(0, 10); ax.set_aspect("equal"); ax.axis("off")
    # torso and neck (facing right)
    ax.add_patch(Polygon([(1.0, 0.0), (1.0, 2.4), (1.6, 3.1), (3.5, 3.6), (4.1, 3.9), (4.3, 4.6), (5.6, 4.7), (5.6, 3.6), (6.6, 3.1), (7.2, 2.4), (7.2, 0.0)],
                         closed=True, fc="#f7f7f7", ec=GRAY, lw=1.3))
    # head profile
    head = [(4.3, 4.6), (4.0, 5.4), (3.6, 6.3), (3.6, 7.6), (4.1, 8.7), (5.0, 9.4), (6.0, 9.5), (6.9, 9.0), (7.3, 8.0), (7.3, 7.0), (7.1, 6.5),
            (7.0, 6.2), (7.35, 6.0), (7.1, 5.7), (7.0, 5.4), (6.6, 5.1), (6.4, 4.8), (5.6, 4.7)]
    ax.add_patch(Polygon(head, closed=True, fc="#f7f7f7", ec=GRAY, lw=1.3))
    ax.add_patch(Ellipse((5.2, 5.9), 0.45, 0.7, fc="none", ec=GRAY, lw=0.8))  # ear
    # brain
    ax.add_patch(Ellipse((5.45, 7.85), 3.0, 2.3, fc=LIGHT, ec=GRAY, lw=1.0, ls="--"))
    tgt = (5.3, 7.35)
    ax.scatter([tgt[0]], [tgt[1]], s=70, color=INH, zorder=6)
    # lead: enters at the top of the skull, straight to target
    ax.plot([5.3, 5.3], [9.48, tgt[1]], color=EXC, lw=2.2, zorder=5)
    ax.add_patch(Rectangle((5.05, 9.4), 0.5, 0.2, fc=EXC, ec="none", zorder=6))  # burr-hole cap
    # extension: over the skull, behind the ear, down the neck to the chest
    ext = np.array([(5.3, 9.5), (4.6, 9.3), (4.0, 8.6), (3.75, 7.6), (3.9, 6.6), (4.2, 5.6), (4.35, 4.7), (4.0, 3.9), (3.2, 3.3), (2.7, 2.6), (2.7, 2.0)])
    ax.plot(ext[:, 0], ext[:, 1], color=EXC, lw=1.6, ls=(0, (4, 2)), zorder=5)
    # pulse generator in the chest
    ax.add_patch(FancyBboxPatch((2.1, 0.9), 1.2, 1.1, boxstyle="round,pad=0.08", fc="white", ec=EXC, lw=1.8, zorder=6))
    ax.text(2.7, 1.45, "IPG", ha="center", va="center", fontsize=9, color=EXC, weight="bold", zorder=7)
    # labels
    ax.annotate("burr hole and lead anchor", xy=(5.4, 9.5), xytext=(7.4, 9.6), fontsize=8.5, color=GRAY, va="center",
                arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.8))
    ax.annotate("lead with electrode\ncontacts at the tip", xy=(5.32, 8.3), xytext=(7.6, 8.6), fontsize=8.5, color=EXC, va="center",
                arrowprops=dict(arrowstyle="-", color=EXC, lw=0.8))
    ax.annotate("target: subthalamic nucleus\n(a few millimetres across)", xy=tgt, xytext=(7.6, 7.2), fontsize=8.5, color=INH, va="center",
                arrowprops=dict(arrowstyle="-", color=INH, lw=0.8, shrinkB=5))
    ax.annotate("extension cable\nunder the skin", xy=(3.85, 6.6), xytext=(0.6, 6.6), fontsize=8.5, color=EXC, va="center",
                arrowprops=dict(arrowstyle="-", color=EXC, lw=0.8))
    ax.annotate("implantable pulse generator\nbelow the collarbone", xy=(3.3, 1.45), xytext=(5.2, 1.3), fontsize=8.5, color=EXC, va="center",
                arrowprops=dict(arrowstyle="-", color=EXC, lw=0.8))
    ax.text(6.3, 8.85, "brain", fontsize=8, color=GRAY, ha="center", style="italic")
    fig.tight_layout(); fig.savefig(OUT / "fig_dbs.png", dpi=200); plt.close(fig)


def fig_stimulator():
    """Figure 3.10: block diagram of a neurostimulator system with its pulse train."""
    fig = plt.figure(figsize=(9.5, 4.6))
    ax = fig.add_axes([0.0, 0.0, 0.62, 1.0]); ax.set_xlim(0, 10); ax.set_ylim(0, 7.4); ax.set_aspect("equal"); ax.axis("off")
    # IPG
    ax.add_patch(FancyBboxPatch((0.5, 2.0), 3.6, 3.4, boxstyle="round,pad=0.1", fc="white", ec=EXC, lw=1.8))
    ax.text(2.3, 5.15, "implantable pulse generator", ha="center", fontsize=9, color=EXC, weight="bold")
    for (x, y, w, h, lab) in [(0.8, 3.7, 1.4, 1.0, "battery"), (2.4, 3.7, 1.4, 1.0, "pulse\ncircuitry"), (0.8, 2.3, 1.4, 1.0, "telemetry\nradio"), (2.4, 2.3, 1.4, 1.0, "controller\nand settings")]:
        ax.add_patch(Rectangle((x, y), w, h, fc=LIGHT, ec=GRAY, lw=1.0)); ax.text(x + w / 2, y + h / 2, lab, ha="center", va="center", fontsize=8)
    arrow(ax, (2.2, 4.2), (2.4, 4.2), GRAY, lw=1.0); arrow(ax, (3.1, 3.3), (3.1, 3.7), GRAY, lw=1.0)
    # extension and lead
    ax.plot([4.1, 5.6], [4.2, 4.2], color=EXC, lw=2.5); ax.text(4.85, 4.45, "extension", ha="center", fontsize=8.5, color=EXC)
    ax.add_patch(Rectangle((5.6, 4.05), 0.35, 0.3, fc=GRAY, ec="none")); ax.text(5.78, 3.75, "connector", ha="center", fontsize=7.5, color=GRAY)
    ax.plot([5.95, 8.6], [4.2, 4.2], color=EXC, lw=2.0); ax.text(7.2, 4.45, "lead", ha="center", fontsize=8.5, color=EXC)
    for k in range(4):
        ax.add_patch(Rectangle((8.65 + k * 0.33, 4.08), 0.22, 0.24, fc=INH, ec="none"))
    ax.text(9.3, 3.75, "four contacts\n(1.5 mm each)", ha="center", va="top", fontsize=7.5, color=INH)
    ax.text(9.3, 4.6, "in the target\nnucleus", ha="center", va="bottom", fontsize=7.5, color=GRAY)
    # programmer
    ax.add_patch(FancyBboxPatch((0.5, 0.2), 2.4, 1.0, boxstyle="round,pad=0.08", fc="white", ec=GOLD, lw=1.6))
    ax.text(1.7, 0.7, "clinician programmer\n(external)", ha="center", va="center", fontsize=8, color=GOLD)
    for r in (0.35, 0.6, 0.85):
        th = np.linspace(np.pi * 0.25, np.pi * 0.75, 50); ax.plot(1.5 + r * np.cos(th), 1.2 + r * np.sin(th), color=GOLD, lw=1.0)
    ax.text(2.6, 1.55, "wireless: adjust\namplitude, frequency,\npulse width, contacts", fontsize=7.5, color=GOLD, va="center")
    ax.text(5.0, 6.9, "A  system components", fontsize=10, color=EXC, weight="bold", ha="center")
    # pulse train inset
    bx = fig.add_axes([0.70, 0.22, 0.28, 0.6])
    period = 1000 / 130.0; t = np.arange(0, 32, 0.005); v = np.zeros_like(t)
    for k in range(5):
        on = k * period + 2.0
        v[(t >= on) & (t < on + 0.06 * 8)] = 3.0                 # cathodic phase (width exaggerated 8x to be visible)
        v[(t >= on + 0.5) & (t < on + 0.5 + 0.06 * 8 * 2)] = -1.5  # charge-balancing phase
    bx.plot(t, v, color=EXC, lw=1.2); bx.set_xlim(0, 32); bx.set_ylim(-2.5, 4.2)
    bx.set_xlabel("time (ms)", fontsize=8); bx.set_ylabel("amplitude (V)", fontsize=8); bx.tick_params(labelsize=7.5)
    for s in ("top", "right"): bx.spines[s].set_visible(False)
    bx.annotate("", xy=(2.0, 3.6), xytext=(2.0 + period, 3.6), arrowprops=dict(arrowstyle="<->", color=GRAY, lw=0.8))
    bx.text(2.0 + period / 2, 3.75, "7.7 ms (130 Hz)", fontsize=7.5, ha="center", color=GRAY)
    bx.text(31, -2.2, "pulse width ~60 µs\n(drawn wider to be visible)", fontsize=7, ha="right", va="bottom", color=GRAY)
    bx.set_title("B  typical pulse train", fontsize=10, color=EXC, weight="bold", loc="left")
    fig.savefig(OUT / "fig_stimulator.png", dpi=200); plt.close(fig)


if __name__ == "__main__":
    fig_transmission(); fig_context(); fig_systems(); fig_cholinergic(); fig_rpe()
    dc, dr = fig_td(); print("TD delta at cue (trial 1,10,40,150):", [round(dc[i - 1], 3) for i in (1, 10, 40, 150)])
    print("TD delta at reward (trial 1,10,40,150):", [round(dr[i - 1], 3) for i in (1, 10, 40, 150)])
    fig_eligibility(); fig_math(); fig_dbs(); fig_stimulator()
    print("done")
