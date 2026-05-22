import re

def minify_js(js):
    # Let's see what each step does
    print("Before comment removal:", [line for line in js.splitlines() if 'counterapi' in line])
    js = re.sub(r'(?<!:)\/\/.*', '', js)
    print("After comment removal:", [line for line in js.splitlines() if 'counterapi' in line])
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
    lines = [line.strip() for line in js.splitlines() if line.strip()]
    return '\n'.join(lines)

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

minified = minify_js(js)
print("Contains counterapi:", 'counterapi' in minified)
if 'counterapi' not in minified:
    # Let's find where 'https:' is
    lines = [line for line in minified.splitlines() if 'https:' in line]
    print("Lines containing https:", lines[:5])
