#!/usr/bin/env python3
"""Regenerate the drawn figures for Chapter 14 (Implications for Learning, Work, and Technology). Outputs into ./images.
Requires matplotlib and numpy. Figures 14.3 and 14.5 are computed; Figures 14.2, 14.4, and 14.6 plot published data."""
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


# Spacing model (illustrative). Retrievability falls as a power function of time, R = 1 / (1 + t / (9 S)),
# where S is the memory's stability in days. A successful restudy multiplies stability by more the more had
# been forgotten (a desirable difficulty); a failed one leaves the memory as it was after the first session.
# Parameters were chosen to approximate the optimal gaps measured by Cepeda et al. (2008).
CEPEDA = {7: 3, 35: 8, 70: 12, 350: 27}   # optimal gaps (days) interpolated by Cepeda et al. (2008)
S0, A, B, C = 2.0, 4.0, 4.0, 1.0
R = lambda t, S: 1 / (1 + t / (9 * S))


def retention(gap, ri):
    r = R(gap, S0)
    s_ok = S0 * (1 + A * (np.exp(B * (1 - r)) - 1))
    return r * R(ri, s_ok) + (1 - r) * R(ri, S0 * C)


def fig_spacing():
    gaps = np.linspace(0.01, 120, 12000)
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.8, 3.9))
    best = {}
    for ri, c in [(7, GOLD), (35, EXC), (350, INH)]:
        f = retention(gaps, ri); i = f.argmax(); best[ri] = (gaps[i], f[i], retention(0.01, ri))
        a.plot(gaps, f, color=c, lw=2, label=f"test {ri} days after the second session")
        a.plot(gaps[i], f[i], "o", color=c)
    a.set_xscale("log"); a.set_xlim(0.1, 120)
    a.set_xlabel("gap between the two study sessions (days, log scale)"); a.set_ylabel("proportion remembered at the test")
    a.set_title("A. Too soon wastes the second session; too late finds\nthe memory gone", fontsize=10, loc="left")
    a.legend(frameon=False, fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=1); clean(a)
    ris = np.array([3, 7, 14, 35, 70, 175, 350]); opt = []
    for ri in ris:
        f = retention(gaps, ri); opt.append(gaps[f.argmax()])
    opt = np.array(opt)
    b.loglog(ris, opt, "o-", color=EXC, lw=2, label="model")
    b.loglog(list(CEPEDA), list(CEPEDA.values()), "s", color=GOLD, ms=8, label="measured (Cepeda et al., 2008)")
    b.legend(frameon=False, fontsize=8, loc="upper left")
    for ri, g in zip(ris, opt):
        off = {7: (6, -22), 35: (8, -22), 350: (-50, -36)}
        if ri in off:
            b.annotate(f"model: {g:.1f} days\n({100 * g / ri:.0f}% of {ri})", (ri, g), xytext=off[ri], textcoords="offset points", fontsize=8)
    from matplotlib.ticker import FixedLocator, NullFormatter, ScalarFormatter
    b.yaxis.set_major_locator(FixedLocator([3, 5, 10, 20, 30])); b.yaxis.set_major_formatter(ScalarFormatter()); b.yaxis.set_minor_formatter(NullFormatter())
    b.xaxis.set_major_locator(FixedLocator([3, 7, 35, 350])); b.xaxis.set_major_formatter(ScalarFormatter()); b.xaxis.set_minor_formatter(NullFormatter())
    b.set_ylim(2.5, 40)
    b.set_xlabel("time from second session to test (days, log scale)"); b.set_ylabel("best gap (days, log scale)")
    b.set_title("B. The best gap grows with the time to the test,\nbut as a shrinking fraction of it", fontsize=10, loc="left"); clean(b)
    fig.tight_layout(); save(fig, "fig_spacing.png")
    return {k: tuple(round(float(x), 2) for x in v) for k, v in best.items()}, dict(zip(ris.tolist(), np.round(opt, 1).tolist()))


def skill_run(f, days=730, rate=0.02, decay=0.004, tasks=20, seed=0):
    """A skill that improves with each manual repetition and decays without use; automation takes over a
    fraction f of the day's tasks. Returns the skill each day (illustrative)."""
    s = 0.9; out = []
    for d in range(days):
        manual = tasks * (1 - f)
        s = s + rate * manual * (1 - s) / tasks * 5
        s = s - decay * s
        s = min(max(s, 0), 1); out.append(s)
    return np.array(out)


def fig_automation():
    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    res = {}
    for f, c in [(0.0, EXC), (0.5, GOLD), (0.9, INH), (0.99, GRAY)]:
        s = skill_run(f); res[f] = (round(s[364], 2), round(s[-1], 2))
        ax.plot(np.arange(len(s)) / 365, s, color=c, lw=2, label=f"automation handles {int(f * 100)}% of tasks")
    ax.set_ylim(0, 1); ax.set_xlabel("years after automation is introduced"); ax.set_ylabel("operator's skill (illustrative)")
    ax.legend(frameon=False, fontsize=8.5, loc="lower left"); clean(ax)
    fig.tight_layout(); save(fig, "fig_automation.png")
    return res



def fig_tutor():
    """Bastani et al. (2025): grades relative to the control group, during AI-assisted practice and on the
    later exam taken without AI. Percentages from the paper's abstract; the GPT Tutor exam effect was not
    statistically distinguishable from zero."""
    fig, ax = plt.subplots(figsize=(6.6, 3.9))
    x = np.array([0, 1]); w = 0.36
    base = [48, -17]; tutor = [127, 0]
    ax.bar(x - w / 2, base, w, color=INH, label="unrestricted chatbot (GPT Base)")
    ax.bar(x + w / 2, tutor, w, color=EXC, label="tutor that gives hints, not answers (GPT Tutor)")
    for xi, v in zip(x - w / 2, base):
        ax.text(xi, v + (4 if v >= 0 else -11), f"{v:+d}%", ha="center", fontsize=9)
    ax.text(x[0] + w / 2, 131, "+127%", ha="center", fontsize=9)
    ax.text(x[1] + w / 2, 4, "no significant\ndifference", ha="center", fontsize=8.5)
    ax.axhline(0, color=GRAY, lw=1)
    ax.set_xticks(x); ax.set_xticklabels(["practice sessions\n(with AI)", "exam\n(AI taken away)"])
    ax.set_ylabel("grades relative to students\nwithout AI (%)"); ax.set_ylim(-30, 150)
    ax.legend(frameon=False, fontsize=8.5, loc="upper right"); clean(ax)
    fig.tight_layout(); save(fig, "fig_tutor.png")



def fig_kuhl():
    """Kuhl, Tsao & Liu (2003): Mandarin discrimination at about 10 to 12 months. Live and English-control
    values (with standard errors) are from the text; the video, audio-only, and Taiwanese values are read
    approximately from the paper's Figure 2."""
    fig, ax = plt.subplots(figsize=(7.2, 3.9))
    labels = ["live Mandarin\nspeakers", "same speakers\non video", "audio\nonly", "English\n(control)", "Taiwanese infants\n(learning Mandarin)"]
    vals = [65.7, 56.5, 56.5, 56.7, 68]; err = [2.4, 0, 0, 2.29, 0]
    cols = [EXC, INH, INH, GRAY, GOLD]
    x = np.arange(len(vals))
    ax.bar(x, vals, color=cols, width=0.65, yerr=[e if e else np.nan for e in err], capsize=4)
    for xi, v, e in zip(x, vals, err):
        ax.text(xi, v + (e or 0) + 1, f"{v:.1f}" if e else f"about {v:.0f}", ha="center", fontsize=8.5)
    ax.axhline(50, color=GRAY, ls=":", lw=1); ax.text(-0.42, 51, "chance", fontsize=8, color=GRAY, ha="left")
    ax.set_ylim(0, 80); ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylabel("Mandarin sounds told apart\n(percent correct)"); clean(ax)
    fig.tight_layout(); save(fig, "fig_kuhl.png")


def fig_kornell():
    """Kornell & Bjork (2008), Experiment 1a: painters' styles learned with spaced (interleaved) or massed
    (blocked) presentation; first test block, and participants' judgments of which had worked better."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(8.6, 3.6), gridspec_kw={"width_ratios": [1, 1.25]})
    a.bar([0, 1], [61, 35], color=[EXC, INH], width=0.6)
    for xi, v in zip([0, 1], [61, 35]):
        a.text(xi, v + 1.5, f"{v}%", ha="center", fontsize=9)
    a.set_xticks([0, 1]); a.set_xticklabels(["paintings\ninterleaved", "paintings\nblocked"])
    a.set_ylim(0, 75); a.set_ylabel("new paintings assigned\nto the right artist (%)")
    a.set_title("A. What happened", fontsize=10, loc="left"); clean(a)
    b.barh([1, 0], [78, 78], color=[EXC, INH], height=0.55)
    b.set_yticks([1, 0]); b.set_yticklabels(["did better with\ninterleaving", "judged blocking as\ngood or better"], fontsize=9)
    for y in (1, 0):
        b.text(79.5, y, "78%", va="center", fontsize=9)
    b.set_xlim(0, 100); b.set_xlabel("participants (%)")
    b.set_title("B. What learners believed", fontsize=10, loc="left"); clean(b)
    fig.tight_layout(); save(fig, "fig_kornell.png")



MAP = [("memories consolidate slowly,\noffline, and in sleep", "space study; protect sleep;\nlater school start", "5"),
       ("retrieval and prediction\nerror rewrite memories", "test rather than reread;\nlet learners guess first", "5, 12"),
       ("learning from other people", "live teachers and partners;\ntutors that respond", "14"),
       ("attention and effort are\nlimited and costly", "fewer switches and interruptions;\nlimits on long, hard work", "1, 8"),
       ("practice builds specific\nroutines; disuse lets them fade", "keep people practiced when\nmachines do the work", "9"),
       ("reward learning shapes habits", "know what a design is\ntraining you to do", "3, 8, 9"),
       ("the brain reshapes itself\naround what it does", "tools change the skills they\nreplace; keep learning", "1, 5, 9")]


def fig_map():
    fig, ax = plt.subplots(figsize=(9.6, 6.6)); ax.set_xlim(0, 10); ax.set_ylim(-0.1, 7.6); ax.axis("off")
    ax.text(2.0, 7.3, "feature of the brain", ha="center", fontsize=10, weight="bold", color=GRAY)
    ax.text(6.6, 7.3, "what it implies", ha="center", fontsize=10, weight="bold", color=GRAY)
    ax.text(9.4, 7.3, "chapters", ha="center", fontsize=10, weight="bold", color=GRAY)
    for i, (f, imp, ch) in enumerate(MAP):
        y = 6.6 - i * 0.98
        box(ax, 2.0, y, 3.4, 0.72, f, fc="#e8eef5", ec=EXC, fs=8.8)
        arrow(ax, (3.8, y), (4.65, y), color=EXC)
        box(ax, 6.6, y, 3.5, 0.72, imp, fc="#f6efd6", ec=GOLD, fs=8.8)
        ax.text(9.4, y, ch, ha="center", va="center", fontsize=9, color=GRAY)
    fig.tight_layout(); save(fig, "fig_map.png")


LEDGER = [("Strong (laboratory and classroom)", EXC,
           ["retrieval practice (quizzing)", "spacing study over time", "interleaving kinds of problems", "the cost of switching between tasks"]),
          ("Supported, with caveats", GRAY,
           ["later school start times (observational)", "skill loss under automation (observational)",
            "small average effects of social media on well-being", "infants learning from partners who respond (small studies)"]),
          ("Small, disputed, or early", GOLD,
           ["growth-mindset interventions", "exercise and the hippocampus", "satellite navigation and spatial memory",
            "AI tutors that guide rather than answer (early)", "a phone's presence (at most a small effect)", "heavy media multitasking"]),
          ("Not supported", INH,
           ["teaching to learning styles", "brain training that transfers", "the Mozart effect", "longhand notes beating laptop notes",
            "willpower used up within minutes"])]


def fig_ledger():
    fig, ax = plt.subplots(figsize=(9.6, 5.6)); ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    for i, (title, c, items) in enumerate(LEDGER):
        x0 = 0.15 + (i % 2) * 5.0; y0 = 9.7 - (i // 2) * 4.9
        ax.add_patch(FancyBboxPatch((x0, y0 - 4.5), 4.7, 4.5, boxstyle="round,pad=0.05", fc="white", ec=c, lw=1.8))
        ax.text(x0 + 0.2, y0 - 0.45, title, fontsize=10.5, weight="bold", color=c, va="center")
        step = min(0.8, 3.3 / len(items))
        for j, it in enumerate(items):
            ax.text(x0 + 0.3, y0 - 1.15 - j * step, "\u2022 " + it, fontsize=9, va="center")
    fig.tight_layout(); save(fig, "fig_ledger.png")


if __name__ == "__main__":
    fig_map(); fig_ledger()
    fig_kuhl(); fig_kornell()
    fig_tutor()
    print("spacing", fig_spacing())
    print("automation", fig_automation())
