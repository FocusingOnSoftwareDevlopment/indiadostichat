import os
import xml.etree.ElementTree as ET

sitemap_xml_path = "sitemap.xml"

# Parse XML sitemap URLs
xml_urls = set()
if os.path.exists(sitemap_xml_path):
    tree = ET.parse(sitemap_xml_path)
    root = tree.getroot()
    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    for loc in root.findall('.//sm:loc', ns):
        xml_urls.add(loc.text.strip())

# Find all physical HTML pages
base_dir = "."
physical_urls = set()
for root, dirs, files in os.walk(base_dir):
    if any(p in root for p in [".git", "scratch", "uno-game", "blog-sources"]):
        continue
    for file in files:
        if file.endswith(".html"):
            if file.startswith("google"):
                continue
            
            # Convert to relative path
            hf = os.path.relpath(os.path.join(root, file), base_dir).replace("\\", "/")
            
            # Map to clean URL
            if hf == "index.html":
                url = "https://www.indiadostichat.com/"
            elif hf.endswith("/index.html"):
                url = "https://www.indiadostichat.com/" + hf[:-10] + "/"
            else:
                url = "https://www.indiadostichat.com/" + hf
                
            physical_urls.add(url)

missing = physical_urls - xml_urls
print("Physical URLs NOT in sitemap.xml:")
for m in sorted(list(missing)):
    print(m)

extra = xml_urls - physical_urls
print("\nExtra sitemap.xml URLs NOT in physical pages:")
for e in sorted(list(extra)):
    print(e)
