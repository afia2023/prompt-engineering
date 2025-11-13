# replication_availability_chart_small_fonts.py
# Same style, slightly smaller fonts, non-bold look for ACM

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# ---------------- rcParams tuned for ACM figures ----------------
mpl.rcParams['svg.fonttype'] = 'none'   # keep text as text in SVG/PDF
mpl.rcParams.update({
    "font.family": "serif",            # Times/serif to match ACM papers
    "font.serif": ["Times New Roman", "Times", "Computer Modern Roman", "serif"],
    "font.size": 8.5,                  # slightly smaller than before
    "axes.titlesize": 9.5,
    "axes.labelsize": 8.5,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "figure.dpi": 200,
    "savefig.dpi": 300,
    "axes.spines.top": False,
    "axes.spines.right": False,
})

# ---------------- Data ----------------
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
accessible = np.array([0, 0, 2, 2, 9, 3])
provided_not_accessible = np.array([0, 0, 1, 3, 1, 0])
not_provided = np.array([0, 0, 1, 1, 4, 0])

counts = pd.DataFrame({
    "Accessible": accessible,
    "Provided but not accessible": provided_not_accessible,
    "Not provided": not_provided
}, index=years)

totals = counts.sum(axis=1)

# ---------------- Layout ----------------
figsize = (3.35, 2.1)   # ACM single-column size
fig, ax = plt.subplots(figsize=figsize)

# ---------------- Colors & hatches (print-friendly) ----------------
c_accessible = "#1f77b4"      # blue
c_pbna = "#7f7f7f"            # medium gray
c_not_provided = "#c7c7c7"    # light gray
edge = "#444444"

h_accessible = ""    # no hatch
h_pbna = "//"
h_not_provided = "\\"

# ---------------- Grouped bars ----------------
bar_width = 0.22
x = years.astype(float)

ax.bar(x - bar_width, counts["Accessible"], width=bar_width, label="Accessible",
       color=c_accessible, edgecolor=edge, linewidth=0.6, hatch=h_accessible, zorder=3)
ax.bar(x, counts["Provided but not accessible"], width=bar_width, label="Provided but not accessible",
       color=c_pbna, edgecolor=edge, linewidth=0.6, hatch=h_pbna, zorder=3)
ax.bar(x + bar_width, counts["Not provided"], width=bar_width, label="Not provided",
       color=c_not_provided, edgecolor=edge, linewidth=0.6, hatch=h_not_provided, zorder=3)

# ---------------- Trend line for totals ----------------
ax.plot(years, totals.values, color="#2c2c2c", linestyle="-", marker="o",
        markersize=3, linewidth=1.0, label="Total papers", zorder=4)

# Annotate totals above markers (smaller, not bold)
for yr, total in totals.items():
    if total > 0:
        ax.text(yr, total + 0.15, str(int(total)),
                ha="center", va="bottom", fontsize=7.5, color="#2c2c2c")

# ---------------- Axes styling ----------------
ax.set_xlabel("Publication Year")
ax.set_ylabel("Number of Papers")

ax.set_xticks(years)
ax.set_xlim(years.min() - 0.6, years.max() + 0.6)
ax.set_ylim(0, max(totals.values) + 2)

ax.yaxis.grid(True, color="#e6e6e6", linewidth=0.7, zorder=0)
ax.xaxis.grid(False)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

# Clean spines
ax.spines["left"].set_visible(True)
ax.spines["bottom"].set_visible(True)
ax.spines["left"].set_color("#aaaaaa")
ax.spines["bottom"].set_color("#aaaaaa")

# Legend above plot (same style, smaller font)
ax.legend(loc="lower left", bbox_to_anchor=(0.0, 1.02),
          ncol=2, frameon=False, handlelength=1.2, columnspacing=1.0)

fig.tight_layout(pad=0.35)

# ---------------- Save ----------------
fig.savefig("replication_availability_by_year.svg", bbox_inches="tight")
fig.savefig("replication_availability_by_year.pdf", bbox_inches="tight")

plt.show()
