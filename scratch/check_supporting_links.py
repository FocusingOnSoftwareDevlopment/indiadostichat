import os
import re

base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
supporting = ["indian-chat", "anonymous-indian-chat", "hindi-chat", "desi-chat", "indian-friendship-chat", "mobile-indian-chat", "irc-chat-india"]

for p in supporting:
    path = os.path.join(base_dir, p, "index.html")
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        has_india_chat = "../india-chat/" in html
        has_chat = "../chat/" in html
        
        print(f"{p:25} | Links to ../india-chat/: {str(has_india_chat):5} | Links to ../chat/: {str(has_chat)}")
    else:
        print(f"{p:25} | DOES NOT EXIST")
