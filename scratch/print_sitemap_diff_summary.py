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
    # Exclude directories we shouldn't touch or index
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
                clean_path = hf[:-10].rstrip("/")
                url = f"https://www.indiadostichat.com/{clean_path}/"
            else:
                url = "https://www.indiadostichat.com/" + hf
                
            physical_urls.add(url)

print(f"Total Physical URLs found: {len(physical_urls)}")
print(f"Total URLs in sitemap.xml: {len(xml_urls)}")

missing_in_sitemap = physical_urls - xml_urls
print(f"Count of Physical URLs missing in sitemap.xml: {len(missing_in_sitemap)}")
print("--- Missing URLs (sorted) ---")
for url in sorted(list(missing_in_sitemap)):
    print(url)

extra_in_sitemap = xml_urls - physical_urls
print(f"Count of Extra URLs in sitemap.xml: {len(extra_in_sitemap)}")
print("--- Extra URLs (sorted) ---")
for url in sorted(list(extra_in_sitemap)):
    print(url)
