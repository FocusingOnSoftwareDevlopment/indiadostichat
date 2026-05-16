import os
import re

def migrate_pages(root_dir):
    subdirs = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d)) and os.path.exists(os.path.join(root_dir, d, 'index.html'))]
    
    for subdir in subdirs:
        if subdir in ['.git', 'assests', 'assets', 'scratch']:
            continue
            
        index_path = os.path.join(root_dir, subdir, 'index.html')
        target_path = os.path.join(root_dir, f"{subdir}.html")
        
        print(f"Migrating {index_path} -> {target_path}")
        
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Update relative asset paths (../assets/ -> assets/)
        content = content.replace('="../assets/', '="assets/')
        content = content.replace('="../js/', '="js/')
        content = content.replace('="../css/', '="css/')
        
        # 2. Update canonical tag to .html
        content = re.sub(r'href="https://www\.indiadostichat\.com/([^/"]+)/"', r'href="https://www.indiadostichat.com/\1.html"', content)
        
        # 3. Update internal links
        # Link to home
        content = content.replace('href="../"', 'href="./"')
        content = content.replace('href="../index.html"', 'href="index.html"')
        
        # Links like href="../chat/" or href="./chat/" or href="chat/"
        # We need to be careful with regex.
        content = re.sub(r'href="(?:\.\./|\./|)([^/"]+)/"', r'href="\1.html"', content)
        
        # Handle the edge case of "..html" or ".html" that might have been created
        content = content.replace('href="..html"', 'href="./"')
        content = content.replace('href=".html"', 'href="./"')
        
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
    # Update root files
    for root_file in os.listdir(root_dir):
        if root_file.endswith('.html') and os.path.isfile(os.path.join(root_dir, root_file)):
            file_path = os.path.join(root_dir, root_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Update links like href="chat/" to href="chat.html"
            content = re.sub(r'href="(?:\./|)([^/"]+)/"', r'href="\1.html"', content)
            
            # Fix any accidentally created ..html
            content = content.replace('href="..html"', 'href="./"')
            content = content.replace('href=".html"', 'href="./"')
            
            # Canonical check for root files
            if root_file != 'index.html':
                canonical_pattern = f'href="https://www\\.indiadostichat\\.com/{root_file.replace(".html", "")}/"'
                content = content.replace(canonical_pattern, f'href="https://www.indiadostichat.com/{root_file}"')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

migrate_pages('.')
print("Migration fixed and completed.")
