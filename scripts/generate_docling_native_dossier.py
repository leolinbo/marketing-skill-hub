# -*- coding: utf-8 -*-
"""
Generate the authentic Data-Driven Engineering Specification Dossier for ALTRON Indonesia.
Strictly relies on the extracted Docling tables and text hierarchies from:
- Encore LED Downlight Catalogue-V4(2).json
- Encore LED Magnetic Track Light Catalogue-V4(2).json
- Encore LED Track light Catalogue-V4(2).json
- Company Profile 2025 V1.json

Design principles:
- Native typographic tables and structured engineering spec cards (Zero random image cuts).
- Complete uncropped architectural visuals for mood and project reference.
- Standard ERCO / iGuzzini specification format tailored for ALTRON Batam's Orvibo/Casambi integration.
"""

import os
import base64
from pathlib import Path
from patchright.sync_api import sync_playwright

asset_dir = Path(r"D:\marketing\assets\extracted_catalog_imgs")

def b64(fname):
    p = asset_dir / fname
    if p.exists():
        with open(p, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
            ext = p.suffix.lower().replace(".", "")
            if ext == "jpg": ext = "jpeg"
            return f"data:image/{ext};base64,{data}"
    return ""

img_hero = b64("full_visual_company_hero.png")
img_museum = b64("full_visual_museum_gallery.png")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>ENCORE LIGHTING · Architectural Specification Dossier for ALTRON Indonesia</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Cinzel:wght@600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

  @page {{
    size: A4 portrait;
    margin: 0;
  }}

  * {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #0f172a;
    background: #ffffff;
    margin: 0;
    padding: 0;
    font-size: 11.5px;
    line-height: 1.5;
  }}

  .page {{
    width: 210mm;
    height: 297mm;
    padding: 18mm 18mm 16mm 18mm;
    margin: 0 auto;
    position: relative;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    background: #ffffff;
  }}

  .mono {{ font-family: 'JetBrains Mono', monospace; }}
  .serif {{ font-family: 'Cinzel', Georgia, serif; letter-spacing: 0.5px; }}

  /* Cover Page */
  .page-cover {{
    background: #09131a;
    color: #ffffff;
    padding: 20mm 18mm 16mm 18mm;
  }}
  .brand-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.15);
    padding-bottom: 12px;
  }}
  .brand-title {{
    font-size: 21px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #ffffff;
  }}
  .brand-title span {{
    font-size: 13px;
    color: #38bdf8;
    font-weight: 300;
    letter-spacing: 1px;
    margin-left: 6px;
  }}
  .doc-tag {{
    font-size: 10px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #38bdf8;
    border: 1px solid rgba(56, 189, 248, 0.4);
    padding: 4px 10px;
    border-radius: 4px;
    background: rgba(56, 189, 248, 0.08);
  }}
  .cover-kicker {{
    font-size: 10.5px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #38bdf8;
    margin: 22px 0 8px 0;
    font-weight: 600;
  }}
  .cover-heading {{
    font-size: 30px;
    line-height: 1.22;
    color: #ffffff;
    margin: 0 0 12px 0;
    font-weight: 700;
  }}
  .cover-heading em {{
    color: #38bdf8;
    font-style: normal;
  }}
  .cover-desc {{
    font-size: 12.5px;
    color: #94a3b8;
    line-height: 1.6;
    max-width: 530px;
    margin-bottom: 18px;
  }}
  .cover-visual-frame {{
    width: 100%;
    height: 290px;
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 20px 40px -10px rgba(0,0,0,0.7);
    margin-bottom: 18px;
  }}
  .cover-visual-frame img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .client-brief-card {{
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 6px;
    padding: 12px 16px;
    display: grid;
    grid-template-columns: 1.25fr 1fr;
    gap: 16px;
    font-size: 11px;
  }}
  .client-brief-card h6 {{
    margin: 0 0 3px 0;
    font-size: 10px;
    color: #38bdf8;
    letter-spacing: 1px;
    text-transform: uppercase;
  }}
  .cover-footer {{
    border-top: 1px solid rgba(255,255,255,0.1);
    padding-top: 8px;
    display: flex;
    justify-content: space-between;
    font-size: 10px;
    color: #64748b;
  }}

  /* Inner Standard Headers */
  .page-top {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 1.5px solid #0f172a;
    padding-bottom: 6px;
    margin-bottom: 12px;
  }}
  .section-tag {{
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #0284c7;
  }}
  .section-target {{
    font-size: 10.5px;
    color: #64748b;
  }}

  .header-intro {{
    margin-bottom: 10px;
  }}
  .header-intro h2 {{
    font-size: 18px;
    color: #0f172a;
    margin: 0 0 3px 0;
    font-weight: 700;
  }}
  .header-intro p {{
    margin: 0;
    font-size: 11.5px;
    color: #475569;
  }}

  /* High Precision Specification Tables (Native Docling Schema) */
  .spec-table-block {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    margin-bottom: 14px;
    overflow: hidden;
  }}
  .spec-table-header {{
    background: #0f172a;
    color: #ffffff;
    padding: 8px 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .spec-table-header h4 {{
    margin: 0;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.5px;
  }}
  .spec-badge {{
    background: #0284c7;
    color: #ffffff;
    font-size: 10px;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 3px;
  }}

  .docling-data-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 10.5px;
  }}
  .docling-data-table th {{
    background: #f1f5f9;
    padding: 6px 10px;
    text-align: left;
    color: #334155;
    font-weight: 600;
    border-bottom: 1px solid #cbd5e1;
  }}
  .docling-data-table td {{
    padding: 6px 10px;
    border-bottom: 1px solid #e2e8f0;
    color: #1e293b;
    vertical-align: top;
  }}
  .docling-data-table tr:last-child td {{
    border-bottom: none;
  }}
  .docling-data-table td.label-col {{
    background: #fafafa;
    color: #475569;
    font-weight: 600;
    width: 25%;
    border-right: 1px solid #e2e8f0;
  }}

  /* Engineering Concept Callouts */
  .eng-callout-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 12px;
  }}
  .eng-card {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 10px 12px;
    border-left: 3.5px solid #0284c7;
  }}
  .eng-card h5 {{
    margin: 0 0 4px 0;
    font-size: 11.5px;
    color: #0369a1;
    display: flex;
    justify-content: space-between;
  }}
  .eng-card p {{
    margin: 0;
    font-size: 10.5px;
    color: #475569;
    line-height: 1.45;
  }}

  /* Bottom Controls & Specs Bar */
  .control-compat-strip {{
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 8px 12px;
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 10.5px;
  }}

  /* Page Footer */
  .page-bottom {{
    border-top: 1px solid #e2e8f0;
    padding-top: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 9.5px;
    color: #94a3b8;
  }}
</style>
</head>
<body>

<!-- ================= PAGE 1: EDITORIAL COVER ================= -->
<div class="page page-cover">
  <div class="brand-bar">
    <div class="brand-title serif">ENCORE <span>COMMERCIAL LIGHTING</span></div>
    <div class="doc-tag mono">ENGINEERING SPECIFICATION DOSSIER</div>
  </div>

  <div>
    <div class="cover-kicker mono">AUTHENTIC ARCHITECTURAL HARDWARE · BATAM 2026</div>
    <h1 class="cover-heading serif">Architectural Hardware Integration for <em>Smart Living</em> &amp; Luxury Villas</h1>
    <div class="cover-desc">
      A rigorous technical hardware portfolio extracted from Encore Engineering Catalogs. Built specifically for system integrators deploying <strong>Casambi Wireless BLE, DALI-2, 0-10V, and Phase-Cut</strong> dimming systems with 0.1% depth without step-dimming or humming.
    </div>

    <div class="cover-visual-frame">
      <img src="{img_hero}" alt="Encore Lighting Architecture" />
    </div>

    <div class="client-brief-card">
      <div>
        <h6>Prepared Exclusively For</h6>
        <strong style="font-size: 12.5px; color:#ffffff;">ALTRON Indonesia</strong><br>
        📍 Ruko Pasir Putih A6 No. 88, Sadai, Bengkong, Batam<br>
        Focus: Luxury Villas, Hospitality &amp; Smart Integration (Orvibo &amp; Yeelight Partner)
      </div>
      <div>
        <h6>Factory Direct Engineering</h6>
        <strong style="font-size: 12.5px; color:#ffffff;">Encore Commercial Lighting</strong><br>
        Engineering &amp; Manufacturing: Shenzhen, China<br>
        Verified Pedigree: National Museum of China &amp; Luxury Resort Supplier
      </div>
    </div>
  </div>

  <div class="cover-footer mono">
    <div>REF: ENC-SPEC-ALTRON2026 · EXTRACTED DIRECTLY FROM OFFICIAL CATALOGUES</div>
    <div>WWW.ENCORE-TECH.COM</div>
  </div>
</div>

<!-- ================= PAGE 2: DELLA MINI DOWNLIGHT SYSTEM (DOCLING STRUCTURED DATA) ================= -->
<div class="page">
  <div>
    <div class="page-top">
      <div class="section-tag mono">01 / DELLA Mini Downlight System Specification</div>
      <div class="section-target mono">ENCORE × ALTRON BATAM</div>
    </div>

    <div class="header-intro">
      <h2 class="serif">DELLA 2.0 Architectural Mini Downlight Specifications</h2>
      <p>True darklight architecture with shift-axis zero light loss and pull-ring maintenance.</p>
    </div>

    <!-- Engineering Innovation Highlights -->
    <div class="eng-callout-grid">
      <div class="eng-card">
        <h5>Shift-Axis™ Zero Light Loss <span class="mono" style="font-size:10px;">100% EFFICIENCY</span></h5>
        <p>
          Adjustment rotates exactly at the optical pivot center. Unlike conventional fixtures whose bezels clip the beam cone at tilt, DELLA ensures 100% full distribution without edge loss.
        </p>
      </div>
      <div class="eng-card">
        <h5>Pull-Ring Tool-Free Servicing <span class="mono" style="font-size:10px;">IP65 / IC RATED</span></h5>
        <p>
          Integrated foldable pull-ring permits LED light engine removal from below the ceiling in seconds, preventing drywall damage during post-handover maintenance or driver swapping.
        </p>
      </div>
    </div>

    <!-- Docling Table 1: DELLA DM30 (1.25" Ultra Mini) -->
    <div class="spec-table-block">
      <div class="spec-table-header">
        <h4>DELLA DM30 · 1.25" Ultra-Mini Downlight (Docling Extracted Spec)</h4>
        <span class="spec-badge mono">1.25" APERTURE</span>
      </div>
      <table class="docling-data-table">
        <tr>
          <td class="label-col">Input Wattage &amp; Output</td>
          <td><strong>5W – 8W</strong> | Delivered Lumens: <strong>292lm – 407lm</strong> (Whole Fixture Efficacy)</td>
        </tr>
        <tr>
          <td class="label-col">Operating Voltage</td>
          <td>120–277V / 230V AC, 50/60Hz | Power Factor: &gt; 0.90 | Lumen Maintenance: 50,000h @ L80</td>
        </tr>
        <tr>
          <td class="label-col">Optical Characteristics</td>
          <td>Beam Angles: <strong>15° Narrow Spot, 24° Spot, 36° Spot, 50° Flood</strong> | Color Quality: <strong>CRI 90+, SDCM ≤ 2</strong></td>
        </tr>
        <tr>
          <td class="label-col">CCT Options</td>
          <td>Static White: 2700K, 3000K, 3500K, 4000K | Secondary Reflector: Matt Black / Matt White / Matt Silver</td>
        </tr>
        <tr>
          <td class="label-col">Dimming Control</td>
          <td><strong>Casambi Wireless BLE, DALI-2, 0/1-10V, Phase-Cut (TRIAC)</strong> (Smooth 0.1% Dimming Depth)</td>
        </tr>
      </table>
    </div>

    <!-- Docling Table 2: DELLA DM50 (2") & DM60 (3") High Output -->
    <div class="spec-table-block">
      <div class="spec-table-header">
        <h4>DELLA DM50 (2") &amp; DM60 (3") · High Performance Darklight Downlight</h4>
        <span class="spec-badge mono">2" / 3" APERTURE</span>
      </div>
      <table class="docling-data-table">
        <tr>
          <td class="label-col">Input Wattage &amp; Output</td>
          <td>
            <strong>DM50 (2"):</strong> 8W – 10W (470lm – 771lm)<br>
            <strong>DM60 (3"):</strong> 10W – 15W (621lm – 1042lm)
          </td>
        </tr>
        <tr>
          <td class="label-col">Color Spectra &amp; Tunable</td>
          <td>
            Static White: 2700K, 3000K, 3500K, 4000K<br>
            <strong>Dim-to-Warm:</strong> 1800K–3000K | <strong>Tunable White:</strong> 2700K–6500K | <strong>Full Spectrum:</strong> RGBW (DM60)
          </td>
        </tr>
        <tr>
          <td class="label-col">Optical Distribution</td>
          <td>15° Narrow Spot, 24°, 28°, 33°, 36° Spot, 42°, 45°, 50° Flood + Asymmetric Wall Washing</td>
        </tr>
        <tr>
          <td class="label-col">Glare Control</td>
          <td>Deep front-focus pinhole darklight architecture achieving <strong>UGR &lt; 6</strong> for supreme visual comfort</td>
        </tr>
        <tr>
          <td class="label-col">Dimming Protocols</td>
          <td><strong>Casambi BLE, DALI-2, 0/1-10V, TRIAC, DMX512</strong> | Fully compatible with Orvibo dimming modules</td>
        </tr>
      </table>
    </div>
  </div>

  <div class="page-bottom mono">
    <div>ENCORE COMMERCIAL LIGHTING · DELLA SPECIFICATION SHEET</div>
    <div>PAGE 02 / 04</div>
  </div>
</div>

<!-- ================= PAGE 3: 48V MAGNETIC TRACK & MOVIA (DOCLING STRUCTURED DATA) ================= -->
<div class="page">
  <div>
    <div class="page-top">
      <div class="section-tag mono">02 / 48V Low-Voltage Magnetic Track &amp; Smart Platforms</div>
      <div class="section-target mono">ENCORE × ALTRON BATAM</div>
    </div>

    <div class="header-intro">
      <h2 class="serif">48V Magnetic Track &amp; Click-in Module Specifications</h2>
      <p>Precision extruded 20mm &amp; 15mm profiles with anti-slip ladder red copper busbars.</p>
    </div>

    <!-- Docling Table: 48V Magnetic Track Mechanical Rail Profiles -->
    <div class="spec-table-block">
      <div class="spec-table-header">
        <h4>48V Low-Voltage Magnetic Track Infrastructure (MT20 Series)</h4>
        <span class="spec-badge mono">SAFE 48V DC</span>
      </div>
      <table class="docling-data-table">
        <tr>
          <td class="label-col">System Profiles</td>
          <td>MT20S2628 (Surface/Pendant 26×28mm) | MT20R2635 (Recessed Plaster Trimless 26×35mm) | MT15 Ultra-Slim</td>
        </tr>
        <tr>
          <td class="label-col">Busbar Engineering</td>
          <td><strong>0.8mm High-Purity Red Copper</strong> co-extruded with polymer; <strong>"Ladder-Type" locking design</strong> to prevent copper slippage</td>
        </tr>
        <tr>
          <td class="label-col">Standard Lengths</td>
          <td>1000mm / 2000mm / 3000mm continuous scalable runs | Finishes: Architectural Sandblasted Black / White</td>
        </tr>
        <tr>
          <td class="label-col">Corner Accessories</td>
          <td>A.A.G. Certified 90° 3D Ceiling-to-Wall and horizontal seamless joint modules</td>
        </tr>
      </table>
    </div>

    <!-- Docling Table: 48V Magnetic Spot & Darklight Module Data -->
    <div class="spec-table-block">
      <div class="spec-table-header">
        <h4>48V Click-in Luminaire Photometric Matrix (Extracted from Catalogue V4)</h4>
        <span class="spec-badge mono">CRI 90+ / SDCM &lt; 3</span>
      </div>
      <table class="docling-data-table">
        <thead>
          <tr>
            <th style="width:20%;">Module Model / Type</th>
            <th style="width:15%;">Power (W)</th>
            <th style="width:25%;">Beam Angles</th>
            <th style="width:20%;">Delivered Flux (lm)</th>
            <th style="width:20%;">System Efficacy</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Magnetic Adjustable Spot</strong></td>
            <td>8W</td>
            <td>15° / 24° / 38° / 50°</td>
            <td>579lm – 594lm</td>
            <td>64 – 65 lm/W</td>
          </tr>
          <tr>
            <td><strong>Magnetic High-Output Spot</strong></td>
            <td>15W</td>
            <td>15° / 24° / 38° / 50°</td>
            <td>1,276lm – 1,354lm</td>
            <td>91 – 97 lm/W</td>
          </tr>
          <tr>
            <td><strong>Magnetic Master Spot</strong></td>
            <td>20W</td>
            <td>15° / 24° / 38° / 50°</td>
            <td>1,614lm – 1,761lm</td>
            <td>80 – 85 lm/W</td>
          </tr>
          <tr>
            <td><strong>Magnetic Linear Darklight</strong></td>
            <td>10W / 20W</td>
            <td>Micro-Grating UGR &lt; 10</td>
            <td>655lm / 1,374lm</td>
            <td>64 – 71 lm/W</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- MOVIA Motorized Platform Card -->
    <div class="spec-table-block" style="margin-bottom:0;">
      <div class="spec-table-header" style="background:#1e1b4b;">
        <h4>MOVIA Motorized Track Light &amp; IMAX 7-in-1 Optical Framing Projector</h4>
        <span class="spec-badge mono" style="background:#4338ca;">SMART AIMING</span>
      </div>
      <table class="docling-data-table">
        <tr>
          <td class="label-col">MOVIA Motorized Spot</td>
          <td>
            <strong>Wireless Pan / Tilt:</strong> 355° motorized rotation and 90° tilt controlled via 2.4G RF / App.<br>
            <strong>Application:</strong> Designed for double-height villa living rooms and stairwell art walls in Batam—re-aim beam angles without scaffolding or ladders.
          </td>
        </tr>
        <tr>
          <td class="label-col">IMAX 7-in-1 Projector</td>
          <td>
            <strong>Optical Projector:</strong> Camera-grade optical glass with internal framing shutters, zoomable beam (15°–36°), and customizable gobo pattern projection for luxury feature walls.
          </td>
        </tr>
      </table>
    </div>
  </div>

  <div class="page-bottom mono">
    <div>ENCORE COMMERCIAL LIGHTING · 48V LOW-VOLTAGE PLATFORM SPECIFICATION</div>
    <div>PAGE 03 / 04</div>
  </div>
</div>

<!-- ================= PAGE 4: CREDENTIALS & COOPERATION MODEL ================= -->
<div class="page">
  <div>
    <div class="page-top">
      <div class="section-tag mono">03 / Manufacturing Credentials &amp; Project Support Framework</div>
      <div class="section-target mono">ENCORE × ALTRON BATAM</div>
    </div>

    <div class="header-intro">
      <h2 class="serif">National Museum-Grade Quality Pedigree</h2>
      <p>Tested and deployed in China's most demanding state cultural institutions and luxury hospitality.</p>
    </div>

    <div class="cover-visual-frame" style="height: 175px; margin-bottom: 12px;">
      <img src="{img_museum}" alt="National Museum of China Reference Installation" />
    </div>

    <div class="eng-callout-grid" style="margin-bottom:12px;">
      <div class="eng-card">
        <h5>State Cultural Landmarks</h5>
        <p>
          Encore fixtures are trusted by the <strong>National Museum of China</strong> and <strong>Sanxingdui Museum</strong>. Strict SDCM ≤ 2 chromatic consistency accurately reveals natural Indonesian teak wood, marble veining, and art collections.
        </p>
      </div>
      <div class="eng-card">
        <h5>R&amp;D &amp; In-House Laboratory</h5>
        <p>
          Encore operates an in-house ISO9001 testing lab equipped with integrating spheres, goniophotometers, and thermal chambers to guarantee 100% true photometric output and longevity.
        </p>
      </div>
    </div>

    <div class="header-intro">
      <h2 class="serif">Direct Project Supply Framework for ALTRON Indonesia</h2>
      <p>Designed to provide maximum commercial margins and zero post-handover contractor callbacks.</p>
    </div>

    <div class="spec-table-block" style="margin-bottom:0;">
      <table class="docling-data-table">
        <tr>
          <td class="label-col" style="width:28%;">Door-to-Door Air Courier</td>
          <td>Working sample kits air-couriered to your Batam showroom (Ruko Pasir Putih) within 7–10 days for physical inspection and Orvibo hub testing.</td>
        </tr>
        <tr>
          <td class="label-col">AutoCAD &amp; DIALux 3D</td>
          <td>Complimentary photometric lighting simulations and luminaire scheduling ready for your client presentations and contractor bids.</td>
        </tr>
        <tr>
          <td class="label-col">Factory Direct Margins</td>
          <td>Direct-from-manufacturer FOB/EXW pricing protects healthy margins for ALTRON's integration, procurement, and installation services.</td>
        </tr>
        <tr>
          <td class="label-col">5-Year Commercial Warranty</td>
          <td>Industrial-grade thermal dissipation with Citizen / Bridgelux COB LED engines ensures long-term reliability in tropical climates.</td>
        </tr>
      </table>
    </div>
  </div>

  <div>
    <div class="control-compat-strip mono" style="background:#0f172a; color:#ffffff; margin-top:12px;">
      <div>
        <strong>CONTACT:</strong> Bob · Project Director | <strong>WhatsApp:</strong> +852 6768 2519 / +852 5765171
      </div>
      <div>
        <strong>EMAIL:</strong> sales@encore-tech.com | <strong>WEB:</strong> www.encore-tech.com
      </div>
    </div>
    <div class="page-bottom mono">
      <div>ENCORE COMMERCIAL LIGHTING · ARCHITECTURAL PROJECT SPECIFICATION DOSSIER</div>
      <div>PAGE 04 / 04</div>
    </div>
  </div>
</div>

</body>
</html>
"""

target_html = r"D:\marketing\proposals\Encore_Engineering_Dossier_ALTRON.html"
target_pdf = r"D:\marketing\proposals\Encore_Engineering_Dossier_ALTRON.pdf"

with open(target_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Native Spec Sheet HTML saved to: {target_html}")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///{target_html.replace(os.sep, '/')}")
    page.wait_for_load_state("networkidle")
    page.pdf(
        path=target_pdf,
        format="A4",
        print_background=True,
        margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
    )
    browser.close()

print(f"[✓] Pristine Native Engineering Dossier PDF generated: {target_pdf}")
