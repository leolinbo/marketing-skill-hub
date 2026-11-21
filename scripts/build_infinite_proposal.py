import os
import base64
import shutil
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

target_dir = 'D:/marketing/开发信Word库_完整版'
os.makedirs(target_dir, exist_ok=True)
img_dest_dir = os.path.join(target_dir, 'Infinite_Lighting_提案配套图片')

dst_mag = os.path.join(img_dest_dir, '1_48V_Magnetic_Track_System.jpeg')
dst_nova = os.path.join(img_dest_dir, '2_NOVA_Pendant_Cylinder.png')
dst_flex = os.path.join(img_dest_dir, '3_FLEX_Foldable_Spotlight.png')
dst_della = os.path.join(img_dest_dir, '4_DELLA_Architectural_Downlight.png')

def to_b64(path):
    with open(path, 'rb') as f:
        ext = 'png' if path.endswith('.png') else 'jpeg'
        return f'data:image/{ext};base64,' + base64.b64encode(f.read()).decode('utf-8')

b64_mag = to_b64(dst_mag)
b64_nova = to_b64(dst_nova)
b64_flex = to_b64(dst_flex)
b64_della = to_b64(dst_della)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Encore Lighting - Supply Proposal for Infinite Lighting Philippines</title>
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
Subject: Factory-direct 48V magnetic tracks &amp; architectural cylinders for Infinite Lighting (MC Home Depot &amp; QC)
</div>

<p>Hi Team Infinite Lighting,</p>

<p>I came across your showrooms on Instagram (@infinitelightingph) and explored your online store at infinitelighting.ph. Really impressive range—especially your presence at <strong>MC Home Depot Taguig</strong> and your Quezon City main branch.</p>

<p>I noticed that while you have an exquisite collection of luxury chandeliers, your catalog also features <strong>Magnetic Track Light, Linear Lights, and Aluminum Profiles</strong>. With Philippine interior designers increasingly pairing decorative statement chandeliers with clean, low-glare architectural lighting, reliable factory supply on magnetic tracks and minimalist pendants is critical for project fulfillment.</p>

<p>We are a direct commercial and architectural lighting manufacturer based in Shenzhen, China (Encore Commercial Lighting). We supply premier lighting showrooms and distributors across Southeast Asia. Here are 4 curated product lines that perfectly complement Infinite Lighting's high-end portfolio:</p>

<h3>1. 48V Ultra-Slim Magnetic Track Platform with 3D Spatial Corners</h3>
<span class="badge">Category: Designer's Essential Architectural System</span>
<ul>
  <li><strong>Complete Track Profiles</strong>: Trimless recessed, surface-mounted, and suspended slim rails that integrate seamlessly into ceiling slots and turn 3D corners onto walls.</li>
  <li><strong>Versatile Click-in Modules</strong>: Magnetic accent spots, continuous linear diffusers, darklight gratings, and drop pendants—swapped tool-free in seconds.</li>
  <li><strong>Safe &amp; Stable</strong>: 48V low voltage with premium copper busbars preventing flickering and voltage drops across long runs.</li>
</ul>
<img class="product-img" src="{b64_mag}" alt="48V Magnetic Track System">

<h3>2. NOVA Ultra-Slim Architectural Pendant &amp; Surface Cylinders (Φ30mm / Φ45mm)</h3>
<span class="badge">Category: Sculptural Decorative Minimalism</span>
<ul>
  <li><strong>Invisible Retractable Wire Lock</strong>: Zero visible screws or bulky top fittings—a seamless floating metal cylinder for dining tables and kitchen islands.</li>
  <li><strong>Luxury Finishes</strong>: Anodized Champagne Gold, Deep Matte Black, and Architectural White to match luxury hardware.</li>
  <li><strong>Visual Comfort (UGR &lt; 6)</strong>: Deeply recessed optical baffle delivers comfortable illumination without harsh glare.</li>
</ul>
<img class="product-img" src="{b64_nova}" alt="NOVA Slim Pendant Cylinder">

<h3>3. FLEX Foldable &amp; Zoomable Geometric Spotlight</h3>
<span class="badge">Category: Dual Aesthetic State</span>
<ul>
  <li><strong>Transformative Design</strong>: Flushes as a sleek architectural ceiling block, or tilts 90° and rotates 360° to highlight featured artwork or furniture displays.</li>
  <li><strong>Zero-Sag Precision Joint</strong>: Holds any sculptured angle permanently without loosening or drooping.</li>
  <li><strong>Tool-Free Beam Zooming</strong>: Rotate the front ring on-site to zoom between accent spot and wide wash.</li>
</ul>
<img class="product-img" src="{b64_flex}" alt="FLEX Foldable Spotlight">

<h3>4. DELLA 2.0 Architectural Anti-Glare Downlight Series</h3>
<span class="badge">Category: High-CRI Darklight Foundation</span>
<ul>
  <li><strong>True Darklight Effect (UGR &lt; 10 &amp; Pinhole UGR &lt; 6)</strong>: Provides rich, warm pools of light while keeping ceilings visually dark and unobtrusive.</li>
  <li><strong>CRI 95+ (R9 &gt; 80)</strong>: Renders rich wood grains, natural stone, and upholstery with absolute fidelity—just like luxury hotel standards.</li>
</ul>
<img class="product-img" src="{b64_della}" alt="DELLA 2.0 Architectural Downlight">

<p><strong>Why partnering with Encore strengthens Infinite Lighting's wholesale &amp; project business:</strong></p>
<ul>
  <li><strong>Low MOQ &amp; Fast Couriered Samples</strong>: Inspect physical samples and test build quality directly at your MC Home Depot or QC showroom.</li>
  <li><strong>Complete Marketing Assets</strong>: Free high-resolution photos, dimension CADs, specification sheets, and IES photometric files ready for your website and sales team.</li>
  <li><strong>Competitive Direct Factory Pricing</strong>: Healthy distributor margins for both retail sales and large contractor supply packages.</li>
</ul>

<p><strong>Would you be open to receiving our complete 2026 Architectural Catalog (PDF) and a sample pricing breakdown for your showrooms?</strong></p>

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

html_path = 'D:/marketing/开发信Word库_完整版/Encore_Infinite_Lighting菲律宾专属定制提案(网页一键复制版).html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated Infinite HTML successfully at:', html_path)

# DOCX
doc = Document()
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

title_p = doc.add_paragraph()
title_run = title_p.add_run("Subject: Factory-direct 48V magnetic tracks & architectural cylinders for Infinite Lighting (MC Home Depot & QC)")
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

add_p('Hi Team Infinite Lighting,')
add_p('I came across your showrooms on Instagram (@infinitelightingph) and explored your online store at infinitelighting.ph. Really impressive range—especially your presence at MC Home Depot Taguig and your Quezon City main branch.')
add_p('I noticed that while you have an exquisite collection of luxury chandeliers, your catalog also features Magnetic Track Light, Linear Lights, and Aluminum Profiles. With Philippine interior designers increasingly pairing decorative statement chandeliers with clean, low-glare architectural lighting, reliable factory supply on magnetic tracks and minimalist pendants is critical for project fulfillment.')
add_p('We are a direct commercial and architectural lighting manufacturer based in Shenzhen, China (Encore Commercial Lighting). We supply premier lighting showrooms and distributors across Southeast Asia. Here are 4 curated product lines that perfectly complement Infinite Lighting\'s high-end portfolio:')

add_heading('1. 48V Ultra-Slim Magnetic Track Platform with 3D Spatial Corners', 'Designer Essential Architectural System')
add_bullet('Complete Track Profiles', 'Trimless recessed, surface-mounted, and suspended slim rails that integrate seamlessly into ceiling slots and turn 3D corners onto walls.')
add_bullet('Versatile Click-in Modules', 'Magnetic accent spots, continuous linear diffusers, darklight gratings, and drop pendants—swapped tool-free in seconds.')
add_bullet('Safe & Stable', '48V low voltage with premium copper busbars preventing flickering and voltage drops across long runs.')
add_img(dst_mag)

add_heading('2. NOVA Ultra-Slim Architectural Pendant & Surface Cylinders (Φ30mm / Φ45mm)', 'Sculptural Decorative Minimalism')
add_bullet('Invisible Retractable Wire Lock', 'Zero visible screws or bulky top fittings—a seamless floating metal cylinder for dining tables and kitchen islands.')
add_bullet('Luxury Finishes', 'Anodized Champagne Gold, Deep Matte Black, and Architectural White to match luxury hardware.')
add_bullet('Visual Comfort (UGR < 6)', 'Deeply recessed optical baffle delivers comfortable illumination without harsh glare.')
add_img(dst_nova)

add_heading('3. FLEX Foldable & Zoomable Geometric Spotlight', 'Dual Aesthetic State')
add_bullet('Transformative Design', 'Flushes as a sleek architectural ceiling block, or tilts 90° and rotates 360° to highlight featured artwork or furniture displays.')
add_bullet('Zero-Sag Precision Joint', 'Holds any sculptured angle permanently without loosening or drooping.')
add_bullet('Tool-Free Beam Zooming', 'Rotate the front ring on-site to zoom between accent spot and wide wash.')
add_img(dst_flex)

add_heading('4. DELLA 2.0 Architectural Anti-Glare Downlight Series', 'High-CRI Darklight Foundation')
add_bullet('True Darklight Effect (UGR < 10 & Pinhole UGR < 6)', 'Provides rich, warm pools of light while keeping ceilings visually dark and unobtrusive.')
add_bullet('CRI 95+ (R9 > 80)', 'Renders rich wood grains, natural stone, and upholstery with absolute fidelity—just like luxury hotel standards.')
add_img(dst_della)

add_p('Why partnering with Encore strengthens Infinite Lighting\'s wholesale & project business:', bold=True)
add_bullet('Low MOQ & Fast Couriered Samples', 'Inspect physical samples and test build quality directly at your MC Home Depot or QC showroom.')
add_bullet('Complete Marketing Assets', 'Free high-resolution photos, dimension CADs, specification sheets, and IES photometric files ready for your website and sales team.')
add_bullet('Competitive Direct Factory Pricing', 'Healthy distributor margins for both retail sales and large contractor supply packages.')

add_p('Would you be open to receiving our complete 2026 Architectural Catalog (PDF) and a sample pricing breakdown for your showrooms?', bold=True)

sig_p = doc.add_paragraph()
sig_p.paragraph_format.space_before = Pt(16)
sig_run = sig_p.add_run('Best regards,\n\nBob\nEncore Commercial Lighting\nWeb: encore-tech.com\nEmail: sales21@encore-tech.com\nWhatsApp: +852 57651719')
sig_run.font.name = 'Segoe UI'
sig_run.font.size = Pt(10)
sig_run.font.color.rgb = RGBColor(71, 85, 105)

docx_path = 'D:/marketing/开发信Word库_完整版/Encore_Infinite_Lighting菲律宾专属定制提案(图文版).docx'
doc.save(docx_path)
print('Generated Infinite DOCX successfully at:', docx_path)
