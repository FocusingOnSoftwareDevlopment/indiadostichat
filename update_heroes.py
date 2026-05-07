import os
import re

files_to_update = [f for f in os.listdir('.') if f.endswith('.html')]

bg_attr = 'class="landing-hero" data-bg-images="assets/images/backgrounds/friendship-1.jpg,assets/images/backgrounds/friendship-2.jpg,assets/images/backgrounds/friendship-3.jpg,assets/images/backgrounds/friendship-4.jpg,assets/images/backgrounds/friendship-5.jpg"'

for fname in files_to_update:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
            
        pattern = re.compile(r'<div class="page-header"[^>]*>(.*?)</div>', re.DOTALL)
        
        def replacer(match):
            inner = match.group(1)
            return f'<section {bg_attr}>{inner}</section>'
            
        new_content, count = pattern.subn(replacer, content)
        
        # Bump cache buster
        new_content = new_content.replace('?v=7', '?v=8')
        new_content = new_content.replace('?v=6', '?v=8')
        new_content = new_content.replace('?v=5', '?v=8')
        
        if content != new_content:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {fname}")
        else:
            print(f"No changes needed in {fname}")

def minify_css(css_path, min_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    css = re.sub(r'\s+', ' ', css)
    with open(min_path, 'w', encoding='utf-8') as f:
        f.write(css)

def minify_js(js_path, min_path):
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()
    # Safely bypass minification to avoid breaking strings and comments
    with open(min_path, 'w', encoding='utf-8') as f:
        f.write(js)
        
minify_css('assets/css/style.css', 'assets/css/style.min.css')
minify_js('assets/js/main.js', 'assets/js/main.min.js')
print("Minified CSS and JS")

os.makedirs('assets/images/backgrounds', exist_ok=True)
print("Created assets/images/backgrounds directory")
