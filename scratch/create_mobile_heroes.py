import os
from PIL import Image

src_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\assets\images\home-hero"
dest_dir = os.path.join(src_dir, "mobile")
os.makedirs(dest_dir, exist_ok=True)

for filename in os.listdir(src_dir):
    if filename.endswith(".webp") and not filename.endswith("-mobile.webp"):
        src_path = os.path.join(src_dir, filename)
        name_part, ext = os.path.splitext(filename)
        dest_filename = f"{name_part}-mobile.webp"
        dest_path = os.path.join(dest_dir, dest_filename)
        
        print(f"Processing {src_path} -> {dest_path}...")
        try:
            with Image.open(src_path) as img:
                width, height = img.size
                new_width = 800
                new_height = int((new_width / width) * height)
                img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                quality = 75
                img_resized.save(dest_path, "WEBP", quality=quality)
                size_kb = os.path.getsize(dest_path) / 1024
                
                while size_kb > 80.0 and quality > 30:
                    quality -= 5
                    img_resized.save(dest_path, "WEBP", quality=quality)
                    size_kb = os.path.getsize(dest_path) / 1024
                
                if size_kb > 80.0:
                    # If still > 80 KB, reduce width to 700px
                    new_width = 700
                    new_height = int((new_width / width) * height)
                    img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    quality = 60
                    img_resized.save(dest_path, "WEBP", quality=quality)
                    size_kb = os.path.getsize(dest_path) / 1024
                    
                    while size_kb > 80.0 and quality > 30:
                        quality -= 5
                        img_resized.save(dest_path, "WEBP", quality=quality)
                        size_kb = os.path.getsize(dest_path) / 1024
                    
                print(f"  Resized to {new_width}x{new_height}. Quality: {quality}, Size: {size_kb:.2f} KB")
        except Exception as e:
            print(f"  Error: {e}")

print("Mobile images generation completed!")
