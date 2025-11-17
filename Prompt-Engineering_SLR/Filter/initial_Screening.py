import pandas as pd
import os

# ====== FILE PATHS ======
input_file = r"E:\AI for SE\Security Aspects of LLM\Paper 2025\prompt engineering\Core Paper\Before Filter\Wiley\Wiley Library_filtered_peerreviewed_only.xlsx"
output_folder = r"E:\AI for SE\Security Aspects of LLM\Paper 2025\prompt engineering\Core Paper\Before Filter\Wiley"
output_file = os.path.join(output_folder, "Wiley_initialscreening_scored_papers.xlsx")

# ====== LOAD EXCEL & CLEAN COLUMN NAMES ======
df = pd.read_excel(input_file)

# Normalize column names
df.columns = df.columns.str.strip().str.replace('\ufeff', '').str.lower()

print("✅ Loaded columns:", df.columns.tolist())

# ====== KEYWORD CONFIGURATION ======
prompt_keywords = [
    # Core Prompt Engineering Variants
    "prompt engineering", "prompt design", "prompt tuning", "prompt optimization",
    "prompt formulation", "prompt strategy", "prompt-based", "prompting paradigm",
    "prompt refinement", "prompt crafting", "prompt adaptation", "prompt template",
    "instruction tuning", "instruction-based", "instruction prompting", "instruct-tuning",

#Few-shot and Zero-shot Paradigms,
    "few-shot", "zero-shot", "one-shot", "n-shot", "in-context learning", "contextual prompting"
]

exclude_keywords = ["survey", "review", "benchmark", "empirical study"]

# ====== SCORING FUNCTION ======
def calculate_score(text):
    if pd.isna(text):
        return 0
    text = str(text).lower()
    return sum(keyword in text for keyword in prompt_keywords)

# ====== APPLY SCORING ======
df["title_score"] = df["document title"].apply(calculate_score)
df["abstract_score"] = df["abstract note"].apply(calculate_score)

if "keywords" in df.columns:
    df["keywords_score"] = df["keywords"].apply(calculate_score)
else:
    df["keywords_score"] = 0

df["total_score"] = df["title_score"] + df["abstract_score"] + df["keywords_score"]

# ====== FILTERING ======
filtered_df = df[df["total_score"] > 0]
filtered_df = filtered_df[
    ~filtered_df["document title"].str.lower().str.contains('|'.join(exclude_keywords), na=False)
]

# ====== SORT AND SAVE TO XLSX ======
filtered_df = filtered_df.sort_values("total_score", ascending=False)
os.makedirs(output_folder, exist_ok=True)
filtered_df.to_excel(output_file, index=False)

# ====== PRINT RESULTS ======
print(f"\n✅ Done! Filtered {len(filtered_df)} papers (out of {len(df)} total).")
print("\nTop 5 papers by score:\n")
print(filtered_df[["document title", "total_score"]].head().to_string(index=False))
