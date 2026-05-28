import os

base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"

def verify_all():
    errors = 0
    
    # 1. Check H1 in index.html
    index_path = os.path.join(base_dir, "index.html")
    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'class="hero-flag-heading"' not in html or "Free India Chat Room" not in html or "indian-flag.svg" not in html:
        print("ERROR: H1 heading not updated in index.html")
        errors += 1
    else:
        print("PASS: H1 heading updated successfully in index.html")
        
    # 2. Check rotating layers markup in index.html
    if 'class="hero-rotating-bg"' not in html or 'class="hero-location-badge"' not in html:
        print("ERROR: Rotating background markup or location badge missing in index.html")
        errors += 1
    else:
        print("PASS: Rotating background markup verified in index.html")

    # 3. Check WebP images
    images = [
        "mumbai-gateway.webp", "delhi-india-gate.webp", "hyderabad-charminar.webp",
        "jaipur-hawa-mahal.webp", "kerala-backwaters.webp", "kashmir-mountains.webp",
        "varanasi-ghats.webp", "goa-beach.webp", "india-festival-lights.webp"
    ]
    img_dir = os.path.join(base_dir, "assets", "images", "home-hero")
    for img in images:
        p = os.path.join(img_dir, img)
        if not os.path.exists(p):
            print(f"ERROR: Image missing: {img}")
            errors += 1
        elif os.path.getsize(p) < 1000:
            print(f"ERROR: Image file is too small/empty: {img}")
            errors += 1
        else:
            print(f"PASS: Image verified: {img} ({os.path.getsize(p)} bytes)")

    # 4. Check CSS styles
    css_path = os.path.join(base_dir, "assets", "css", "style.css")
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    required_classes = [".hero-rotating-bg", ".hero-bg-layer", ".hero-bg-overlay", ".hero-location-badge", ".hero-location-text", "h1.hero-flag-heading"]
    for c in required_classes:
        if c not in css:
            print(f"ERROR: CSS class missing in style.css: {c}")
            errors += 1
        else:
            print(f"PASS: CSS class found: {c}")

    # 5. Check JS code
    js_path = os.path.join(base_dir, "assets", "js", "main.js")
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()
    if "heroBgLayers" not in js or "mumbai-gateway.webp" not in js:
        print("ERROR: JS slider code missing in main.js")
        errors += 1
    else:
        print("PASS: JS slider code found in main.js")
        
    print(f"\nVerification finished with {errors} errors.")
    return errors == 0

if __name__ == "__main__":
    verify_all()
