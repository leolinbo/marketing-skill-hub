import os
import base64
import shutil
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

target_dir = 'D:/marketing/开发信Word库_完整版'
os.makedirs(target_dir, exist_ok=True)
img_dest_dir = os.path.join(target_dir, 'Arkultura_Architecture_提案配套图片')
os.makedirs(img_dest_dir, exist_ok=True)

src_della = 'D:/marketing/assets/products/DELLA/DELLA 2.0 Downlight Mail Group-Evan-V0-20260626_image1.png'
src_mag = 'D:/marketing/assets/products/MAGNETIC/Choco Mail Group-Magnetic_image1.jpeg'
src_nova = 'D:/marketing/assets/products/NOVA/NOVA Cylinder Mail Group-Choco-V0-20260825_image1.png'

dst_della = os.path.join(img_dest_dir, '1_DELLA_2.0_Modular_Downlight.png')
dst_mag = os.path.join(img_dest_dir, '2_48V_Magnetic_Track_System.jpeg')
dst_nova = os.path.join(img_dest_dir, '3_NOVA_Slim_Pendant_Cylinder.png')

shutil.copy(src_della, dst_della)
shutil.copy(src_mag, dst_mag)
shutil.copy(src_nova, dst_nova)

def to_b64(path):
    with open(path, 'rb') as f:
        ext = 'png' if path.endswith('.png') else 'jpeg'
        return f'data:image/{ext};base64,' + base64.b64encode(f.read()).decode('utf-8')

b64_della = to_b64(dst_della)
b64_mag = to_b64(dst_mag)
b64_nova = to_b64(dst_nova)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Encore Lighting - Fit-Out Lighting Supply for Arkultura Architecture</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; line-height: 1.6; max-width: 650px; margin: 20px auto; padding: 24px; border: 1px solid #e2e8f0; border-radius: 8px; }}
.subject-box {{ background-color: #f0fdf4; border-left: 4px solid #16a34a; padding: 12px 16px; margin-bottom: 22px; font-weight: bold; color: #166534; font-size: 15px; }}
h3 {{ color: #0f172a; margin-top: 26px; margin-bottom: 8px; font-size: 16px; }}
ul {{ margin-top: 6px; padding-left: 20px; }}
li {{ margin-bottom: 7px; font-size: 14.5px; color: #334155; }}
.product-img {{ display: block; max-width: 100%; height: auto; margin: 16px auto; border-radius: 6px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }}
.signature {{ margin-top: 32px; border-top: 1px solid #e2e8f0; padding-top: 18px; font-size: 14px; color: #475569; }}
.signature strong {{ color: #0f172a; font-size: 15px; }}
p {{ font-size: 14.5px; margin-bottom: 14px; }}
.badge {{ display: inline-block; background-color: #f1f5f9; color: #475569; font-size: 12px; font-weight: 600; padding: 2px 8px; border-radius: 4px; margin-bottom: 6px; }}
</style>
</head>
<body>

<div class="subject-box">
Subject: Direct factory lighting supply for Arkultura's fit-out &amp; renovation projects (Ortigas / Pasig)
</div>

<p>Hi Team Arkultura,</p>

<p>I came across your work on Instagram (@arkultura) and really appreciate your tagline—<em>"Built with passion. Defined by quality."</em> Seeing your focus across <strong>construction, renovation, commercial fit-out, and custom furniture</strong> in Ortigas Center and Pasig, it’s clear you care about solid execution and finish quality.</p>

<p>For fit-out contractors and renovation teams in Metro Manila, lighting is often one of the trickiest parts: retail suppliers markup prices heavily, ceiling depths vary between gypsum and concrete slabs, and clients constantly complain if downlights cause harsh glare or wash out custom woodwork.</p>

<p>We are a direct commercial and architectural lighting manufacturer based in Shenzhen, China (Encore Commercial Lighting). We work closely with contractors and fit-out specialists to provide builder-friendly, factory-direct lighting packages. Here are 3 versatile fixture families designed to make your site installations smooth and client-approved:</p>

<h3>1. DELLA 2.0 Modular Architectural Downlights</h3>
<span class="badge">Application: Residential Renovations &amp; Executive Offices</span>
<ul>
  <li><strong>Zero Glare Comfort (UGR &lt; 10 &amp; Pinhole UGR &lt; 6)</strong>: Eliminates ceiling glare completely, delivering luxurious, soft lighting pools that elevate any ceiling finish.</li>
  <li><strong>Modular Engine</strong>: One single cutout fits fixed spots, 30° adjustable accents, and wall-washers to illuminate custom feature walls and cabinetry.</li>
  <li><strong>CRI 95+ True Color</strong>: Perfectly highlights natural wood grains, stone textures, and custom paint finishes.</li>
</ul>
<img class="product-img" src="{b64_della}" alt="DELLA 2.0 Architectural Downlights">

<h3>2. 48V Low-Voltage Ultra-Slim Magnetic Track System</h3>
<span class="badge">Application: Modern Commercial Fit-Outs &amp; Open Layouts</span>
<ul>
  <li><strong>Trimless &amp; Surface Mounting</strong>: Recesses completely flush into standard gypsum ceiling boards with no visible flanges, or mounts cleanly on raw concrete slabs.</li>
  <li><strong>Tool-Free Click-in Modules</strong>: Magnetic spotlights, wide linear diffusers, and darklight modules can be clicked, repositioned, or added by hand in seconds.</li>
  <li><strong>Safe 48V DC Operation</strong>: Safe low voltage with reliable external power supplies, eliminating flickering and heat issues on site.</li>
</ul>
<img class="product-img" src="{b64_mag}" alt="48V Magnetic Track System">

<h3>3. NOVA Minimalist Slim Cylinders (Φ30mm / Φ45mm)</h3>
<span class="badge">Application: Concrete Slabs, Kitchen Counters &amp; Breakout Zones</span>
<ul>
  <li><strong>No Drop Ceiling Needed</strong>: Surface-mounts directly onto concrete slabs or suspends neatly via thin aircraft wire with an <strong>invisible internal cable lock</strong> (no ugly visible screws).</li>
  <li><strong>Sleek Architectural Finishes</strong>: Matte Black, Clean White, and Anodized Champagne Gold that seamlessly blend with modern interior furniture and hardware.</li>
  <li><strong>UGR &lt; 6 Deep Baffle</strong>: Visual comfort even in low-ceiling dining spaces and reception counters.</li>
</ul>
<img class="product-img" src="{b64_nova}" alt="NOVA Slim Cylinders">

<p><strong>How Encore supports Arkultura's contracting workflow:</strong></p>
<ul>
  <li><strong>Direct BOM &amp; CAD Takeoff Quoting</strong>: Send us your AutoCAD ceiling plans or fixture schedule, and we will quote full factory packages with driver recommendations within 24 hours.</li>
  <li><strong>Fast Couriered Sample Kits</strong>: Test the actual aluminum housing, spring clips, and light quality on-site before committing.</li>
  <li><strong>Direct Factory Pricing</strong>: Keep project margins healthy while delivering high-spec lighting to your clients.</li>
</ul>

<p><strong>Do you have any ongoing fit-out, renovation, or commercial projects currently on your board? We’d be delighted to quote your fixture schedule or courier a sample box to your Ortigas office. Open to taking a look?</strong></p>

<div class="signature">
  Best regards,<br><br>
  <strong>Bob</strong><br>
  Encore Commercial Lighting<br>
  Web: <a href="https://encore-tech.com">encore-tech.com</a><br>
  Email: sales21@encore-tech.com<br>
  WhatsApp: +852 57651719
</div>

</body>
</html>'''

html_path = 'D:/marketing/开发信Word库_完整版/Encore_Arkultura_Architecture菲律宾专属定制提案(网页一键复制版).html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated Arkultura HTML successfully at:', html_path)

# Build docx
doc = Document()
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

title_p = doc.add_paragraph()
title_run = title_p.add_run("Subject: Direct factory lighting supply for Arkultura's fit-out & renovation projects (Ortigas / Pasig)")
title_run.font.name = 'Segoe UI'
title_run.font.size = Pt(13)
title_run.font.bold = True
title_run.font.color.rgb = RGBColor(22, 101, 52)
title_p.paragraph_format.space_after = Pt(14)

def add_p(text, bold=False, space_after=8):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.name = 'Segoe UI'
    r.font.size = Pt(10.5)
    r.font.bold = bold
    r.font.color.rgb = RGBColor(30, 41, 59)
    p.paragraph_format.space_after = Pt(space_after)
    return p

def add_heading(text, badge=''):
    p = doc.add_paragraph()
    r = p.add_run(text + (' (' + badge + ')' if badge else ''))
    r.font.name = 'Segoe UI'
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(15, 23, 42)
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    return p

def add_bullet(lead, text):
    p = doc.add_paragraph(style='List Bullet')
    r1 = p.add_run(lead + ': ')
    r1.font.name = 'Segoe UI'
    r1.font.size = Pt(10)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(30, 41, 59)
    
    r2 = p.add_run(text)
    r2.font.name = 'Segoe UI'
    r2.font.size = Pt(10)
    r2.font.color.rgb = RGBColor(71, 85, 105)
    p.paragraph_format.space_after = Pt(3)
    return p

def add_img(path):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(12)
    p.add_run().add_picture(path, width=Inches(4.8))

add_p('Hi Team Arkultura,')
add_p('I came across your work on Instagram (@arkultura) and really appreciate your tagline—"Built with passion. Defined by quality." Seeing your focus across construction, renovation, commercial fit-out, and custom furniture in Ortigas Center and Pasig, it’s clear you care about solid execution and finish quality.')
add_p('For fit-out contractors and renovation teams in Metro Manila, lighting is often one of the trickiest parts: retail suppliers markup prices heavily, ceiling depths vary between gypsum and concrete slabs, and clients constantly complain if downlights cause harsh glare or wash out custom woodwork.')
add_p('We are a direct commercial and architectural lighting manufacturer based in Shenzhen, China (Encore Commercial Lighting). We work closely with contractors and fit-out specialists to provide builder-friendly, factory-direct lighting packages. Here are 3 versatile fixture families designed to make your site installations smooth and client-approved:')

add_heading('1. DELLA 2.0 Modular Architectural Downlights', 'Residential Renovations & Executive Offices')
add_bullet('Zero Glare Comfort (UGR < 10 & Pinhole UGR < 6)', 'Eliminates ceiling glare completely, delivering luxurious, soft lighting pools that elevate any ceiling finish.')
add_bullet('Modular Engine', 'One single cutout fits fixed spots, 30° adjustable accents, and wall-washers to illuminate custom feature walls and cabinetry.')
add_bullet('CRI 95+ True Color', 'Perfectly highlights natural wood grains, stone textures, and custom paint finishes.')
add_img(dst_della)

add_heading('2. 48V Low-Voltage Ultra-Slim Magnetic Track System', 'Modern Commercial Fit-Outs & Open Layouts')
add_bullet('Trimless & Surface Mounting', 'Recesses completely flush into standard gypsum ceiling boards with no visible flanges, or mounts cleanly on raw concrete slabs.')
add_bullet('Tool-Free Click-in Modules', 'Magnetic spotlights, wide linear diffusers, and darklight modules can be clicked, repositioned, or added by hand in seconds.')
add_bullet('Safe 48V DC Operation', 'Safe low voltage with reliable external power supplies, eliminating flickering and heat issues on site.')
add_img(dst_mag)

add_heading('3. NOVA Minimalist Slim Cylinders (Φ30mm / Φ45mm)', 'Concrete Slabs, Kitchen Counters & Breakout Zones')
add_bullet('No Drop Ceiling Needed', 'Surface-mounts directly onto concrete slabs or suspends neatly via thin aircraft wire with an invisible internal cable lock (no ugly visible screws).')
add_bullet('Sleek Architectural Finishes', 'Matte Black, Clean White, and Anodized Champagne Gold that seamlessly blend with modern interior furniture and hardware.')
add_bullet('UGR < 6 Deep Baffle', 'Visual comfort even in low-ceiling dining spaces and reception counters.')
add_img(dst_nova)

add_p('How Encore supports Arkultura\'s contracting workflow:', bold=True)
add_bullet('Direct BOM & CAD Takeoff Quoting', 'Send us your AutoCAD ceiling plans or fixture schedule, and we will quote full factory packages with driver recommendations within 24 hours.')
add_bullet('Fast Couriered Sample Kits', 'Test the actual aluminum housing, spring clips, and light quality on-site before committing.')
add_bullet('Direct Factory Pricing', 'Keep project margins healthy while delivering high-spec lighting to your clients.')

add_p('Do you have any ongoing fit-out, renovation, or commercial projects currently on your board? We’d be delighted to quote your fixture schedule or courier a sample box to your Ortigas office. Open to taking a look?', bold=True)

sig_p = doc.add_paragraph()
sig_p.paragraph_format.space_before = Pt(16)
sig_run = sig_p.add_run('Best regards,\n\nBob\nEncore Commercial Lighting\nWeb: encore-tech.com\nEmail: sales21@encore-tech.com\nWhatsApp: +852 57651719')
sig_run.font.name = 'Segoe UI'
sig_run.font.size = Pt(10)
sig_run.font.color.rgb = RGBColor(71, 85, 105)

docx_path = 'D:/marketing/开发信Word库_完整版/Encore_Arkultura_Architecture菲律宾专属定制提案(图文版).docx'
doc.save(docx_path)
print('Generated Arkultura DOCX successfully at:', docx_path)
