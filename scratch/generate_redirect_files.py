import os

base_dir = "."

redirects = {
    # Core pages
    "chat.html": "https://www.indiadostichat.com/chat/",
    "about.html": "https://www.indiadostichat.com/about/",
    "contact.html": "https://www.indiadostichat.com/contact/",
    "rules.html": "https://www.indiadostichat.com/rules/",
    "blog.html": "https://www.indiadostichat.com/blog/",
    "blogs.html": "https://www.indiadostichat.com/blog/",
    "india-chat.html": "https://www.indiadostichat.com/india-chat/",
    "allindiachat.html": "https://www.indiadostichat.com/allindiachat/",
    "anonymous-indian-chat.html": "https://www.indiadostichat.com/anonymous-indian-chat/",
    "hindi-chat.html": "https://www.indiadostichat.com/hindi-chat/",
    "desi-chat.html": "https://www.indiadostichat.com/desi-chat/",
    "indian-friendship-chat.html": "https://www.indiadostichat.com/indian-friendship-chat/",
    "mobile-indian-chat.html": "https://www.indiadostichat.com/mobile-indian-chat/",
    "irc-chat-india.html": "https://www.indiadostichat.com/irc-chat-india/",
    
    # City Rooms
    "mumbai-chat-room.html": "https://www.indiadostichat.com/mumbai-chat-room/",
    "delhi-chat-room.html": "https://www.indiadostichat.com/delhi-chat-room/",
    "bangalore-chat-room.html": "https://www.indiadostichat.com/bangalore-chat-room/",
    "hyderabad-chat-room.html": "https://www.indiadostichat.com/hyderabad-chat-room/",
    "chennai-chat-room.html": "https://www.indiadostichat.com/chennai-chat-room/",
    "kolkata-chat-room.html": "https://www.indiadostichat.com/kolkata-chat-room/",
    "pune-chat-room.html": "https://www.indiadostichat.com/pune-chat-room/",
    "jaipur-chat-room.html": "https://www.indiadostichat.com/jaipur-chat-room/",
    "ahmedabad-chat-room.html": "https://www.indiadostichat.com/ahmedabad-chat-room/",
    "lucknow-chat-room.html": "https://www.indiadostichat.com/lucknow-chat-room/",
    "surat-chat-room.html": "https://www.indiadostichat.com/surat-chat-room/",
    "kanpur-chat-room.html": "https://www.indiadostichat.com/kanpur-chat-room/",
    
    # Language Rooms
    "telugu-chat-room.html": "https://www.indiadostichat.com/telugu-chat-room/",
    "marathi-chat-room.html": "https://www.indiadostichat.com/marathi-chat-room/",
    "punjabi-chat-room.html": "https://www.indiadostichat.com/punjabi-chat-room/",
    "tamil-chat-room.html": "https://www.indiadostichat.com/tamil-chat-room/",
    "bengali-chat-room.html": "https://www.indiadostichat.com/bengali-chat-room/",
    "gujarati-chat-room.html": "https://www.indiadostichat.com/gujarati-chat-room/",
    "malayalam-chat-room.html": "https://www.indiadostichat.com/malayalam-chat-room/",
    "kannada-chat-room.html": "https://www.indiadostichat.com/kannada-chat-room/",
    
    # Nested folder redirect
    "topics/money-talk/index.html": "https://www.indiadostichat.com/topics/money-chat/"
}

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirecting...</title>
    <link rel="canonical" href="{target_url}">
    <meta http-equiv="refresh" content="0;url={target_url}">
    <meta name="robots" content="noindex, follow">
    <script>
        window.location.replace("{target_url}");
    </script>
</head>
<body>
    <p>Redirecting to <a href="{target_url}">{target_url}</a>...</p>
</body>
</html>
"""

def main():
    created_count = 0
    for filename, target_url in redirects.items():
        filepath = os.path.join(base_dir, filename)
        
        # Ensure directories exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Write the redirect file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(template.format(target_url=target_url))
            
        print(f"Created redirect file: {filename} -> {target_url}")
        created_count += 1
        
    print(f"Done! Successfully created {created_count} legacy redirect HTML files.")

if __name__ == "__main__":
    main()
