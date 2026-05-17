import os

def update_footers():
    base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
    
    # 1. Update root index.html
    root_file = os.path.join(base_dir, "index.html")
    if os.path.exists(root_file):
        with open(root_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        target = '<li><a href="india-chat/" style="color: #ccc; text-decoration: none;">India Chat</a></li>'
        replacement = '<li><a href="india-chat/" style="color: #ccc; text-decoration: none;">India Chat</a></li>\n                    <li><a href="allindiachat/" style="color: #ccc; text-decoration: none;">All India Chat</a></li>'
        
        if target in content and "allindiachat/" not in content:
            new_content = content.replace(target, replacement)
            with open(root_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Updated root index.html footer link successfully.")

    # 2. Update subdirectory index.html files
    for root, dirs, files in os.walk(base_dir):
        # Exclude git and assets
        if ".git" in root or "assets" in root:
            continue
        
        for file in files:
            if file == "index.html" and root != base_dir:
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                target = '<li><a href="../india-chat/" style="color: #ccc; text-decoration: none;">India Chat</a></li>'
                replacement = '<li><a href="../india-chat/" style="color: #ccc; text-decoration: none;">India Chat</a></li>\n                    <li><a href="../allindiachat/" style="color: #ccc; text-decoration: none;">All India Chat</a></li>'
                
                if target in content and "allindiachat/" not in content:
                    new_content = content.replace(target, replacement)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated footer in {filepath}")

if __name__ == "__main__":
    update_footers()
