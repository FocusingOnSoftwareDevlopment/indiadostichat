import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

base_dir = "."
site_domain = "www.indiadostichat.com"
site_url = f"https://{site_domain}"

# Find all HTML files to check
html_files = []
for root, dirs, files in os.walk(base_dir):
    # Exclude directories we shouldn't touch or index
    if any(p in root for p in [".git", "scratch", "uno-game", "blog-sources"]):
        continue
    for file in files:
        if file.endswith(".html"):
            # Exclude google verification file
            if file.startswith("google"):
                continue
            html_files.append(os.path.relpath(os.path.join(root, file), base_dir))

print(f"Analyzing {len(html_files)} HTML files...")

# Map of clean path to relative file path
# e.g., "" or "/" -> "index.html"
# "about/" -> "about/index.html"
# "duno-tournament.html" -> "duno-tournament.html"
url_to_file = {}
for hf in html_files:
    clean_path = hf.replace("\\", "/")
    if clean_path == "index.html":
        url_to_file[""] = hf
        url_to_file["/"] = hf
    elif clean_path.endswith("/index.html"):
        path = clean_path[:-10] # remove "index.html"
        url_to_file[path] = hf
        url_to_file[path + "/"] = hf
        url_to_file["/" + path + "/"] = hf
        url_to_file["/" + path] = hf
    else:
        url_to_file[clean_path] = hf
        url_to_file["/" + clean_path] = hf

# Let's verify each page
canonical_issues = []
noindex_pages = []
broken_links = []
html_extension_links = []

for hf in html_files:
    file_path = os.path.join(base_dir, hf)
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    
    # 1. Check Canonical tag
    canonical_tag = soup.find("link", rel="canonical")
    if not canonical_tag:
        canonical_issues.append((hf, "No canonical tag found"))
    else:
        href = canonical_tag.get("href", "")
        if not href.startswith(site_url):
            canonical_issues.append((hf, f"Canonical does not start with {site_url}: {href}"))
        elif ".html" in href:
            canonical_issues.append((hf, f"Canonical contains .html: {href}"))
        else:
            # Check if it has a trailing slash (unless homepage)
            expected_href = site_url
            clean_path = hf.replace("\\", "/")
            if clean_path != "index.html":
                if clean_path.endswith("/index.html"):
                    expected_href = site_url + "/" + clean_path[:-10]
                else:
                    expected_href = site_url + "/" + clean_path
            
            # Normalize to check
            if href != expected_href:
                # Let's check trailing slash
                if expected_href.endswith("/") and href != expected_href:
                    canonical_issues.append((hf, f"Canonical mismatch. Expected: {expected_href}, Got: {href}"))
                elif not expected_href.endswith("/") and href != expected_href + "/":
                    # If it's a subpage (non-index.html), it should have trailing slash
                    if expected_href != site_url and not href.endswith("/"):
                        canonical_issues.append((hf, f"Canonical mismatch (no trailing slash). Expected: {expected_href}/, Got: {href}"))
                    elif href != expected_href + "/" and href != expected_href:
                        canonical_issues.append((hf, f"Canonical mismatch. Expected: {expected_href}/, Got: {href}"))

    # 2. Check noindex
    robots_meta = soup.find("meta", attrs={"name": "robots"})
    if robots_meta:
        robots_content = robots_meta.get("content", "").lower()
        if "noindex" in robots_content:
            noindex_pages.append(hf)

    # 3. Check Links
    a_tags = soup.find_all("a")
    for a in a_tags:
        href = a.get("href", "")
        if not href:
            continue
        
        # Check if internal link has .html
        if "google" not in href and "uno-game" not in href and not href.startswith("http") and not href.startswith("//"):
            if ".html" in href:
                if href.endswith("index.html") or "index.html" in href:
                    # It's an index.html link
                    html_extension_links.append((hf, href, "index.html link", a.text.strip()))
                else:
                    # It's another .html link
                    html_extension_links.append((hf, href, "non-index.html link", a.text.strip()))
        
        # Check if internal link
        is_internal = False
        parsed_href = urlparse(href)
        if not parsed_href.scheme and not parsed_href.netloc:
            # relative or absolute path
            is_internal = True
            link_path = parsed_href.path
        elif parsed_href.netloc == site_domain:
            is_internal = True
            link_path = parsed_href.path
        
        if is_internal:
            # Remove hash or query params for checking file existence
            link_path_clean = link_path
            if not link_path_clean or link_path_clean == "#":
                continue
            
            # Resolve link path relative to current file if it's relative
            if not link_path_clean.startswith("/"):
                # Relative link
                dir_of_file = os.path.dirname(hf.replace("\\", "/"))
                resolved_path = urljoin(dir_of_file + "/", link_path_clean)
            else:
                resolved_path = link_path_clean.lstrip("/")
            
            # Check if this resolves to a file
            file_exists = False
            check_paths = [
                resolved_path,
                resolved_path + "/index.html" if not resolved_path.endswith(".html") else resolved_path,
                resolved_path + "index.html" if resolved_path.endswith("/") else resolved_path,
                os.path.join(resolved_path, "index.html") if not resolved_path.endswith(".html") else resolved_path
            ]
            
            for cp in check_paths:
                cp_normalized = os.path.normpath(cp).replace("\\", "/")
                # Remove leading dots or slashes
                cp_normalized = cp_normalized.lstrip("./").lstrip("/")
                if cp_normalized == "" or cp_normalized == "index.html":
                    if os.path.exists("index.html"):
                        file_exists = True
                        break
                elif os.path.exists(cp_normalized) and os.path.isfile(cp_normalized):
                    file_exists = True
                    break
            
            if not file_exists:
                broken_links.append((hf, href, resolved_path, a.text.strip()))

# Output Results
print("\n--- Canonical Issues ---")
print(f"Total canonical issues: {len(canonical_issues)}")
for issue in canonical_issues[:15]:
    print(f"File: {issue[0]} -> {issue[1]}")

print("\n--- Noindex Pages ---")
print(f"Total noindex pages: {len(noindex_pages)}")
for p in noindex_pages:
    print(p)

print("\n--- Broken Internal Links (404) ---")
print(f"Total broken links: {len(broken_links)}")
for bl in broken_links[:20]:
    print(f"In File: {bl[0]} -> Link: '{bl[1]}' (Resolves to: '{bl[2]}') [Text: '{bl[3]}']")

print("\n--- HTML Extension Links ---")
index_links = [hel for hel in html_extension_links if hel[2] == "index.html link"]
non_index_links = [hel for hel in html_extension_links if hel[2] == "non-index.html link"]
print(f"Total index.html links: {len(index_links)}")
print(f"Total non-index.html links: {len(non_index_links)}")
print("\n--- Non-index.html links (sample):")
for hel in non_index_links[:30]:
    print(f"In File: {hel[0]} -> Link: '{hel[1]}' [Text: '{hel[3]}']")

