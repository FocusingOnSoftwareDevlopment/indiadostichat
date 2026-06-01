import os
from bs4 import BeautifulSoup

base_dir = "./topics"

def check_topic_page(dir_path):
    index_path = os.path.join(dir_path, "index.html")
    if not os.path.exists(index_path):
        print(f"Directory {dir_path} has no index.html")
        return None
        
    with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        
    soup = BeautifulSoup(content, "html.parser")
    
    # Check H1
    h1s = soup.find_all("h1")
    h1_count = len(h1s)
    h1_text = h1s[0].get_text().strip() if h1s else "None"
    
    # Check Title
    title = soup.title.get_text().strip() if soup.title else "None"
    
    # Check Description
    meta_desc = soup.find("meta", attrs={"name": "description"})
    desc = meta_desc.get("content", "").strip() if meta_desc else "None"
    
    # Check Canonical
    canonical_tag = soup.find("link", rel="canonical")
    canonical = canonical_tag.get("href", "").strip() if canonical_tag else "None"
    
    # Check Noindex
    meta_robots = soup.find("meta", attrs={"name": "robots"})
    noindex = False
    if meta_robots:
        robots_content = meta_robots.get("content", "").lower()
        if "noindex" in robots_content:
            noindex = True
            
    # Check if uses clean folder URL in canonical
    rel_dir = os.path.relpath(dir_path, ".").replace("\\", "/")
    if rel_dir == "topics":
        expected_canonical = "https://www.indiadostichat.com/topics/"
    else:
        # e.g., topics/food-chat
        expected_canonical = f"https://www.indiadostichat.com/{rel_dir}/"
        
    canonical_correct = (canonical == expected_canonical)
    
    return {
        "path": index_path,
        "h1_count": h1_count,
        "h1_text": h1_text,
        "title": title,
        "description": desc,
        "canonical": canonical,
        "canonical_correct": canonical_correct,
        "expected_canonical": expected_canonical,
        "noindex": noindex
    }

def main():
    print("Scanning topics directories...")
    dirs_to_check = [base_dir]
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path):
            dirs_to_check.append(item_path)
            
    for d in dirs_to_check:
        res = check_topic_page(d)
        if res:
            print(f"\nPage: {res['path']}")
            print(f"  H1 count: {res['h1_count']} (Text: '{res['h1_text']}')")
            print(f"  Title: '{res['title']}'")
            print(f"  Description: '{res['description']}'")
            print(f"  Canonical: '{res['canonical']}' (Expected: '{res['expected_canonical']}' - Correct: {res['canonical_correct']})")
            print(f"  Noindex: {res['noindex']}")

if __name__ == "__main__":
    main()
