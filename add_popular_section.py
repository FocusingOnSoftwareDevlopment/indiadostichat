import os

def add_popular_section():
    filepath = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\index.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    popular_section = """
        <!-- Popular India Chat Pages Section -->
        <section style="padding: 4rem 2rem; background: var(--bg-color);">
            <div class="container">
                <h2 style="text-align: center; color: var(--accent-color); margin-bottom: 2.5rem;">Popular India Chat Pages</h2>
                <div class="grid" style="grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1.5rem;">
                    <a href="india-chat.html" class="card" style="text-decoration: none; padding: 1.5rem; text-align: center; border: 1px solid var(--border-color); transition: transform 0.3s ease;">
                        <i class="fas fa-comments" style="font-size: 1.5rem; color: var(--primary-color); margin-bottom: 0.5rem;"></i>
                        <h3 style="font-size: 1.1rem; margin-bottom: 0;">India Chat</h3>
                    </a>
                    <a href="anonymous-indian-chat.html" class="card" style="text-decoration: none; padding: 1.5rem; text-align: center; border: 1px solid var(--border-color); transition: transform 0.3s ease;">
                        <i class="fas fa-user-secret" style="font-size: 1.5rem; color: var(--primary-color); margin-bottom: 0.5rem;"></i>
                        <h3 style="font-size: 1.1rem; margin-bottom: 0;">Anonymous Indian Chat</h3>
                    </a>
                    <a href="hindi-chat.html" class="card" style="text-decoration: none; padding: 1.5rem; text-align: center; border: 1px solid var(--border-color); transition: transform 0.3s ease;">
                        <i class="fas fa-language" style="font-size: 1.5rem; color: var(--primary-color); margin-bottom: 0.5rem;"></i>
                        <h3 style="font-size: 1.1rem; margin-bottom: 0;">Hindi Chat</h3>
                    </a>
                    <a href="desi-chat.html" class="card" style="text-decoration: none; padding: 1.5rem; text-align: center; border: 1px solid var(--border-color); transition: transform 0.3s ease;">
                        <i class="fas fa-users" style="font-size: 1.5rem; color: var(--primary-color); margin-bottom: 0.5rem;"></i>
                        <h3 style="font-size: 1.1rem; margin-bottom: 0;">Desi Chat</h3>
                    </a>
                    <a href="indian-friendship-chat.html" class="card" style="text-decoration: none; padding: 1.5rem; text-align: center; border: 1px solid var(--border-color); transition: transform 0.3s ease;">
                        <i class="fas fa-heart" style="font-size: 1.5rem; color: var(--primary-color); margin-bottom: 0.5rem;"></i>
                        <h3 style="font-size: 1.1rem; margin-bottom: 0;">Indian Friendship Chat</h3>
                    </a>
                    <a href="mobile-indian-chat.html" class="card" style="text-decoration: none; padding: 1.5rem; text-align: center; border: 1px solid var(--border-color); transition: transform 0.3s ease;">
                        <i class="fas fa-mobile-alt" style="font-size: 1.5rem; color: var(--primary-color); margin-bottom: 0.5rem;"></i>
                        <h3 style="font-size: 1.1rem; margin-bottom: 0;">Mobile Indian Chat</h3>
                    </a>
                    <a href="irc-chat-india.html" class="card" style="text-decoration: none; padding: 1.5rem; text-align: center; border: 1px solid var(--border-color); transition: transform 0.3s ease;">
                        <i class="fas fa-terminal" style="font-size: 1.5rem; color: var(--primary-color); margin-bottom: 0.5rem;"></i>
                        <h3 style="font-size: 1.1rem; margin-bottom: 0;">IRC Chat India</h3>
                    </a>
                    <a href="mumbai-chat-room.html" class="card" style="text-decoration: none; padding: 1.5rem; text-align: center; border: 1px solid var(--border-color); transition: transform 0.3s ease;">
                        <i class="fas fa-city" style="font-size: 1.5rem; color: var(--primary-color); margin-bottom: 0.5rem;"></i>
                        <h3 style="font-size: 1.1rem; margin-bottom: 0;">Mumbai Chat Room</h3>
                    </a>
                    <a href="hyderabad-chat-room.html" class="card" style="text-decoration: none; padding: 1.5rem; text-align: center; border: 1px solid var(--border-color); transition: transform 0.3s ease;">
                        <i class="fas fa-mosque" style="font-size: 1.5rem; color: var(--primary-color); margin-bottom: 0.5rem;"></i>
                        <h3 style="font-size: 1.1rem; margin-bottom: 0;">Hyderabad Chat Room</h3>
                    </a>
                    <a href="marathi-chat-room.html" class="card" style="text-decoration: none; padding: 1.5rem; text-align: center; border: 1px solid var(--border-color); transition: transform 0.3s ease;">
                        <i class="fas fa-om" style="font-size: 1.5rem; color: var(--primary-color); margin-bottom: 0.5rem;"></i>
                        <h3 style="font-size: 1.1rem; margin-bottom: 0;">Marathi Chat Room</h3>
                    </a>
                    <a href="telugu-chat-room.html" class="card" style="text-decoration: none; padding: 1.5rem; text-align: center; border: 1px solid var(--border-color); transition: transform 0.3s ease;">
                        <i class="fas fa-university" style="font-size: 1.5rem; color: var(--primary-color); margin-bottom: 0.5rem;"></i>
                        <h3 style="font-size: 1.1rem; margin-bottom: 0;">Telugu Chat Room</h3>
                    </a>
                    <a href="punjabi-chat-room.html" class="card" style="text-decoration: none; padding: 1.5rem; text-align: center; border: 1px solid var(--border-color); transition: transform 0.3s ease;">
                        <i class="fas fa-drum" style="font-size: 1.5rem; color: var(--primary-color); margin-bottom: 0.5rem;"></i>
                        <h3 style="font-size: 1.1rem; margin-bottom: 0;">Punjabi Chat Room</h3>
                    </a>
                </div>
            </div>
        </section>
"""
    
    target = """        <!-- Regional & Language Chat Communities -->"""
    # Find the end of this section
    target_end = """        </section>"""
    
    # We want to insert after the first occurrence of target_end that comes after target
    idx_start = content.find(target)
    if idx_start == -1:
        print("Could not find start target")
        return
    
    idx_end = content.find(target_end, idx_start)
    if idx_end == -1:
        print("Could not find end target")
        return
    
    insertion_point = idx_end + len(target_end)
    
    new_content = content[:insertion_point] + popular_section + content[insertion_point:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully updated index.html")

if __name__ == "__main__":
    add_popular_section()
