#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 2 (Neurons). Outputs into ./images.
Requires matplotlib and numpy. Figure 2.3 (OpenStax, CC BY 4.0) is not drawn here."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, FancyBboxPatch, Rectangle, Polygon, Wedge

OUT = Path(__file__).parent / "images"; OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
EXC, INH, GRAY, GOLD, GREEN = "#1f4e79", "#b03a2e", "#555555", "#c9a227", "#2e7d32"
PALE_EXC, PALE_INH, PALE_GOLD, PALE_GREEN = "#e8eef5", "#fbeeea", "#fbf3dc", "#e6f0e6"


def arrow(ax, a, b, color=GRAY, lw=1.5, style="-|>", ls="-", shrink=0, cs=None, ms=12):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, color=color, lw=lw, linestyle=ls, mutation_scale=ms,
                                 shrinkA=shrink, shrinkB=shrink, connectionstyle=cs or "arc3,rad=0"))


def label(ax, xy, text, xytext, color=GRAY, fs=8, ha="left", va="center"):
    ax.annotate(text, xy=xy, xytext=xytext, fontsize=fs, color=color, ha=ha, va=va,
                arrowprops=dict(arrowstyle="-", color=color, lw=0.7, shrinkA=0, shrinkB=1))


def branch(ax, x, y, ang, length, depth, color=EXC, lw=2.0, rng=None, spread=0.55):
    """Recursive dendritic branch; returns nothing."""
    rng = rng or np.random.default_rng(2)
    x2, y2 = x + length * np.cos(ang), y + length * np.sin(ang)
    ax.plot([x, x2], [y, y2], color=color, lw=lw, solid_capstyle="round")
    if depth > 0:
        for d in (-spread, spread):
            branch(ax, x2, y2, ang + d + rng.uniform(-0.15, 0.15), length * 0.68, depth - 1, color, lw * 0.72, rng, spread)


def psp_kernel(t, t0, tau_r=0.8, tau_d=6.0):
    k = np.where(t >= t0, np.exp(-(t - t0) / tau_d) - np.exp(-(t - t0) / tau_r), 0.0)
    return k / k.max() if k.max() > 0 else k


def spike_wave(t, t0):
    """Stereotyped action potential starting at t0 (ms), in mV relative to rest."""
    s = np.zeros_like(t); m = t >= t0; u = t[m] - t0
    s[m] = 100 * (np.exp(-u / 0.9) - np.exp(-u / 0.25)) * 1.95 - 9 * np.exp(-u / 4.0) * (1 - np.exp(-u / 0.6))
    return s


def fig_cell():
    """Figure 2.1: a neuron is a living cell."""
    fig, ax = plt.subplots(figsize=(9, 4.2)); ax.set_xlim(0, 18); ax.set_ylim(0, 8.4); ax.set_aspect("equal"); ax.axis("off")
    cx, cy = 6.2, 4.3
    ax.add_patch(Ellipse((cx, cy), 9.0, 6.0, fc="#f7f7f7", ec=EXC, lw=2.6))
    ax.add_patch(Ellipse((cx, cy), 8.6, 5.6, fc="none", ec=EXC, lw=1.0))
    ax.text(cx, cy + 2.3, "cytoplasm", ha="center", fontsize=8, color=GRAY, style="italic")
    # nucleus
    ax.add_patch(Ellipse((cx - 1.2, cy + 0.2), 2.6, 2.0, fc=PALE_EXC, ec=EXC, lw=1.4))
    ax.add_patch(Ellipse((cx - 1.5, cy + 0.4), 0.5, 0.4, fc=EXC, ec="none"))
    ax.text(cx - 1.2, cy - 0.3, "nucleus", ha="center", fontsize=8, color=EXC)
    # mitochondria
    for (mx, my, ang) in [(cx + 2.3, cy + 1.2, 20), (cx + 1.6, cy - 1.4, -30)]:
        ax.add_patch(Ellipse((mx, my), 1.6, 0.7, angle=ang, fc=PALE_GREEN, ec=GREEN, lw=1.2))
        for k in range(-2, 3):
            px = mx + 0.28 * k * np.cos(np.radians(ang)); py = my + 0.28 * k * np.sin(np.radians(ang))
            ax.plot([px - 0.12 * np.sin(np.radians(ang)), px + 0.12 * np.sin(np.radians(ang))],
                    [py + 0.12 * np.cos(np.radians(ang)), py - 0.12 * np.cos(np.radians(ang))], color=GREEN, lw=0.8)
    label(ax, (cx + 2.9, cy + 1.5), "mitochondria\n(make ATP)", (cx + 3.3, cy + 2.6), color=GREEN)
    # ribosomes / proteins
    rng = np.random.default_rng(1)
    for _ in range(60):
        a = rng.uniform(0, 2 * np.pi); r = rng.uniform(0.1, 0.92)
        px, py = cx + 4.1 * r * np.cos(a), cy + 2.6 * r * np.sin(a)
        if ((px - (cx - 1.2)) / 1.4) ** 2 + ((py - (cy + 0.2)) / 1.1) ** 2 < 1: continue
        ax.plot(px, py, ".", color="#bbbbbb", ms=3)
    # sodium-potassium pump on the right membrane
    px, py = cx + 4.5, cy - 0.2
    ax.add_patch(FancyBboxPatch((px - 0.3, py - 0.5), 0.6, 1.0, boxstyle="round,pad=0.05", fc=GOLD, ec="#8a6d12", lw=1))
    arrow(ax, (px - 1.1, py + 0.25), (px + 1.0, py + 0.25), color=INH, lw=1.4)   # Na+ out
    arrow(ax, (px + 1.0, py - 0.25), (px - 1.1, py - 0.25), color=EXC, lw=1.4)   # K+ in
    ax.text(px - 1.2, py + 0.5, "3 Na$^+$ out", ha="right", fontsize=7.5, color=INH)
    ax.text(px - 1.2, py - 0.55, "2 K$^+$ in", ha="right", fontsize=7.5, color=EXC)
    ax.text(px, py - 0.95, "ATP → ADP", ha="center", fontsize=7.5, color=GOLD)
    label(ax, (px, py + 0.55), "Na$^+$/K$^+$ pump\n(runs continuously)", (px + 0.3, py + 1.9), color="#8a6d12", ha="center")
    # ion channel on the top-left membrane
    qx, qy = cx - 3.4, cy + 1.95
    ax.add_patch(Rectangle((qx - 0.32, qy - 0.5), 0.22, 1.0, fc=EXC, ec="none")); ax.add_patch(Rectangle((qx + 0.1, qy - 0.5), 0.22, 1.0, fc=EXC, ec="none"))
    arrow(ax, (qx, qy + 0.95), (qx, qy - 0.9), color=INH, lw=1.3)
    label(ax, (qx - 0.35, qy + 0.1), "ion channel\n(gated)", (qx - 1.9, qy - 0.6), color=EXC, ha="center")
    # membrane label
    label(ax, (cx - 0.2, cy - 3.0), "membrane: two lipid layers, 5 nm thick", (cx + 1.4, cy - 3.75), color=EXC)
    # outside / inside text
    ax.text(0.3, 0.6, "outside the cell:\nNa$^+$ high, K$^+$ low", fontsize=8, color=GRAY, va="bottom")
    ax.text(cx - 0.4, cy - 2.2, "inside: K$^+$ high, Na$^+$ low, about −70 mV", fontsize=8, color=GRAY, ha="center")
    # right-hand note
    ax.add_patch(FancyBboxPatch((12.5, 0.7), 5.3, 7.1, boxstyle="round,pad=0.1", fc=PALE_GOLD, ec=GOLD, lw=1.2))
    ax.text(15.15, 7.35, "A cell, not a logic gate", ha="center", fontsize=9.5, color="#8a6d12", weight="bold")
    note = ("• bounded by a membrane that\n   separates two salt solutions\n\n"
            "• burns energy constantly just to\n   keep its ion gradients in place\n\n"
            "• its 'signal' is a change in the\n   voltage across that membrane\n\n"
            "• it grows, repairs itself, ages,\n   and can die\n\n"
            "• what makes it a neuron is\n   excitability: it can fire, send\n   the signal far, and change")
    ax.text(12.75, 6.85, note, fontsize=7.2, color=GRAY, va="top", linespacing=1.25)
    fig.tight_layout(); fig.savefig(OUT / "fig_cell.png", dpi=200); plt.close(fig)


def draw_neuron(ax, sx, sy, s=1.0, myelin=True, nodes=3, color=EXC, lw=2.0, seed=2, dend=True):
    """Draw a polarized neuron with soma at (sx, sy); axon runs to the right. Returns key coordinates."""
    rng = np.random.default_rng(seed)
    if dend:
        for ang in np.radians([150, 120, 95, 185, 215, 245, 60]):
            branch(ax, sx + 0.55 * s * np.cos(ang), sy + 0.5 * s * np.sin(ang), ang, 0.9 * s, 2, color, lw, rng)
    ax.add_patch(Ellipse((sx, sy), 1.5 * s, 1.3 * s, fc=PALE_EXC, ec=color, lw=lw))
    ax.add_patch(Ellipse((sx - 0.1 * s, sy), 0.5 * s, 0.45 * s, fc=color, ec="none", alpha=0.6))
    # hillock + axon
    hx = sx + 0.7 * s
    ax.add_patch(Polygon([(hx - 0.1 * s, sy + 0.32 * s), (hx + 0.9 * s, sy + 0.08 * s), (hx + 0.9 * s, sy - 0.08 * s), (hx - 0.1 * s, sy - 0.32 * s)],
                         closed=True, fc=PALE_EXC, ec=color, lw=lw * 0.8))
    ax_end = hx + 0.9 * s + (4.8 if myelin else 4.2) * s
    ax.plot([hx + 0.85 * s, ax_end], [sy, sy], color=color, lw=lw * 0.9)
    node_xs, seg_c = [], []
    if myelin:
        seg = (ax_end - (hx + 1.1 * s)) / nodes; gap = 0.18 * s
        node_xs = [hx + 1.1 * s + k * seg for k in range(1, nodes)]; seg_c = [hx + 1.1 * s + (k + 0.5) * seg for k in range(nodes)]
        for k in range(nodes):
            x0 = hx + 1.1 * s + k * seg + gap / 2
            ax.add_patch(FancyBboxPatch((x0, sy - 0.22 * s), seg - gap, 0.44 * s, boxstyle="round,pad=0.02", fc="#eeeeee", ec=GRAY, lw=1.0))
    # terminals
    for ang in np.radians([35, 10, -15, -40]):
        x1, y1 = ax_end + 0.9 * s * np.cos(ang), sy + 0.9 * s * np.sin(ang)
        ax.plot([ax_end, x1], [sy, y1], color=color, lw=lw * 0.7)
        ax.add_patch(Circle((x1, y1), 0.12 * s, fc=color, ec="none"))
    return dict(hillock=(hx + 0.4 * s, sy), axon_end=ax_end, soma=(sx, sy), nodes=node_xs, segs=seg_c)


def fig_polarized():
    """Figure 2.2: dendrites, soma, axon hillock, myelinated axon, terminals."""
    fig, ax = plt.subplots(figsize=(9.5, 4.0)); ax.set_xlim(0, 19); ax.set_ylim(0, 8); ax.set_aspect("equal"); ax.axis("off")
    k = draw_neuron(ax, 5.2, 3.6, s=1.5, myelin=True, nodes=3)
    sx, sy = k["soma"]; hx, hy = k["hillock"]; ax_end = k["axon_end"]
    label(ax, (sx - 1.4, sy + 2.4), "dendrites: receive thousands of inputs", (1.2, 7.7), color=EXC)
    label(ax, (sx + 0.55, sy + 0.5), "cell body (soma): integration and metabolism", (6.5, 7.0), color=EXC)
    label(ax, (hx + 0.2, hy - 0.42), "axon hillock and initial segment:\nwhere the spike is decided", (hx - 1.2, 0.9), color=INH)
    label(ax, (k["segs"][0], sy + 0.33), "myelin sheath (insulation)", (k["segs"][0] - 0.4, 6.2), color=GRAY)
    label(ax, (k["nodes"][0], sy - 0.33), "node of Ranvier", (k["nodes"][0] - 0.6, 1.6), color=GRAY)
    label(ax, (ax_end + 1.2, sy + 0.55), "axon terminals: output to other cells", (ax_end - 1.5, 7.2), color=EXC)
    # input arrows into dendrites, output arrow from terminals
    for (x, y) in [(2.0, 5.9), (2.6, 6.6), (1.7, 4.8), (1.8, 2.4), (2.5, 1.5), (3.5, 0.9)]:
        arrow(ax, (x - 0.6, y), (x, y), color=GOLD, lw=1.4, ms=9)
    ax.text(0.2, 3.6, "many\ninputs", fontsize=8.5, color=GOLD, ha="left", weight="bold", va="center")
    arrow(ax, (ax_end + 1.5, sy - 1.3), (ax_end + 2.6, sy - 1.3), color=GOLD, lw=2.0)
    ax.text(ax_end + 2.0, sy - 1.9, "one output", fontsize=8.5, color=GOLD, ha="center", weight="bold")
    ax.text(10.5, 0.25, "Signals travel one way: dendrites → soma → axon → terminals.", ha="center", fontsize=8.5, color=GRAY)
    fig.tight_layout(); fig.savefig(OUT / "fig_polarized.png", dpi=200); plt.close(fig)


def fig_psp():
    """Figure 2.4: EPSP, IPSP, temporal summation to threshold, cancellation."""
    t = np.linspace(0, 40, 4000); rest, thr = -70.0, -55.0
    fig, axes = plt.subplots(2, 2, figsize=(9, 5.2), sharex=True, sharey=True)
    axes = axes.flat
    cases = [("A. One excitatory input (EPSP)", [(5, 4.0)], []),
             ("B. One inhibitory input (IPSP)", [], [(5, -3.0)]),
             ("C. Temporal summation: five EPSPs in quick succession", [(5 + 2.0 * i, 6.0) for i in range(5)], []),
             ("D. Excitation and inhibition together cancel", [(5, 4.0)], [(5.5, -3.5)])]
    checks = {}
    for ax, (title, exc, inh) in zip(axes, cases):
        v = np.full_like(t, rest)
        for (t0, a) in exc: v += a * psp_kernel(t, t0)
        for (t0, a) in inh: v += a * psp_kernel(t, t0, tau_d=9.0)
        spiked = np.where(v >= thr)[0]
        if spiked.size:
            ts = t[spiked[0]]; v = np.where(t < ts, v, rest + spike_wave(t, ts) * 0 + (v[spiked[0]] - rest) * np.exp(-(t - ts) / 3.0)); v += spike_wave(t, ts)
            ax.text(ts + 1.2, 25, "action potential", fontsize=8, color=INH)
        checks[title[0]] = round(float(v.max()), 1)
        ax.plot(t, v, color=EXC, lw=1.8)
        ax.axhline(thr, color=INH, lw=0.9, ls="--"); ax.axhline(rest, color=GRAY, lw=0.6, ls=":")
        for (t0, _) in exc: ax.plot(t0, rest - 4.5, marker="^", color=GOLD, ms=6, clip_on=False)
        for (t0, _) in inh: ax.plot(t0, rest - 4.5, marker="^", color=INH, ms=6, clip_on=False)
        ax.set_title(title, fontsize=9, loc="left")
        for s in ("top", "right"): ax.spines[s].set_visible(False)
    axes[0].set_ylim(-80, 40); axes[0].set_yticks([-70, -55, 0, 30])
    axes[0].text(39, thr + 1.5, "threshold −55 mV", fontsize=7.5, color=INH, ha="right")
    axes[0].text(39, rest - 7.5, "rest −70 mV", fontsize=7.5, color=GRAY, ha="right")
    axes[1].text(39, thr + 1.5, "threshold", fontsize=7.5, color=INH, ha="right")
    axes[0].set_ylabel("membrane potential (mV)", fontsize=9); axes[2].set_ylabel("membrane potential (mV)", fontsize=9)
    axes[2].set_xlabel("time (ms)", fontsize=9); axes[3].set_xlabel("time (ms)", fontsize=9)
    axes[3].text(2, 20, "▲ gold = excitatory input   ▲ red = inhibitory input", fontsize=7.5, color=GRAY)
    fig.tight_layout(); fig.savefig(OUT / "fig_psp.png", dpi=200); plt.close(fig)
    return checks


def fig_ais():
    """Figure 2.5: sodium-channel density peaks at the axon initial segment; graded input becomes a spike there."""
    fig = plt.figure(figsize=(9, 4.4)); gs = fig.add_gridspec(2, 1, height_ratios=[1.0, 1.0], hspace=0.35)
    ax = fig.add_subplot(gs[0]); ax.set_xlim(0, 18); ax.set_ylim(0, 4); ax.set_aspect("equal"); ax.axis("off")
    rng = np.random.default_rng(5)
    sx, sy = 2.6, 2.0
    for ang in np.radians([140, 100, 65, 180]):
        branch(ax, sx + 0.9 * np.cos(ang), sy + 0.85 * np.sin(ang), ang, 0.8, 1, EXC, 1.6, rng)
    ax.add_patch(Ellipse((sx, sy), 2.0, 1.8, fc=PALE_EXC, ec=EXC, lw=1.8))
    ax.add_patch(Polygon([(sx + 0.85, sy + 0.45), (sx + 2.2, sy + 0.16), (sx + 2.2, sy - 0.16), (sx + 0.85, sy - 0.45)], closed=True, fc=PALE_EXC, ec=EXC, lw=1.4))
    ax.add_patch(Rectangle((sx + 2.2, sy - 0.16), 13.0, 0.32, fc=PALE_EXC, ec=EXC, lw=1.4))
    # channel dots: density profile along x
    def density(x):
        if x < sx + 0.9: return 0.25
        if x < sx + 2.2: return 1.4
        if x < sx + 5.2: return 5.0
        return 1.0
    xs = np.arange(sx - 0.9, sx + 15.2, 0.04)
    for x in xs:
        if rng.uniform() < density(x) * 0.09:
            y = sy + rng.uniform(-0.13, 0.13) if x > sx + 0.9 else sy + rng.uniform(-0.8, 0.8)
            if x <= sx + 0.9 and ((x - sx) / 1.0) ** 2 + ((y - sy) / 0.9) ** 2 > 0.85: continue
            ax.plot(x, y, "s", color=INH, ms=2.2)
    ax.plot([sx + 2.2, sx + 5.2], [sy + 0.55, sy + 0.55], color=INH, lw=1.2)
    ax.plot([sx + 2.2, sx + 2.2], [sy + 0.45, sy + 0.65], color=INH, lw=1.2); ax.plot([sx + 5.2, sx + 5.2], [sy + 0.45, sy + 0.65], color=INH, lw=1.2)
    ax.text(sx + 3.7, sy + 0.8, "initial segment: densest Na$^+$ channels,\nlowest threshold", ha="center", fontsize=8, color=INH)
    ax.text(sx, sy - 1.75, "soma: few channels,\nintegrates inputs", ha="center", va="center", fontsize=8, color=EXC)
    ax.text(sx + 10.8, sy + 0.6, "axon: enough channels to regenerate the spike", ha="center", fontsize=8, color=GRAY)
    ax.text(sx + 1.55, sy - 0.75, "hillock", ha="center", fontsize=7.5, color=GRAY)
    ax.text(17.6, sy, "→", fontsize=14, color=GRAY, va="center", ha="center")
    ax.text(17.8, 0.2, "■ = voltage-gated sodium channel (schematic density)", fontsize=7.5, color=INH, va="bottom", ha="right")
    # lower panel: graded soma voltage and AIS spike
    ax2 = fig.add_subplot(gs[1]); t = np.linspace(0, 40, 4000); rest, thr = -70.0, -55.0
    v_soma = rest + sum(5.0 * psp_kernel(t, 5 + 2.0 * i) for i in range(6))
    i0 = np.where(v_soma >= thr)[0]; ts = t[i0[0]]
    v_ais = v_soma.copy(); v_ais = np.where(t < ts, v_ais, rest + (v_soma[i0[0]] - rest) * np.exp(-(t - ts) / 3.0)) + spike_wave(t, ts)
    ax2.plot(t, v_ais, color=INH, lw=1.8, label="initial segment: fires a spike")
    ax2.plot(t, v_soma, color=EXC, lw=1.8, ls="-", label="soma: graded sum of inputs")
    ax2.axhline(thr, color=INH, lw=0.8, ls="--"); ax2.text(39.5, thr + 1.5, "threshold", fontsize=7.5, color=INH, ha="right")
    ax2.axhline(rest, color=GRAY, lw=0.6, ls=":")
    ax2.set_ylim(-80, 40); ax2.set_yticks([-70, -55, 0, 30]); ax2.set_ylabel("mV", fontsize=9); ax2.set_xlabel("time (ms)", fontsize=9)
    ax2.legend(fontsize=7.5, frameon=False, loc="upper right"); ax2.set_title("Graded input becomes a discrete output", fontsize=9, loc="left")
    for s in ("top", "right"): ax2.spines[s].set_visible(False)
    fig.savefig(OUT / "fig_ais.png", dpi=200, bbox_inches="tight"); plt.close(fig)
    return round(float(ts), 2)


def fig_propagation():
    """Figure 2.6: continuous conduction in a bare axon; saltatory conduction in a myelinated axon."""
    fig, (ax, ax2) = plt.subplots(2, 1, figsize=(9, 5.0));
    for a in (ax, ax2): a.set_xlim(0, 18); a.set_ylim(0, 4.6); a.set_aspect("equal"); a.axis("off")
    # panel A
    ax.set_title("A. Unmyelinated axon: the spike is regenerated at every point", fontsize=9, loc="left")
    y0, h = 1.6, 1.0
    ax.add_patch(Rectangle((1, y0), 16, h, fc="#f4f4f4", ec=GRAY, lw=1.4))
    ax.add_patch(Rectangle((1, y0), 5, h, fc=PALE_INH, ec="none")); ax.add_patch(Rectangle((6, y0), 4, h, fc="#9fb4cb", ec="none")); ax.add_patch(Rectangle((10, y0), 7, h, fc="#f4f4f4", ec="none"))
    ax.add_patch(Rectangle((1, y0), 16, h, fc="none", ec=GRAY, lw=1.4))
    ax.text(3.5, y0 + h / 2, "refractory\n(just fired; Na$^+$ channels inactivated)", ha="center", va="center", fontsize=7.5, color=INH)
    ax.text(8, y0 + h / 2, "active\n(Na$^+$ flowing in)", ha="center", va="center", fontsize=7.5, color="white", weight="bold")
    ax.text(13.5, y0 + h / 2 + 0.12, "resting (ahead of the spike)", ha="center", va="center", fontsize=7.5, color=GRAY)
    for x in (7.0, 8.0, 9.0):
        arrow(ax, (x, y0 + h + 0.7), (x, y0 + h + 0.05), color=INH, lw=1.3, ms=9); arrow(ax, (x, y0 - 0.7), (x, y0 - 0.05), color=INH, lw=1.3, ms=9)
    ax.text(8, y0 + h + 0.95, "Na$^+$ enters", ha="center", fontsize=7.5, color=INH)
    # local circuit: current spreads inside to the resting zone and returns outside
    arrow(ax, (9.5, y0 + 0.75), (11.5, y0 + 0.75), color=EXC, lw=1.5, cs="arc3,rad=0.0")
    arrow(ax, (11.8, y0 + h + 0.15), (10.2, y0 + h + 0.15), color=EXC, lw=1.0, ls="--", cs="arc3,rad=0.5")
    ax.text(10.6, y0 - 0.2, "current spreads inside and depolarizes\nthe next patch to threshold", fontsize=7.2, color=EXC, va="top")
    arrow(ax, (12.0, 4.3), (15.0, 4.3), color=GOLD, lw=2); ax.text(13.5, 4.35, "direction of travel", ha="center", va="bottom", fontsize=8, color=GOLD)
    ax.text(1, 0.25, "Nothing moves along the axon except the pattern; each patch uses its own ion gradients to fire.", fontsize=7.8, color=GRAY)
    # panel B
    ax2.set_title("B. Myelinated axon: the spike jumps from node to node (saltatory conduction)", fontsize=9, loc="left")
    y0 = 1.6
    ax2.add_patch(Rectangle((1, y0 + 0.3), 16, 0.4, fc="#f4f4f4", ec=GRAY, lw=1.2))
    nodes = [1.0 + k * 3.2 for k in range(1, 6)]
    for k in range(5):
        x0 = 1.0 + k * 3.2 + 0.2
        ax2.add_patch(FancyBboxPatch((x0, y0 - 0.05), 2.8, 1.1, boxstyle="round,pad=0.03", fc="#e4e4e4", ec=GRAY, lw=1.0))
    for i, x in enumerate(nodes[:-1]):
        ax2.plot([x, x], [y0 + 0.3, y0 + 0.7], color=INH, lw=3)
        if i < 3:
            arrow(ax2, (x + 0.1, y0 + 1.15), (x + 3.1, y0 + 1.15), color=EXC, lw=1.5, cs="arc3,rad=-0.55")
    ax2.text(nodes[0], y0 - 0.35, "node of Ranvier:\nchannels concentrated here", ha="center", va="top", fontsize=7.5, color=INH)
    ax2.text(1.0 + 1.6, y0 + 1.35, "myelin: no channels,\ncurrent cannot leak", ha="center", fontsize=7.5, color=GRAY)
    ax2.text(nodes[2] + 1.6, y0 + 2.35, "current flows inside the sheath to the next node", ha="center", fontsize=7.5, color=EXC)
    ax2.text(1, 0.25, "Fewer regenerations: faster conduction and less energy per spike.", fontsize=7.8, color=GRAY)
    fig.tight_layout(); fig.savefig(OUT / "fig_propagation.png", dpi=200); plt.close(fig)


def fig_timing():
    """Figure 2.7: spikes are all the same size; information is in rate and timing."""
    rng = np.random.default_rng(7); t = np.linspace(0, 200, 8000)
    fig, axes = plt.subplots(3, 1, figsize=(9, 4.6), sharex=True)
    def train(ax, times, color=EXC, lab=None):
        v = np.full_like(t, -70.0)
        for ts in times: v += spike_wave(t, ts)
        ax.plot(t, v, color=color, lw=1.3); ax.set_ylim(-80, 45); ax.set_yticks([-70, 30]); ax.set_yticklabels(["−70", "+30"], fontsize=7.5)
        for s in ("top", "right"): ax.spines[s].set_visible(False)
        if lab: ax.text(201, -20, lab, fontsize=8, color=color, va="center")
    weak = np.sort(rng.uniform(5, 195, 7)); strong = np.sort(rng.uniform(5, 195, 26))
    strong = strong[np.r_[True, np.diff(strong) > 4]]
    train(axes[0], weak, lab="weak stimulus:\n7 spikes in 200 ms")
    train(axes[1], strong, lab=f"strong stimulus:\n{len(strong)} spikes in 200 ms")
    axes[0].set_title("A. Rate: a stronger input gives more spikes, not bigger ones", fontsize=9, loc="left")
    base = np.arange(20, 200, 30); burst = np.concatenate([base[:3], [110, 114, 118], [160, 164, 168]])
    train(axes[2], np.sort(burst), color=INH, lab="same count, different\npattern: bursts")
    axes[2].set_title("B. Timing: the same number of spikes arranged differently carries a different message", fontsize=9, loc="left")
    axes[2].set_xlabel("time (ms)", fontsize=9); axes[1].set_ylabel("membrane potential (mV)", fontsize=9)
    axes[0].set_xlim(0, 200)
    fig.tight_layout(rect=(0, 0, 0.86, 1)); fig.savefig(OUT / "fig_timing.png", dpi=200); plt.close(fig)
    return len(strong), len(weak)


def synapse(ax, x, y, s, n_rec, n_ves, spine_r, color_pre=EXC, color_post=EXC):
    """Presynaptic bouton above a dendritic spine at (x, y)."""
    ax.add_patch(Ellipse((x, y + 1.25 * s), 1.6 * s, 1.3 * s, fc=PALE_EXC, ec=color_pre, lw=1.6))
    ax.plot([x, x], [y + 1.9 * s, y + 3.0 * s], color=color_pre, lw=2.0 * s)
    rng = np.random.default_rng(int(n_ves))
    for _ in range(n_ves):
        vx, vy = x + rng.uniform(-0.5, 0.5) * s, y + rng.uniform(0.95, 1.65) * s
        ax.add_patch(Circle((vx, vy), 0.09 * s, fc="white", ec=color_pre, lw=0.8))
    ax.add_patch(Ellipse((x, y + 0.55 * s), 0.9 * s, 0.1 * s, fc="none", ec="none"))
    # spine: neck + head
    ax.add_patch(Rectangle((x - 0.12 * s, y - 1.2 * s), 0.24 * s, 1.0 * s, fc=PALE_EXC, ec=color_post, lw=1.2))
    ax.add_patch(Circle((x, y + 0.15 * s), spine_r * s, fc=PALE_EXC, ec=color_post, lw=1.6))
    # dendrite shaft
    ax.add_patch(Rectangle((x - 1.6 * s, y - 1.6 * s), 3.2 * s, 0.42 * s, fc=PALE_EXC, ec=color_post, lw=1.6))
    # receptors across the spine head top
    for i in range(n_rec):
        rx = x + (i - (n_rec - 1) / 2) * 0.17 * s
        ry = y + 0.15 * s + np.sqrt(max(spine_r ** 2 - ((rx - x) / s) ** 2, 0)) * s
        ax.add_patch(Rectangle((rx - 0.05 * s, ry - 0.12 * s), 0.1 * s, 0.24 * s, fc=INH, ec="none"))
    return (x, y + 0.6 * s)


def fig_plasticity():
    """Figure 2.8: a synapse before and after strengthening."""
    fig = plt.figure(figsize=(9, 4.4)); gs = fig.add_gridspec(2, 2, height_ratios=[1.6, 1.0], hspace=0.05, wspace=0.15)
    t = np.linspace(0, 40, 2000)
    for col, (title, n_rec, n_ves, r, amp) in enumerate([("Before: a weak synapse", 3, 5, 0.42, 1.0), ("After: the same synapse, strengthened", 7, 11, 0.62, 2.6)]):
        ax = fig.add_subplot(gs[0, col]); ax.set_xlim(-3, 3); ax.set_ylim(-2.2, 3.6); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(title, fontsize=9.5, loc="left")
        synapse(ax, 0, 0, 1.0, n_rec, n_ves, r)
        ax.text(0, 3.3, "presynaptic axon", ha="center", fontsize=7.5, color=EXC)
        ax.text(1.0, 1.3, f"{n_ves} docked\nvesicles\n({'fewer' if col == 0 else 'more'})", fontsize=7.2, color=GRAY, va="center")
        ax.text(1.0, 0.25, f"{n_rec} receptors", fontsize=7.2, color=INH, va="center")
        ax.text(-2.9, -1.4, "dendrite", fontsize=7.5, color=EXC)
        ax.text(-1.05, 0.15, "spine\nhead", fontsize=7.2, color=GRAY, ha="right", va="center")
        ax2 = fig.add_subplot(gs[1, col]); v = -70 + amp * 1.5 * psp_kernel(t, 5)
        ax2.plot(t, v, color=EXC, lw=1.8); ax2.set_ylim(-71, -64); ax2.set_yticks([-70, -66]); ax2.set_xlabel("time (ms)", fontsize=8)
        ax2.text(30, -65.2, f"EPSP {amp * 1.5:.1f} mV", fontsize=8, color=EXC, ha="center")
        for s in ("top", "right"): ax2.spines[s].set_visible(False)
        if col == 0: ax2.set_ylabel("mV", fontsize=8)
    fig.text(0.5, 0.955, "", ha="center")
    ax_mid = fig.add_axes([0.44, 0.55, 0.12, 0.1]); ax_mid.axis("off")
    arrow(ax_mid, (0.0, 0.5), (1.0, 0.5), color=GOLD, lw=2.5, ms=16); ax_mid.set_xlim(0, 1); ax_mid.set_ylim(0, 1)
    fig.text(0.5, 0.67, "repeated, correlated\nactivity", ha="center", fontsize=7.5, color=GOLD)
    fig.savefig(OUT / "fig_plasticity.png", dpi=200, bbox_inches="tight"); plt.close(fig)


def fig_costs():
    """Figure 2.9: slow, noisy, expensive."""
    fig = plt.figure(figsize=(9.5, 3.6)); gs = fig.add_gridspec(1, 3, width_ratios=[1.3, 1.1, 0.8], wspace=0.45)
    # A: timescales
    ax = fig.add_subplot(gs[0]); ax.set_xscale("log"); ax.set_xlim(1e-11, 10)
    items = [("transistor switch (~100 ps)", 1e-10, EXC), ("ion channel opening", 1e-4, GRAY), ("synaptic delay", 5e-4, GOLD),
             ("action potential", 1e-3, INH), ("EPSP", 1e-2, GREEN), ("reaction time", 2.5e-1, GRAY)]
    for i, (name, x, c) in enumerate(items):
        ax.plot([1e-11, x], [i, i], color=c, lw=1.2, alpha=0.5); ax.plot(x, i, "o", color=c, ms=7)
    ax.set_yticks(range(len(items))); ax.set_yticklabels([n for n, _, _ in items], fontsize=7.5); ax.set_ylim(-0.6, len(items) - 0.4)
    ax.set_xticks([1e-10, 1e-7, 1e-4, 1e-1]); ax.tick_params(axis="x", labelsize=7.5)
    ax.set_xlabel("duration (seconds, log scale)", fontsize=8.5); ax.set_title("A. Slow: a spike lasts ten million times\nlonger than a transistor switch", fontsize=9, loc="left")
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    # B: raster
    ax2 = fig.add_subplot(gs[1]); rng = np.random.default_rng(9)
    for trial in range(8):
        base = np.array([22, 31, 39, 48, 60, 74]) + rng.normal(0, 2.2, 6)
        extra = rng.uniform(5, 100, rng.integers(0, 3))
        ts = np.concatenate([base[rng.uniform(size=6) < 0.8], extra])
        ax2.vlines(ts, trial + 0.15, trial + 0.85, color=EXC, lw=1.2)
    ax2.axvspan(20, 80, color=PALE_GOLD, zorder=0); ax2.text(50, 8.3, "identical stimulus", ha="center", fontsize=7.5, color=GOLD)
    ax2.set_xlim(0, 100); ax2.set_ylim(0, 9); ax2.set_yticks([0.5, 7.5]); ax2.set_yticklabels(["trial 1", "trial 8"], fontsize=7.5)
    ax2.set_xlabel("time (ms)", fontsize=8.5); ax2.set_title("B. Noisy: the same input never\ngives exactly the same spikes", fontsize=9, loc="left")
    for s in ("top", "right"): ax2.spines[s].set_visible(False)
    # C: energy
    ax3 = fig.add_subplot(gs[2]); ax3.bar([0, 1], [2, 20], color=[GRAY, INH], width=0.6)
    ax3.set_xticks([0, 1]); ax3.set_xticklabels(["share of\nbody mass", "share of\nresting energy"], fontsize=7.5)
    ax3.set_ylim(0, 25); ax3.set_yticks([0, 10, 20]); ax3.set_ylabel("percent", fontsize=8.5)
    for x, v in [(0, 2), (1, 20)]: ax3.text(x, v + 0.6, f"{v}%", ha="center", fontsize=8, color=GRAY)
    ax3.set_title("C. Expensive: the human\nbrain, about 20 watts", fontsize=9, loc="left")
    for s in ("top", "right"): ax3.spines[s].set_visible(False)
    fig.text(0.5, -0.04, "Slowness and noise are tolerable because the brain computes with populations of cells; "
             "the energy buys signaling elements that can rewire themselves.", ha="center", fontsize=8, color=GRAY)
    fig.savefig(OUT / "fig_costs.png", dpi=200, bbox_inches="tight"); plt.close(fig)


def fig_context():
    """Figure 2.10: the same input gives a different output depending on neuromodulatory context."""
    fig, ax = plt.subplots(figsize=(9, 4.0)); ax.set_xlim(0, 18); ax.set_ylim(0, 8); ax.set_aspect("equal"); ax.axis("off")
    rng = np.random.default_rng(10); t_in = np.sort(rng.uniform(0.2, 4.8, 9))
    def raster(x0, y, times, color, h=0.6):
        ax.plot([x0, x0 + 5.0], [y, y], color="#cccccc", lw=0.8)
        for ts in times: ax.plot([x0 + ts, x0 + ts], [y, y + h], color=color, lw=1.6)
    for row, (y, title, out_times, cloud) in enumerate([
            (5.6, "baseline chemical context", t_in[[1, 4, 7]] + 0.25, False),
            (1.6, "with a neuromodulator present", np.sort(np.concatenate([t_in + 0.2, t_in[[2, 5]] + 0.35])), True)]):
        raster(0.8, y, t_in, GOLD); ax.text(3.3, y + 0.9, "same input spikes", ha="center", fontsize=8, color=GOLD)
        arrow(ax, (6.0, y + 0.3), (7.0, y + 0.3), color=GRAY, lw=1.3)
        if cloud:
            for _ in range(70):
                a = rng.uniform(0, 2 * np.pi); r = rng.uniform(0, 1) ** 0.5
                ax.plot(8.6 + 1.9 * r * np.cos(a), y + 0.3 + 1.5 * r * np.sin(a), ".", color=GOLD, ms=4, alpha=0.6)
            ax.text(8.6, y + 2.0, "e.g. dopamine, acetylcholine, noradrenaline", ha="center", va="bottom", fontsize=7.5, color="#8a6d12")
        ax.add_patch(Circle((8.6, y + 0.3), 0.75, fc=PALE_EXC, ec=EXC, lw=1.8))
        ax.text(8.6, y + 0.3, "neuron", ha="center", va="center", fontsize=8, color=EXC)
        arrow(ax, (10.2, y + 0.3), (11.2, y + 0.3), color=GRAY, lw=1.3)
        raster(11.5, y, out_times, EXC if not cloud else INH)
        ax.text(14.0, y + 0.9, "output", ha="center", fontsize=8, color=EXC if not cloud else INH)
        ax.text(17.2, y + 0.3, f"{len(out_times)} spikes", ha="center", va="center", fontsize=8, color=EXC if not cloud else INH)
        ax.text(0.8, y + 1.55, title, fontsize=9, color=GRAY, weight="bold")
    ax.text(9.0, 0.1, "Same cell, same wiring, same input: a different output because the chemical context changed. Chapter 3 explains how.",
            ha="center", fontsize=8, color=GRAY)
    fig.tight_layout(); fig.savefig(OUT / "fig_context.png", dpi=200); plt.close(fig)


if __name__ == "__main__":
    fig_cell(); fig_polarized(); print("2.4 peaks:", fig_psp()); print("2.5 spike at", fig_ais(), "ms"); fig_propagation()
    print("2.7 spikes strong/weak:", fig_timing()); fig_plasticity(); fig_costs(); fig_context()
    print("done:", sorted(p.name for p in OUT.iterdir()))
