import os
import json

base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
blog_dir = os.path.join(base_dir, "blog")
os.makedirs(blog_dir, exist_ok=True)

css_version = "25"
js_version = "20"

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


# Data for individual blogs
blogs_data = [
    {
        "slug": "mumbai-chat-room",
        "title": "Mumbai Chat Room: Where Bollywood Dreams and Desi Hearts Connect Online",
        "h1": "Mumbai Chat Room: Where Bollywood Dreams and Desi Hearts Connect Online",
        "meta_desc": "Step into our free Mumbai chat room. Connect with Mumbaikars, discuss cutting chai, local train stories, Bollywood movies, and the city that never sleeps.",
        "category": "Desi Communities",
        "read_time": "5 min read",
        "intro_p": "Mumbai, the Maximum City, is a feeling carried by millions of people every single day. From late-night Marine Drive talks watching the waves silently to the daily local train stories, every Mumbaikar carries a unique vibe. But when the day ends and you look for a genuine conversation, where do you go? IndiaDostiChat Mumbai is built for those hearts. Whether you are returning home tired in crowded local trains or sitting with a cutting chai on your balcony, our online community brings Mumbaikars together for real, friendly, and emotional conversations without judgment.",
        "content_html": """
        <h2 style="color: var(--accent-color); margin-top: 2rem;">Mumbai Style Conversations</h2>
        <p>In our Mumbai chat room, the local spirit is alive in every line of text. You will instantly feel at home with phrases that represent the real Mumbai culture:</p>
        <ul style="line-height: 1.8; margin-bottom: 1.5rem;">
            <li><strong>"Kaay mhantay Mumbai?"</strong> - The classic Marathi greeting that starts the warmest friendships.</li>
            <li><strong>"Scene kya hai?"</strong> - Finding out what's trending around Bandra, Andheri, or South Bombay.</li>
            <li><strong>"Cutting chai pe discussion"</strong> - Simulating those roadside tea stall debates on cricket, movies, and weather.</li>
            <li><strong>"Local train late stories"</strong> - Sharing the collective sigh of relief when the local train finally arrives.</li>
        </ul>
        <p>Our community feels natural because users speak in Hindi, Marathi, English, or full Mumbai Hinglish. No pretenses, no verification pressure—just raw, authentic conversations.</p>

        <h2 style="color: var(--accent-color); margin-top: 2rem;">Why Mumbaikars Love IndiaDostiChat</h2>
        <p>Whether you're from Thane, Borivali, Dadar, or Navi Mumbai, here is why our platform stands out as the ultimate Mumbai chat community:</p>
        <ul style="line-height: 1.8; margin-bottom: 1.5rem;">
            <li><strong>Anonymous Nickname-Based Chatting:</strong> Protect your privacy. You don't need an email or phone verification. Just pick a nickname and start chatting.</li>
            <li><strong>Mobile-Optimized Experience:</strong> The lightweight interface loads in seconds on mobile browsers. No app downloads required, saving your phone storage.</li>
            <li><strong>Late-Night Active Users:</strong> Mumbai never sleeps, and neither do we. At 2 AM, you will find active users online sharing thoughts they cannot tell anyone else.</li>
            <li><strong>Desi Vibe:</strong> Discuss local train timings, rains, Ganpati celebrations, late-night street food cravings, and local street memes.</li>
        </ul>

        <h2 style="color: var(--accent-color); margin-top: 2rem;">Midnight Marine Drive Vibes: Rain, Music, and Connection</h2>
        <p>There is something magical about Mumbai nights, especially during monsoons. Rainy streets, earphones playing classic Bollywood romance tracks, and city lights reflecting on wet roads. When you're sitting alone and a stranger online asks a simple <em>"Kaise ho?"</em>, it feels more comforting than anything else. In the city of dreams where everyone is running, our chat room is a place to stop, breathe, and connect. Some talk about career pressure, some about heartbreaks, and some share dreams they never gave up on. Here, strangers slowly become familiar names, and simple messages become beautiful memories.</p>

        <h2 style="color: var(--accent-color); margin-top: 2rem;">Join the Maximum City Online Community</h2>
        <p>You don't have to navigate the fast life alone. Connect with real people who understand the hustle, the struggle, and the joy of being a Mumbaikar. Tap the CTA below, pick your nickname, and jump into the room. Let's share a digital cutting chai together!</p>
        """,
        "faqs": [
            ("Is there a dedicated chat room for Mumbai residents?", "Yes! Mumbaikars and those who love Mumbai culture gather in our main chat rooms, which act as a centralized, highly active hub for users from Mumbai, Delhi, Bangalore, and across India."),
            ("Do I need to sign up or download an app?", "No registration is needed. You can join the conversation using just a nickname, keeping your experience fast, secure, and private."),
            ("Can I chat in Marathi or Hinglish?", "Absolutely. We encourage cultural expression. People talk in Hindi, Marathi, English, or full Mumbai Hinglish without judgment."),
            ("Is the chat active late at night?", "Yes. Since Mumbai is the city that never sleeps, our chat room is highly active during late-night hours with users sharing late-night vibes, music, and deep thoughts.")
        ]
    },
    {
        "slug": "indian-korean-friendship",
        "title": "Indian Korean Friendship: Exploring Culture, Language, and Global Connections",
        "h1": "Indian Korean Friendship: Exploring Culture, Language, and Global Connections",
        "meta_desc": "Connect with Korean friends online. Practice language learning, share food recipes like kimchi and biryani, and explore cultural exchange between India and Korea.",
        "category": "Cultural Exchange",
        "read_time": "4 min read",
        "intro_p": "For many Indians, interest in South Korea begins with curiosity—discovering a K-drama, listening to a catchy K-pop track, or trying a spicy Korean dish. Over time, that simple curiosity often grows into a deep appreciation for Korean culture, language, and history. Conversely, South Koreans are increasingly fascinated by India's rich traditions, diversity, and wellness practices. Friendship is the strongest bridge between these two worlds. Through online communities and language exchange, Indians and Koreans are connecting to build authentic international friendships.",
        "content_html": """
        <h2 style="color: var(--accent-color); margin-top: 2rem;">Bridges of Connection: Food, Language, and Travel</h2>
        <p>Online friendship communities are thriving because people want authentic, respectful interactions with native speakers. It's a space free from stereotypes where you can learn directly from real people. Here are the core topics that spark conversations between Indian and Korean peers:</p>

        <h3 style="color: var(--primary-color); margin-top: 1.5rem;">1. Language Practice and Exchange</h3>
        <p>Language learning is a major driver of these friendships. Indian learners interested in Korean can practice Hangul (alphabet), grammar, and colloquial phrases with native speakers. In return, Korean speakers can practice English or learn basic Hindi words. This mutual exchange creates a positive, supportive environment where everyone benefits and grows together.</p>

        <h3 style="color: var(--primary-color); margin-top: 1.5rem;">2. Culinary Exchange: Kimchi Meets Biryani</h3>
        <p>Food is a universal language that brings cultures together. Korean dishes like <strong>Kimchi, Bibimbap, Bulgogi, and Tteokbokki</strong> have gained massive popularity in Indian cities. At the same time, Korean friends enjoy learning about the complex spices of Indian cuisine, discussing dishes like <strong>Biryani, Dosa, Samosas, and local street foods</strong>. Sharing recipes and food stories is an instant conversation starter.</p>

        <h3 style="color: var(--primary-color); margin-top: 1.5rem;">3. Travel and Cultural Exploration</h3>
        <p>Both countries offer breathtaking landscapes and historical landmarks. Friends often discuss travel itineraries—sharing tips on visiting Seoul, Busan, or Jeju Island, and suggesting beautiful destinations in India like Delhi, Mumbai, Hyderabad, Goa, Kerala, and Bengaluru. These exchange chats inspire future travel plans and strengthen bonds.</p>

        <h2 style="color: var(--accent-color); margin-top: 2rem;">Respect and Understanding Across Borders</h2>
        <p>Through respectful dialogue on platforms like IndiaDostiChat, members learn about family values, work culture, festivals, and daily lifestyles. By exchanging perspectives, they challenge cultural assumptions and develop a global outlook. Friendship has no borders, and every conversation brings people closer. If you want to practice your Korean, share K-drama theories, or simply meet friendly people from South Korea, your journey begins with a simple, polite conversation.</p>
        """,
        "faqs": [
            ("How can I find Korean friends online safely?", "You can join dedicated cultural chat rooms on IndiaDostiChat. Because the platform is anonymous and nickname-based, you can chat safely without sharing personal social media profiles or phone numbers."),
            ("Is language learning possible through text chat?", "Yes! Text chat is excellent for language practice. You can learn Hangul, practice basic grammar, and receive real-time corrections from native speakers."),
            ("What topics are popular in Indian-Korean chat rooms?", "Members discuss K-pop comebacks, popular K-dramas, food recipes (like ramyeon and biryani), travel spots in Seoul and Goa, and daily life experiences."),
            ("Are there guidelines for respectful conversation?", "Yes. We maintain a zero-tolerance policy against hate speech, stereotypes, and disrespectful comments. Cultivating mutual respect is essential for cross-cultural friendships.")
        ]
    },
    {
        "slug": "india-korea-cultural-exchange-community",
        "title": "India-Korea Cultural Exchange Community: Friendship, Study, Travel, and Opportunities",
        "h1": "India-Korea Cultural Exchange Community: Friendship, Study, Travel, and Opportunities",
        "meta_desc": "Join our India-Korea cultural exchange community. Explore language roadmaps, study resources, scholarship guides, jobs in Korea, travel tips, and cultural similarities.",
        "category": "Community Guide",
        "read_time": "6 min read",
        "intro_p": "The partnership between India and South Korea has evolved from diplomatic ties into a vibrant cultural connection. Today, millions of young minds in both nations are discovering each other's heritage. IndiaDostiChat provides a dedicated, moderated environment to connect these individuals. Whether you want to learn Korean, find resources for studying in South Korea, explore career opportunities in multinational corporations, or chat about travel tips, our cultural exchange community is your go-to guide.",
        "content_html": """
        <h2 style="color: var(--accent-color); margin-top: 2rem;">Why South Korea is Popular Among Indians</h2>
        <p>South Korea attracts Indian students and professionals for a variety of reasons:</p>
        <ul style="line-height: 1.8; margin-bottom: 1.5rem;">
            <li><strong>World-Class Education:</strong> Korean universities offer advanced scientific research, cutting-edge technology, and top global rankings.</li>
            <li><strong>Career Growth:</strong> Global conglomerates like Samsung, LG, Hyundai, and Kia offer exciting careers for skilled professionals.</li>
            <li><strong>Hallyu Wave:</strong> The global spread of K-Pop, Korean movies, and dramas has created a deep interest in the country's language and lifestyle.</li>
            <li><strong>Safe & Modern Cities:</strong> Cities like Seoul and Busan are known for safety, clean infrastructure, and modern public transit.</li>
        </ul>

        <h2 style="color: var(--accent-color); margin-top: 2rem;">Why Koreans Are Interested in India</h2>
        <p>At the same time, South Koreans are deeply curious about India's diverse heritage:</p>
        <ul style="line-height: 1.8; margin-bottom: 1.5rem;">
            <li><strong>Rich History & Heritage:</strong> India's centuries-old monuments, philosophy, and historical links attract cultural tourists.</li>
            <li><strong>Yoga and Wellness:</strong> Traditional Indian spiritual practices, yoga, and meditation are popular in Korea.</li>
            <li><strong>Market Potential & Tech Collaboration:</strong> Korea's hardware strength combined with India's software talent creates strong business opportunities.</li>
            <li><strong>Culinary Variety:</strong> The complex flavors of Indian curries, biryani, and regional dishes are highly popular among Korean food lovers.</li>
        </ul>

        <h2 style="color: var(--accent-color); margin-top: 2rem;">Korean Language Learning Roadmap</h2>
        <p>Mastering a new language requires a systematic approach. Here is a roadmap recommended by our community members:</p>
        <ol style="line-height: 1.8; margin-bottom: 1.5rem;">
            <li><strong>Beginner:</strong> Master Hangul (the Korean alphabet). It is highly logical and can be learned in a few hours. Learn basic greetings and simple vocabulary.</li>
            <li><strong>Intermediate:</strong> Focus on grammar structures, verb conjugations, and honorific levels (which are crucial in Korean social hierarchy). Practice forming basic conversational sentences.</li>
            <li><strong>Advanced:</strong> Watch dramas without subtitles, read Korean news articles, and engage in real-time conversation practice with native speakers on platforms like IndiaDostiChat.</li>
        </ol>

        <h2 style="color: var(--accent-color); margin-top: 2rem;">Study & Job Opportunities: Visas and Scholarships</h2>
        <p>For students, the <strong>Global Korea Scholarship (GKS)</strong> is a premium opportunity that covers full tuition, flights, monthly allowances, and language training. Top universities include Seoul National University (SNU), KAIST, Yonsei, and Korea University. When it comes to jobs, demand is rising for Indian software developers, research scientists, and international trade specialists in South Korea. Knowing the Korean language is a major advantage for career growth in Korean companies operating in India, such as Hyundai, Samsung, and LG.</p>

        <h2 style="color: var(--accent-color); margin-top: 2rem;">Shared Values and Cultural Similarities</h2>
        <p>Despite geographical distance, India and Korea share deep social values. Both cultures emphasize respect for elders (using honorific language), prioritising family relationships, maintaining academic discipline, and showing warm hospitality to guests. This shared societal foundation makes it easy for Indians and Koreans to form deep, long-lasting friendships.</p>
        """,
        "faqs": [
            ("What is the Global Korea Scholarship (GKS)?", "The GKS is a fully-funded scholarship program by the South Korean government for international students to pursue undergraduate and postgraduate degrees in Korea."),
            ("Are there job opportunities in South Korea for Indians?", "Yes. Opportunities are abundant in IT, engineering, software development, biotechnology, and multinational corporate roles."),
            ("How long does it take to learn basic conversational Korean?", "With daily practice, most learners can grasp basic conversational Korean in 3 to 6 months. Learning the Hangul alphabet takes only a few hours."),
            ("What is the best way to practice speaking Korean?", "Practicing with native speakers in language exchange communities is the most effective way. IndiaDostiChat provides a safe space for real-time text practice.")
        ]
    },
    {
        "slug": "india-korea-cultural-exchange-complete-guide",
        "title": "India-Korea Cultural Exchange: The Complete Guide to Language, Education, and Careers",
        "h1": "India-Korea Cultural Exchange: The Complete Guide to Language, Education, and Careers",
        "meta_desc": "Our ultimate pillar guide to India-Korea cultural exchange. Discover language roadmaps, study abroad scholarships, job search tips, travel guides, and food culture.",
        "category": "Pillar Article",
        "read_time": "12 min read",
        "intro_p": "The connection between India and South Korea has grown exceptionally. What began as trade has evolved into a deep cultural exchange. Today, young Indians and South Koreans are connecting through technology, music, language, travel, and career aspirations. This comprehensive guide provides a detailed roadmap for anyone interested in navigating the cultural bridge between India and South Korea.",
        "content_html": "",  # Generated dynamically below to prevent redundancy
        "faqs": [
            ("What is the historical connection between India and Korea?", "According to ancient texts, Princess Suriratna from Ayodhya traveled to Korea in 48 AD and married King Kim Suro of Geumgwan Gaya, becoming Queen Heo Hwang-ok. This historic connection is still celebrated today."),
            ("What is the Global Korea Scholarship (GKS)?", "The GKS is a prestigious fully-funded scholarship program covering tuition fees, round-trip airfare, monthly stipend, settlement allowance, and insurance for international students studying in South Korea."),
            ("Can Indian software developers find jobs in South Korea?", "Yes, there is high demand for IT professionals, semiconductor researchers, and AI developers in South Korea, with giants like Samsung and LG actively hiring global talent."),
            ("Is learning Hangul difficult for Indian speakers?", "No, Hangul is one of the most scientific and logical alphabets in the world. Many Indian speakers find it easy to pick up due to similar phonetic structures between Korean and Indian languages like Hindi and Tamil.")
        ]
    }
]

# Set complete guide content
complete_guide = blogs_data[3]
complete_guide["content_html"] = """
            <!-- Table of Contents -->
            <div class="toc-container" style="background: var(--card-bg); border: 1px solid var(--border-color); border-radius: var(--border-radius); padding: 1.8rem; margin: 2rem 0; box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
                <h3 style="margin-top: 0; color: var(--accent-color); font-size: 1.25rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
                    <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h7"/></svg>
                    Table of Contents
                </h3>
                <nav>
                    <ol style="line-height: 2; font-size: 0.98rem; padding-left: 1.2rem; margin: 0; color: var(--primary-color);">
                        <li><a href="#intro" style="color: inherit; text-decoration: none; font-weight: 500;">1. Introduction to India–Korea Cultural Exchange</a></li>
                        <li><a href="#connecting" style="color: inherit; text-decoration: none; font-weight: 500;">2. Why Koreans and Indians Are Connecting</a></li>
                        <li><a href="#friendship" style="color: inherit; text-decoration: none; font-weight: 500;">3. Friendship Across Borders</a></li>
                        <li><a href="#language" style="color: inherit; text-decoration: none; font-weight: 500;">4. Learning Korean Language</a></li>
                        <li><a href="#students" style="color: inherit; text-decoration: none; font-weight: 500;">5. Indian Students in Korea</a></li>
                        <li><a href="#scholarships" style="color: inherit; text-decoration: none; font-weight: 500;">6. Scholarships and Universities</a></li>
                        <li><a href="#jobs" style="color: inherit; text-decoration: none; font-weight: 500;">7. Jobs and Careers in South Korea</a></li>
                        <li><a href="#culture" style="color: inherit; text-decoration: none; font-weight: 500;">8. Korean Culture and Traditions</a></li>
                        <li><a href="#visitors" style="color: inherit; text-decoration: none; font-weight: 500;">9. Indian Culture for Korean Visitors</a></li>
                        <li><a href="#travel" style="color: inherit; text-decoration: none; font-weight: 500;">10. Travel Guide to Korea</a></li>
                        <li><a href="#food" style="color: inherit; text-decoration: none; font-weight: 500;">11. Food, Festivals and Community</a></li>
                        <li><a href="#tech" style="color: inherit; text-decoration: none; font-weight: 500;">12. Technology and Innovation</a></li>
                        <li><a href="#exchange" style="color: inherit; text-decoration: none; font-weight: 500;">13. Language Exchange Communities</a></li>
                        <li><a href="#future" style="color: inherit; text-decoration: none; font-weight: 500;">14. Future of India–Korea Relations</a></li>
                        <li><a href="#join" style="color: inherit; text-decoration: none; font-weight: 500;">15. Why Join IndiaDostiChat.com</a></li>
                        <li><a href="#conclusion" style="color: inherit; text-decoration: none; font-weight: 500;">16. Conclusion</a></li>
                    </ol>
                </nav>
            </div>

            <section id="intro" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">1. Introduction to India–Korea Cultural Exchange</h2>
                <p>The cultural relationship between India and South Korea has blossomed over the past two decades. What was once a relationship driven by geopolitical treaties and corporate trade has now matured into a deep social connection. The Hallyu (Korean Wave) has captured the imagination of millions of Indian youth, who love K-pop, K-dramas, skincare, and Korean food. Simultaneously, Koreans are discovering the depth of Indian philosophy, history, and yoga. Online platforms have simplified this connection, enabling language learners, students, and travelers from both nations to connect directly.</p>
            </section>

            <section id="connecting" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">2. Why Koreans and Indians Are Connecting</h2>
                <p>Curiosity is the starting point. Indian youth are highly interested in Korean pop culture, but this interest quickly expands to professional aspirations, travel planning, and education. On the other hand, Korean nationals are fascinated by India's massive cultural diversity, spiritual heritage, yoga traditions, and organic food practices. In a digitized world, these two demographics are connecting to exchange perspectives, build long-term relationships, and share opportunities in tech, tourism, and academics.</p>
            </section>

            <section id="friendship" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">3. Friendship Across Borders</h2>
                <p>Cross-border friendships allow individuals to challenge regional stereotypes, practice new languages with native speakers, and build global awareness. Talking to real peers online reveals shared human experiences. Whether sharing stories about family structures, study habits, or favorite meals, these international friendships build mutual empathy and pave the way for cross-cultural collaboration.</p>
            </section>

            <section id="language" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">4. Learning Korean Language</h2>
                <p>Korean has become one of the fastest-growing foreign languages in India. The Korean alphabet, Hangul, is famous for its logical structure and phonetic clarity, making it accessible to beginners. Learning Korean opens significant avenues—improving eligibility for scholarships, qualifying for roles in multinational Korean conglomerates, and allowing travelers to explore South Korea without language barriers. Dedicated practice, combined with peer conversations, is key to fluency.</p>
            </section>

            <section id="students" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">5. Indian Students in Korea</h2>
                <p>South Korea has emerged as a premier destination for higher education, particularly in STEM, biotechnology, and business administration. Indian students benefit from state-of-the-art laboratory facilities, competitive academic programs, and safe campus environments. Living in South Korea offers students a unique blend of modern convenience and rich traditional culture, preparing them for careers in global research and development.</p>
            </section>

            <section id="scholarships" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">6. Scholarships and Universities</h2>
                <p>The Global Korea Scholarship (GKS), fully funded by the Korean government, is highly sought after by Indian applicants. It covers full tuition fees, monthly stipends, airfare, and a mandatory year of language training. Top institutions like Seoul National University, KAIST, Yonsei University, Korea University, and Sungkyunkwan University offer world-class English-taught degrees, making international education highly accessible.</p>
            </section>

            <section id="jobs" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">7. Jobs and Careers in South Korea</h2>
                <p>South Korea's job market is open to skilled international professionals, particularly in tech, semiconductors, artificial intelligence, automotive engineering, and international business. Companies like Samsung, LG, Hyundai, and Kia recruit global talent. Additionally, Korean language proficiency is a massive asset for Indian professionals seeking roles in Korean corporate subsidiaries operating in India.</p>
            </section>

            <section id="culture" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">8. Korean Culture and Traditions</h2>
                <p>Korean culture places a strong emphasis on community harmony and respect. Bowing is the standard greeting, and hierarchy is reflected in how language honorifics are used. Dining etiquette, such as waiting for the elders to lift their utensils first, is highly valued. Holidays like Seollal (Lunar New Year) and Chuseok (Harvest Festival) are celebrated with traditional food and family gatherings, reflecting values shared closely with Indian culture.</p>
            </section>

            <section id="visitors" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">9. Indian Culture for Korean Visitors</h2>
                <p>For Koreans visiting India, the diversity is fascinating. From historical architectures to the warm concept of "Atithi Devo Bhava" (the guest is god), India offers hospitality at every step. Korean visitors enjoy exploring major festivals like Diwali and Holi, learning about the philosophy of yoga, and trying diverse regional cuisines, which helps bridge understanding between the two societies.</p>
            </section>

            <section id="travel" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">10. Travel Guide to Korea</h2>
                <p>Traveling in South Korea is highly convenient due to its rapid public transportation network and high-speed rail systems. Must-visit places include Seoul (for Gyeongbokgung Palace, shopping districts, and city views from N Seoul Tower), Busan (for its seaside temples and Haeundae beach), and Jeju Island (for natural volcanic landscapes). The country is incredibly safe, clean, and welcoming for international backpackers.</p>
            </section>

            <section id="food" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">11. Food, Festivals and Community</h2>
                <p>Culinary exchange is at the heart of community building. Korean foods like Kimchi, Ramyeon, and Bibimbap have become popular staples in urban Indian households. In return, Indian curries, flatbreads (Naan), and regional samosas are appreciated by Korean food lovers. Food festivals and community cooking challenges serve as great opportunities for cultural integration.</p>
            </section>

            <section id="tech" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">12. Technology and Innovation</h2>
                <p>Technology binds the future of both countries. South Korea is a global pioneer in hardware manufacturing, electronics, and automotive engineering, while India is a powerhouse in software development, AI models, and dynamic tech startups. Collaborative engineering programs, tech workshops, and research exchange prepare young professionals from both nations for a competitive future.</p>
            </section>

            <section id="exchange" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">13. Language Exchange Communities</h2>
                <p>Language exchange is an organic method to gain fluency. Connecting with native speakers in a relaxed, friendly environment helps learners overcome conversational hesitation. Text-based chats allow learners to write, edit, and read messages at their own pace, making it an excellent starting point for beginners who are self-studying Korean or English.</p>
            </section>

            <section id="future" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">14. Future of India–Korea Relations</h2>
                <p>The bilateral relationship between India and South Korea is poised for expansion. Joint efforts in green energy, semiconductor supply chains, smart cities, and digital health will open up career pathways. Culturally, academic collaborations, tourism initiatives, and media partnerships will continue to foster deep mutual respect and friendship between citizens.</p>
            </section>

            <section id="join" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">15. Why Join IndiaDostiChat.com</h2>
                <p>Unlike social networks that demand phone numbers, personal verification, or linking accounts, IndiaDostiChat.com offers a private, secure, and completely free chat experience. You can chat anonymously by simply choosing a nickname. Our web client is lightweight and optimized for mobile devices, and active volunteer moderators prevent spam and toxicity, ensuring a clean space for cultural exchange.</p>
            </section>

            <section id="conclusion" style="margin-bottom: 2.5rem;">
                <h2 style="color: var(--accent-color); font-size: 1.6rem; border-left: 4px solid var(--primary-color); padding-left: 0.8rem;">16. Conclusion</h2>
                <p>Friendship builds understanding, which builds respect, and ultimately forms international bridges. Through language practice, travel exchange, educational resources, and friendly conversations, India and South Korea are building a stronger relationship for future generations. Your contribution to this cultural exchange begins with a simple conversation. Grab a nickname and start chatting today!</p>
            </section>
"""

# Let's generate the individual blog subpages
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
    
    # Generate related blog articles links (the other 3)
    related_links_html = ""
    for other in blogs_data:
        if other["slug"] != slug:
            related_links_html += f'<li><a href="../{other["slug"]}/" style="color: var(--primary-color); text-decoration: none; font-weight: 500;">{other["title"]}</a></li>\n'
            
    # Compile schema objects
    bc_schema = make_bc_schema(slug, title)
    faq_schema = make_faq_schema(faqs)
    posting_schema = make_posting_schema(slug, title, meta_desc)
    
    # Generate list of FAQs html
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
                <p style="margin-bottom: 1.5rem; font-size: 1.15rem; line-height: 1.8; font-weight: 500; opacity: 0.95;">{intro_p}</p>
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

# Breadcrumb schema for blog index page
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
