# -*- coding: utf-8 -*-
import os
import base64
from patchright.sync_api import sync_playwright

def get_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            b = base64.b64encode(f.read()).decode("utf-8")
            ext = os.path.splitext(path)[1].lower().replace(".", "")
            if ext == "jpg": ext = "jpeg"
            return f"data:image/{ext};base64,{b}"
    return ""

d = r"D:\marketing\assets\extracted_catalog_imgs"

img_hero = get_b64(os.path.join(d, "company_p4_img0_1770x2866.jpeg"))
img_casambi_system = get_b64(os.path.join(d, "company_p10_img0_5352x1555.jpeg"))
img_mag_track = get_b64(os.path.join(d, "mag_p4_0_2066x1299.png"))
img_mag_scene = get_b64(os.path.join(d, "mag_p5_0_2067x1299.png"))
img_down_della = get_b64(os.path.join(d, "down_p4_0_1787x962.png"))
img_down_optic = get_b64(os.path.join(d, "down_p4_1_1585x1055.png"))
img_cyl_linear = get_b64(os.path.join(d, "cyl_p3_5_1300x743.png"))
img_museum_ref = get_b64(os.path.join(d, "company_p15_img7_2107x925.jpeg"))

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Encore Lighting - Curated Architectural Hardware for ALTRON Indonesia</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap');

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
    background: #f8fafc;
    margin: 0;
    padding: 0;
    font-size: 13px;
    line-height: 1.6;
  }}

  .page {{
    width: 210mm;
    min-height: 297mm;
    height: 297mm;
    padding: 20mm 20mm 18mm 20mm;
    margin: 0 auto;
    background: #ffffff;
    position: relative;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
  }}

  /* Page 1 - Cover */
  .cover-page {{
    background: linear-gradient(135deg, #091e28 0%, #0d2836 60%, #11384a 100%);
    color: #ffffff;
    padding: 24mm 22mm 20mm 22mm;
  }}

  .cover-top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.15);
    padding-bottom: 16px;
  }}

  .brand-logo {{
    font-size: 24px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #ffffff;
  }}

  .brand-logo span {{
    color: #38bdf8;
    font-weight: 300;
  }}

  .doc-tag {{
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    padding: 6px 14px;
    background: rgba(56, 189, 248, 0.12);
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-radius: 20px;
    color: #38bdf8;
    font-weight: 600;
  }}

  .cover-middle {{
    margin-top: 36px;
  }}

  .hero-badge {{
    display: inline-block;
    color: #cbd5e1;
    font-size: 12px;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-bottom: 14px;
    font-weight: 600;
  }}

  .cover-title {{
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 34px;
    line-height: 1.25;
    font-weight: 700;
    margin: 0 0 18px 0;
    color: #ffffff;
  }}

  .cover-title em {{
    font-style: italic;
    color: #38bdf8;
  }}

  .cover-subtitle {{
    font-size: 14px;
    color: #94a3b8;
    max-width: 520px;
    line-height: 1.7;
    margin-bottom: 28px;
  }}

  .hero-img-box {{
    width: 100%;
    height: 220px;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 20px 35px -10px rgba(0,0,0,0.5);
    margin-bottom: 30px;
  }}

  .hero-img-box img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}

  .target-client-card {{
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    backdrop-filter: blur(10px);
    border-radius: 8px;
    padding: 16px 20px;
    display: grid;
    grid-template-columns: 1.4fr 1fr;
    gap: 15px;
    font-size: 12px;
  }}

  .client-col strong {{
    display: block;
    color: #38bdf8;
    font-size: 13px;
    margin-bottom: 3px;
  }}

  .cover-footer {{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid rgba(255,255,255,0.1);
    padding-top: 14px;
    font-size: 11px;
    color: #64748b;
  }}

  /* Inner Pages Standard Layout */
  .page-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid #0f172a;
    padding-bottom: 10px;
    margin-bottom: 18px;
  }}

  .page-header-left {{
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #0369a1;
  }}

  .page-header-right {{
    font-size: 11px;
    color: #94a3b8;
  }}

  .section-headline {{
    margin-bottom: 14px;
  }}

  .section-headline h2 {{
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 22px;
    color: #0f172a;
    margin: 0 0 6px 0;
    font-weight: 700;
  }}

  .section-headline p {{
    font-size: 12.5px;
    color: #475569;
    margin: 0;
  }}

  /* Content Cards */
  .grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 16px;
  }}

  .feature-box {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 14px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
  }}

  .feature-box.highlight {{
    background: #f0fdf4;
    border-color: #bbf7d0;
  }}

  .feature-title {{
    font-size: 13.5px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .badge-tag {{
    display: inline-block;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 10.5px;
    font-weight: 600;
    background: #e0f2fe;
    color: #0369a1;
  }}

  .badge-tag.green {{
    background: #dcfce7;
    color: #15803d;
  }}

  .feature-desc {{
    font-size: 12px;
    color: #475569;
    margin-bottom: 10px;
  }}

  .img-showcase {{
    width: 100%;
    height: 145px;
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
    margin-top: 8px;
  }}

  .img-showcase img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}

  .spec-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 11.5px;
    margin-top: 10px;
  }}

  .spec-table th {{
    background: #f1f5f9;
    padding: 6px 10px;
    text-align: left;
    color: #334155;
    font-weight: 600;
    border-bottom: 1px solid #cbd5e1;
  }}

  .spec-table td {{
    padding: 6px 10px;
    border-bottom: 1px solid #e2e8f0;
    color: #475569;
  }}

  .spec-table tr:last-child td {{
    border-bottom: none;
  }}

  .page-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #e2e8f0;
    padding-top: 10px;
    font-size: 10.5px;
    color: #94a3b8;
  }}

  .casambi-banner {{
    background: #0f172a;
    color: #ffffff;
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 16px;
    display: flex;
    gap: 16px;
    align-items: center;
  }}

  .casambi-banner-left {{
    flex: 1.4;
  }}

  .casambi-banner-left h4 {{
    margin: 0 0 4px 0;
    font-size: 14px;
    color: #38bdf8;
  }}

  .casambi-banner-left p {{
    margin: 0;
    font-size: 11.5px;
    color: #cbd5e1;
    line-height: 1.5;
  }}

  .casambi-banner-right {{
    flex: 1;
    height: 90px;
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.15);
  }}

  .casambi-banner-right img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}

  .closing-card {{
    background: #f8fafc;
    border: 1.5px dashed #0284c7;
    border-radius: 8px;
    padding: 16px;
    margin-top: 10px;
  }}

  .closing-title {{
    font-size: 14px;
    font-weight: 700;
    color: #0369a1;
    margin-bottom: 6px;
  }}
</style>
</head>
<body>

<!-- PAGE 1: COVER & EXECUTIVE SUMMARY -->
<div class="page cover-page">
  <div class="cover-top">
    <div class="brand-logo">ENCORE <span>LIGHTING</span></div>
    <div class="doc-tag">Architectural Hardware Portfolio 2026</div>
  </div>

  <div class="cover-middle">
    <div class="hero-badge">Smart Home Hardware Integration · Batam Region</div>
    <h1 class="cover-title">Precision Architectural Lighting for <em>Smart Living</em> &amp; Villa Spaces</h1>
    <div class="cover-subtitle">
      Engineered specifically for system integrators and lighting consultants. High-CRI luminaires natively paired with <strong>Casambi Wireless BLE, DALI-2, 0-10V, and Phase-cut (Triac)</strong> dimming ecosystems.
    </div>

    <div class="hero-img-box">
      <img src="{img_hero}" alt="Architectural Ambience" />
    </div>

    <div class="target-client-card">
      <div class="client-col">
        <strong>Curated Specifically For:</strong>
        ALTRON Indonesia (Orvibo &amp; Smart Home Specialist)<br>
        📍 Ruko Pasir Putih A6 No. 88, Bengkong, Sadai, Batam<br>
        Focus: Luxury Villas, Boutique Retail &amp; Showroom Integration
      </div>
      <div class="client-col">
        <strong>Engineering &amp; Manufacturing:</strong>
        Encore Commercial Lighting (Encore-Tech)<br>
        Engineering HQ: Shenzhen, China<br>
        Authority: National Museum of China &amp; Luxury Hospitality
      </div>
    </div>
  </div>

  <div class="cover-footer">
    <div>CONFIDENTIAL &amp; PROPRIETARY · PREPARED FOR ALTRON INDONESIA</div>
    <div>WWW.ENCORE-TECH.COM</div>
  </div>
</div>

<!-- PAGE 2: CASAMBI & CONTROL SYSTEM COMPATIBILITY + 48V MAGNETIC TRACK -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="page-header-left">01 / Smart Control Integration &amp; 48V Magnetic Track</div>
      <div class="page-header-right">Encore × ALTRON Batam</div>
    </div>

    <div class="section-headline">
      <h2>Seamless Control Protocol Architecture</h2>
      <p>Eliminate flicker, step-dimming, and acoustic driver buzz. Certified low-end 0.1% dimming stability.</p>
    </div>

    <div class="casambi-banner">
      <div class="casambi-banner-left">
        <h4>⚡ Certified Casambi BLE &amp; DALI-2 Driver Integration</h4>
        <p>
          Encore fixtures are tested across full dimming ranges with Casambi Bluetooth mesh and DALI-2 broadcast/addressable controls. Perfect for villa master suites and boutique shops requiring seamless smartphone, keypad, and sensor automation.
        </p>
      </div>
      <div class="casambi-banner-right">
        <img src="{img_casambi_system}" alt="Casambi Integration" />
      </div>
    </div>

    <div class="section-headline" style="margin-top: 18px;">
      <h2>48V Ultra-Slim Magnetic Track System</h2>
      <p>Architectural flexibility with trimless recessed, surface-mount, and suspended low-voltage rails.</p>
    </div>

    <div class="grid-2">
      <div class="feature-box">
        <div class="feature-title">
          <span>Recessed Trimless System</span>
          <span class="badge-tag">Casambi / DALI</span>
        </div>
        <div class="feature-desc">
          Integrated directly into false ceilings before plastering. Flushes with gypsum boards to deliver pure, uninterrupted architectural ceiling planes.
        </div>
        <table class="spec-table">
          <tr><th>Operating Voltage</th><td>Safe 48V DC Low Voltage</td></tr>
          <tr><th>Copper Busbar</th><td>High-purity Red Copper (0.8mm)</td></tr>
          <tr><th>Dimming Support</th><td>Casambi Wireless / DALI / 0-10V</td></tr>
        </table>
        <div class="img-showcase">
          <img src="{img_mag_track}" alt="Magnetic Track Profiles" />
        </div>
      </div>

      <div class="feature-box">
        <div class="feature-title">
          <span>Click-in Modular Versatility</span>
          <span class="badge-tag green">UGR &lt; 10 Darklight</span>
        </div>
        <div class="feature-desc">
          Tool-free, instant repositioning. Mix and match adjustable spot lenses (15°/24°/36°), opal linear ambient bars, and micro-louvers within seconds.
        </div>
        <table class="spec-table">
          <tr><th>Color Quality</th><td>CRI 95+ | R9 &gt; 80 | SDCM &lt; 3</td></tr>
          <tr><th>CCT Choices</th><td>2700K / 3000K / 4000K / Tunable</td></tr>
          <tr><th>Application</th><td>Batam Modern Villas &amp; Showrooms</td></tr>
        </table>
        <div class="img-showcase">
          <img src="{img_mag_scene}" alt="Magnetic Light Applications" />
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <div>ENCORE COMMERCIAL LIGHTING · 48V MAGNETIC TRACK PLATFORM</div>
    <div>PAGE 02</div>
  </div>
</div>

<!-- PAGE 3: DOWNLIGHTS, CYLINDERS & PROJECT COOPERATION -->
<div class="page">
  <div>
    <div class="page-header">
      <div class="page-header-left">02 / Architectural Downlights &amp; Batam Service Model</div>
      <div class="page-header-right">Encore × ALTRON Batam</div>
    </div>

    <div class="section-headline">
      <h2>DELLA 2.0 Darklight Downlight System</h2>
      <p>"See the light, not the source" — deep pinhole shielding for quiet, glare-free ceiling design.</p>
    </div>

    <div class="grid-2">
      <div class="feature-box">
        <div class="feature-title">
          <span>Pinhole Anti-Glare Optics</span>
          <span class="badge-tag">UGR &lt; 6 Visual Comfort</span>
        </div>
        <div class="feature-desc">
          Deep recessed aluminum heatsink with secondary baffle. The ceiling remains clean without the blinding glow typical of standard commercial downlights.
        </div>
        <table class="spec-table">
          <tr><th>Aperture Sizes</th><td>DM30 (1.25") / DM50 (2") / DM60 (3")</td></tr>
          <tr><th>Wattage / Lumen</th><td>5W–8W (400lm) to 15W (1200lm)</td></tr>
          <tr><th>Beam Options</th><td>Narrow 15° / Medium 24° / Wide 38°</td></tr>
        </table>
        <div class="img-showcase">
          <img src="{img_down_della}" alt="DELLA Downlight" />
        </div>
      </div>

      <div class="feature-box">
        <div class="feature-title">
          <span>Museum-Grade Color Rendering</span>
          <span class="badge-tag green">National Museum Spec</span>
        </div>
        <div class="feature-desc">
          Engineered with identical optical standards developed for the National Museum of China. Flawlessly reveals natural stone, teak wood, and artwork.
        </div>
        <table class="spec-table">
          <tr><th>Driver Options</th><td>Casambi BLE / DALI-2 / Phase-cut</td></tr>
          <tr><th>Dimming Depth</th><td>Down to 0.1% Smooth Fade-to-Black</td></tr>
          <tr><th>Circadian Option</th><td>Tunable White (1800K–6500K)</td></tr>
        </table>
        <div class="img-showcase">
          <img src="{img_down_optic}" alt="Optics & Light Quality" />
        </div>
      </div>
    </div>

    <div class="section-headline" style="margin-top: 14px;">
      <h2>Project Supply Model for ALTRON Indonesia</h2>
      <p>Direct manufacturer support tailored for Batam integrators and contractors.</p>
    </div>

    <div class="closing-card">
      <div class="closing-title">Why Partner Directly with Encore Factory?</div>
      <div style="font-size: 12px; color: #334155; line-height: 1.6;">
        • <strong>Fast Express Courier to Batam:</strong> Working samples and demo kits air-shipped to your Ruko Pasir Putih office within 7–10 days.<br>
        • <strong>Free DIALux Lighting Simulations:</strong> Provide your CAD drawings; our optical team generates comprehensive 3D lux calculations and luminaire schedules for your client presentations.<br>
        • <strong>Healthy Integrator Margins:</strong> Direct-from-factory FOB/EXW pricing provides substantial commercial margins compared to buying from intermediate distributors.<br>
        • <strong>5-Year Commercial Warranty:</strong> Robust thermal dissipation and Tier-1 LED chips (Citizen / Bridgelux) ensure zero post-handover callbacks.
      </div>
    </div>
  </div>

  <div>
    <div style="display: flex; justify-content: space-between; align-items: flex-end; background: #f1f5f9; padding: 10px 14px; border-radius: 6px; font-size: 11px; margin-bottom: 8px;">
      <div>
        <strong>Contact Person:</strong> Bob · Project Director<br>
        <strong>Email:</strong> sales@encore-tech.com / sales21@encore-tech.com<br>
        <strong>WhatsApp:</strong> +852 6768 2519 / +852 5765171
      </div>
      <div style="text-align: right;">
        <strong>Web:</strong> www.encore-tech.com<br>
        <strong>Factory:</strong> Shenzhen, China<br>
        <strong>Hong Kong HQ:</strong> Tsim Sha Tsui, Kowloon
      </div>
    </div>
    <div class="page-footer">
      <div>ENCORE COMMERCIAL LIGHTING · ARCHITECTURAL SPECIFICATION PROPOSAL</div>
      <div>PAGE 03</div>
    </div>
  </div>
</div>

</body>
</html>
"""

html_out = r"D:\marketing\proposals\Encore_Architectural_Proposal_ALTRON.html"
pdf_out = r"D:\marketing\proposals\Encore_Architectural_Proposal_ALTRON.pdf"

with open(html_out, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Targeted HTML written to {html_out}")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///{html_out.replace(os.sep, '/')}")
    page.wait_for_load_state("networkidle")
    page.pdf(
        path=pdf_out,
        format="A4",
        print_background=True,
        margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
    )
    browser.close()

print(f"High-aesthetic PDF generated successfully at {pdf_out}")
