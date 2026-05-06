import glob
import re

html_files = glob.glob('*.html')

new_nav = '''<ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="chat.html">Chat</a></li>
                <li><a href="games.html">Games</a></li>
                <li><a href="blog.html">Blog</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="rules.html">Rules</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>'''

for file in html_files:
    if file == 'chat.html':
        continue # chat.html doesn't have a navbar
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to find and replace the nav-links block
    pattern = r'<ul class="nav-links">.*?</ul>'
    
    # We use DOTALL to match across newlines
    new_content = re.sub(pattern, new_nav, content, flags=re.DOTALL)
    
    # Update cache buster to v=6
    new_content = new_content.replace('?v=5', '?v=6')
    new_content = new_content.replace('?v=4', '?v=6') # just in case
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Navigation updated.")
