import os
import xml.etree.ElementTree as ET

sitemap_path = "sitemap.xml"
base_dir = "."

tree = ET.parse(sitemap_path)
root = tree.getroot()
ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

total_urls = 0
missing_count = 0

for loc in root.findall('.//sm:loc', ns):
    url = loc.text
    total_urls += 1
    
    # Map to local path
    rel_path = url.replace("https://www.indiadostichat.com/", "")
    if not rel_path or rel_path == "/":
        local_file = "index.html"
    elif rel_path.endswith("/"):
        local_file = os.path.join(rel_path, "index.html")
    else:
        local_file = rel_path
        
    local_file_norm = os.path.normpath(local_file).replace("\\", "/")
    if not os.path.exists(local_file_norm):
        print(f"MISSING FILE: URL {url} maps to non-existent local file: {local_file_norm}")
        missing_count += 1

print(f"Sitemap verification: Total URLs={total_urls}, Missing={missing_count}")
