import matplotlib.pyplot as plt
import matplotlib as mpl

# keep text as text (not paths) in SVG → crisper, editable
mpl.rcParams['svg.fonttype'] = 'none'
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
plt.rcParams.update({'font.size': 12})  # adjust font size for readability

years = list(range(2015, 2026))
rule_counts       = [3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]
neural_counts     = [0, 3, 6, 9, 10, 5, 3, 0, 0, 0, 0]
transformer_counts= [0, 0, 0, 0, 1, 8, 11, 12, 8, 5, 3]
llm_counts        = [0, 0, 0, 0, 0, 0, 1, 5, 12, 17, 22]

# Use colors similar to the example (yellow, green, blue, purple)
colors = ["#FDE725", "#35B779", "#31688E", "#440154"]

plt.figure(figsize=(10, 6))
plt.bar(years, rule_counts, color=colors[0], label='Rule-based/IR')
plt.bar(years, neural_counts, bottom=rule_counts, color=colors[1], label='Neural (RNN)')
bottom_transformer = [r+n for r, n in zip(rule_counts, neural_counts)]
plt.bar(years, transformer_counts, bottom=bottom_transformer, color=colors[2], label='Transformer-based')
bottom_llm = [r+n+t for r, n, t in zip(rule_counts, neural_counts, transformer_counts)]
plt.bar(years, llm_counts, bottom=bottom_llm, color=colors[3], label='LLM-based')

plt.xlabel('Year')
plt.ylabel('Number of Publications')
plt.title('Publication Trends in Code Summarization by Model Type (2015–2025)')
plt.xticks(years, rotation=45)
plt.legend()
plt.tight_layout()

# Save as SVG (vector) for LaTeX/Overleaf
plt.savefig("publication_trends.svg", format="svg", bbox_inches="tight")

# Optional: also save a PDF (ACM often prefers this)
plt.savefig("publication_trends.pdf", bbox_inches="tight")

plt.show()
