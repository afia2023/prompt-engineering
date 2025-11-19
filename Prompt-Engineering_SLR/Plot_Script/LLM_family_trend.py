# Re-create the grouped LLM family trend chart (2020–2025) 
import matplotlib.pyplot as plt
from collections import OrderedDict
import numpy as np

# ------------------ Data ------------------
year_by_ref = {
    "ahmed2022few": 2022, "fried2022incoder": 2022, "ahmed2024automatic": 2024, "arakelyan2023exploring": 2023,
    "chai2022ernie": 2022, "dhulshette2025hierarchical": 2025, "gao2023makes": 2023,
    "geng2024large": 2024, "imani2024context": 2024, "khan2022automatic": 2022,
    "kruse2024can": 2024, "li2024only": 2024, "lomshakov2024proconsul": 2024,
    "lu2024instructive": 2024, "makharev2025code": 2025, "Pan2024ContextPromptTuning": 2024,
    "rukmono2023achieving": 2023, "shin2023prompt": 2023, "sun2023automatic": 2023,
    "sun2024source": 2024, "sun2025commenting": 2025, "wang2024natural": 2024,
    "wang2024purpose": 2024, "YUN2024112149": 2024, "zhang2024attacks": 2024,
    "zhang2024commit": 2024, "zhou2023towards": 2023,
}

llms_by_ref = {
    "sun2023automatic": ["ChatGPT (GPT-3.5 series)"],
    "geng2024large": ["Codex"],
    "wang2024natural": ["CodeBERT", "CodeT5", "GPT-4"],
    "fried2022incoder": ["InCoder"],
    "sun2024source": ["CodeLlama-Instruct-7B", "StarChat-β (16B)", "GPT-3.5 (gpt-3.5-turbo)", "GPT-4 (gpt-4-1106-preview)"],
    "chai2022ernie": ["ERNIE-Code (T5 architecture)"],
    "shin2023prompt": ["GPT-4"],
    "khan2022automatic": ["OpenAI Codex (GPT-3-based)"],
    "Pan2024ContextPromptTuning": ["PLBART", "CodeT5", "ChatGPT"],
    "ahmed2022few": ["OpenAI Codex"],
    "kruse2024can": ["GPT-4"],
    "zhang2024attacks": ["GPT-4"],
    "gao2023makes": ["Codex", "GPT-3.5", "ChatGPT"],
    "ahmed2024automatic": ["code-davinci-002", "text-davinci-003", "GPT-3.5-turbo"],
    "arakelyan2023exploring": ["CodeT5", "Codex", "ChatGPT"],
    "YUN2024112149": ["ChatGPT (text-davinci-003)", "CodeBERT", "CodeT5"],
    "lomshakov2024proconsul": ["CodeLlama-7B/34B-Instruct", "GPT-4o"],
    "lu2024instructive": ["GPT-Neo-2.7B", "Code Llama-13B"],
    "zhou2023towards": ["Meta-learner via MAML"],
    "rukmono2023achieving": ["OpenAI GPT-3.5-turbo-0613"],
    "sun2025commenting": ["CodeLlama-Instruct-7B", "CodeGemma-7B", "GPT-4"],
    "makharev2025code": ["DeepSeek-Coder-1.3B", "DeepSeek-Coder-6.7B", "DeepSeek-Coder-33B", "StarCoder2-15B"],
    "dhulshette2025hierarchical": ["Llama-3", "StarChat2", "Codestral"],
    "imani2024context": ["GPT-4", "Llama3 70B Instruct (AWQ-quantized)", "Llama3 8B Instruct"],
    "li2024only": ["GPT-4"],
    "zhang2024commit": ["ChatGPT (gpt-3.5-turbo)", "Llama 2 (7B)", "Llama 2 (70B)"],
}

# ------------------ Family grouping ------------------
families = OrderedDict({
    "GPT family": [
        "GPT-4","GPT-4o","GPT-3.5","GPT-3.5 (gpt-3.5-turbo)","GPT-3.5-turbo","OpenAI GPT-3.5-turbo-0613",
        "ChatGPT","ChatGPT (gpt-3.5-turbo)","ChatGPT (GPT-3.5 series)","ChatGPT (text-davinci-003)",
        "text-davinci-003","code-davinci-002","OpenAI Codex (GPT-3-based)","OpenAI Codex","Codex"
    ],
    "CodeT5 family": ["CodeT5"],
    "PLBART": ["PLBART"],
    "InCoder": ["InCoder"],
    "CodeBERT": ["CodeBERT"],
    "ERNIE-Code": ["ERNIE-Code (T5 architecture)"],
    "Llama family": [
        "Llama 2 (7B)","Llama 2 (70B)","Llama-3","Llama3","Llama3 8B Instruct","Llama3 70B Instruct (AWQ-quantized)",
        "CodeLlama-Instruct-7B","CodeLlama-7B","CodeLlama-7B/34B-Instruct","Code Llama-13B"
    ],
    "DeepSeek family": ["DeepSeek-Coder-1.3B","DeepSeek-Coder-6.7B","DeepSeek-Coder-33B"],
    "StarCoder / StarChat": ["StarCoder2-15B","StarChat-β (16B)","StarChat2"],
    "Gemma family": ["CodeGemma-7B"],
    "Codestral": ["Codestral"],
    "GPT-Neo": ["GPT-Neo-2.7B"],
})

# ------------------ Helper function ------------------
def model_to_family(model: str):
    for fam, members in families.items():
        for m in members:
            if m.lower() in model.lower():
                return fam
    return None

# ------------------ Aggregate counts ------------------
years = list(range(2020, 2026))
fam_counts = {fam: [0]*len(years) for fam in families.keys()}

for ref, models in llms_by_ref.items():
    y = year_by_ref.get(ref)
    if y is None:
        continue
    seen = set()
    for mdl in models:
        fam = model_to_family(mdl)
        if not fam:
            continue
        if fam not in seen:
            fam_counts[fam][y-2020] += 1
            seen.add(fam)

fam_counts = {k:v for k,v in fam_counts.items() if sum(v) > 0}

# ------------------ Global font & style setup ------------------
plt.rcParams.update({
    'font.size': 13,        # increased by 1
    'font.weight': 'bold',
    'axes.labelcolor': '#000000',
    'text.color': '#000000',
    'pdf.fonttype': 42,
    'ps.fonttype': 42
})

# ------------------ Plot ------------------
plt.figure(figsize=(14, 4.8))
x = np.array(years, dtype=float)
plot_order = [f for f in [
    "GPT family","Llama family","CodeT5 family","DeepSeek family",
    "StarCoder / StarChat","PLBART","InCoder","CodeBERT",
    "ERNIE-Code","Gemma family","Codestral","GPT-Neo"
] if f in fam_counts]

offsets = np.linspace(-0.15, 0.15, len(plot_order))

for i, fam in enumerate(plot_order):
    y = np.array(fam_counts[fam], dtype=float)
    plt.plot(
        x + offsets[i], y,
        marker='o', markersize=7, linewidth=1.8,
        label=fam, markeredgecolor='white',
        markeredgewidth=1.2, zorder=3
    )

max_y = max(max(v) for v in fam_counts.values())

plt.ylim(-0.2, max_y + 1)
plt.axvline(2022.9, color='gray', linestyle='--', linewidth=1)

# ------------------ FIXED ANNOTATION (moved left & up + bigger font) ------------------
plt.text(
    2022.7, max_y * 0.9,          # moved left & higher
    "ChatGPT released\nNov 2022",
    fontsize=12, va='center', ha='right'
)

plt.xticks(years)
plt.yticks(range(0, max_y + 1))
plt.grid(True, axis='y', linestyle=':', linewidth=0.9)

plt.xlabel("Year", fontsize=13, fontweight='bold')
plt.ylabel("Mentions in studies (per family)", fontsize=13, fontweight='bold')

plt.legend(loc='upper left', ncol=2, frameon=False, fontsize=12)
plt.tight_layout()

for spine in ["top", "right"]:
    plt.gca().spines[spine].set_visible(False)

# ------------------ Save ------------------
plt.savefig("LLM_Trend_by_Family.pdf", format="pdf",
            bbox_inches="tight", transparent=True, dpi=600)
plt.savefig("LLM_Trend_by_Family.png", dpi=600, bbox_inches="tight")

plt.show()

print("Saved: LLM_Trend_by_Family.pdf and LLM_Trend_by_Family.png")

