import os
import re

base_dir = "."

def clean_file(file_path):
    # Skip DUNO, UNO tournament, and uno-game files
    normalized_path = file_path.replace("\\", "/").lower()
    if "duno-room" in normalized_path or "duno-tournament" in normalized_path or "uno-game" in normalized_path:
        print(f"Skipping: {file_path}")
        return 0
        
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    # Regex to find href="...index.html..."
    # Pattern: href="[path]index.html[#fragment]"
    pattern = r'href=(["\'])(.*?)(index\.html)(#.*?)?\1'
    
    def replacer(match):
        quote = match.group(1)
        path = match.group(2)
        fragment = match.group(4) if match.group(4) else ""
        
        if not path:
            new_href = f"./{fragment}"
        else:
            new_href = f"{path}{fragment}"
            
        return f'href={quote}{new_href}{quote}'
        
    new_content, count = re.subn(pattern, replacer, content)
    
    if count > 0:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {count} links in: {file_path}")
        
    return count

def main():
    total_updated = 0
    for root, dirs, files in os.walk(base_dir):
        if any(p in root for p in [".git", "scratch", "uno-game", "blog-sources"]):
            continue
        for file in files:
            if file.endswith(".html"):
                if file.startswith("google"):
                    continue
                file_path = os.path.join(root, file)
                total_updated += clean_file(file_path)
                
    print(f"Done! Cleaned a total of {total_updated} index.html link references.")

if __name__ == "__main__":
    main()
