import os
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

sitemap_xml_path = "sitemap.xml"
sitemap_html_path = "sitemap/index.html"

# Parse XML sitemap
xml_urls = set()
if os.path.exists(sitemap_xml_path):
    tree = ET.parse(sitemap_xml_path)
    root = tree.getroot()
    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    for loc in root.findall('.//sm:loc', ns):
        xml_urls.add(loc.text.strip())

# Parse HTML sitemap
html_links = set()
if os.path.exists(sitemap_html_path):
    with open(sitemap_html_path, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    for a in soup.find_all("a"):
        href = a.get("href", "")
        if not href.startswith("http") and not href.startswith("//"):
            # relative link, resolve it to absolute URL
            # sitemap/index.html is inside sitemap/ folder, so relative to root is href
            # wait, if href is "../chat/", relative to sitemap/ is "../chat/", which resolves to root/chat/
            if href.startswith("../"):
                clean_href = href[3:]
            else:
                clean_href = href
            abs_url = f"https://www.indiadostichat.com/{clean_href}"
            # normalize trailing slash
            if not abs_url.endswith("/") and "." not in abs_url.split("/")[-1]:
                abs_url += "/"
            html_links.add(abs_url)

print(f"Total XML sitemap URLs: {len(xml_urls)}")
print(f"Total HTML sitemap links: {len(html_links)}")

diff_xml_only = xml_urls - html_links
diff_html_only = html_links - xml_urls

print(f"\nURLs in XML but not in HTML sitemap ({len(diff_xml_only)}):")
for url in sorted(list(diff_xml_only))[:20]:
    print(url)

print(f"\nURLs in HTML but not in XML sitemap ({len(diff_html_only)}):")
for url in sorted(list(diff_html_only))[:20]:
    print(url)
