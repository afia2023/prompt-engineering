# import matplotlib.pyplot as plt
# from collections import OrderedDict
# import numpy as np

# # ------------------ Data (Final Refined Version) ------------------
# year_by_ref = {
#     "ahmed2022few": 2022, "fried2022incoder": 2022, "ahmed2024automatic": 2024, "arakelyan2023exploring": 2023,
#     "chai2022ernie": 2022, "dhulshette2025hierarchical": 2025, "gao2023makes": 2023,
#     "geng2024large": 2024, "imani2024context": 2024, "khan2022automatic": 2022,
#     "kruse2024can": 2024, "li2024only": 2024, "lomshakov2024proconsul": 2024,
#     "lu2024instructive": 2024, "makharev2025code": 2025, "Pan2024ContextPromptTuning": 2024,
#     "rukmono2023achieving": 2023, "shin2023prompt": 2023, "sun2023automatic": 2023,
#     "sun2024source": 2024, "sun2025commenting": 2025, "wang2024natural": 2024,
#     "wang2024purpose": 2024, "YUN2024112149": 2024, "zhang2024attacks": 2024,
#     "zhang2024commit": 2024, "zhou2023towards": 2023,
# }

# llms_by_ref = {
#     "sun2023automatic": ["ChatGPT (GPT-3.5 series)"],
#     "geng2024large": ["Codex"],
#     "wang2024natural": ["GPT-4"],
#     "fried2022incoder": ["InCoder"],
#     "sun2024source": ["CodeLlama-Instruct-7B", "StarChat-β (16B)", "GPT-3.5 (gpt-3.5-turbo)", "GPT-4 (gpt-4-1106-preview)"],
#     "chai2022ernie": ["ERNIE-Code"],
#     "shin2023prompt": ["GPT-4"],
#     "khan2022automatic": ["OpenAI Codex (GPT-3-based)"],
#     "Pan2024ContextPromptTuning": ["ChatGPT"],
#     "ahmed2022few": ["OpenAI Codex"],
#     "kruse2024can": ["GPT-4"],
#     "zhang2024attacks": ["GPT-4"],
#     "gao2023makes": ["Codex", "GPT-3.5"], 
#     "ahmed2024automatic": ["code-davinci-002", "text-davinci-003", "GPT-3.5-turbo"],
#     "arakelyan2023exploring": ["Codex", "ChatGPT"],
#     "YUN2024112149": ["ChatGPT (text-davinci-003)"],
#     "lomshakov2024proconsul": ["CodeLlama-7B/34B-Instruct", "GPT-4o"],
#     "lu2024instructive": ["GPT-Neo-2.7B", "Code Llama-13B"],
#     "zhou2023towards": ["2-layer Seq2Seq (LSTM)"], 
#     "rukmono2023achieving": ["OpenAI GPT-3.5-turbo-0613"],
#     "sun2025commenting": ["CodeLlama-Instruct-7B", "CodeGemma-7B", "GPT-4"],
#     "makharev2025code": ["DeepSeek-Coder-1.3B", "DeepSeek-Coder-6.7B", "DeepSeek-Coder-33B", "StarCoder2-15B"],
#     "dhulshette2025hierarchical": ["Llama-3", "StarChat2", "Codestral"],
#     "imani2024context": ["GPT-4", "Llama3 70B Instruct", "Llama3 8B Instruct"],
#     "li2024only": ["GPT-4"],
#     "zhang2024attacks": ["GPT-4"],
#     "zhang2024commit": ["ChatGPT (gpt-3.5-turbo)", "Llama 2 (7B)", "Llama 2 (70B)"],
#     "wang2024purpose": ["ChatGPT", "GPT-4"]
# }

# # ------------------ Families (From Table 2) ------------------
# families = OrderedDict({
#     "GPT (OpenAI)": ["GPT-4", "GPT-3.5", "ChatGPT", "Codex", "davinci"],
#     "Llama (Meta)": ["Llama", "CodeLlama"],
#     "ERNIE series": ["ERNIE"],
#     "DeepSeek": ["DeepSeek"],
#     "StarCoder": ["StarCoder", "StarChat"],
#     "Gemma": ["Gemma"],
#     "Mistral": ["Codestral"],
#     "EleutherAI": ["GPT-Neo"],
#     "Meta-Research": ["InCoder"],
#     "Meta-Adaptive": ["Seq2Seq", "MAML"]
# })

# def model_to_family(model: str):
#     for fam, keywords in families.items():
#         for kw in keywords:
#             if kw.lower() in model.lower():
#                 return fam
#     return None

# # Aggregate counts
# years_list = list(range(2022, 2026))
# fam_counts = {fam: [0]*len(years_list) for fam in families.keys()}

# for ref, models in llms_by_ref.items():
#     y = year_by_ref.get(ref)
#     if y is None or y < 2022: continue
#     seen_fams = set()
#     for mdl in models:
#         fam = model_to_family(mdl)
#         if fam and fam not in seen_fams:
#             fam_counts[fam][y-2022] += 1
#             seen_fams.add(fam)

# fam_counts = {k: v for k, v in fam_counts.items() if sum(v) > 0}

# # Global plot setup
# plt.rcParams.update({'font.size': 11, 'font.weight': 'bold'})
# plt.figure(figsize=(14, 7))
# ax = plt.gca()

# x = np.array(years_list, dtype=float)
# plot_order = [f for f in families.keys() if f in fam_counts]
# offsets = np.linspace(-0.3, 0.3, len(plot_order))

# for i, fam in enumerate(plot_order):
#     y = np.array(fam_counts[fam], dtype=float)
#     plt.plot(x + offsets[i], y, marker='o', markersize=8, linewidth=2.0, label=fam)

# # Annotation in ASH (GRAY) color
# max_y = max(max(v) for v in fam_counts.values())
# plt.axvline(2022.9, color='lightgray', linestyle='--', alpha=0.6)
# plt.text(2022.85, max_y * 0.9, "ChatGPT released\nNov 2022", 
#          ha='right', fontweight='bold', color='gray') 

# # --- STYLE: REMOVE OUTER BOX ---
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

# plt.xticks(years_list)
# plt.yticks(range(0, int(max_y) + 2))
# plt.xlabel("Year", fontsize=13, fontweight='bold')
# plt.ylabel("Count of Studies (per family)", fontsize=13, fontweight='bold')

# # --- LEGEND INSIDE PLOT - TOP RIGHT ---
# plt.legend(loc='upper right', ncol=2, frameon=True, fontsize=10)

# plt.tight_layout()
# plt.savefig("LLM_Trend_by_Family.pdf", format="pdf", bbox_inches="tight")
# plt.savefig("LLM_Trend_by_Family.png", format="png", dpi=300, bbox_inches="tight")
# plt.show()

import matplotlib.pyplot as plt
from collections import OrderedDict
import numpy as np

# ============================================================
# 1. STUDY → YEAR (29 UNIQUE PAPERS)
# ============================================================
year_by_ref = {
    # ---- 2022 ----
    "ahmed2022few": 2022,
    "fried2022incoder": 2022,
    "chai2022ernie": 2022,
    "khan2022automatic": 2022,

    # ---- 2023 ----
    "sun2023automatic": 2023,
    "shin2023prompt": 2023,
    "gao2023makes": 2023,
    "arakelyan2023exploring": 2023,
    "zhou2023towards": 2023,

    # ---- 2024 ----
    "ahmed2024automatic": 2024,
    "geng2024large": 2024,
    "wang2024natural": 2024,
    "kruse2024can": 2024,
    "li2024only": 2024,
    "lomshakov2024proconsul": 2024,
    "lu2024instructive": 2024,
    "imani2024context": 2024,
    "wang2024purpose": 2024,
    "YUN2024112149": 2024,
    "zhang2024attacks": 2024,
    "zhang2024commit": 2024,
    "sun2024source": 2024,

    # ---- 2025 ----
    "makharev2025code": 2025,
    "sun2025commenting": 2025,
    "dhulshette2025hierarchical": 2025,
    "zhang2025dlcog": 2025,
    "yang2025docagent": 2025,
    "zhu2025reposummary": 2025,
    "wu2025empirical": 2025,
}

# ============================================================
# 2. STUDY → MODELS (FROM TAXONOMY TABLE)
# ============================================================
llms_by_ref = {
    "sun2023automatic": ["ChatGPT (GPT-3.5 series)"],
    "geng2024large": ["Codex"],
    "wang2024natural": ["GPT-4"],
    "fried2022incoder": ["InCoder-6.7B"],
    "chai2022ernie": ["ERNIE-Code"],
    "shin2023prompt": ["GPT-4"],
    "khan2022automatic": ["OpenAI Codex (GPT-3-based)"],
    "ahmed2022few": ["OpenAI Codex"],

    "gao2023makes": ["Codex", "GPT-3.5"],
    "ahmed2024automatic": ["code-davinci-002", "text-davinci-003", "GPT-3.5-turbo"],
    "arakelyan2023exploring": ["Codex", "ChatGPT"],
    "YUN2024112149": ["gpt-3.5-turbo", "text-davinci-003", "LLaMA"],
    "lomshakov2024proconsul": ["CodeLlama-7B", "CodeLlama-34B", "GPT-4o"],
    "lu2024instructive": ["GPT-Neo-2.7B", "Code Llama-13B"],
    "zhou2023towards": ["2-layer Seq2Seq (LSTM)"],

    "sun2024source": [
        "CodeLlama-Instruct-7B",
        "StarChat-β-16B",
        "GPT-3.5-turbo",
        "GPT-4-1106"
    ],

    "kruse2024can": ["GPT-4"],
    "zhang2024attacks": ["GPT-4"],
    "imani2024context": ["GPT-4", "Llama-3-70B", "Llama-3-8B"],
    "li2024only": ["GPT-4"],
    "zhang2024commit": ["ChatGPT", "Llama-2-7B", "Llama-2-70B"],
    "wang2024purpose": ["ChatGPT", "GPT-4"],

    "makharev2025code": [
        "DeepSeek-Coder-1.3B",
        "DeepSeek-Coder-6.7B",
        "DeepSeek-Coder-33B",
        "StarCoder2-15B"
    ],
    "sun2025commenting": ["CodeLlama-Instruct-7B", "CodeGemma-7B", "GPT-4"],
    "dhulshette2025hierarchical": ["Llama-3", "StarChat2", "Codestral"],
    "zhang2025dlcog": ["CodeGeeX4", "GPT-4"],
    "yang2025docagent": ["GPT-4o-mini", "CodeLlama-34B-Instruct"],
    "zhu2025reposummary": ["GPT-4o-mini", "Claude-3-Haiku"],
    "wu2025empirical": [
        "GPT-3.5-Turbo", "Claude-3-Haiku",
        "Qwen1.5-7B-Chat", "CodeQwen1.5-7B-Chat",
        "DeepSeek-V2-Chat", "DeepSeek-Coder-V2-Instruct"
    ],
}

# ============================================================
# 3. LLM FAMILIES (EXACTLY MATCHING YOUR TABLE)
# ============================================================
families = OrderedDict({
    "GPT (OpenAI)": [
        "GPT-4", "GPT-3.5", "ChatGPT",
        "Codex", "text-davinci", "code-davinci"
    ],
    "Llama (Meta)": [
        "Llama-2", "Llama-3", "Llama", "CodeLlama"
    ],
    "ERNIE series": ["ERNIE"],
    "DeepSeek": ["DeepSeek"],
    "Qwen (Alibaba)": ["Qwen1.5", "CodeQwen1.5"],
    "Claude family (Anthropic)": ["Claude"],
    "CodeGeeX": ["CodeGeeX"],
    "StarCoder": ["StarCoder", "StarChat"],
    "Gemma": ["Gemma"],
    "Mistral": ["Codestral"],
    "EleutherAI": ["GPT-Neo"],
    "Meta-Research": ["InCoder"],
    "Meta-Adaptive": ["Seq2Seq", "LSTM", "MAML"],
})

def model_to_family(model: str):
    for fam, keywords in families.items():
        for kw in keywords:
            if kw.lower() in model.lower():
                return fam
    return None

# ============================================================
# 4. AGGREGATE COUNTS (ONE COUNT PER FAMILY PER PAPER)
# ============================================================
years_list = list(range(2022, 2026))
fam_counts = {fam: [0] * len(years_list) for fam in families}

for ref, models in llms_by_ref.items():
    y = year_by_ref.get(ref)
    if y is None:
        continue
    seen_fams = set()
    for mdl in models:
        fam = model_to_family(mdl)
        if fam and fam not in seen_fams:
            fam_counts[fam][y - 2022] += 1
            seen_fams.add(fam)

fam_counts = {k: v for k, v in fam_counts.items() if sum(v) > 0}

# ============================================================
# 5. PLOT
# ============================================================
plt.rcParams.update({'font.size': 11, 'font.weight': 'bold'})
plt.figure(figsize=(14, 7))
ax = plt.gca()

x = np.array(years_list, dtype=float)
plot_order = [f for f in families if f in fam_counts]
offsets = np.linspace(-0.3, 0.3, len(plot_order))

for i, fam in enumerate(plot_order):
    y = np.array(fam_counts[fam], dtype=float)
    plt.plot(x + offsets[i], y, marker='o', linewidth=2, markersize=7, label=fam)

# ChatGPT release marker
max_y = max(max(v) for v in fam_counts.values())
plt.axvline(2022.9, color='lightgray', linestyle='--', alpha=0.6)
plt.text(2022.85, max_y * 0.9, "ChatGPT released\nNov 2022",
         ha='right', color='gray', fontweight='bold')

# Style
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xticks(years_list)
plt.yticks(range(0, int(max_y) + 2))
plt.xlabel("Year", fontsize=13, fontweight='bold')
plt.ylabel("Count of Studies (per family)", fontsize=13, fontweight='bold')
plt.legend(loc='upper right', ncol=2, frameon=True, fontsize=10)

plt.tight_layout()
plt.savefig("LLM_Trend_by_Family.pdf", bbox_inches="tight")
plt.savefig("LLM_Trend_by_Family.png", dpi=300, bbox_inches="tight")
plt.show()
