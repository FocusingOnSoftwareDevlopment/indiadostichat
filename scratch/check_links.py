import os
import re
from urllib.parse import urljoin, urlparse

def get_links_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    return re.findall(r'href="([^"]+)"', content)

def check_links(root_dir):
    html_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
                
    broken_links = []
    for html_file in html_files:
        links = get_links_from_file(html_file)
        rel_dir = os.path.dirname(html_file)
        
        for link in links:
            if link.startswith(('http', 'mailto:', 'tel:', '#')):
                continue
                
            # Normalize link
            clean_link = link.split('?')[0].split('#')[0]
            if not clean_link:
                continue
                
            if clean_link.startswith('/'):
                target_path = os.path.join(root_dir, clean_link.lstrip('/'))
            else:
                target_path = os.path.join(rel_dir, clean_link)
                
            # Check if directory or file exists
            if os.path.isdir(target_path):
                # Check for index.html in directory
                if not os.path.exists(os.path.join(target_path, 'index.html')):
                    broken_links.append((html_file, link, target_path))
            elif not os.path.exists(target_path):
                # Try adding .html if not present
                if not clean_link.endswith('.html') and os.path.exists(target_path + '.html'):
                    continue
                broken_links.append((html_file, link, target_path))
                
    return broken_links

broken = check_links('.')
if broken:
    print("Broken links found:")
    for src, link, target in broken:
        print(f"File: {src} -> Link: {link} -> Target Path: {target}")
else:
    print("No broken internal links found.")
