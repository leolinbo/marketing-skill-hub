# -*- coding: utf-8 -*-
import os
import base64
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

img_dir = r"D:\marketing\开发信Word库_完整版\Favix_Technology_回信配套图片"
img1_p = os.path.join(img_dir, "1_Encore_Linear_Catalogue_Cover.jpg")
img2_p = os.path.join(img_dir, "2_Encore_Slim_Linear_System.jpg")
img3_p = os.path.join(img_dir, "photo_IMG_0419.JPG")
img4_p = os.path.join(img_dir, "3_Encore_Linear_Detail.jpg")

def b64(p):
    with open(p, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

b64_1 = b64(img1_p)
b64_2 = b64(img2_p)
b64_3 = b64(img3_p)
b64_4 = b64(img4_p)

# Build HTML
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Encore Lighting - Response to Favix Technology Ltd</title>
<style>
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    color: #1e293b;
    line-height: 1.6;
    max-width: 680px;
    margin: 20px auto;
    padding: 24px 28px;
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.04);
  }}
  .subject-box {{
    background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
    border-left: 4px solid #0284c7;
    padding: 12px 16px;
    margin-bottom: 24px;
    border-radius: 4px;
    font-size: 14.5px;
    color: #0369a1;
    font-weight: 600;
  }}
  .subject-box span {{
    color: #0f172a;
    font-weight: 700;
  }}
  h3 {{
    color: #0f172a;
    font-size: 16px;
    margin-top: 26px;
    margin-bottom: 10px;
    padding-bottom: 4px;
    border-bottom: 1px solid #f1f5f9;
  }}
  p {{
    font-size: 14px;
    margin-top: 0;
    margin-bottom: 12px;
    color: #334155;
  }}
  ul {{
    margin-top: 6px;
    margin-bottom: 16px;
    padding-left: 20px;
  }}
  li {{
    font-size: 13.5px;
    color: #334155;
    margin-bottom: 6px;
    line-height: 1.5;
  }}
  li strong {{
    color: #0f172a;
  }}
  .product-img {{
    display: block;
    max-width: 100%;
    height: auto;
    margin: 14px auto 6px auto;
    border-radius: 8px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  }}
  .caption {{
    text-align: center;
    font-size: 12px;
    color: #64748b;
    font-style: italic;
    margin-bottom: 18px;
  }}
  .highlight-card {{
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 14px 18px;
    margin: 16px 0;
  }}
  .highlight-card h4 {{
    margin: 0 0 8px 0;
    font-size: 14px;
    color: #0369a1;
  }}
  .signature {{
    margin-top: 32px;
    border-top: 1px solid #e2e8f0;
    padding-top: 16px;
    font-size: 13.5px;
    color: #475569;
    line-height: 1.6;
  }}
  .signature strong {{
    color: #0f172a;
    font-size: 15px;
  }}
  .cta-box {{
    background-color: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 8px;
    padding: 14px 18px;
    margin-top: 22px;
    color: #166534;
    font-size: 14px;
  }}
</style>
</head>
<body>

<div class="subject-box">
  Subject: <span>Re: Product Line Card &amp; Latest Catalogues: Under-Cabinet Slim Linear &amp; Rechargeable Series (Encore Lighting)</span>
</div>

<p>Hi Siamand,</p>

<p>Thank you for getting back to me, and thanks to your Instagram team for making the introduction! It is great to connect with you and <strong>Favix Technology</strong>.</p>

<p>We are very familiar with Favix's focus on practical, wire-free, and easy-to-install lighting solutions across the UK market. As an engineering-driven commercial and architectural LED lighting manufacturer based in Shenzhen (with our HK international office), we specialize in high-efficiency slim linear systems, modular magnetic track lights, and wire-free sensor fixtures built specifically for trade and direct retail distribution.</p>

<p>Below is an overview of our latest catalogues and direct solutions tailored to your two core inquiries:</p>

<h3>1. Latest Catalogues &amp; Product Line Card Overview</h3>
<p>We have released our full <strong>2025–2026 Architectural Lighting Collection</strong>, featuring high-CRI optics (Ra &gt; 95, SDCM &lt; 3) and contractor-friendly mounting systems:</p>
<ul>
  <li><strong>Linear Light Systems &amp; Cylinders Catalogue</strong>: Continuous slim profiles, under-cabinet modular tracks, and low-glare architectural diffusers.</li>
  <li><strong>48V Magnetic Track Light Catalogue</strong>: Ultra-slim 15mm/20mm profiles with magnetic snap-in linear and spotlight inserts.</li>
  <li><strong>Architectural Downlight &amp; Commercial Range</strong>: Deep anti-glare museum-grade optics (UGR &lt; 10).</li>
</ul>

<img class="product-img" src="data:image/jpeg;base64,{b64_1}" alt="Encore Linear Light System Catalogue Cover" style="max-width: 580px;">
<div class="caption">[Encore 2025–2026 Edition: Architectural Linear &amp; Cylinder Catalogue]</div>

<h3>2. Under-Cabinet Slim Linear Range: ATRO &amp; Modular Micro-Profiles</h3>
<p>To eliminate bulky installations and unsightly driver boxes under kitchen cabinetry, wardrobes, and retail shelving, our under-cabinet slim linear fixtures feature:</p>
<ul>
  <li><strong>Ultra-Slim Low-Profile Extrusion</strong>: Height as thin as 8mm to 12mm, providing seamless concealment under cabinetry without visible hardware.</li>
  <li><strong>Dotless Diffused Illumination (UGR &lt; 16)</strong>: High-transmittance opal PC cover paired with high-density LED arrays (120–140 lm/W), ensuring smooth, uniform light without diode spotting on polished countertops.</li>
  <li><strong>Color Consistency &amp; CCT Selection</strong>: CRI 95+, R9 &gt; 80, available in switchable 2700K / 3000K / 4000K to suit diverse British residential and hospitality palettes.</li>
  <li><strong>Plug-and-Play Quick Linking</strong>: Male/female micro-couplers allowing continuous daisy-chain runs up to 4 meters from a single slimline power feed.</li>
</ul>

<img class="product-img" src="data:image/jpeg;base64,{b64_2}" alt="Encore Slim Linear System Specifications">
<div class="caption">[Slim Linear System: Continuous Splicing, Wide Flood &amp; Multiple Mounting Options]</div>

<h3>3. Rechargeable &amp; Battery-Powered Wire-Free Series</h3>
<p>Recognizing Favix’s emphasis on wire-free installation where mains wiring is impractical, we have engineered dedicated rechargeable lithium fixtures:</p>
<div class="highlight-card">
  <h4>Key Engineering Highlights for Favix Wire-Free Line:</h4>
  <ul>
    <li><strong>Dual PIR &amp; Daylight Sensor</strong>: 120° wide-angle human motion sensing (3-meter detection range) with built-in ambient light detection. 3 operational modes: <em>Always-On</em>, <em>Night Auto-Sensor</em>, and <em>Off</em>.</li>
    <li><strong>High-Density Li-ion Battery &amp; Fast USB-C</strong>: Built-in 1,500mAh to 3,000mAh rechargeable lithium cells providing 60 to 90 days of normal usage (approx. 8–10 sensor activations daily) on a single 1.5-hour charge.</li>
    <li><strong>Magnetic Snap-On Base</strong>: Heavy-duty 3M adhesive magnetic mounting plate—simply snap off for effortless Type-C recharging without removing brackets.</li>
    <li><strong>Full UKCA / CE / RoHS Certification</strong>: UN38.3 &amp; MSDS battery safety compliance, fully cleared for UK imports and retail distribution.</li>
  </ul>
</div>

<img class="product-img" src="data:image/jpeg;base64,{b64_3}" alt="Factory Optical &amp; Profile Testing">
<div class="caption">[Encore Production &amp; Optical Precision: Robust Aluminum Extrusion &amp; Rigorous QC]</div>

<h3>4. Direct Factory Advantage for Favix Technology (UK)</h3>
<ul>
  <li><strong>Direct Air Express to Solihull / UK</strong>: Quick sample turnaround in 3–5 business days via DHL/FedEx directly to your facility in Solihull or trade partners.</li>
  <li><strong>Custom OEM / Private Label</strong>: Tailored laser-etched Favix branding, bespoke packaging, barcode labeling, and UKCA compliant user guides.</li>
  <li><strong>Flexible Order Quantities</strong>: Low-friction trial batch support to facilitate your trade catalog onboarding and direct customer promotions.</li>
</ul>

<img class="product-img" src="data:image/jpeg;base64,{b64_4}" alt="One-Step Splicing &amp; Assembly Reliability">
<div class="caption">[Patented Quick Splicing &amp; Mounting Kits for Flawless On-Site Alignment]</div>

<div class="cta-box">
  <strong>Next Steps &amp; Sample Evaluation:</strong><br>
  I would be delighted to send across our complete PDF spec sheets and arrange a tailored <strong>sample evaluation kit</strong> (including our under-cabinet slim linear section and rechargeable sensor unit) for your team to test hands-on.<br><br>
  <strong>Could you let me know your preferred lengths (e.g. 300mm, 500mm, 1000mm) and whether you would like the sample pack dispatched to your Solihull office this week?</strong>
</div>

<div class="signature">
  Best regards,<br><br>
  <strong>Bob</strong><br>
  B2B Export &amp; Engineering Division<br>
  <strong>Encore Commercial Lighting</strong><br>
  Website: <a href="https://encore-tech.com" target="_blank" style="color: #0284c7; text-decoration: none;">www.encore-tech.com</a><br>
  Email: <a href="mailto:sales@encore-tech.com" style="color: #0284c7; text-decoration: none;">sales@encore-tech.com</a><br>
  Mobile / WhatsApp: <strong>+852 6768 2519</strong><br>
  <em>HK HQ: Tsim Sha Tsui, KL | Factory: Zhengzhong Industrial Park, Bao'an, Shenzhen</em>
</div>

</body>
</html>
"""

out_html_path = r"D:\marketing\开发信Word库_完整版\Encore_Favix_Technology_回信提案(网页一键复制版).html"
with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("SUCCESS: HTML saved to", out_html_path)

# Build Word Doc
doc = docx.Document()
for s in doc.sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

p_subj = doc.add_paragraph()
r_s1 = p_subj.add_run("Subject: ")
r_s1.bold = True
r_s1.font.color.rgb = RGBColor(3, 105, 161)
r_s2 = p_subj.add_run("Re: Product Line Card & Latest Catalogues: Under-Cabinet Slim Linear & Rechargeable Series (Encore Lighting)")
r_s2.bold = True

p_g = doc.add_paragraph("Hi Siamand,")
p_t1 = doc.add_paragraph("Thank you for getting back to me, and thanks to your Instagram team for making the introduction! Great to connect with you and Favix Technology.")
p_t2 = doc.add_paragraph("We are very familiar with Favix's focus on practical, wire-free, and easy-to-install lighting solutions across the UK market. As an engineering-driven commercial and architectural LED lighting manufacturer based in Shenzhen, we specialize in high-efficiency slim linear systems, modular magnetic track lights, and wire-free sensor fixtures built specifically for trade and direct retail distribution.")

# H1
h1 = doc.add_heading("1. Latest Catalogues & Product Line Card Overview", level=3)
doc.add_paragraph("We have released our full 2025–2026 Architectural Lighting Collection, featuring high-CRI optics (Ra > 95, SDCM < 3) and contractor-friendly mounting systems:")
for b in [
    "Linear Light Systems & Cylinders Catalogue: Continuous slim profiles, under-cabinet modular tracks, and low-glare architectural diffusers.",
    "48V Magnetic Track Light Catalogue: Ultra-slim 15mm/20mm profiles with magnetic snap-in linear and spotlight inserts.",
    "Architectural Downlight & Commercial Range: Deep anti-glare museum-grade optics (UGR < 10)."
]:
    doc.add_paragraph(b, style="List Bullet")

p_im1 = doc.add_paragraph()
p_im1.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_im1.add_run().add_picture(img1_p, width=Inches(4.5))
p_c1 = doc.add_paragraph("[Encore 2025–2026 Edition: Architectural Linear & Cylinder Catalogue]")
p_c1.alignment = WD_ALIGN_PARAGRAPH.CENTER

# H2
h2 = doc.add_heading("2. Under-Cabinet Slim Linear Range: ATRO & Modular Micro-Profiles", level=3)
doc.add_paragraph("To eliminate bulky installations and unsightly driver boxes under kitchen cabinetry, wardrobes, and retail shelving:")
for b in [
    "Ultra-Slim Low-Profile Extrusion: Height as thin as 8mm to 12mm, providing seamless concealment under cabinetry without visible hardware.",
    "Dotless Diffused Illumination (UGR < 16): High-transmittance opal PC cover paired with high-density LED arrays (120–140 lm/W), ensuring smooth, uniform light without diode spotting.",
    "Color Consistency & CCT Selection: CRI 95+, R9 > 80, available in switchable 2700K / 3000K / 4000K.",
    "Plug-and-Play Quick Linking: Male/female micro-couplers allowing continuous daisy-chain runs up to 4 meters."
]:
    doc.add_paragraph(b, style="List Bullet")

p_im2 = doc.add_paragraph()
p_im2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_im2.add_run().add_picture(img2_p, width=Inches(4.5))
p_c2 = doc.add_paragraph("[Slim Linear System: Continuous Splicing, Wide Flood & Mounting Options]")
p_c2.alignment = WD_ALIGN_PARAGRAPH.CENTER

# H3
h3 = doc.add_heading("3. Rechargeable & Battery-Powered Wire-Free Series", level=3)
doc.add_paragraph("Recognizing Favix’s emphasis on wire-free installation where mains wiring is impractical:")
for b in [
    "Dual PIR & Daylight Sensor: 120° wide-angle motion detection (3m range) with 3 modes (Always-On, Auto-Sensor, Off).",
    "High-Density Li-ion Battery & Fast USB-C: 1,500mAh to 3,000mAh lithium cells providing 60 to 90 days of normal usage on a single 1.5-hour charge.",
    "Magnetic Snap-On Base: 3M adhesive magnetic mounting plate—simply snap off for effortless Type-C recharging.",
    "Full UKCA / CE / RoHS Certification: UN38.3 & MSDS battery safety compliance."
]:
    doc.add_paragraph(b, style="List Bullet")

p_im3 = doc.add_paragraph()
p_im3.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_im3.add_run().add_picture(img3_p, width=Inches(4.5))
p_c3 = doc.add_paragraph("[Encore Production & Optical Precision: Robust Aluminum Extrusion & Rigorous QC]")
p_c3.alignment = WD_ALIGN_PARAGRAPH.CENTER

# H4
h4 = doc.add_heading("4. Direct Factory Advantage for Favix Technology (UK)", level=3)
for b in [
    "Direct Air Express to Solihull / UK: Quick sample turnaround in 3–5 business days via DHL/FedEx.",
    "Custom OEM / Private Label: Tailored laser-etched Favix branding, bespoke packaging, and UKCA compliant user guides.",
    "Flexible Order Quantities: Low-friction trial batch support to facilitate your trade catalog onboarding."
]:
    doc.add_paragraph(b, style="List Bullet")

p_im4 = doc.add_paragraph()
p_im4.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_im4.add_run().add_picture(img4_p, width=Inches(4.5))
p_c4 = doc.add_paragraph("[Patented Quick Splicing & Mounting Kits for Flawless Alignment]")
p_c4.alignment = WD_ALIGN_PARAGRAPH.CENTER

p_cta = doc.add_paragraph("Next Steps & Sample Evaluation:\nI would be delighted to send across our complete PDF spec sheets and arrange a tailored sample evaluation kit (including our under-cabinet slim linear section and rechargeable sensor unit) for your team to test hands-on.\nCould you let me know your preferred lengths (e.g. 300mm, 500mm, 1000mm) and whether you would like the sample pack dispatched to your Solihull office this week?")

p_sig = doc.add_paragraph("\nBest regards,\nBob\nB2B Export & Engineering Division\nEncore Commercial Lighting\nWebsite: www.encore-tech.com\nEmail: sales@encore-tech.com\nMobile / WhatsApp: +852 6768 2519")

out_docx_path = r"D:\marketing\开发信Word库_完整版\Encore_Favix_Technology_回信提案(图文版).docx"
doc.save(out_docx_path)
print("SUCCESS: Docx saved to", out_docx_path)
