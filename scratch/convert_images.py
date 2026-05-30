import os
import glob
from PIL import Image

brain_dir = r"C:\Users\mks1j\.gemini\antigravity-ide\brain\ca83ed8a-2764-4e2f-b264-e7c442cbd2e0"
dest_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\assets\images\home-hero"

os.makedirs(dest_dir, exist_ok=True)

image_mappings = {
    "mumbai_gateway": "mumbai-gateway.webp",
    "delhi_india_gate": "delhi-india-gate.webp",
    "hyderabad_charminar": "hyderabad-charminar.webp",
    "jaipur_hawa_mahal": "jaipur-hawa-mahal.webp",
    "kerala_backwaters": "kerala-backwaters.webp",
    "kashmir_mountains": "kashmir-mountains.webp",
    "varanasi_ghats": "varanasi-ghats.webp",
    "goa_beach": "goa-beach.webp",
    "india_festival_lights": "india-festival-lights.webp"
}

for pattern, target_name in image_mappings.items():
    search_path = os.path.join(brain_dir, f"{pattern}_*.png")
    matched_files = glob.glob(search_path)
    if not matched_files:
        print(f"WARNING: No file found for pattern: {pattern}")
        continue
        
    # Get the latest matched file (or first)
    src_file = matched_files[0]
    dest_file = os.path.join(dest_dir, target_name)
    
    print(f"Processing {src_file} -> {dest_file}...")
    try:
        with Image.open(src_file) as img:
            # Resize image to width 1920 if it's larger, preserving aspect ratio
            width, height = img.size
            if width > 1920:
                new_height = int((1920 / width) * height)
                img = img.resize((1920, new_height), Image.Resampling.LANCZOS)
                print(f"  Resized from {width}x{height} to 1920x{new_height}")
            
            # Save as WebP with compression
            img.save(dest_file, "WEBP", quality=80)
            print(f"  Saved successfully! Size: {os.path.getsize(dest_file)} bytes")
    except Exception as e:
        print(f"  ERROR processing {pattern}: {e}")

print("Image conversion completed!")
