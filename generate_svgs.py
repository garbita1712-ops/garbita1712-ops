import base64
from PIL import Image, ImageEnhance
import io
import shutil
import xml.etree.ElementTree as ET

# 1. Dark Mode Portrait: Crystal Clear Sketch on Pitch Black Background
dark_img_path = '/home/akashbiswas/.gemini/antigravity/brain/4d0cbaf7-8dd4-47de-9ba4-46576c19472a/dark_obsidian_sketch_portrait_1788707557901.png'
dark_img = Image.open(dark_img_path)

# Crop to frame face & upper body
w, h = dark_img.size
crop_box = (int(w * 0.02), int(h * 0.02), int(w * 0.98), int(h * 0.98))
dark_cropped = dark_img.crop(crop_box)

dark_buf = io.BytesIO()
dark_cropped.save(dark_buf, format='PNG', compress_level=6)
dark_b64 = base64.b64encode(dark_buf.getvalue()).decode('utf-8')
dark_data_uri = f'data:image/png;base64,{dark_b64}'

# 2. Light Mode Portrait: Original Paper Background Sketch
orig_path = '/home/akashbiswas/.gemini/antigravity/brain/4d0cbaf7-8dd4-47de-9ba4-46576c19472a/media__1788705592456.jpg'
orig_img = Image.open(orig_path)
w_orig, h_orig = orig_img.size
orig_cropped = orig_img.crop((int(w_orig * 0.05), int(h_orig * 0.04), int(w_orig * 0.95), int(h_orig * 0.96)))

light_buf = io.BytesIO()
orig_cropped.save(light_buf, format='JPEG', quality=95)
light_b64 = base64.b64encode(light_buf.getvalue()).decode('utf-8')
light_data_uri = f'data:image/jpeg;base64,{light_b64}'

# 3. Construct Dark Mode SVG (No blue border stroke)
dark_svg = f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ui-monospace,SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace" width="1000px" height="550px" font-size="14.5px">
<style>
.key {{fill: #ffa657;}}
.value {{fill: #a5d6ff;}}
.addColor {{fill: #3fb950;}}
.delColor {{fill: #f85149;}}
.cc {{fill: #616e7f;}}
text, tspan {{white-space: pre;}}
</style>
<defs>
  <clipPath id="avatar-clip">
    <rect x="25" y="25" width="330" height="500" rx="15" />
  </clipPath>
</defs>
<rect width="1000px" height="550px" fill="#161b22" rx="15"/>
<!-- Left Column: Borderless Crystal Clear Pencil Sketch on Pitch Black Background -->
<image href="{dark_data_uri}" x="25" y="25" width="330" height="500" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatar-clip)" />

<!-- Right Column: System Telemetry -->
<text x="380" y="45" fill="#c9d1d9">
<tspan x="380" y="45">garbita@chowdhury</tspan> ——————————————————————————————————————-—-
<tspan x="380" y="70" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> .......... </tspan><tspan class="value">Linux (NixOS / Arch / Ubuntu)</tspan>
<tspan x="380" y="93" class="cc">. </tspan><tspan class="key">Role</tspan>:<tspan class="cc"> ........ </tspan><tspan class="value">Full-Stack Architect &amp; AI Engineer</tspan>
<tspan x="380" y="116" class="cc">. </tspan><tspan class="key">IDE</tspan>:<tspan class="cc"> ......... </tspan><tspan class="value">VSCode 1.96.0, Neovim, IntelliJ</tspan>
<tspan x="380" y="136" class="cc">. </tspan>
<tspan x="380" y="159" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Code</tspan>:<tspan class="cc"> .. </tspan><tspan class="value">TypeScript, Python, JavaScript, C++</tspan>
<tspan x="380" y="182" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Web</tspan>:<tspan class="cc"> ... </tspan><tspan class="value">HTML5, CSS3, JSON, Markdown, YAML</tspan>
<tspan x="380" y="205" class="cc">. </tspan><tspan class="key">Frameworks</tspan>:<tspan class="cc"> ... </tspan><tspan class="value">Next.js 16, React 19, FastAPI, Flutter</tspan>
<tspan x="380" y="228" class="cc">. </tspan><tspan class="key">AI &amp; ML Stack</tspan>:<tspan class="cc"> . </tspan><tspan class="value">PyTorch, Scikit-Learn, Pandas, NumPy</tspan>
<tspan x="380" y="251" class="cc">. </tspan><tspan class="key">Databases</tspan>:<tspan class="cc"> .... </tspan><tspan class="value">MongoDB, PostgreSQL, Cloudinary CDN</tspan>
<tspan x="380" y="271" class="cc">. </tspan>
<tspan x="380" y="294" class="cc">. </tspan><tspan class="key">Storefront</tspan>:<tspan class="cc"> ... </tspan><tspan class="value">ShopTrend (Next.js 16 E-Commerce)</tspan>
<tspan x="380" y="317" class="cc">. </tspan><tspan class="key">Telemetry</tspan>:<tspan class="cc"> .... </tspan><tspan class="value">WeatherTrack (GIS Map &amp; Tasking)</tspan>
<tspan x="380" y="340" class="cc">. </tspan><tspan class="key">AI/ML Core</tspan>:<tspan class="cc"> ... </tspan><tspan class="value">NER-SHIELD (SIH 2026 Hazard AI)</tspan>
<tspan x="380" y="360" class="cc">. </tspan>
<tspan x="380" y="383">- Contact ———————————————————————————————————————————-—-</tspan>
<tspan x="380" y="406" class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ........ </tspan><tspan class="value">garbita.chowdhury.arcade25@gmail.com</tspan>
<tspan x="380" y="429" class="cc">. </tspan><tspan class="key">GitHub</tspan>:<tspan class="cc"> ....... </tspan><tspan class="value">garbita1712-ops</tspan>
<tspan x="380" y="449" class="cc">. </tspan>
<tspan x="380" y="472">- GitHub Telemetry —————————————————————————————————-—-</tspan>
<tspan x="380" y="495" class="cc">. </tspan><tspan class="key">Repos</tspan>:<tspan class="cc"> .. </tspan><tspan class="value">5</tspan>&#160;{{<tspan class="key">Contributed</tspan>: <tspan class="value">12</tspan>}} | <tspan class="key">Stars</tspan>:<tspan class="cc"> .. </tspan><tspan class="value">18</tspan> | <tspan class="key">Commits</tspan>:<tspan class="cc"> .. </tspan><tspan class="value">47</tspan>
<tspan x="380" y="518" class="cc">. </tspan><tspan class="key">LOC</tspan>:<tspan class="cc"> .... </tspan><tspan class="value">124,890</tspan> ( <tspan class="addColor">142,500++</tspan>, <tspan class="delColor">17,610--</tspan> )
</text>
</svg>"""

# 4. Construct Light Mode SVG (No blue border stroke)
light_svg = f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ui-monospace,SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace" width="1000px" height="550px" font-size="14.5px">
<style>
.key {{fill: #0969da;}}
.value {{fill: #1f2328;}}
.addColor {{fill: #1a7f37;}}
.delColor {{fill: #cf222e;}}
.cc {{fill: #8c959f;}}
text, tspan {{white-space: pre;}}
</style>
<defs>
  <clipPath id="avatar-clip">
    <rect x="25" y="25" width="330" height="500" rx="15" />
  </clipPath>
</defs>
<rect width="1000px" height="550px" fill="#ffffff" rx="15" stroke="#d0d7de" stroke-width="2"/>
<!-- Left Column: Borderless Clear Original Pencil Sketch -->
<image href="{light_data_uri}" x="25" y="25" width="330" height="500" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatar-clip)" />

<!-- Right Column: System Telemetry -->
<text x="380" y="45" fill="#1f2328">
<tspan x="380" y="45">garbita@chowdhury</tspan> ——————————————————————————————————————-—-
<tspan x="380" y="70" class="cc">. </tspan><tspan class="key">OS</tspan>:<tspan class="cc"> .......... </tspan><tspan class="value">Linux (NixOS / Arch / Ubuntu)</tspan>
<tspan x="380" y="93" class="cc">. </tspan><tspan class="key">Role</tspan>:<tspan class="cc"> ........ </tspan><tspan class="value">Full-Stack Architect &amp; AI Engineer</tspan>
<tspan x="380" y="116" class="cc">. </tspan><tspan class="key">IDE</tspan>:<tspan class="cc"> ......... </tspan><tspan class="value">VSCode 1.96.0, Neovim, IntelliJ</tspan>
<tspan x="380" y="136" class="cc">. </tspan>
<tspan x="380" y="159" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Code</tspan>:<tspan class="cc"> .. </tspan><tspan class="value">TypeScript, Python, JavaScript, C++</tspan>
<tspan x="380" y="182" class="cc">. </tspan><tspan class="key">Languages</tspan>.<tspan class="key">Web</tspan>:<tspan class="cc"> ... </tspan><tspan class="value">HTML5, CSS3, JSON, Markdown, YAML</tspan>
<tspan x="380" y="205" class="cc">. </tspan><tspan class="key">Frameworks</tspan>:<tspan class="cc"> ... </tspan><tspan class="value">Next.js 16, React 19, FastAPI, Flutter</tspan>
<tspan x="380" y="228" class="cc">. </tspan><tspan class="key">AI &amp; ML Stack</tspan>:<tspan class="cc"> . </tspan><tspan class="value">PyTorch, Scikit-Learn, Pandas, NumPy</tspan>
<tspan x="380" y="251" class="cc">. </tspan><tspan class="key">Databases</tspan>:<tspan class="cc"> .... </tspan><tspan class="value">MongoDB, PostgreSQL, Cloudinary CDN</tspan>
<tspan x="380" y="271" class="cc">. </tspan>
<tspan x="380" y="294" class="cc">. </tspan><tspan class="key">Storefront</tspan>:<tspan class="cc"> ... </tspan><tspan class="value">ShopTrend (Next.js 16 E-Commerce)</tspan>
<tspan x="380" y="317" class="cc">. </tspan><tspan class="key">Telemetry</tspan>:<tspan class="cc"> .... </tspan><tspan class="value">WeatherTrack (GIS Map &amp; Tasking)</tspan>
<tspan x="380" y="340" class="cc">. </tspan><tspan class="key">AI/ML Core</tspan>:<tspan class="cc"> ... </tspan><tspan class="value">NER-SHIELD (SIH 2026 Hazard AI)</tspan>
<tspan x="380" y="360" class="cc">. </tspan>
<tspan x="380" y="383">- Contact ———————————————————————————————————————————-—-</tspan>
<tspan x="380" y="406" class="cc">. </tspan><tspan class="key">Email</tspan>:<tspan class="cc"> ........ </tspan><tspan class="value">garbita.chowdhury.arcade25@gmail.com</tspan>
<tspan x="380" y="429" class="cc">. </tspan><tspan class="key">GitHub</tspan>:<tspan class="cc"> ....... </tspan><tspan class="value">garbita1712-ops</tspan>
<tspan x="380" y="449" class="cc">. </tspan>
<tspan x="380" y="472">- GitHub Telemetry —————————————————————————————————-—-</tspan>
<tspan x="380" y="495" class="cc">. </tspan><tspan class="key">Repos</tspan>:<tspan class="cc"> .. </tspan><tspan class="value">5</tspan>&#160;{{<tspan class="key">Contributed</tspan>: <tspan class="value">12</tspan>}} | <tspan class="key">Stars</tspan>:<tspan class="cc"> .. </tspan><tspan class="value">18</tspan> | <tspan class="key">Commits</tspan>:<tspan class="cc"> .. </tspan><tspan class="value">47</tspan>
<tspan x="380" y="518" class="cc">. </tspan><tspan class="key">LOC</tspan>:<tspan class="cc"> .... </tspan><tspan class="value">124,890</tspan> ( <tspan class="addColor">142,500++</tspan>, <tspan class="delColor">17,610--</tspan> )
</text>
</svg>"""

dark_file = '/home/akashbiswas/Desktop/projects/projects/garbita/garbita1712-ops/dark_mode.svg'
light_file = '/home/akashbiswas/Desktop/projects/projects/garbita/garbita1712-ops/light_mode.svg'

with open(dark_file, 'w') as f:
    f.write(dark_svg)

with open(light_file, 'w') as f:
    f.write(light_svg)

shutil.copy(dark_file, '/home/akashbiswas/Desktop/projects/projects/garbita/dark_mode.svg')
shutil.copy(light_file, '/home/akashbiswas/Desktop/projects/projects/garbita/light_mode.svg')

ET.parse(dark_file)
ET.parse(light_file)
print('SUCCESS! Blue border removed completely from image frame!')
