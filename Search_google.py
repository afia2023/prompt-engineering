

import os

# Set the folder containing your BibTeX files
folder_path = r"E:\AI for SE\Security Aspects of LLM\Paper 2025\prompt engineering\Core Paper\Initial Study\Science Direct Papers"

# Check if the folder exists
if not os.path.exists(folder_path):
    raise FileNotFoundError(f"The folder path '{folder_path}' does not exist.")

# Collect all .bib files
bib_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".bib")])

# Check if any .bib files are found
if not bib_files:
    raise FileNotFoundError(f"No .bib files found in the folder '{folder_path}'.")

# Create merged output path
output_file = os.path.join(folder_path, "merged_sciencedirect.bib")

# Merge all BibTeX files into one
with open(output_file, "w", encoding="utf-8") as outfile:
    for fname in bib_files:
        file_path = os.path.join(folder_path, fname)
        with open(file_path, "r", encoding="utf-8") as infile:
            outfile.write(infile.read())
            outfile.write("\n\n")  # Add spacing between entries

print(f"✅ Merged {len(bib_files)} files into:\n{output_file}")
