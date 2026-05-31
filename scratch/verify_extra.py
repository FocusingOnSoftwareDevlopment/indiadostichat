import os
import re

base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
topics_dir = os.path.join(base_dir, "topics")
images_dir = os.path.join(base_dir, "assets", "images", "topics")

slugs = [
    "money-chat",
    "korea-chat",
    "japan-chat",
    "anime-chat",
    "kpop-chat",
    "travel-chat",
    "food-chat",
    "gaming-chat",
    "ai-chat",
    "international-friendship-chat"
]

print("=== EXTRA VERIFICATION RUN ===")

# 1. Verify Image Sizes
print("\n1. Verifying image file sizes:")
image_errors = 0
for slug in slugs:
    main_img = f"{slug}.webp"
    thumb_img = f"{slug}-thumb.webp"
    
    main_path = os.path.join(images_dir, main_img)
    thumb_path = os.path.join(images_dir, thumb_img)
    
    if not os.path.exists(main_path):
        print(f"  [FAIL] Main image missing: {main_path}")
        image_errors += 1
    else:
        sz = os.path.getsize(main_path)
        if sz > 60 * 1024:
            print(f"  [FAIL] {main_img} size is {sz} bytes (exceeds 60 KB)")
            image_errors += 1
        else:
            print(f"  [PASS] {main_img}: {sz} bytes")
            
    if not os.path.exists(thumb_path):
        print(f"  [FAIL] Thumbnail image missing: {thumb_path}")
        image_errors += 1
    else:
        sz = os.path.getsize(thumb_path)
        if sz > 25 * 1024:
            print(f"  [FAIL] {thumb_img} size is {sz} bytes (exceeds 25 KB)")
            image_errors += 1
        else:
            print(f"  [PASS] {thumb_img}: {sz} bytes")

if image_errors == 0:
    print("  [ALL PASS] All topic images are within size limits.")

# 2. Verify Page HTML Structure
print("\n2. Verifying page HTML structure:")
html_errors = 0

# Check index page
index_path = os.path.join(topics_dir, "index.html")
if not os.path.exists(index_path):
    print("  [FAIL] Topics index page missing!")
    html_errors += 1
else:
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", content, re.IGNORECASE)
    if len(h1s) != 1:
        print(f"  [FAIL] Index has {len(h1s)} H1 tags (expected 1)")
        html_errors += 1
    else:
        print("  [PASS] Index H1 tags count is 1")
        
    canonical = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](https://www.indiadostichat.com/topics/)["\']', content, re.IGNORECASE)
    if not canonical:
        print("  [FAIL] Index canonical tag is incorrect or missing")
        html_errors += 1
    else:
        print("  [PASS] Index canonical is correct")

# Check subpages
for slug in slugs:
    page_path = os.path.join(topics_dir, slug, "index.html")
    if not os.path.exists(page_path):
        print(f"  [FAIL] Page missing: {page_path}")
        html_errors += 1
        continue
        
    with open(page_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check H1
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", content, re.IGNORECASE)
    if len(h1s) != 1:
        print(f"  [FAIL] {slug} has {len(h1s)} H1 tags (expected 1)")
        html_errors += 1
    else:
        # Check canonical
        expected_canonical = f"https://www.indiadostichat.com/topics/{slug}/"
        canonical = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']' + re.escape(expected_canonical) + r'["\']', content, re.IGNORECASE)
        if not canonical:
            print(f"  [FAIL] {slug} canonical tag is incorrect or missing (expected {expected_canonical})")
            html_errors += 1
        
        # Check CSS and JS versions
        css_match = "style.min.css?v=25" in content
        js_match = "main.min.js?v=20" in content
        
        if not css_match:
            print(f"  [FAIL] {slug} is not using style.min.css?v=25")
            html_errors += 1
        if not js_match:
            print(f"  [FAIL] {slug} is not using main.min.js?v=20")
            html_errors += 1
            
        # Check no Font Awesome link
        fa_match = "cdnjs.cloudflare.com/ajax/libs/font-awesome" in content
        if fa_match:
            print(f"  [FAIL] {slug} loads Font Awesome CSS from CDN (violates performance constraints)")
            html_errors += 1

if html_errors == 0:
    print("  [ALL PASS] All HTML structures, canonical tags, and style/script versions are correct.")

print("\nExtra verification completed!")
