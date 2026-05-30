import os
import math
from PIL import Image, ImageDraw

def generate_favicons():
    # Workspace directories
    base_dir = r"c:\Users\mks1j\.gemini\antigravity\scratch\indiadostichat_seo"
    assets_favicon_dir = os.path.join(base_dir, "assets", "images", "favicon")
    os.makedirs(assets_favicon_dir, exist_ok=True)
    
    # 1. Create base 1024x1024 RGBA image with transparent background
    canvas_size = 1024
    img = Image.new("RGBA", (canvas_size, canvas_size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    center_x, center_y = canvas_size // 2, canvas_size // 2
    
    # Color definitions (RGBA)
    saffron = (255, 153, 51, 255)
    green = (19, 136, 8, 255)
    navy = (0, 0, 128, 255)
    white = (255, 255, 255, 255)
    
    # 2. Draw outer tricolor border rings
    # Saffron Ring (radius 490)
    draw.ellipse([center_x - 490, center_y - 490, center_x + 490, center_y + 490], fill=saffron)
    # White Gap 1
    draw.ellipse([center_x - 470, center_y - 470, center_x + 470, center_y + 470], fill=white)
    # Green Ring (radius 450)
    draw.ellipse([center_x - 450, center_y - 450, center_x + 450, center_y + 450], fill=green)
    # White base circle for Chakra
    draw.ellipse([center_x - 430, center_y - 430, center_x + 430, center_y + 430], fill=white)
    
    # 3. Draw navy Ashoka Chakra
    # Outer navy wheel of Chakra (radius 380)
    draw.ellipse([center_x - 380, center_y - 380, center_x + 380, center_y + 380], fill=navy)
    # White circle to create the wheel outline (inner radius 350)
    draw.ellipse([center_x - 350, center_y - 350, center_x + 350, center_y + 350], fill=white)
    
    # 24 Domes (small circles centered at the inner edge radius 350)
    for i in range(24):
        # Dome angle is exactly halfway between spokes (e.g. 7.5 deg offset)
        angle_deg = i * 15 + 7.5
        angle_rad = math.radians(angle_deg)
        dome_r = 12
        dome_cx = center_x + 350 * math.cos(angle_rad)
        dome_cy = center_y + 350 * math.sin(angle_rad)
        draw.ellipse([dome_cx - dome_r, dome_cy - dome_r, dome_cx + dome_r, dome_cy + dome_r], fill=navy)
        
    # 24 Tapered spokes (radiating from hub radius 55 to inner edge radius 350)
    r_hub = 55
    r_outer = 350
    w_base = 18
    w_tip = 8
    
    for i in range(24):
        angle_deg = i * 15
        angle_rad = math.radians(angle_deg)
        
        # Direction and perpendicular unit vectors
        sx = math.cos(angle_rad)
        sy = math.sin(angle_rad)
        dx = -math.sin(angle_rad)
        dy = math.cos(angle_rad)
        
        # 4 polygon points for the tapered spoke
        half_w_base = w_base / 2
        half_w_tip = w_tip / 2
        
        p1 = (center_x + r_hub * sx + half_w_base * dx, center_y + r_hub * sy + half_w_base * dy)
        p2 = (center_x + r_hub * sx - half_w_base * dx, center_y + r_hub * sy - half_w_base * dy)
        p3 = (center_x + r_outer * sx - half_w_tip * dx, center_y + r_outer * sy - half_w_tip * dy)
        p4 = (center_x + r_outer * sx + half_w_tip * dx, center_y + r_outer * sy + half_w_tip * dy)
        
        draw.polygon([p1, p2, p3, p4], fill=navy)
        
    # Center Hub (navy circle of radius 55)
    draw.ellipse([center_x - 55, center_y - 55, center_x + 55, center_y + 55], fill=navy)
    # White axle center circle (radius 16)
    draw.ellipse([center_x - 16, center_y - 16, center_x + 16, center_y + 16], fill=white)
    
    # Save base large image for verification
    base_output_path = os.path.join(assets_favicon_dir, "ashoka-chakra-512.png")
    
    # 4. Generate all downscaled sizes and formats
    print("Resizing and saving favicons...")
    
    # favicon-512x512.png
    f512 = img.resize((512, 512), Image.Resampling.LANCZOS)
    f512.save(os.path.join(base_dir, "favicon-512x512.png"), "PNG")
    f512.save(base_output_path, "PNG")
    
    # favicon-192x192.png
    f192 = img.resize((192, 192), Image.Resampling.LANCZOS)
    f192.save(os.path.join(base_dir, "favicon-192x192.png"), "PNG")
    
    # favicon-96x96.png
    f96 = img.resize((96, 96), Image.Resampling.LANCZOS)
    f96.save(os.path.join(base_dir, "favicon-96x96.png"), "PNG")
    
    # favicon-48x48.png
    f48 = img.resize((48, 48), Image.Resampling.LANCZOS)
    f48.save(os.path.join(base_dir, "favicon-48x48.png"), "PNG")
    
    # apple-touch-icon.png (180x180 with solid white square background)
    apple_canvas = Image.new("RGBA", (180, 180), white)
    f180 = img.resize((180, 180), Image.Resampling.LANCZOS)
    # Paste f180 on top of the solid white square
    apple_canvas.alpha_composite(f180)
    # Convert to RGB (to drop alpha channel since apple-touch-icons should be flat RGB)
    apple_canvas.convert("RGB").save(os.path.join(base_dir, "apple-touch-icon.png"), "PNG")
    
    # favicon.ico (multi-resolution: 16x16, 32x32, 48x48)
    f16 = img.resize((16, 16), Image.Resampling.LANCZOS)
    f32 = img.resize((32, 32), Image.Resampling.LANCZOS)
    
    # Save the multiple resolutions inside standard .ico format
    ico_dest = os.path.join(base_dir, "favicon.ico")
    f48.save(ico_dest, format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    
    print("Favicon generation completed successfully!")
    print(f"Generated: favicon.ico, favicon-48x48.png, favicon-96x96.png, favicon-192x192.png, favicon-512x512.png, apple-touch-icon.png, and assets/images/favicon/ashoka-chakra-512.png")

if __name__ == "__main__":
    generate_favicons()
