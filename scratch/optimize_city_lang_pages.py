import os
import re

base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"

city_pages = [
    ("ahmedabad-chat-room", "Ahmedabad"),
    ("bangalore-chat-room", "Bangalore"),
    ("chennai-chat-room", "Chennai"),
    ("delhi-chat-room", "Delhi"),
    ("hyderabad-chat-room", "Hyderabad"),
    ("jaipur-chat-room", "Jaipur"),
    ("kanpur-chat-room", "Kanpur"),
    ("kolkata-chat-room", "Kolkata"),
    ("lucknow-chat-room", "Lucknow"),
    ("mumbai-chat-room", "Mumbai"),
    ("pune-chat-room", "Pune"),
    ("surat-chat-room", "Surat")
]

lang_pages = [
    ("bengali-chat-room", "Bengali"),
    ("gujarati-chat-room", "Gujarati"),
    ("kannada-chat-room", "Kannada"),
    ("malayalam-chat-room", "Malayalam"),
    ("marathi-chat-room", "Marathi"),
    ("punjabi-chat-room", "Punjabi"),
    ("tamil-chat-room", "Tamil"),
    ("telugu-chat-room", "Telugu")
]

def optimize_city_pages():
    for folder, city in city_pages:
        path = os.path.join(base_dir, folder, "index.html")
        if not os.path.exists(path):
            print(f"File not found: {path}")
            continue
            
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if already optimized in main body
        main_match = re.search(r'<main>(.*?)</main>', content, re.DOTALL)
        if main_match and "../india-chat/" in main_match.group(1):
            print(f"{city} page already optimized in body.")
            continue
            
        # We will insert a natural paragraph right at the beginning of the content section
        # Look for the container/section block
        pattern = r'(<section style="margin-bottom: 3rem;[^>]*>\s*<p>)'
        match = re.search(pattern, content)
        if not match:
            # Try a simpler match
            pattern = r'(<div class="container">\s*<section[^>]*>\s*<p>)'
            match = re.search(pattern, content)
            
        if not match:
            # Let's search for first <p> after <main>
            pattern = r'(<main>.*?(?:<div[^>]*>)?\s*<section[^>]*>\s*<p>)'
            match = re.search(pattern, content, re.DOTALL)
            
        if match:
            prefix = match.group(0)
            # Mumbai/Ahmedabad/Hyderabad/Lucknow have their own style, let's append a standard natural linking sentence
            link_text = f"{city} users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. "
            
            content = content.replace(prefix, prefix + link_text, 1)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Optimized city page: {city}")
        else:
            print(f"COULD NOT MATCH pattern in {city} page.")

def optimize_lang_pages():
    for folder, lang in lang_pages:
        path = os.path.join(base_dir, folder, "index.html")
        if not os.path.exists(path):
            print(f"File not found: {path}")
            continue
            
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        main_match = re.search(r'<main>(.*?)</main>', content, re.DOTALL)
        if main_match and "../india-chat/" in main_match.group(1):
            print(f"{lang} page already optimized in body.")
            continue
            
        # Let's insert linking sentence in the first paragraph
        pattern = r'(<section style="margin-bottom: 3rem;[^>]*>\s*<p>)'
        match = re.search(pattern, content)
        if not match:
            pattern = r'(<main>.*?(?:<div[^>]*>)?\s*<section[^>]*>\s*<p>)'
            match = re.search(pattern, content, re.DOTALL)
            
        if match:
            prefix = match.group(0)
            link_text = f"Join the main room to meet people from all over India and enjoy a lively <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> experience. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to connect. "
            content = content.replace(prefix, prefix + link_text, 1)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Optimized language page: {lang}")
        else:
            print(f"COULD NOT MATCH pattern in {lang} page.")

if __name__ == "__main__":
    optimize_city_pages()
    optimize_lang_pages()
