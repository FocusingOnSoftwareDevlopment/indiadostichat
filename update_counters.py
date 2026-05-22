import os
import re

def update_counters():
    base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
    
    new_footer_bottom = """<div class="footer-bottom" style="display: flex; flex-direction: column; align-items: center; gap: 1rem; border-top: 1px solid var(--border-color); padding: 2rem 1rem 1rem;">
            <p>&copy; 2026 IndiaDostiChat.com. All Rights Reserved.</p>
            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem; font-weight: 500; font-size: 0.95rem; color: #aaa;">
                <div>
                    <i class="fas fa-users" style="color: var(--primary-color); margin-right: 0.5rem;"></i>
                    Community Visits: <span id="visitor-count">Loading...</span>
                </div>
                <div>
                    <i class="fas fa-comments" style="color: var(--accent-color); margin-right: 0.5rem;"></i>
                    Chat Entries: <span id="join-count">Loading...</span>
                </div>
            </div>
            <p style="font-size: 0.8rem; color: #777; margin: 0; text-align: center; max-width: 600px; line-height: 1.4;">
                Community activity is counted from real page visits and Join Chat actions, not random clicks.
            </p>
        </div>"""

    # Target the entire footer-bottom block, including the nested div
    pattern = re.compile(r'<div class="footer-bottom">.*?Total Visitors:.*?</span>\s*</div>\s*</div>', re.DOTALL)

    updated_count = 0
    total_html_files = 0

    for root, dirs, files in os.walk(base_dir):
        # Skip internal directories
        dirs[:] = [d for d in dirs if d not in ('.git', 'assets', 'node_modules', '.github')]
        for file in files:
            if file.endswith('.html'):
                total_html_files += 1
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if pattern.search(content):
                    new_content = pattern.sub(new_footer_bottom, content)
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        # Print relative path for cleaner output
                        rel_path = os.path.relpath(filepath, base_dir)
                        print(f"Updated footer in {rel_path}")
                        updated_count += 1
                else:
                    # In case the file already has the new footer-bottom or the pattern is different
                    rel_path = os.path.relpath(filepath, base_dir)
                    if 'id="join-count"' in content:
                        # Already updated
                        pass
                    else:
                        print(f"Warning: Could not match footer-bottom pattern in {rel_path}")

    print(f"Done! Scanned {total_html_files} HTML files, updated {updated_count} files.")

if __name__ == "__main__":
    update_counters()
