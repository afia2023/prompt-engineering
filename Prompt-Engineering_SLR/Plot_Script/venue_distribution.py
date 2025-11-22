import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------
# 1. Aggregated venue data (27 total)
# ----------------------------------
venue_counts = {
    "ICSE": 6,
    "ASE": 5,
    "FSE": 2,
    "JSS": 1,
    "ITOEC": 1,
    "ICSME": 1,
    "TSE": 1,
    "IJCAI": 1,
    "ICLR": 1,
    "EMNLP": 1,
    "COMPSAC": 1,
    "MSR": 1,
    "ACL": 2,
    "SANER": 1,
    "arXiv": 2
}

venues = list(venue_counts.keys())
counts = list(venue_counts.values())

# ----------------------------------
# 2. Polar bar setup
# ----------------------------------
N = len(venues)
theta = np.linspace(0, 2 * np.pi, N, endpoint=False)
radii = counts
width = 2 * np.pi / N * 0.88

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})
colors = plt.cm.tab20.colors

bars = ax.bar(
    theta, radii, width=width, bottom=0.0,
    edgecolor='white', linewidth=1, zorder=3,
    color=[colors[i % 20] for i in range(N)]
)

# ----------------------------------
# 3. Remove gridlines and ticks
# ----------------------------------
ax.set_xticks([])
ax.set_yticks([])
ax.spines['polar'].set_visible(False)
ax.grid(False)

# # ----------------------------------
# 4. Label connectors (shorter lines)
# ----------------------------------
label_radius = max(radii) + 0.8
tail_length = 0.8

for i, (angle, radius) in enumerate(zip(theta, radii)):
    color = colors[i % 20]

    x0, y0 = label_radius * np.cos(angle), label_radius * np.sin(angle)

    angle_perp = angle + (np.pi / 2)
    x1 = x0 + tail_length * np.cos(angle_perp)
    y1 = y0 + tail_length * np.sin(angle_perp)

    ax.plot([angle, angle], [radius, label_radius], color=color, lw=2)
    ax.plot([x0, x1], [y0, y1], color=color, lw=2, transform=ax.transData._b)

    ha = 'left' if np.cos(angle_perp) > 0 else 'right'

    # --- ADD LABEL SPACING ---
    label_offset = 0.35
    x_text = x1 + label_offset * np.cos(angle_perp)
    y_text = y1 + label_offset * np.sin(angle_perp)

    ax.text(
        np.arctan2(y_text, x_text),
        np.hypot(x_text, y_text),
        venues[i],
        fontsize=13,
        fontweight='bold',
        color='black',
        ha=ha,
        va='center',
        rotation=0,
        rotation_mode='anchor',
        zorder=4
    )

# ----------------------------------
# 5. Save and show
# ----------------------------------
plt.tight_layout()
plt.savefig("venue_distribution.pdf", format="pdf", bbox_inches="tight", pad_inches=0.4)
plt.show()
