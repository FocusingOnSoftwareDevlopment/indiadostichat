import os

base_dir = "c:\\Users\\mks1j\\.gemini\\antigravity\\scratch"
terms = ["404", "Not found", "coverage", "indexing", "impressions", "duplicate", "canonical"]

for file in os.listdir(base_dir):
    if file.endswith((".txt", ".csv", ".json", ".xml", ".md")):
        file_path = os.path.join(base_dir, file)
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            for term in terms:
                if term.lower() in content.lower():
                    print(f"Found '{term}' in file: {file_path}")
        except Exception as e:
            pass
