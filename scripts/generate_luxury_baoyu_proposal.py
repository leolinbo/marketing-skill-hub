# -*- coding: utf-8 -*-
"""
Generate a luxury, high-aesthetic, multi-page PDF brochure tailored for ALTRON Indonesia.
Employs baoyu-design principles: refined typography, deliberate color hierarchy, modular cards,
authentic assets from Docling extracted data, and professional architectural lighting aesthetics.
"""
import os
import base64
from pathlib import Path
from patchright.sync_api import sync_playwright

asset_dir = Path(r"D:\marketing\assets\extracted_catalog_imgs")

def b64(filename):
    p = asset_dir / filename
    if p.exists():
        with open(p, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
            ext = p.suffix.lower().replace(".", "")
            if ext == "jpg": ext = "jpeg"
            return f"data:image/{ext};base64,{data}"
    return ""

img_cover_hero = b64("company_p4_img0_1770x2866.jpeg")
img_casambi_topo = b64("company_p10_img0_5352x1555.jpeg")
img_mag_system = b64("mag_p4_0_2066x1299.png")
img_mag_scene = b64("mag_p5_0_2067x1299.png")
img_della_exploded = b64("down_p4_0_1787x962.png")
img_della_optic = b64("down_p4_1_1585x1055.png")
img_cyl_pendant = b64("cyl_p4_8_1111x1476.png")
img_linear_run = b64("company_p20_img0_1280x624.jpeg")
img_museum_proj = b64("company_p15_img7_2107x925.jpeg")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Encore Lighting · Tailored Architectural Hardware Portfolio for ALTRON Indonesia</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Cinzel:wght@600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

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
    font-size: 13px;
    line-height: 1.55;
  }}

  .page {{
    width: 210mm;
    height: 297mm;
    padding: 18mm 20mm 16mm 20mm;
    margin: 0 auto;
    position: relative;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    background: #ffffff;
  }}

  /* Typography Classes */
  .font-display {{
    font-family: 'Cinzel', Georgia, serif;
    letter-spacing: 0.5px;
  }}
  .font-mono-tech {{
    font-family: 'Space Grotesk', monospace;
  }}

  /* Page 1 - Cover (Luxury Architectural Minimalist) */
  .cover {{
    background: #091319;
    color: #ffffff;
    padding: 22mm 20mm 18mm 20mm;
  }}
  .cover-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.12);
    padding-bottom: 16px;
  }}
  .brand-logo-text {{
    font-family: 'Cinzel', serif;
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #ffffff;
  }}
  .brand-logo-text span {{
    color: #38bdf8;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 300;
    font-size: 14px;
    letter-spacing: 1px;
    margin-left: 6px;
  }}
  .badge-curated {{
    font-size: 10.5px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 5px 12px;
    border-radius: 4px;
    background: rgba(56, 189, 248, 0.1);
    border: 1px solid rgba(56, 189, 248, 0.28);
    color: #38bdf8;
    font-weight: 600;
  }}
  .cover-body {{
    margin-top: 26px;
  }}
  .cover-kicker {{
    font-size: 11.5px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #94a3b8;
    margin-bottom: 12px;
    font-weight: 600;
  }}
  .cover-headline {{
    font-size: 34px;
    line-height: 1.2;
    color: #ffffff;
    margin: 0 0 16px 0;
    font-weight: 700;
  }}
  .cover-headline span {{
    color: #38bdf8;
    font-style: italic;
  }}
  .cover-desc {{
    font-size: 13.5px;
    color: #94a3b8;
    line-height: 1.65;
    max-width: 530px;
    margin-bottom: 22px;
  }}
  .cover-hero-img-wrap {{
    width: 100%;
    height: 250px;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 25px 40px -15px rgba(0,0,0,0.6);
    margin-bottom: 24px;
  }}
  .cover-hero-img-wrap img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .client-brief-card {{
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 8px;
    padding: 14px 18px;
    display: grid;
    grid-template-columns: 1.25fr 1fr;
    gap: 16px;
    font-size: 11.5px;
  }}
  .client-brief-col h5 {{
    margin: 0 0 4px 0;
    color: #38bdf8;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .cover-bottom {{
    border-top: 1px solid rgba(255,255,255,0.08);
    padding-top: 12px;
    display: flex;
    justify-content: space-between;
    font-size: 10.5px;
    color: #64748b;
  }}

  /* Inner Pages Common Structure */
  .inner-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    border-bottom: 1.5px solid #0f172a;
    padding-bottom: 8px;
    margin-bottom: 16px;
  }}
  .inner-header .section-tag {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #0284c7;
  }}
  .inner-header .target-mark {{
    font-size: 11px;
    color: #64748b;
  }}

  .section-intro {{
    margin-bottom: 14px;
  }}
  .section-intro h2 {{
    font-family: 'Cinzel', serif;
    font-size: 21px;
    color: #0f172a;
    margin: 0 0 4px 0;
  }}
  .section-intro p {{
    margin: 0;
    font-size: 12.5px;
    color: #475569;
  }}

  /* Casambi Callout */
  .casambi-panel {{
    background: #0b1720;
    color: #f1f5f9;
    border-radius: 8px;
    padding: 14px 16px;
    margin-bottom: 16px;
    display: grid;
    grid-template-columns: 1.4fr 1fr;
    gap: 16px;
    align-items: center;
  }}
  .casambi-panel h4 {{
    margin: 0 0 4px 0;
    font-size: 13.5px;
    color: #38bdf8;
  }}
  .casambi-panel p {{
    margin: 0;
    font-size: 11.5px;
    color: #94a3b8;
    line-height: 1.5;
  }}
  .casambi-panel img {{
    width: 100%;
    height: 82px;
    object-fit: cover;
    border-radius: 6px;
    border: 1px solid rgba(255,255,255,0.15);
  }}

  /* 2-Column Product Grids */
  .grid-dual {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 14px;
  }}
  .card-module {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 13px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .card-module-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 6px;
  }}
  .card-title {{
    font-size: 13.5px;
    font-weight: 700;
    color: #0f172a;
  }}
  .pill {{
    font-size: 10px;
    font-weight: 600;
    padding: 2px 7px;
    border-radius: 4px;
  }}
  .pill-blue {{
    background: #e0f2fe;
    color: #0369a1;
  }}
  .pill-teal {{
    background: #ccfbf1;
    color: #0f766e;
  }}
  .pill-amber {{
    background: #fef3c7;
    color: #b45309;
  }}
  .card-desc {{
    font-size: 11.5px;
    color: #475569;
    margin-bottom: 8px;
    line-height: 1.5;
  }}
  .spec-mini-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 11px;
    margin-bottom: 10px;
  }}
  .spec-mini-table td {{
    padding: 4px 6px;
    border-bottom: 1px solid #e2e8f0;
    color: #334155;
  }}
  .spec-mini-table td.label {{
    color: #64748b;
    font-weight: 600;
    width: 42%;
  }}
  .card-img {{
    width: 100%;
    height: 135px;
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid #e2e8f0;
  }}
  .card-img img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}

  /* Page Footer */
  .inner-footer {{
    border-top: 1px solid #e2e8f0;
    padding-top: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 10.5px;
    color: #94a3b8;
  }}

  /* Page 3 Highlights & Cooperation */
  .authority-banner {{
    background: #f1f5f9;
    border-left: 4px solid #0284c7;
    border-radius: 0 8px 8px 0;
    padding: 12px 16px;
    margin-bottom: 16px;
    display: grid;
    grid-template-columns: 1.4fr 1fr;
    gap: 14px;
    align-items: center;
  }}
  .authority-banner h4 {{
    margin: 0 0 4px 0;
    font-size: 13px;
    color: #0369a1;
  }}
  .authority-banner p {{
    margin: 0;
    font-size: 11.5px;
    color: #334155;
  }}
  .authority-banner img {{
    width: 100%;
    height: 75px;
    object-fit: cover;
    border-radius: 5px;
    border: 1px solid #cbd5e1;
  }}

  .service-box {{
    background: #fafaf9;
    border: 1px dashed #0284c7;
    border-radius: 8px;
    padding: 14px 16px;
    margin-bottom: 14px;
  }}
  .service-box h4 {{
    margin: 0 0 6px 0;
    font-size: 13px;
    color: #0369a1;
  }}
  .service-list {{
    margin: 0;
    padding-left: 18px;
    font-size: 11.5px;
    color: #334155;
  }}
  .service-list li {{
    margin-bottom: 4px;
  }}

  .contact-bar {{
    background: #0f172a;
    color: #ffffff;
    border-radius: 6px;
    padding: 10px 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 11px;
    margin-bottom: 6px;
  }}
  .contact-bar strong {{
    color: #38bdf8;
  }}
</style>
</head>
<body>

<!-- ================= PAGE 1: COVER & EXECUTIVE SUMMARY ================= -->
<div class="page cover">
  <div class="cover-header">
    <div class="brand-logo-text">ENCORE <span>COMMERCIAL LIGHTING</span></div>
    <div class="badge-curated">Targeted Architectural Curation</div>
  </div>

  <div class="cover-body">
    <div class="cover-kicker font-mono-tech">EXCLUSIVE PROPOSAL · BATAM REGION 2026</div>
    <h1 class="cover-headline font-display">Architectural Hardware Curation for <span>Smart Living</span> &amp; Villas</h1>
    <div class="cover-desc">
      Engineered for premium lighting consultants and smart system integrators. Native deep-dimming pairing with <strong>Casambi Wireless BLE, DALI-2, 0-10V, and Phase-cut</strong> protocols without flicker or acoustic noise.
    </div>

    <div class="cover-hero-img-wrap">
      <img src="{img_cover_hero}" alt="Architectural Lighting Atmosphere" />
    </div>

    <div class="client-brief-card">
      <div class="client-brief-col">
        <h5>Prepared Specifically For</h5>
        <strong style="color:#ffffff; font-size:13px;">ALTRON Indonesia</strong><br>
        📍 Ruko Pasir Putih A6 No. 88, Sadai, Bengkong, Batam<br>
        Smart Home &amp; Lighting Integration Specialist (Orvibo &amp; Yeelight Partner)
      </div>
      <div class="client-brief-col">
        <h5>Direct Manufacturer Support</h5>
        <strong style="color:#ffffff; font-size:13px;">Encore Commercial Lighting (Encore-Tech)</strong><br>
        Engineering &amp; Factory: Shenzhen, China<br>
        Credential: National Museum of China &amp; Luxury Hospitality Supplier
      </div>
    </div>
  </div>

  <div class="cover-bottom font-mono-tech">
    <div>REF: ENC-ID-ALT2026 · CONFIDENTIAL FOR ALTRON TEAM</div>
    <div>WWW.ENCORE-TECH.COM</div>
  </div>
</div>

<!-- ================= PAGE 2: CASAMBI & 48V MAGNETIC TRACK SYSTEM ================= -->
<div class="page">
  <div>
    <div class="inner-header">
      <div class="section-tag">01 / Smart Control Synergy &amp; 48V Magnetic Track</div>
      <div class="target-mark font-mono-tech">ENCORE × ALTRON BATAM</div>
    </div>

    <div class="section-intro">
      <h2 class="font-display">Certified Smart Dimming Architecture</h2>
      <p>Precision-engineered drivers eliminating low-end shimmer, steps, and transformer coil buzz.</p>
    </div>

    <div class="casambi-panel">
      <div>
        <h4>⚡ Certified Casambi Wireless Mesh &amp; DALI-2 Driver Integration</h4>
        <p>
          Encore fixtures are tested across full 0.1%–100% dimming curves. Natively compatible with Casambi Bluetooth mesh and DALI-2 broadcast/addressable systems, enabling individual module tuning directly from touch panels and mobile apps.
        </p>
      </div>
      <div>
        <img src="{img_casambi_topo}" alt="Casambi Smart Control Diagram" />
      </div>
    </div>

    <div class="section-intro">
      <h2 class="font-display">48V Ultra-Slim Magnetic Track Platform</h2>
      <p>Low-voltage architectural rail platform with trimless recessed, surface, and pendant mounting.</p>
    </div>

    <div class="grid-dual">
      <!-- Card A: Recessed Trimless -->
      <div class="card-module">
        <div>
          <div class="card-module-header">
            <span class="card-title">Trimless Recessed Profiles</span>
            <span class="pill pill-blue">Casambi / DALI</span>
          </div>
          <div class="card-desc">
            Embedded into gypsum false ceilings for a clean zero-trim appearance. Ladder-type extrusion prevents copper sliding during long thermal cycles.
          </div>
          <table class="spec-mini-table">
            <tr><td class="label">Working Voltage</td><td>Safe 48V DC Low Voltage</td></tr>
            <tr><td class="label">Copper Busbar</td><td>0.8mm High-Purity Red Copper</td></tr>
            <tr><td class="label">Dimming Options</td><td>Casambi BLE / DALI / 0-10V</td></tr>
            <tr><td class="label">Finishes</td><td>Architectural Matte Black / White</td></tr>
          </table>
        </div>
        <div class="card-img">
          <img src="{img_mag_system}" alt="Magnetic Track Profiles" />
        </div>
      </div>

      <!-- Card B: Interchangeable Modules -->
      <div class="card-module">
        <div>
          <div class="card-module-header">
            <span class="card-title">Modular Click-in Luminaires</span>
            <span class="pill pill-teal">UGR &lt; 10 Darklight</span>
          </div>
          <div class="card-desc">
            Instant tool-free hot swap. Combine optical spot lenses (15°/24°/36°), opal linear diffusers, and micro-louvers within the same track.
          </div>
          <table class="spec-mini-table">
            <tr><td class="label">Optical Quality</td><td>CRI 95+ | R9 &gt; 80 | SDCM &lt; 3</td></tr>
            <tr><td class="label">Color Temp (CCT)</td><td>2700K / 3000K / 4000K / Tunable</td></tr>
            <tr><td class="label">Aesthetics</td><td>Micro Darklight Anti-Glare</td></tr>
            <tr><td class="label">Application</td><td>Batam Villas, Salons &amp; Showrooms</td></tr>
          </table>
        </div>
        <div class="card-img">
          <img src="{img_mag_scene}" alt="Magnetic Track Application Scene" />
        </div>
      </div>
    </div>
  </div>

  <div class="inner-footer font-mono-tech">
    <div>ENCORE COMMERCIAL LIGHTING · 48V LOW-VOLTAGE PLATFORM</div>
    <div>PAGE 02 / 03</div>
  </div>
</div>

<!-- ================= PAGE 3: DOWNLIGHTS, CYLINDERS & PARTNERSHIP ================= -->
<div class="page">
  <div>
    <div class="inner-header">
      <div class="section-tag">02 / Architectural Downlights, Cylinders &amp; Project Support</div>
      <div class="target-mark font-mono-tech">ENCORE × ALTRON BATAM</div>
    </div>

    <div class="section-intro">
      <h2 class="font-display">DELLA 2.0 Pinhole Darklight Downlights</h2>
      <p>"See the light, not the source" — deep baffle shielding for tranquil luxury interior ceilings.</p>
    </div>

    <div class="grid-dual">
      <!-- Card C: DELLA Downlight -->
      <div class="card-module">
        <div>
          <div class="card-module-header">
            <span class="card-title">DELLA 2.0 Architectural Series</span>
            <span class="pill pill-teal">UGR &lt; 6 Visual Comfort</span>
          </div>
          <div class="card-desc">
            Deep secondary reflector design eliminates distracting ceiling glare. Specially tuned low-end dimming down to 0.1% for bedroom and cinema scenes.
          </div>
          <table class="spec-mini-table">
            <tr><td class="label">Apertures</td><td>DM30 (1.25") / DM50 (2") / DM60 (3")</td></tr>
            <tr><td class="label">Wattage</td><td>5W–8W (400lm) to 15W (1200lm)</td></tr>
            <tr><td class="label">Beams</td><td>15° / 24° / 38° / Wall Wash</td></tr>
          </table>
        </div>
        <div class="card-img">
          <img src="{img_della_exploded}" alt="DELLA Downlight Exploded View" />
        </div>
      </div>

      <!-- Card D: NOVA Cylinders & Linear -->
      <div class="card-module">
        <div>
          <div class="card-module-header">
            <span class="card-title">NOVA Cylinders &amp; ARTO Linear</span>
            <span class="pill pill-amber">Architectural Accents</span>
          </div>
          <div class="card-desc">
            Invisible retractable wire lock without visible canopy screws. Ideal for dining table islands, reception desks, and modern bar counters.
          </div>
          <table class="spec-mini-table">
            <tr><td class="label">Diameters</td><td>Φ30mm / Φ45mm / Φ60mm Cylinders</td></tr>
            <tr><td class="label">Luxury Finishes</td><td>Champagne Gold / Bronze / Black</td></tr>
            <tr><td class="label">Linear System</td><td>ARTO 1 &amp; SLEM 1.7 Continuous Run</td></tr>
          </table>
        </div>
        <div class="card-img">
          <img src="{img_cyl_pendant}" alt="NOVA Cylinders and Pendants" />
        </div>
      </div>
    </div>

    <!-- Museum Credential Banner -->
    <div class="authority-banner">
      <div>
        <h4>Museum-Grade Optical Pedigree</h4>
        <p>
          Encore optics are trusted by the <strong>National Museum of China</strong>, <strong>Sanxingdui Museum</strong>, and high-end hotel presidential suites. Flawlessly reveals natural Indonesian teak wood, marble veining, and art textures.
        </p>
      </div>
      <div>
        <img src="{img_museum_proj}" alt="National Museum of China Reference Project" />
      </div>
    </div>

    <!-- Tailored Supply Model for ALTRON -->
    <div class="service-box">
      <h4>Direct Engineering &amp; Supply Support for ALTRON Batam:</h4>
      <ul class="service-list">
        <li><strong>Rapid Working Samples (Air Courier):</strong> Door-to-door air courier to Batam (within 7–10 days) for showroom display and bench testing with Orvibo &amp; Casambi hubs.</li>
        <li><strong>Complimentary DIALux 3D Lighting Design:</strong> Send us your AutoCAD floorplans; our engineering team provides complete photometric calculations and fixture schedules.</li>
        <li><strong>Direct Manufacturer Pricing:</strong> Healthy wholesale &amp; project margins for your engineering installations.</li>
        <li><strong>5-Year Commercial Warranty:</strong> Industrial-grade thermal dissipation with Bridgelux/Citizen LED chips ensures zero post-handover maintenance headaches.</li>
      </ul>
    </div>
  </div>

  <div>
    <div class="contact-bar font-mono-tech">
      <div>
        <strong>CONTACT:</strong> Bob · Project Director | <strong>WhatsApp:</strong> +852 6768 2519 / +852 5765171
      </div>
      <div>
        <strong>EMAIL:</strong> sales@encore-tech.com | <strong>HQ:</strong> Shenzhen, China
      </div>
    </div>
    <div class="inner-footer font-mono-tech">
      <div>ENCORE COMMERCIAL LIGHTING · ARCHITECTURAL PROJECT CURATION</div>
      <div>PAGE 03 / 03</div>
    </div>
  </div>
</div>

</body>
</html>
"""

html_out_path = r"D:\marketing\proposals\Encore_ALTRON_Batam_Proposal.html"
pdf_out_path = r"D:\marketing\proposals\Encore_ALTRON_Batam_Proposal.pdf"

with open(html_out_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML written to {html_out_path}")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///{html_out_path.replace(os.sep, '/')}")
    page.wait_for_load_state("networkidle")
    page.pdf(
        path=pdf_out_path,
        format="A4",
        print_background=True,
        margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
    )
    browser.close()

print(f"Luxury PDF generated successfully at {pdf_out_path}")
