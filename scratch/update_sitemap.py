import os
import re
import datetime

sitemap_path = "sitemap.xml"
stories_dir = "india-stories"

# Define the 38 original non-stories URLs exactly
non_stories_urls = [
    "https://www.indiadostichat.com/",
    "https://www.indiadostichat.com/about/",
    "https://www.indiadostichat.com/games/",
    "https://www.indiadostichat.com/blog/",
    "https://www.indiadostichat.com/blog/mumbai-chat-room/",
    "https://www.indiadostichat.com/blog/indian-korean-friendship/",
    "https://www.indiadostichat.com/blog/india-korea-cultural-exchange-community/",
    "https://www.indiadostichat.com/blog/india-korea-cultural-exchange-complete-guide/",
    "https://www.indiadostichat.com/contact/",
    "https://www.indiadostichat.com/chat/",
    "https://www.indiadostichat.com/rules/",
    "https://www.indiadostichat.com/donate/",
    "https://www.indiadostichat.com/anonymous-indian-chat/",
    "https://www.indiadostichat.com/india-chat/",
    "https://www.indiadostichat.com/allindiachat/",
    "https://www.indiadostichat.com/indian-chat/",
    "https://www.indiadostichat.com/hindi-chat/",
    "https://www.indiadostichat.com/desi-chat/",
    "https://www.indiadostichat.com/indian-friendship-chat/",
    "https://www.indiadostichat.com/irc-chat-india/",
    "https://www.indiadostichat.com/mobile-indian-chat/",
    "https://www.indiadostichat.com/mumbai-chat-room/",
    "https://www.indiadostichat.com/delhi-chat-room/",
    "https://www.indiadostichat.com/bangalore-chat-room/",
    "https://www.indiadostichat.com/kolkata-chat-room/",
    "https://www.indiadostichat.com/chennai-chat-room/",
    "https://www.indiadostichat.com/hyderabad-chat-room/",
    "https://www.indiadostichat.com/pune-chat-room/",
    "https://www.indiadostichat.com/jaipur-chat-room/",
    "https://www.indiadostichat.com/ahmedabad-chat-room/",
    "https://www.indiadostichat.com/lucknow-chat-room/",
    "https://www.indiadostichat.com/surat-chat-room/",
    "https://www.indiadostichat.com/kanpur-chat-room/",
    "https://www.indiadostichat.com/tamil-chat-room/",
    "https://www.indiadostichat.com/telugu-chat-room/",
    "https://www.indiadostichat.com/bengali-chat-room/",
    "https://www.indiadostichat.com/marathi-chat-room/",
    "https://www.indiadostichat.com/gujarati-chat-room/",
    "https://www.indiadostichat.com/punjabi-chat-room/",
    "https://www.indiadostichat.com/malayalam-chat-room/",
    "https://www.indiadostichat.com/kannada-chat-room/",
    "https://www.indiadostichat.com/sitemap/",
    "https://www.indiadostichat.com/topics/",
    "https://www.indiadostichat.com/topics/money-chat/",
    "https://www.indiadostichat.com/topics/korea-chat/",
    "https://www.indiadostichat.com/topics/japan-chat/",
    "https://www.indiadostichat.com/topics/anime-chat/",
    "https://www.indiadostichat.com/topics/kpop-chat/",
    "https://www.indiadostichat.com/topics/travel-chat/",
    "https://www.indiadostichat.com/topics/food-chat/",
    "https://www.indiadostichat.com/topics/gaming-chat/",
    "https://www.indiadostichat.com/topics/ai-chat/",
    "https://www.indiadostichat.com/topics/international-friendship-chat/"
]

# Scan india-stories directory to build the list of indexable stories URLs
stories_urls = []
for root, dirs, files in os.walk(stories_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, stories_dir)
            
            # format as clean folder URL
            clean_path = rel_path.replace('\\', '/')
            if clean_path == "index.html":
                subpath = ""
            elif clean_path.endswith("/index.html"):
                subpath = clean_path[:-10]
            else:
                subpath = clean_path
            
            url = f"https://www.indiadostichat.com/india-stories/{subpath}"
            if subpath == "":
                url = "https://www.indiadostichat.com/india-stories/"
                
            stories_urls.append(url)

# Sort stories URLs logically
def sort_key(url):
    if url == "https://www.indiadostichat.com/india-stories/":
        return ("", "")
    subpath = url[len("https://www.indiadostichat.com/india-stories/"):]
    parts = subpath.strip('/').split('/')
    hub = parts[0]
    chapter = parts[1] if len(parts) > 1 else ""
    return (hub, chapter)

stories_urls.sort(key=sort_key)

# Function to generate a valid sitemap URL XML block
def make_url_block(url, lastmod, changefreq, priority):
    # Escape ampersands just in case
    escaped_url = url.replace("&", "&amp;")
    return f"""  <url>
    <loc>{escaped_url}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>"""

# Assemble all URL blocks
all_blocks = []

# Process non-stories URLs
for url in non_stories_urls:
    # Determine priority
    if url == "https://www.indiadostichat.com/":
        priority = "1.0"
        changefreq = "daily"
        lastmod = "2026-05-29"
    elif url in [
        "https://www.indiadostichat.com/chat/",
        "https://www.indiadostichat.com/anonymous-indian-chat/",
        "https://www.indiadostichat.com/india-chat/",
        "https://www.indiadostichat.com/allindiachat/",
        "https://www.indiadostichat.com/indian-chat/",
        "https://www.indiadostichat.com/hindi-chat/",
        "https://www.indiadostichat.com/desi-chat/",
        "https://www.indiadostichat.com/indian-friendship-chat/",
        "https://www.indiadostichat.com/irc-chat-india/",
        "https://www.indiadostichat.com/mobile-indian-chat/"
    ]:
        priority = "0.9"
        changefreq = "weekly"
        lastmod = "2026-05-11"
        if "allindiachat" in url:
            lastmod = "2026-05-17"
    elif "/blog/" in url:
        priority = "0.8"
        changefreq = "weekly"
        lastmod = "2026-05-31"
    elif url in [
        "https://www.indiadostichat.com/about/",
        "https://www.indiadostichat.com/games/",
        "https://www.indiadostichat.com/blog/",
        "https://www.indiadostichat.com/contact/"
    ] or "chat-room" in url:
        priority = "0.8"
        changefreq = "weekly"
        lastmod = "2026-05-11"
    elif url in [
        "https://www.indiadostichat.com/rules/",
        "https://www.indiadostichat.com/donate/"
    ]:
        priority = "0.7"
        changefreq = "weekly"
        lastmod = "2026-05-11"
        if "donate" in url:
            lastmod = "2026-05-16"
    elif url == "https://www.indiadostichat.com/sitemap/":
        priority = "0.5"
        changefreq = "weekly"
        lastmod = "2026-05-16"
    elif "/topics/" in url:
        if url == "https://www.indiadostichat.com/topics/":
            priority = "0.8"
        else:
            priority = "0.7"
        changefreq = "weekly"
        lastmod = "2026-05-31"
    else:
        priority = "0.8"
        changefreq = "weekly"
        lastmod = "2026-05-11"
        
    all_blocks.append(make_url_block(url, lastmod, changefreq, priority))

# Process stories URLs
today_str = "2026-05-29"
for url in stories_urls:
    slash_count = url.count('/')
    if url == "https://www.indiadostichat.com/india-stories/":
        priority = "0.85"
    elif slash_count == 5:
        priority = "0.75"
    else:
        priority = "0.65"
    all_blocks.append(make_url_block(url, today_str, "weekly", priority))

# Build sitemap.xml
new_xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]
new_xml_lines.extend(all_blocks)
new_xml_lines.append('</urlset>')

new_sitemap_content = "\n".join(new_xml_lines) + "\n"

# Write to sitemap.xml
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(new_sitemap_content)

print(f"Successfully generated clean valid sitemap.xml!")
print(f"Total non-stories URLs: {len(non_stories_urls)}")
print(f"Total stories URLs: {len(stories_urls)}")
print(f"Total URLs in sitemap: {len(non_stories_urls) + len(stories_urls)}")
print(f"Total lines in sitemap.xml: {len(new_sitemap_content.splitlines())}")
