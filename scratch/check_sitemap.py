import os
import xml.etree.ElementTree as ET

def check_sitemap(sitemap_path, root_dir):
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = root.findall('ns:url/ns:loc', ns)
    
    missing = []
    for url in urls:
        path = url.text.replace('https://www.indiadostichat.com/', '')
        if not path or path == '/':
            full_path = os.path.join(root_dir, 'index.html')
        elif path.endswith('/'):
            full_path = os.path.join(root_dir, path.strip('/'), 'index.html')
        else:
            full_path = os.path.join(root_dir, path)
            
        if not os.path.exists(full_path):
            missing.append((url.text, full_path))
            
    return missing

missing = check_sitemap('sitemap.xml', '.')
if missing:
    print("Missing pages found in sitemap:")
    for url, path in missing:
        print(f"URL: {url} -> Path: {path}")
else:
    print("All sitemap URLs exist in the file system.")
