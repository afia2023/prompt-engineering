import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# Parse your publication data
pubs = [
    "Mingyang Geng et al. (2024)",
    "Chaozheng Wang et al. (2022)",
    "Toufique Ahmed et al. (2022)",
    "Jiawei Lu et al. (2024)",
    "Yan Wang et al.(2024)",
    "Toufique Ahmed et al. (2024)",
    "Weisong Sun et al.(2024)",
    "Shuzheng Gao et al (2023)",
    "Jia Li et al(2023)",
    "Chaozheng Wang (2023)",
    "Hans-Alexander Kruse et al. (2024)",
    "Ziyi Zhou et al(2023)",
    "Weisong Sun et al.(2023)",
    "Chia-Yi Su et al. (2024)",
    "Shushan Arakelyan (2023)",
    "Daniel Fried et al.(2022)",
    "Yekun Chai et al.(2022)",
    "Xinglu Pan et al(2024)",
    "Jie Zhu et al.(2023)",
    "Jiho Shin et al. (2023)",
    "Vladimir Makharev et al.(2025)(arxiv)",
    "Junaed Younus Khan et al(2022)",
    "YunSeok Choi et al. (2023)",
    "Weisong Sun et al(2025)",
    "Nilesh Dhulshette et al. (2025)",
    "Vadim Lomshakov et al. (2024)",
    "Rui Xie et al (2022)"
]

years = []
for line in pubs:
    found = re.findall(r"\((20\d{2})", line)
    for y in found:
        years.append(y)

# Make sure all years 2020-2025 are present
all_years = [str(y) for y in range(2020, 2026)]
counts = Counter(years)
pub_counts = [counts[y] for y in all_years]

# Find the peak year for highlighting
peak_idx = np.argmax(pub_counts)

# Plot trend line with gradient fill
plt.figure(figsize=(10,6))
x = np.arange(len(all_years))
y = pub_counts

# Fill under the curve for "drama"
plt.fill_between(all_years, y, color="skyblue", alpha=0.7)
plt.plot(all_years, y, color="dodgerblue", lw=4, marker='o', markersize=12, label='Publications')
plt.scatter(all_years[peak_idx], y[peak_idx], color='red', s=200, edgecolor='k', zorder=3, label='Peak year')

# Annotate counts on top of each point
for i, count in enumerate(y):
    plt.text(all_years[i], count+0.3, str(count), ha='center', va='bottom', fontsize=14, fontweight='bold',
             color='red' if i == peak_idx else 'black')

plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Publications', fontsize=14)
plt.title('Publication Years (2020–2025)', fontsize=18, fontweight='bold')
plt.ylim(0, max(y)+2)
plt.grid(axis='y', alpha=0.3)
# plt.legend()
# plt.tight_layout()
# plt.show()
plt.legend()
plt.tight_layout()
plt.savefig("publication_trend.svg", format="svg")  # ✅ save as SVG
plt.show()