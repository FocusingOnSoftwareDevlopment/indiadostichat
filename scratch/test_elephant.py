import re
import urllib.parse

def make_svg():
    # Symmetrical Elephant path with detailed stout outline, trunk loop, ear, tusk, tail, saddle cloth and body stars
    svg = """<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160' viewBox='0 0 160 160'>
  <defs>
    <!-- Symmetrical Elephant facing Right -->
    <g id='elephant'>
      <!-- Main body and loop trunk -->
      <path d='M 8,28 C 8,14 20,8 38,8 C 42,8 45,11 46,14 C 48,14 53,10 54,3 C 51,-3 46,-1 47,4 C 48,8 44,14 41,16 C 39,17 37,18 36,19 C 35,21 34,25 34,28 L 34,44 L 28,44 L 28,32 C 24,34 18,34 14,32 L 14,44 L 8,44 Z' fill='none' stroke='currentColor' stroke-width='1.2' stroke-linecap='round' stroke-linejoin='round' />
      <!-- Tail -->
      <path d='M 8,26 C 6,30 5,36 5,40' fill='none' stroke='currentColor' stroke-width='1' stroke-linecap='round' />
      <!-- Large traditional ear -->
      <path d='M 28,14 C 23,16 22,24 26,27 C 30,29 33,23 31,16 C 30,14 29,14 28,14 Z' fill='none' stroke='currentColor' stroke-width='1' />
      <!-- Eye -->
      <circle cx='38' cy='13' r='1' fill='currentColor' />
      <!-- Tusk -->
      <path d='M 41,18 L 46,20 L 41,22 Z' fill='currentColor' />
      <!-- Saddle blanket (caparison) -->
      <path d='M 15,14 L 27,14 C 27,24 15,24 15,14 Z' fill='none' stroke='currentColor' stroke-width='1' />
      <!-- Saddle blanket decorations -->
      <circle cx='18' cy='17' r='0.8' fill='currentColor' />
      <circle cx='21' cy='19' r='0.8' fill='currentColor' />
      <circle cx='24' cy='17' r='0.8' fill='currentColor' />
      <circle cx='21' cy='15' r='0.8' fill='currentColor' />
      <!-- Small printed stars on elephant body (representing block print stamp stars) -->
      <!-- Rump stars -->
      <path d='M 11,20 H 13 M 12,19 V 21' stroke='currentColor' stroke-width='0.8' />
      <path d='M 12,25 H 14 M 13,24 V 26' stroke='currentColor' stroke-width='0.8' />
      <!-- Shoulder star -->
      <path d='M 32,22 H 34 M 33,21 V 23' stroke='currentColor' stroke-width='0.8' />
    </g>
  </defs>

  <!-- Top Border Vine -->
  <line x1='0' y1='10' x2='160' y2='10' stroke='currentColor' stroke-width='1' />
  <line x1='0' y1='14' x2='160' y2='14' stroke='currentColor' stroke-width='0.6' stroke-dasharray='2,3' />
  <!-- Small top border flowers/dots (seamless 16 waves) -->
  <path d='M 0,10 Q 5,4 10,10 Q 15,4 20,10 Q 25,4 30,10 Q 35,4 40,10 Q 45,4 50,10 Q 55,4 60,10 Q 65,4 70,10 Q 75,4 80,10 Q 85,4 90,10 Q 95,4 100,10 Q 105,4 110,10 Q 115,4 120,10 Q 125,4 130,10 Q 135,4 140,10 Q 145,4 150,10 Q 155,4 160,10' fill='none' stroke='currentColor' stroke-width='0.8' />

  <!-- Bottom Border Vine -->
  <line x1='0' y1='150' x2='160' y2='150' stroke='currentColor' stroke-width='1' />
  <line x1='0' y1='146' x2='160' y2='146' stroke='currentColor' stroke-width='0.6' stroke-dasharray='2,3' />
  <path d='M 0,150 Q 5,156 10,150 Q 15,156 20,150 Q 25,156 30,150 Q 35,156 40,150 Q 45,156 50,150 Q 55,156 60,150 Q 65,156 70,150 Q 75,156 80,150 Q 85,156 90,150 Q 95,156 100,150 Q 105,156 110,150 Q 115,156 120,150 Q 125,156 130,150 Q 135,156 140,150 Q 145,156 150,150 Q 155,156 160,150' fill='none' stroke='currentColor' stroke-width='0.8' />

  <!-- Center Tree / Flower Pot Motif -->
  <g>
    <!-- Stand -->
    <line x1='72' y1='116' x2='88' y2='116' stroke='currentColor' stroke-width='1' />
    <!-- Pot -->
    <path d='M 74,110 C 74,115 86,115 86,110 Z' fill='currentColor' />
    <path d='M 74,110 L 86,110 L 82,106 L 78,106 Z' fill='none' stroke='currentColor' stroke-width='0.8' />
    <!-- Main stem -->
    <path d='M 80,106 L 80,56' stroke='currentColor' stroke-width='1.2' />
    <!-- Top 4-petal flower -->
    <circle cx='80' cy='53' r='2' fill='currentColor' />
    <path d='M 80,53 C 77,46 83,46 80,53 C 80,46 87,49 80,53 C 80,60 83,60 80,53 C 73,53 73,49 80,53' fill='none' stroke='currentColor' stroke-width='0.8' />
    <!-- Radiating dots -->
    <circle cx='80' cy='44' r='0.8' fill='currentColor' />
    <circle cx='89' cy='53' r='0.8' fill='currentColor' />
    <circle cx='71' cy='53' r='0.8' fill='currentColor' />
    <!-- Branches/Curls -->
    <!-- Lower branches -->
    <path d='M 80,95 C 68,95 64,83 70,79 C 74,81 73,89 80,91' fill='none' stroke='currentColor' stroke-width='0.8' />
    <path d='M 80,95 C 92,95 96,83 90,79 C 86,81 87,89 80,91' fill='none' stroke='currentColor' stroke-width='0.8' />
    <!-- Upper branches -->
    <path d='M 80,78 C 70,78 66,70 72,66 C 75,68 74,74 80,75' fill='none' stroke='currentColor' stroke-width='0.8' />
    <path d='M 80,78 C 90,78 94,70 88,66 C 85,68 86,74 80,75' fill='none' stroke='currentColor' stroke-width='0.8' />
  </g>

  <!-- Left Elephant (facing right) -->
  <use href='#elephant' x='12' y='64' />

  <!-- Right Elephant (facing left, mirrored) -->
  <use href='#elephant' transform='translate(160, 0) scale(-1, 1)' x='12' y='64' />

  <!-- Symmetrical Half-Diamonds on Left and Right borders to form seamless diamonds -->
  <g>
    <!-- Left half-diamonds -->
    <path d='M 0,26 L 4,30 L 0,34 Z' fill='currentColor' />
    <path d='M 0,76 L 4,80 L 0,84 Z' fill='currentColor' />
    <path d='M 0,126 L 4,130 L 0,134 Z' fill='currentColor' />
    <!-- Right half-diamonds -->
    <path d='M 160,26 L 156,30 L 160,34 Z' fill='currentColor' />
    <path d='M 160,76 L 156,80 L 160,84 Z' fill='currentColor' />
    <path d='M 160,126 L 156,130 L 160,134 Z' fill='currentColor' />
  </g>
</svg>"""
    return svg

def clean_encode_svg(svg, color_hex, opacity):
    svg_colored = svg.replace("currentColor", color_hex)
    defs_end = svg_colored.find("</defs>")
    if defs_end != -1:
        insert_idx = defs_end + len("</defs>")
        svg_colored = (
            svg_colored[:insert_idx]
            + f"<g opacity='{opacity}'>"
            + svg_colored[insert_idx:-6]
            + "</g></svg>"
        )
    else:
        svg_colored = f"<svg opacity='{opacity}'" + svg_colored[4:]

    import re
    svg_clean = re.sub(r'\s+', ' ', svg_colored)
    svg_clean = svg_clean.replace("> <", "><").strip()
    
    encoded = (svg_clean
               .replace("#", "%23")
               .replace("<", "%3C")
               .replace(">", "%3E")
               .replace("'", "%27")
               .replace('"', "%22"))
    return f"data:image/svg+xml,{encoded}"

svg = make_svg()
print("Dark Mode background-image:")
print(f'background-image: url("{clean_encode_svg(svg, "#ffffff", 0.06)}");')
print("\nLight Mode background-image:")
print(f'background-image: url("{clean_encode_svg(svg, "#8c2d19", 0.08)}"), linear-gradient(180deg, #fff7e8 0%, #f8ead3 100%) !important;')
