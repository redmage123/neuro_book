#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 4 (Circuits, Networks, and Coordinated Behavior).

Outputs (into ./images):
  fig_motifs.png   Figure 4.1  six circuit motifs
  fig_ei.png       Figure 4.2  excitation-inhibition balance (rate-model simulation)
  fig_cpg.png      Figure 4.4  half-center oscillator (rate-model simulation)
  fig_bg.png       Figure 4.7  selection by disinhibition in the basal ganglia
  fig_rhythms.png  Figure 4.10 EEG bands composite (needs eeg_theta/alpha/beta/gamma.png,
                   Hugo Gamboa, Wikimedia Commons, CC BY-SA 3.0)

The other figures are downloaded from Wikimedia Commons; see "Figure Credits" in the chapter
and the URLs listed at the bottom of this file.

Requires: matplotlib, numpy, Pillow.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).parent / "images"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
EXC, INH, GRAY = "#1f4e79", "#b03a2e", "#555555"


def neuron(ax, x, y, label, color=EXC, r=0.22):
    ax.add_patch(Circle((x, y), r, fc="white", ec=color, lw=2, zorder=3))
    ax.text(x, y, label, ha="center", va="center", fontsize=9, color=color, zorder=4)


def conn(ax, p, q, kind="exc", rad=0.0, r=0.22):
    (x1, y1), (x2, y2) = p, q
    d = np.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    start = (x1 + ux * r, y1 + uy * r)
    end = (x2 - ux * (r + 0.05), y2 - uy * (r + 0.05))
    if kind == "exc":
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=14, lw=1.6, color=EXC,
                                     connectionstyle=f"arc3,rad={rad}", zorder=2))
    else:
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-", lw=1.6, color=INH,
                                     connectionstyle=f"arc3,rad={rad}", zorder=2))
        ax.add_patch(Circle(end, 0.07, fc=INH, ec=INH, zorder=3))


def fig_motifs():
    fig, axes = plt.subplots(2, 3, figsize=(9, 5.6))
    titles = ["A. Reflex arc (reciprocal inhibition)", "B. Feedforward inhibition", "C. Feedback (recurrent) inhibition",
              "D. Lateral inhibition", "E. Recurrent excitation", "F. Disinhibition"]
    for ax, t in zip(axes.flat, titles):
        ax.set_xlim(0, 4); ax.set_ylim(0, 3); ax.set_aspect("equal"); ax.axis("off"); ax.set_title(t, fontsize=9.5, loc="left")
    ax = axes[0, 0]
    neuron(ax, 0.6, 2.2, "S"); neuron(ax, 2.0, 2.2, "M1"); neuron(ax, 2.0, 0.8, "M2"); neuron(ax, 1.3, 1.5, "I", INH, 0.18)
    conn(ax, (0.6, 2.2), (2.0, 2.2)); conn(ax, (0.6, 2.2), (1.3, 1.5), r=0.2); conn(ax, (1.3, 1.5), (2.0, 0.8), "inh", r=0.18)
    ax.text(3.0, 2.2, "flexor", fontsize=8, color=GRAY, va="center"); ax.text(3.0, 0.8, "extensor", fontsize=8, color=GRAY, va="center")
    ax.text(0.6, 2.65, "sensory", fontsize=8, color=GRAY, ha="center")
    ax = axes[0, 1]
    neuron(ax, 0.6, 1.5, "In"); neuron(ax, 2.0, 2.3, "I", INH, 0.18); neuron(ax, 3.2, 1.5, "E")
    conn(ax, (0.6, 1.5), (3.2, 1.5)); conn(ax, (0.6, 1.5), (2.0, 2.3), r=0.2); conn(ax, (2.0, 2.3), (3.2, 1.5), "inh", r=0.18)
    ax.text(2.0, 0.5, "input excites E and, slightly later,\nthe interneuron that shuts E off:\na narrow window for integration", fontsize=7.5, ha="center", color=GRAY)
    ax = axes[0, 2]
    neuron(ax, 0.6, 1.5, "In"); neuron(ax, 2.0, 1.5, "E"); neuron(ax, 3.2, 2.3, "I", INH, 0.18)
    conn(ax, (0.6, 1.5), (2.0, 1.5)); conn(ax, (2.0, 1.5), (3.2, 2.3), rad=-0.3); conn(ax, (3.2, 2.3), (2.0, 1.5), "inh", rad=-0.3, r=0.18); conn(ax, (2.0, 1.5), (3.6, 0.9))
    ax.text(2.0, 0.4, "E's own output recruits inhibition\nthat limits E: a thermostat", fontsize=7.5, ha="center", color=GRAY)
    ax = axes[1, 0]
    for i, x in enumerate([0.7, 2.0, 3.3]):
        neuron(ax, x, 2.3, f"In{i + 1}"); neuron(ax, x, 0.8, f"E{i + 1}"); conn(ax, (x, 2.3), (x, 0.8))
    neuron(ax, 1.35, 1.55, "I", INH, 0.16); neuron(ax, 2.65, 1.55, "I", INH, 0.16)
    conn(ax, (2.0, 2.3), (1.35, 1.55), r=0.16); conn(ax, (2.0, 2.3), (2.65, 1.55), r=0.16)
    conn(ax, (1.35, 1.55), (0.7, 0.8), "inh", r=0.16); conn(ax, (2.65, 1.55), (3.3, 0.8), "inh", r=0.16)
    ax = axes[1, 1]
    neuron(ax, 0.6, 1.5, "In"); neuron(ax, 2.0, 1.5, "E1"); neuron(ax, 3.2, 1.5, "E2")
    conn(ax, (0.6, 1.5), (2.0, 1.5)); conn(ax, (2.0, 1.5), (3.2, 1.5), rad=-0.4); conn(ax, (3.2, 1.5), (2.0, 1.5), rad=-0.4)
    ax.text(2.6, 0.5, "activity outlives its input:\npersistence, memory, risk of runaway", fontsize=7.5, ha="center", color=GRAY)
    ax = axes[1, 2]
    neuron(ax, 0.6, 1.5, "In"); neuron(ax, 1.7, 1.5, "I1", INH, 0.18); neuron(ax, 2.8, 1.5, "I2", INH, 0.18); neuron(ax, 3.8, 1.5, "E", r=0.2)
    conn(ax, (0.6, 1.5), (1.7, 1.5), r=0.18); conn(ax, (1.7, 1.5), (2.8, 1.5), "inh", r=0.18); conn(ax, (2.8, 1.5), (3.8, 1.5), "inh", r=0.2)
    ax.text(2.2, 0.5, "I2 holds E silent by default;\ninput silences I2 and releases E", fontsize=7.5, ha="center", color=GRAY)
    fig.text(0.5, 0.01, "Arrowheads: excitatory synapses.  Filled circles: inhibitory synapses.", ha="center", fontsize=8, color=GRAY)
    fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(OUT / "fig_motifs.png", dpi=200); plt.close(fig)


def fig_ei():
    def sim(gI, T=300, dt=1.0, seed=3, cap=5.0):
        rng = np.random.default_rng(seed); E = np.zeros(T); I = np.zeros(T); e = i = 0.0
        f = lambda x: cap * np.tanh(np.maximum(0, x) / cap)
        for t in range(1, T):
            inp = 0.6 + (0.8 if 100 <= t < 110 else 0) + rng.normal(0, 0.15)
            e += (-e + f(1.6 * e - gI * i + inp)) / 10 * dt
            i += (-i + f(1.2 * e)) / 5 * dt
            E[t] = e; I[t] = i
        return E, I
    fig, axes = plt.subplots(1, 3, figsize=(9, 2.7))
    for ax, g, t in zip(axes, [0.0, 1.6, 3.5], ["No inhibition: runaway to saturation", "Balanced: brief, bounded response", "Too much inhibition: muted"]):
        E, I = sim(g); ax.plot(E, color=EXC, lw=1.5, label="excitatory rate")
        if g > 0:
            ax.plot(I, color=INH, lw=1.2, label="inhibitory rate")
        ax.axvspan(100, 110, color="gold", alpha=0.35, lw=0); ax.axhline(5, color=GRAY, ls=":", lw=1)
        ax.set_title(t, fontsize=9.5); ax.set_xlabel("time (ms)"); ax.set_ylim(0, 5.6)
    axes[0].text(150, 5.12, "ceiling: every neuron firing flat out", fontsize=7, color=GRAY, ha="left", va="bottom")
    axes[0].set_ylabel("population activity"); axes[1].legend(fontsize=7.5, loc="center right", frameon=False)
    fig.text(0.5, -0.02, "Yellow band: a brief sensory input. The same excitatory network behaves differently depending only on inhibitory gain.", ha="center", fontsize=8, color=GRAY)
    fig.tight_layout(); fig.savefig(OUT / "fig_ei.png", dpi=200, bbox_inches="tight"); plt.close(fig)


def fig_cpg(w=2.5, ga=3.0, tau_a=120, T=800, dt=0.5):
    n = int(T / dt); a = np.zeros(n); b = np.zeros(n); x, y, ua, ub = 0.6, 0.0, 0.0, 0.0
    for k in range(1, n):
        t = k * dt; drive = 1.0 if t >= 50 else 0.0
        dx = (-x + max(0, drive - w * y - ua)) / 8; dy = (-y + max(0, drive - w * x - ub)) / 8
        dua = (-ua + ga * x) / tau_a; dub = (-ub + ga * y) / tau_a
        x += dx * dt; y += dy * dt; ua += dua * dt; ub += dub * dt; a[k] = x; b[k] = y
    t = np.arange(n) * dt
    fig = plt.figure(figsize=(9, 3.2)); gs = fig.add_gridspec(1, 2, width_ratios=[1, 2])
    ax = fig.add_subplot(gs[0]); ax.set_xlim(0, 3); ax.set_ylim(0, 3); ax.set_aspect("equal"); ax.axis("off"); ax.set_title("A. Half-center circuit", fontsize=9.5, loc="left")
    neuron(ax, 0.8, 1.5, "L"); neuron(ax, 2.2, 1.5, "R"); conn(ax, (0.8, 1.5), (2.2, 1.5), "inh", rad=-0.45); conn(ax, (2.2, 1.5), (0.8, 1.5), "inh", rad=-0.45)
    for xx in (0.8, 2.2):
        ax.annotate("", xy=(xx, 1.78), xytext=(xx, 2.6), arrowprops=dict(arrowstyle="-|>", color=EXC, lw=1.5))
    ax.text(1.5, 2.75, "steady (non-rhythmic) drive", ha="center", fontsize=8, color=GRAY)
    ax.text(0.8, 0.75, "left\nmuscles", ha="center", fontsize=8, color=GRAY); ax.text(2.2, 0.75, "right\nmuscles", ha="center", fontsize=8, color=GRAY)
    ax.text(1.5, 0.95, "mutual inhibition\n+ fatigue", ha="center", fontsize=7.5, color=INH)
    ax2 = fig.add_subplot(gs[1]); ax2.plot(t, a, color=EXC, lw=1.5, label="L"); ax2.plot(t, b, color="#e67e22", lw=1.5, label="R")
    ax2.axvline(50, color=GRAY, ls="--", lw=1); ax2.text(55, ax2.get_ylim()[1] * 0.97, "drive switched on", fontsize=8, color=GRAY, va="top")
    ax2.set_title("B. Output: alternation from a constant input", fontsize=9.5, loc="left"); ax2.set_xlabel("time (ms)"); ax2.set_ylabel("activity"); ax2.legend(frameon=False, fontsize=8, loc="upper right")
    fig.tight_layout(); fig.savefig(OUT / "fig_cpg.png", dpi=200); plt.close(fig)


def fig_bg():
    fig, ax = plt.subplots(figsize=(7.5, 4.2)); ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")

    def box(x, y, w, h, label, color=EXC):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05", fc="white", ec=color, lw=2))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=9, color=color)

    def arrow(p, q, kind="exc", color=None, text=None, tx=None, ty=None):
        color = color or (EXC if kind == "exc" else INH)
        if kind == "exc":
            ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=14, lw=1.8, color=color))
        else:
            ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-", lw=1.8, color=color)); ax.add_patch(Circle(q, 0.09, fc=color, ec=color))
        if text:
            ax.text(tx, ty, text, fontsize=8, color=color, ha="center")

    box(0.5, 4.6, 3, 0.9, "Cortex\n(candidate actions, in parallel)"); box(0.5, 2.6, 3, 0.9, "Striatum\n(input nucleus)")
    box(4.5, 2.6, 2.6, 0.9, "GPi / SNr\n(output: tonic inhibition)", INH); box(8.0, 2.6, 1.7, 0.9, "Thalamus")
    box(4.5, 0.5, 2.6, 0.9, "Brainstem motor\ncircuits"); box(0.5, 0.5, 3, 0.9, "Dopamine (SNc)\nsets the gain, Ch. 3", GRAY)
    arrow((2.0, 4.6), (2.0, 3.55)); arrow((3.5, 3.05), (4.45, 3.05), "inh", text="direct pathway:\nstriatum inhibits the inhibitor", tx=4.0, ty=3.75)
    arrow((7.1, 3.05), (7.95, 3.05), "inh"); arrow((5.8, 2.6), (5.8, 1.45), "inh"); arrow((8.85, 3.5), (3.5, 5.3), color=EXC)
    ax.text(8.6, 4.6, "selected action\nreleased", fontsize=8, color=EXC, ha="center"); arrow((2.0, 1.4), (2.0, 2.55), color=GRAY)
    ax.text(5.0, 5.5, "Default state: every action is held off by tonic inhibition from GPi/SNr.\nSelecting an action means switching off the inhibition that covers it.", fontsize=8.5, color=GRAY, ha="left")
    fig.tight_layout(); fig.savefig(OUT / "fig_bg.png", dpi=200); plt.close(fig)


def fig_rhythms():
    from PIL import Image
    names = [("eeg_theta.png", "Theta (4-8 Hz): memory encoding, navigation"), ("eeg_alpha.png", "Alpha (8-12 Hz): idling, inhibition of unused regions"),
             ("eeg_beta.png", "Beta (13-30 Hz): holding a motor or cognitive state"), ("eeg_gamma.png", "Gamma (30-100 Hz): local processing, attention")]
    fig, axes = plt.subplots(4, 1, figsize=(7.5, 6))
    for ax, (f, lab) in zip(axes, names):
        im = Image.open(OUT / f).convert("RGBA"); bg = Image.new("RGBA", im.size, "white"); bg.alpha_composite(im)
        ax.imshow(bg.convert("RGB")); ax.axis("off"); ax.set_title(lab, fontsize=9.5, loc="left")
    fig.text(0.5, 0.005, "One second of scalp EEG filtered into four frequency bands. Traces: Hugo Gamboa, Wikimedia Commons, CC BY-SA 3.0.", ha="center", fontsize=8, color=GRAY)
    fig.tight_layout(rect=(0, 0.02, 1, 1)); fig.savefig(OUT / "fig_rhythms.png", dpi=200); plt.close(fig)


# Wikimedia Commons sources for the downloaded figures (fetch with a descriptive User-Agent):
COMMONS = {
    "retina.png": "https://upload.wikimedia.org/wikipedia/commons/2/21/Fig_retine.png",
    "cajal_cortex.png": "https://upload.wikimedia.org/wikipedia/commons/5/5b/Cajal_cortex_drawings.png",
    "columns.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Cortical_Columns.jpg/1280px-Cortical_Columns.jpg",
    "cereb2.png": "https://upload.wikimedia.org/wikipedia/commons/7/72/CerebCircuit.png",
    "hippo.png": "https://upload.wikimedia.org/wikipedia/commons/2/25/CajalHippocampus_%28modified%29.png",
    "ws.png": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Watts-Strogatz_small-world_model_100nodes.png",
    "connectome.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/The_Human_Connectome.png/1280px-The_Human_Connectome.png",
    "eeg_theta.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Eeg_theta.svg/1280px-Eeg_theta.svg.png",
    "eeg_alpha.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Eeg_alpha.svg/1280px-Eeg_alpha.svg.png",
    "eeg_beta.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Eeg_beta.svg/1280px-Eeg_beta.svg.png",
    "eeg_gamma.png": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Eeg_gamma.svg/1280px-Eeg_gamma.svg.png",
}

if __name__ == "__main__":
    fig_motifs(); fig_ei(); fig_cpg(); fig_bg()
    if all((OUT / f"eeg_{b}.png").exists() for b in ("theta", "alpha", "beta", "gamma")):
        fig_rhythms()
    else:
        print("EEG band images missing; download them from the COMMONS table first.")
    print("done:", sorted(p.name for p in OUT.glob("fig_*.png")))
