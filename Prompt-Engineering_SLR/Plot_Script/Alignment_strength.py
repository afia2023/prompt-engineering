import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------
# 1. Data
# ----------------------------------
categories = ["Human ↔ LLM", "NL Metrics ↔ LLM", "NL Metrics ↔ Human"]
strong = np.array([7, 2, 3])
weak = np.array([0, 1, 4])
not_assessed = np.array([7, 11, 7])

y_pos = np.arange(len(categories))

# ----------------------------------
# 2. Figure setup
# ----------------------------------
fig, ax = plt.subplots(figsize=(8, 5.8))  # slightly taller

# ----------------------------------
# 3. Colors
# ----------------------------------
colors = {
    "Strong": "#4B74B1",
    "Weak": "#D97C49",
    "Not": "#C5BBB3"
}

# ----------------------------------
# 4. Horizontal stacked bars
# ----------------------------------
ax.barh(y_pos, strong, color=colors["Strong"], label="Strong Alignment")
ax.barh(y_pos, weak, left=strong, color=colors["Weak"], label="Weak Alignment")
ax.barh(y_pos, not_assessed, left=strong + weak, color=colors["Not"], label="Not Assessed")

# ----------------------------------
# 5. Labels inside bars
# ----------------------------------
for i in range(len(categories)):
    ax.text(strong[i]/2, i, str(strong[i]), va='center', ha='center',
            color='black', fontsize=11, fontweight='bold')
    if weak[i] > 0:
        ax.text(strong[i] + weak[i]/2, i, str(weak[i]), va='center', ha='center',
                color='black', fontsize=10, fontweight='bold')
    ax.text(strong[i] + weak[i] + not_assessed[i]/2, i, str(not_assessed[i]),
            va='center', ha='center', color='black', fontsize=11, fontweight='bold')

# ----------------------------------
# 6. Axes labels
# ----------------------------------
ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=11, fontweight='bold', color='black')
ax.set_xlabel("Number of Studies", fontsize=11, fontweight='bold', color='black', labelpad=18)

# ----------------------------------
# 7. Legend (moved slightly lower and with more space)
# ----------------------------------
legend = ax.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, -0.15),  # more space below
    ncol=3,
    fontsize=10,
    frameon=False,
    handlelength=1.5,
    handletextpad=0.8,
    columnspacing=1.5
)
for text in legend.get_texts():
    text.set_fontweight('bold')
    text.set_color('#111111')

# ----------------------------------
# 8. Aesthetic touches
# ----------------------------------
ax.grid(axis="x", linestyle="--", alpha=0.4, color='gray')
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_color('black')
ax.tick_params(colors='black', labelsize=10)

# Adjust layout (increase bottom margin)
plt.tight_layout(rect=[0, 0.08, 1, 1])
plt.savefig("alignment_strength_distribution1.pdf", format="pdf", bbox_inches="tight", pad_inches=0.3)


# ----------------------------------
# 9. Show
# ----------------------------------
plt.show()
