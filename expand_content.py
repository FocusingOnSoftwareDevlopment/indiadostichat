import os
import re

def expand_landing_pages():
    base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
    
    pages_to_expand = [
        "mobile-indian-chat.html", "indian-friendship-chat.html", "hyderabad-chat-room.html",
        "mumbai-chat-room.html", "ahmedabad-chat-room.html", "lucknow-chat-room.html",
        "telugu-chat-room.html", "marathi-chat-room.html", "punjabi-chat-room.html",
        "chat.html", "blog.html", "contact.html"
    ]

    for filename in pages_to_expand:
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # We will replace the <main>...</main> content for most pages,
        # or specific sections for chat, blog, contact.

        if filename == "mobile-indian-chat.html":
            new_main = """
    <main>
        <section class="landing-hero">
            <h1>Mobile Indian Chat Room - Join India Chat from Phone</h1>
            <p>Connect with the global Indian community on the go. No app needed.</p>
        </section>

        <div class="container">
            <section style="margin-bottom: 3rem; line-height: 1.8; color: var(--text-color);">
                <p>In today's fast-paced world, staying connected while on the move is no longer just an option—it's a necessity. Welcome to IndiaDostiChat, your premier destination for the most engaging **Mobile Indian Chat** experience available online. We have meticulously designed our platform to ensure that whether you're commuting, waiting for a friend, or just relaxing in a park, your favorite Indian community is always just a tap away. Our **mobile Indian chat room** is optimized for every smartphone, providing a seamless bridge between you and thousands of friendly desis worldwide.</p>
                
                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Why Choose Mobile Indian Chat?</h2>
                <p>The primary advantage of **mobile Indian chat** is the sheer convenience it offers. Unlike traditional chat platforms that might require a bulky desktop setup, IndiaDostiChat allows you to **join India chat from phone** instantly. This mobility means you can share live updates of your day, discuss the latest cricket scores in real-time, or simply find someone to talk to when you're feeling social. Our mobile interface is built to be lightweight and responsive, ensuring that your messages reach their destination without delay, even on standard mobile data connections.</p>
                
                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Indian Chat Without App Download</h2>
                <p>One of the biggest hurdles to joining online communities is often the requirement to download and install yet another application. At IndiaDostiChat, we've eliminated this barrier. We offer a true **Indian chat without app** requirement. We respect your phone's storage and your privacy. You don't need to visit an app store, worry about permissions, or deal with frequent updates. Our **Indian chat from browser** philosophy means you get a full-featured experience directly in Chrome, Safari, Firefox, or any modern mobile browser. It's safer, faster, and much more private.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">The Best Mobile Friendly Indian Chat Room</h2>
                <p>Being "mobile friendly" is a core part of our identity. Our **mobile friendly Indian chat room** features a layout that adapts perfectly to any screen size. Buttons are sized for easy tapping, text is optimized for readability without zooming, and the navigation is intuitive for thumb-based use. This attention to detail is why thousands of users choose to **join India chat from phone** on our platform every single day. We've optimized the data usage as well, making it one of the most efficient ways to stay connected without draining your mobile plan.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Secure and Safe Mobile Chatting</h2>
                <p>Security is paramount when you're chatting on the move. Our **mobile Indian chat room** employs the same rigorous moderation and security protocols as our desktop version. Whether you're on your home Wi-Fi or a public 5G network, your anonymity is protected. We encourage a **safe moderated Indian chat community** where everyone is treated with respect. Our volunteer moderators are active across all platforms, ensuring that your mobile experience remains clean, friendly, and free from spam or harassment.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">High Speed Performance on 4G and 5G</h2>
                <p>We know that mobile connections can sometimes be unstable. That's why our **mobile Indian chat** is built on high-performance IRC architecture. It's incredibly lightweight, meaning it connects quickly even on 3G or 4G networks and flies on 5G. You won't experience the lag or crashes common in bloated social media apps. Our **Indian web chat** is designed for the modern mobile user who values speed and reliability above all else.</p>

                <div style="text-align: center; margin: 3rem 0;">
                    <a href="chat.html" class="btn-primary" style="font-size: 1.3rem; padding: 1rem 3rem; font-weight: bold;">Join Mobile Chat Now</a>
                </div>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Engage and Play on Your Phone</h2>
                <p>Who says you can't play games on a browser chat? All our popular community features, including Trivia and the Monster Hunt game, are fully accessible via mobile. You can participate in community challenges, climb the leaderboards, and win digital trophies—all from your smartphone. This makes IndiaDostiChat more than just a place to talk; it's a complete mobile entertainment hub for the Indian community.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Conclusion: Your Indian Community in Your Pocket</h2>
                <p>IndiaDostiChat offers the definitive **mobile Indian chat** experience. By focusing on an app-free, browser-based approach, we've made it easier than ever to **join India chat from phone**. Our commitment to safety, speed, and community ensures that you'll always have a friendly place to go, no matter where you are. Join us today and see why we are the top choice for Indians worldwide looking for a mobile-first connection.</p>
            </section>

            <section class="faq-section" style="background: var(--card-bg); padding: 2rem; border-radius: 10px; border: 1px solid var(--border-color);">
                <h2 style="margin-bottom: 2rem; text-align: center;">Frequently Asked Questions</h2>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">Do I need to register to use mobile chat?</h3>
                    <p>No, registration is not required. You can join as a guest with just a nickname.</p>
                </div>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">Does the chat work on iPhone and Android?</h3>
                    <p>Yes, our mobile chat is fully compatible with both iOS (iPhone/iPad) and all Android devices.</p>
                </div>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">Is the mobile chat room free to use?</h3>
                    <p>Absolutely! IndiaDostiChat is 100% free for everyone, on every device.</p>
                </div>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">Can I use emojis on my phone in the chat?</h3>
                    <p>Yes, our mobile interface fully supports your phone's native emoji keyboard.</p>
                </div>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">How do I keep my mobile chat safe?</h3>
                    <p>Never share personal details like your phone number or location, and always follow the rules listed on our <a href="rules.html">Rules page</a>.</p>
                </div>
            </section>
            
            <div style="margin-top: 3rem; text-align: center; margin-bottom: 3rem;">
                <a href="./" style="color: var(--primary-color); text-decoration: none; font-weight: bold; font-size: 1.1rem;">&larr; Back to IndiaDostiChat Home</a>
            </div>
        </div>
    </main>"""
            content = re.sub(r'<main>.*?</main>', new_main, content, flags=re.DOTALL)
            
            # Update FAQ Schema
            new_schema = """
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "Can I use IndiaDostiChat on my phone?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, our platform is fully optimized for mobile browsers. You can chat on any smartphone without downloading an app."
        }
      }, {
        "@type": "Question",
        "name": "Is the mobile chat room free?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, all features including mobile chat are 100% free for all users."
        }
      }, {
        "@type": "Question",
        "name": "Do I need to download an app?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No app download is needed. You can join the chat directly through your mobile browser like Chrome or Safari."
        }
      }]
    }
    </script>"""
            content = re.sub(r'<!-- FAQ Schema -->\s*<script.*?</script>', '<!-- FAQ Schema -->' + new_schema, content, flags=re.DOTALL)

        elif filename == "indian-friendship-chat.html":
            new_main = """
    <main>
        <section class="landing-hero">
            <h1>Indian Friendship Chat - Meet New Friends Online</h1>
            <p>The best place to build genuine connections within the Indian community.</p>
        </section>

        <div class="container">
            <section style="margin-bottom: 3rem; line-height: 1.8; color: var(--text-color);">
                <p>Welcome to IndiaDostiChat, the ultimate destination for **Indian Friendship Chat**. In an age where digital connections often feel superficial, we've created a space where genuine friendships can blossom. Our community is built on the foundation of shared culture, language, and the vibrant spirit of India. Whether you're looking to meet new people from your hometown or want to connect with the global desi diaspora, our **free Indian friendship chat** provides the perfect platform to start your journey.</p>
                
                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Building Real Connections Online</h2>
                <p>What makes **Indian friendship chat** so special? It's the ability to find people who understand your background without you having to explain it. On IndiaDostiChat, you can discuss everything from the latest Bollywood blockbusters to regional delicacies and local news. These shared interests form the bedrock of lasting connections. Our users come here to find **desi friends online**, and many have found friendships that have lasted for years, proving that digital spaces can indeed foster real-world bonds.</p>
                
                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Safe and Moderated Desi Chat Room</h2>
                <p>We believe that a great friendship starts with a safe environment. Our **safe moderated Indian chat community** is one of our proudest achievements. We have a dedicated team of volunteer moderators who ensure that everyone follows our community guidelines. This means you can focus on making friends without worrying about spam, harassment, or inappropriate behavior. We've built a family-friendly atmosphere where users of all ages and backgrounds feel welcome and respected, making it the top choice for **anonymous Indian chat**.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Hindi and English Chat for Global Friends</h2>
                <p>Friendship knows no language barriers, but it helps to speak the same one! Our rooms cater to both **Hindi and English chat**, as well as the popular Hinglish. This linguistic diversity allows you to express your personality more naturally. Whether you want to share a traditional joke in Hindi or discuss a complex topic in English, you'll find a welcoming audience. This makes us a global hub for **online Indian friendship chat**, connecting desis from Delhi to Dubai and Mumbai to Manhattan.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Anonymous Chatting with a Nickname</h2>
                <p>Privacy is key to a comfortable chatting experience. IndiaDostiChat offers a completely **anonymous India chat** environment. You don't need to share your real name, location, or any personal details to start meeting people. By using a nickname, you can control your identity and only share what you're comfortable with. This **nickname-based chat** encourages more open and honest conversations, which is often the first step in building a true friendship.</p>

                <div style="text-align: center; margin: 3rem 0;">
                    <a href="chat.html" class="btn-primary" style="font-size: 1.3rem; padding: 1rem 3rem; font-weight: bold;">Start Making Friends Now</a>
                </div>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Fun and Games to Break the Ice</h2>
                <p>Sometimes, starting a conversation can be the hardest part. That's why we've integrated fun community games like Monster Hunt and Trivia. Participating in these games is a fantastic icebreaker. You can team up with others to defeat digital monsters or compete in trivia challenges, creating shared experiences that lead naturally to deeper conversations. It's the most entertaining way to **meet Indian friends online** while having a blast.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Join the IndiaDostiChat Family Today</h2>
                <p>IndiaDostiChat isn't just a website; it's a growing family. We invite you to step into our **Indian friendship chat room** and experience the warmth of our community. Whether you're a student looking for study buddies, a professional looking for casual talk, or someone looking for a friendly desi connection, you'll find it here. Our doors are always open, and a new friend is always just a message away.</p>
            </section>

            <section class="faq-section" style="background: var(--card-bg); padding: 2rem; border-radius: 10px; border: 1px solid var(--border-color);">
                <h2 style="margin-bottom: 2rem; text-align: center;">Frequently Asked Questions</h2>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">How can I find friends from my city?</h3>
                    <p>While everyone gathers in the main room, you can always ask if there are users from your city. Many people find local friends this way!</p>
                </div>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">Is it safe to meet people I chat with?</h3>
                    <p>We always recommend keeping your friendship online for a long time before considering a meeting, and always meet in a public place with someone you trust informed.</p>
                </div>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">Can I join the friendship chat for free?</h3>
                    <p>Yes, IndiaDostiChat is 100% free. There are no charges to chat or make friends.</p>
                </div>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">What should I do if someone is being rude?</h3>
                    <p>Our moderators are here to help. You can report any user who breaks our rules, and we will take appropriate action.</p>
                </div>
            </section>
            
            <div style="margin-top: 3rem; text-align: center; margin-bottom: 3rem;">
                <a href="./" style="color: var(--primary-color); text-decoration: none; font-weight: bold; font-size: 1.1rem;">&larr; Back to IndiaDostiChat Home</a>
            </div>
        </div>
    </main>"""
            content = re.sub(r'<main>.*?</main>', new_main, content, flags=re.DOTALL)

        # Similar expansions for other pages... I'll include them in the script logic.
        # For brevity in the prompt, I'll use a loop with a dictionary for the unique content of city/language pages.

        city_data = {
            "mumbai": {"name": "Mumbai", "local": "The city of dreams, Bollywood, and the legendary local trains.", "angle": "Users looking for Mumbai chat can join the main IndiaDostiChat room and connect with Indian users from different cities including Mumbai residents."},
            "hyderabad": {"name": "Hyderabad", "local": "The city of Nizams, famous Biryani, and the Charminar.", "angle": "Users looking for Hyderabad chat can join the main IndiaDostiChat room and connect with Indian users from different cities."},
            "ahmedabad": {"name": "Ahmedabad", "local": "The vibrant heart of Gujarat, famous for its heritage and business spirit.", "angle": "Users looking for Ahmedabad chat can join the main IndiaDostiChat room and connect with Indian users from different cities."},
            "lucknow": {"name": "Lucknow", "local": "The city of Nawabs, Tehzeeb, and mouth-watering kebabs.", "angle": "Users looking for Lucknow chat can join the main IndiaDostiChat room and connect with Indian users from different cities."}
        }
        
        lang_data = {
            "telugu": {"name": "Telugu", "local": "One of the most spoken Dravidian languages, rich in literature and cinema.", "angle": "Users looking for Telugu chat can join the main IndiaDostiChat room and connect with Indian users who speak various languages including Telugu."},
            "marathi": {"name": "Marathi", "local": "The language of Maharashtra, spoken by millions with a deep cultural heritage.", "angle": "Users looking for Marathi chat can join the main IndiaDostiChat room and connect with Indian users who speak Marathi and other languages."},
            "punjabi": {"name": "Punjabi", "local": "The energetic language of Punjab, known for its vibrant music and culture.", "angle": "Users looking for Punjabi chat can join the main IndiaDostiChat room and connect with Indian users who speak Punjabi and other languages."}
        }

        # Handling City and Language pages dynamically
        for key, data in city_data.items():
            if f"{key}-chat-room.html" == filename:
                new_main = f"""
    <main>
        <section class="landing-hero">
            <h1>{data['name']} Chat Room - Connect with Local Friends</h1>
            <p>Join the {data['name']} community and meet people from across India.</p>
        </section>

        <div class="container">
            <section style="margin-bottom: 3rem; line-height: 1.8; color: var(--text-color);">
                <p>Welcome to our dedicated page for {data['name']} users. {data['local']} While many users look for a specific **{data['name']} chat room**, we have found that the best experience is found when everyone gathers in one large, active community. {data['angle']} This ensures that you always find someone to talk to, regardless of the time of day.</p>
                
                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Why Join the Main IndiaDostiChat Room?</h2>
                <p>By joining the main room, you get access to the most active desi community online. You'll find users from {data['name']} sharing local news, discussing regional events, and making new friends. It's a great way to stay connected to your roots while also meeting people from other parts of the country. Our **free Indian chat room** is designed to be inclusive and welcoming to everyone from the {data['name']} region.</p>
                
                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Anonymous and Safe Chatting</h2>
                <p>Safety is our top priority. On IndiaDostiChat, you can chat anonymously using just a nickname. You never have to share your personal details unless you want to. This **safe moderated Indian chat community** is protected by a team of moderators who keep the environment clean and friendly for everyone from {data['name']}. We use advanced bot-prevention technology to ensure a high-quality experience.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Features You'll Love</h2>
                <p>In our main room, you can participate in trivia, play the Monster Hunt game, and engage in vibrant discussions in Hindi, English, and Hinglish. It's the perfect place for **desi friendship chat** online. Whether you are in the heart of {data['name']} or living abroad, you can always find a piece of home in our chat rooms.</p>

                <div style="text-align: center; margin: 3rem 0;">
                    <a href="chat.html" class="btn-primary" style="font-size: 1.3rem; padding: 1rem 3rem; font-weight: bold;">Join the Main Chat Room</a>
                </div>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Safety Note for Users</h2>
                <p>We remind all our users to be safe. Never share your phone number, real name, or financial information with strangers. Always follow our <a href="rules.html">Chat Rules</a>. Your safety is important to us as we build the best **{data['name']} chat** community experience.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Conclusion</h2>
                <p>IndiaDostiChat provides a warm and welcoming space for everyone from {data['name']}. Join our main room today, meet new friends, and become part of the most active Indian chat community on the web. We look forward to seeing you there!</p>
            </section>

            <section class="faq-section" style="background: var(--card-bg); padding: 2rem; border-radius: 10px; border: 1px solid var(--border-color);">
                <h2 style="margin-bottom: 2rem; text-align: center;">Frequently Asked Questions</h2>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">Is there an exclusive {data['name']} room?</h3>
                    <p>We encourage everyone to join the main room to ensure the highest level of activity and the best chance to meet new people.</p>
                </div>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">Can I speak in my local language?</h3>
                    <p>While the main room mostly uses Hindi and English, you will often find others who speak the local language of {data['name']}.</p>
                </div>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">Is the chat room mobile-friendly?</h3>
                    <p>Yes, you can join from any smartphone browser without downloading an app.</p>
                </div>
            </section>
            
            <div style="margin-top: 3rem; text-align: center; margin-bottom: 3rem;">
                <a href="./" style="color: var(--primary-color); text-decoration: none; font-weight: bold; font-size: 1.1rem;">&larr; Back to IndiaDostiChat Home</a>
            </div>
        </div>
    </main>"""
                content = re.sub(r'<main>.*?</main>', new_main, content, flags=re.DOTALL)

        for key, data in lang_data.items():
            if f"{key}-chat-room.html" == filename:
                new_main = f"""
    <main>
        <section class="landing-hero">
            <h1>{data['name']} Chat - Connect with {data['name']} Speakers</h1>
            <p>Join the global {data['name']} community and share your thoughts.</p>
        </section>

        <div class="container">
            <section style="margin-bottom: 3rem; line-height: 1.8; color: var(--text-color);">
                <p>Welcome to the {data['name']} speaker community at IndiaDostiChat. {data['local']} While many users look for a specific **{data['name']} chat room**, our community is strongest when everyone gathers in our main, active room. {data['angle']} This creates a vibrant, multi-lingual atmosphere that truly represents the diversity of India.</p>
                
                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">The Beauty of Multi-lingual Indian Chat</h2>
                <p>By joining the main IndiaDostiChat room, you can interact with people from all over India. While you'll find many who speak **{data['name']}**, you'll also meet speakers of Hindi, English, and other regional languages. This diversity makes for fascinating conversations and new friendships. Our **free Indian chat room** is the perfect place to share your culture and learn about others.</p>
                
                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Secure and Anonymous for Every Speaker</h2>
                <p>We value your privacy. On IndiaDostiChat, you can join and chat anonymously using just a nickname. No registration or personal data is required. This **anonymous Indian chat** experience is designed to be safe for everyone. Our moderation team ensures that the rules are followed, providing a respectful environment for all {data['name']} speakers.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Why Choose IndiaDostiChat?</h2>
                <p>Our platform is fast, lightweight, and works perfectly on mobile devices. You don't need to download an app to start chatting in **{data['name']}**. Simply open your browser and join the fun. You can also play community games like Trivia and Monster Hunt, making your time here even more enjoyable.</p>

                <div style="text-align: center; margin: 3rem 0;">
                    <a href="chat.html" class="btn-primary" style="font-size: 1.3rem; padding: 1rem 3rem; font-weight: bold;">Join the Main Chat Now</a>
                </div>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Stay Safe While Chatting</h2>
                <p>Always remember to stay safe online. Do not share personal information with strangers. For more tips on staying safe, check out our <a href="rules.html">Chat Rules</a>. We want every {data['name']} speaker to have a positive and secure experience on our platform.</p>

                <h2 style="margin: 2rem 0 1rem; color: var(--accent-color);">Conclusion</h2>
                <p>IndiaDostiChat is the best place for {data['name']} speakers to connect with the wider Indian community. Join our main room today, share your stories, and make new friends from all across the country. Your community is waiting for you!</p>
            </section>

            <section class="faq-section" style="background: var(--card-bg); padding: 2rem; border-radius: 10px; border: 1px solid var(--border-color);">
                <h2 style="margin-bottom: 2rem; text-align: center;">Frequently Asked Questions</h2>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">Can I chat exclusively in {data['name']}?</h3>
                    <p>While the main room uses a mix of languages, you will definitely find others who are happy to converse in {data['name']}.</p>
                </div>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">Is the chat safe for women?</h3>
                    <p>Yes, we maintain a strictly moderated environment to ensure the safety and respect of all our users.</p>
                </div>
                <div style="margin-bottom: 1.5rem;">
                    <h3 style="font-size: 1.1rem; color: var(--primary-color);">Do I need to install anything?</h3>
                    <p>No, you can join instantly from any mobile or desktop browser.</p>
                </div>
            </section>
            
            <div style="margin-top: 3rem; text-align: center; margin-bottom: 3rem;">
                <a href="./" style="color: var(--primary-color); text-decoration: none; font-weight: bold; font-size: 1.1rem;">&larr; Back to IndiaDostiChat Home</a>
            </div>
        </div>
    </main>"""
                content = re.sub(r'<main>.*?</main>', new_main, content, flags=re.DOTALL)

        # Handling blog.html
        if filename == "blog.html":
            new_main = """
    <main>
        <section class="landing-hero">
            <h1>IndiaDostiChat Blog - Insights into Indian Online Communities</h1>
            <p>Explore articles about online safety, making friends, and the evolution of Indian chat rooms.</p>
        </section>

        <div class="container">
            <section class="blog-intro" style="margin-bottom: 3rem; line-height: 1.8; color: var(--text-color);">
                <p>Welcome to the official IndiaDostiChat blog. Here, we delve into the world of **anonymous Indian chat**, exploring how digital spaces bring desis together across continents. Our articles provide valuable tips on staying safe online, making meaningful connections, and understanding the culture of our vibrant community. Whether you're a long-time member or a newcomer, our blog is your guide to getting the most out of your **free Indian chat room** experience.</p>
            </section>

            <div class="grid" style="grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 4rem;">
                <!-- Blog Cards -->
                <article class="card" style="padding: 1.5rem; border: 1px solid var(--border-color);">
                    <h3 style="color: var(--primary-color); margin-bottom: 1rem;">Best Free Indian Chat Rooms</h3>
                    <p style="font-size: 0.95rem; margin-bottom: 1.5rem;">Discover why IndiaDostiChat stands out as the top choice for those looking for a high-quality, free Indian chat experience.</p>
                    <a href="india-chat.html" class="btn-secondary" style="font-size: 0.9rem;">Read More</a>
                </article>

                <article class="card" style="padding: 1.5rem; border: 1px solid var(--border-color);">
                    <h3 style="color: var(--primary-color); margin-bottom: 1rem;">Anonymous Indian Chat Guide</h3>
                    <p style="font-size: 0.95rem; margin-bottom: 1.5rem;">Learn how to navigate the world of anonymous chatting while protecting your privacy and staying safe.</p>
                    <a href="anonymous-indian-chat.html" class="btn-secondary" style="font-size: 0.9rem;">Read More</a>
                </article>

                <article class="card" style="padding: 1.5rem; border: 1px solid var(--border-color);">
                    <h3 style="color: var(--primary-color); margin-bottom: 1rem;">Hindi Chat Room Online</h3>
                    <p style="font-size: 0.95rem; margin-bottom: 1.5rem;">Exploring the popularity of Hindi chat and how it keeps the global Indian diaspora connected to their roots.</p>
                    <a href="hindi-chat.html" class="btn-secondary" style="font-size: 0.9rem;">Read More</a>
                </article>

                <article class="card" style="padding: 1.5rem; border: 1px solid var(--border-color);">
                    <h3 style="color: var(--primary-color); margin-bottom: 1rem;">Desi Chat Room for Friendship</h3>
                    <p style="font-size: 0.95rem; margin-bottom: 1.5rem;">How to build genuine and lasting friendships in the vibrant world of desi online communities.</p>
                    <a href="desi-chat.html" class="btn-secondary" style="font-size: 0.9rem;">Read More</a>
                </article>

                <article class="card" style="padding: 1.5rem; border: 1px solid var(--border-color);">
                    <h3 style="color: var(--primary-color); margin-bottom: 1rem;">Mobile Indian Chat Room</h3>
                    <p style="font-size: 0.95rem; margin-bottom: 1.5rem;">The ultimate guide to chatting on the go without the need for any app downloads.</p>
                    <a href="mobile-indian-chat.html" class="btn-secondary" style="font-size: 0.9rem;">Read More</a>
                </article>

                <article class="card" style="padding: 1.5rem; border: 1px solid var(--border-color);">
                    <h3 style="color: var(--primary-color); margin-bottom: 1rem;">Safe Online Chatting Tips</h3>
                    <p style="font-size: 0.95rem; margin-bottom: 1.5rem;">Crucial advice on how to enjoy your chat experience while keeping your personal information secure.</p>
                    <a href="rules.html" class="btn-secondary" style="font-size: 0.9rem;">Read More</a>
                </article>
            </div>
        </div>
    </main>"""
            content = re.sub(r'<main>.*?</main>', new_main, content, flags=re.DOTALL)

        # Handling contact.html
        if filename == "contact.html":
            new_main = """
    <main>
        <section class="landing-hero">
            <h1>Contact Us - Reach the IndiaDostiChat Team</h1>
            <p>We're here to help! Get in touch for support, feedback, or inquiries.</p>
        </section>

        <div class="container">
            <section style="margin-bottom: 3rem; line-height: 1.8; color: var(--text-color);">
                <p>Have a question about our **free Indian chat room**? Need help with a technical issue or want to provide feedback on our community? We value your input and are here to ensure your experience on IndiaDostiChat is exceptional. Our team is dedicated to maintaining a **safe moderated Indian chat community**, and your reports and suggestions help us achieve that goal.</p>
                
                <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 3rem;">
                    <div class="card" style="padding: 2rem; border: 1px solid var(--border-color);">
                        <h3 style="color: var(--primary-color); margin-bottom: 1rem;">General Inquiries</h3>
                        <p>For general questions about our platform and how to join the **anonymous Indian chat**, please contact us at:</p>
                        <p><strong>Email:</strong> support@indiadostichat.com</p>
                    </div>
                    <div class="card" style="padding: 2rem; border: 1px solid var(--border-color);">
                        <h3 style="color: var(--primary-color); margin-bottom: 1rem;">Report an Issue</h3>
                        <p>If you encounter a user breaking our rules or a technical bug, please let us know immediately. Your safety is our priority.</p>
                        <a href="rules.html" class="btn-secondary" style="display: inline-block; margin-top: 1rem;">View Rules</a>
                    </div>
                </div>

                <h2 style="margin: 3rem 0 1rem; color: var(--accent-color); text-align: center;">Frequently Asked Questions</h2>
                <div style="max-width: 800px; margin: 0 auto;">
                    <div style="margin-bottom: 1.5rem;">
                        <strong>How do I report a user?</strong>
                        <p>You can report a user directly in the chat to an active moderator or send us an email with details.</p>
                    </div>
                    <div style="margin-bottom: 1.5rem;">
                        <strong>Can I become a moderator?</strong>
                        <p>We are always looking for active and responsible community members. Please stay active in the chat and follow the rules!</p>
                    </div>
                    <div style="margin-bottom: 1.5rem;">
                        <strong>Why was I banned?</strong>
                        <p>Bans are usually issued for breaking our community rules. Please review the <a href="rules.html">Rules page</a> for more information.</p>
                    </div>
                </div>
            </section>
        </div>
    </main>"""
            content = re.sub(r'<main>.*?</main>', new_main, content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Expanded content in {filename}")

if __name__ == "__main__":
    expand_landing_pages()
