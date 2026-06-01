import os
from bs4 import BeautifulSoup

base_dir = "."
html_files = []
for root, dirs, files in os.walk(base_dir):
    if any(p in root for p in [".git", "scratch", "uno-game", "blog-sources"]):
        continue
    for file in files:
        if file.endswith(".html"):
            if file.startswith("google"):
                continue
            html_files.append(os.path.join(root, file))

links_sample = set()
for hf in html_files:
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    soup = BeautifulSoup(content, "html.parser")
    for a in soup.find_all("a"):
        href = a.get("href", "")
        if "index.html" in href:
            links_sample.add(href)

print(f"Found {len(links_sample)} unique index.html link variants:")
for l in sorted(list(links_sample)):
    print(l)
