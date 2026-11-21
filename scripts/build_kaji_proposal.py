# -*- coding: utf-8 -*-
import os
import base64
import docx
from PIL import Image
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# 1. Process & Prepare Images
user_raw_img = r'C:/Users/HUAWEI/.gemini/antigravity/brain/2ea0abc2-e913-49a0-a32f-e6db00286799/.user_uploaded/media_1793858660385_f30ae5f0.jpg'
vega_raw_img = r'D:\marketing\assets\products\VEGA\Choco Mail Group-VEGA_image1.png'
evo_raw_img = r'D:\marketing\assets\products\EVO\EVO Track Light Mail Group-Choco-V0-20260722_image1.png'

out_img_dir = r'D:\marketing\开发信Word库_完整版\KAJI_Architects_询盘配套图片'
os.makedirs(out_img_dir, exist_ok=True)

def optimize_img(src_p, dst_name):
    im = Image.open(src_p)
    if im.width > 650:
        h = int(im.height * (650 / im.width))
        im = im.resize((650, h), Image.Resampling.LANCZOS)
    dst_p = os.path.join(out_img_dir, dst_name)
    im.convert('RGB').save(dst_p, 'JPEG', quality=88)
    return dst_p

img1_p = optimize_img(user_raw_img, '1_Your_Reference_Photo.jpg')
img2_p = optimize_img(vega_raw_img, '2_Encore_Suspended_Track_System.jpg')
img3_p = optimize_img(evo_raw_img, '3_Optical_Detail_and_Finish.jpg')

print("Images prepared successfully.")

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
r_st = p_subj.add_run("Regarding your Facebook inquiry: Suspended trackbar & minimalist spotlights (Encore Lighting)")
r_st.bold = True
r_st.font.size = Pt(11)

# Greeting
p_g = doc.add_paragraph()
p_g.paragraph_format.space_after = Pt(8)
p_g.add_run("Hi KAJI Architects Team,").font.size = Pt(10.5)

# Intro
p_i1 = doc.add_paragraph()
p_i1.paragraph_format.space_after = Pt(8)
p_i1.add_run("Saw your post on Facebook looking for a reliable supplier for suspended trackbar and cylindrical spotlights matching your reference photo.").font.size = Pt(10.5)

p_i2 = doc.add_paragraph()
p_i2.paragraph_format.space_after = Pt(10)
p_i2.add_run("We are an engineering-driven commercial lighting manufacturer based in Shenzhen, China (Encore Commercial Lighting). We specialize in exactly this clean, architectural suspended track aesthetic for boutique interiors, cafes, and modern residences.").font.size = Pt(10.5)

# Section 1: Comparison with photo
p_h1 = doc.add_paragraph()
p_h1.paragraph_format.space_before = Pt(8)
p_h1.paragraph_format.space_after = Pt(4)
r_h1 = p_h1.add_run("1. Exact Match to Your Reference Requirement")
r_h1.bold = True
r_h1.font.size = Pt(10.5)
r_h1.font.color.rgb = RGBColor(26, 54, 93)

p_b1 = doc.add_paragraph()
p_b1.paragraph_format.space_after = Pt(8)
p_b1.add_run("As shown in your reference image below, our architectural suspended system combines ultra-slim white/black track bars with heavy-duty stainless steel wire suspension kits (adjustable height from 1.0m to 3.0m).").font.size = Pt(10)

# Image 1 (User Reference)
p_img1 = doc.add_paragraph()
p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_img1.paragraph_format.space_after = Pt(4)
p_img1.add_run().add_picture(img1_p, width=Inches(3.8))

p_cap1 = doc.add_paragraph()
p_cap1.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap1.paragraph_format.space_after = Pt(12)
r_c1 = p_cap1.add_run("[Reference Photo from your Facebook post]")
r_c1.font.size = Pt(8.5)
r_c1.font.italic = True
r_c1.font.color.rgb = RGBColor(148, 163, 184)

# Section 2: Encore System Match
p_h2 = doc.add_paragraph()
p_h2.paragraph_format.space_before = Pt(8)
p_h2.paragraph_format.space_after = Pt(4)
r_h2 = p_h2.add_run("2. Our Matching Architectural Solution: Encore VEGA & EVO Track Series")
r_h2.bold = True
r_h2.font.size = Pt(10.5)
r_h2.font.color.rgb = RGBColor(26, 54, 93)

p_b2_1 = doc.add_paragraph(style='List Bullet')
p_b2_1.paragraph_format.space_after = Pt(2)
p_b2_1.add_run("Minimalist Cylindrical Spotlights: Compact architectural heads with concealed/flush adapters, eliminating bulky driver boxes on the track.").font.size = Pt(10)

p_b2_2 = doc.add_paragraph(style='List Bullet')
p_b2_2.paragraph_format.space_after = Pt(2)
p_b2_2.add_run("Deep Anti-Glare Optics (UGR < 12): Deep-regression reflector delivering high-intensity accent light without eye glare.").font.size = Pt(10)

p_b2_3 = doc.add_paragraph(style='List Bullet')
p_b2_3.paragraph_format.space_after = Pt(2)
p_b2_3.add_run("True Color Rendering: CRI 95+, 2700K / 3000K / 4000K, powered by Bridgelux / Citizen COBs for rich spatial textures.").font.size = Pt(10)

p_b2_4 = doc.add_paragraph(style='List Bullet')
p_b2_4.paragraph_format.space_after = Pt(8)
p_b2_4.add_run("Heavy-Duty Stainless Steel Suspension Kit: Seamless ceiling anchors with micro-adjustable aircraft cables for flawless alignment.").font.size = Pt(10)

# Image 2 (Encore Matching Real System)
p_img2 = doc.add_paragraph()
p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_img2.paragraph_format.space_after = Pt(4)
p_img2.add_run().add_picture(img2_p, width=Inches(4.2))

p_cap2 = doc.add_paragraph()
p_cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap2.paragraph_format.space_after = Pt(12)
r_c2 = p_cap2.add_run("[Encore Matching Solution: Clean In-Track Architectural Spotlight System]")
r_c2.font.size = Pt(8.5)
r_c2.font.italic = True
r_c2.font.color.rgb = RGBColor(148, 163, 184)

# Section 3: Delivery to Philippines
p_h3 = doc.add_paragraph()
p_h3.paragraph_format.space_before = Pt(8)
p_h3.paragraph_format.space_after = Pt(4)
r_h3 = p_h3.add_run("3. Direct Factory Supply to Angeles City / Clark")
r_h3.bold = True
r_h3.font.size = Pt(10.5)
r_h3.font.color.rgb = RGBColor(26, 54, 93)

p_b3_1 = doc.add_paragraph(style='List Bullet')
p_b3_1.paragraph_format.space_after = Pt(2)
p_b3_1.add_run("Fast Courier Delivery: Direct air express from our Shenzhen facility to Pampanga / Angeles City in just 3 to 5 business days.").font.size = Pt(10)

p_b3_2 = doc.add_paragraph(style='List Bullet')
p_b3_2.paragraph_format.space_after = Pt(2)
p_b3_2.add_run("Free Fixture Take-off & DIALux: Send us your floor plan or reflected ceiling layout, and we will calculate the exact track lengths and fixture quantities with a complete BOM quote within 24 hours.").font.size = Pt(10)

p_b3_3 = doc.add_paragraph(style='List Bullet')
p_b3_3.paragraph_format.space_after = Pt(8)
p_b3_3.add_run("Flexible Sample Order: We can dispatch sample track sections and spotlights right away for your client mock-up.").font.size = Pt(10)

# Image 3 (Detail)
p_img3 = doc.add_paragraph()
p_img3.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_img3.paragraph_format.space_after = Pt(4)
p_img3.add_run().add_picture(img3_p, width=Inches(4.2))

p_cap3 = doc.add_paragraph()
p_cap3.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap3.paragraph_format.space_after = Pt(12)
r_c3 = p_cap3.add_run("[Optical Reflector & Compact Architectural Body Details]")
r_c3.font.size = Pt(8.5)
r_c3.font.italic = True
r_c3.font.color.rgb = RGBColor(148, 163, 184)

# CTA
p_cta = doc.add_paragraph()
p_cta.paragraph_format.space_after = Pt(14)
r_cta = p_cta.add_run("What are the total track lengths and spotlight quantities required for your current project? Happy to review your drawings and provide direct factory pricing.")
r_cta.bold = True
r_cta.font.size = Pt(10.5)

# Sign-off
p_sign = doc.add_paragraph()
p_sign.add_run("Best regards,\n\n").font.size = Pt(10)
r_bob = p_sign.add_run("Bob\n")
r_bob.bold = True
r_bob.font.size = Pt(10.5)
p_sign.add_run("Encore Commercial Lighting\nWeb: encore-tech.com\nWhatsApp: +852 57651719\nEmail: encorelightingbob (via inquiry response)").font.size = Pt(10)

docx_path = r"D:\marketing\开发信Word库_完整版\Encore_KAJI_Architects悬吊轨道询盘报价提案(图文版).docx"
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
<title>Encore Lighting - Proposal for KAJI Architects</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; line-height: 1.6; max-width: 650px; margin: 20px auto; padding: 20px; border: 1px solid #e2e8f0; border-radius: 8px; }}
.subject-box {{ background-color: #f0f9ff; border-left: 4px solid #0284c7; padding: 10px 14px; margin-bottom: 20px; font-weight: bold; color: #0369a1; }}
h3 {{ color: #1a365d; margin-top: 24px; margin-bottom: 8px; font-size: 16px; }}
ul {{ margin-top: 4px; padding-left: 20px; }}
li {{ margin-bottom: 6px; font-size: 14px; }}
.product-img {{ display: block; max-width: 100%; height: auto; margin: 14px auto 6px auto; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
.caption {{ text-align: center; font-size: 12px; color: #94a3b8; font-style: italic; margin-bottom: 16px; }}
.signature {{ margin-top: 28px; border-top: 1px solid #e2e8f0; padding-top: 14px; font-size: 14px; color: #475569; }}
.signature strong {{ color: #0f172a; font-size: 15px; }}
</style>
</head>
<body>

<div class="subject-box">
Subject: Regarding your Facebook inquiry: Suspended trackbar & minimalist spotlights (Encore Lighting)
</div>

<p>Hi KAJI Architects Team,</p>

<p>Saw your post on Facebook looking for a reliable supplier for suspended trackbar and cylindrical spotlights matching your reference photo.</p>

<p>We are an engineering-driven commercial lighting manufacturer based in Shenzhen, China (Encore Commercial Lighting). We specialize in exactly this clean, architectural suspended track aesthetic for boutique interiors, cafes, and modern residences.</p>

<h3>1. Exact Match to Your Reference Requirement</h3>
<p>As shown in your reference image below, our architectural suspended system combines ultra-slim white/black track bars with heavy-duty stainless steel wire suspension kits (adjustable height from 1.0m to 3.0m).</p>

<img class="product-img" src="data:image/jpeg;base64,{b64_1}" alt="Your Reference Photo" style="max-width: 380px;">
<div class="caption">[Reference Photo from your Facebook post]</div>

<h3>2. Our Matching Architectural Solution: Encore VEGA & EVO Track Series</h3>
<ul>
  <li><strong>Minimalist Cylindrical Spotlights</strong>: Compact architectural heads with concealed/flush adapters, eliminating bulky driver boxes on the track.</li>
  <li><strong>Deep Anti-Glare Optics (UGR &lt; 12)</strong>: Deep-regression reflector delivering high-intensity accent light without eye glare.</li>
  <li><strong>True Color Rendering (CRI 95+)</strong>: Powered by Bridgelux / Citizen COBs (2700K / 3000K / 4000K) for rich interior textures.</li>
  <li><strong>Heavy-Duty Stainless Steel Suspension Kit</strong>: Seamless ceiling anchors with micro-adjustable aircraft cables for flawless alignment.</li>
</ul>

<img class="product-img" src="data:image/jpeg;base64,{b64_2}" alt="Encore Suspended Track System">
<div class="caption">[Encore Matching Solution: Clean In-Track Architectural Spotlight System]</div>

<h3>3. Direct Factory Supply to Angeles City / Clark</h3>
<ul>
  <li><strong>Fast Courier Delivery</strong>: Direct air express from our Shenzhen facility to Pampanga / Angeles City in just 3 to 5 business days.</li>
  <li><strong>Free Fixture Take-off &amp; DIALux</strong>: Send us your floor plan or reflected ceiling layout, and we will calculate the exact track lengths and fixture quantities with a complete BOM quote within 24 hours.</li>
  <li><strong>Flexible Sample Order</strong>: We can dispatch sample track sections and spotlights right away for your client mock-up.</li>
</ul>

<img class="product-img" src="data:image/jpeg;base64,{b64_3}" alt="Optical Details and Finish">
<div class="caption">[Optical Reflector &amp; Compact Architectural Body Details]</div>

<p><strong>What are the total track lengths and spotlight quantities required for your current project? Happy to review your drawings and provide direct factory pricing.</strong></p>

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

html_path = r"D:\marketing\开发信Word库_完整版\Encore_KAJI_Architects悬吊轨道询盘报价提案(网页一键复制版).html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("SUCCESS: HTML saved to", html_path)
