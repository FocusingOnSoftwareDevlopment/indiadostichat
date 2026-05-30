import os

base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"

city_replacements = {
    "delhi-chat-room": (
        "Delhi users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. ",
        "Delhi users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. Discuss historic landmarks like the India Gate, Red Fort, and Qutub Minar, share updates about universities, or recommend local street food. "
    ),
    "bangalore-chat-room": (
        "Bangalore users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. ",
        "Bangalore users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. Talk about the local IT hub, startup culture, student life, or the city's beautiful gardens and cafes. "
    ),
    "lucknow-chat-room": (
        "Lucknow users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. ",
        "Lucknow users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. Chat about the Nawabi culture and tehzeeb, speak in Hindi or Urdu, and share recommendations for local food. "
    ),
    "kolkata-chat-room": (
        "Kolkata users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. ",
        "Kolkata users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. Discuss the Howrah Bridge, iconic trams, Durga Puja festivities, and Bengali literature. "
    ),
    "chennai-chat-room": (
        "Chennai users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. ",
        "Chennai users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. Discuss Tamil culture, cinema, Marina Beach, and famous local temples. "
    ),
    "pune-chat-room": (
        "Pune users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. ",
        "Pune users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. Meet students, talk about IT startups, and explore Pune's rich history and culture. "
    ),
    "jaipur-chat-room": (
        "Jaipur users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. ",
        "Jaipur users looking for <a href=\"../india-chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">India chat room</a> options can join the main IndiaDostiChat room to connect with users from different cities. Simply <a href=\"../chat/\" style=\"color: var(--primary-color); font-weight: bold; text-decoration: none;\">Join IndiaDostiChat</a> to get started chatting. Discuss the Pink City, majestic forts, local tourism, and Rajasthani culture. "
    )
}

for folder, (target, replacement) in city_replacements.items():
    path = os.path.join(base_dir, folder, "index.html")
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if target in content:
        content = content.replace(target, replacement, 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated local references for: {folder}")
    else:
        # Check if already has the replacement (in case script was run before)
        if replacement in content:
            print(f"Already updated: {folder}")
        else:
            print(f"ERROR: Could not find target paragraph in {folder}")
