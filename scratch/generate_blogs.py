import os
import json
import re

base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
blog_dir = os.path.join(base_dir, "blog")
os.makedirs(blog_dir, exist_ok=True)

css_version = "25"
js_version = "20"

downloads_dir = r"C:\Users\mks1j\Downloads\files"
fallback_dir = os.path.join(base_dir, "blog-sources", "files")

# SVG Icons (inline to avoid FontAwesome dependency)
menu_icon_svg = """<svg class="icon-menu" viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round" style="display: block; margin: auto;">
                        <line class="line-1" x1="3" y1="6" x2="21" y2="6" style="transition: transform 0.3s, opacity 0.3s;"></line>
                        <line class="line-2" x1="3" y1="12" x2="21" y2="12" style="transition: transform 0.3s, opacity 0.3s;"></line>
                        <line class="line-3" x1="3" y1="18" x2="21" y2="18" style="transition: transform 0.3s, opacity 0.3s;"></line>
                    </svg>"""

fb_svg = '<svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24" style="vertical-align: middle;"><path d="M9 8H7v3h2v9h4v-9h3.6l.4-3H13V6c0-.5.5-1 1-1h3V1H13c-3.3 0-4 1.7-4 4v3z"/></svg>'
tw_svg = '<svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24" style="vertical-align: middle;"><path d="M18.2 2.4h3.3L14.3 11l8.5 11.3h-6.7L11 15.6l-6 6.7H1.7l7.6-8.7L1.2 2.4h6.9l4.6 6.1 5.5-6.1zm-1.2 17.5h1.8L7 4.2H5.1l11.9 15.7z"/></svg>'
ig_svg = '<svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24" style="vertical-align: middle;"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37zM17.5 6.5h.01"/></svg>'
users_svg = '<svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24" style="vertical-align: -2px; margin-right: 0.5rem; color: var(--primary-color);"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>'
comments_svg = '<svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24" style="vertical-align: -2px; margin-right: 0.5rem; color: var(--accent-color);"><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 9h12v2H6V9zm8 5H6v-2h8v2zm4-6H6V6h12v2z"/></svg>'
calendar_svg = '<svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" style="vertical-align: -1px; margin-right: 0.4rem; opacity: 0.8;"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>'

# Helper schemas
def make_bc_schema(slug, title):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://www.indiadostichat.com/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Community Blog",
                "item": "https://www.indiadostichat.com/blog/"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": title,
                "item": f"https://www.indiadostichat.com/blog/{slug}/"
            }
        ]
    }, indent=2)

def make_faq_schema(faqs):
    entities = []
    for q, a in faqs:
        entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    }, indent=2)

def make_posting_schema(slug, title, desc, pub_date="2026-05-31"):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": desc,
        "datePublished": pub_date,
        "dateModified": pub_date,
        "author": {
            "@type": "Organization",
            "name": "IndiaDostiChat"
        },
        "publisher": {
            "@type": "Organization",
            "name": "IndiaDostiChat",
            "logo": {
                "@type": "ImageObject",
                "url": "https://www.indiadostichat.com/assets/logo/logo-512x512.png"
            }
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"https://www.indiadostichat.com/blog/{slug}/"
        },
        "image": f"https://www.indiadostichat.com/assets/images/topics/{slug}.webp"
    }, indent=2)

def read_source_file(filename):
    p1 = os.path.join(downloads_dir, filename)
    if os.path.exists(p1):
        with open(p1, "r", encoding="utf-8") as f:
            return f.read()
    p2 = os.path.join(fallback_dir, filename)
    if os.path.exists(p2):
        with open(p2, "r", encoding="utf-8") as f:
            return f.read()
    raise FileNotFoundError(f"Could not find source file {filename} in {downloads_dir} or {fallback_dir}")

def parse_mumbai_room():
    text = read_source_file("mumbairoom.txt")
    text = text.replace("\r\n", "\n")
    lines = text.split("\n")
    html_blocks = []
    in_list = False
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if in_list:
                html_blocks.append("</ul>")
                in_list = False
            continue
            
        # Check headings
        if stripped.startswith("### "):
            if in_list:
                html_blocks.append("</ul>")
                in_list = False
            val = stripped[4:].strip()
            html_blocks.append(f'<h4 style="color: var(--primary-color); margin-top: 1.5rem;">{val}</h4>')
        elif stripped.startswith("## "):
            if in_list:
                html_blocks.append("</ul>")
                in_list = False
            val = stripped[3:].strip()
            html_blocks.append(f'<h3 style="color: var(--primary-color); margin-top: 1.8rem;">{val}</h3>')
        elif stripped.startswith("# "):
            if in_list:
                html_blocks.append("</ul>")
                in_list = False
            val = stripped[2:].strip()
            html_blocks.append(f'<h2 style="color: var(--accent-color); margin-top: 2rem;">{val}</h2>')
        elif stripped.startswith("- ") or stripped.startswith("* "):
            if not in_list:
                html_blocks.append('<ul style="line-height: 1.8; margin-bottom: 1.5rem; padding-left: 1.5rem;">')
                in_list = True
            val = stripped[2:].strip()
            html_blocks.append(f"<li>{val}</li>")
        elif stripped.startswith("=======") or stripped.startswith("-------") or stripped in ("VERSION 1", "VERSION 2 – EMOTIONAL", "VERSION 3 – BOLLYWOOD STYLE"):
            if in_list:
                html_blocks.append("</ul>")
                in_list = False
            if stripped in ("VERSION 1", "VERSION 2 – EMOTIONAL", "VERSION 3 – BOLLYWOOD STYLE"):
                html_blocks.append(f'<div style="margin-top: 3rem; border-top: 2px dashed var(--border-color); padding-top: 2rem; font-weight: bold; font-size: 1.2rem; color: var(--primary-color); text-transform: uppercase;">{stripped}</div>')
        else:
            if in_list:
                html_blocks.append("</ul>")
                in_list = False
            # Blockquote detection
            if (stripped.startswith("“") or stripped.startswith('"')) and (stripped.endswith("”") or stripped.endswith('"') or "kare?" in stripped or "diya!" in stripped or "leli..." in stripped or "dosti banate" in stripped):
                html_blocks.append(f'<blockquote style="border-left: 4px solid var(--primary-color); padding-left: 1.2rem; margin-left: 0; line-height: 1.8; color: var(--text-color); font-style: italic; margin-bottom: 1.5rem;">{stripped}</blockquote>')
            else:
                html_blocks.append(f'<p style="line-height: 1.8; margin-bottom: 1.5rem;">{stripped}</p>')
                
    if in_list:
        html_blocks.append("</ul>")
        
    content_html = "\n".join(html_blocks)
    return {
        "slug": "mumbai-chat-room",
        "title": "Mumbai Chat Room: Where Bollywood Dreams and Desi Hearts Connect Online",
        "h1": "Mumbai Chat Room: Where Bollywood Dreams and Desi Hearts Connect Online",
        "meta_desc": "Step into our free Mumbai chat room. Connect with Mumbaikars, discuss cutting chai, local train stories, Bollywood movies, and the city that never sleeps.",
        "category": "Desi Communities",
        "read_time": "5 min read",
        "intro_p": "Mumbai, the Maximum City, is a feeling carried by millions of people every single day. From late-night Marine Drive talks watching the waves silently to the daily local train stories, every Mumbaikar carries a unique vibe.",
        "content_html": content_html,
        "faqs": [
            ("Is there a dedicated chat room for Mumbai residents?", "Yes! Mumbaikars and those who love Mumbai culture gather in our main chat rooms, which act as a centralized, highly active hub for users from Mumbai, Delhi, Bangalore, and across India."),
            ("Do I need to sign up or download an app?", "No registration is needed. You can join the conversation using just a nickname, keeping your experience fast, secure, and private."),
            ("Can I chat in Marathi or Hinglish?", "Absolutely. We encourage cultural expression. People talk in Hindi, Marathi, English, or full Mumbai Hinglish without judgment."),
            ("Is the chat active late at night?", "Yes. Since Mumbai is the city that never sleeps, our chat room is highly active during late-night hours with users sharing late-night vibes, music, and deep thoughts.")
        ]
    }

def parse_friendship_blog():
    text = read_source_file("Indian_Korean_Friendship_Blog.txt")
    text = text.replace("\r\n", "\n")
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    title = paragraphs[0].replace("\n", " ")
    
    html_blocks = []
    for p in paragraphs[1:]:
        lines = [line.strip() for line in p.split("\n") if line.strip()]
        p_text = " ".join(lines)
        html_blocks.append(f'<p style="line-height: 1.8; margin-bottom: 1.5rem;">{p_text}</p>')
        
    content_html = "\n".join(html_blocks)
    return {
        "slug": "indian-korean-friendship",
        "title": title,
        "h1": title,
        "meta_desc": "Connect with Korean friends online. Practice language learning, share food recipes like kimchi and biryani, and explore cultural exchange between India and Korea.",
        "category": "Cultural Exchange",
        "read_time": "4 min read",
        "intro_p": "Friendship is the strongest bridge between different countries and cultures.",
        "content_html": content_html,
        "faqs": [
            ("How can I find Korean friends online safely?", "You can join dedicated cultural chat rooms on IndiaDostiChat. Because the platform is anonymous and nickname-based, you can chat safely without sharing personal social media profiles or phone numbers."),
            ("Is language learning possible through text chat?", "Yes! Text chat is excellent for language practice. You can learn Hangul, practice basic grammar, and receive real-time corrections from native speakers."),
            ("What topics are popular in Indian-Korean chat rooms?", "Members discuss K-pop comebacks, popular K-dramas, food recipes (like ramyeon and biryani), travel spots in Seoul and Goa, and daily life experiences."),
            ("Are there guidelines for respectful conversation?", "Yes. We maintain a zero-tolerance policy against hate speech, stereotypes, and disrespectful comments. Cultivating mutual respect is essential for cross-cultural friendships.")
        ]
    }

def parse_cultural_exchange_master():
    text = read_source_file("India_Korea_Cultural_Exchange_Master_Blog.txt")
    text = text.replace("\r\n", "\n")
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    title = paragraphs[0].replace("\n", " ")
    
    headings_list = {
        "introduction", "why korea is becoming popular among indians",
        "why koreans are interested in india", "building friendships across borders",
        "learning korean language", "language exchange communities",
        "indian students in south korea", "scholarships for indian students",
        "jobs for indians in korea", "korean companies and global opportunities",
        "korean food culture", "indian food through korean eyes",
        "travel destinations in korea", "travel destinations in india",
        "similarities between india and korea", "top reasons koreans should learn about india",
        "study abroad resources for korea", "career opportunities for korean speakers in india",
        "korean tourism guide for indians", "indian tourism guide for koreans",
        "india and korea in the future", "historical connection between india and korea",
        "korean language learning roadmap", "korean etiquette every indian should know",
        "indian culture explained for korean visitors", "best korean cities for international students",
        "best indian cities for korean visitors", "indian startups and korean innovation",
        "korean entertainment beyond k-pop", "volunteering and cultural exchange programs",
        "digital nomads and remote workers in korea", "why join indiadostichat.com",
        "seo keywords included", "conclusion"
    }
    
    html_blocks = []
    for p in paragraphs[1:]:
        p_clean = p.replace("\n", " ").strip()
        if p_clean.lower().strip(":") in headings_list:
            html_blocks.append(f'<h2 style="color: var(--accent-color); margin-top: 2.2rem;">{p_clean}</h2>')
        else:
            if "Indian Korean Friendship India Korea Cultural Exchange" in p_clean:
                html_blocks.append(f'<p style="font-size: 0.9rem; color: #777; line-height: 1.6; font-style: italic; margin-top: 2rem;"><strong>Keywords:</strong> {p_clean}</p>')
            else:
                html_blocks.append(f'<p style="line-height: 1.8; margin-bottom: 1.5rem;">{p_clean}</p>')
                
    content_html = "\n".join(html_blocks)
    return {
        "slug": "india-korea-cultural-exchange-community",
        "title": title,
        "h1": title,
        "meta_desc": "Join our India-Korea cultural exchange community. Explore language roadmaps, study resources, scholarship guides, jobs in Korea, travel tips, and cultural similarities.",
        "category": "Community Guide",
        "read_time": "6 min read",
        "intro_p": "The partnership between India and South Korea has evolved from diplomatic ties into a vibrant cultural connection.",
        "content_html": content_html,
        "faqs": [
            ("What is the Global Korea Scholarship (GKS)?", "The GKS is a fully-funded scholarship program by the South Korean government for international students to pursue undergraduate and postgraduate degrees in Korea."),
            ("Are there job opportunities in South Korea for Indians?", "Yes. Opportunities are abundant in IT, engineering, software development, biotechnology, and multinational corporate roles."),
            ("How long does it take to learn basic conversational Korean?", "With daily practice, most learners can grasp basic conversational Korean in 3 to 6 months. Learning the Hangul alphabet takes only a few hours."),
            ("What is the best way to practice speaking Korean?", "Practicing with native speakers in language exchange communities is the most effective way. IndiaDostiChat provides a safe space for real-time text practice.")
        ]
    }

def parse_complete_seo_guide():
    text = read_source_file("India_Korea_Complete_SEO_Blog.txt")
    text = text.replace("\r\n", "\n")
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    title = paragraphs[0].replace("\n", " ")
    
    headings_list = {
        "introduction to india–korea cultural exchange", "why koreans and indians are connecting",
        "friendship across borders", "learning korean language",
        "indian students in korea", "scholarships and universities",
        "jobs and careers in korea", "korean culture and traditions",
        "indian culture explained for korean visitors", "travel guide to korea",
        "food, festivals and community", "technology and innovation",
        "language exchange communities", "future of india–korea relations",
        "why join indiadostichat.com", "conclusion"
    }
    
    parsed_sections = []
    current_heading = None
    
    for p in paragraphs[1:]:
        p_clean = p.replace("\n", " ").strip()
        p_lower = p_clean.lower()
        
        if p_lower in headings_list:
            current_heading = p_clean
            parsed_sections.append((current_heading, []))
        else:
            if current_heading:
                # Normalizing check for repeated block of text (we only write the block once per heading)
                p_norm = re.sub(r'\s+', ' ', p_clean).strip()
                if p_norm.startswith("This section discusses friendship"):
                    if not parsed_sections[-1][1]:
                        parsed_sections[-1][1].append(p_clean)
                elif p_norm.startswith("India and South Korea are connected"):
                    if not parsed_sections[-1][1]:
                        parsed_sections[-1][1].append(p_clean)
                else:
                    if p_clean not in parsed_sections[-1][1]:
                        parsed_sections[-1][1].append(p_clean)
                        
    toc_items = []
    section_html_blocks = []
    anchor_map = {
        "Introduction to India–Korea Cultural Exchange": "intro",
        "Why Koreans and Indians Are Connecting": "connecting",
        "Friendship Across Borders": "friendship",
        "Learning Korean Language": "language",
        "Indian Students in Korea": "students",
        "Scholarships and Universities": "scholarships",
        "Jobs and Careers in Korea": "jobs",
        "Korean Culture and Traditions": "culture",
        "Indian Culture Explained for Korean Visitors": "visitors",
        "Travel Guide to Korea": "travel",
        "Food, Festivals and Community": "food",
        "Technology and Innovation": "tech",
        "Language Exchange Communities": "exchange",
        "Future of India–Korea Relations": "future",
        "Why Join IndiaDostiChat.com": "join",
        "Conclusion": "conclusion"
    }
    
    for i, (heading, text_list) in enumerate(parsed_sections, 1):
        anchor_id = anchor_map.get(heading, f"sec-{i}")
        toc_items.append(f'<li><a href="#{anchor_id}" style="color: inherit; text-decoration: none; font-weight: 500;">{i}. {heading}</a></li>')
        
        para_html = "".join([f'<p style="line-height: 1.8; margin-bottom: 1.5rem;">{t}</p>' for t in text_list])
        section_html_blocks.append(f"""
        <section id="{anchor_id}" style="margin-bottom: 2.5rem;">
            <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">{i}. {heading}</h2>
            {para_html}
        </section>
        """)
        
    toc_items_str = "\n".join(toc_items)
    toc_html = f"""
    <div class="toc-container" style="background: var(--card-bg); border: 1px solid var(--border-color); border-radius: var(--border-radius); padding: 1.8rem; margin: 2rem 0; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
        <h3 style="margin-top: 0; color: var(--accent-color); font-size: 1.25rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
            <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h7"/></svg>
            Table of Contents
        </h3>
        <nav>
            <ol style="line-height: 2; font-size: 0.98rem; padding-left: 1.2rem; margin: 0; color: var(--primary-color);">
                {toc_items_str}
            </ol>
        </nav>
    </div>
    """
    
    content_html = toc_html + "\n".join(section_html_blocks)
    return {
        "slug": "india-korea-cultural-exchange-complete-guide",
        "title": title,
        "h1": title,
        "meta_desc": "Our ultimate pillar guide to India-Korea cultural exchange. Discover language roadmaps, study abroad scholarships, job search tips, travel guides, and food culture.",
        "category": "Pillar Article",
        "read_time": "12 min read",
        "intro_p": "The connection between India and South Korea has grown exceptionally. What began as trade has evolved into a deep cultural exchange.",
        "content_html": content_html,
        "faqs": [
            ("What is the historical connection between India and Korea?", "According to ancient texts, Princess Suriratna from Ayodhya traveled to Korea in 48 AD and married King Kim Suro of Geumgwan Gaya, becoming Queen Heo Hwang-ok. This historic connection is still celebrated today."),
            ("What is the Global Korea Scholarship (GKS)?", "The GKS is a prestigious fully-funded scholarship program covering tuition fees, round-trip airfare, monthly stipend, settlement allowance, and insurance for international students studying in South Korea."),
            ("Can Indian software developers find jobs in South Korea?", "Yes, there is high demand for IT professionals, semiconductor researchers, and AI developers in South Korea, with giants like Samsung and LG actively hiring global talent."),
            ("Is learning Hangul difficult for Indian speakers?", "No, Hangul is one of the most scientific and logical alphabets in the world. Many Indian speakers find it easy to pick up due to similar phonetic structures between Korean and Indian languages like Hindi and Tamil.")
        ]
    }

# Dynamic generation data
blogs_data = [
    parse_mumbai_room(),
    parse_friendship_blog(),
    parse_cultural_exchange_master(),
    parse_complete_seo_guide()
]

# Generate individual blog subpages
for config in blogs_data:
    slug = config["slug"]
    title = config["title"]
    h1 = config["h1"]
    meta_desc = config["meta_desc"]
    category = config["category"]
    read_time = config["read_time"]
    intro_p = config["intro_p"]
    content_html = config["content_html"]
    faqs = config["faqs"]
    
    # Generate related blog links (other 3)
    related_links_html = ""
    for other in blogs_data:
        if other["slug"] != slug:
            related_links_html += f'<li><a href="../{other["slug"]}/" style="color: var(--primary-color); text-decoration: none; font-weight: 500;">{other["title"]}</a></li>\n'
            
    bc_schema = make_bc_schema(slug, title)
    faq_schema = make_faq_schema(faqs)
    posting_schema = make_posting_schema(slug, title, meta_desc)
    
    faqs_html = ""
    for q, a in faqs:
        faqs_html += f"""<div style="margin-bottom: 2rem; border-left: 4px solid var(--accent-color); padding-left: 1.5rem;">
            <h3 style="color: var(--primary-color); margin-top: 0; margin-bottom: 0.5rem; font-size: 1.25rem;">{q}</h3>
            <p style="margin: 0; line-height: 1.6;">{a}</p>
        </div>"""
        
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | IndiaDostiChat Blog</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="https://www.indiadostichat.com/blog/{slug}/">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{title} | IndiaDostiChat Blog">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="https://www.indiadostichat.com/blog/{slug}/">
    <meta property="og:type" content="article">
    <meta property="og:image" content="https://www.indiadostichat.com/assets/images/topics/{slug}.webp">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title} | IndiaDostiChat Blog">
    <meta name="twitter:description" content="{meta_desc}">
    <meta name="twitter:image" content="https://www.indiadostichat.com/assets/images/topics/{slug}.webp">

    <link rel="stylesheet" href="../../assets/css/style.min.css?v={css_version}">
    <link rel="prefetch" href="../../chat/">
    
    <!-- Custom styling to guarantee system font fallback and styling refinement -->
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol" !important;
        }}
        .hero-banner {{
            max-width: 800px;
            height: auto;
            border-radius: var(--border-radius);
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            margin: 2rem auto;
            display: block;
            border: 1px solid var(--border-color);
        }}
        .landing-hero {{
            padding: 4rem 1rem;
            text-align: center;
            background: linear-gradient(135deg, var(--hero-bg-gradient-start, #0f172a), var(--hero-bg-gradient-end, #1e293b));
            color: #fff;
            margin-bottom: 2rem;
        }}
        .landing-hero h1 {{
            font-size: 2.3rem;
            margin-bottom: 1rem;
            font-weight: 700;
            line-height: 1.3;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }}
        .blog-meta {{
            font-size: 0.95rem;
            opacity: 0.85;
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 1rem;
            flex-wrap: wrap;
        }}
        .blog-meta span {{
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}
        @media (max-width: 768px) {{
            .landing-hero h1 {{
                font-size: 1.75rem !important;
            }}
            .landing-hero {{
                padding: 2.5rem 1rem !important;
            }}
            .hero-banner {{
                margin: 1rem auto !important;
                max-width: 100% !important;
            }}
            .blog-meta {{
                gap: 0.8rem !important;
                font-size: 0.85rem !important;
            }}
            .toc-container {{
                padding: 1rem !important;
            }}
        }}
    </style>

    <!-- Schemas JSON-LD -->
    <script type="application/ld+json">
    {bc_schema}
    </script>
    <script type="application/ld+json">
    {faq_schema}
    </script>
    <script type="application/ld+json">
    {posting_schema}
    </script>
<!-- Favicon -->
<link rel="icon" href="/favicon.ico?v=3" sizes="any">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png?v=3">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png?v=3">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png?v=3">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=3">
<link rel="manifest" href="/site.webmanifest?v=3">
</head>
<body>
    <header>
        <nav>
            <a href="../../" class="logo">
                <img src="../../assets/logo/logo-40.webp" alt="IndiaDostiChat logo" width="40" height="40" style="height: 40px;" decoding="async" onerror="this.style.display='none'">
                IndiaDostiChat
            </a>
            <div class="nav-controls" style="display: flex; align-items: center; gap: 10px;">
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle dark mode" title="Toggle dark mode">
                  <span class="theme-icon">🌙</span>
                </button>
                <button class="mobile-menu-btn" aria-label="Toggle navigation menu" id="mobile-menu-btn">
                    {menu_icon_svg}
                </button>
            </div>
            
            <ul class="nav-links">
                <li><a href="../../">Home</a></li>
                <li><a href="../../chat/">Chat</a></li>
                <li><a href="../../games/">Games</a></li>
                <li><a href="../../blog/">Blog</a></li>
                <li><a href="../../about/">About</a></li>
                <li><a href="../../rules/">Rules</a></li>
                <li><a href="../../contact/">Contact</a></li>
                <li><a href="../../donate/">Donate</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="landing-hero">
            <h1>{h1}</h1>
            <div class="blog-meta">
                <span>
                    {calendar_svg} May 31, 2026
                </span>
                <span>
                    <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> {read_time}
                </span>
                <span>
                    <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M7 7h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg> {category}
                </span>
            </div>
        </section>

        <div class="container" style="max-width: 900px; margin: 0 auto; padding: 0 1rem 3rem;">
            <!-- Hero Banner Image -->
            <img class="hero-banner" src="../../assets/images/topics/{slug}.webp" alt="{title}" width="800" height="800" decoding="async">

            <!-- Intro Section -->
            <section style="margin-bottom: 3rem; line-height: 1.8; color: var(--text-color); font-size: 1.08rem;">
                {content_html}

                <!-- Fast Join CTA Button -->
                <div style="text-align: center; margin: 3.5rem 0;">
                    <a href="../../chat/" class="btn-primary" style="font-size: 1.35rem; padding: 1.2rem 2.8rem; background-color: #28a745; border-color: #28a745; box-shadow: 0 4px 15px rgba(40,167,69,0.3); text-decoration: none; border-radius: 25px; display: inline-block; color: white; font-weight: bold; transition: transform 0.2s ease;">
                        Join Live Chat Room
                    </a>
                    <p style="font-size: 0.9rem; margin-top: 0.8rem; opacity: 0.7;">No registration required &bull; 100% Free &bull; Join in 5 seconds</p>
                </div>
            </section>

            <!-- Light FAQ section -->
            <section style="margin-bottom: 3.5rem;">
                <h2 style="color: var(--accent-color); margin-bottom: 2rem; font-size: 1.8rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem;">
                    Frequently Asked Questions
                </h2>
                <div class="faq-container">
                    {faqs_html}
                </div>
            </section>

            <!-- Related Blogs Section -->
            <section style="margin-top: 4rem; border-top: 1px solid var(--border-color); padding-top: 2rem;">
                <h3 style="color: var(--accent-color); margin-bottom: 1.2rem; font-size: 1.4rem;">Read More Community Articles</h3>
                <ul style="list-style: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.2rem; margin: 0;">
                    {related_links_html}
                </ul>
            </section>
        </div>
    </main>

    <footer>
        <div class="footer-content" style="max-width: 1200px; margin: 0 auto; padding: 3rem 1rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
            <div class="footer-section">
                <a href="../../" class="logo" style="color: white; margin-bottom: 1rem; display: inline-block; text-decoration: none;">
                    <img src="../../assets/logo/logo-30.webp" alt="IndiaDostiChat logo" width="30" height="30" style="height: 30px;" decoding="async" loading="lazy" onerror="this.style.display='none'"> 
                    IndiaDostiChat
                </a>
                <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.6;">
                    The premier destination for Indians globally to connect, share, and build friendships in a free Indian chat room.
                </p>
            </div>
            <div class="footer-section">
                <h4 style="color: #fff; margin-bottom: 1.2rem; font-size: 1.1rem;">Explore IndiaDostiChat</h4>
                <ul style="list-style: none; display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; padding: 0; margin: 0;">
                    <li><a href="../../" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Home</a></li>
                    <li><a href="../../chat/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Chat</a></li>
                    <li><a href="../../india-chat/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">India Chat</a></li>
                    <li><a href="../../allindiachat/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">All India Chat</a></li>
                    <li><a href="../../anonymous-indian-chat/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Anonymous Chat</a></li>
                    <li><a href="../../hindi-chat/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Hindi Chat</a></li>
                    <li><a href="../../desi-chat/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Desi Chat</a></li>
                    <li><a href="../../games/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Games</a></li>
                    <li><a href="../../donate/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Donate</a></li>
                    <li><a href="../../rules/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Rules</a></li>
                    <li><a href="../../contact/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Contact</a></li>
                    <li><a href="../../sitemap/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Sitemap</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4 style="color: #fff; margin-bottom: 1.2rem; font-size: 1.1rem;">Connect With Us</h4>
                <div class="social-links" style="display: flex; gap: 1.2rem; align-items: center; color: #cbd5e1;">
                    <a href="#" aria-label="Facebook" style="color: inherit; text-decoration: none;">{fb_svg}</a>
                    <a href="#" aria-label="Twitter" style="color: inherit; text-decoration: none;">{tw_svg}</a>
                    <a href="#" aria-label="Instagram" style="color: inherit; text-decoration: none;">{ig_svg}</a>
                </div>
            </div>
        </div>
        <div class="footer-bottom" style="display: flex; flex-direction: column; align-items: center; gap: 1rem; border-top: 1px solid var(--border-color); padding: 2rem 1rem 1rem; max-width: 1200px; margin: 0 auto; text-align: center;">
            <p style="margin: 0; color: #94a3b8; font-size: 0.9rem;">&copy; 2026 IndiaDostiChat.com. All Rights Reserved.</p>
            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem; font-weight: 500; font-size: 0.95rem; color: #aaa;">
                <div style="display: flex; align-items: center;">
                    {users_svg}
                    Community Visits: <span id="visitor-count" style="margin-left: 0.2rem;">Loading...</span>
                </div>
                <div style="display: flex; align-items: center;">
                    {comments_svg}
                    Chat Entries: <span id="join-count" style="margin-left: 0.2rem;">Loading...</span>
                </div>
            </div>
            <p style="font-size: 0.8rem; color: #777; margin: 0; max-width: 600px; line-height: 1.4;">
                Community activity is counted from real page visits and Join Chat actions, not random clicks.
            </p>
        </div>
    </footer>

    <script src="../../assets/js/main.min.js?v={js_version}" defer></script>
</body>
</html>
"""
    # Create directory for subpage
    subpage_dir = os.path.join(blog_dir, slug)
    os.makedirs(subpage_dir, exist_ok=True)
    
    subpage_file = os.path.join(subpage_dir, "index.html")
    with open(subpage_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated subpage: {subpage_file}")


# ----------------------------------------------------
# Now generate the central blog index page `/blog/index.html`
# ----------------------------------------------------

bc_index_schema = json.dumps({
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://www.indiadostichat.com/"
        },
        {
            "@type": "ListItem",
            "position": 2,
            "name": "Community Blog",
            "item": "https://www.indiadostichat.com/blog/"
        }
    ]
}, indent=2)

cards_html = ""
for config in blogs_data:
    slug = config["slug"]
    h1 = config["h1"]
    meta_desc = config["meta_desc"]
    read_time = config["read_time"]
    category = config["category"]
    
    cards_html += f"""
    <div class="card" style="border: 1px solid var(--border-color); border-radius: var(--border-radius); background: var(--card-bg); overflow: hidden; display: flex; flex-direction: column; transition: transform 0.2s ease, box-shadow 0.2s ease; box-shadow: 0 4px 10px rgba(0,0,0,0.02);">
        <img src="../assets/images/topics/{slug}-thumb.webp" alt="{h1}" width="300" height="300" style="width: 100%; height: 200px; object-fit: cover;" decoding="async" loading="lazy">
        <div style="padding: 1.5rem; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <div style="font-size: 0.8rem; font-weight: bold; color: var(--primary-color); text-transform: uppercase; margin-bottom: 0.5rem; display: flex; gap: 1rem;">
                    <span>{category}</span>
                    <span style="opacity: 0.6; font-weight: normal;">{read_time}</span>
                </div>
                <h3 style="margin-top: 0; margin-bottom: 0.8rem; color: var(--accent-color); font-size: 1.3rem; line-height: 1.4;">{h1}</h3>
                <p style="font-size: 0.92rem; line-height: 1.6; color: var(--text-color); margin-bottom: 1.5rem; opacity: 0.9;">{meta_desc}</p>
            </div>
            <a href="{slug}/" style="align-self: flex-start; padding: 0.6rem 1.5rem; background: var(--primary-color); color: #fff; text-decoration: none; border-radius: 20px; font-weight: bold; font-size: 0.9rem; transition: background 0.2s;">
                Read Article
            </a>
        </div>
    </div>
    """

index_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IndiaDostiChat Blog - Indian Chat & Cultural Exchange Topics</title>
    <meta name="description" content="Explore topics on Mumbai chat rooms, Indian-Korean friendship, language practice, and cultural exchange on the IndiaDostiChat blog.">
    <link rel="canonical" href="https://www.indiadostichat.com/blog/">
    
    <!-- Open Graph -->
    <meta property="og:title" content="IndiaDostiChat Blog - Indian Chat & Cultural Exchange Topics">
    <meta property="og:description" content="Explore topics on Mumbai chat rooms, Indian-Korean friendship, language practice, and cultural exchange on the IndiaDostiChat blog.">
    <meta property="og:url" content="https://www.indiadostichat.com/blog/">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://www.indiadostichat.com/assets/logo/logo.svg">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="IndiaDostiChat Blog - Indian Chat & Cultural Exchange Topics">
    <meta name="twitter:description" content="Explore topics on Mumbai chat rooms, Indian-Korean friendship, language practice, and cultural exchange on the IndiaDostiChat blog.">
    <meta name="twitter:image" content="https://www.indiadostichat.com/assets/logo/logo.svg">

    <link rel="stylesheet" href="../assets/css/style.min.css?v={css_version}">
    <link rel="prefetch" href="../chat/">
    
    <!-- Custom styling for index layout -->
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol" !important;
        }}
        .topics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 2rem;
            margin-top: 3rem;
        }}
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 25px rgba(0,0,0,0.06) !important;
        }}
        .landing-hero {{
            padding: 4rem 1rem;
            text-align: center;
            background: linear-gradient(135deg, var(--hero-bg-gradient-start, #0f172a), var(--hero-bg-gradient-end, #1e293b));
            color: #fff;
            margin-bottom: 2rem;
        }}
        .landing-hero h1 {{
            font-size: 2.8rem;
            margin-bottom: 1rem;
            font-weight: 700;
        }}
        @media (max-width: 768px) {{
            .landing-hero h1 {{
                font-size: 2rem !important;
            }}
            .landing-hero {{
                padding: 2.5rem 1rem !important;
            }}
            .topics-grid {{
                grid-template-columns: 1fr !important;
                gap: 1.5rem !important;
            }}
        }}
    </style>

    <!-- Schema JSON-LD -->
    <script type="application/ld+json">
    {bc_index_schema}
    </script>
<!-- Favicon -->
<link rel="icon" href="/favicon.ico?v=3" sizes="any">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png?v=3">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png?v=3">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png?v=3">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png?v=3">
<link rel="manifest" href="/site.webmanifest?v=3">
</head>
<body>
    <header>
        <nav>
            <a href="../" class="logo">
                <img src="../assets/logo/logo-40.webp" alt="IndiaDostiChat logo" width="40" height="40" style="height: 40px;" decoding="async" onerror="this.style.display='none'">
                IndiaDostiChat
            </a>
            <div class="nav-controls" style="display: flex; align-items: center; gap: 10px;">
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle dark mode" title="Toggle dark mode">
                  <span class="theme-icon">🌙</span>
                </button>
                <button class="mobile-menu-btn" aria-label="Toggle navigation menu" id="mobile-menu-btn">
                    {menu_icon_svg}
                </button>
            </div>
            
            <ul class="nav-links">
                <li><a href="../">Home</a></li>
                <li><a href="../chat/">Chat</a></li>
                <li><a href="../games/">Games</a></li>
                <li><a href="../blog/">Blog</a></li>
                <li><a href="../about/">About</a></li>
                <li><a href="../rules/">Rules</a></li>
                <li><a href="../contact/">Contact</a></li>
                <li><a href="../donate/">Donate</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="landing-hero">
            <h1>IndiaDostiChat Community Blog</h1>
            <p style="font-size: 1.25rem; max-width: 800px; margin: 0 auto; line-height: 1.6; opacity: 0.95;">
                Explore insights on Indian chat rooms, international friendships, language study roadmaps, and cross-cultural exchange.
            </p>
            <p style="font-size: 0.95rem; margin-top: 1rem; opacity: 0.8; font-weight: 500;">
                {calendar_svg} Updated for 2026
            </p>
        </section>

        <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 1rem 4rem;">
            <p style="line-height: 1.8; font-size: 1.1rem; color: var(--text-color); max-width: 800px; margin: 2rem auto 0; text-align: center;">
                Welcome to our official community blog. Here, we share guides, tips, and stories designed to help you get the most out of IndiaDostiChat. Whether you're interested in connecting with local Mumbaikars, practicing your Korean language skills, or understanding the cultural exchange between India and Korea, explore our featured articles below.
            </p>

            <div class="topics-grid">
                {cards_html}
            </div>
        </div>
    </main>

    <footer>
        <div class="footer-content" style="max-width: 1200px; margin: 0 auto; padding: 3rem 1rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
            <div class="footer-section">
                <a href="../" class="logo" style="color: white; margin-bottom: 1rem; display: inline-block; text-decoration: none;">
                    <img src="../assets/logo/logo-30.webp" alt="IndiaDostiChat logo" width="30" height="30" style="height: 30px;" decoding="async" loading="lazy" onerror="this.style.display='none'"> 
                    IndiaDostiChat
                </a>
                <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.6;">
                    The premier destination for Indians globally to connect, share, and build friendships in a free Indian chat room.
                </p>
            </div>
            <div class="footer-section">
                <h4 style="color: #fff; margin-bottom: 1.2rem; font-size: 1.1rem;">Explore IndiaDostiChat</h4>
                <ul style="list-style: none; display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; padding: 0; margin: 0;">
                    <li><a href="../" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Home</a></li>
                    <li><a href="../chat/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Chat</a></li>
                    <li><a href="../india-chat/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">India Chat</a></li>
                    <li><a href="../allindiachat/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">All India Chat</a></li>
                    <li><a href="../anonymous-indian-chat/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Anonymous Chat</a></li>
                    <li><a href="../hindi-chat/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Hindi Chat</a></li>
                    <li><a href="../desi-chat/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Desi Chat</a></li>
                    <li><a href="../games/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Games</a></li>
                    <li><a href="../donate/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Donate</a></li>
                    <li><a href="../rules/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Rules</a></li>
                    <li><a href="../contact/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Contact</a></li>
                    <li><a href="../sitemap/" style="color: #cbd5e1; text-decoration: none; font-size: 0.9rem;">Sitemap</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h4 style="color: #fff; margin-bottom: 1.2rem; font-size: 1.1rem;">Connect With Us</h4>
                <div class="social-links" style="display: flex; gap: 1.2rem; align-items: center; color: #cbd5e1;">
                    <a href="#" aria-label="Facebook" style="color: inherit; text-decoration: none;">{fb_svg}</a>
                    <a href="#" aria-label="Twitter" style="color: inherit; text-decoration: none;">{tw_svg}</a>
                    <a href="#" aria-label="Instagram" style="color: inherit; text-decoration: none;">{ig_svg}</a>
                </div>
            </div>
        </div>
        <div class="footer-bottom" style="display: flex; flex-direction: column; align-items: center; gap: 1rem; border-top: 1px solid var(--border-color); padding: 2rem 1rem 1rem; max-width: 1200px; margin: 0 auto; text-align: center;">
            <p style="margin: 0; color: #94a3b8; font-size: 0.9rem;">&copy; 2026 IndiaDostiChat.com. All Rights Reserved.</p>
            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem; font-weight: 500; font-size: 0.95rem; color: #aaa;">
                <div style="display: flex; align-items: center;">
                    {users_svg}
                    Community Visits: <span id="visitor-count" style="margin-left: 0.2rem;">Loading...</span>
                </div>
                <div style="display: flex; align-items: center;">
                    {comments_svg}
                    Chat Entries: <span id="join-count" style="margin-left: 0.2rem;">Loading...</span>
                </div>
            </div>
            <p style="font-size: 0.8rem; color: #777; margin: 0; max-width: 600px; line-height: 1.4;">
                Community activity is counted from real page visits and Join Chat actions, not random clicks.
            </p>
        </div>
    </footer>

    <script src="../assets/js/main.min.js?v={js_version}" defer></script>
</body>
</html>
"""

index_file = os.path.join(blog_dir, "index.html")
with open(index_file, "w", encoding="utf-8") as f:
    f.write(index_html_content)
print(f"Generated index page: {index_file}")

print("All blog pages generated successfully!")
