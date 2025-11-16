import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# === Load Excel with FULL PATH ===
df = pd.read_excel("/Users/AfiaFarjana/Downloads/final_merged_table.xlsx")

# === Detect publication column ===
pub_col_candidates = [c for c in df.columns if "publication" in c.lower()]
if not pub_col_candidates:
    raise ValueError("Could not find publication year column.")
pub_col = pub_col_candidates[0]

# === Extract years ===
years_series = df[pub_col].dropna().astype(int)

# === Count publications per year ===
counts = Counter(years_series)

# 🔒 FIXED YEAR RANGE 2020–2025
all_years = list(range(2020, 2026))          # 2020, 2021, 2022, 2023, 2024, 2025
pub_counts = [counts.get(y, 0) for y in all_years]

# If all counts are zero (just in case), avoid crash on argmax
if any(pub_counts):
    peak_idx = int(np.argmax(pub_counts))
else:
    peak_idx = 0

# === Plot Trend Line ===
plt.figure(figsize=(10, 6))

x = np.arange(len(all_years))
y = pub_counts
all_years_str = [str(y) for y in all_years]

# Gradient fill
plt.fill_between(all_years_str, y, color="skyblue", alpha=0.7)

# Trend line
plt.plot(all_years_str, y, color="dodgerblue", lw=4, marker='o', markersize=12)

# Peak highlight
plt.scatter(all_years_str[peak_idx], y[peak_idx],
            color='red', s=200, edgecolor='k', zorder=3)

# Labels on points
for i, count in enumerate(y):
    plt.text(all_years_str[i], count + 0.3, str(count),
             ha='center', va='bottom', fontsize=14,
             fontweight='bold',
             color='red' if i == peak_idx else 'black')

# Axis labels
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Publications', fontsize=14)

# No title
plt.title("")

# Only X & Y axes (no box)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)

# Y-limit based on data
plt.ylim(0, max(y) + 2 if any(y) else 2)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# Save SVG
plt.savefig("publication_year.svg", format="svg")
plt.show()

