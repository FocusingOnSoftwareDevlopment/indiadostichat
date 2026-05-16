import os
import re

city_data = {
    "bangalore": {
        "title": "Bangalore Chat Room",
        "intro": "Looking for a tech-savvy **Bangalore chat room**? IndiaDostiChat provides users from the Silicon Valley of India and beyond a fast and secure way to connect. Bangalore, known for its pleasant weather, vibrant pub culture, and booming IT industry, is home to a diverse and intellectual community. Whether you're a software engineer in Electronic City or a student in Koramangala, our chat room is the perfect place to meet fellow Bangaloreans.",
        "section1": "Connect with Bangalore's Tech Community",
        "text1": "Bangalore is a hub of innovation, and our chat rooms reflect that. You'll find many users discussing the latest in technology, startups, and gaming. It's a great place to network and find like-minded individuals who share your interests in the digital world.",
        "food": "Masala Dosa and Filter Coffee",
        "vibe": "Garden City and Pub Capital"
    },
    "kolkata": {
        "title": "Kolkata Chat Room",
        "intro": "Welcome to the **Kolkata chat room** on IndiaDostiChat. Kolkata, the City of Joy, is famous for its rich literary heritage, colonial architecture, and deep-rooted love for art and music. Our community in Kolkata is known for its passionate discussions on everything from football to politics and the latest cultural festivals.",
        "section1": "Experience the Cultural Hub of India",
        "text1": "Kolkata has a soul like no other city. Our chat rooms are a digital extension of the city's famous 'Adda' culture—where people gather for intellectual and lively conversations. Join us to share your love for Roshogollas, the iconic Howrah Bridge, and the vibrant atmosphere of Park Street.",
        "food": "Sweets and Street Food",
        "vibe": "Literary and Artistic"
    },
    "chennai": {
        "title": "Chennai Chat Room",
        "intro": "Join the **Chennai chat room** on IndiaDostiChat and connect with users from the Gateway to South India. Chennai is a city of traditions, famous for its Bharatanatyam, Carnatic music, and the beautiful Marina Beach. Our Chennai community is warm, welcoming, and loves to engage in meaningful conversations.",
        "section1": "Connect with the Heart of Tamil Culture",
        "text1": "Chennai's mix of traditional values and modern growth makes it a fascinating place. In our chat rooms, you can discuss the latest Tamil cinema news, the excitement of the IPL, or simply find a friend to talk about your day. It's a safe and friendly space for all residents of the city.",
        "food": "Idli, Sambar, and Filter Coffee",
        "vibe": "Cultural and Coastal"
    },
    "hyderabad": {
        "title": "Hyderabad Chat Room",
        "intro": "Welcome to the **Hyderabad chat room**! Known as the City of Pearls and a major tech hub, Hyderabad offers a unique blend of Nizami heritage and modern lifestyle. Our Hyderabad community is active and diverse, reflecting the city's welcoming and multicultural spirit.",
        "section1": "Join the Vibrant Hyderabadi Community",
        "text1": "From the historic Charminar to the high-tech Hitech City, Hyderabad is a city of contrasts. In our rooms, you can discuss the world-famous Hyderabadi Biryani, the latest Tollywood movies, or the city's growing startup scene. It's the perfect place to meet new friends from the region.",
        "food": "Hyderabadi Biryani and Irani Chai",
        "vibe": "Historic and High-Tech"
    },
    "pune": {
        "title": "Pune Chat Room",
        "intro": "Looking for a **Pune chat room**? Join IndiaDostiChat to connect with users from the Cultural Capital of Maharashtra and the Oxford of the East. Pune is known for its prestigious educational institutions, growing IT sector, and beautiful surrounding hills.",
        "section1": "Connect with Pune's Youthful Energy",
        "text1": "Pune's large student population and young professional community make our chat rooms incredibly dynamic. Whether you want to discuss the latest events at Savitribai Phule Pune University or plan a trek to Sinhagad Fort, you'll find plenty of company here.",
        "food": "Misal Pav and Bhakarwadi",
        "vibe": "Educational and Energetic"
    },
    "jaipur": {
        "title": "Jaipur Chat Room",
        "intro": "Welcome to the **Jaipur chat room**! The Pink City of India is world-renowned for its majestic forts, palaces, and vibrant heritage. Our Jaipur community is proud of its royal history and loves to share the city's beauty with others.",
        "section1": "Experience the Royalty of Jaipur",
        "text1": "In our chat rooms, you can discuss the stunning architecture of Amer Fort, the colorful markets of the old city, and the rich Rajasthani culture. It's a great place to meet local residents and those who admire the city from afar.",
        "food": "Dal Baati Churma and Ghevar",
        "vibe": "Royal and Colorful"
    },
    "ahmedabad": {
        "title": "Ahmedabad Chat Room",
        "intro": "Join the **Ahmedabad chat room** on IndiaDostiChat! Ahmedabad, a UNESCO World Heritage City, is a hub of commerce, textiles, and vibrant Gujarati culture. Our community here is known for its entrepreneurial spirit and friendly nature.",
        "section1": "Connect with Ahmedabad's Business Spirit",
        "text1": "Ahmedabad is a city that loves to celebrate, especially during Navratri. In our rooms, you can discuss the city's industrial growth, the peaceful Sabarmati Ashram, and the bustling food streets like Manek Chowk.",
        "food": "Dhokla, Khandvi, and Thali",
        "vibe": "Commercial and Cultural"
    },
    "lucknow": {
        "title": "Lucknow Chat Room",
        "intro": "Welcome to the **Lucknow chat room**! The City of Nawabs is famous for its 'Tehzeeb' (etiquette), beautiful Chikankari work, and exquisite Awadhi cuisine. Our Lucknow community is polite, cultured, and loves a good conversation.",
        "section1": "Experience the Elegance of Lucknow",
        "text1": "In our chat rooms, you can discuss the grand architecture of Bara Imambara, the peaceful Rumi Darwaza, and the legendary kebabs of Tunday Kababi. It's a place where tradition meets modernity in the most graceful way.",
        "food": "Kabab and Biryani",
        "vibe": "Elegant and Historical"
    },
    "surat": {
        "title": "Surat Chat Room",
        "intro": "Join the **Surat chat room**! Known as the Diamond City of India, Surat is a major hub for textiles and diamond polishing. Our Surat community is hardworking, prosperous, and loves to socialize.",
        "section1": "Connect with Surat's Industrial Might",
        "text1": "Surat is one of the cleanest and fastest-growing cities in India. In our rooms, you can discuss the city's massive textile markets, its clean streets, and the shared love for unique Surati food items.",
        "food": "Undhiyu and Locho",
        "vibe": "Industrial and Prosperous"
    },
    "kanpur": {
        "title": "Kanpur Chat Room",
        "intro": "Welcome to the **Kanpur chat room**! Known as the Leather City of the World, Kanpur is a major industrial and educational center in Uttar Pradesh. our community here is active, practical, and grounded.",
        "section1": "Join Kanpur's Industrial Community",
        "text1": "Kanpur is a city with a strong industrial heritage and a bustling market life. In our rooms, you can discuss the latest in the city's growth, its educational institutions like IIT Kanpur, and the local news of the region.",
        "food": "Thaggu Ke Laddu and Chaat",
        "vibe": "Industrial and Educational"
    }
}

template = """            <section style="margin-bottom: 3rem; line-height: 1.8; color: var(--text-color);">
                <p>{intro}</p>
                
                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">{section1}</h2>
                <p>On IndiaDostiChat, we provide a platform that matches the vibrant spirit of {city_name}. {text1} Connecting with people from your own city brings a level of comfort that is hard to find elsewhere. Whether you're a student, a professional, or someone looking to socialize, our platform offers a safe and anonymous space for everyone.</p>
                
                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Why Users from {city_name} Choose IndiaDostiChat</h2>
                <p>{city_name} is a city of growth and energy. Our IRC-based platform ensures that your messages are delivered instantly, even on slower mobile data connections. We prioritize your privacy—no registration, no personal data, just a nickname and you're in. This 'no-nonsense' approach is what makes us a top choice for users in the city.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Discussing {city_name} Culture and {food}</h2>
                <p>{city_name} has a rich cultural heritage that is a point of pride for its residents. From its famous {food} to its unique {vibe} vibe, there's always something to talk about. Our chat rooms are a great place to share recommendations, discuss local news, and celebrate the identity of your city with others.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Safe and Moderated Desi Chat Community</h2>
                <p>Safety is a non-negotiable for us. We understand that many users in {city_name} are looking for a respectful place to socialize. Our dedicated moderation team ensures that the rooms are free from spam, harassment, and inappropriate content. Check our <a href="rules.html">Chat Rules</a> to see how we keep our environment positive for everyone.</p>

                <div style="text-align: center; margin: 3rem 0;">
                    <a href="chat.html" class="btn-primary" style="font-size: 1.2rem; padding: 1rem 2.5rem;">Join IndiaDostiChat Main Room</a>
                </div>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Join from Mobile or Desktop</h2>
                <p>IndiaDostiChat is a 100% web-based platform. You can access our chat directly from your mobile browser while you're on the move or from your desktop at home. Our interface is designed to be responsive and easy to navigate, providing a premium experience on all devices.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Interactive IRC Games</h2>
                <p>To make your time even more exciting, we offer integrated games like **Monster Hunt** and **Trivia**. You can collaborate with other users to hunt digital monsters or test your knowledge in our trivia room. These games are a great way to break the ice and build stronger connections with other chatters.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Building Desi Friendships Online</h2>
                <p>IndiaDostiChat is more than just a website; it's a social hub. Many of our users have formed genuine friendships that have lasted for years. Whether you're looking for a casual chat or a long-term friend, you'll find a welcoming community here that understands your cultural background.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Conclusion</h2>
                <p>IndiaDostiChat is the premier choice for people in {city_name} looking for a reliable and engaging online chat experience. By focusing on privacy, safety, and community, we have built a platform that truly serves the needs of modern Indian users. Join the IndiaDostiChat main room today and start your journey of desi friendship and fun!</p>
            </section>"""

def expand_all(root_dir):
    for city, data in city_data.items():
        filename = f"{city}-chat-room.html"
        filepath = os.path.join(root_dir, filename)
        
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue
            
        print(f"Expanding {filename}...")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Format the template
        new_section = template.format(
            city_name=city.capitalize(),
            intro=data['intro'],
            section1=data['section1'],
            text1=data['text1'],
            food=data['food'],
            vibe=data['vibe']
        )
        
        # Replace the section
        # Use regex to find the section between <main> and </main> or specific tags
        pattern = re.compile(r'<section style="margin-bottom: 3rem; line-height: 1.8; color: var\(--text-color\);">(.*?)</section>', re.DOTALL)
        if not pattern.search(content):
            # Try the old color pattern
            pattern = re.compile(r'<section style="margin-bottom: 3rem; line-height: 1.8; color: #444;">(.*?)</section>', re.DOTALL)
            
        if pattern.search(content):
            content = pattern.sub(new_section, content)
            
            # Also update FAQ for uniqueness
            faq_pattern = re.compile(r'<section class="faq-section".*?>(.*?)</section>', re.DOTALL)
            new_faq = f'''<section class="faq-section" style="background: #f1f1f1; padding: 2rem; border-radius: 10px;">
                <h2 style="margin-bottom: 1.5rem; text-align: center;">Frequently Asked Questions about {city.capitalize()} Chat</h2>
                <div style="margin-bottom: 1rem;">
                    <strong>Is there a specific {city.capitalize()} chat room?</strong>
                    <p>While everyone from {city.capitalize()} gathers in our main IndiaDostiChat room to keep the conversation lively, you'll find plenty of fellow residents to talk to.</p>
                </div>
                <div style="margin-bottom: 1rem;">
                    <strong>Is IndiaDostiChat free for users in {city.capitalize()}?</strong>
                    <p>Absolutely! It is 100% free and requires no registration or personal details.</p>
                </div>
                <div style="margin-bottom: 1rem;">
                    <strong>Can I use a nickname?</strong>
                    <p>Yes, anonymity is our priority. You can choose any nickname you like and start chatting instantly.</p>
                </div>
            </section>'''
            content = faq_pattern.sub(new_faq, content)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        else:
            print(f"Could not find section in {filename}")

expand_all('.')
print("All major city pages expanded.")
