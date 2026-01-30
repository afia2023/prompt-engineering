


import matplotlib.pyplot as plt
import numpy as np

# ------------------ Updated Data (including 2025 entries) ------------------
# Proportions adjusted for CommitBench (Wu), RepoSummary (Zhu), 
# DocAgent (Yang), and DLCog (Zhang).
language_shares = {
    "Zero-shot": {"Python": 22, "Java": 34, "JavaScript": 12, "C/C++": 10, "Go": 8, "PHP": 6, "Ruby": 5, "Other": 3},
    "Few-shot": {"Python": 26, "Java": 28, "JavaScript": 10, "C/C++": 10, "Go": 9, "PHP": 7, "Ruby": 6, "Other": 4},
    "RAG": {"Python": 24, "Java": 32, "C/C++": 14, "JavaScript": 8, "PHP": 6, "Go": 6, "Ruby": 5, "Other": 5},
    "Chain-of-Thought": {"Python": 38, "Java": 40, "Other": 22},
}

# ------------------ High-Contrast Color Palette ------------------
colors = {
    "Python": "#64B5F6", "Java": "#FF8A80", "JavaScript": "#FFD54F",  
    "C/C++": "#4DD0E1", "Go": "#81C784", "PHP": "#BA68C8",         
    "Ruby": "#FFB74D", "Other": "#E0E0E0"        
}

# ------------------ Figure Setup ------------------
paradigms = list(language_shares.keys())
radius_step = 0.23   
current_radius = 1.0
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))

# Vector settings for PDF (Type 42 fonts for paper submission)
plt.rcParams.update({
    'font.size': 11, 'font.weight': 'bold',
    'pdf.fonttype': 42, 'ps.fonttype': 42
})

language_angle_map = {lang: [] for lang in colors.keys()}
start_angle = 90

# ------------------ Create Concentric Rings ------------------
for paradigm in paradigms:
    data = language_shares[paradigm]
    langs, sizes = list(data.keys()), list(data.values())
    total = sum(sizes)
    current_angle = start_angle

    for lang, size in zip(langs, sizes):
        theta1, theta2 = current_angle, current_angle - (size / total) * 360
        # Map labels to the outermost ring segments
        language_angle_map[lang].append((theta1, theta2, current_radius - radius_step / 2))
        current_angle = theta2

    ax.pie(
        sizes, radius=current_radius,
        colors=[colors[l] for l in langs],
        startangle=start_angle, counterclock=False,
        wedgeprops=dict(width=radius_step, edgecolor="#FFFFFF", linewidth=1.0),
    )

    label_text = "CoT" if paradigm == "Chain-of-Thought" else paradigm
    ax.text(0, current_radius - (radius_step * 0.5), label_text, ha="center", va="center")
    current_radius -= radius_step

# ------------------ Center Decoration ------------------
centre_circle = plt.Circle((0, 0), current_radius + 0.05, color='white')
ax.add_artist(centre_circle)
ax.text(0, 0, "Language\nCoverage\n(%)", ha='center', va='center')

# ------------------ Labels & Connectors ------------------
for lang, segs in language_angle_map.items():
    if not segs: continue
    theta1, theta2, ring_mid = segs[0]
    mid_angle = np.deg2rad((theta1 + theta2) / 2)
    x_inner, y_inner = np.cos(mid_angle) * ring_mid, np.sin(mid_angle) * ring_mid
    x_mid, y_mid = np.cos(mid_angle) * 1.18, np.sin(mid_angle) * 1.18
    x_end = x_mid + (0.12 if np.cos(mid_angle) > 0 else -0.12)
    
    ax.plot([x_inner, x_mid, x_end], [y_inner, y_mid, y_mid], color=colors[lang], lw=1.5)
    ax.text(x_end + (0.05 if np.cos(mid_angle) > 0 else -0.05), y_mid,
            lang, ha='left' if np.cos(mid_angle) > 0 else 'right', va='center')

# ------------------ Save Section ------------------
plt.tight_layout()

# Save as PDF (Vector format - best for LaTeX/Publication)
plt.savefig("Language_Distribution.pdf", format="pdf", bbox_inches="tight")

# Save as PNG (Raster format - 600 DPI for high resolution)
plt.savefig("Language_Distribution.png", format="png", dpi=600, bbox_inches="tight")

print("Files saved as 'Language_Distribution.pdf' and 'Language_Distribution.png'")
plt.show()