with open("sitemap.xml", "r", encoding="utf-8") as f:
    lines = f.readlines()

search_terms = ["chat-room", "mumbai", "kannada", "duno-tournament", "delhi", "bangalore"]

for term in search_terms:
    print(f"=== Matches for '{term}' ===")
    found = False
    for i, line in enumerate(lines):
        if term in line.lower():
            print(f"Line {i+1}: {line.strip()}")
            found = True
    if not found:
        print("No matches")
