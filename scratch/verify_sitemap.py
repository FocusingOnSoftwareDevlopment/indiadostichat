import os
import re
import urllib.request
import urllib.error
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer

sitemap_path = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\sitemap.xml"
project_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"

# 1. Parse sitemap.xml to extract all URLs
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

url_pattern = re.compile(r'<loc>(.*?)</loc>')
urls = [u.strip() for u in url_pattern.findall(sitemap_content)]

print(f"Total URLs in sitemap: {len(urls)}")

# 2. Setup a local server running in a background thread
PORT = 8012
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass # Suppress logging to keep output clean

server = HTTPServer(('localhost', PORT), QuietHandler)

def start_server():
    # Change working directory to project root so SimpleHTTPRequestHandler serves files from there
    os.chdir(project_dir)
    server.serve_forever()

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()
print(f"Started local server on port {PORT}...")

# 3. Test each URL
failures = []
noindex_failures = []
html_extension_failures = []
non_200_failures = []

for url in urls:
    # Check if URL ends with .html
    if ".html" in url:
        html_extension_failures.append(url)
        
    # Rewrite live URL to local server URL
    local_url = url.replace("https://www.indiadostichat.com", f"http://localhost:{PORT}")
    
    try:
        req = urllib.request.Request(local_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            status = response.status
            html = response.read().decode('utf-8')
            
            if status != 200:
                non_200_failures.append((url, f"Status {status}"))
            else:
                # Check for noindex in the HTML content
                if 'noindex' in html.lower() and ('robots' in html.lower() or 'name="robots"' in html.lower()):
                    # double check with regex
                    meta_robots = re.search(r'<meta\s+name=["\']robots["\']\s+content=["\']([^"\']*noindex[^"\']*)["\']', html, re.IGNORECASE)
                    if meta_robots:
                        noindex_failures.append((url, meta_robots.group(0)))
                        
    except urllib.error.HTTPError as e:
        non_200_failures.append((url, f"HTTP Error {e.code}"))
    except urllib.error.URLError as e:
        non_200_failures.append((url, f"URL Error {e.reason}"))
    except Exception as e:
        non_200_failures.append((url, f"Exception: {str(e)}"))

# Shut down the server
server.shutdown()
print("Stopped local server.")

# 4. Report results
print("\n=== VERIFICATION REPORT ===")
print(f"Total tested URLs: {len(urls)}")
print(f"Total India Stories URLs: {len([u for u in urls if '/india-stories/' in u])}")

print(f"\n1. Confirm no .html extension URLs in loc tags:")
if html_extension_failures:
    print(f"   [FAIL] Found {len(html_extension_failures)} URLs with .html:")
    for u in html_extension_failures:
        print(f"     - {u}")
else:
    print("   [PASS] No .html URLs found.")

print(f"\n2. Confirm all URLs return HTTP 200:")
if non_200_failures:
    print(f"   [FAIL] Found {len(non_200_failures)} failed URLs:")
    for u, err in non_200_failures:
        print(f"     - {u}: {err}")
else:
    print("   [PASS] All URLs returned HTTP 200 successfully.")

print(f"\n3. Confirm no page contains noindex:")
if noindex_failures:
    print(f"   [FAIL] Found {len(noindex_failures)} pages marked noindex:")
    for u, tag in noindex_failures:
        print(f"     - {u}: {tag}")
else:
    print("   [PASS] No pages contain noindex.")

if not html_extension_failures and not non_200_failures and not noindex_failures:
    print("\nSUCCESS: All sitemap URLs are valid, indexable, clean, and return 200 OK.")
else:
    print("\nFAILURE: Some validation checks failed. Please fix before publishing.")
