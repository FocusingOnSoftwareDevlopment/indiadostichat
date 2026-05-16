import os
import re

def standardize_footer():
    base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
    html_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]
    
    standard_footer = """
    <footer>
        <div class="footer-content">
            <div class="footer-section">
                <a href="./" class="logo" style="color: white; margin-bottom: 1rem; display: inline-block;">
                    <img src="assets/logo/logo.svg" alt="IndiaDostiChat Indian Chat Room Logo" style="height: 30px;" onerror="this.style.display='none'"> 
                    IndiaDostiChat
                </a>
                <p>The premier destination for Indians globally to connect, share, and build friendships in a free Indian chat room.</p>
            </div>
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
            </div>
            <div class="footer-section">
                <h4>Connect With Us</h4>
                <div class="social-links">
                    <a href="#"><i class="fab fa-facebook"></i></a>
                    <a href="#"><i class="fab fa-twitter"></i></a>
                    <a href="#"><i class="fab fa-instagram"></i></a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 IndiaDostiChat.com. All Rights Reserved.</p>
            <div style="margin-top: 1rem; color: #aaa; font-weight: 500; font-size: 0.95rem;">
                <i class="fas fa-eye" style="color: var(--primary-color);"></i> Total Visitors: <span id="visitor-count">Loading...</span>
            </div>
        </div>
    </footer>"""

    # Regex to match the entire <footer> block
    footer_pattern = re.compile(r'<footer.*?>.*?</footer>', re.DOTALL)

    for filename in html_files:
        filepath = os.path.join(base_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = footer_pattern.sub(standard_footer, content)
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Standardized footer in {filename}")

if __name__ == "__main__":
    standardize_footer()
