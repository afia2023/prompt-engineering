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

# Soft, journal-style palette
colors = [
    "#4F81BD", "#9BBB59", "#F79646", "#C0504D",
    "#8064A2", "#4BACC6", "#A2A2A2", "#77933C", "#B29200"
]

fig, ax = plt.subplots(figsize=(5.5, 5.5))  # square keeps the donut centered

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
    textprops={'fontsize': 10, 'color': 'black', 'weight': 'bold'}
)

# Donut hole
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
ax.add_artist(centre_circle)

# =======================
# Legend under the donut (lowered to prevent overlap)
# =======================
ax.legend(
    wedges,
    categories,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.25),   # moved slightly lower
    ncol=3,
    fontsize=9,
    frameon=False,
    columnspacing=1.5,
    handlelength=1.2,
    handletextpad=0.6
)

# =======================
# Layout adjustments
# =======================
ax.axis('equal')
plt.subplots_adjust(top=0.92, bottom=0.30)  # more bottom space, no overlap
plt.margins(0, 0)

plt.savefig("artifact_sharing_landscape.pdf", bbox_inches='tight')
plt.show()
