import re
import os

def minify_css(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r' ?\{ ?', '{', css)
    css = re.sub(r' ?\} ?', '}', css)
    css = re.sub(r' ?: ?', ':', css)
    css = re.sub(r' ?; ?', ';', css)
    css = re.sub(r' ?, ?', ',', css)
    return css.strip()

def minify_js(js):
    js = re.sub(r'(?<!:)\/\/.*', '', js)
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
    lines = [line.strip() for line in js.splitlines() if line.strip()]
    return '\n'.join(lines)

# Update HTML files version to v=10
files = [f for f in os.listdir('.') if f.endswith('.html')]
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace('?v=9"', '?v=10"')
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

# Minify
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()
with open('assets/css/style.min.css', 'w', encoding='utf-8') as f:
    f.write(minify_css(css))

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()
with open('assets/js/main.min.js', 'w', encoding='utf-8') as f:
    f.write(minify_js(js))

print("Updated to Version 10.0")
