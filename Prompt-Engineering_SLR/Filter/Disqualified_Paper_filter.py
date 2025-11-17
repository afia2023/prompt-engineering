import pandas as pd
import os

# Load the CSV
input_path = r"E:\AI for SE\Security Aspects of LLM\Paper 2025\prompt engineering\Core Paper\Before Filter\Scopus\scopus_filtered.csv"  # ⬅ Update this with your actual file path

# Load the CSV file
df = pd.read_csv(input_path)

# Normalize the 'Item Type' column to lowercase for consistent filtering
df["Item Type"] = df["Item Type"].astype(str).str.strip().str.lower()

# Print unique types before filtering (optional check)
print("📋 Unique 'Item Type' values before filtering:")
print(df["Item Type"].unique())

# Define the item types you want to exclude (all lowercase)
exclude_types = [
    "review",
    "conference review",
    "webpage",
    "book chapter",
    "book",
    "chapter"
]

# Filter out the excluded types
df_filtered = df[~df["Item Type"].isin(exclude_types)]

# Save the filtered CSV in the same location with "_filtered" added
base, ext = os.path.splitext(input_path)
output_path = base + "_peer_reviewed_only.csv"
df_filtered.to_csv(output_path, index=False)

print(f"\n✅ Done! Filtered file saved to:\n{output_path}")
