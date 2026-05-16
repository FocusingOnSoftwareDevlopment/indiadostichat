import os
import re

def fix_donate_page():
    filepath = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\donate.html"
    if not os.path.exists(filepath):
        print("donate.html not found")
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace ../ with ./
    content = content.replace("../", "./")
    
    # 2. Fix OG/Twitter URLs
    content = content.replace('content="https://www.indiadostichat.com/donate/"', 'content="https://www.indiadostichat.com/donate.html"')
    
    # 3. Standardize Header Nav (remove ../ and fix active class)
    # The header in index.html is:
    standard_header_nav = """
    <header>
        <nav>
            <a href="./" class="logo">
                <img src="assets/logo/logo.svg" alt="IndiaDostiChat Indian Chat Room Logo" style="height: 40px;" onerror="this.style.display='none'">
                IndiaDostiChat
            </a>
            
            <div class="nav-controls" style="display: flex; align-items: center; gap: 10px;">
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle dark mode" title="Toggle dark mode">
                  <span class="theme-icon">🌙</span>
                </button>
                <button class="mobile-menu-btn">
                <i class="fas fa-bars"></i>
            </button>
            </div>
            
            <ul class="nav-links">
                <li><a href="./">Home</a></li>
                <li><a href="chat.html">Chat</a></li>
                <li><a href="games.html">Games</a></li>
                <li><a href="blog.html">Blog</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="rules.html">Rules</a></li>
                <li><a href="contact.html">Contact</a></li>
                <li><a href="donate.html" class="active">Donate</a></li>
            </ul>
        </nav>
    </header>"""
    
    content = re.sub(r'<header>.*?</header>', standard_header_nav, content, flags=re.DOTALL)
    
    # 4. Fix footer links (though they might have been fixed by standardize_footer.py, let's be sure)
    # Re-run standardization might be easier.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed donate.html")

if __name__ == "__main__":
    fix_donate_page()
