import os
import re

stories_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\india-stories"

html_files = []
for root, dirs, files in os.walk(stories_dir):
    for file in files:
        if file.endswith('.html'):
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, stories_dir)
            html_files.append(rel_path)

print(f"Total HTML files found under india-stories/: {len(html_files)}")
for f in sorted(html_files):
    print(f)
