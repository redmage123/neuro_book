#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 0 (Foundations). Outputs into ./images.
Requires matplotlib and numpy."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, FancyBboxPatch, Rectangle, Polygon, Wedge

OUT = Path(__file__).parent / "images"; OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
EXC, INH, GRAY, GOLD, GREEN = "#1f4e79", "#b03a2e", "#555555", "#c9a227", "#2e7d32"


def arrow(ax, a, b, color=GRAY, lw=1.5, style="-|>", ls="-", shrink=0, cs=None, ms=12):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, color=color, lw=lw, linestyle=ls, mutation_scale=ms,
                                 shrinkA=shrink, shrinkB=shrink, connectionstyle=cs or "arc3,rad=0"))


def fig_cell_energy_entropy():
    """Figure 0.2: a cell keeps its own entropy low by taking in free energy and exporting entropy."""
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9, 3.6), gridspec_kw={"width_ratios": [2.1, 1]})
    ax.set_xlim(0, 12); ax.set_ylim(0, 6); ax.set_aspect("equal"); ax.axis("off")
    # the cell
    ax.add_patch(Ellipse((6, 3), 6.2, 4.4, fc="#eef3f8", ec=EXC, lw=2))
    ax.text(6, 4.6, "the cell", ha="center", fontsize=10, color=EXC, fontweight="bold")
    ax.text(6, 3.85, "order maintained:", ha="center", fontsize=8.5, color=GRAY)
    ax.text(6, 3.45, "ion gradients, folded proteins,\nintact membranes", ha="center", va="top", fontsize=8.5, color=GRAY)
    ax.add_patch(FancyBboxPatch((4.3, 1.75), 3.4, 0.75, boxstyle="round,pad=0.08", fc="white", ec=GOLD, lw=1.4))
    ax.text(6, 2.12, "ATP + H$_2$O $\\rightarrow$ ADP + P$_i$", ha="center", va="center", fontsize=9, color=GOLD)
    ax.text(6, 1.2, "free energy spent on work", ha="center", fontsize=8, color=GOLD)
    # inputs: food and oxygen (low entropy, high free energy)
    arrow(ax, (0.3, 3.4), (2.8, 3.4), color=GREEN, lw=2.2, ms=16)
    ax.text(1.55, 3.95, "glucose, oxygen", ha="center", fontsize=9, color=GREEN)
    ax.text(1.55, 2.95, "low entropy,\nhigh free energy", ha="center", va="top", fontsize=8, color=GREEN)
    # outputs: heat and waste (high entropy)
    arrow(ax, (9.1, 3.9), (11.6, 4.7), color=INH, lw=2.2, ms=16)
    ax.text(10.5, 5.2, "heat", ha="center", fontsize=9, color=INH)
    arrow(ax, (9.1, 2.5), (11.6, 1.7), color=INH, lw=2.2, ms=16)
    ax.text(10.4, 1.2, "CO$_2$, water, waste", ha="center", va="top", fontsize=9, color=INH)
    ax.text(10.6, 3.2, "high entropy", ha="center", fontsize=8, color=INH)
    ax.text(6, 0.25, "A. Energy in, entropy out", ha="center", fontsize=9.5, color=GRAY)
    # ledger: who gains entropy
    bx.set_xlim(-0.6, 2.6); bx.set_ylim(-1.6, 3.2); bx.axis("off")
    names = ["cell", "surroundings", "universe"]; vals = [0.0, 1.9, 1.9]; cols = [EXC, INH, GRAY]
    for i, (n, v, c) in enumerate(zip(names, vals, cols)):
        bx.add_patch(Rectangle((i - 0.3, 0), 0.6, 0.35, fc="#dddddd", ec="none"))  # starting level
        if v > 0:
            bx.add_patch(Rectangle((i - 0.3, 0.35), 0.6, v, fc=c, ec="none", alpha=0.85))
            bx.text(i, 0.35 + v + 0.12, "rises", ha="center", fontsize=8, color=c)
        else:
            bx.text(i, 0.35 + 0.12, "steady", ha="center", fontsize=8, color=c)
        bx.text(i, -0.22, n, ha="center", va="top", fontsize=8.5, color=GRAY)
    bx.plot([-0.5, 2.5], [0, 0], color=GRAY, lw=0.8)
    bx.text(1.0, 2.95, "entropy change while the cell lives", ha="center", fontsize=8.5, color=GRAY)
    bx.text(1.0, -0.95, "B. The second law is kept:\nthe total still goes up", ha="center", va="top", fontsize=9.5, color=GRAY)
    fig.tight_layout(); fig.savefig(OUT / "fig_cell_energy_entropy.png", dpi=200); plt.close(fig)


def hodgkin_huxley(dt=0.01, t_end=20.0, i_amp=15.0, i_on=4.0, i_off=5.0):
    """Hodgkin and Huxley (1952) squid-axon model, 6.3 degrees C, membrane potential in absolute mV.
    Returns time, V, gNa, gK, and the injected current."""
    gNa_max, gK_max, gL = 120.0, 36.0, 0.3           # mS/cm^2
    ENa, EK, EL, C = 50.0, -77.0, -54.387, 1.0        # mV, uF/cm^2

    def rates(V):
        v = V + 65.0  # depolarization from rest, as in the 1952 paper
        a_m = 0.1 * (25.0 - v) / (np.exp((25.0 - v) / 10.0) - 1.0) if abs(25.0 - v) > 1e-6 else 1.0
        b_m = 4.0 * np.exp(-v / 18.0)
        a_h = 0.07 * np.exp(-v / 20.0)
        b_h = 1.0 / (np.exp((30.0 - v) / 10.0) + 1.0)
        a_n = 0.01 * (10.0 - v) / (np.exp((10.0 - v) / 10.0) - 1.0) if abs(10.0 - v) > 1e-6 else 0.1
        b_n = 0.125 * np.exp(-v / 80.0)
        return a_m, b_m, a_h, b_h, a_n, b_n

    t = np.arange(0.0, t_end, dt)
    V = np.empty_like(t); gNa = np.empty_like(t); gK = np.empty_like(t); I = np.where((t >= i_on) & (t < i_off), i_amp, 0.0)
    v = -65.0; a_m, b_m, a_h, b_h, a_n, b_n = rates(v)
    m, h, n = a_m / (a_m + b_m), a_h / (a_h + b_h), a_n / (a_n + b_n)
    for k, tk in enumerate(t):
        a_m, b_m, a_h, b_h, a_n, b_n = rates(v)
        gna, gk = gNa_max * m ** 3 * h, gK_max * n ** 4
        V[k], gNa[k], gK[k] = v, gna, gk
        dv = (I[k] - gna * (v - ENa) - gk * (v - EK) - gL * (v - EL)) / C
        v += dt * dv
        m += dt * (a_m * (1 - m) - b_m * m); h += dt * (a_h * (1 - h) - b_h * h); n += dt * (a_n * (1 - n) - b_n * n)
    return t, V, gNa, gK, I


def fig_hodgkin_huxley_simulation():
    """Figure 0.7: one action potential from the Hodgkin-Huxley equations, with the two conductances."""
    t, V, gNa, gK, I = hodgkin_huxley()
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(9, 5.2), sharex=True, gridspec_kw={"height_ratios": [1.3, 1]})
    ax.plot(t, V, color=EXC, lw=2)
    ax.axhline(-65, color=GRAY, lw=0.8, ls=":")
    ax.text(19.6, -63.5, "resting potential", ha="right", va="bottom", fontsize=8.5, color=GRAY)
    ax.fill_between(t, -95, -85, where=I > 0, color=GOLD, alpha=0.6)
    ax.text(4.5, -83.5, "stimulus\n(1 ms)", ha="center", va="bottom", fontsize=8, color=GOLD)
    k = int(np.argmax(V)); ax.annotate(f"peak {V[k]:+.0f} mV", (t[k], V[k]), (t[k] + 1.6, V[k] - 4), fontsize=8.5, color=EXC,
                                        arrowprops=dict(arrowstyle="-", color=EXC, lw=0.8))
    ax.annotate("undershoot: potassium\nchannels still open", (t[np.argmin(V[400:])+400], V.min()), (11.3, -55),
                fontsize=8.5, color=INH, arrowprops=dict(arrowstyle="-", color=INH, lw=0.8))
    ax.set_ylim(-95, 50); ax.set_ylabel("membrane potential (mV)")
    ax.text(0.3, 42, "A. Membrane potential", fontsize=9.5, color=GRAY)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    bx.plot(t, gNa, color=EXC, lw=2, label="sodium conductance $g_{Na}$")
    bx.plot(t, gK, color=INH, lw=2, label="potassium conductance $g_K$")
    bx.set_ylabel("conductance (mS/cm$^2$)"); bx.set_xlabel("time (ms)")
    bx.set_xlim(0, 20); bx.set_ylim(0, 40)
    bx.legend(frameon=False, fontsize=9, loc="upper right")
    bx.text(0.3, 36, "B. The two conductances that produce it", fontsize=9.5, color=GRAY)
    bx.annotate("sodium opens first\nand fast", (t[np.argmax(gNa)], gNa.max()), (2.0, 24), fontsize=8.5, color=EXC,
                arrowprops=dict(arrowstyle="-", color=EXC, lw=0.8))
    bx.annotate("potassium opens later\nand closes slowly", (t[np.argmax(gK)] + 1.2, gK[np.argmax(gK) + 120]), (10.5, 20),
                fontsize=8.5, color=INH, arrowprops=dict(arrowstyle="-", color=INH, lw=0.8))
    for s in ("top", "right"): bx.spines[s].set_visible(False)
    fig.tight_layout(); fig.savefig(OUT / "fig_hodgkin_huxley_simulation.png", dpi=200); plt.close(fig)


def fig_axon_guidance_refinement():
    """Figure 0.9: chemical gradients lay down a coarse retinotopic map; correlated activity sharpens it."""
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.9))
    cols = [EXC, "#5b7fa6", GOLD, INH]  # four retinal positions, temporal to nasal
    for ax, sharp in zip(axes, (False, True)):
        ax.set_xlim(-0.3, 12); ax.set_ylim(-0.7, 7); ax.set_aspect("equal"); ax.axis("off")
        # retina: a half disc on the left with four origin cells
        ax.add_patch(Wedge((1.6, 3.5), 1.7, 90, 270, fc="#f4f4f4", ec=GRAY, lw=1.2))
        ax.text(1.0, 6.0, "retina", ha="center", fontsize=9, color=GRAY)
        ax.text(1.05, 1.6, "nasal", ha="center", va="top", fontsize=7.5, color=GRAY)
        ax.text(1.05, 5.3, "temporal", ha="center", va="bottom", fontsize=7.5, color=GRAY)
        ys = [4.7, 3.9, 3.1, 2.3]
        # target: a box with a chemical gradient (ephrin-A rises from anterior to posterior)
        x0, x1, y0, y1 = 6.2, 11.4, 1.6, 5.7
        grad = np.linspace(0, 1, 200)[None, :]
        ax.imshow(grad, extent=(x0, x1, y0, y1), cmap=matplotlib.colors.LinearSegmentedColormap.from_list("g", ["#ffffff", "#d9d2b5"]),
                  aspect="auto", zorder=0)
        frame = Rectangle((x0, y0), x1 - x0, y1 - y0, fc="none", ec=GRAY, lw=1.2, zorder=4); ax.add_patch(frame)
        ax.text((x0 + x1) / 2, 6.1, "target (superior colliculus)", ha="center", fontsize=9, color=GRAY)
        ax.text(x0 + 0.1, 0.55, "anterior", ha="left", va="top", fontsize=7.5, color=GRAY)
        ax.text(x1 - 0.1, 0.55, "posterior", ha="right", va="top", fontsize=7.5, color=GRAY)
        if not sharp:
            arrow(ax, (x0 + 0.4, y0 - 0.3), (x1 - 0.4, y0 - 0.3), color="#8a7d4a", lw=1.2, ms=10)
            ax.text((x0 + x1) / 2, y0 - 0.5, "ephrin-A gradient (repels temporal axons)", ha="center", va="top", fontsize=7.5, color="#8a7d4a")
        # axons: temporal axons stop anterior, nasal axons run posterior
        xs = [7.4, 8.5, 9.6, 10.6]
        for y, x, c in zip(ys, xs, cols):
            ax.add_patch(Circle((2.1, y), 0.17, fc=c, ec="none", zorder=3))
            ax.plot([2.3, 4.2, x], [y, 3.5 + (y - 3.5) * 0.9, 3.5 + (y - 3.5) * 0.9], color=c, lw=1.3, zorder=3)
            yt = 3.5 + (y - 3.5) * 0.9
            if sharp:
                e = Ellipse((x, yt), 0.7, 1.2, fc=c, ec="none", alpha=0.75, zorder=3); ax.add_patch(e); e.set_clip_path(frame)
            else:  # broad, overlapping arbors: the map is only roughly ordered
                e = Ellipse((x, yt), 2.0, 2.4, fc=c, ec="none", alpha=0.28, zorder=3); ax.add_patch(e); e.set_clip_path(frame)
        if sharp:
            ax.text((x0 + x1) / 2, y0 - 0.3, "each arbor pruned to one position", ha="center", va="top", fontsize=7.5, color=GRAY)
    axes[0].text(6, -0.45, "A. Chemical gradients lay down a coarse map", ha="center", fontsize=9.5, color=GRAY)
    axes[1].text(6, -0.45, "B. Correlated activity sharpens it", ha="center", fontsize=9.5, color=GRAY)
    axes[1].text(3.6, 1.15, "driven by spontaneous\nretinal waves,\nthen by vision", ha="center", va="top", fontsize=7.5, color=GREEN)
    fig.tight_layout(); fig.savefig(OUT / "fig_axon_guidance_refinement.png", dpi=200); plt.close(fig)


if __name__ == "__main__":
    fig_cell_energy_entropy(); fig_hodgkin_huxley_simulation(); fig_axon_guidance_refinement()
    print("wrote figures to", OUT)
