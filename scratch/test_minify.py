import re

def minify_js(js):
    js = re.sub(r'(?<!:)\/\/.*', '', js)
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
    lines = [line.strip() for line in js.splitlines() if line.strip()]
    return '\n'.join(lines)

code = "fetch('https://api.counterapi.dev/v1/indiadostichat_main/visitors/up')"
print("Original:", code)
print("Minified:", minify_js(code))
