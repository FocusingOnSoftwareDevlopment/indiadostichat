import os

root_dir = "c:/Users/mks1j/.gemini/antigravity/scratch/indiadostichat_seo"
targets = ["logo.svg", "logo.webp"]

matches = []
for dirpath, _, filenames in os.walk(root_dir):
    # Skip .git assets
    if ".git" in dirpath:
        continue
    for filename in filenames:
        if filename.endswith(".html"):
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                for target in targets:
                    if target in content:
                        matches.append((filepath, target))
            except Exception as e:
                pass

print("=== Found Logo References ===")
for path, target in matches:
    rel = os.path.relpath(path, root_dir)
    print(f"{rel}: contains {target}")
