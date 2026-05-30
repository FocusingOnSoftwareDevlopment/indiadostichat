import os
import re

base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
city_pages = [
    "ahmedabad-chat-room", "bangalore-chat-room", "chennai-chat-room", "delhi-chat-room",
    "hyderabad-chat-room", "jaipur-chat-room", "kanpur-chat-room", "kolkata-chat-room",
    "lucknow-chat-room", "mumbai-chat-room", "pune-chat-room", "surat-chat-room"
]
lang_pages = [
    "bengali-chat-room", "gujarati-chat-room", "kannada-chat-room", "malayalam-chat-room",
    "marathi-chat-room", "punjabi-chat-room", "tamil-chat-room", "telugu-chat-room"
]

print("--- CITY PAGES ---")
for p in city_pages:
    path = os.path.join(base_dir, p, "index.html")
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        main_match = re.search(r'<main>.*?(<p>.*?</p>)', html, re.DOTALL)
        p_text = main_match.group(1)[:120] if main_match else "N/A"
        print(f"{p:25} | Intro: {p_text}...")
    else:
        print(f"{p:25} | DOES NOT EXIST")

print("\n--- LANGUAGE PAGES ---")
for p in lang_pages:
    path = os.path.join(base_dir, p, "index.html")
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        main_match = re.search(r'<main>.*?(<p>.*?</p>)', html, re.DOTALL)
        p_text = main_match.group(1)[:120] if main_match else "N/A"
        print(f"{p:25} | Intro: {p_text}...")
    else:
        print(f"{p:25} | DOES NOT EXIST")
