# -*- coding: utf-8 -*-
import os
import base64
from patchright.sync_api import sync_playwright

def get_base64_img(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
            ext = os.path.splitext(path)[1].lower().replace(".", "")
            if ext == "jpg": ext = "jpeg"
            return f"data:image/{ext};base64,{b64}"
    return ""

img_magnetic = get_base64_img(r"D:\marketing\assets\products\MAGNETIC\48V magnetic track system_EU AU Middle East market-Selena_image1.png")
img_della = get_base64_img(r"D:\marketing\assets\products\DELLA\DELLA 2.0 Downlight Mail Group-Choco-V0-20260709_image1.png")
img_nova = get_base64_img(r"D:\marketing\assets\products\NOVA\NOVA Cylinder Mail Group-Choco-V0-20260825_image1.png")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Architectural Lighting Proposal - ALTRON Indonesia</title>
<style>
  @page {{
    size: A4;
    margin: 18mm 16mm 18mm 16mm;
  }}
  body {{
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    line-height: 1.55;
    font-size: 13.5px;
    margin: 0;
    padding: 0;
    background: #ffffff;
  }}
  .header {{
    border-bottom: 2px solid #0f766e;
    padding-bottom: 12px;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }}
  .logo-text {{
    font-size: 20px;
    font-weight: 800;
    color: #0f766e;
    letter-spacing: 0.5px;
  }}
  .sub-logo {{
    font-size: 11px;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 1px;
  }}
  .meta-info {{
    text-align: right;
    font-size: 11px;
    color: #64748b;
  }}
  .target-badge {{
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    color: #166534;
    font-size: 12px;
    font-weight: 600;
    padding: 6px 12px;
    border-radius: 6px;
    margin-bottom: 16px;
  }}
  h1 {{
    font-size: 18px;
    color: #0f172a;
    margin: 0 0 10px 0;
    font-weight: 700;
  }}
  h2 {{
    font-size: 15px;
    color: #0f766e;
    margin: 22px 0 8px 0;
    border-left: 3.5px solid #0f766e;
    padding-left: 8px;
    font-weight: 700;
  }}
  p {{
    margin: 0 0 10px 0;
  }}
  .highlight {{
    color: #0f766e;
    font-weight: 600;
  }}
  .product-card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 14px;
    margin-bottom: 16px;
    page-break-inside: avoid;
  }}
  .product-title {{
    font-size: 14.5px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 6px;
  }}
  .specs-tag {{
    display: inline-block;
    background: #e0f2fe;
    color: #0369a1;
    font-size: 11px;
    font-weight: 600;
    padding: 2px 7px;
    border-radius: 4px;
    margin-right: 5px;
    margin-bottom: 8px;
  }}
  ul {{
    margin: 0;
    padding-left: 18px;
  }}
  li {{
    margin-bottom: 4px;
    color: #334155;
  }}
  .prod-img {{
    width: 100%;
    max-height: 180px;
    object-fit: cover;
    border-radius: 6px;
    margin-top: 10px;
    border: 1px solid #e2e8f0;
  }}
  .ecosystem-box {{
    background: #fefce8;
    border: 1px solid #fef08a;
    border-radius: 6px;
    padding: 10px 14px;
    margin: 16px 0;
    font-size: 12.5px;
    color: #713f12;
    page-break-inside: avoid;
  }}
  .footer-sig {{
    margin-top: 24px;
    padding-top: 14px;
    border-top: 1px solid #e2e8f0;
    font-size: 12px;
    color: #475569;
    display: flex;
    justify-content: space-between;
  }}
</style>
</head>
<body>

<div class="header">
  <div>
    <div class="logo-text">ENCORE LIGHTING</div>
    <div class="sub-logo">Commercial & Architectural Lighting Engineering</div>
  </div>
  <div class="meta-info">
    Project Ref: ENC-ID-2026-ALT<br>
    Batam Showroom Project Curation<br>
    Date: November 2026
  </div>
</div>

<div class="target-badge">
  📍 Prepared Exclusively for: <strong>ALTRON Indonesia</strong> (Ruko Pasir Putih A6 No. 88, Sadai, Bengkong, Batam)
</div>

<h1>Smart Architectural Lighting Hardware Integration</h1>
<p>
  Hi Team ALTRON Indonesia, following your showroom presence at Ruko Pasir Putih and your focus on premium residential & hospitality projects in Batam, we curated this dedicated hardware portfolio.
</p>
<p>
  Unlike residential consumer bulbs, <strong>Encore-Tech</strong> engineers museum-grade architectural luminaires designed for seamless hardware pairing with high-end control protocols—including <strong>Casambi Wireless, DALI-2, 0-10V, and Phase-cut (Triac)</strong>.
</p>

<div class="ecosystem-box">
  ⚡ <strong>Control System Synergy for ALTRON Projects:</strong><br>
  All Encore drivers and luminaires are precision-tested for deep, smooth dimming (down to 0.1% flicker-free), eliminating buzzing and step-dimming issues when paired with smart dimming modules and <strong>Casambi</strong> wireless BLE networks.
</div>

<h2>1. 48V Low-Voltage Magnetic Track System (Architectural Series)</h2>
<div class="product-card">
  <div class="product-title">Ultra-Slim 48V Magnetic Platform · Recessed / Surface / Pendant</div>
  <div>
    <span class="specs-tag">Casambi / DALI-2 Compatible</span>
    <span class="specs-tag">CRI 95+ (R9 &gt; 80)</span>
    <span class="specs-tag">Low-Voltage 48V Safe</span>
  </div>
  <ul>
    <li><strong>Designed for Modern Residences &amp; Boutiques:</strong> Ultra-slim trimless tracks integrate flush with gypsum ceilings for zero-frame minimalist aesthetics.</li>
    <li><strong>Modular Click-in Interchangeability:</strong> Spotlights with precision lenses (15°/24°/36°), linear diffusers for ambient lighting, and darklight micro-gratings (UGR &lt; 10).</li>
    <li><strong>Smart Integration:</strong> Compatible with integrated Casambi / DALI-2 track drivers, enabling individual or group addressable tuning right from touch panels or mobile apps.</li>
  </ul>
  {"<img class='prod-img' src='" + img_magnetic + "' />" if img_magnetic else ""}
</div>

<h2>2. DELLA 2.0 Architectural Anti-Glare Downlight Series</h2>
<div class="product-card">
  <div class="product-title">Deep Pinhole Darklight Downlights · Museum-Grade Color Rendering</div>
  <div>
    <span class="specs-tag">UGR &lt; 6 Visual Comfort</span>
    <span class="specs-tag">Casambi / 0-10V / DALI-2</span>
    <span class="specs-tag">SDCM &lt; 3 Strict Binning</span>
  </div>
  <ul>
    <li><strong>True "See the Light, Not the Source" Effect:</strong> Deep optical chamber and secondary reflectors completely conceal the light source, keeping ceilings calm and glare-free.</li>
    <li><strong>Museum-Grade Optics:</strong> Same optical engineering trusted by the National Museum of China and luxury hospitality suites. Accurately reveals wood grains, marble, and artwork textures.</li>
    <li><strong>Dimming Smoothness:</strong> Matches luxury villa demands with ultra-smooth low-end dimming curves.</li>
  </ul>
  {"<img class='prod-img' src='" + img_della + "' />" if img_della else ""}
</div>

<h2>3. NOVA Minimalist Architectural Cylinder &amp; Pendants</h2>
<div class="product-card">
  <div class="product-title">Sculptural Surface &amp; Dining Pendant Cylinders (Φ30mm / Φ45mm)</div>
  <div>
    <span class="specs-tag">Invisible Wire Lock</span>
    <span class="specs-tag">Luxury Anodized Finishes</span>
    <span class="specs-tag">Deep Anti-Glare</span>
  </div>
  <ul>
    <li><strong>Invisible Retractable Suspension:</strong> Zero ugly canopy screws—clean, modern lines over dining islands, reception desks, and bar counters.</li>
    <li><strong>Architectural Finishes:</strong> Deep Matte Black, Architectural White, and Anodized Champagne Bronze to elevate interior hardware coordination.</li>
  </ul>
  {"<img class='prod-img' src='" + img_nova + "' />" if img_nova else ""}
</div>

<h2>Direct Engineering Support for ALTRON Batam</h2>
<ul>
  <li><strong>Rapid Sample Evaluation:</strong> Express door-to-door air courier to Batam (within 7–10 days) for your showroom display and bench testing.</li>
  <li><strong>DIALux Lighting Layouts:</strong> Send us your AutoCAD/interior plans; we provide full photometric simulation and luminaire scheduling for your clients.</li>
  <li><strong>Direct Factory Partnership:</strong> Healthy margins for installation contractors, backed by 5-year commercial warranties.</li>
</ul>

<div class="footer-sig">
  <div>
    <strong>Bob · International Projects</strong><br>
    Encore Commercial Lighting (Encore-Tech)<br>
    Web: encore-tech.com | WhatsApp: +852 5765171
  </div>
  <div style="text-align: right;">
    Factory: Shenzhen, China<br>
    National Museum &amp; Commercial Project Supplier
  </div>
</div>

</body>
</html>
"""

html_path = r"D:\marketing\proposals\Encore_Proposal_ALTRON_Indonesia.html"
pdf_path = r"D:\marketing\proposals\Encore_Proposal_ALTRON_Indonesia.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML generated at {html_path}")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///{html_path.replace(os.sep, '/')}")
    page.wait_for_load_state("networkidle")
    page.pdf(
        path=pdf_path,
        format="A4",
        print_background=True,
        margin={"top": "15mm", "bottom": "15mm", "left": "15mm", "right": "15mm"}
    )
    browser.close()

print(f"PDF successfully rendered at {pdf_path}")
