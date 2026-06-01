import os

base_dir = "."
search_terms = ["money-talk", "money-chat", "404", "mumbai-chat-room.html", "chat.html", "about.html", "contact.html"]

for root, dirs, files in os.walk(base_dir):
    if any(p in root for p in [".git", "scratch", "uno-game"]):
        continue
    for file in files:
        if file.endswith((".html", ".xml", ".txt", ".json", ".js", ".css")):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                for term in search_terms:
                    if term in content:
                        # Find line number
                        lines = content.splitlines()
                        for i, line in enumerate(lines):
                            if term in line:
                                print(f"Found '{term}' in {file_path} on line {i+1}: {line.strip()[:100]}")
            except Exception as e:
                pass
