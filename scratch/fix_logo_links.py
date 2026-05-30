import os
import re

def fix_logo_links():
    base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
    stories_dir = os.path.join(base_dir, "india-stories")
    
    updated_count = 0
    
    for root, dirs, files in os.walk(stories_dir):
        # Skip git or other system dirs if they happen to be here
        dirs[:] = [d for d in dirs if d not in ('.git', 'scratch', 'assets')]
        
        for file in files:
            if not file.endswith('.html'):
                continue
                
            filepath = os.path.join(root, file)
            
            # Calculate directory depth relative to the base directory
            # For example:
            # - base_dir is "c:\...\indiadostichat_seo"
            # - stories_dir is "c:\...\indiadostichat_seo\india-stories"
            # - root is "c:\...\indiadostichat_seo\india-stories" (file is index.html)
            #   relative path is "india-stories" -> depth is 1. Relative homepage is "../index.html".
            # - root is "c:\...\indiadostichat_seo\india-stories\indian-history"
            #   relative path is "india-stories\indian-history" -> depth is 2. Relative homepage is "../../index.html".
            # - root is "c:\...\indiadostichat_seo\india-stories\yoga-spirituality-india\yoga"
            #   relative path is "india-stories\yoga-spirituality-india\yoga" -> depth is 3. Relative homepage is "../../../index.html".
            
            rel_to_base = os.path.relpath(root, base_dir)
            # Split by path separator and filter out empty strings
            parts = [p for p in rel_to_base.split(os.sep) if p]
            depth = len(parts)
            
            # Construct relative path to the root homepage (index.html)
            relative_homepage = "../" * depth + "index.html"
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Regex callback function to replace href inside <a class="hidden-india-logo" ...>
            def repl_logo_link(match):
                tag = match.group(0)
                if 'hidden-india-logo' in tag:
                    # Replace whatever value is currently in href="..."
                    # We handle double quotes
                    new_tag = re.sub(r'href=["\'][^"\']*["\']', f'href="{relative_homepage}"', tag)
                    return new_tag
                return tag

            # Replace any <a ...> tags using the callback
            new_content = re.sub(r'<a\s+[^>]*>', repl_logo_link, content, flags=re.IGNORECASE)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated logo link in: {os.path.relpath(filepath, base_dir)} -> {relative_homepage}")
                updated_count += 1
                
    print(f"Successfully updated logo links in {updated_count} HTML files!")

if __name__ == "__main__":
    fix_logo_links()
