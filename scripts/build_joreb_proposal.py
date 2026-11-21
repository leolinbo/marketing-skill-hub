# -*- coding: utf-8 -*-
import os
import base64
import docx
from PIL import Image
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# 1. Images preparation
della_raw_img = r'D:\marketing\assets\products\DELLA\DELLA 2.0 Downlight Mail Group-Choco-V0-20260709_image1.png'
magnetic_raw_img = r'D:\marketing\assets\products\MAGNETIC\48V magnetic track system_EU AU Middle East market-Selena_image1.png'
nova_raw_img = r'D:\marketing\assets\products\NOVA\NOVA Cylinder Mail Group-Choco-V0-20260825_image1.png'

out_img_dir = r'D:\marketing\开发信Word库_完整版\Joreb_Design_提案配套图片'
os.makedirs(out_img_dir, exist_ok=True)

def optimize_img(src_p, dst_name):
    im = Image.open(src_p)
    if im.width > 650:
        h = int(im.height * (650 / im.width))
        im = im.resize((650, h), Image.Resampling.LANCZOS)
    dst_p = os.path.join(out_img_dir, dst_name)
    im.convert('RGB').save(dst_p, 'JPEG', quality=88)
    return dst_p

img1_p = optimize_img(della_raw_img, '1_DELLA_Architectural_Downlight.jpg')
img2_p = optimize_img(magnetic_raw_img, '2_48V_Magnetic_Track_System.jpg')
img3_p = optimize_img(nova_raw_img, '3_NOVA_Slim_Cylinder.jpg')

# 2. Build Word Document
doc = docx.Document()
for s in doc.sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

# Subject
p_subj = doc.add_paragraph()
p_subj.paragraph_format.space_after = Pt(12)
r_sl = p_subj.add_run("Subject: ")
r_sl.bold = True
r_sl.font.size = Pt(11)
r_sl.font.color.rgb = RGBColor(3, 105, 161)
r_st = p_subj.add_run("Architectural lighting for Joreb Design's bungalow & residential projects (Encore)")
r_st.bold = True
r_st.font.size = Pt(11)

# Greeting
p_g = doc.add_paragraph()
p_g.paragraph_format.space_after = Pt(8)
p_g.add_run("Hi Joreb Team,").font.size = Pt(10.5)

# Intro
p_i1 = doc.add_paragraph()
p_i1.paragraph_format.space_after = Pt(8)
p_i1.add_run("I recently went through your interior design and visualization portfolio—really impressed by the refined lighting mood and spatial balance across your Bungalow Interior Design and Townhouse projects.").font.size = Pt(10.5)

p_i2 = doc.add_paragraph()
p_i2.paragraph_format.space_after = Pt(10)
p_i2.add_run("When translating high-end 3D renderings into built reality, the biggest challenge is often finding fixtures that achieve that exact 'dark-light' visual comfort (seeing the warm light pool without glare from the ceiling).").font.size = Pt(10.5)

p_i3 = doc.add_paragraph()
p_i3.paragraph_format.space_after = Pt(12)
p_i3.add_run("We are an engineering-driven commercial lighting manufacturer based in Shenzhen, China (Encore Commercial Lighting). Based on the architectural language in your portfolio, here are 3 matching fixture families we regularly supply to interior design studios:").font.size = Pt(10.5)

# Section 1: DELLA 2.0
p_h1 = doc.add_paragraph()
p_h1.paragraph_format.space_before = Pt(8)
p_h1.paragraph_format.space_after = Pt(4)
r_h1 = p_h1.add_run("1. For Your Bungalow & Multi-Storey Residences: DELLA 2.0 Architectural Downlights")
r_h1.bold = True
r_h1.font.size = Pt(10.5)
r_h1.font.color.rgb = RGBColor(26, 54, 93)

p_b1_1 = doc.add_paragraph(style='List Bullet')
p_b1_1.paragraph_format.space_after = Pt(2)
p_b1_1.add_run("Ultra-Deep Anti-Glare (UGR < 10 & Pinhole UGR < 6): Keeps ceilings visually quiet and dark from normal angles, eliminating glare.").font.size = Pt(10)

p_b1_2 = doc.add_paragraph(style='List Bullet')
p_b1_2.paragraph_format.space_after = Pt(2)
p_b1_2.add_run("Modular Bezel System: One core LED engine adapts to fixed downlights, 30° adjustable accents, and wall-washers for art walls.").font.size = Pt(10)

p_b1_3 = doc.add_paragraph(style='List Bullet')
p_b1_3.paragraph_format.space_after = Pt(8)
p_b1_3.add_run("True Color Rendering: CRI 95+, 2700K / 3000K, ensuring wood grains, fabrics, and natural stone look rich and authentic.").font.size = Pt(10)

p_img1 = doc.add_paragraph()
p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_img1.paragraph_format.space_after = Pt(12)
p_img1.add_run().add_picture(img1_p, width=Inches(4.2))

# Section 2: Magnetic 48V
p_h2 = doc.add_paragraph()
p_h2.paragraph_format.space_before = Pt(8)
p_h2.paragraph_format.space_after = Pt(4)
r_h2 = p_h2.add_run("2. For Modern Townhouse & Office Spaces: 48V Low-Voltage Magnetic Track System")
r_h2.bold = True
r_h2.font.size = Pt(10.5)
r_h2.font.color.rgb = RGBColor(26, 54, 93)

p_b2_1 = doc.add_paragraph(style='List Bullet')
p_b2_1.paragraph_format.space_after = Pt(2)
p_b2_1.add_run("Tool-Free Modularity: Snap-in micro-spots, linear diffuse wash, and folding accent lights for seamless ceiling lines.").font.size = Pt(10)

p_b2_2 = doc.add_paragraph(style='List Bullet')
p_b2_2.paragraph_format.space_after = Pt(2)
p_b2_2.add_run("Dual Safety Mechanism: Magnetic attraction paired with quick-release mechanical locking for zero maintenance hassle.").font.size = Pt(10)

p_b2_3 = doc.add_paragraph(style='List Bullet')
p_b2_3.paragraph_format.space_after = Pt(8)
p_b2_3.add_run("Precision Dimming: Smooth 0-10V, DALI-2, and wireless Casambi app control.").font.size = Pt(10)

p_img2 = doc.add_paragraph()
p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_img2.paragraph_format.space_after = Pt(12)
p_img2.add_run().add_picture(img2_p, width=Inches(4.2))

# Section 3: NOVA
p_h3 = doc.add_paragraph()
p_h3.paragraph_format.space_before = Pt(8)
p_h3.paragraph_format.space_after = Pt(4)
r_h3 = p_h3.add_run("3. For Kitchen Islands & Dining Areas: NOVA Slim Architectural Cylinders")
r_h3.bold = True
r_h3.font.size = Pt(10.5)
r_h3.font.color.rgb = RGBColor(26, 54, 93)

p_b3_1 = doc.add_paragraph(style='List Bullet')
p_b3_1.paragraph_format.space_after = Pt(2)
p_b3_1.add_run("Clean Canopy Transition: Flawless ceiling integration with zero exposed screws or bulky fasteners.").font.size = Pt(10)

p_b3_2 = doc.add_paragraph(style='List Bullet')
p_b3_2.paragraph_format.space_after = Pt(8)
p_b3_2.add_run("UGR < 6 Deep Shielding: Direct warm accentuation on table tops while remaining completely comfortable to look at.").font.size = Pt(10)

p_img3 = doc.add_paragraph()
p_img3.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_img3.paragraph_format.space_after = Pt(12)
p_img3.add_run().add_picture(img3_p, width=Inches(4.2))

# Offer & Close
p_c1 = doc.add_paragraph()
p_c1.paragraph_format.space_after = Pt(8)
p_c1.add_run("We provide free IES photometric files and 3D lighting asset data to help design studios achieve seamless visualization rendering and lighting calculation.").font.size = Pt(10.5)

p_c2 = doc.add_paragraph()
p_c2.paragraph_format.space_after = Pt(14)
r_c2 = p_c2.add_run("If you have any ongoing residential or office interiors currently in development, we’d love to courier a sample kit to your studio or quote directly from your CAD layouts. Open to taking a look?")
r_c2.bold = True
r_c2.font.size = Pt(10.5)

# Sign-off
p_sign = doc.add_paragraph()
p_sign.add_run("Best regards,\n\n").font.size = Pt(10)
r_bob = p_sign.add_run("Bob\n")
r_bob.bold = True
r_bob.font.size = Pt(10.5)
p_sign.add_run("Encore Commercial Lighting\nWeb: encore-tech.com\nWhatsApp: +852 57651719\nEmail: jorebdesign contact follow-up").font.size = Pt(10)

docx_path = r"D:\marketing\开发信Word库_完整版\Encore_Joreb_Design专属定制设计提案(图文版).docx"
doc.save(docx_path)
print("SUCCESS: Docx saved to", docx_path)

# 3. Build HTML Copy-Paste Version
def b64(p):
    with open(p, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

b64_1 = b64(img1_p)
b64_2 = b64(img2_p)
b64_3 = b64(img3_p)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Encore Lighting - Proposal for Joreb Design</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; line-height: 1.6; max-width: 650px; margin: 20px auto; padding: 20px; border: 1px solid #e2e8f0; border-radius: 8px; }}
.subject-box {{ background-color: #f0f9ff; border-left: 4px solid #0284c7; padding: 10px 14px; margin-bottom: 20px; font-weight: bold; color: #0369a1; }}
h3 {{ color: #1a365d; margin-top: 24px; margin-bottom: 8px; font-size: 15px; }}
ul {{ margin-top: 4px; padding-left: 20px; }}
li {{ margin-bottom: 6px; font-size: 14px; }}
.product-img {{ display: block; max-width: 100%; height: auto; margin: 14px auto 14px auto; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
.signature {{ margin-top: 28px; border-top: 1px solid #e2e8f0; padding-top: 14px; font-size: 14px; color: #475569; }}
.signature strong {{ color: #0f172a; font-size: 15px; }}
</style>
</head>
<body>

<div class="subject-box">
Subject: Architectural lighting for Joreb Design's bungalow & residential projects (Encore)
</div>

<p>Hi Joreb Team,</p>

<p>I recently went through your interior design and visualization portfolio—really impressed by the refined lighting mood and spatial balance across your <strong>Bungalow Interior Design</strong> and <strong>Townhouse projects</strong>.</p>

<p>When translating high-end 3D renderings into built reality, the biggest challenge is often finding fixtures that achieve that exact "dark-light" visual comfort (seeing the warm light pool without glare from the ceiling).</p>

<p>We are an engineering-driven commercial lighting manufacturer based in Shenzhen, China (Encore Commercial Lighting). Based on the architectural language in your portfolio, here are 3 matching fixture families we regularly supply to interior design studios:</p>

<h3>1. For Your Bungalow & Multi-Storey Residences: DELLA 2.0 Architectural Downlights</h3>
<ul>
  <li><strong>Ultra-Deep Anti-Glare (UGR &lt; 10 &amp; Pinhole UGR &lt; 6)</strong>: Keeps ceilings visually quiet and dark from normal angles, eliminating glare.</li>
  <li><strong>Modular Bezel System</strong>: One core LED engine adapts to fixed downlights, 30° adjustable accents, and wall-washers for art walls.</li>
  <li><strong>True Color Rendering (CRI 95+)</strong>: 2700K / 3000K options, ensuring wood grains, fabrics, and natural stone look rich and authentic.</li>
</ul>
<img class="product-img" src="data:image/jpeg;base64,{b64_1}" alt="DELLA Architectural Downlight System">

<h3>2. For Modern Townhouse & Office Spaces: 48V Low-Voltage Magnetic Track System</h3>
<ul>
  <li><strong>Tool-Free Modularity</strong>: Snap-in micro-spots, linear diffuse wash, and folding accent lights for seamless ceiling lines.</li>
  <li><strong>Dual Safety Mechanism</strong>: Magnetic attraction paired with quick-release mechanical locking for zero maintenance hassle.</li>
  <li><strong>Precision Dimming</strong>: Smooth 0-10V, DALI-2, and wireless Casambi app control.</li>
</ul>
<img class="product-img" src="data:image/jpeg;base64,{b64_2}" alt="48V Magnetic Track System">

<h3>3. For Kitchen Islands & Dining Areas: NOVA Slim Architectural Cylinders</h3>
<ul>
  <li><strong>Clean Canopy Transition</strong>: Flawless ceiling integration with zero exposed screws or bulky fasteners.</li>
  <li><strong>UGR &lt; 6 Deep Shielding</strong>: Direct warm accentuation on table tops while remaining completely comfortable to look at.</li>
</ul>
<img class="product-img" src="data:image/jpeg;base64,{b64_3}" alt="NOVA Slim Cylinder">

<p>We provide free IES photometric files and 3D lighting asset data to help design studios achieve seamless visualization rendering and lighting calculation.</p>

<p><strong>If you have any ongoing residential or office interiors currently in development, we’d love to courier a sample kit to your studio or quote directly from your CAD layouts. Open to taking a look?</strong></p>

<div class="signature">
  Best regards,<br><br>
  <strong>Bob</strong><br>
  Encore Commercial Lighting<br>
  Web: <a href="https://encore-tech.com">encore-tech.com</a><br>
  WhatsApp: +852 57651719
</div>

</body>
</html>
"""

html_path = r"D:\marketing\开发信Word库_完整版\Encore_Joreb_Design专属定制设计提案(网页一键复制版).html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("SUCCESS: HTML saved to", html_path)
