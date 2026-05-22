import re

def minify_js(js):
    pattern = re.compile(
        r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|`(?:[^`\\]|\\.)*`|/\*[\s\S]*?\*/|//.*)'
    )
    def replacer(match):
        s = match.group(0)
        if s.startswith('/*') or s.startswith('//'):
            return ''
        return s
    js = pattern.sub(replacer, js)
    
    # Simple whitespace removal outside of strings is harder without full parser,
    # but we can at least strip lines and remove empty lines:
    lines = [line.strip() for line in js.splitlines() if line.strip()]
    return '\n'.join(lines)

code = """
// this is a comment
const x = "https://example.com"; // URL in double quotes
const y = 'https://example.com'; // URL in single quotes
const z = `https://example.com`; // URL in template literal
/* multiline
   comment */
console.log(x, y, z);
"""
print("Result:\n", minify_js(code))
