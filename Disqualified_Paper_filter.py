import pandas as pd
import os

# Set the path to your original CSV file
input_path = r"E:\AI for SE\Security Aspects of LLM\Paper 2025\prompt engineering\Core Paper\Before Filter\SearchResults (1).csv"  # ⬅ Replace with your actual file path

# Load the CSV
df = pd.read_csv(input_path)

# Remove rows where 'Content Type' is 'Book' or 'Chapter' (case-insensitive)
df_cleaned = df[~df['Content Type'].str.lower().isin(['book', 'chapter'])]

# Create output filename in the same folder
base, ext = os.path.splitext(input_path)
output_path = base + "_filtered.csv"

# Save the filtered CSV
df_cleaned.to_csv(output_path, index=False)

print(f"✅ Cleaned CSV saved to: {output_path}")
