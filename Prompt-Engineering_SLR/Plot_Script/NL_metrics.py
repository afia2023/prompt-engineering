import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np

# ---------------------------------------
# Data - Strictly matched to Table Sections
# ---------------------------------------
entries = [
    (
        "Zero-shot (n=9)",
        "BLEU-family: 88.9%\n"
        "ROUGE-L: 55.6%, METEOR: 22.2%\n"
        "11.1% with no NL metrics"
    ),
    (
        "Few-shot (n=3)",
        "BLEU-family: 33%\n"
        "Accuracy / ASR: 33%\n"
        "33% with no NL metrics"
    ),
    (
        "RAG (n=4)",
        "BLEU-family: 75%\n"
        "ROUGE-L: 62.5%, METEOR: 50%\n"
        "25% with no NL metrics"
    ),
    (
        "CoT (n=1)",
        "Precision / F1 / LLM accuracy: 100%"
    ),
    (
        "Hybrid (n=12)",
        "BLEU-family: 83.3%\n"
        "ROUGE-L & METEOR: 83.3%\n"
        "Semantic metrics: 25%\n"
        "Surface (Readability/TF-IDF/Length): 16.7%"
    ),
]

circle_colors = ["#B8E3DF", "#C6C5F5", "#F3D9C4", "#E0B894", "#F6E0A6"]
box_colors    = ["#E4F8F4", "#E6E5FF", "#FBE9DD", "#F3DCC8", "#FFF2C9"]

# ---------------------------------------
# Figure setup
# ---------------------------------------
fig, ax = plt.subplots(figsize=(11, 8))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.axis("off")

ax.set_xlim(0, 12)
ax.set_ylim(0, 12)

# Curved spine
t = np.linspace(0, 1, 300)
y_curve = 11.5 - 9 * t
x_curve = 4.0 + 0.55 * np.sin((t - 0.5) * np.pi)
ax.plot(x_curve, y_curve, color="#444444", linewidth=1.6, zorder=1)

t_nodes = np.linspace(0.12, 0.88, len(entries))
circle_radius = 0.55
box_gap = 0.5
box_width = 6.2
box_height = 1.45 

start_number = 1

# ---------------------------------------
# Draw circles + boxes
# ---------------------------------------
for k, ((title, text), tt) in enumerate(zip(entries, t_nodes)):
    cx = 4.0 + 0.55 * np.sin((tt - 0.5) * np.pi)
    cy = 11.5 - 9 * tt

    # Circle
    circ = Circle((cx, cy), circle_radius, facecolor=circle_colors[k],
                  edgecolor="#404040", linewidth=1.0, zorder=3)
    ax.add_patch(circ)
    ax.text(cx, cy, str(start_number + k), ha="center", va="center",
            fontsize=11, fontweight="bold", color="#000000", zorder=4)

    # Box
    box_x = cx + circle_radius + box_gap
    box = FancyBboxPatch((box_x, cy - box_height / 2), box_width, box_height,
                        boxstyle="round,pad=0.3,rounding_size=0.08",
                        linewidth=0.8, facecolor=box_colors[k],
                        edgecolor="#C0C0C0", zorder=2)
    ax.add_patch(box)

    # Box title
    ax.text(box_x + 0.45, cy + box_height / 2 - 0.30, title,
            ha="left", va="center", fontsize=11, fontweight="bold", zorder=4)

    # Box body text with logic for Hybrid offset
    text_offset = 0.55
    if k == len(entries) - 1: # Hybrid box
        text_offset = 0.45

    ax.text(box_x + 0.45, cy + box_height / 2 - text_offset, text,
            ha="left", va="top", fontsize=10, color="#000000", zorder=4, linespacing=1.3)

# Label
ax.text(0.5, 6.0, "NL Metric Usage\nBy Category", ha="left", va="center",
        fontsize=20, fontweight="bold", color="#4A4A4A")

plt.tight_layout()
plt.savefig("nl_metrics_final_style.png", dpi=350, bbox_inches="tight")
plt.savefig("nl_metrics_final_style.svg", format="svg", bbox_inches="tight")
plt.show()