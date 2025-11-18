import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np

# ---------------------------------------
# Data
# ---------------------------------------
entries = [
    (
        "Zero-shot",
        "BLEU-family: 90%\n"
        "ROUGE-L: 50%, METEOR: 20%\n"
        "10% with no NL metrics"
    ),
    (
        "Few-shot",
        "BLEU-family: 33%\n"
        "Accuracy / ASR: 33%\n"
        "33% with no NL metrics"
    ),
    (
        "RAG",
        "BLEU-family: 88%\n"
        "ROUGE-L: 75%, METEOR: 63%\n"
        "13% with no NL metrics"
    ),
    (
        "CoT",
        "Precision / F1 / LLM accuracy: 50%\n"
        "50% qualitative only"
    ),
    (
        "Hybrid",
        "BLEU-family: 100%\n"
        "ROUGE-L & METEOR: 75%\n"
        "Semantic metrics (BERTScore / SIDE): 25%"
    ),
]

circle_colors = ["#B8E3DF", "#C6C5F5", "#F3D9C4", "#E0B894", "#F6E0A6"]
box_colors    = ["#E4F8F4", "#E6E5FF", "#FBE9DD", "#F3DCC8", "#FFF2C9"]

# ---------------------------------------
# Figure setup
# ---------------------------------------
fig, ax = plt.subplots(figsize=(11, 7))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.axis("off")

ax.set_xlim(0, 12)
ax.set_ylim(0, 12)

# ---------------------------------------
# Curved spine (we'll place circles ON this curve)
# ---------------------------------------
t = np.linspace(0, 1, 300)
y_curve = 11.5 - 9 * t
x_curve = 4.0 + 0.55 * np.sin((t - 0.5) * np.pi)  # gentle S / C shape

ax.plot(x_curve, y_curve, color="#444444", linewidth=1.6, zorder=1)

# t positions for the 5 nodes
t_nodes = np.linspace(0.12, 0.88, len(entries))

circle_radius = 0.55
box_gap = 0.5      # gap from circle edge to box
box_width = 6.0
box_height = 1.15

start_number = 1   # change to 11 if you want 11–15

for k, ((title, text), tt) in enumerate(zip(entries, t_nodes)):
    # circle center exactly ON the spine
    cx = 4.0 + 0.55 * np.sin((tt - 0.5) * np.pi)
    cy = 11.5 - 9 * tt

    # ---- Circle with number ----
    circ = Circle(
        (cx, cy),
        circle_radius,
        facecolor=circle_colors[k],
        edgecolor="#404040",
        linewidth=1.0,
        zorder=3,
    )
    ax.add_patch(circ)

    ax.text(
        cx,
        cy,
        str(start_number + k),
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#000000",
        zorder=4,
    )

    # ---- Box to the right ----
    box_x = cx + circle_radius + box_gap
    box = FancyBboxPatch(
        (box_x, cy - box_height / 2),
        box_width,
        box_height,
        boxstyle="round,pad=0.3,rounding_size=0.08",
        linewidth=0.8,
        facecolor=box_colors[k],
        edgecolor="#C0C0C0",
        zorder=2,
    )
    ax.add_patch(box)

    # Box title
    ax.text(
        box_x + 0.35,
        cy + 0.25,
        title,
        ha="left",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#000000",
        zorder=4,
    )

    # Box body text
    ax.text(
        box_x + 0.35,
        cy - 0.05,
        text,
        ha="left",
        va="top",
        fontsize=9,
        color="#000000",
        zorder=4,
    )

# ---------------------------------------
# Left title: NL Metrics
# ---------------------------------------
# Place around the middle circle vertically
mid_tt = t_nodes[len(t_nodes)//2]
mid_y = 11.5 - 9 * mid_tt

ax.text(
    0.8,
    mid_y,
    "NL Metrics",
    ha="left",
    va="center",
    fontsize=24,
    fontweight="bold",
    color="#4A4A4A",
)

plt.tight_layout()
plt.savefig("nl_metrics_final_style.png", dpi=300, bbox_inches="tight")
plt.savefig("nl_metrics_final_style.svg", format="svg", bbox_inches="tight")
plt.show()
