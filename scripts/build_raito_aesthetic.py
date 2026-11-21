import os
import base64
import shutil
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

target_dir = 'D:/marketing/开发信Word库_完整版'
os.makedirs(target_dir, exist_ok=True)
img_dest_dir = os.path.join(target_dir, 'Raito_Lighting_高审美设计款图片')
os.makedirs(img_dest_dir, exist_ok=True)

src_nova = 'D:/marketing/assets/products/NOVA/NOVA Cylinder Mail Group-Choco-V0-20260825_image1.png'
src_flex = 'D:/marketing/assets/products/FLEX/FLEX Track Light Mail Group-Choco-V0-20260704_image1.png'
src_display = 'D:/marketing/assets/products/Digital Display Track Light/Digital Display Track Light Mail Group-Choco-V0-20260817_image1.png'
src_mag = 'D:/marketing/assets/products/MAGNETIC/Choco Mail Group-Magnetic_image1.jpeg'

dst_nova = os.path.join(img_dest_dir, '1_NOVA_Slim_Pendant_Cylinder.png')
dst_flex = os.path.join(img_dest_dir, '2_FLEX_Foldable_Architectural_Spot.png')
dst_display = os.path.join(img_dest_dir, '3_Digital_Screen_Smart_Track_Light.png')
dst_mag = os.path.join(img_dest_dir, '4_48V_Magnetic_Track_System.jpeg')

shutil.copy(src_nova, dst_nova)
shutil.copy(src_flex, dst_flex)
shutil.copy(src_display, dst_display)
shutil.copy(src_mag, dst_mag)

def to_b64(path):
    with open(path, 'rb') as f:
        ext = 'png' if path.endswith('.png') else 'jpeg'
        return f'data:image/{ext};base64,' + base64.b64encode(f.read()).decode('utf-8')

b64_nova = to_b64(dst_nova)
b64_flex = to_b64(dst_flex)
b64_display = to_b64(dst_display)
b64_mag = to_b64(dst_mag)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Encore Lighting - High-Aesthetic Decorative &amp; Architectural Range for Raito Lightings</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; line-height: 1.6; max-width: 650px; margin: 20px auto; padding: 24px; border: 1px solid #e2e8f0; border-radius: 8px; }}
.subject-box {{ background-color: #fdf4ff; border-left: 4px solid #c026d3; padding: 12px 16px; margin-bottom: 22px; font-weight: bold; color: #86198f; font-size: 15px; }}
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
Subject: High-aesthetic sculptural &amp; decorative architectural fixtures for Raito's designer marketplace
</div>

<p>Hi Team Raito,</p>

<p>Following up on my note earlier—I spent some more time browsing your curated gallery on Instagram (@raitolighting.ph). You clearly cater to interior designers and homeowners who prioritize <strong>high aesthetics, striking form factors, and Instagram-worthy decorative appeal</strong> rather than boring, generic utility lights.</p>

<p>As a designer marketplace in Taguig, your clients want pieces that make an architectural statement while delivering museum-grade light quality.</p>

<p>We are an engineering-driven commercial and decorative lighting manufacturer based in Shenzhen (Encore Commercial Lighting). Here are 4 of our most visually refined, design-led statement fixtures created specifically for boutique studios and designer marketplaces:</p>

<h3>1. NOVA Ultra-Slim Pendant &amp; Surface Cylinders (Φ30mm / Φ45mm)</h3>
<span class="badge">Aesthetic Focus: Pure Minimalist Silhouette</span>
<ul>
  <li><strong>Invisible Retractable Wire Lock</strong>: Zero visible screws or bulky hardware at the top—just a seamless, floating metal cylinder.</li>
  <li><strong>Luxury Interior Finishes</strong>: Anodized Champagne Gold, Deep Matte Black, Architectural White, and custom RAL finishes for kitchen islands, dining tables, and bedside drops.</li>
  <li><strong>Dark-Light Visual Comfort (UGR &lt; 6)</strong>: Deeply regressed 50° cut-off optic keeps the light pool soft and glare-free.</li>
</ul>
<img class="product-img" src="{b64_nova}" alt="NOVA Slim Cylinder">

<h3>2. FLEX Geometric Foldable Cylinder Spotlight</h3>
<span class="badge">Aesthetic Focus: Dual Architectural State</span>
<ul>
  <li><strong>Transformative Form</strong>: Sits flush as a sculptural ceiling block, or tilts 90° and rotates 360° to become an active, dynamic directional spot.</li>
  <li><strong>Patented Zero-Sag Mechanical Joint</strong>: Stays crisp in any sculptured angle without drooping over time.</li>
  <li><strong>On-Site Twist Zooming</strong>: Rotate the knurled front bezel to smoothly adjust the beam angle without touching lenses or tools.</li>
</ul>
<img class="product-img" src="{b64_flex}" alt="FLEX Foldable Track Light">

<h3>3. Digital Display Smart Track Light</h3>
<span class="badge">Aesthetic Focus: High-Tech Modern Luxury</span>
<ul>
  <li><strong>Built-in Micro LED Display &amp; Precision Dial</strong>: Designers and clients can see exact CCT (2800K to 6000K) and 0.1% dimming levels digitally on the fixture body.</li>
  <li><strong>Interactive Centerpiece</strong>: Delivers that high-tech showroom "wow factor" that clients love to touch, demonstrate, and share on social media.</li>
  <li><strong>Museum-Grade Color Fidelity (CRI 95+)</strong>: Accentuates fine artwork, curated objects, and luxury fabrics.</li>
</ul>
<img class="product-img" src="{b64_display}" alt="Digital Display Track Light">

<h3>4. 48V Low-Voltage Magnetic Track System with 3D Spatial Continuity</h3>
<span class="badge">Aesthetic Focus: Seamless Ceiling-to-Wall Light Lines</span>
<ul>
  <li><strong>Continuous 3D Spatial Lines</strong>: Seamlessly turns corners from ceiling to walls, creating an architectural light-sculpture across the room.</li>
  <li><strong>Curated Decorative Modules</strong>: Click-in spherical globes, linear ambient diffusers, and ultra-mini magnetic drops that swap out in 2 seconds.</li>
  <li><strong>Safe 48V DC Low-Voltage Architecture</strong>: Clean and completely flush trimless installation into drywall slots.</li>
</ul>
<img class="product-img" src="{b64_mag}" alt="48V Magnetic Track System">

<p><strong>Factory Partnership Perks for Raito's Marketplace:</strong></p>
<ul>
  <li><strong>Showroom Display Samples &amp; Kits</strong>: Fast courier delivery to Taguig so your team and visiting designers can evaluate the build quality in person.</li>
  <li><strong>Ready-to-Post Marketing Assets</strong>: High-resolution lifestyle photography, 3D CAD models, and video clips ready for your Instagram grid and client mood boards.</li>
  <li><strong>Flexible MOQ &amp; Designer Pricing</strong>: Factory-direct pricing structures allowing healthy dealer margins for your marketplace.</li>
</ul>

<p><strong>Would you be open to receiving our full Aesthetic &amp; Architectural Lookbook (PDF) and sample pricing for your showroom?</strong></p>

<div class="signature">
  Warm regards,<br><br>
  <strong>Bob</strong><br>
  Encore Commercial Lighting<br>
  Web: <a href="https://encore-tech.com">encore-tech.com</a><br>
  WhatsApp: +852 57651719<br>
  Email: sales@encore-tech.com
</div>

</body>
</html>'''

html_path = 'D:/marketing/开发信Word库_完整版/Encore_Raito_Lightings菲律宾高审美设计款提案(网页一键复制版).html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated Aesthetic HTML successfully at:', html_path)

# Build docx
doc = Document()
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

title_p = doc.add_paragraph()
title_run = title_p.add_run("Subject: High-aesthetic sculptural & decorative architectural fixtures for Raito's designer marketplace")
title_run.font.name = 'Segoe UI'
title_run.font.size = Pt(13)
title_run.font.bold = True
title_run.font.color.rgb = RGBColor(192, 38, 211)
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

add_p('Hi Team Raito,')
add_p('Following up on my note earlier—I spent some more time browsing your curated gallery on Instagram (@raitolighting.ph). You clearly cater to interior designers and homeowners who prioritize high aesthetics, striking form factors, and Instagram-worthy decorative appeal rather than boring, generic utility lights.')
add_p('As a designer marketplace in Taguig, your clients want pieces that make an architectural statement while delivering museum-grade light quality.')
add_p('We are an engineering-driven commercial and decorative lighting manufacturer based in Shenzhen (Encore Commercial Lighting). Here are 4 of our most visually refined, design-led statement fixtures created specifically for boutique studios and designer marketplaces:')

add_heading('1. NOVA Ultra-Slim Pendant & Surface Cylinders (Φ30mm / Φ45mm)', 'Pure Minimalist Silhouette')
add_bullet('Invisible Retractable Wire Lock', 'Zero visible screws or bulky hardware at the top—just a seamless, floating metal cylinder.')
add_bullet('Luxury Interior Finishes', 'Anodized Champagne Gold, Deep Matte Black, Architectural White, and custom RAL finishes for kitchen islands, dining tables, and bedside drops.')
add_bullet('Dark-Light Visual Comfort (UGR < 6)', 'Deeply regressed 50° cut-off optic keeps the light pool soft and glare-free.')
add_img(dst_nova)

add_heading('2. FLEX Geometric Foldable Cylinder Spotlight', 'Dual Architectural State')
add_bullet('Transformative Form', 'Sits flush as a sculptural ceiling block, or tilts 90° and rotates 360° to become an active, dynamic directional spot.')
add_bullet('Patented Zero-Sag Mechanical Joint', 'Stays crisp in any sculptured angle without drooping over time.')
add_bullet('On-Site Twist Zooming', 'Rotate the knurled front bezel to smoothly adjust the beam angle without touching lenses or tools.')
add_img(dst_flex)

add_heading('3. Digital Display Smart Track Light', 'High-Tech Modern Luxury')
add_bullet('Built-in Micro LED Display & Precision Dial', 'Designers and clients can see exact CCT (2800K to 6000K) and 0.1% dimming levels digitally on the fixture body.')
add_bullet('Interactive Centerpiece', 'Delivers that high-tech showroom "wow factor" that clients love to touch, demonstrate, and share on social media.')
add_bullet('Museum-Grade Color Fidelity (CRI 95+)', 'Accentuates fine artwork, curated objects, and luxury fabrics.')
add_img(dst_display)

add_heading('4. 48V Low-Voltage Magnetic Track System', 'Seamless Ceiling-to-Wall Light Lines')
add_bullet('Continuous 3D Spatial Lines', 'Seamlessly turns corners from ceiling to walls, creating an architectural light-sculpture across the room.')
add_bullet('Curated Decorative Modules', 'Click-in spherical globes, linear ambient diffusers, and ultra-mini magnetic drops that swap out in 2 seconds.')
add_bullet('Safe 48V DC Low-Voltage Architecture', 'Clean and completely flush trimless installation into drywall slots.')
add_img(dst_mag)

add_p('Factory Partnership Perks for Raito\'s Marketplace:', bold=True)
add_bullet('Showroom Display Samples & Kits', 'Fast courier delivery to Taguig so your team and visiting designers can evaluate the build quality in person.')
add_bullet('Ready-to-Post Marketing Assets', 'High-resolution lifestyle photography, 3D CAD models, and video clips ready for your Instagram grid and client mood boards.')
add_bullet('Flexible MOQ & Designer Pricing', 'Factory-direct pricing structures allowing healthy dealer margins for your marketplace.')

add_p('Would you be open to receiving our full Aesthetic & Architectural Lookbook (PDF) and sample pricing for your showroom?', bold=True)

sig_p = doc.add_paragraph()
sig_p.paragraph_format.space_before = Pt(16)
sig_run = sig_p.add_run('Warm regards,\n\nBob\nEncore Commercial Lighting\nWeb: encore-tech.com\nWhatsApp: +852 57651719\nEmail: sales@encore-tech.com')
sig_run.font.name = 'Segoe UI'
sig_run.font.size = Pt(10)
sig_run.font.color.rgb = RGBColor(71, 85, 105)

docx_path = 'D:/marketing/开发信Word库_完整版/Encore_Raito_Lightings菲律宾高审美设计款提案(图文版).docx'
doc.save(docx_path)
print('Generated Aesthetic DOCX successfully at:', docx_path)
