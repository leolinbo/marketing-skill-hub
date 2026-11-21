# -*- coding: utf-8 -*-
"""
Generate an authentic, high-craft, 4-page architectural curation catalogue for ALTRON Indonesia.
Strictly constructed from the Docling-parsed markdown/JSON datasets of:
1. Company Profile 2025 V1
2. Encore LED Downlight Catalogue-V4(2)
3. Encore LED Magnetic Track Light Catalogue-V4(2)
4. Encore LED Track light Catalogue-V4(2)
5. Encore LED Cylinder&Linear Light Catalogue-V4(2)

Real technologies applied:
- Circadian Lighting (1600K-12000K, Planckian Locus, James Turrell philosophy)
- Casambi BLE Wireless & DALI-2 integration
- DELLA Shift-Axis Zero Light Loss & Pull-Ring maintenance design (UGR < 6)
- 48V Ultra-Slim Magnetic Track (MT20 20mm & 15mm, 0.8mm Red Copper busbar, Ladder-type extrusion)
- MOVIA Motorized track light & IMAX 7-in-1 projector
- Authentic museum credentials (National Museum of China, Sanxingdui Museum)
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

img_cover = b64("company_p4_img0_1770x2866.jpeg")
img_circadian = b64("company_p10_img0_5352x1555.jpeg")
img_della_shift = b64("della_tech_p15_0_1553x1021.png")
img_della_exploded = b64("della_tech_p14_0_1111x1572.png")
img_della_optical = b64("della_tech_p16_0_2220x1571.png")
img_mag_track_system = b64("mag_p4_0_2066x1299.png")
img_mag_scene = b64("mag_p5_0_2067x1299.png")
img_movia_motor = b64("track_tech_p19_3_1554x1023.png")
img_imax_proj = b64("track_tech_p22_0_1286x932.png")
img_museum_proof = b64("company_p15_img7_2107x925.jpeg")

html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>ENCORE LIGHTING · Architectural Specification Portfolio for ALTRON Indonesia</title>
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
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    color: #1e293b;
    background: #ffffff;
    margin: 0;
    padding: 0;
    font-size: 12.5px;
    line-height: 1.55;
  }}

  .page {{
    width: 210mm;
    height: 297mm;
    padding: 16mm 18mm 14mm 18mm;
    margin: 0 auto;
    position: relative;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    background: #ffffff;
  }}

  .mono {{
    font-family: 'JetBrains Mono', monospace;
  }}

  .serif {{
    font-family: 'Cinzel', Georgia, serif;
    letter-spacing: 0.5px;
  }}

  /* Page 1 - Architectural Editorial Cover */
  .cover {{
    background: #081116;
    color: #ffffff;
    padding: 20mm 18mm 16mm 18mm;
  }}
  .cover-top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.15);
    padding-bottom: 14px;
  }}
  .brand-logo {{
    font-size: 22px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #ffffff;
  }}
  .brand-logo span {{
    font-size: 13px;
    color: #38bdf8;
    font-weight: 300;
    letter-spacing: 1px;
    margin-left: 6px;
  }}
  .cover-kicker {{
    font-size: 10.5px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #38bdf8;
    font-weight: 600;
    margin: 24px 0 8px 0;
  }}
  .cover-title {{
    font-size: 32px;
    line-height: 1.2;
    color: #ffffff;
    margin: 0 0 14px 0;
    font-weight: 700;
  }}
  .cover-title em {{
    color: #38bdf8;
    font-style: normal;
  }}
  .cover-lead {{
    font-size: 13px;
    color: #94a3b8;
    line-height: 1.65;
    max-width: 530px;
    margin-bottom: 20px;
  }}
  .cover-hero-frame {{
    width: 100%;
    height: 275px;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 25px 50px -12px rgba(0,0,0,0.7);
    margin-bottom: 20px;
  }}
  .cover-hero-frame img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .client-brief {{
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 6px;
    padding: 12px 16px;
    display: grid;
    grid-template-columns: 1.3fr 1fr;
    gap: 16px;
    font-size: 11px;
  }}
  .client-brief h6 {{
    margin: 0 0 3px 0;
    font-size: 10.5px;
    color: #38bdf8;
    letter-spacing: 1px;
    text-transform: uppercase;
  }}
  .cover-footer {{
    border-top: 1px solid rgba(255,255,255,0.1);
    padding-top: 10px;
    display: flex;
    justify-content: space-between;
    font-size: 10px;
    color: #64748b;
  }}

  /* Inner Pages Structure */
  .page-nav {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 1.5px solid #0f172a;
    padding-bottom: 6px;
    margin-bottom: 14px;
  }}
  .page-nav .tag {{
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #0284c7;
  }}
  .page-nav .sub {{
    font-size: 10.5px;
    color: #64748b;
  }}

  .section-head {{
    margin-bottom: 12px;
  }}
  .section-head h2 {{
    font-size: 19px;
    color: #0f172a;
    margin: 0 0 3px 0;
    font-weight: 700;
  }}
  .section-head p {{
    margin: 0;
    font-size: 12px;
    color: #475569;
  }}

  /* Casambi Callout */
  .circadian-banner {{
    background: #091319;
    color: #ffffff;
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 14px;
    display: grid;
    grid-template-columns: 1.35fr 1fr;
    gap: 14px;
    align-items: center;
  }}
  .circadian-banner h4 {{
    margin: 0 0 4px 0;
    font-size: 13px;
    color: #38bdf8;
  }}
  .circadian-banner p {{
    margin: 0;
    font-size: 11px;
    color: #cbd5e1;
    line-height: 1.5;
  }}
  .circadian-banner img {{
    width: 100%;
    height: 80px;
    object-fit: cover;
    border-radius: 4px;
    border: 1px solid rgba(255,255,255,0.15);
  }}

  /* 2-Column Product Layouts */
  .grid-2col {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 12px;
  }}
  .tech-card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 12px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .tech-card-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 6px;
  }}
  .tech-card-title {{
    font-size: 13px;
    font-weight: 700;
    color: #0f172a;
  }}
  .pill {{
    font-size: 9.5px;
    font-weight: 600;
    padding: 2px 6px;
    border-radius: 3px;
  }}
  .pill-blue {{ background: #e0f2fe; color: #0369a1; }}
  .pill-teal {{ background: #ccfbf1; color: #0f766e; }}
  .pill-purple {{ background: #f3e8ff; color: #7e22ce; }}

  .tech-card-desc {{
    font-size: 11px;
    color: #475569;
    margin-bottom: 8px;
    line-height: 1.5;
  }}
  .spec-grid-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 10.5px;
    margin-bottom: 8px;
  }}
  .spec-grid-table td {{
    padding: 3px 5px;
    border-bottom: 1px solid #e2e8f0;
    color: #334155;
  }}
  .spec-grid-table td.key {{
    color: #64748b;
    font-weight: 600;
    width: 44%;
  }}
  .card-img-frame {{
    width: 100%;
    height: 140px;
    border-radius: 5px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
    background: #ffffff;
  }}
  .card-img-frame img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
  }}

  /* Page Footer */
  .page-foot {{
    border-top: 1px solid #e2e8f0;
    padding-top: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 10px;
    color: #94a3b8;
  }}

  /* Authority & Supply Model Cards */
  .authority-strip {{
    background: #f1f5f9;
    border-left: 3.5px solid #0284c7;
    border-radius: 0 6px 6px 0;
    padding: 10px 14px;
    margin-bottom: 12px;
    display: grid;
    grid-template-columns: 1.4fr 1fr;
    gap: 12px;
    align-items: center;
  }}
  .authority-strip h4 {{
    margin: 0 0 3px 0;
    font-size: 12.5px;
    color: #0369a1;
  }}
  .authority-strip p {{
    margin: 0;
    font-size: 11px;
    color: #334155;
  }}
  .authority-strip img {{
    width: 100%;
    height: 70px;
    object-fit: cover;
    border-radius: 4px;
    border: 1px solid #cbd5e1;
  }}

  .supply-box {{
    background: #fafaf9;
    border: 1px dashed #0284c7;
    border-radius: 6px;
    padding: 12px 14px;
    margin-bottom: 12px;
  }}
  .supply-box h4 {{
    margin: 0 0 6px 0;
    font-size: 12.5px;
    color: #0369a1;
  }}
  .supply-list {{
    margin: 0;
    padding-left: 16px;
    font-size: 11px;
    color: #334155;
  }}
  .supply-list li {{
    margin-bottom: 4px;
  }}

  .contact-strip {{
    background: #0f172a;
    color: #ffffff;
    border-radius: 5px;
    padding: 9px 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 10.5px;
    margin-bottom: 6px;
  }}
  .contact-strip strong {{
    color: #38bdf8;
  }}
</style>
</head>
<body>

<!-- ================= PAGE 1: EDITORIAL COVER ================= -->
<div class="page cover">
  <div class="cover-top">
    <div class="brand-logo serif">ENCORE <span>COMMERCIAL LIGHTING</span></div>
    <div class="mono" style="font-size: 10px; color:#38bdf8; border:1px solid #38bdf8; padding:3px 8px; border-radius:3px;">
      SPECIFICATION DOSSIER · BATAM
    </div>
  </div>

  <div>
    <div class="cover-kicker mono">AUTHENTIC ARCHITECTURAL HARDWARE 2026</div>
    <h1 class="cover-title serif">Architectural Hardware Integration for <em>Smart Living</em> &amp; Luxury Villas</h1>
    <div class="cover-lead">
      Engineered for high-end lighting consultants and smart home integrators. Precision luminaires paired natively with <strong>Casambi Wireless BLE, DALI-2, 0-10V, and Phase-Cut</strong> systems for smooth 0.1% flicker-free dimming.
    </div>

    <div class="cover-hero-frame">
      <img src="{img_cover}" alt="Architectural Lighting Architecture" />
    </div>

    <div class="client-brief">
      <div>
        <h6>Curated Exclusively For</h6>
        <strong style="font-size: 12.5px; color:#ffffff;">ALTRON Indonesia</strong><br>
        📍 Ruko Pasir Putih A6 No. 88, Sadai, Bengkong, Batam<br>
        Smart Home &amp; Lighting Specialist (Orvibo &amp; Yeelight Partner)
      </div>
      <div>
        <h6>Factory Direct Manufacturer</h6>
        <strong style="font-size: 12.5px; color:#ffffff;">Encore Commercial Lighting</strong><br>
        R&amp;D &amp; Manufacturing: Shenzhen, China<br>
        Proven Pedigree: National Museum of China &amp; Luxury Resorts
      </div>
    </div>
  </div>

  <div class="cover-footer mono">
    <div>REF: ENC-DOC-ALTRON2026 · STRICTLY FOR PROJECT EVALUATION</div>
    <div>WWW.ENCORE-TECH.COM</div>
  </div>
</div>

<!-- ================= PAGE 2: CASAMBI CIRCADIAN & DELLA ZERO-LOSS DOWNLIGHT ================= -->
<div class="page">
  <div>
    <div class="page-nav">
      <div class="tag mono">01 / Circadian Lighting &amp; Shift-Axis Downlight Engineering</div>
      <div class="sub mono">ENCORE × ALTRON BATAM</div>
    </div>

    <div class="section-head">
      <h2 class="serif">Circadian Dynamics &amp; Optical Mastery</h2>
      <p>Following the James Turrell emotional lighting philosophy across the natural Planckian locus.</p>
    </div>

    <div class="circadian-banner">
      <div>
        <h4>⚡ Circadian Rhythm Spectrum (1600K–12000K) + Casambi BLE</h4>
        <p>
          Replicates natural sunlight from candlelit warm embers (1600K) to crisp midday sky (12000K). Integrated with Casambi Bluetooth mesh &amp; DALI-2 addressable drivers for deep 0.1% dimming without step-dimming artifacts or coil humming.
        </p>
      </div>
      <div>
        <img src="{img_circadian}" alt="Circadian Lighting & Casambi Topology" />
      </div>
    </div>

    <div class="section-head">
      <h2 class="serif">DELLA 2.0 Architectural Mini Downlight System</h2>
      <p>Patented Shift-Axis zero light loss engineering with quick-service Pull-Ring architecture.</p>
    </div>

    <div class="grid-2col">
      <!-- DELLA Shift Axis -->
      <div class="tech-card">
        <div>
          <div class="tech-card-header">
            <span class="tech-card-title">Shift-Axis™ Zero Light Loss</span>
            <span class="pill pill-teal">100% Efficiency</span>
          </div>
          <div class="tech-card-desc">
            Unlike conventional tilt downlights where the bezel clips the light cone, DELLA’s adjustment pivots precisely at the optical center, ensuring full beam distribution without edge cutoff.
          </div>
          <table class="spec-grid-table">
            <tr><td class="key">Aperture Sizes</td><td>DM30 (1.25") / DM50 (2") / DM60 (3")</td></tr>
            <tr><td class="key">Visual Comfort</td><td>Pinhole Darklight UGR &lt; 6</td></tr>
            <tr><td class="key">Beam Angles</td><td>15°, 24°, 36°, 55° Precise Optics</td></tr>
            <tr><td class="key">Maintenance</td><td>Pull-Ring Design (LED swap in seconds)</td></tr>
          </table>
        </div>
        <div class="card-img-frame">
          <img src="{img_della_shift}" alt="DELLA Shift-Axis Mechanism" />
        </div>
      </div>

      <!-- DELLA Optical System -->
      <div class="tech-card">
        <div>
          <div class="tech-card-header">
            <span class="tech-card-title">Modular Optical Chamber</span>
            <span class="pill pill-blue">IP65 / IC Rated</span>
          </div>
          <div class="tech-card-desc">
            Deep secondary reflector design conceals the source ("see the light, not the fixture"). Fully enclosed structure prevents ceiling dust leakage and optical contamination.
          </div>
          <table class="spec-grid-table">
            <tr><td class="key">Wattage &amp; Flux</td><td>5W–8W (400lm) up to 15W (1200lm)</td></tr>
            <tr><td class="key">Color Rendering</td><td>CRI 95+ (R9 &gt; 80, SDCM &lt; 3)</td></tr>
            <tr><td class="key">Reflector Finishes</td><td>Matt Black / Matt White / Matt Silver</td></tr>
            <tr><td class="key">Driver Ecosystem</td><td>Casambi BLE / DALI-2 / 0-10V / Phase</td></tr>
          </table>
        </div>
        <div class="card-img-frame">
          <img src="{img_della_exploded}" alt="DELLA Exploded Modular Architecture" />
        </div>
      </div>
    </div>
  </div>

  <div class="page-foot mono">
    <div>ENCORE COMMERCIAL LIGHTING · DELLA 2.0 MODULAR ARCHITECTURE</div>
    <div>PAGE 02 / 04</div>
  </div>
</div>

<!-- ================= PAGE 3: 48V MAGNETIC TRACK & MOTORIZED SMART TRACK ================= -->
<div class="page">
  <div>
    <div class="page-nav">
      <div class="tag mono">02 / 48V Low-Voltage Magnetic &amp; Motorized Track Platforms</div>
      <div class="sub mono">ENCORE × ALTRON BATAM</div>
    </div>

    <div class="section-head">
      <h2 class="serif">48V Ultra-Slim Magnetic Track Platform</h2>
      <p>Precision extruded 20mm &amp; 15mm profiles engineered with anti-slip red copper busbars.</p>
    </div>

    <div class="grid-2col">
      <!-- 48V Magnetic -->
      <div class="tech-card">
        <div>
          <div class="tech-card-header">
            <span class="tech-card-title">MT20 &amp; MT15 Low-Voltage Rails</span>
            <span class="pill pill-blue">48V / 24V DC</span>
          </div>
          <div class="tech-card-desc">
            Equipped with 0.8mm high-purity red copper busbars extruded as a single unit with thermal-stabilized polymer. Patented "ladder-type" interior prevents copper strip slip-out over years of operation.
          </div>
          <table class="spec-grid-table">
            <tr><td class="key">Mounting Types</td><td>Trimless Recessed / Surface / Pendant</td></tr>
            <tr><td class="key">Corner Connectors</td><td>A.A.G. Certified 90° 3D Seamless Joints</td></tr>
            <tr><td class="key">Click-in Modules</td><td>Spots, Micro-Grating Grille, Diffusers</td></tr>
            <tr><td class="key">Smart Pairing</td><td>Casambi BLE / DALI Broadcast &amp; Addressable</td></tr>
          </table>
        </div>
        <div class="card-img-frame">
          <img src="{img_mag_track_system}" alt="48V Magnetic Track Profiles" />
        </div>
      </div>

      <!-- MOVIA & IMAX -->
      <div class="tech-card">
        <div>
          <div class="tech-card-header">
            <span class="tech-card-title">MOVIA Motorized &amp; IMAX Projector</span>
            <span class="pill pill-purple">Wireless Pan / Tilt</span>
          </div>
          <div class="tech-card-desc">
            MOVIA offers motorized pan (355°) and tilt (90°) remote aiming via app/remote, eliminating ladder setups in double-height villa atriums. IMAX provides framing shutters and gobo pattern projection.
          </div>
          <table class="spec-grid-table">
            <tr><td class="key">MOVIA Control</td><td>RF 2.4G / App Motorized Aiming</td></tr>
            <tr><td class="key">IMAX 7-in-1</td><td>Zooming (15°-36°), Framing, Gobo Projector</td></tr>
            <tr><td class="key">Beam Precision</td><td>Camera-grade optical glass framing</td></tr>
            <tr><td class="key">Application</td><td>Villa Art Walls, Sculptures &amp; Double Ceilings</td></tr>
          </table>
        </div>
        <div class="card-img-frame">
          <img src="{img_movia_motor}" alt="MOVIA Motorized Track Light" />
        </div>
      </div>
    </div>

    <!-- Application Scene Showcase -->
    <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:10px 14px; margin-top:4px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
        <strong style="color:#0f172a; font-size:12px;">Batam Luxury Villa &amp; Retail Interior Application</strong>
        <span class="mono" style="font-size:10px; color:#64748b;">UGR &lt; 10 DARK LIGHTING AMBIENCE</span>
      </div>
      <div style="width:100%; height:130px; border-radius:4px; overflow:hidden; border:1px solid #cbd5e1;">
        <img src="{img_mag_scene}" style="width:100%; height:100%; object-fit:cover;" alt="Magnetic Track Installation" />
      </div>
    </div>
  </div>

  <div class="page-foot mono">
    <div>ENCORE COMMERCIAL LIGHTING · 48V LOW-VOLTAGE PLATFORMS</div>
    <div>PAGE 03 / 04</div>
  </div>
</div>

<!-- ================= PAGE 4: CREDENTIALS & BATAM SUPPLY MODEL ================= -->
<div class="page">
  <div>
    <div class="page-nav">
      <div class="tag mono">03 / Manufacturing Pedigree &amp; Project Supply Framework</div>
      <div class="sub mono">ENCORE × ALTRON BATAM</div>
    </div>

    <div class="section-head">
      <h2 class="serif">Museum-Grade Optical Pedigree</h2>
      <p>Tested and trusted by China's most rigorous cultural institutions and luxury hotels.</p>
    </div>

    <!-- Museum Credential Banner -->
    <div class="authority-strip">
      <div>
        <h4>Proven National-Level Reference Installations</h4>
        <p>
          Encore luminaires are trusted by the <strong>National Museum of China</strong>, <strong>Sanxingdui Museum</strong>, and five-star presidential suites. Delivering strict optical consistency (SDCM &lt; 3) that flawlessly flatters Indonesian teak, stone, and luxury fabrics.
        </p>
      </div>
      <div>
        <img src="{img_museum_proof}" alt="National Museum of China Reference Installation" />
      </div>
    </div>

    <div class="section-head">
      <h2 class="serif">Dedicated Engineering Support for ALTRON Batam</h2>
      <p>A direct factory partnership designed specifically for local integrators and contractors.</p>
    </div>

    <div class="supply-box">
      <h4>Direct Integrator Support Matrix:</h4>
      <ul class="supply-list">
        <li><strong>Express Air Courier to Batam:</strong> Working evaluation samples dispatched directly to your Ruko Pasir Putih office within 7–10 days for bench testing with Orvibo &amp; Casambi gateways.</li>
        <li><strong>Complimentary DIALux 3D Lighting Simulations:</strong> Send your AutoCAD layouts; our lighting engineers provide photometric heatmaps and fixture schedules ready for your client pitches.</li>
        <li><strong>Factory-Direct Margin Protection:</strong> Direct EXW / FOB pricing ensuring healthy margins for system integration and installation services.</li>
        <li><strong>5-Year Commercial Warranty:</strong> Industrial-grade thermal dissipation with Citizen / Bridgelux COB chips guarantees zero post-handover contractor callbacks.</li>
      </ul>
    </div>
  </div>

  <div>
    <div class="contact-strip mono">
      <div>
        <strong>CONTACT:</strong> Bob · Project Director | <strong>WhatsApp:</strong> +852 6768 2519 / +852 5765171
      </div>
      <div>
        <strong>EMAIL:</strong> sales@encore-tech.com | <strong>HQ:</strong> Shenzhen, China
      </div>
    </div>
    <div class="page-foot mono">
      <div>ENCORE COMMERCIAL LIGHTING · ARCHITECTURAL SPECIFICATION DOSSIER</div>
      <div>PAGE 04 / 04</div>
    </div>
  </div>
</div>

</body>
</html>
"""

out_html = r"D:\marketing\proposals\Encore_Architectural_Dossier_ALTRON.html"
out_pdf = r"D:\marketing\proposals\Encore_Architectural_Dossier_ALTRON.pdf"

with open(out_html, "w", encoding="utf-8") as f:
    f.write(html_doc)

print(f"HTML Dossier saved to {out_html}")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///{out_html.replace(os.sep, '/')}")
    page.wait_for_load_state("networkidle")
    page.pdf(
        path=out_pdf,
        format="A4",
        print_background=True,
        margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
    )
    browser.close()

print(f"[✓] Authentic Architectural Dossier PDF successfully generated: {out_pdf}")
