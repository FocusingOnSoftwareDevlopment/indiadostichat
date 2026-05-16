import os
import re

def update_footer():
    base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
    html_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]
    
    new_footer_section = """
            <div class="footer-section">
                <h4>Explore IndiaDostiChat</h4>
                <ul style="list-style: none; display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
                    <li><a href="./" style="color: #ccc; text-decoration: none;">Home</a></li>
                    <li><a href="chat.html" style="color: #ccc; text-decoration: none;">Chat</a></li>
                    <li><a href="india-chat.html" style="color: #ccc; text-decoration: none;">India Chat</a></li>
                    <li><a href="anonymous-indian-chat.html" style="color: #ccc; text-decoration: none;">Anonymous Indian Chat</a></li>
                    <li><a href="hindi-chat.html" style="color: #ccc; text-decoration: none;">Hindi Chat</a></li>
                    <li><a href="desi-chat.html" style="color: #ccc; text-decoration: none;">Desi Chat</a></li>
                    <li><a href="indian-friendship-chat.html" style="color: #ccc; text-decoration: none;">Indian Friendship Chat</a></li>
                    <li><a href="mobile-indian-chat.html" style="color: #ccc; text-decoration: none;">Mobile Indian Chat</a></li>
                    <li><a href="games.html" style="color: #ccc; text-decoration: none;">Games</a></li>
                    <li><a href="donate.html" style="color: #ccc; text-decoration: none;">Donate</a></li>
                    <li><a href="rules.html" style="color: #ccc; text-decoration: none;">Rules</a></li>
                    <li><a href="contact.html" style="color: #ccc; text-decoration: none;">Contact</a></li>
                </ul>
            </div>"""

    # We want to replace the <div class="footer-section"> that contains "Quick Links"
    # Note: Indentation might vary, so we use a flexible regex.
    pattern = re.compile(r'<div class="footer-section">\s*<h4>Quick Links</h4>.*?</ul>\s*</div>', re.DOTALL)

    for filename in html_files:
        filepath = os.path.join(base_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "Quick Links" in content:
            new_content = pattern.sub(new_footer_section, content)
            if new_content != content:
                # Adjust links for pages in subdirectories (if any existed, but they don't seem to now)
                # If we were in a subfolder, we would need to prefix with ../
                # But all files are in the root now.
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated footer in {filename}")

if __name__ == "__main__":
    update_footer()
