import os

stories_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\india-stories"

modified_count = 0
for root, dirs, files in os.walk(stories_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # check if it has the noindex meta
            # We want to replace it regardless of exact whitespace/case
            # but usually it's `<meta name="robots" content="noindex, nofollow">`
            # Let's use a regex replace to be completely safe
            import re
            pattern = re.compile(r'<meta\s+name=["\']robots["\']\s+content=["\']noindex,\s*nofollow["\']\s*/?>', re.IGNORECASE)
            
            if pattern.search(content):
                new_content = pattern.sub('<meta name="robots" content="index, follow">', content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                modified_count += 1
                print(f"Updated: {os.path.relpath(filepath, stories_dir)}")

print(f"\nCompleted! Total files updated: {modified_count}")
