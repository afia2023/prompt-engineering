import matplotlib.pyplot as plt
import numpy as np

# ------------------ Data ------------------
language_shares = {
    "Zero-shot": {"Python": 24, "Java": 36, "JavaScript": 8, "PHP": 8, "Go": 8, "Ruby": 8, "Other": 8},
    "Few-shot": {"Python": 30, "Java": 20, "JavaScript": 10, "PHP": 10, "Go": 10, "Ruby": 10, "Other": 10},
    "RAG": {"Python": 22, "Java": 27, "JavaScript": 9, "PHP": 9, "Go": 9, "Ruby": 9, "C/C++": 15},
    "Chain-of-Thought": {"Python": 33, "Java": 33, "Other": 34},
}

# ------------------ Brighter Color Palette ------------------
colors = {
    "Python": "#64B5F6",      # bright blue
    "Java": "#FF8A80",        # bright red-pink
    "JavaScript": "#FFD54F",  # bright yellow
    "PHP": "#BA68C8",         # bright purple
    "Go": "#81C784",          # bright green
    "Ruby": "#FFB74D",        # bright orange
    "C/C++": "#4DD0E1",       # bright cyan
    "Other": "#E0E0E0"        # light grey
}

# ------------------ Chart setup ------------------
paradigms = list(language_shares.keys())
radius_step = 0.23   # slightly smaller to balance 12pt text
current_radius = 1.0
fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(aspect="equal"))

# Global font and vector settings
plt.rcParams.update({
    'font.size': 12,            # uniform font size across the figure
    'font.weight': 'bold',
    'axes.labelcolor': '#000000',
    'text.color': '#000000',
    'pdf.fonttype': 42,         # keep fonts as vector text (not paths)
    'ps.fonttype': 42
})

language_angle_map = {lang: [] for lang in colors.keys()}
start_angle = 90

# ------------------ Pie layers ------------------
for paradigm in paradigms:
    data = language_shares[paradigm]
    langs, sizes = list(data.keys()), list(data.values())
    total = sum(sizes)
    current_angle = start_angle

    for lang, size in zip(langs, sizes):
        theta1, theta2 = current_angle, current_angle - (size / total) * 360
        language_angle_map[lang].append((theta1, theta2, current_radius - radius_step / 2))
        current_angle = theta2

    wedges, _ = ax.pie(
        sizes, radius=current_radius,
        colors=[colors[l] for l in langs],
        startangle=start_angle, counterclock=False,
        wedgeprops=dict(width=radius_step, edgecolor="#FFFFFF", linewidth=0.8),
    )

    # Paradigm text placement
    if paradigm == "Chain-of-Thought":
        y_offset = radius_step * 0.42
        label_text = "CoT"  # shortened for fit
    else:
        y_offset = radius_step * 0.5
        label_text = paradigm

    ax.text(0, current_radius - y_offset, label_text,
            ha="center", va="center", fontsize=12, fontweight='bold', color="#000000")
    current_radius -= radius_step

# ------------------ Center Label ------------------
centre_circle = plt.Circle((0, 0), current_radius + 0.05, color='white')
ax.add_artist(centre_circle)
ax.text(0, 0, "Language\nCoverage\n(%)",
        ha='center', va='center', fontsize=12, fontweight='bold', color="#000000")

# ------------------ Connector lines and outer labels ------------------
for lang, segs in language_angle_map.items():
    if not segs:
        continue
    theta1, theta2, ring_mid = segs[0]
    mid_angle = np.deg2rad((theta1 + theta2) / 2)
    x_inner, y_inner = np.cos(mid_angle) * ring_mid, np.sin(mid_angle) * ring_mid
    x_mid, y_mid = np.cos(mid_angle) * 1.1, np.sin(mid_angle) * 1.1
    horiz_shift = 0.1 if np.cos(mid_angle) > 0 else -0.1
    x_end, y_end = x_mid + horiz_shift, y_mid

    ax.plot([x_inner, x_mid], [y_inner, y_mid], color=colors[lang], lw=1.2)
    ax.plot([x_mid, x_end], [y_mid, y_end], color=colors[lang], lw=1.2)

    ax.text(x_end + (0.045 if np.cos(mid_angle) > 0 else -0.045), y_end,
            lang, ha='left' if np.cos(mid_angle) > 0 else 'right',
            va='center', fontsize=12, fontweight='bold', color="#000000")

# ------------------ Save and Show ------------------
plt.tight_layout()
plt.savefig("Language_distribution_Piechart.pdf",
            format="pdf", bbox_inches="tight", transparent=True, dpi=600)
plt.show()
