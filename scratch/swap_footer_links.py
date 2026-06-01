import os
import re

base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"

def swap_footer_links(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the footer section that contains "Explore IndiaDostiChat"
    # We look for <div class="footer-section"> ... <h4>Explore IndiaDostiChat</h4> ... <ul> ... </ul>
    # And we capture the <ul>...</ul> block
    footer_pattern = re.compile(
        r'(<div class="footer-section"[^>]*>\s*<h4[^>]*>\s*Explore IndiaDostiChat\s*</h4>\s*<ul[^>]*>)(.*?)(</ul>)',
        re.DOTALL | re.IGNORECASE
    )

    match = footer_pattern.search(content)
    if not match:
        return False

    prefix, ul_content, suffix = match.groups()

    # Extract all <li>...</li> items from the <ul> block
    li_pattern = re.compile(r'(<li[^>]*>.*?</li>)', re.DOTALL)
    li_items = li_pattern.findall(ul_content)

    if not li_items:
        return False

    anon_idx = -1
    desi_idx = -1

    for i, li in enumerate(li_items):
        if "anonymous-indian-chat" in li:
            anon_idx = i
        elif "desi-chat" in li:
            desi_idx = i

    if anon_idx != -1 and desi_idx != -1:
        # Swap the elements
        li_items[anon_idx], li_items[desi_idx] = li_items[desi_idx], li_items[anon_idx]
        
        # Reconstruct the <ul> content
        new_ul_content = "\n" + "\n".join([li.strip() for li in li_items]) + "\n"
        
        # Replace the old <ul> section with the new swapped <ul> section
        # Note: to preserve indentation/formatting, we can construct the exact match block
        old_full_block = match.group(0)
        new_full_block = prefix + new_ul_content + suffix
        
        new_content = content.replace(old_full_block, new_full_block)
        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True

    return False

def main():
    count = 0
    for root_dir, dirs, files in os.walk(base_dir):
        rel_dir = os.path.relpath(root_dir, base_dir)
        parts = rel_dir.split(os.sep)
        if any(p in parts for p in [".git", "scratch", "uno-game", "blog-sources"]):
            continue
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root_dir, file)
                try:
                    if swap_footer_links(file_path):
                        print(f"Swapped footer links in: {file_path}")
                        count += 1
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
                    
    print(f"Completed. Total files updated: {count}")

if __name__ == "__main__":
    main()
