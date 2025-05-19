import pandas as pd
import requests
import time

# Path to your original CSV file
file_path = r"E:\AI for SE\Security Aspects of LLM\Paper 2025\prompt engineering\Core Paper\Before Filter\SearchResults (1)_filtered.csv"

# Load the CSV and skip the first 5 rows
df = pd.read_csv(file_path)
df_remaining = df.iloc[5:].copy()

# Springer Meta API key
API_KEY = "4763e4cb6c16323e801915d6f7acd764"

# Function to get abstract and keywords using DOI
def get_metadata(doi):
    url = f"http://api.springernature.com/meta/v2/json?q=doi:{doi}&api_key={API_KEY}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "records" in data and data["records"]:
                record = data["records"][0]
                abstract = record.get("abstract", "")
                keywords = ", ".join(record.get("keyword", []))
                return abstract, keywords
    except Exception as e:
        print(f"❌ Error for DOI {doi}: {e}")
    return "", ""

# Extract metadata
abstracts = []
keywords = []

for idx, doi in enumerate(df_remaining["Item DOI"], start=6):  # start=6 for correct log count
    doi = str(doi).strip()
    if doi and doi.lower() != "nan":
        abstract, kw = get_metadata(doi)
        print(f"✔ Processed {idx + 1}/{len(df)}: DOI {doi}")
    else:
        abstract, kw = "", ""
        print(f"⚠ Skipped {idx + 1}/{len(df)}: DOI missing or invalid")
    abstracts.append(abstract)
    keywords.append(kw)
    time.sleep(1)

# Add metadata to the DataFrame
df_remaining["Abstract Note"] = abstracts
df_remaining["Keywords"] = keywords

# Combine with the first 5 already-processed rows
df_first5 = df.iloc[:5].copy()
final_df = pd.concat([df_first5, df_remaining], ignore_index=True)

# Save the updated file
output_path = file_path.replace(".csv", "_with_all_abstracts.csv")
final_df.to_csv(output_path, index=False)

print(f"\n✅ Done! Full metadata saved to:\n{output_path}")
