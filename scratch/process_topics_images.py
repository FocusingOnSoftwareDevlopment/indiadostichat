import os
import glob
from PIL import Image

brain_dir = r"C:\Users\mks1j\.gemini\antigravity-ide\brain\c2179847-338a-44df-b7ba-7a200520efb5"
dest_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\assets\images\topics"

os.makedirs(dest_dir, exist_ok=True)

image_mappings = {
    "topic_money": "money-chat.webp",
    "topic_korea": "korea-chat.webp",
    "topic_japan": "japan-chat.webp",
    "topic_anime": "anime-chat.webp",
    "topic_kpop": "kpop-chat.webp",
    "topic_travel": "travel-chat.webp",
    "topic_food": "food-chat.webp",
    "topic_gaming": "gaming-chat.webp",
    "topic_ai": "ai-chat.webp",
    "topic_friendship": "international-friendship-chat.webp"
}

print("Starting dynamic image processing for CHAT naming...")

for pattern, target_name in image_mappings.items():
    search_path = os.path.join(brain_dir, f"{pattern}_*.png")
    matched_files = glob.glob(search_path)
    if not matched_files:
        print(f"WARNING: No file found for pattern: {pattern}")
        continue
        
    src_file = matched_files[0]
    dest_main = os.path.join(dest_dir, target_name)
    name_parts = os.path.splitext(target_name)
    dest_thumb = os.path.join(dest_dir, f"{name_parts[0]}-thumb.webp")
    
    print(f"Processing {src_file}:")
    try:
        # 1. Main image: Max 800 width, max 60 KB
        with Image.open(src_file) as img:
            width, height = img.size
            if width > 800:
                new_height = int((800 / width) * height)
                img_resized = img.resize((800, new_height), Image.Resampling.LANCZOS)
            else:
                img_resized = img.copy()
            
            # Dynamically find the best quality that keeps file size < 60 KB
            quality = 80
            while quality >= 20:
                img_resized.save(dest_main, "WEBP", quality=quality)
                size = os.path.getsize(dest_main)
                if size < 60 * 1024:
                    print(f"  Saved main: {dest_main} ({size} bytes) at quality {quality}")
                    break
                quality -= 5
            else:
                print(f"  WARNING: Main image could not be compressed below 60 KB even at quality 20. Final size: {size} bytes")

        # 2. Thumbnail image: Max 300 width, max 25 KB
        with Image.open(src_file) as img:
            width, height = img.size
            if width > 300:
                new_height = int((300 / width) * height)
                img_resized = img.resize((300, new_height), Image.Resampling.LANCZOS)
            else:
                img_resized = img.copy()
                
            # Dynamically find the best quality that keeps file size < 25 KB
            quality = 75
            while quality >= 20:
                img_resized.save(dest_thumb, "WEBP", quality=quality)
                size = os.path.getsize(dest_thumb)
                if size < 25 * 1024:
                    print(f"  Saved thumb: {dest_thumb} ({size} bytes) at quality {quality}")
                    break
                quality -= 5
            else:
                print(f"  WARNING: Thumbnail image could not be compressed below 25 KB even at quality 20. Final size: {size} bytes")

    except Exception as e:
        print(f"  ERROR processing {pattern}: {e}")

print("Dynamic image processing completed!")
