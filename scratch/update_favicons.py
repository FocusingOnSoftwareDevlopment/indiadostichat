import os
import re

def update_favicons_in_html():
    base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
    
    # New standardized favicon block
    new_favicon_block = """    <!-- Favicon -->
    <link rel="icon" href="/favicon.ico?v=3" sizes="any">
    <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png?v=3">
    <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png?v=3">
    <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png?v=3">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=3">
    <link rel="manifest" href="/site.webmanifest?v=3">"""

    # Regex patterns to find and remove old favicon tags
    patterns_to_remove = [
        r'^\s*<link[^>]*rel=["\'](?:shortcut\s+)?icon["\'][^>]*>\s*$',
        r'^\s*<link[^>]*rel=["\']apple-touch-icon["\'][^>]*>\s*$',
        r'^\s*<link[^>]*rel=["\']manifest["\'][^>]*>\s*$',
        r'^\s*<!--\s*Favicon\s*-->\s*$'  # Remove old comment line to avoid duplicates
    ]
    
    compiled_patterns = [re.compile(pat, re.MULTILINE | re.IGNORECASE) for pat in patterns_to_remove]
    
    updated_count = 0
    
    for root, dirs, files in os.walk(base_dir):
        # Exclude directories we don't want to modify
        dirs[:] = [d for d in dirs if d not in ('.git', 'scratch', 'assets', 'node_modules', '.github')]
        
        for file in files:
            if not file.endswith('.html'):
                continue
                
            filepath = os.path.join(root, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Perform cleanup line-by-line
            lines = content.split('\n')
            cleaned_lines = []
            removed_any = False
            
            for line in lines:
                should_remove = False
                for pat in compiled_patterns:
                    if pat.match(line):
                        should_remove = True
                        removed_any = True
                        break
                if not should_remove:
                    cleaned_lines.append(line)
                    
            cleaned_content = '\n'.join(cleaned_lines)
            
            # Now, locate </head> (case insensitive) and inject the new block
            head_end_pat = re.compile(r'(\s*)</head>', re.IGNORECASE)
            
            match = head_end_pat.search(cleaned_content)
            if match:
                indent = match.group(1) or "    "
                # Indent our new block lines nicely to match the file's indentation
                indented_block = "\n".join(
                    line if not line.strip() else (indent + line.lstrip())
                    for line in new_favicon_block.split('\n')
                )
                
                # Replace </head> with our block followed by </head>
                replacement = f"{indented_block}\n{indent}</head>"
                final_content = head_end_pat.sub(replacement, cleaned_content, count=1)
                
                # Write back if there is any change
                if final_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(final_content)
                    print(f"Updated: {os.path.relpath(filepath, base_dir)}")
                    updated_count += 1
            else:
                print(f"WARNING: Could not find </head> tag in {os.path.relpath(filepath, base_dir)}")
                
    print(f"Successfully updated {updated_count} HTML files!")

if __name__ == "__main__":
    update_favicons_in_html()
