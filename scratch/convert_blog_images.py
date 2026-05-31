import os
import glob
from PIL import Image

brain_dir = r"C:\Users\mks1j\.gemini\antigravity-ide\brain\c2179847-338a-44df-b7ba-7a200520efb5"
dest_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\assets\images\topics"

os.makedirs(dest_dir, exist_ok=True)

image_mappings = {
    "mumbai_chat_room": "mumbai-chat-room",
    "korean_friendship": "indian-korean-friendship",
    "korea_community": "india-korea-cultural-exchange-community",
    "korea_guide": "india-korea-cultural-exchange-complete-guide"
}

for pattern, target_base in image_mappings.items():
    search_path = os.path.join(brain_dir, f"{pattern}_*.png")
    matched_files = glob.glob(search_path)
    if not matched_files:
        print(f"WARNING: No file found for pattern: {pattern}")
        continue
        
    src_file = matched_files[0]
    
    # Save main 800x800 WebP
    dest_main = os.path.join(dest_dir, f"{target_base}.webp")
    # Save thumb 300x300 WebP
    dest_thumb = os.path.join(dest_dir, f"{target_base}-thumb.webp")
    
    print(f"Processing {src_file}...")
    try:
        with Image.open(src_file) as img:
            # Main image: crop/resize to 800x800
            img_main = img.resize((800, 800), Image.Resampling.LANCZOS)
            img_main.save(dest_main, "WEBP", quality=80)
            print(f"  Saved main: {dest_main} ({os.path.getsize(dest_main)} bytes)")
            
            # Thumb image: crop/resize to 300x300
            img_thumb = img.resize((300, 300), Image.Resampling.LANCZOS)
            img_thumb.save(dest_thumb, "WEBP", quality=80)
            print(f"  Saved thumb: {dest_thumb} ({os.path.getsize(dest_thumb)} bytes)")
    except Exception as e:
        print(f"  ERROR processing {pattern}: {e}")

print("Image conversion completed!")
