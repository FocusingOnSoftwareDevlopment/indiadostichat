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

print(f"Total Physical URLs: {len(physical_urls)}")
print(f"Total XML Sitemap URLs: {len(xml_urls)}")

missing_in_sitemap = physical_urls - xml_urls
extra_in_sitemap = xml_urls - physical_urls

print(f"\nPhysical URLs missing in sitemap.xml ({len(missing_in_sitemap)}):")
for url in sorted(list(missing_in_sitemap)):
    print(url)

print(f"\nExtra URLs in sitemap.xml that don't match physical pages ({len(extra_in_sitemap)}):")
for url in sorted(list(extra_in_sitemap)):
    print(url)
