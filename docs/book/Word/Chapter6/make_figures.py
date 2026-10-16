#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 6 (Perception as Inference). Outputs into ./images.
Requires matplotlib and numpy."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle, Polygon, Wedge

OUT = Path(__file__).parent / "images"; OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
EXC, INH, GRAY, GOLD, GREEN = "#1f4e79", "#b03a2e", "#555555", "#c9a227", "#2e7d32"


def arrow(ax, a, b, color=GRAY, lw=1.5, style="-|>", ls="-", shrink=0, cs=None):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, color=color, lw=lw, linestyle=ls, mutation_scale=12,
                                 shrinkA=shrink, shrinkB=shrink, connectionstyle=cs or "arc3,rad=0"))


def fig_inverse():
    """Figure 6.1: one retinal image, many possible worlds."""
    fig, ax = plt.subplots(figsize=(9, 3.4)); ax.set_xlim(0, 18); ax.set_ylim(0, 6.5); ax.set_aspect("equal"); ax.axis("off")
    # retinal image in the middle
    ax.add_patch(FancyBboxPatch((7.4, 1.6), 3.2, 3.4, boxstyle="round,pad=0.1", fc="#f4f4f4", ec=GRAY, lw=1.2))
    ax.add_patch(Polygon([(8.3, 2.3), (9.7, 2.3), (9.4, 4.2), (8.6, 4.2)], closed=True, fc="white", ec=EXC, lw=2))
    ax.text(9.0, 5.3, "the retinal image", ha="center", fontsize=9, color=GRAY); ax.text(9.0, 1.2, "a trapezoid", ha="center", fontsize=8.5, color=EXC)
    # four worlds: each drawn in a small scene whose grid shows the plane the shape lies in
    def scene(x0, y0, label, kind):
        if kind == "floor":      # rectangle lying on a receding ground plane: seen in perspective as a trapezoid
            for k in range(5):   # receding lines converge toward a vanishing point
                ax.plot([x0 + 0.1 + k * 0.7, x0 + 1.0 + k * 0.35], [y0, y0 + 1.9], color="#cccccc", lw=0.7)
            for k in range(4):   # horizontal lines get closer with distance
                yk = y0 + 1.9 * (1 - 0.72 ** (k + 1)); ax.plot([x0 - 0.1, x0 + 3.1], [yk, yk], color="#cccccc", lw=0.7)
            ax.add_patch(Polygon([(x0 + 0.65, y0 + 0.35), (x0 + 2.35, y0 + 0.35), (x0 + 2.0, y0 + 1.45), (x0 + 1.0, y0 + 1.45)], closed=True, fc="white", ec=GRAY, lw=1.6))
        else:                    # trapezoid painted on a wall facing the viewer: a flat square grid
            for k in range(5): ax.plot([x0 + k * 0.75, x0 + k * 0.75], [y0, y0 + 1.9], color="#cccccc", lw=0.7)
            for k in range(4): ax.plot([x0, x0 + 3.0], [y0 + 0.48 * (k + 0.5), y0 + 0.48 * (k + 0.5)], color="#cccccc", lw=0.7)
            ax.add_patch(Polygon([(x0 + 0.65, y0 + 0.35), (x0 + 2.35, y0 + 0.35), (x0 + 2.0, y0 + 1.45), (x0 + 1.0, y0 + 1.45)], closed=True, fc="white", ec=GRAY, lw=1.6))
        ax.text(x0 + 1.5, y0 - 0.25, label, ha="center", va="top", fontsize=8, color=GRAY)
    scene(0.6, 3.9, "a rectangle lying flat,\nreceding from the viewer", "floor")
    scene(0.6, 0.7, "a trapezoid on a wall,\nface on", "wall")
    scene(14.4, 3.9, "a rectangle on a desk,\nseen from a standing viewer", "floor")
    scene(14.4, 0.7, "a trapezoid painted on\na billboard", "wall")
    for (xa, ya) in [(3.9, 4.6), (3.9, 1.6)]:
        arrow(ax, (xa, ya), (7.3, 3.3), color=GOLD, lw=1.4)
    for (xa, ya) in [(14.1, 4.6), (14.1, 1.6)]:
        arrow(ax, (xa, ya), (10.7, 3.3), color=GOLD, lw=1.4)
    ax.text(2.1, 6.2, "many possible causes...", ha="center", fontsize=9, color=GOLD)
    ax.text(15.9, 6.2, "...of the same evidence", ha="center", fontsize=9, color=GOLD)
    fig.tight_layout(); fig.savefig(OUT / "fig_inverse.png", dpi=200); plt.close(fig)


def fig_hierarchy():
    """Figure 6.2: the ventral visual pathway with receptive fields growing at each stage."""
    fig, ax = plt.subplots(figsize=(9.5, 3.8)); ax.set_xlim(0, 19); ax.set_ylim(0, 7.6); ax.set_aspect("equal"); ax.axis("off")
    stages = [("retina", 1.3, "points of\ncontrast", 0.18), ("LGN\n(thalamus)", 4.3, "points, with\ngain control", 0.22),
              ("V1", 7.3, "oriented\nedges", 0.35), ("V2", 10.3, "contours,\ntextures", 0.6), ("V4", 13.3, "shape parts,\ncolor", 1.0),
              ("IT", 16.6, "objects,\nfaces", 1.6)]
    for name, x, what, r in stages:
        ax.add_patch(FancyBboxPatch((x - 1.1, 3.0), 2.2, 1.4, boxstyle="round,pad=0.08", fc="white", ec=EXC, lw=1.6))
        ax.text(x, 3.7, name, ha="center", va="center", fontsize=9.5, color=EXC, fontweight="bold")
        ax.text(x, 2.5, what, ha="center", va="top", fontsize=8, color=GRAY)
        ax.add_patch(Circle((x, 6.2), r * 0.62, fc="#dbe5f0", ec=EXC, lw=1))
    ax.text(0.2, 7.3, "receptive field size (schematic):", fontsize=8, color=GRAY)
    for i in range(len(stages) - 1):
        x0, x1 = stages[i][1] + 1.1, stages[i + 1][1] - 1.1
        arrow(ax, (x0, 3.95), (x1, 3.95), color=EXC, lw=2.2)
        if i >= 1:
            arrow(ax, (x1, 3.35), (x0, 3.35), color=INH, lw=2.6)
    arrow(ax, (stages[1][1] - 1.1, 3.35), (stages[0][1] + 1.1, 3.35), color="white", lw=0)  # no feedback to retina
    ax.plot([6.2, 6.2], [3.95, 4.0], color="white")
    # LGN gets cortical feedback (strong)
    arrow(ax, (6.2, 3.35), (5.4, 3.35), color=INH, lw=2.6)
    ax.text(9.5, 0.9, "feedforward (blue, upward through the hierarchy): fast, carries evidence\n"
                      "feedback (red, downward): more numerous axons, carries predictions and context",
            ha="center", fontsize=8.2, color=GRAY)
    ax.text(9.5, 0.15, "The feedforward sweep reaches IT in about 100 ms; most of what the cortex does with an image happens after that, in the loops.",
            ha="center", fontsize=7.8, color=GRAY, style="italic")
    fig.tight_layout(); fig.savefig(OUT / "fig_hierarchy.png", dpi=200); plt.close(fig)


def fig_bayes():
    """Figure 6.3: prior, likelihood, posterior for a one-dimensional estimate."""
    x = np.linspace(-30, 50, 800)
    def g(m, s): return np.exp(-0.5 * ((x - m) / s) ** 2) / (s * np.sqrt(2 * np.pi))
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.3))
    for ax, (sl, title) in zip(axes, [(5.0, "A. Precise evidence: the posterior follows the evidence"), (15.0, "B. Noisy evidence: the posterior stays near the prior")]):
        mp, sp, ml = 0.0, 10.0, 20.0
        prior, like = g(mp, sp), g(ml, sl)
        post_prec = 1 / sp ** 2 + 1 / sl ** 2; mpost = (mp / sp ** 2 + ml / sl ** 2) / post_prec; spost = np.sqrt(1 / post_prec)
        post = g(mpost, spost)
        ax.plot(x, prior, color=GRAY, lw=1.8, label="prior (what is usually true)")
        ax.plot(x, like, color=GOLD, lw=1.8, label="likelihood (what the senses say)")
        ax.plot(x, post, color=EXC, lw=2.4, label="posterior (the percept)")
        ax.axvline(mpost, color=EXC, lw=0.8, ls="--")
        ax.set_title(title, fontsize=9.5, loc="left"); ax.set_yticks([]); ax.set_xlabel("estimated position (degrees)", fontsize=9)
        ax.text(mpost, ax.get_ylim()[1] * 0.02, f"{mpost:.0f}°", color=EXC, fontsize=8.5, ha="left")
        for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    axes[0].legend(fontsize=7.5, frameon=False, loc="upper left")
    fig.tight_layout(); fig.savefig(OUT / "fig_bayes.png", dpi=200); plt.close(fig)


def fig_light_above():
    """Figure 6.4: shaded discs read as bumps or dents according to the light-from-above prior."""
    n = 120; yy, xx = np.mgrid[-1:1:complex(0, n), -1:1:complex(0, n)]; rr = np.sqrt(xx ** 2 + yy ** 2)
    def disc(light_from_top):
        shade = 0.55 + 0.45 * (yy if light_from_top else -yy)  # brighter at the top if lit from above
        img = np.ones((n, n)) * 0.78; img[rr <= 0.92] = shade[rr <= 0.92]; return img
    fig, axes = plt.subplots(1, 2, figsize=(8, 2.6))
    for ax, title in zip(axes, ["A. Viewed this way up", "B. The same image, rotated by 180°"]):
        grid = np.ones((2 * n + 20, 3 * n + 40)) * 0.78
        pattern = [[True, False, True], [False, True, False]] if title.startswith("A") else [[False, True, False], [True, False, True]]
        for i in range(2):
            for j in range(3):
                grid[10 + i * n:10 + (i + 1) * n, 10 + j * (n + 10):10 + j * (n + 10) + n] = disc(pattern[i][j])
        ax.imshow(grid, cmap="gray", vmin=0, vmax=1); ax.axis("off"); ax.set_title(title, fontsize=9.5, loc="left")
    fig.text(0.5, 0.02, "Discs lighter on top look like bumps; discs lighter on the bottom look like dents. Rotate the page and they swap.",
             ha="center", fontsize=8, color=GRAY)
    fig.tight_layout(rect=(0, 0.06, 1, 1)); fig.savefig(OUT / "fig_light_above.png", dpi=200); plt.close(fig)


def fig_predictive():
    """Figure 6.5: a predictive-coding hierarchy and the error signal it produces for a repeated input with one oddball."""
    fig = plt.figure(figsize=(9.5, 4.2)); gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 1])
    ax = fig.add_subplot(gs[0]); ax.set_xlim(0, 10); ax.set_ylim(0, 8.2); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("A. Predictions down, errors up", fontsize=9.5, loc="left")
    levels = [("level 1  (e.g. V1)", 1.0), ("level 2  (e.g. V2)", 3.6), ("level 3  (e.g. V4)", 6.2)]
    for name, y in levels:
        ax.add_patch(FancyBboxPatch((1.0, y), 3.2, 1.5, boxstyle="round,pad=0.08", fc="#fbeeea", ec=INH, lw=1.4))
        ax.text(2.6, y + 1.05, "prediction units", ha="center", fontsize=8, color=INH); ax.text(2.6, y + 0.45, "deep layers (5/6)", ha="center", fontsize=7, color=GRAY)
        ax.add_patch(FancyBboxPatch((5.4, y), 3.2, 1.5, boxstyle="round,pad=0.08", fc="#e8eef5", ec=EXC, lw=1.4))
        ax.text(7.0, y + 1.05, "error units", ha="center", fontsize=8, color=EXC); ax.text(7.0, y + 0.45, "superficial layers (2/3)", ha="center", fontsize=7, color=GRAY)
        ax.text(9.9, y + 0.75, name, ha="right", va="center", fontsize=7.5, color=GRAY, rotation=90)
        arrow(ax, (4.2, y + 0.75), (5.4, y + 0.75), color=INH, lw=1.6, style="-|>")  # prediction subtracted from input
        ax.text(4.8, y + 0.95, "−", ha="center", fontsize=12, color=INH)
    for (n0, y0), (n1, y1) in zip(levels[:-1], levels[1:]):
        arrow(ax, (7.0, y0 + 1.5), (2.9, y1), color=EXC, lw=2.0)        # error up to next level's predictions
        arrow(ax, (2.3, y1), (2.3, y0 + 1.5), color=INH, lw=2.0)       # predictions down
    ax.text(0.15, 7.95, "errors ascend (fast, gamma)", fontsize=7.5, color=EXC)
    ax.text(0.15, 0.25, "predictions descend (slower, alpha/beta)", fontsize=7.5, color=INH)
    arrow(ax, (7.0, 0.1), (7.0, 1.0), color=GOLD, lw=2.0); ax.text(7.2, 0.3, "sensory input", fontsize=7.5, color=GOLD)
    # panel B: simulated error for a repeated tone with an oddball
    ax2 = fig.add_subplot(gs[1]); ax2.set_title("B. Simulated error signal: repetition and surprise", fontsize=9.5, loc="left")
    pred, eta = 0.0, 0.5; stims = [1.0] * 6 + [0.3] + [1.0] * 4; errs = []
    for s in stims:
        e = s - pred; errs.append(abs(e)); pred += eta * e
    xs = np.arange(1, len(stims) + 1)
    ax2.bar(xs, errs, color=[INH if i == 6 else EXC for i in range(len(stims))], width=0.6)
    ax2.set_xticks(xs); ax2.set_xticklabels(["A"] * 6 + ["B"] + ["A"] * 4, fontsize=8); ax2.set_xlabel("stimulus sequence", fontsize=9)
    ax2.set_ylabel("|prediction error|", fontsize=9); ax2.set_ylim(0, 1.15)
    ax2.text(1, 1.05, "first presentation", fontsize=7.5, color=EXC); ax2.text(7, 0.75, "oddball", fontsize=7.5, color=INH, ha="center")
    ax2.text(4.6, 0.3, "repetition\nsuppression", fontsize=7.5, color=GRAY, ha="center")
    for s in ("top", "right"): ax2.spines[s].set_visible(False)
    fig.tight_layout(); fig.savefig(OUT / "fig_predictive.png", dpi=200); plt.close(fig)
    return errs


def fig_illusions():
    """Figure 6.7: Kanizsa triangle and the Müller-Lyer figure."""
    fig, axes = plt.subplots(1, 2, figsize=(8.5, 3.6))
    ax = axes[0]; ax.set_xlim(0, 10); ax.set_ylim(0, 9); ax.set_aspect("equal"); ax.axis("off"); ax.set_title("A. Kanizsa triangle", fontsize=9.5, loc="left")
    verts = np.array([(5, 7.6), (1.8, 2.0), (8.2, 2.0)])
    for v in verts:
        ax.add_patch(Circle(v, 1.1, fc="black", ec="none"))
    ax.add_patch(Polygon(verts, closed=True, fc="white", ec="none"))
    # inverted outline triangle behind
    inv = np.array([(5, 1.0), (1.4, 7.1), (8.6, 7.1)])
    def inside(p, tri):
        (x1, y1), (x2, y2), (x3, y3) = tri; px, py = p
        d1 = (px - x2) * (y1 - y2) - (x1 - x2) * (py - y2); d2 = (px - x3) * (y2 - y3) - (x2 - x3) * (py - y3); d3 = (px - x1) * (y3 - y1) - (x3 - x1) * (py - y1)
        return not ((d1 < 0 or d2 < 0 or d3 < 0) and (d1 > 0 or d2 > 0 or d3 > 0))
    for i in range(3):
        a, b = inv[i], inv[(i + 1) % 3]; ts = np.linspace(0, 1, 400); pts = [a + t * (b - a) for t in ts]
        vis = [not inside(p, verts) for p in pts]; run = []
        for p, v in zip(pts, vis):
            if v: run.append(p)
            if (not v or p is pts[-1]) and run:
                ax.plot([q[0] for q in run], [q[1] for q in run], color="black", lw=1.2); run = []
    ax.text(5, 0.2, "no white triangle is drawn; the brain infers an occluder", ha="center", fontsize=8, color=GRAY)
    ax = axes[1]; ax.set_xlim(0, 10); ax.set_ylim(0, 9); ax.set_aspect("equal"); ax.axis("off"); ax.set_title("B. Müller-Lyer", fontsize=9.5, loc="left")
    for y, out in [(6.5, True), (3.0, False)]:
        ax.plot([2, 8], [y, y], color="black", lw=2)
        for x, sgn in [(2, 1), (8, -1)]:
            dx = 0.9 * sgn * (1 if out else -1)
            ax.plot([x, x + dx], [y, y + 0.9], color="black", lw=2); ax.plot([x, x + dx], [y, y - 0.9], color="black", lw=2)
    ax.text(5, 1.4, "both horizontal lines are the same length (6 units)", ha="center", fontsize=8, color=GRAY)
    ax.text(5, 0.4, "top: arrowheads, read as a near outside corner, looks shorter;\nbottom: arrow tails, read as a far inside corner, looks longer", ha="center", fontsize=7.5, color=GRAY)
    fig.tight_layout(); fig.savefig(OUT / "fig_illusions.png", dpi=200); plt.close(fig)


def fig_cues():
    """Figure 6.8: precision-weighted cue combination (vision and touch estimating a width)."""
    x = np.linspace(40, 70, 800)
    def g(m, s): return np.exp(-0.5 * ((x - m) / s) ** 2) / (s * np.sqrt(2 * np.pi))
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.3))
    for ax, (sv, title) in zip(axes, [(2.0, "A. Clear view: vision dominates"), (8.0, "B. Vision blurred: touch takes over")]):
        mv, mh, sh = 52.0, 58.0, 4.0
        pv, ph = 1 / sv ** 2, 1 / sh ** 2; wv = pv / (pv + ph); mc = wv * mv + (1 - wv) * mh; sc = np.sqrt(1 / (pv + ph))
        ax.plot(x, g(mv, sv), color=EXC, lw=1.8, label=f"vision (σ = {sv:.0f} mm)")
        ax.plot(x, g(mh, sh), color=GOLD, lw=1.8, label=f"touch (σ = {sh:.0f} mm)")
        ax.plot(x, g(mc, sc), color=GRAY, lw=2.4, ls="--", label=f"combined (σ = {sc:.1f} mm)")
        ax.axvline(mc, color=GRAY, lw=0.8, ls=":"); ax.text(mc + 0.4, ax.get_ylim()[1] * 0.45, f"combined: {mc:.1f} mm\nweight on vision = {wv:.2f}", fontsize=8, color=GRAY)
        ax.set_title(title, fontsize=9.5, loc="left"); ax.set_yticks([]); ax.set_xlabel("estimated width (mm)", fontsize=9)
        ax.legend(fontsize=7.5, frameon=False, loc="upper left")
        for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    fig.tight_layout(); fig.savefig(OUT / "fig_cues.png", dpi=200); plt.close(fig)


def fig_efference():
    """Figure 6.9: efference copy cancels the sensory consequences of one's own movement."""
    fig, ax = plt.subplots(figsize=(9, 3.6)); ax.set_xlim(0, 18); ax.set_ylim(0, 7); ax.set_aspect("equal"); ax.axis("off")
    def box(x, y, w, h, text, color=EXC):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08", fc="white", ec=color, lw=1.5))
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=8.5, color=color)
    box(0.5, 4.4, 3.2, 1.4, "motor command\n(move the eye 10° right)")
    box(0.5, 1.0, 3.2, 1.4, "eye muscles", GRAY)
    box(6.0, 4.4, 3.4, 1.4, "forward model\n(cerebellum, Chapter 4)", INH)
    box(6.0, 1.0, 3.4, 1.4, "retina", GRAY)
    box(11.0, 2.7, 3.0, 1.6, "compare\n(actual − predicted)", GRAY)
    box(14.6, 2.7, 3.0, 1.6, "perceived motion\nof the world", EXC)
    arrow(ax, (2.1, 4.4), (2.1, 2.4), color=EXC, lw=1.8); ax.text(2.3, 3.3, "command", fontsize=7.5, color=EXC)
    arrow(ax, (3.7, 5.1), (6.0, 5.1), color=INH, lw=1.8); ax.text(4.85, 5.35, "efference copy", fontsize=7.5, color=INH, ha="center")
    arrow(ax, (3.7, 1.7), (6.0, 1.7), color=GRAY, lw=1.8); ax.text(4.85, 2.05, "eye turns: image\nslides 10° left", fontsize=7.5, color=GRAY, ha="center", va="bottom")
    arrow(ax, (9.4, 5.1), (12.2, 4.3), color=INH, lw=1.8); ax.text(11.0, 5.2, "predicted slip: 10° left", fontsize=7.5, color=INH, ha="center")
    arrow(ax, (9.4, 1.7), (12.2, 2.7), color=GRAY, lw=1.8); ax.text(11.0, 1.5, "actual slip: 10° left", fontsize=7.5, color=GRAY, ha="center")
    arrow(ax, (14.0, 3.5), (14.9, 3.5), color=EXC, lw=1.8); ax.text(16.35, 2.2, "= 0: the world stays still", fontsize=8, color=EXC, ha="center")
    ax.text(9, 0.3, "Press on your eyelid instead: the image slips with no command, no prediction is subtracted, and the world appears to jump.",
            ha="center", fontsize=8, color=GRAY, style="italic")
    fig.tight_layout(); fig.savefig(OUT / "fig_efference.png", dpi=200); plt.close(fig)


def fig_gabor():
    """Figure 6.10: Gabor-like receptive fields of the kind found in V1 and learned from natural images."""
    n = 48; yy, xx = np.mgrid[-1:1:complex(0, n), -1:1:complex(0, n)]
    fig, axes = plt.subplots(2, 6, figsize=(9, 3.2))
    rng = np.random.default_rng(6)
    for k, ax in enumerate(axes.flat):
        th = np.pi * k / 6 + rng.uniform(-0.1, 0.1); f = rng.uniform(2.0, 3.6); ph = rng.choice([0, np.pi / 2]); s = rng.uniform(0.28, 0.4)
        xr = xx * np.cos(th) + yy * np.sin(th); yr = -xx * np.sin(th) + yy * np.cos(th)
        g = np.exp(-(xr ** 2 + (0.8 * yr) ** 2) / (2 * s ** 2)) * np.cos(2 * np.pi * f * xr + ph)
        ax.imshow(g, cmap="gray", vmin=-1, vmax=1); ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values(): sp.set_edgecolor("#cccccc")
    fig.text(0.5, 0.04, "Receptive fields of V1 simple cells (schematic): localized, oriented, band-pass. Light = excitatory region, dark = inhibitory.",
             ha="center", fontsize=8.5, color=GRAY)
    fig.tight_layout(rect=(0, 0.1, 1, 1)); fig.savefig(OUT / "fig_gabor.png", dpi=200); plt.close(fig)


if __name__ == "__main__":
    fig_inverse(); fig_hierarchy(); fig_bayes(); fig_light_above(); errs = fig_predictive(); fig_illusions(); fig_cues(); fig_efference(); fig_gabor()
    print("errors in 6.5B:", [round(e, 3) for e in errs])
    print("done:", sorted(p.name for p in OUT.iterdir()))
