import os
from PIL import Image

logo_png = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo\assets\logo\logo.png"
logo_dir = os.path.dirname(logo_png)

sizes = {
    "logo-30.webp": (30, 30),
    "logo-40.webp": (40, 40),
    "logo-80.webp": (80, 80)
}

print("Generating logo variants...")
try:
    with Image.open(logo_png) as img:
        for name, size in sizes.items():
            dest_path = os.path.join(logo_dir, name)
            img_resized = img.resize(size, Image.Resampling.LANCZOS)
            img_resized.save(dest_path, "WEBP", quality=80)
            print(f"  Saved {name} ({size[0]}x{size[1]}). Size: {os.path.getsize(dest_path)} bytes")
except Exception as e:
    print(f"Error: {e}")

print("Logo generation complete!")
