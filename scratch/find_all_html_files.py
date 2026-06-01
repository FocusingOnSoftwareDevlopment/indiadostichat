import os

base_dir = "."
html_files = []

for root, dirs, files in os.walk(base_dir):
    if ".git" in root or "scratch" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.relpath(os.path.join(root, file), base_dir))

print(f"Total HTML files: {len(html_files)}")
for f in sorted(html_files):
    print(f)
