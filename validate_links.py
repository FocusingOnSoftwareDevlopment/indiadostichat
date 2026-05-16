import os
import re

def validate_links():
    base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
    html_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]
    
    all_pages = set(html_files)
    all_pages.add("./")
    all_pages.add("index.html")
    
    errors = []
    
    for filename in html_files:
        filepath = os.path.join(base_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all href="..."
        links = re.findall(r'href=["\']([^"\']+)["\']', content)
        for link in links:
            # Skip external links, anchors, and mailto/tel
            if link.startswith(("http", "#", "mailto:", "tel:", "javascript:")):
                continue
            
            # Normalize link (remove query params, anchors)
            clean_link = link.split('?')[0].split('#')[0]
            if clean_link == "" or clean_link == "./":
                continue
            
            if clean_link not in all_pages:
                # Check for assets
                if clean_link.startswith("assets/"):
                    if not os.path.exists(os.path.join(base_dir, clean_link)):
                        errors.append(f"Broken asset link in {filename}: {link}")
                else:
                    errors.append(f"Broken internal link in {filename}: {link}")
    
    if errors:
        for err in errors:
            print(err)
    else:
        print("All internal links are valid.")

if __name__ == "__main__":
    validate_links()
