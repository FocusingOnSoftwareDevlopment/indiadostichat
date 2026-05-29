import os
import re

def update_js_version():
    base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
    pattern = re.compile(r'main\.min\.js\?v=\d+')
    
    updated_files = 0
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in ('.git', 'assets', 'node_modules', '.github')]
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if pattern.search(content):
                    new_content = pattern.sub('main.min.js?v=17', content)
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        rel_path = os.path.relpath(filepath, base_dir)
                        print(f"Updated JS version to v=17 in {rel_path}")
                        updated_files += 1

    print(f"Completed! Updated {updated_files} HTML files.")

if __name__ == "__main__":
    update_js_version()
