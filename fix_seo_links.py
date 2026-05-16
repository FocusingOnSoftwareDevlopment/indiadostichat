import os
import re

def fix_links_and_canonicals():
    base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
    html_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]
    
    # List of pages to fix (from sitemap and previous analysis)
    pages = [
        "about", "chat", "blog", "contact", "rules", "games", "donate",
        "anonymous-indian-chat", "india-chat", "indian-chat", "hindi-chat", "desi-chat",
        "indian-friendship-chat", "irc-chat-india", "mobile-indian-chat",
        "mumbai-chat-room", "delhi-chat-room", "bangalore-chat-room", "kolkata-chat-room",
        "chennai-chat-room", "hyderabad-chat-room", "pune-chat-room", "jaipur-chat-room",
        "ahmedabad-chat-room", "lucknow-chat-room", "surat-chat-room", "kanpur-chat-room",
        "tamil-chat-room", "telugu-chat-room", "bengali-chat-room", "marathi-chat-room",
        "gujarati-chat-room", "punjabi-chat-room", "malayalam-chat-room", "kannada-chat-room"
    ]

    for filename in html_files:
        filepath = os.path.join(base_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. Fix internal links: href="page/" -> href="page.html"
        for page in pages:
            # Match href="page/", href="./page/", href="../page/"
            pattern = rf'href=(["\'])(?:\.\./|\./|)?{page}/\1'
            replacement = rf'href=\1{page}.html\1'
            content = re.sub(pattern, replacement, content)
            
            # Also handle absolute links if any (though unlikely based on current files)
            pattern_abs = rf'href=(["\'])https://www\.indiadostichat\.com/{page}/\1'
            replacement_abs = rf'href=\1https://www.indiadostichat.com/{page}.html\1'
            content = re.sub(pattern_abs, replacement_abs, content)

        # 2. Fix canonical tags: <link rel="canonical" href=".../page/"> -> <link rel="canonical" href=".../page.html">
        # Special case for homepage: keep it as /
        for page in pages:
            pattern_can = rf'<link rel="canonical" href="https://www\.indiadostichat\.com/{page}/">'
            replacement_can = f'<link rel="canonical" href="https://www.indiadostichat.com/{page}.html">'
            content = re.sub(pattern_can, replacement_can, content)

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed links in {filename}")

    # 3. Fix sitemap.xml
    sitemap_path = os.path.join(base_dir, "sitemap.xml")
    if os.path.exists(sitemap_path):
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            sitemap_content = f.read()
        
        original_sitemap = sitemap_content
        for page in pages:
            pattern_smap = rf'<loc>https://www\.indiadostichat\.com/{page}/</loc>'
            replacement_smap = f'<loc>https://www.indiadostichat.com/{page}.html</loc>'
            sitemap_content = re.sub(pattern_smap, replacement_smap, sitemap_content)
        
        if sitemap_content != original_sitemap:
            with open(sitemap_path, 'w', encoding='utf-8') as f:
                f.write(sitemap_content)
            print("Fixed sitemap.xml")

if __name__ == "__main__":
    fix_links_and_canonicals()
