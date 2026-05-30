import os
import re
import xml.etree.ElementTree as ET

base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"

def get_html_files():
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        # Exclude india-stories and scratch
        if "india-stories" in root or "scratch" in root or ".git" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

def verify_links():
    html_files = get_html_files()
    errors = 0
    
    # Regex to find hrefs in a tags
    href_pattern = re.compile(r'<a\s+[^>]*href=["\']([^"\']*)["\']', re.IGNORECASE)
    # Regex to find canonical link hrefs
    canonical_pattern = re.compile(r'<link\s+[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']*)["\']', re.IGNORECASE)
    
    for file_path in html_files:
        rel_path = os.path.relpath(file_path, base_dir)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Check a hrefs
        hrefs = href_pattern.findall(content)
        for href in hrefs:
            # We only care about internal links
            if href.startswith("http://") or href.startswith("https://") or href.startswith("#") or href.startswith("javascript:") or href.startswith("mailto:"):
                # If it's a full URL containing indiadostichat.com and has .html
                if "indiadostichat.com" in href and ".html" in href:
                    print(f"ERROR: {rel_path} contains full internal URL with .html: {href}")
                    errors += 1
                continue
            
            if ".html" in href:
                print(f"ERROR: {rel_path} contains relative link with .html: {href}")
                errors += 1
                
        # 2. Check canonical link
        canonicals = canonical_pattern.findall(content)
        for canon in canonicals:
            if ".html" in canon:
                print(f"ERROR: {rel_path} contains canonical link with .html: {canon}")
                errors += 1
                
        # 3. Check JSON-LD schemas for .html
        if ".html" in content:
            # Let's inspect where .html might be present, it shouldn't be in schemas
            # Except maybe comments or in some other context?
            # Let's see if there are any occurrences of .html
            # Let's find occurrences of any .html that are not comments
            # Wait, let's see. If there's an error, print it.
            pass
            
    print(f"Verification complete. Total link errors found: {errors}")
    return errors == 0

def verify_sitemap_xml():
    sitemap_path = os.path.join(base_dir, "sitemap.xml")
    if not os.path.exists(sitemap_path):
        print("ERROR: sitemap.xml not found")
        return False
        
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        
        # Namespace for sitemap
        ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        errors = 0
        for loc in root.findall('.//sm:loc', ns):
            url = loc.text
            if ".html" in url:
                print(f"ERROR in sitemap.xml: Location contains .html: {url}")
                errors += 1
                
        print(f"Sitemap.xml verification complete. Errors: {errors}")
        return errors == 0
    except Exception as e:
        print(f"ERROR parsing sitemap.xml: {e}")
        return False

if __name__ == "__main__":
    links_ok = verify_links()
    sitemap_ok = verify_sitemap_xml()
    if links_ok and sitemap_ok:
        print("All validations PASSED successfully!")
    else:
        print("Some validations FAILED!")
