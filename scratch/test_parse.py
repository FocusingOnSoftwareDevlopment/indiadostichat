import os

downloads_dir = r"C:\Users\mks1j\Downloads\files"
fallback_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\blog-sources\files"

def get_file_path(filename):
    p1 = os.path.join(downloads_dir, filename)
    if os.path.exists(p1):
        return p1
    p2 = os.path.join(fallback_dir, filename)
    if os.path.exists(p2):
        return p2
    raise FileNotFoundError(f"Could not find {filename} in {downloads_dir} or {fallback_dir}")

# Test 1: parse Indian_Korean_Friendship_Blog.txt
friendship_path = get_file_path("Indian_Korean_Friendship_Blog.txt")
with open(friendship_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

print("--- Friendship Blog First Lines ---")
for i, line in enumerate(lines[:10]):
    print(f"{i}: {line}")
