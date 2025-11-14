import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# Parse publication data
pubs = [
    "Mingyang Geng et al. (2024)",#ACM3 #ICSE2024
    "YAN WANG et al. (2024)",#ACM12 #FSE2024
    "Toufique Ahmed et al. (2022)",#ACM6 #ASE2022
    "Jiawei Lu et al. (2024)",#ACM9 #ASE2024
    "Toufique Ahmed et al. (2024)",#ACM18 #ICSE2024
    "Chi Zhang et al.(2024)",#ACM24 #ASE2024
    "Shuzheng Gao et al (2023)",#ACM25 #ASE2023
    "Weisong Sun et al(2025)",#ACM36 #ICSE2025
    "Shangbo Yun et al(2024)",#sciencedirect7 #JSS2024
    "Rukmono et al. (2023)",#IEEE3 #ITOEC2023
    "Hans-Alexander Kruse et al. (2024)",#IEEE5 #ICSME2024
    "Ziyi Zhou et al(2023)",#IEEE8 #TSE2023
    "Yi Wang  et al.(2024)",#Scopus15 # IJCAI2024
    "Shushan Arakelyan (2023)",#Scopus21
    "Daniel Fried et al.(2022)",#Scopus16 #ICLR2023
    "Yekun Chai et al.(2022)",##Scopus19 ACL2023
    "Xinglu Pan et al(2024)",#Manual1 EMNLP 2023
    "Vadim Lomshakov et al. (2024)",#Manual2 #EMNLP 2024
    "Jiho Shin et al. (2023)",#Manual3 #MSR2025
    "Vladimir Makharev et al.(2025)(arxiv)",#Manual4 #ICSE2025
    "Aaron Imani et al (2024)" #Manual6 #ICSE2025 #WorkshpPaper
    "Weisong Sun et al.(2023)",#Snow1 #Arvix2023
    "Junaed Younus Khan et al(2022)",#Snow2 #ASE2022
    "Weisong Sun et al.(2025)",#Snow4 #ArVix2025
    "JIAWEI LI et al(2024)",#Snow6 #FSE2024
    "Nilesh Dhulshette et al. (2025)",#sbow8 #ICSE 2025
    "Linghao Zhang et al. (2024)",#Snow9 #SANER2024

]

# Extract years
years = []
for line in pubs:
    found = re.findall(r"\((20\d{2})", line)
    for y in found:
        years.append(y)

# Prepare counts
all_years = [str(y) for y in range(2020, 2026)]
counts = Counter(years)
pub_counts = [counts[y] for y in all_years]

# Identify peak year
peak_idx = np.argmax(pub_counts)

# Plot
plt.figure(figsize=(10, 6))
x = np.arange(len(all_years))
y = pub_counts

# Line + fill
plt.fill_between(all_years, y, color="skyblue", alpha=0.7)
plt.plot(all_years, y, color="dodgerblue", lw=4, marker='o', markersize=12)
plt.scatter(all_years[peak_idx], y[peak_idx], color='red', s=200, edgecolor='k', zorder=3)

# Add data labels
for i, count in enumerate(y):
    plt.text(all_years[i], count + 0.3, str(count),
             ha='center', va='bottom', fontsize=14, fontweight='bold',
             color='red' if i == peak_idx else 'black')

# Axis labels only
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Publications', fontsize=14)

# Remove title
# plt.title('Publication Years (2020–2025)', fontsize=18, fontweight='bold')

# Remove all outer box lines (spines)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# Optional: light horizontal grid
plt.grid(axis='y', alpha=0.3)

plt.ylim(0, max(y) + 2)
plt.tight_layout()
plt.savefig("publication_trend_clean.svg", format="svg", bbox_inches="tight", transparent=True)
plt.show()
