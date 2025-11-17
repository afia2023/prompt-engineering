import matplotlib.pyplot as plt

# =======================
# Verified artifact data
# =======================
categories = [
    "Preprocessing/Extraction Scripts",
    "Prompt Construction/Selection Scripts",
    "Training/Evaluation Scripts",
    "Datasets/Corpora",
    "Environment Files",
    "Documentation/Instructions (incl. Usage Examples)",
    "Tools/Extensions",
    "Model Weights",
    "No Repository"
]
counts = [6, 3, 6, 4, 1, 4, 2, 1, 11]

# =======================
# Softer professional color palette
# =======================
colors = [
    "#4F81BD", "#9BBB59", "#F79646", "#C0504D",
    "#8064A2", "#4BACC6", "#A2A2A2", "#77933C", "#B29200"
]

# =======================
# Global font & export settings
# =======================
plt.rcParams.update({
    'font.size': 12,            # match Overleaf body text
    'font.weight': 'bold',
    'axes.labelcolor': '#000000',
    'text.color': '#000000',
    'pdf.fonttype': 42,         # keep text as vector
    'ps.fonttype': 42
})

# =======================
# Figure setup
# =======================
fig, ax = plt.subplots(figsize=(5.8, 5.8))  # square for symmetry

def absolute_value(pct, allvals):
    total = sum(allvals)
    val = int(round(pct * total / 100.0))
    return f"{val}"

wedges, texts, autotexts = ax.pie(
    counts,
    labels=None,
    autopct=lambda pct: absolute_value(pct, counts),
    startangle=90,
    colors=colors,
    pctdistance=0.78,
    textprops={'fontsize': 12, 'color': '#000000', 'weight': 'bold'}
)

# Donut hole
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
ax.add_artist(centre_circle)

# =======================
# Legend below the donut
# =======================
ax.legend(
    wedges,
    categories,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.28),  # fine-tuned for balance
    ncol=3,
    fontsize=11,                  # larger for readability
    frameon=False,
    columnspacing=1.8,
    handlelength=1.3,
    handletextpad=0.8
)

# =======================
# Layout & export
# =======================
ax.axis('equal')
plt.subplots_adjust(top=0.93, bottom=0.30)
plt.margins(0, 0)

# Save high-quality outputs
plt.savefig("artifact_sharing_landscape.pdf", format="pdf",
            bbox_inches="tight", transparent=True, dpi=600)
plt.savefig("artifact_sharing_landscape.png", format="png",
            bbox_inches="tight", dpi=600)

plt.show()
print("Saved: artifact_sharing_landscape.pdf and artifact_sharing_landscape.png")
