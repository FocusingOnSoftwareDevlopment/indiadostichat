import os
import re

base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
supporting = ["indian-chat", "anonymous-indian-chat", "hindi-chat", "desi-chat", "indian-friendship-chat", "mobile-indian-chat", "irc-chat-india"]

for p in supporting:
    path = os.path.join(base_dir, p, "index.html")
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
        title = title_match.group(1) if title_match else "N/A"
        
        desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html, re.IGNORECASE)
        if not desc_match:
            desc_match = re.search(r'<meta\s+content="([^"]*)"\s+name="description"', html, re.IGNORECASE)
        desc = desc_match.group(1) if desc_match else "N/A"
        
        main_match = re.search(r'<main>(.*?)</main>', html, re.DOTALL)
        if main_match:
            text = re.sub(r'<[^>]+>', ' ', main_match.group(1))
            words = len(re.findall(r'\b\w+\b', text))
        else:
            words = 0
            
        print(f"{p:25} | Title: {title[:50]:50} | Words: {words:5} | Desc: {desc[:60]}")
    else:
        print(f"{p:25} | DOES NOT EXIST")
