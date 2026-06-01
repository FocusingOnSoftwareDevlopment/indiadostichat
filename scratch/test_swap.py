import os
import re

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

footer_pattern = re.compile(
    r'(<div class="footer-section"[^>]*>\s*<h4[^>]*>\s*Explore IndiaDostiChat\s*</h4>\s*<ul[^>]*>)(.*?)(</ul>)',
    re.DOTALL | re.IGNORECASE
)

match = footer_pattern.search(content)
if not match:
    print("No regex match")
else:
    prefix, ul_content, suffix = match.groups()
    li_pattern = re.compile(r'(<li[^>]*>.*?</li>)', re.DOTALL)
    li_items = li_pattern.findall(ul_content)
    print(f"Found {len(li_items)} LI items")
    
    anon_idx = -1
    desi_idx = -1
    for i, li in enumerate(li_items):
        if "anonymous-indian-chat" in li:
            anon_idx = i
        elif "desi-chat" in li:
            desi_idx = i

    print(f"anon_idx: {anon_idx}, desi_idx: {desi_idx}")
    
    if anon_idx != -1 and desi_idx != -1:
        li_items[anon_idx], li_items[desi_idx] = li_items[desi_idx], li_items[anon_idx]
        new_ul_content = "\n" + "\n".join([li.strip() for li in li_items]) + "\n"
        old_full_block = match.group(0)
        new_full_block = prefix + new_ul_content + suffix
        
        print("old_full_block in content:", old_full_block in content)
        new_content = content.replace(old_full_block, new_full_block)
        print("new_content differs from content:", new_content != content)
