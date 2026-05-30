import os

base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"

city_keywords = {
    "mumbai-chat-room": ["Bollywood", "Marine Drive", "local trains", "street food"],
    "delhi-chat-room": ["India Gate", "Red Fort", "Qutub Minar", "universities", "food"],
    "bangalore-chat-room": ["IT", "startups", "students", "gardens", "cafes"],
    "hyderabad-chat-room": ["Charminar", "biryani", "tech", "culture"],
    "lucknow-chat-room": ["tehzeeb", "Nawabi", "Hindi", "Urdu", "food"],
    "kolkata-chat-room": ["Howrah Bridge", "trams", "Durga Puja", "literature"],
    "chennai-chat-room": ["Marina Beach", "Tamil", "cinema", "temples"],
    "pune-chat-room": ["students", "IT", "history", "culture"],
    "ahmedabad-chat-room": ["heritage", "Sabarmati", "Gujarati"],
    "jaipur-chat-room": ["Pink City", "forts", "tourism", "Rajasthani"]
}

for folder, keywords in city_keywords.items():
    path = os.path.join(base_dir, folder, "index.html")
    if not os.path.exists(path):
        print(f"ERROR: {folder} does not exist!")
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    missing = []
    for kw in keywords:
        if kw.lower() not in html.lower():
            missing.append(kw)
            
    if missing:
        print(f"{folder:25} | MISSING keywords: {missing}")
    else:
        print(f"{folder:25} | All local references verified!")
