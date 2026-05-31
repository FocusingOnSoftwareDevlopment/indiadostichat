import os
from PIL import Image

screenshot_path = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\assets\images\screenshots\indiadostichat-room-preview.webp"

if not os.path.exists(screenshot_path):
    print("ERROR: Screenshot not found")
    exit(1)

old_size = os.path.getsize(screenshot_path)
print(f"Original size: {old_size / 1024:.2f} KB")

try:
    with Image.open(screenshot_path) as img:
        width, height = img.size
        print(f"Screenshot dimensions: {width}x{height}")
        
        # Save WebP with slightly lower quality to target ~60 KB
        quality = 70
        img.save(screenshot_path, "WEBP", quality=quality)
        new_size = os.path.getsize(screenshot_path)
        print(f"Compressed size at quality={quality}: {new_size / 1024:.2f} KB")
        
        while new_size > 70 * 1024 and quality > 40:
            quality -= 5
            img.save(screenshot_path, "WEBP", quality=quality)
            new_size = os.path.getsize(screenshot_path)
            print(f"Compressed size at quality={quality}: {new_size / 1024:.2f} KB")
            
except Exception as e:
    print(f"Error: {e}")

print("Screenshot optimization complete!")
