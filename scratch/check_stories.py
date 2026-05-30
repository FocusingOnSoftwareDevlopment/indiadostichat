import os
import re
from bs4 import BeautifulSoup

stories_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\india-stories"

html_files = []
for root, dirs, files in os.walk(stories_dir):
    for file in files:
        if file.endswith('.html'):
            full_path = os.path.join(root, file)
            html_files.append(full_path)

print(f"Total HTML files found: {len(html_files)}")

noindex_pages = []
placeholder_pages = []
clean_urls = []
mismatch_canonicals = []

for filepath in sorted(html_files):
    rel_path = os.path.relpath(filepath, stories_dir)
    # clean folder URL path
    clean_path = rel_path.replace('\\', '/')
    if clean_path == "index.html":
        url_subpath = ""
    elif clean_path.endswith("/index.html"):
        url_subpath = clean_path[:-10]  # strip index.html
    else:
        url_subpath = clean_path
    
    expected_canonical = f"https://www.indiadostichat.com/india-stories/{url_subpath}"
    if url_subpath == "":
        expected_canonical = "https://www.indiadostichat.com/india-stories/"
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    
    # Check noindex
    robots = soup.find('meta', attrs={'name': 'robots'})
    has_noindex = False
    if robots:
        robots_content = robots.get('content', '').lower()
        if 'noindex' in robots_content:
            has_noindex = True
            noindex_pages.append((rel_path, robots_content))
            
    # Check canonical
    canonical = soup.find('link', rel='canonical')
    canonical_href = canonical.get('href', '') if canonical else None
    
    if canonical_href != expected_canonical:
        mismatch_canonicals.append((rel_path, canonical_href, expected_canonical))
        
    # Check placeholder/unfinished indicators
    # Examples: empty body, very small text, "coming soon", "placeholder", "lorem ipsum", "draft"
    body_text = soup.body.get_text() if soup.body else ""
    text_len = len(body_text.strip())
    
    is_placeholder = False
    re_placeholder = re.compile(r'coming soon|placeholder|lorem ipsum|todo|under construction', re.I)
    match_placeholder = re_placeholder.search(body_text)
    
    if text_len < 500 or match_placeholder:
        is_placeholder = True
        placeholder_pages.append((rel_path, text_len, match_placeholder.group(0) if match_placeholder else "Too short"))
        
    if not has_noindex and not is_placeholder:
        clean_urls.append(expected_canonical)

print("\n--- NOINDEX PAGES ---")
for p, reason in noindex_pages:
    print(f"{p}: {reason}")

print("\n--- PLACEHOLDER / UNFINISHED PAGES ---")
for p, length, reason in placeholder_pages:
    print(f"{p}: length={length}, reason='{reason}'")

print("\n--- MISMATCHED CANONICALS ---")
for p, got, expected in mismatch_canonicals:
    print(f"{p}: got='{got}', expected='{expected}'")

print(f"\nTotal indexable URLs found: {len(clean_urls)}")
