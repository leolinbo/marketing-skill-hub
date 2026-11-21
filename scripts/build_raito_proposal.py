import os
import base64
import shutil
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

target_dir = 'D:/marketing/开发信Word库_完整版'
os.makedirs(target_dir, exist_ok=True)
img_dest_dir = os.path.join(target_dir, 'Raito_Lighting_提案配套图片')
os.makedirs(img_dest_dir, exist_ok=True)

img_della_src = 'D:/marketing/assets/products/DELLA/DELLA 2.0 Downlight Mail Group-Evan-V0-20260626_image1.png'
img_magnetic_src = 'D:/marketing/assets/products/MAGNETIC/Evan Mail Group-Magnetic V2_image1.png'
img_nova_src = 'D:/marketing/assets/products/NOVA/NOVA Cylinder Mail Group-Evan-V0-20260825_image1.png'

img_della = os.path.join(img_dest_dir, '1_DELLA_2.0_Downlight.png')
img_magnetic = os.path.join(img_dest_dir, '2_48V_Magnetic_Track_System.png')
img_nova = os.path.join(img_dest_dir, '3_NOVA_Slim_Cylinder.png')

shutil.copy(img_della_src, img_della)
shutil.copy(img_magnetic_src, img_magnetic)
shutil.copy(img_nova_src, img_nova)

def to_b64(path):
    with open(path, 'rb') as f:
        ext = 'png' if path.endswith('.png') else 'jpeg'
        return f'data:image/{ext};base64,' + base64.b64encode(f.read()).decode('utf-8')

b64_della = to_b64(img_della)
b64_magnetic = to_b64(img_magnetic)
b64_nova = to_b64(img_nova)

# 1. HTML Email
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Encore Lighting - Supply Proposal for Raito Lightings Taguig</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; line-height: 1.6; max-width: 650px; margin: 20px auto; padding: 22px; border: 1px solid #e2e8f0; border-radius: 8px; }}
.subject-box {{ background-color: #f0f9ff; border-left: 4px solid #0284c7; padding: 12px 16px; margin-bottom: 22px; font-weight: bold; color: #0369a1; font-size: 15px; }}
h3 {{ color: #1a365d; margin-top: 26px; margin-bottom: 10px; font-size: 16px; }}
ul {{ margin-top: 6px; padding-left: 20px; }}
li {{ margin-bottom: 7px; font-size: 14.5px; color: #334155; }}
.product-img {{ display: block; max-width: 100%; height: auto; margin: 16px auto; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
.signature {{ margin-top: 30px; border-top: 1px solid #e2e8f0; padding-top: 16px; font-size: 14px; color: #475569; }}
.signature strong {{ color: #0f172a; font-size: 15px; }}
p {{ font-size: 14.5px; margin-bottom: 14px; }}
</style>
</head>
<body>

<div class="subject-box">
Subject: Factory-direct architectural fixtures for Raito Lightings' designer marketplace (Taguig)
</div>

<p>Hi Team Raito,</p>

<p>I came across your store on Instagram (@raitolighting.ph) and really like your positioning as a <strong>designer's marketplace for lighting fixtures</strong> in Taguig City.</p>

<p>Interior designers, architects, and fit-out contractors in Metro Manila are specifying more minimalist, glare-free architectural lighting than ever before. But sourcing consistent, high-CRI fixtures without high retail markups or long supply lead times is always a bottleneck.</p>

<p>We are a direct commercial lighting manufacturer based in Shenzhen, China (Encore Commercial Lighting). We supply boutique lighting showrooms, interior contractors, and design marketplaces across Southeast Asia. Here are 3 best-selling product categories that fit right into Raito's designer catalog:</p>

<h3>1. 48V Low-Voltage Ultra-Slim Magnetic Track System</h3>
<ul>
  <li><strong>The #1 Designer Choice</strong>: Recessed trimless, surface-mounted, and suspended track rails that fit flush in modern residences, condos, and cafes.</li>
  <li><strong>Complete Click-and-Play Module Suite</strong>: Magnetic accent spots, continuous linear diffusers, low-glare darklight gratings, and wall-washers.</li>
  <li><strong>Safe &amp; Flexible</strong>: Safe 48V DC voltage with reliable external/internal drivers and seamless corner joiners.</li>
</ul>
<img class="product-img" src="{b64_magnetic}" alt="48V Magnetic Track System">

<h3>2. DELLA 2.0 Modular Architectural Downlights</h3>
<ul>
  <li><strong>Deep Anti-Glare Comfort (UGR &lt; 10 &amp; Pinhole UGR &lt; 6)</strong>: Delivers soft, premium darklight pools without annoying ceiling glare.</li>
  <li><strong>Interchangeable Bezels &amp; Baffles</strong>: Round, square, fixed, and 30° adjustable angles with interchangeable inner reflectors (Black, White, Matte Gold).</li>
  <li><strong>High Color Fidelity</strong>: CRI 95+, 2700K / 3000K / 4000K, bringing out the genuine texture of wood, stone, and luxury fabrics.</li>
</ul>
<img class="product-img" src="{b64_della}" alt="DELLA 2.0 Architectural Downlights">

<h3>3. NOVA Slim Architectural Cylinders</h3>
<ul>
  <li><strong>Sleek Minimalist Form</strong>: High-grade aluminum body with zero visible exterior screws, perfect for exposed slab ceilings and kitchen islands.</li>
  <li><strong>Multi-Mount Options</strong>: Ceiling surface mount, track adapter mount, or thin aircraft wire suspension.</li>
  <li><strong>Low Glare Baffle</strong>: UGR &lt; 6 with deep regression for superior visual comfort.</li>
</ul>
<img class="product-img" src="{b64_nova}" alt="NOVA Slim Cylinders">

<p><strong>Why partner with Encore for Raito's marketplace:</strong></p>
<ul>
  <li><strong>Low MOQ &amp; Sample Kits</strong>: Fast sample couriering directly to your Taguig location so designers can inspect the quality hands-on.</li>
  <li><strong>Full Digital Assets</strong>: Free high-res lifestyle photos, dimension CADs, specification cut sheets, and IES photometric files ready for your Instagram &amp; catalog.</li>
  <li><strong>Factory-Direct Margin</strong>: Healthy profit margins tailored for lighting stores and distributor markups.</li>
</ul>

<p><strong>Would you be open to receiving a digital PDF catalog and a sample kit quotation for your showroom display?</strong></p>

<div class="signature">
  Best regards,<br><br>
  <strong>Bob</strong><br>
  Encore Commercial Lighting<br>
  Web: <a href="https://encore-tech.com">encore-tech.com</a><br>
  WhatsApp: +852 57651719<br>
  Email: sales@encore-tech.com
</div>

</body>
</html>'''

html_path = 'D:/marketing/开发信Word库_完整版/Encore_Raito_Lightings菲律宾专属定制提案(网页一键复制版).html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated HTML successfully at:', html_path)

# 2. Word Docx
doc = Document()
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

title_p = doc.add_paragraph()
title_run = title_p.add_run("Subject: Factory-direct architectural fixtures for Raito Lightings' designer marketplace (Taguig)")
title_run.font.name = 'Segoe UI'
title_run.font.size = Pt(13)
title_run.font.bold = True
title_run.font.color.rgb = RGBColor(2, 132, 199)
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

def add_heading(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.name = 'Segoe UI'
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(26, 54, 93)
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
    p.add_run().add_picture(path, width=Inches(4.5))

add_p('Hi Team Raito,')
add_p("I came across your store on Instagram (@raitolighting.ph) and really like your positioning as a designer's marketplace for lighting fixtures in Taguig City.")
add_p('Interior designers, architects, and fit-out contractors in Metro Manila are specifying more minimalist, glare-free architectural lighting than ever before. But sourcing consistent, high-CRI fixtures without high retail markups or long supply lead times is always a bottleneck.')
add_p('We are a direct commercial lighting manufacturer based in Shenzhen, China (Encore Commercial Lighting). We supply boutique lighting showrooms, interior contractors, and design marketplaces across Southeast Asia. Here are 3 best-selling product categories that fit right into Raito\'s designer catalog:')

add_heading('1. 48V Low-Voltage Ultra-Slim Magnetic Track System')
add_bullet('The #1 Designer Choice', 'Recessed trimless, surface-mounted, and suspended track rails that fit flush in modern residences, condos, and cafes.')
add_bullet('Complete Click-and-Play Module Suite', 'Magnetic accent spots, continuous linear diffusers, low-glare darklight gratings, and wall-washers.')
add_bullet('Safe & Flexible', 'Safe 48V DC voltage with reliable external/internal drivers and seamless corner joiners.')
add_img(img_magnetic)

add_heading('2. DELLA 2.0 Modular Architectural Downlights')
add_bullet('Deep Anti-Glare Comfort (UGR < 10 & Pinhole UGR < 6)', 'Delivers soft, premium darklight pools without annoying ceiling glare.')
add_bullet('Interchangeable Bezels & Baffles', 'Round, square, fixed, and 30° adjustable angles with interchangeable inner reflectors (Black, White, Matte Gold).')
add_bullet('High Color Fidelity', 'CRI 95+, 2700K / 3000K / 4000K, bringing out the genuine texture of wood, stone, and luxury fabrics.')
add_img(img_della)

add_heading('3. NOVA Slim Architectural Cylinders')
add_bullet('Sleek Minimalist Form', 'High-grade aluminum body with zero visible exterior screws, perfect for exposed slab ceilings and kitchen islands.')
add_bullet('Multi-Mount Options', 'Ceiling surface mount, track adapter mount, or thin aircraft wire suspension.')
add_bullet('Low Glare Baffle', 'UGR < 6 with deep regression for superior visual comfort.')
add_img(img_nova)

add_p('Why partner with Encore for Raito\'s marketplace:', bold=True)
add_bullet('Low MOQ & Sample Kits', 'Fast sample couriering directly to your Taguig location so designers can inspect the quality hands-on.')
add_bullet('Full Digital Assets', 'Free high-res lifestyle photos, dimension CADs, specification cut sheets, and IES photometric files ready for your Instagram & catalog.')
add_bullet('Factory-Direct Margin', 'Healthy profit margins tailored for lighting stores and distributor markups.')

add_p('Would you be open to receiving a digital PDF catalog and a sample kit quotation for your showroom display?', bold=True)

sig_p = doc.add_paragraph()
sig_p.paragraph_format.space_before = Pt(16)
sig_run = sig_p.add_run('Best regards,\n\nBob\nEncore Commercial Lighting\nWeb: encore-tech.com\nWhatsApp: +852 57651719\nEmail: sales@encore-tech.com')
sig_run.font.name = 'Segoe UI'
sig_run.font.size = Pt(10)
sig_run.font.color.rgb = RGBColor(71, 85, 105)

docx_path = 'D:/marketing/开发信Word库_完整版/Encore_Raito_Lightings菲律宾专属定制提案(图文版).docx'
doc.save(docx_path)
print('Generated DOCX successfully at:', docx_path)
