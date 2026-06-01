import os

base_dir = "."
search_terms = ["tournament", "duno"]

for root, dirs, files in os.walk(base_dir):
    if any(p in root for p in [".git", "scratch", "uno-game"]):
        continue
    for file in files:
        if file.endswith((".html", ".xml", ".txt", ".json", ".js", ".css")):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                for term in search_terms:
                    if term.lower() in content.lower():
                        lines = content.splitlines()
                        for i, line in enumerate(lines):
                            if term.lower() in line.lower():
                                print(f"Found '{term}' in {file_path} on line {i+1}: {line.strip()[:120]}")
            except Exception as e:
                pass
