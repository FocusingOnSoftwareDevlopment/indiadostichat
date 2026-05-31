import os
import json

base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
topics_dir = os.path.join(base_dir, "topics")
os.makedirs(topics_dir, exist_ok=True)

# 10 Topics configurations with -chat slugs and highly specific chat keywords
topics_config = [
    {
        "slug": "money-chat",
        "title": "Money Chat - Personal Finance & Budgeting Chat Room",
        "h1": "Money Chat & Personal Finance Chat Room",
        "meta_desc": "Join our free money chat room to chat about personal finance, budgeting tips, stock investments, savings, and financial planning with peers.",
        "image": "money-chat.webp",
        "image_alt": "Personal finance chat, wealth building and saving money chat graphic",
        "intro_p": "Welcome to the Money Chat room, the ultimate destination on IndiaDostiChat for open, honest, and anonymous chats about personal finance, wealth building, and smart money management. Money is one of the most important aspects of our daily lives, yet it remains a taboo subject in many Indian households and social circles. Whether you want to join a budgeting chat, chat about mutual funds and stock market investing, ask about side hustles, or exchange ideas in our financial independence chat, our community provides a supportive space. Chatting about money anonymously allows you to share real experiences, questions, and insights without the fear of judgment or social comparison.",
        "p1": "In today's fast-paced economy, managing your money is about more than just earning a salary; it's about making your money work for you. Many young adults are navigating the complex world of personal finance for the first time—from understanding tax structures and retirement planning to choosing between renting and buying a home. The Money Chat room connects you with peers who are on the same journey. Here, you can chat about the pros and cons of different investment avenues, compare financial apps, and exchange advice on avoiding common debt traps. It is a collaborative environment where beginners can learn from more experienced community members.",
        "p2": "We believe that financial literacy should be accessible to everyone. By engaging in peer-to-peer chats, you can demystify complex terms like compound interest, emergency funds, asset allocation, and liquid assets. Share your favorite books, podcasts, and calculators that helped you understand money better. Remember, while the community is full of passionate individuals sharing their experiences, all chats are for educational and entertainment purposes. It's a place to brainstorm ideas, seek motivation for your savings goals, and build the discipline needed for a secure financial future.",
        "ideas": [
            "How to start investing in mutual funds with a small monthly budget",
            "What are the best budgeting apps for students and young professionals in India",
            "How to manage money and build saving habits in your early 20s",
            "Is renting better than buying a house in major Indian cities like Mumbai and Bangalore",
            "Passive income streams that actually work for beginners without large capital",
            "How to calculate and build a solid emergency fund from scratch",
            "Simple and creative ways to reduce daily expenses without feeling restricted",
            "Discussing cryptocurrency and stock market trends: tips and warning signs",
            "How to handle difficult financial conversations and set boundaries with family",
            "Strategies for paying off student or personal loans faster and smarter"
        ],
        "faqs": [
            {
                "q": "Is registration required to chat about finance on IndiaDostiChat?",
                "a": "No, you do not need to register or share any personal information. Simply choose a nickname and join the chat room instantly."
            },
            {
                "q": "Can I get professional financial advice in the Money Chat?",
                "a": "No. The chats in the room are for peer-to-peer sharing, education, and brainstorming. You should always consult a certified financial advisor before making major investment decisions."
            },
            {
                "q": "Are there rules against promoting financial schemes or courses?",
                "a": "Yes. IndiaDostiChat has a strict zero-tolerance policy against spam, promotional links, selling financial courses, or advertising multi-level marketing (MLM) schemes. Violators are banned immediately."
            },
            {
                "q": "How can I protect my privacy while chatting about money?",
                "a": "Because our platform is nickname-based and anonymous, you should never share your real name, bank details, contact information, or precise location in public rooms."
            }
        ]
    },
    {
        "slug": "korea-chat",
        "title": "Korea Chat - Korean Culture, Language & K-Drama Chat Room",
        "h1": "Korea Chat & K-Drama Chat Room",
        "meta_desc": "Connect with fellow Korean culture fans in our Korea chat room. Chat about K-Dramas, learn Korean, chat about K-beauty, and travel experiences.",
        "image": "korea-chat.webp",
        "image_alt": "Korea chat room illustration depicting traditional hanok architecture and mountains",
        "intro_p": "Welcome to the Korea Chat room, the dedicated space on IndiaDostiChat for everyone fascinated by the rich heritage, language, and modern culture of South Korea. The Hallyu wave has swept across the globe, creating a massive community of fans who love everything from classic K-Dramas and language learning to traditional cuisine. Whether you are studying Korean and looking for a language exchange chat, planning a trip to Seoul, or eager to chat about the latest television drama releases, this chat room is your virtual gateway. Connect with fellow enthusiasts, share recommendations, and celebrate your shared passion in a friendly, interactive setting.",
        "p1": "Korea is a land of beautiful contrasts, where ancient palaces stand next to futuristic skyscrapers, and quiet mountains overlook bustling city streets. In Korea Chat, we dive deep into these various facets. Members regularly share their travel itineraries, chat about the best budget stays in Busan, and trade tips on how to apply for a tourist visa. It's a great place to learn about Korean social etiquette, historical customs, and regional celebrations like Chuseok. By sharing stories and travel tips, you can prepare for an authentic trip that goes beyond the standard tourist tracks.",
        "p2": "For language learners, Korea Chat offers an invaluable resource. Learning Hangul and mastering honorifics can be challenging, but practicing with peers makes it engaging and fun. Share your favorite textbooks, vocabulary apps, and learning strategies. You can also discuss how watching K-Dramas has helped you understand colloquial expressions and cultural nuances. Beyond language, we chat about Korean culinary delights—from making authentic Kimchi and Tteokbokki at home to finding the best Korean restaurants and grocery stores in major Indian cities. Join the community today and start sharing your love for Korea!",
        "ideas": [
            "What are the best free resources and apps for learning the Korean language online",
            "Must-visit places in Seoul, Busan, and Jeju Island for first-time travelers",
            "Our favorite classic K-Dramas and ongoing series that you need to watch",
            "How to cook authentic Kimchi jjigae and ramen hacks at home",
            "Korean skincare (K-beauty) routines: what products actually work for your skin type",
            "Understanding the differences between traditional Hanok villages and modern districts",
            "How to apply for a South Korea tourist visa from India: step-by-step tips",
            "Discussing Korean history, traditional holidays, and social etiquette guidelines",
            "Finding authentic Korean restaurants and grocery shops in major metro areas",
            "Sharing budget-friendly travel tips, accommodation hacks, and transport guides for Korea"
        ],
        "faqs": [
            {
                "q": "Do I need to speak fluent Korean to join the chat?",
                "a": "Not at all! Most users chat in English, Hindi, or Hinglish. We have many beginners who are just starting to learn the alphabet (Hangul)."
            },
            {
                "q": "Can I find travel buddies for my trip to South Korea?",
                "a": "Yes! Korea Chat is a great place to meet other travelers who are planning trips, allowing you to share itineraries and travel tips."
            },
            {
                "q": "Are we allowed to chat about K-pop in this room?",
                "a": "Yes, cultural chats of all kinds are welcome, though we also have a dedicated K-pop chat room for music-specific chats."
            },
            {
                "q": "Is the chat room free and anonymous?",
                "a": "Yes, IndiaDostiChat is 100% free and registration-free. You only need a nickname to join the chat."
            }
        ]
    },
    {
        "slug": "japan-chat",
        "title": "Japan Chat - Japan Travel, Culture & Language Chat Room",
        "h1": "Japan Chat & Japanese Culture Chat Room",
        "meta_desc": "Chat about Japan travel, culture, heritage, and learn Japanese online. Join our free Japan chat room to connect with fans.",
        "image": "japan-chat.webp",
        "image_alt": "Japan chat room graphics showing Mount Fuji, cherry blossoms, and red sun",
        "intro_p": "Welcome to Japan Chat on IndiaDostiChat, a vibrant community space for chatting about the culture, language, travel destinations, and traditional heritage of Japan. From the serene temples of Kyoto and the majestic silhouette of Mount Fuji to the neon-lit streets of Tokyo and Osaka, Japan captures the imagination of travelers and culture lovers worldwide. Whether you are preparing for the JLPT exams, planning a backpacking trip through the Japanese countryside, or want to chat about traditional arts like tea ceremonies and origami, you will find welcoming peers here. Join us to share your experiences and learn more about the Land of the Rising Sun.",
        "p1": "India and Japan share deep historical and cultural bonds, and today, that mutual interest is stronger than ever. In our Japan Chat room, members chat about everything from travel logistics—like using the Japan Rail Pass and navigating the Tokyo subway—to seasonal travel highlights. Share your tips on the best spots to view the cherry blossoms (Sakura) in spring or the vibrant red maples in autumn. You can also get recommendations for budget-friendly accommodations like capsule hotels and traditional ryokans, helping you plan a memorable trip on a realistic budget.",
        "p2": "Language study is another major focus in Japan Chat. Learning Kanji, Hiragana, and Katakana requires dedication, and having a group of study partners makes the process much easier. Chat about study guides, online dictionaries, and effective methods for vocabulary memorization. We also chat about Japanese cuisine, which is celebrated globally for its focus on freshness and presentation. Share your favorite recipes for sushi, tempura, gyoza, and regional ramen variations, or discuss where to find authentic Japanese ingredients. Discover the concept of Ikigai and how Japanese philosophies shape daily life.",
        "ideas": [
            "Practical tips for planning a budget-friendly trip to Japan as an independent traveler",
            "Understanding the JLPT (Japanese Language Proficiency Test) structure and study strategies",
            "Traditional Japanese arts: tea ceremonies, flower arrangement (Ikebana), and rock gardens",
            "Must-try street foods in Osaka, Tokyo, and Hiroshima",
            "Exploring the scenic beauty of Mount Fuji, Hakone, and surrounding hot springs (Onsen)",
            "What is the philosophy of Ikigai and how does it apply to daily life and happiness",
            "How to get around Japan using the Shinkansen (bullet trains) and regional rail passes",
            "Cultural differences: essential customs and etiquette to know before visiting Japan",
            "The best time of the year and top locations for viewing cherry blossoms in Japan",
            "Comparing historical temples in Kyoto with the modern skyscrapers of Shinjuku, Tokyo"
        ],
        "faqs": [
            {
                "q": "Is the Japan Chat room conducted in Japanese?",
                "a": "No, most members communicate in English, Hindi, or Hinglish. Japanese learners are welcome to practice their writing, but translation is usually provided."
            },
            {
                "q": "Can I chat about anime and manga in this room?",
                "a": "Yes! Anime and manga are major parts of Japanese culture. You can chat about them here, or head over to our dedicated Anime Chat room."
            },
            {
                "q": "How can I join the chat room anonymously?",
                "a": "Simply visit the IndiaDostiChat chat page, enter a nickname of your choice, and you will be connected instantly without registration."
            },
            {
                "q": "Are there moderators to keep the chat clean?",
                "a": "Yes, volunteer moderators ensure all conversations are respectful, family-friendly, and free from spam."
            }
        ]
    },
    {
        "slug": "anime-chat",
        "title": "Anime Chat - Free Anime & Manga Chat Room | IndiaDostiChat",
        "h1": "Anime Chat & Manga Chat Room",
        "meta_desc": "Join our free anime chat room to chat about your favorite anime series, manga recommendations, movie reviews, and fan art with fellow fans.",
        "image": "anime-chat.webp",
        "image_alt": "Anime chat room illustration with a school classroom window overlooking a summer sky",
        "intro_p": "Welcome to Anime Chat, the premier chat space on IndiaDostiChat for anime fans, manga readers, and digital artists. Anime has evolved from a niche hobby into a global cultural phenomenon, connecting millions of fans through breathtaking animation, deep storytelling, and memorable characters. Whether you are a fan of classic shonen adventures, emotional slice-of-life dramas, thrilling psychological mysteries, or the beautiful films of Studio Ghibli, our anime chat room is the perfect place to chat about your thoughts. Join a friendly community of fans to chat about recent episodes, recommend manga, and share your creative digital art.",
        "p1": "What makes anime so special is its ability to cover a vast range of genres and themes, often pushing the boundaries of what animation can achieve. In our Anime Chat room, we celebrate this diversity. Members share their custom watchlists, debate the adaptation choices of manga-to-anime series, and review theatrical releases. You can find recommendations based on your favorite themes, whether you are looking for an action-packed series to binge-watch or a heartwarming slice-of-life story for a quiet evening. It is a welcoming space for both veteran otaku and beginners starting their anime journey.",
        "p2": "Beyond watching and reading, this room is a hub for creativity. Many members are passionate digital artists, cosplayers, and musicians who draw inspiration from anime aesthetics. Chat about drawing techniques, software recommendations for digital art, and how to create original characters. You can also chat about the incredible soundtracks, composers, and opening theme songs that bring these stories to life. Our community maintains a positive and respectful atmosphere, ensuring that fans of all series can chat about their interests without gatekeeping or negativity.",
        "ideas": [
            "Underrated anime series that deserve more attention and where to watch them",
            "Our favorite Studio Ghibli movies and their visual artistry and storytelling themes",
            "Comparing manga to their anime adaptations: which format delivers the better experience",
            "Chatting about classic shonen series vs. modern psychological and thriller anime",
            "The best slice-of-life and cozy anime series for a relaxing weekend watch",
            "Reviewing recent theatrical anime movie releases and discussing their animation quality",
            "Top recommendations and advice for beginners starting their anime journey",
            "Discussing anime soundtracks, orchestral scores, and famous opening themes",
            "How the anime art style influences modern digital illustration and global animation",
            "Speculations, fan theories, and release date predictions for upcoming anime seasons"
        ],
        "faqs": [
            {
                "q": "Do you stream anime episodes in the chat?",
                "a": "No. IndiaDostiChat is a text-based community platform. We do not host, stream, or distribute any copyrighted anime or manga files."
            },
            {
                "q": "Can I share my own anime fan art?",
                "a": "Yes! You can discuss your artwork, describe your drawing process, and share tips about digital illustration with fellow creators."
            },
            {
                "q": "Is the anime chat room free to join?",
                "a": "Yes, it is 100% free and does not require registration. Just pick a nickname and start chatting."
            },
            {
                "q": "Are chats kept family-friendly?",
                "a": "Yes. Our volunteer moderators enforce our rules to ensure the chat environment is respectful, welcoming, and safe for all users."
            }
        ]
    },
    {
        "slug": "kpop-chat",
        "title": "K-Pop Chat - Connect with K-Pop Fans Online | IndiaDostiChat",
        "h1": "K-Pop Chat & Music Fan Chat Room",
        "meta_desc": "Join our free K-pop chat room. Chat about K-pop music, album comebacks, choreography, concert vibes, and fan theories with other stans.",
        "image": "kpop-chat.webp",
        "image_alt": "K-pop chat room illustration of a concert stage with neon lights and silhouettes",
        "intro_p": "Welcome to K-Pop Chat, the dedicated meeting point on IndiaDostiChat for K-Pop fans to connect, share music, and talk about the global music phenomenon. Korean pop music has taken the world by storm, known for its high-energy choreographies, high-production music videos, and unique fashion styles. Whether you want to chat about the latest comeback, analyze music video concepts, share your favorite b-side tracks, or chat about the excitement of live concerts in our K-pop fan chat, this chat room is for you. Join fellow fans in a positive, welcoming environment where music brings everyone together.",
        "p1": "What sets K-Pop apart is the deep connection between artists and their global communities of fans. From custom lightsticks and fan chants to synchronized choreography and concept storylines, K-Pop offers a unique entertainment experience. In our chat room, members share their experiences of attending concerts, unboxing albums, and learning dance routines. It is a great place to stay updated on upcoming tours, award shows, and new music releases. By sharing your favorite tracks, you can discover new groups and solo artists across various subgenres like pop, hip-hop, and R&B.",
        "p2": "We believe in celebrating music and creativity. Many members enjoy practicing dance covers, editing video montages, and chatting about the visual design and fashion trends seen in music videos. Share your favorite choreographies, tips for learning dance steps at home, and reviews of live performances. Our K-Pop Chat room focuses on maintaining a friendly, positive atmosphere, free from toxicity and fan wars, so that everyone can express their appreciation for music in a supportive space.",
        "ideas": [
            "What makes K-pop choreography so unique, energetic, and engaging for fans",
            "How K-pop music videos push the boundaries of visual effects and conceptual storytelling",
            "Our favorite recent album releases and hidden b-sides you need to listen to",
            "Discussing the evolution of K-pop generations, from the pioneers to modern groups",
            "The cultural impact of K-pop on global fashion, makeup trends, and streetwear",
            "Sharing practical tips for learning K-pop dance covers at home as a beginner",
            "Concert experiences: the energy of lightsticks, fan chants, and live vocals",
            "How K-pop integrates different musical styles like EDM, hip-hop, and house music",
            "The role of complex storylines and fictional universes in K-pop album concepts",
            "How to support your favorite musical artists, stream albums, and join fan activities"
        ],
        "faqs": [
            {
                "q": "Can I chat about any K-pop group or solo artist?",
                "a": "Yes! All artists, groups, and soloists from all music generations are welcome to be chatted about in a respectful manner."
            },
            {
                "q": "Do I need to sign up to join the K-pop chat?",
                "a": "No registration is needed. You can join the conversation using just a nickname, keeping your experience fast and private."
            },
            {
                "q": "Are fan wars or arguments allowed in the chat?",
                "a": "No. We have a strict policy against toxicity, harassment, and disrespectful arguments. Our moderators ensure a positive environment for all fans."
            },
            {
                "q": "Is the chat room mobile-friendly?",
                "a": "Yes, the chat client is optimized for all mobile browsers, allowing you to discuss music on the go without installing an app."
            }
        ]
    },
    {
        "slug": "travel-chat",
        "title": "Travel Chat - Backpacking Tips, Travel Guides & Chat Room",
        "h1": "Travel Chat & Backpackers Chat Room",
        "meta_desc": "Chat about travel guides, backpacking experiences, solo travel, and budget itineraries in our free travel chat room.",
        "image": "travel-chat.webp",
        "image_alt": "Travel chat room vector illustration of travel suitcase and globe",
        "intro_p": "Welcome to Travel Chat, the central hub on IndiaDostiChat for backpackers, solo travelers, and adventure seekers to chat about stories, travel tips, and itineraries. Traveling is one of the most rewarding ways to experience the world, learn about different cultures, and meet new people. Whether you are planning a trek in the Himalayas, a beach getaway in Goa, or a budget-friendly trip abroad, this travel chat room connects you with fellow explorers. Share your travel hacks, ask for destination recommendations, and get real, unfiltered advice from experienced travelers who have been there.",
        "p1": "One of the biggest hurdles in planning a trip is finding reliable, practical information. In Travel Chat, you can ask direct questions about transport schedules, budget accommodations, and local safety guidelines. Chat about the pros and cons of staying in backpacker hostels versus local homestays, and share your favorite packing hacks to keep your luggage light. Sharing firsthand experiences helps other community members avoid common travel scams, locate hidden gems off the beaten path, and budget their trips more effectively.",
        "p2": "For solo travelers, especially those planning their first solo trip, the community offers support and encouragement. Chat about safety precautions, useful travel apps, and how to meet friendly locals and fellow travelers on the road. We also celebrate the culinary aspect of travel—chatting about where to find the best street food, authentic regional cuisines, and traditional markets. Join Travel Chat to inspire your next adventure, refine your travel plans, and connect with people who share your passion for exploring the world.",
        "ideas": [
            "Backpacking across India: budget-friendly routes, hostel guides, and local transport options",
            "Essential safety tips and packing advice for solo travelers, especially women",
            "How to pack light: minimalist packing list for a multi-week trip in different climates",
            "Offbeat and hidden travel destinations in India that are not crowded by tourists",
            "How to plan and budget for an international trip on a tight savings plan",
            "Finding authentic local food, street eats, and traditional markets while traveling",
            "The pros and cons of staying in backpacker hostels vs. guesthouses and homestays",
            "How to travel sustainably, reduce waste, and respect local cultures and environments",
            "Tips for long-term travel, digital nomad life, and working remotely on the road",
            "Dealing with travel challenges: what to do in case of lost items, delays, or language barriers"
        ],
        "faqs": [
            {
                "q": "Can I share my travel blog or vlog in the chat?",
                "a": "While you can share helpful tips and describe your travel experiences, spamming promotional links or advertising travel agencies is not allowed."
            },
            {
                "q": "Is the Travel Chat room helpful for international travel?",
                "a": "Yes! Many members travel internationally and share advice on visas, currency exchange, and itineraries for destinations around the world."
            },
            {
                "q": "How do I enter the chat room?",
                "a": "Simply visit the IndiaDostiChat chat page, enter a nickname, and click join. It is completely free and registration-free."
            },
            {
                "q": "Can I find travel partners in this chat room?",
                "a": "Yes! You can connect with other users who are planning similar trips and coordinate plans in a safe, peer-to-peer environment."
            }
        ]
    },
    {
        "slug": "food-chat",
        "title": "Food Chat - Cooking Recipes, Street Food & Foodie Chat Room",
        "h1": "Food Chat & Cooking Recipes Chat Room",
        "meta_desc": "Join our free food chat room to chat about cooking, recipes, regional street foods, baking, and global cuisines with fellow foodies.",
        "image": "food-chat.webp",
        "image_alt": "Food chat room illustration of steaming ramen bowl",
        "intro_p": "Welcome to Food Chat, the delicious corner of IndiaDostiChat where foodies, home cooks, and culinary enthusiasts gather to chat about recipes, street food, baking, and global cuisines in a dedicated food chat room. Food is a universal language that brings people together, reflecting history, culture, and personal memories. Whether you are looking for quick weeknight recipe ideas, baking tips for beginners, recommendations for the best street food in Delhi or Mumbai, or eager to chat about global culinary trends, our foodie chat is open. Connect with others, share your cooking successes, and discover new flavors.",
        "p1": "India is famous for its rich and diverse culinary landscape, with each state offering unique spices, traditional cooking methods, and regional specialties. In Food Chat, we celebrate this variety. Members chat about and swap recipes for classic comfort foods like biryani, butter chicken, dosa, and street snacks like golgappe. You can learn about traditional spice blends, chat about the secrets to achieving the perfect texture in curries, and share cooking hacks that save time in the kitchen. It is an interactive space where you can ask for cooking advice and get instant help.",
        "p2": "Beyond traditional Indian cooking, our chats explore international cuisines, baking techniques, and healthy lifestyle choices. Share your recipes for homemade pasta, fresh salads, breads, and desserts. You can also chat about dietary preferences like vegetarian, vegan, and gluten-free cooking, trading tips on simple ingredient swaps. Whether you are a beginner learning how to cook your first meal or an experienced cook sharing advanced techniques, Food Chat is a friendly space to share your culinary journey.",
        "ideas": [
            "Secret ingredients and cooking techniques that elevate home-cooked Indian meals",
            "The great biryani debate: comparing Hyderabadi, Lucknowi, and Kolkata styles",
            "Quick, nutritious, and easy breakfast recipes for busy students and professionals",
            "Baking tips for beginners: common baking mistakes to avoid and how to fix them",
            "Recreating restaurant-style global cuisines like Italian, Chinese, and Mexican at home",
            "Exploring regional street food specialties and hidden food joints across Indian cities",
            "Simple and delicious vegetarian swaps for popular meat-based recipes",
            "How to master traditional spice blends and masalas from scratch at home",
            "Discussing tea (chai) and coffee cultures, brewing methods, and custom recipes",
            "Meal prepping guides to save time, eat healthier, and reduce food waste during the week"
        ],
        "faqs": [
            {
                "q": "Do I need to be an expert cook to join the chat?",
                "a": "Not at all! Beginners are very welcome to ask simple questions, gather basic recipes, and learn kitchen tips from other members."
            },
            {
                "q": "Can I share photos of the food I cook?",
                "a": "While the main chat is text-based, you can describe your cooking processes, share ingredient lists, and talk about presentation."
            },
            {
                "q": "Is the Food Chat room free to access?",
                "a": "Yes, IndiaDostiChat is 100% free. No registration or signup is required; you only need a nickname to start chatting."
            },
            {
                "q": "Are commercial ads or restaurant promotions allowed?",
                "a": "No. To keep our community discussions genuine, advertising restaurants, catering services, or commercial cooking courses is not permitted."
            }
        ]
    },
    {
        "slug": "gaming-chat",
        "title": "Gaming Chat - Video Games, Esports & Console Chat Room",
        "h1": "Gaming Chat & Video Games Chat Room",
        "meta_desc": "Join our free gaming chat room to chat about PC/console games, mobile gaming, competitive esports, and retro video games with other gamers.",
        "image": "gaming-chat.webp",
        "image_alt": "Gaming chat room illustration showing game controller with neon glows",
        "intro_p": "Welcome to Gaming Chat on IndiaDostiChat, the ultimate gathering place for video game players, esports fans, and console gamers. Gaming has become one of the most popular forms of entertainment and community building in the world. Whether you play competitive multiplayer shooters, immersive single-player role-playing games (RPGs), mobile games on your phone, or retro classics from older consoles, our gamer chat room is for you. Connect with fellow players, share gaming news, coordinate multiplayer matches, and chat about your favorite gaming moments.",
        "p1": "The gaming landscape is constantly evolving, with new game releases, hardware updates, and competitive esports tournaments happening regularly. In our Gaming Chat room, members stay updated on the latest industry trends. Chat about the performance of new graphics cards, share reviews of recently launched titles, and chat about PC versus console gaming setups. For mobile gamers, it is a great space to find teammates, chat about strategies, and chat about popular titles that are highly active in India. Sharing tips and hardware recommendations helps everyone optimize their gaming experience.",
        "p2": "In addition to modern titles, our community has a strong appreciation for indie games and retro classics. Share your recommendations for hidden gems created by independent developers, or chat about the nostalgic games of your childhood. Plus, IndiaDostiChat features built-in text-based games like Monster Hunt and Trivia that you can play directly in our main chat rooms, combining chatting and gaming in one place. Join Gaming Chat today to share your passion, meet new gaming friends, and play along with the community.",
        "ideas": [
            "Discussing PC vs. console vs. mobile gaming preferences and hardware performance",
            "The rapid growth of competitive esports tournaments and teams in India",
            "Our favorite single-player games with immersive storytelling and memorable characters",
            "Practical tips for building a budget-friendly gaming PC in today's market",
            "Retro gaming classics: older console games that still hold up and are worth playing today",
            "How to balance gaming hobbies with work, study routines, and daily life",
            "Discussing the latest game releases, patches, DLCs, and gaming industry news",
            "Underrated indie games with unique mechanics that everyone should try",
            "How game development, art styles, and narrative design have evolved over the decades",
            "Playing text-based IRC games like Monster Hunt and Trivia directly on IndiaDostiChat"
        ],
        "faqs": [
            {
                "q": "Can I promote my streaming channel or gaming videos?",
                "a": "No. To protect the quality of the chat, we do not allow self-promotion, advertising streams, or sharing referral links."
            },
            {
                "q": "How can I play the built-in games like Monster Hunt?",
                "a": "You can play directly inside our chat rooms by interacting with the community bots. Ask other members in the chat for tips on commands and rules."
            },
            {
                "q": "Is the Gaming Chat room free to join?",
                "a": "Yes, IndiaDostiChat is completely free and requires no registration. Simply pick a nickname and join the chat."
            },
            {
                "q": "Can I find players to form co-op teams?",
                "a": "Yes! Many members use the chat to coordinate co-op games and find reliable teammates for multiplayer matches."
            }
        ]
    },
    {
        "slug": "ai-chat",
        "title": "AI Chat Room - Artificial Intelligence, Tech & Future Chat Room",
        "h1": "AI Chat & Future Tech Chat Room",
        "meta_desc": "Join our AI chat room to chat about artificial intelligence, machine learning advances, tech trends, automation, and coding scripts with enthusiasts.",
        "image": "ai-chat.webp",
        "image_alt": "AI chat room graphic representing neural network connections",
        "intro_p": "Welcome to AI Chat on IndiaDostiChat, a forward-looking space where technology enthusiasts, developers, and curious minds gather to chat about artificial intelligence, machine learning, and future tech trends in our free tech chat room. AI is transforming how we work, create, communicate, and solve global challenges. Whether you are a software engineer working with neural networks, a student interested in prompt engineering, or someone curious about how automation will shape future careers, this room is open. Connect with others to share news, discuss ethical questions, and explore the cutting edge of tech.",
        "p1": "The pace of technological innovation can feel overwhelming, with new models, tools, and research papers being released almost daily. In AI Chat, we break down these developments in a clear and accessible way. Members chat about the practical uses of generative AI tools in creative work, software development, and daily productivity. Share your favorite programming resources, chat about the difference between machine learning algorithms, and talk about how AI is being integrated into fields like medicine, finance, and education.",
        "p2": "Beyond the technical details, this room is a place for chatting about the broader social impact of technology. We engage in chats about the ethics of artificial intelligence, intellectual property rights, data privacy, and the future of work. How do we ensure technology benefits everyone? What are the limits of machine intelligence, and when will we see true Artificial General Intelligence (AGI)? AI Chat provides a space to debate these interesting concepts with fellow technology enthusiasts. Join us today to share your insights and stay informed.",
        "ideas": [
            "How generative AI is changing creative industries, digital art, and writing",
            "The ethical implications of artificial intelligence and automated decision-making systems",
            "How to learn machine learning, python coding, and data science as a beginner",
            "Practical ways to use AI tools to boost productivity and efficiency in daily work",
            "The future of automation and its long-term impact on the job market and career paths",
            "Discussing neural networks, deep learning models, and how they process information",
            "Futuristic tech trends: what major innovations can we expect to see in the next decade",
            "How AI is being applied in healthcare, diagnostic medicine, and drug discovery",
            "The advantages and limitations of AI coding assistants for software developers",
            "Debating sci-fi concepts: path to Artificial General Intelligence (AGI) and superintelligence"
        ],
        "faqs": [
            {
                "q": "Do I need to be a software developer to join AI Chat?",
                "a": "No, you don't. The room is open to anyone interested in technology, from absolute beginners to expert researchers."
            },
            {
                "q": "Are there automated AI bots answering questions in the chat?",
                "a": "No. IndiaDostiChat is a community of real humans. You will be chatting with other people who share an interest in technology."
            },
            {
                "q": "Is the chat room free to access?",
                "a": "Yes, our platform is 100% free and does not require registration. Just enter a nickname and start chatting."
            },
            {
                "q": "Can I ask for coding help in the chat?",
                "a": "Yes! Tech-minded members often exchange coding advice, chat about algorithms, and share helpful development resources."
            }
        ]
    },
    {
        "slug": "international-friendship-chat",
        "title": "International Friendship Chat - Global Cultural Exchange Chat Room",
        "h1": "International Friendship Chat Room",
        "meta_desc": "Connect with friends worldwide. Join our free international friendship chat room for cultural exchanges and global penpals.",
        "image": "international-friendship-chat.webp",
        "image_alt": "International friendship chat room graphic with diverse group holding hands around the globe",
        "intro_p": "Welcome to the International Friendship Chat room on IndiaDostiChat, a global space designed for cross-cultural communication, language practice, and building friendships across borders in our free global chat. Traveling is one of the most rewarding ways to experience the world, learn about different cultures, and meet new people. Whether you want to practice a new language, share traditional stories, learn about holidays celebrated in other countries, or simply chat with friendly people worldwide, this friendship chat room is your international hub. Connect with a global community and celebrate our shared humanity.",
        "p1": "Every culture has its own unique customs, festivals, culinary habits, and daily routines. In our International Friendship Chat room, members enjoy chatting about these cultural details. Share stories about your local festivals, discuss traditional music and instruments, and describe your favorite regional dishes. It is a virtual cultural exchange where you can discover both the interesting differences and the surprising similarities that connect people from different parts of the world. Sharing these stories helps build mutual respect and global understanding.",
        "p2": "For language learners, the chat room offers a friendly environment to chat and practice speaking with native speakers. Share language learning tips, chat about translation nuances, and help others learn your native language. Since IndiaDostiChat is nickname-based and anonymous, it provides a safe, low-pressure space to converse and build confidence. We are committed to keeping our international community positive and inclusive. Join the room, say hello, and start building meaningful friendships with people from all over the world.",
        "ideas": [
            "Sharing interesting cultural traditions, regional celebrations, and local festivals",
            "Practical tips for learning and practicing new languages with native speakers in chat",
            "How having international friendships changes our perspectives and broadens our minds",
            "Discussing global cinema, indie music, and traditional arts that cross borders",
            "How school, university life, and daily routines differ across different countries",
            "Sharing traditional stories, regional folklore, and historical legends from home",
            "How to stay in touch and maintain long-distance friendships across different time zones",
            "Discussing culinary habits, traditional breakfast routines, and daily food differences",
            "What cultural detail surprised you most when chatting with someone from another country",
            "Building global empathy, cultural understanding, and unity through open communication"
        ],
        "faqs": [
            {
                "q": "Is the chat room open to people from outside India?",
                "a": "Yes! IndiaDostiChat welcomes users from every country and cultural background. We celebrate global diversity and cross-cultural friendships."
            },
            {
                "q": "What languages are spoken in the International Friendship Chat room?",
                "a": "Most conversations are in English, but members are welcome to practice and share phrases in any language they are learning."
            },
            {
                "q": "How does nickname-based chat help protect my privacy?",
                "a": "Since no registration or personal details are required, you can chat with international peers safely without sharing social media handles or phone numbers."
            },
            {
                "q": "Are there rules against discriminatory behavior?",
                "a": "Yes. We have a strict zero-tolerance policy against hate speech, racism, xenophobia, discrimination, and harassment of any kind. Moderators ban violators immediately."
            }
        ]
    }
]

# Theme versions
css_version = "25"
js_version = "20"

# SVG Icons code
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

# Helper to generate FAQ Schema JSON-LD
def generate_faq_schema(faqs):
    entities = []
    for faq in faqs:
        entities.append({
            "@type": "Question",
            "name": faq["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq["a"]
            }
        })
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    }, indent=2)

# Helper to generate Breadcrumb Schema JSON-LD
def generate_breadcrumb_schema(topic_slug, topic_title):
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
                "name": "Trending Chat Topics",
                "item": "https://www.indiadostichat.com/topics/"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": topic_title,
                "item": f"https://www.indiadostichat.com/topics/{topic_slug}/"
            }
        ]
    }, indent=2)

# Generate individual pages
for config in topics_config:
    slug = config["slug"]
    title = config["title"]
    h1 = config["h1"]
    meta_desc = config["meta_desc"]
    image = config["image"]
    image_alt = config["image_alt"]
    intro_p = config["intro_p"]
    p1 = config["p1"]
    p2 = config["p2"]
    ideas = config["ideas"]
    faqs = config["faqs"]
    
    # Calculate related links: 4 other topics
    related_links = []
    count = 0
    for other in topics_config:
        if other["slug"] != slug and count < 5:
            related_links.append(other)
            count += 1
            
    related_html_list = ""
    for r in related_links:
        related_html_list += f'<li><a href="../{r["slug"]}/" style="color: var(--primary-color); text-decoration: none; font-weight: 500;">{r["h1"]}</a></li>\n'
    
    # Breadcrumb schema
    bc_schema = generate_breadcrumb_schema(slug, h1)
    # FAQ schema
    faq_schema = generate_faq_schema(faqs)
    
    # Render ideas list
    ideas_html = ""
    for idea in ideas:
        ideas_html += f'<li style="margin-bottom: 0.8rem; padding-left: 0.5rem; border-left: 3px solid var(--primary-color);">{idea}</li>\n'
        
    # Render FAQs list
    faqs_html = ""
    for faq in faqs:
        faqs_html += f"""<div style="margin-bottom: 2rem; border-left: 4px solid var(--accent-color); padding-left: 1.5rem;">
            <h3 style="color: var(--primary-color); margin-top: 0; margin-bottom: 0.5rem; font-size: 1.25rem;">{faq["q"]}</h3>
            <p style="margin: 0; line-height: 1.6;">{faq["a"]}</p>
        </div>"""

    # HTML Template for topic subpage
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | IndiaDostiChat</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="https://www.indiadostichat.com/topics/{slug}/">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{title} | IndiaDostiChat">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="https://www.indiadostichat.com/topics/{slug}/">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://www.indiadostichat.com/assets/images/topics/{image}">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title} | IndiaDostiChat">
    <meta name="twitter:description" content="{meta_desc}">
    <meta name="twitter:image" content="https://www.indiadostichat.com/assets/images/topics/{image}">

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
            padding: 3rem 1rem;
            text-align: center;
            background: linear-gradient(135deg, var(--hero-bg-gradient-start, #0f172a), var(--hero-bg-gradient-end, #1e293b));
            color: #fff;
            margin-bottom: 2rem;
        }}
        .landing-hero h1 {{
            font-size: 2.5rem;
            margin-bottom: 1rem;
            font-weight: 700;
        }}
    </style>

    <!-- Schema JSON-LD -->
    <script type="application/ld+json">
    {bc_schema}
    </script>
    <script type="application/ld+json">
    {faq_schema}
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
            <p style="font-size: 1.15rem; max-width: 800px; margin: 0 auto; line-height: 1.6; opacity: 0.95;">
                Explore real conversations, build friendships, and connect with peers around the world on IndiaDostiChat.
            </p>
            <p style="font-size: 0.95rem; margin-top: 1rem; opacity: 0.8; font-weight: 500;">
                {calendar_svg} Updated for 2026
            </p>
        </section>

        <div class="container" style="max-width: 900px; margin: 0 auto; padding: 0 1rem 3rem;">
            <!-- Hero Topic Banner Image -->
            <img class="hero-banner" src="../../assets/images/topics/{image}" alt="{image_alt}" width="800" height="800" decoding="async">

            <!-- Intro Section -->
            <section style="margin-bottom: 3rem; line-height: 1.8; color: var(--text-color); font-size: 1.08rem;">
                <p style="margin-bottom: 1.5rem;">{intro_p}</p>
                <p style="margin-bottom: 1.5rem;">{p1}</p>
                <p style="margin-bottom: 1.5rem;">{p2}</p>

                <!-- Fast Join CTA Button -->
                <div style="text-align: center; margin: 3.5rem 0;">
                    <a href="../../chat/" class="btn-primary" style="font-size: 1.35rem; padding: 1.2rem 2.8rem; background-color: #28a745; border-color: #28a745; box-shadow: 0 4px 15px rgba(40,167,69,0.3); text-decoration: none; border-radius: 25px; display: inline-block; color: white; font-weight: bold; transition: transform 0.2s ease;">
                        Join Live Chat Room
                    </a>
                    <p style="font-size: 0.9rem; margin-top: 0.8rem; opacity: 0.7;">No registration required &bull; 100% Free &bull; Join in 5 seconds</p>
                </div>
            </section>

            <!-- Conversation Ideas Section -->
            <section style="margin-bottom: 3.5rem; background: var(--card-bg); padding: 2.2rem; border-radius: var(--border-radius); border: 1px solid var(--border-color); box-shadow: 0 5px 15px rgba(0,0,0,0.02);">
                <h2 style="color: var(--accent-color); margin-top: 0; margin-bottom: 1.5rem; font-size: 1.8rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem;">
                    Trending Conversation Starters
                </h2>
                <p style="margin-bottom: 1.5rem; line-height: 1.6;">
                    Here are some popular topics and questions active community members are discussing right now. Jump into the room and share your perspective:
                </p>
                <ul style="list-style: none; padding: 0; margin: 0; line-height: 1.8; font-size: 1.05rem;">
                    {ideas_html}
                </ul>
            </section>

            <!-- Why IndiaDostiChat Section -->
            <section style="margin-bottom: 3.5rem; line-height: 1.8; color: var(--text-color);">
                <h2 style="color: var(--accent-color); margin-bottom: 1.2rem; font-size: 1.8rem;">Why Join IndiaDostiChat?</h2>
                <p>
                    Unlike social networking applications that require phone number verifications, email profiles, or linking social media accounts, IndiaDostiChat is focused on raw community connection and privacy. You can chat anonymously by just selecting a nickname. We host people globally, enabling cultural and tech discussions in a secure environment. Our volunteer moderators work around the clock to prevent spam, scams, and bot activity, ensuring a clean and respectful environment.
                </p>
                <p>
                    Our web client is lightweight and optimized for both desktop and mobile web browsers. This means you do not need to install memory-heavy apps, nor worry about background trackers. Simply access our site, select a nickname, and you're in.
                </p>
            </section>

            <!-- Safety Note Section -->
            <section style="margin-bottom: 3.5rem; background-color: rgba(231,76,60,0.06); border-left: 4px solid #e74c3c; padding: 1.8rem; border-radius: var(--border-radius);">
                <h3 style="color: #e74c3c; margin-top: 0; margin-bottom: 0.8rem; font-size: 1.35rem;">Community Safety Guidelines</h3>
                <p style="margin: 0; line-height: 1.6; font-size: 0.98rem;">
                    While IndiaDostiChat supports nickname-based and anonymous conversations, safety remains our top priority. We strongly advise all users to never share personal contact numbers, residential locations, bank details, or passwords with anyone in public or private chat rooms. Report spam, aggressive behavior, or inappropriate content to our active moderators immediately.
                </p>
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

            <!-- Related Topics Section -->
            <section style="margin-top: 4rem; border-top: 1px solid var(--border-color); padding-top: 2rem;">
                <h3 style="color: var(--accent-color); margin-bottom: 1.2rem; font-size: 1.4rem;">Explore More Trending Chat Rooms</h3>
                <ul style="list-style: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.2rem; margin: 0;">
                    {related_html_list}
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
    
    # Create topic directory
    topic_path = os.path.join(topics_dir, slug)
    os.makedirs(topic_path, exist_ok=True)
    
    file_path = os.path.join(topic_path, "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated subpage: {file_path}")

# Now generate `/topics/index.html` (Index Page)
# Render grid of topic cards
cards_html = ""
for config in topics_config:
    slug = config["slug"]
    h1 = config["h1"]
    meta_desc = config["meta_desc"]
    image_thumb = f"{os.path.splitext(config['image'])[0]}-thumb.webp"
    
    cards_html += f"""
    <div class="card" style="border: 1px solid var(--border-color); border-radius: var(--border-radius); background: var(--card-bg); overflow: hidden; display: flex; flex-direction: column; transition: transform 0.2s ease, box-shadow 0.2s ease; box-shadow: 0 4px 10px rgba(0,0,0,0.02);">
        <img src="../assets/images/topics/{image_thumb}" alt="{config["image_alt"]}" width="300" height="300" style="width: 100%; height: 200px; object-fit: cover;" decoding="async" loading="lazy">
        <div style="padding: 1.5rem; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <h3 style="margin-top: 0; margin-bottom: 0.8rem; color: var(--accent-color); font-size: 1.35rem;">{h1}</h3>
                <p style="font-size: 0.95rem; line-height: 1.6; color: var(--text-color); margin-bottom: 1.5rem; opacity: 0.9;">{meta_desc}</p>
            </div>
            <a href="{slug}/" style="align-self: flex-start; padding: 0.6rem 1.5rem; background: var(--primary-color); color: #fff; text-decoration: none; border-radius: 20px; font-weight: bold; font-size: 0.9rem; transition: background 0.2s;">
                Join Chat Room
            </a>
        </div>
    </div>
    """

# Breadcrumb schema for index page
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
            "name": "Trending Chat Topics",
            "item": "https://www.indiadostichat.com/topics/"
        }
    ]
}, indent=2)

index_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trending Chat Topics & Chat Rooms | IndiaDostiChat</title>
    <meta name="description" content="Discover popular chat rooms and trending chat topics on IndiaDostiChat including personal finance chat, anime chat, gaming chat, travel chat, and food chat.">
    <link rel="canonical" href="https://www.indiadostichat.com/topics/">
    
    <!-- Open Graph -->
    <meta property="og:title" content="Trending Chat Topics & Chat Rooms | IndiaDostiChat">
    <meta property="og:description" content="Discover popular chat rooms and trending chat topics on IndiaDostiChat including personal finance chat, anime chat, gaming chat, travel chat, and food chat.">
    <meta property="og:url" content="https://www.indiadostichat.com/topics/">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://www.indiadostichat.com/assets/logo/logo.svg">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Trending Chat Topics & Chat Rooms | IndiaDostiChat">
    <meta name="twitter:description" content="Discover popular chat rooms and trending chat topics on IndiaDostiChat including personal finance chat, anime chat, gaming chat, travel chat, and food chat.">
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
            <h1>Trending Chat Topics & Rooms</h1>
            <p style="font-size: 1.25rem; max-width: 800px; margin: 0 auto; line-height: 1.6; opacity: 0.95;">
                Explore community-driven chat rooms and chat topics. Find peers who share your interests and join the conversation in real time!
            </p>
            <p style="font-size: 0.95rem; margin-top: 1rem; opacity: 0.8; font-weight: 500;">
                {calendar_svg} Updated for 2026
            </p>
        </section>

        <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 1rem 4rem;">
            <p style="line-height: 1.8; font-size: 1.1rem; color: var(--text-color); max-width: 800px; margin: 2rem auto 0; text-align: center;">
                Welcome to the IndiaDostiChat Trending Chat Topics index. Here, you can browse through specialized chat rooms curated for our global community members. Whether you want to join personal finance chats, anime chats, travel chats, gaming chats, or food chats, these pages connect you instantly. Select a chat card below to view starters, guides, and enter the live chat room.
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

index_path = os.path.join(topics_dir, "index.html")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html_content)
print(f"Generated index page: {index_path}")
print("All topic pages generated successfully!")
