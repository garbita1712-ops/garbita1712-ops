import urllib.request, os, base64, io
from PIL import Image, ImageDraw, ImageFont
import xml.etree.ElementTree as ET

# 1. Download Great Vibes Cursive Handwriting Font
font_url = "https://github.com/google/fonts/raw/main/ofl/greatvibes/GreatVibes-Regular.ttf"
font_path = "/tmp/GreatVibes-Regular.ttf"
if not os.path.exists(font_path):
    urllib.request.urlretrieve(font_url, font_path)

font = ImageFont.truetype(font_path, 95)

# 2. Render Dark Theme Handwritten Signature (Electric Cyan #79C0FF)
img_dark = Image.new("RGBA", (850, 160), (0, 0, 0, 0))
draw_dark = ImageDraw.Draw(img_dark)
draw_dark.text((425, 75), "Garbita Chowdhury", font=font, fill=(121, 192, 255, 255), anchor="mm")

dark_buf = io.BytesIO()
img_dark.save(dark_buf, format="PNG")
dark_b64 = base64.b64encode(dark_buf.getvalue()).decode("utf-8")
dark_data_uri = f"data:image/png;base64,{dark_b64}"

# 3. Render Light Theme Handwritten Signature (Deep Blue #0969DA)
img_light = Image.new("RGBA", (850, 160), (0, 0, 0, 0))
draw_light = ImageDraw.Draw(img_light)
draw_light.text((425, 75), "Garbita Chowdhury", font=font, fill=(9, 105, 218, 255), anchor="mm")

light_buf = io.BytesIO()
img_light.save(light_buf, format="PNG")
light_b64 = base64.b64encode(light_buf.getvalue()).decode("utf-8")
light_data_uri = f"data:image/png;base64,{light_b64}"

# 4. Construct Dark Mode Signature SVG
dark_sig_svg = f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ui-monospace,SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace" width="850px" height="190px">
<style>
.title {{fill: #8b949e; font-size: 13px; letter-spacing: 4px; font-weight: 600; text-anchor: middle;}}
.tag {{fill: #616e7f; font-size: 12px; letter-spacing: 2px; text-anchor: middle;}}
</style>
<g>
  <image href="{dark_data_uri}" x="0" y="0" width="850" height="150" />
  <text x="425" y="160" class="title">FULL-STACK ARCHITECT &amp; AI SYSTEMS LEAD</text>
  <text x="425" y="180" class="tag">KALYANI GOVT. ENGINEERING COLLEGE (KGEC)</text>
</g>
</svg>"""

# 5. Construct Light Mode Signature SVG
light_sig_svg = f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ui-monospace,SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace" width="850px" height="190px">
<style>
.title {{fill: #57606a; font-size: 13px; letter-spacing: 4px; font-weight: 600; text-anchor: middle;}}
.tag {{fill: #8c959f; font-size: 12px; letter-spacing: 2px; text-anchor: middle;}}
</style>
<g>
  <image href="{light_data_uri}" x="0" y="0" width="850" height="150" />
  <text x="425" y="160" class="title">FULL-STACK ARCHITECT &amp; AI SYSTEMS LEAD</text>
  <text x="425" y="180" class="tag">KALYANI GOVT. ENGINEERING COLLEGE (KGEC)</text>
</g>
</svg>"""

dark_file = '/home/akashbiswas/Desktop/projects/projects/garbita/garbita1712-ops/signature_dark.svg'
light_file = '/home/akashbiswas/Desktop/projects/projects/garbita/garbita1712-ops/signature_light.svg'

with open(dark_file, 'w') as f:
    f.write(dark_sig_svg)

with open(light_file, 'w') as f:
    f.write(light_sig_svg)

ET.parse(dark_file)
ET.parse(light_file)
print("SUCCESS! Big handwritten signature SVGs created successfully!")
