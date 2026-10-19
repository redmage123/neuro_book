#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 7 (Emotion and the Body). Outputs into ./images.
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


def arrow(ax, a, b, color=GRAY, lw=1.5, style="-|>", ls="-", shrink=0, cs=None):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, color=color, lw=lw, linestyle=ls, mutation_scale=12,
                                 shrinkA=shrink, shrinkB=shrink, connectionstyle=cs or "arc3,rad=0"))


def box(ax, x, y, w, h, text, fc="white", ec=GRAY, color="black", fs=9, lw=1.2, weight="normal"):
    """Rounded box centered on (x, y)."""
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.08", fc=fc, ec=ec, lw=lw))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=color, weight=weight)


def save(fig, name):
    fig.savefig(OUT / name, dpi=200, bbox_inches="tight", facecolor="white"); plt.close(fig)


def fig_reactive_predictive():
    """Figure 7.1: a meal perturbs glucose; reactive vs anticipatory control (simulated)."""
    dt = 0.5; t = np.arange(-30, 180, dt)
    meal = np.where(t >= 0, 0.06 * np.exp(-t.clip(0) / 40), 0.0)          # glucose influx from the gut
    def run(anticipate):
        g, ins, out_g, out_i = 5.0, 0.0, [], []
        for k, tk in enumerate(t):
            err = max(g - 5.0, 0)
            cue = 0.045 * np.exp(-max(tk, 0) / 25) if (anticipate and tk >= -10) else 0.0          # cephalic-phase insulin on the cue
            target = 0.02 * err + cue
            lag = 15.0
            ins += dt * (target - ins) / lag
            g += dt * (meal[k] - 0.9 * ins - 0.004 * (g - 5.0))
            out_g.append(g); out_i.append(ins)
        return np.array(out_g), np.array(out_i)
    g_r, i_r = run(False); g_p, i_p = run(True)
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(9, 5.2), sharex=True, gridspec_kw={"height_ratios": [2.2, 1]})
    a1.axhline(5.0, color=GRAY, ls=":", lw=1); a1.text(-28, 5.03, "set point", ha="left", fontsize=8.5, color=GRAY)
    a1.plot(t, g_r, color=GRAY, lw=2, label="reactive: responds to the error")
    a1.plot(t, g_p, color=EXC, lw=2, label="predictive: responds to the cue")
    a1.axvline(0, color=GOLD, lw=1.2); a1.text(1.5, a1.get_ylim()[1] * 0.98, "meal", color=GOLD, fontsize=9, va="top")
    a1.axvspan(-10, 0, color=GOLD, alpha=0.12); a1.text(-5, a1.get_ylim()[1] * 0.98, "cue", ha="center", va="top", fontsize=8.5, color=GOLD)
    a1.set_ylabel("blood glucose (mM)"); a1.legend(frameon=False, loc="upper right", fontsize=9)
    a1.spines[["top", "right"]].set_visible(False)
    a2.plot(t, i_r, color=GRAY, lw=2); a2.plot(t, i_p, color=EXC, lw=2)
    a2.axvline(0, color=GOLD, lw=1.2); a2.axvspan(-10, 0, color=GOLD, alpha=0.12)
    a2.set_ylabel("insulin\n(arbitrary)"); a2.set_xlabel("time from start of meal (minutes)"); a2.set_yticks([])
    a2.spines[["top", "right"]].set_visible(False)
    save(fig, "fig_reactive_predictive.png")


def fig_interoceptive_pathways():
    """Figure 7.2: vagal and spinal interoceptive routes to the insula."""
    fig, ax = plt.subplots(figsize=(9, 5.6)); ax.set_xlim(0, 18); ax.set_ylim(0, 11); ax.axis("off")
    # body organs on the left
    organs = [("heart", 8.6), ("lungs", 7.3), ("gut", 6.0), ("blood chemistry,\nimmune signals", 4.5), ("muscle, skin, joints\n(temperature,\npain, itch)", 2.2)]
    for name, y in organs:
        box(ax, 1.9, y, 3.0, 1.0 if "\n" not in name else 1.25, name, fc="#f6f6f6", fs=8.5)
    # relays
    box(ax, 7.0, 7.3, 3.2, 1.1, "nucleus of the\nsolitary tract", ec=EXC, color=EXC)
    box(ax, 7.0, 2.2, 3.2, 1.1, "spinal cord\nlamina I", ec=EXC, color=EXC)
    box(ax, 10.6, 4.8, 2.6, 1.1, "parabrachial\nnucleus", ec=EXC, color=EXC)
    box(ax, 10.6, 8.9, 3.0, 1.1, "hypothalamus,\namygdala", ec=INH, color=INH)
    box(ax, 13.6, 2.6, 2.4, 1.0, "thalamus", ec=EXC, color=EXC)
    box(ax, 15.9, 5.8, 3.0, 1.1, "posterior\ninsula", fc="#e8eef5", ec=EXC, color=EXC, weight="bold")
    box(ax, 15.9, 8.9, 3.0, 1.1, "anterior\ninsula", fc="#e8eef5", ec=EXC, color=EXC, weight="bold")
    # vagal route
    for y in (8.6, 7.3, 6.0, 4.5):
        arrow(ax, (3.45, y), (5.35, 7.3), color=EXC, lw=1.3)
    ax.text(4.2, 8.55, "vagus nerve", fontsize=8.5, color=EXC, style="italic", rotation=0)
    # spinal route
    arrow(ax, (3.45, 2.2), (5.35, 2.2), color=EXC, lw=1.3); ax.text(4.4, 2.45, "thin\nafferents", fontsize=8, color=EXC, ha="center", va="bottom", style="italic")
    arrow(ax, (8.65, 7.0), (9.4, 5.35), color=EXC); arrow(ax, (8.65, 2.5), (9.4, 4.3), color=EXC)
    arrow(ax, (8.0, 7.9), (9.1, 8.6), color=INH); arrow(ax, (10.6, 5.4), (10.6, 8.3), color=INH)
    arrow(ax, (11.9, 4.5), (12.4, 3.0), color=EXC); arrow(ax, (8.65, 2.0), (12.4, 2.5), color=EXC, cs="arc3,rad=0.12")
    arrow(ax, (14.4, 3.15), (15.4, 5.2), color=EXC)
    # blood-borne signals sampled where the blood-brain barrier is leaky
    box(ax, 7.0, 4.75, 2.9, 1.0, "circumventricular\norgans (no barrier)", ec=INH, color=INH, fs=8)
    arrow(ax, (3.45, 4.3), (5.45, 4.75), color=INH, ls="--", lw=1.2)
    arrow(ax, (8.0, 5.3), (9.3, 8.3), color=INH, ls="--", lw=1.2, cs="arc3,rad=0.15")
    arrow(ax, (15.9, 6.4), (15.9, 8.3), color=EXC, lw=2); ax.text(16.15, 7.35, "re-represented\nand integrated", fontsize=8, color=EXC, va="center")
    ax.text(0.4, 10.4, "body", fontsize=10, color=GRAY, weight="bold"); ax.text(7.0, 10.4, "brainstem and spinal relays", fontsize=10, color=GRAY, weight="bold", ha="center")
    ax.text(15.9, 10.4, "cortex", fontsize=10, color=GRAY, weight="bold", ha="center")
    save(fig, "fig_interoceptive_pathways.png")


def fig_affect_circumplex():
    """Figure 7.3: valence and arousal (positions approximate)."""
    fig, ax = plt.subplots(figsize=(7.2, 7.2)); ax.set_xlim(-1.45, 1.45); ax.set_ylim(-1.35, 1.35); ax.set_aspect("equal"); ax.axis("off")
    th = np.linspace(0, 2 * np.pi, 300); ax.plot(np.cos(th), np.sin(th), color="#cccccc", lw=1)
    arrow(ax, (-1.2, 0), (1.2, 0), color=GRAY, lw=1.2, style="<|-|>"); arrow(ax, (0, -1.15), (0, 1.15), color=GRAY, lw=1.2, style="<|-|>")
    ax.text(1.24, 0, "pleasant", va="center", fontsize=10, color=GREEN, weight="bold")
    ax.text(-1.24, 0, "unpleasant", va="center", ha="right", fontsize=10, color=INH, weight="bold")
    ax.text(0, 1.2, "activated", ha="center", fontsize=10, color=GRAY, weight="bold")
    ax.text(0, -1.22, "deactivated", ha="center", va="top", fontsize=10, color=GRAY, weight="bold")
    words = {"alarmed": 100, "afraid": 114, "angry": 127, "distressed": 145, "frustrated": 160,
             "sad": 200, "gloomy": 212, "bored": 235, "tired": 248, "sleepy": 262, "calm": 300, "relaxed": 315,
             "content": 330, "serene": 340, "pleased": 5, "happy": 14, "delighted": 33, "excited": 52, "aroused": 80}
    for w, deg in words.items():
        a = np.deg2rad(deg); x, y = np.cos(a), np.sin(a)
        col = GRAY if w in ("aroused", "sleepy", "tense") else GREEN if x > 0 else INH
        ax.plot(x, y, "o", color=col, ms=5)
        ax.text(x * 1.09, y * 1.09, w, fontsize=9, color=col, ha="left" if x > 0.1 else "right" if x < -0.03 else "center",
                va="bottom" if y > 0.1 else "top" if y < -0.1 else "center")
    ax.text(0.04, -0.06, "valence", fontsize=8.5, color=GRAY, ha="left", va="top", style="italic")
    ax.text(0.05, 0.62, "arousal", fontsize=8.5, color=GRAY, rotation=90, va="center", style="italic")
    save(fig, "fig_affect_circumplex.png")


def fig_threat_circuit():
    """Figure 7.4: fear conditioning circuit."""
    fig, ax = plt.subplots(figsize=(9, 5.4)); ax.set_xlim(0, 18); ax.set_ylim(0, 10.8); ax.axis("off")
    box(ax, 1.6, 8.6, 2.4, 1.0, "tone", fc="#f6f6f6", fs=9.5)
    box(ax, 1.6, 2.4, 2.4, 1.0, "shock", fc="#f6f6f6", fs=9.5)
    box(ax, 5.2, 8.6, 2.8, 1.1, "auditory\nthalamus", ec=EXC, color=EXC)
    box(ax, 8.8, 9.8, 2.8, 1.0, "auditory cortex", ec=EXC, color=EXC)
    box(ax, 5.2, 2.4, 2.8, 1.1, "pain pathways", ec=INH, color=INH)
    # amygdala outline
    ax.add_patch(FancyBboxPatch((8.0, 3.2), 4.4, 4.6, boxstyle="round,pad=0.15", fc="#fbf6e6", ec=GOLD, lw=1.5))
    ax.text(10.2, 7.45, "amygdala", ha="center", fontsize=10, color=GOLD, weight="bold")
    box(ax, 10.2, 6.1, 3.2, 1.0, "lateral nucleus", ec=EXC, color=EXC)
    box(ax, 10.2, 4.2, 3.2, 1.0, "central nucleus", ec=EXC, color=EXC)
    arrow(ax, (2.85, 8.6), (3.75, 8.6))
    arrow(ax, (6.65, 8.75), (7.35, 9.65), color=EXC); ax.text(6.4, 9.5, "slow,\ndetailed", fontsize=7.5, color=EXC, ha="right")
    arrow(ax, (9.6, 9.25), (10.0, 6.65), color=EXC)
    arrow(ax, (6.0, 8.0), (8.7, 6.45), color=EXC); ax.text(6.9, 7.05, "fast,\ncoarse", fontsize=7.5, color=EXC, ha="right")
    arrow(ax, (2.85, 2.4), (3.75, 2.4))
    arrow(ax, (6.65, 2.6), (8.9, 5.65), color=INH)
    arrow(ax, (10.2, 5.55), (10.2, 4.75), color=EXC, lw=2)
    outs = [("periaqueductal gray\n(freezing)", 9.0), ("hypothalamus\n(blood pressure,\nstress hormones)", 6.4), ("brainstem nuclei\n(norepinephrine,\nother modulators)", 3.8)]
    for txt, y in outs:
        box(ax, 15.7, y, 3.8, 1.5, txt, ec=GRAY, fs=8.5)
        arrow(ax, (11.85, 4.2), (13.75, y), color=GRAY)
    box(ax, 10.2, 1.0, 5.8, 1.0, "ventromedial prefrontal cortex", ec=GREEN, color=GREEN)
    arrow(ax, (10.2, 1.55), (10.2, 3.6), color=GREEN, style="-[", lw=1.8)
    ax.text(10.45, 2.25, "suppresses after extinction", fontsize=7.5, color=GREEN, ha="left", style="italic")
    save(fig, "fig_threat_circuit.png")


def fig_stress_axes():
    """Figure 7.5: sympathetic-adrenomedullary and HPA arms."""
    fig, ax = plt.subplots(figsize=(9, 5.2)); ax.set_xlim(0, 18); ax.set_ylim(0, 10.4); ax.axis("off")
    box(ax, 9.0, 9.4, 6.0, 1.0, "brain predicts a demand (cortex, amygdala)", fc="#f6f6f6", fs=9.5)
    box(ax, 9.0, 7.5, 4.0, 1.0, "hypothalamus", ec=EXC, color=EXC, weight="bold")
    arrow(ax, (9.0, 8.85), (9.0, 8.05))
    # fast arm (left)
    ax.text(3.6, 7.4, "fast: seconds", fontsize=10, color=INH, weight="bold", ha="center")
    box(ax, 3.6, 5.6, 4.4, 1.0, "sympathetic nerves", ec=INH, color=INH)
    box(ax, 3.6, 3.6, 4.4, 1.0, "adrenal medulla", ec=INH, color=INH)
    box(ax, 3.6, 1.5, 4.8, 1.3, "epinephrine: heart rate, blood\npressure, airways, glucose", fc="#fbeeee", ec=INH, color=INH, fs=8.5)
    arrow(ax, (7.0, 7.2), (5.0, 6.15), color=INH); arrow(ax, (3.6, 5.05), (3.6, 4.15), color=INH); arrow(ax, (3.6, 3.05), (3.6, 2.2), color=INH)
    # slow arm (right)
    ax.text(14.4, 7.4, "slow: tens of minutes", fontsize=10, color=EXC, weight="bold", ha="center")
    box(ax, 14.4, 5.6, 4.4, 1.0, "pituitary gland", ec=EXC, color=EXC)
    box(ax, 14.4, 3.6, 4.4, 1.0, "adrenal cortex", ec=EXC, color=EXC)
    box(ax, 14.4, 1.5, 4.8, 1.3, "cortisol: glucose, immune\nfunction, memory", fc="#e8eef5", ec=EXC, color=EXC, fs=8.5)
    arrow(ax, (11.0, 7.2), (13.0, 6.15), color=EXC); ax.text(12.4, 7.0, "CRH", fontsize=8.5, color=EXC)
    arrow(ax, (14.4, 5.05), (14.4, 4.15), color=EXC); ax.text(14.6, 4.6, "ACTH", fontsize=8.5, color=EXC)
    arrow(ax, (14.4, 3.05), (14.4, 2.2), color=EXC)
    # negative feedback loop
    arrow(ax, (11.95, 1.5), (9.6, 6.95), color=GREEN, ls="--", style="-[", cs="arc3,rad=-0.25", lw=1.5)
    ax.text(7.5, 2.9, "negative feedback\nto hypothalamus,\npituitary, hippocampus", fontsize=8, color=GREEN, ha="center", style="italic")
    save(fig, "fig_stress_axes.png")


def fig_inverted_u():
    """Figure 7.6: prefrontal function vs catecholamine level (illustrative)."""
    x = np.linspace(0, 10, 400)
    pfc = np.exp(-((x - 3.6) / 2.1) ** 2)
    habit = 1 / (1 + np.exp(-(x - 6.2) / 0.9)) * 0.9 + 0.05
    fig, ax = plt.subplots(figsize=(9, 4.4))
    ax.plot(x, pfc, color=EXC, lw=2.5, label="prefrontal working memory and flexible control")
    ax.plot(x, habit, color=INH, lw=2.5, ls="--", label="amygdala-driven and habitual responses")
    for xs, lab in [(1.0, "drowsy"), (3.6, "alert"), (8.6, "acute stress")]:
        ax.axvline(xs, color="#dddddd", lw=1, zorder=0); ax.text(xs, 1.08, lab, ha="center", fontsize=9, color=GRAY)
    ax.set_ylim(0, 1.15); ax.set_xlim(0, 10); ax.set_yticks([]); ax.set_xticks([])
    ax.set_xlabel("level of norepinephrine and dopamine in prefrontal cortex"); ax.set_ylabel("influence on behavior")
    ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    save(fig, "fig_inverted_u.png")


def fig_iowa_gambling():
    """Figure 7.7: Iowa gambling task payoffs (A) and illustrative choice curves (B)."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.4, 4.0), gridspec_kw={"width_ratios": [1, 1.25]})
    decks = ["A", "B", "C", "D"]; gain = [1000, 1000, 500, 500]; loss = [-1250, -1250, -250, -250]
    xs = np.arange(4)
    a1.bar(xs, gain, color=[INH, INH, GREEN, GREEN], alpha=0.35, width=0.6, label="winnings")
    a1.bar(xs, loss, color=[INH, INH, GREEN, GREEN], width=0.6, label="penalties")
    for i in range(4):
        net = gain[i] + loss[i]
        a1.text(xs[i], gain[i] + 60, f"net {net:+d}", ha="center", fontsize=8.5, color=INH if net < 0 else GREEN, weight="bold")
    a1.axhline(0, color=GRAY, lw=0.8); a1.set_xticks(xs); a1.set_xticklabels([f"deck {d}" for d in decks])
    a1.set_ylabel("dollars per 10 cards (play money)"); a1.set_ylim(-1500, 1300)
    a1.set_title("A", loc="left", weight="bold"); a1.spines[["top", "right"]].set_visible(False)
    a1.text(0.5, -1420, "bad decks", ha="center", fontsize=8.5, color=INH); a1.text(2.5, -1420, "good decks", ha="center", fontsize=8.5, color=GREEN)
    blocks = np.arange(1, 6)
    ctrl = [4.2, 5.6, 6.6, 7.3, 7.6]; pat = [4.4, 4.0, 3.9, 4.2, 4.0]
    a2.plot(blocks, ctrl, "o-", color=EXC, lw=2, label="healthy players")
    a2.plot(blocks, pat, "s--", color=INH, lw=2, label="ventromedial prefrontal damage")
    a2.axhline(5, color=GRAY, ls=":", lw=1); a2.text(5.15, 5.05, "chance", fontsize=8, color=GRAY, va="bottom", ha="right")
    a2.set_xticks(blocks); a2.set_xticklabels([f"{20*(b-1)+1}-{20*b}" for b in blocks], fontsize=8.5)
    a2.set_xlabel("trials"); a2.set_ylabel("good-deck choices per 10 cards"); a2.set_ylim(2, 9)
    a2.legend(frameon=False, loc="upper left", fontsize=9); a2.set_title("B", loc="left", weight="bold")
    a2.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); save(fig, "fig_iowa_gambling.png")


if __name__ == "__main__":
    for f in (fig_reactive_predictive, fig_interoceptive_pathways, fig_affect_circumplex, fig_threat_circuit,
              fig_stress_axes, fig_inverted_u, fig_iowa_gambling):
        f()
    print("figures written to", OUT)
