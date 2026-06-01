import os

base_dir = "."
term = "duno-tournament"

for root, dirs, files in os.walk(base_dir):
    if any(p in root for p in [".git", "scratch", "uno-game"]):
        continue
    for file in files:
        if file.endswith((".html", ".xml", ".txt", ".json", ".js", ".css")):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                if term in content:
                    lines = content.splitlines()
                    for i, line in enumerate(lines):
                        if term in line:
                            print(f"Found in {file_path} on line {i+1}: {line.strip()}")
            except Exception as e:
                pass
