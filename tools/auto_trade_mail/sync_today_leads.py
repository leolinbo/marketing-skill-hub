# -*- coding: utf-8 -*-
"""
Sync Today's Leads: 英国第三轮 (3家) + 中东阿联酋 (9家) + 中东沙特 (7家)
清理老旧测试数据，统一灌入 Encore AIDA 数据集与客户线索数据库
"""
import sqlite3
from pathlib import Path

DB_PATH = Path("d:/marketing/tools/auto_trade_mail/data/trade_mail.db")

# 19 家真实买家完整画像
TODAY_LEADS = [
    # ================= 英国第三轮 (UK Round 3) =================
    {
        "email": "contact@amdgb.com",
        "first_name": "AMD Team",
        "company": "AMD Interior Architecture",
        "title": "Commercial Interior Architects",
        "country": "United Kingdom",
        "city": "London",
        "category": "英国-第三轮",
        "project_reference": "LiGHT '26 'Lights we loved' Reel 零售换季调光方案",
        "recommended_product": "48V 磁吸轨道 / Magnetic",
        "subject_step1": "Your LIGHT '26 picks — 48V magnetic track for retail fit-outs",
        "pain_point_opener": "Saw your 'Lights we loved at LIGHT '26' reel — on commercial and retail fit-outs, are clients asking more for track systems that can be easily re-set or re-aimed between seasons without rewiring or specialist tools?",
        "product_bullets": """Our 48V Low-Voltage Magnetic Track System provides:
• Tool-Free Snap-in: Spot, linear and wall-wash modules click in instantly without breaking clean ceiling lines.
• Clean Architectural Aesthetics: Super slim 5.5mm profile made to custom lengths for British retail schemes.
• Optical Excellence: CRI 90+, 2700K–6500K Tunable White, DALI-2 compliant.
• CE / UKCA Certified: Shipped factory-direct from Shenzhen with dedicated trade project support."""
    },
    {
        "email": "beata.denton@reflexark.se",
        "first_name": "Beata",
        "company": "Beata Denton Architectural Lighting",
        "title": "Senior Lighting Designer",
        "country": "United Kingdom",
        "city": "London / Stockholm",
        "category": "英国-第三轮",
        "project_reference": "LiGHT26 强调灯具必须'按设计任务书组装定制'(assembled to the brief)",
        "recommended_product": "DELLA 模块化防眩筒灯",
        "subject_step1": "LiGHT26 follow-up // Modular fittings built to project brief",
        "pain_point_opener": "Hope you had a smooth trip back after LiGHT26! Your note emphasizing that luminaires must be 'assembled to the project brief' rather than forced standard catalog models really resonated with our engineering ethos in Shenzhen.",
        "product_bullets": """ENCORE Custom Modular Engineering offers:
• Assembled-to-Brief Architecture: 18+ trimless & flanged interchangeable bezels built around one miniature light engine.
• Glare-Free Visual Comfort: Optical cut-off delivering certified UGR < 16 for high-end hospitality and galleries.
• Precision Museum Spec: Genuine CRI 95+ (R9 > 80) preserving authentic textures and wall finishes.
• 7-Day Rapid Prototyping: Dedicated engineering team building custom optics and brackets for your brief."""
    },
    {
        "email": "hello@soitisdesign.com",
        "first_name": "Carla",
        "company": "So It Is Design Studio",
        "title": "Interiors & Landscape Lead",
        "country": "United Kingdom",
        "city": "London",
        "category": "英国-第三轮",
        "project_reference": "LiGHT '26 现场演示轨道系统探讨绿植造景与可移位光照",
        "recommended_product": "48V 磁吸轨道 + VEGA 聚光射灯",
        "subject_step1": "Your LIGHT '26 track demo // Precision lighting for planting & interiors",
        "pain_point_opener": "Saw your live track system demonstration at LiGHT26 — when integrating precision lighting with lush indoor planting schemes, is finding miniature fixtures that deliver sufficient lux without burning foliage a recurring challenge?",
        "product_bullets": """Our Biophilic & Interior Magnetic Spotlight Solution delivers:
• Cold-Beam Optical Design: Precision lens directing pure lumens onto botanical textures with minimal forward heat.
• High Photosynthetic CRI: CRI 95+ enhancing the natural vibrant greens of interior biophilic walls.
• Tool-Free Re-positioning: Move spotlights effortlessly as botanical arrangements grow or shift.
• Architectural Miniature Size: Compact 48V track seamlessly integrating into timber battens and acoustic ceilings."""
    },

    # ================= 中东 - 阿联酋 (GCC UAE) =================
    {
        "email": "info@sadeemlighting.com",
        "first_name": "Procurement Team",
        "company": "Sadeem Lighting LLC",
        "title": "Lighting & Project Contractor",
        "country": "United Arab Emirates",
        "city": "Dubai / Sharjah",
        "category": "中东-阿联酋",
        "project_reference": "Hidayath Office 黑色轨道灯 & BurJuman Mall Suwen 店",
        "recommended_product": "48V 磁吸轨道 / Magnetic",
        "subject_step1": "Attn: Project / Procurement Manager — Slim 48V magnetic track for office & retail schemes",
        "pain_point_opener": "Saw your recent retail fit-out at BurJuman Mall — on commercial store fit-outs, do clients frequently request track systems that can be re-aimed between seasons without rewiring?",
        "product_bullets": """Our 48V Magnetic Track System provides:
• Tool-Free Snap-in: Spots, linear diffusers, and wall washers click in instantly anywhere along the track.
• Ultra-Slim Architectural Profile: 5.5mm visible edge seamlessly recessing into drywall or surface mounting.
• Precision Commercial Optics: CRI 90+, DALI-2 & 0-10V dimming ready for flexible retail zoning.
• 7-Day Fast Dispatch: Core components pre-assembled for urgent commercial handover deadlines."""
    },
    {
        "email": "Moissar@pxls.ae",
        "first_name": "Moissar",
        "company": "PXLS Lighting Systems",
        "title": "Procurement / Project Lead",
        "country": "United Arab Emirates",
        "city": "Abu Dhabi",
        "category": "中东-阿联酋",
        "project_reference": "TOTO 卫浴高端展厅 (Abu Dhabi) & Supreme Council 总部",
        "recommended_product": "DELLA 深度防眩筒灯",
        "subject_step1": "TOTO showroom lighting — Deep anti-glare architectural downlights",
        "pain_point_opener": "Saw your TOTO showroom project in Abu Dhabi — sleek ceramic displays, but did specular surface glare ever compromise the clean ceiling aesthetics?",
        "product_bullets": """DELLA mini architectural downlight system offers:
• Deep Glare Control: High optical cut-off angle delivering UGR < 16 to keep commercial ceilings exceptionally comfortable.
• Museum-Grade Color: CRI 95+ (R9 > 80) preserving authentic ceramic and architectural textures without distortion.
• Modular Flexibility: Trimless & flanged interchangeable bezels fitting 50mm miniature apertures for a clean architectural finish.
• Anti-Glare Aiming: Precision honeycomb louvers and dual beam options tailored for premium retail & showroom mockups."""
    },
    {
        "email": "info@skyelume.com",
        "first_name": "Lighting Design Team",
        "company": "Skyelume",
        "title": "Lighting Consultant & Contractor",
        "country": "United Arab Emirates",
        "city": "Dubai",
        "category": "中东-阿联酋",
        "project_reference": "Trèsind 顶级餐厅 & Al Quoz Nestt",
        "recommended_product": "48V 磁吸轨道 + WASH 洗墙模组",
        "subject_step1": "Attn: Sourcing & Design Team — Hospitality wall-wash & magnetic systems",
        "pain_point_opener": "Saw your lighting scheme at Trèsind in Dubai — noticed your profile mentions partnering with global manufacturers for custom hospitality schemes. When highlighting vertical finishes, is scallop-free uniform wall washing something you find hard to source standard?",
        "product_bullets": """Our Hospitality Magnetic Wash System offers:
• Asymmetric Optical Lens: Delivering 95% uniform light beam distribution on walls right up to the ceiling line.
• Warm CCT Range: Tunable White (2200K–4000K) with CRI 95+ to elevate dining and lounge atmospheres.
• Zero Glare: Deep recessed baffle ensuring patrons never look directly into the source.
• Custom Extrusion Lengths: Made to measure for continuous linear ceiling slots."""
    },
    {
        "email": "lights@hsilighting.co.uk",
        "first_name": "Project Engineering Team",
        "company": "HSI Lighting",
        "title": "Lighting & Automation Contractor",
        "country": "United Arab Emirates",
        "city": "Dubai",
        "category": "中东-阿联酋",
        "project_reference": "Ipanema 鞋店 & Business Bay 办公空间",
        "recommended_product": "MOVIA 电机智能轨道灯 (Casambi/DALI)",
        "subject_step1": "Attn: Projects & Controls — DALI & Motorized track fixtures for UAE retail",
        "pain_point_opener": "Saw your recent commercial project at Business Bay — as a KNX & DALI member, when lighting high ceilings in retail or boardrooms, is manual ladder re-aiming becoming a client headache?",
        "product_bullets": """MOVIA Motorized Architectural Track Spotlight features:
• Remote Pan & Tilt: Precise 360° pan and 90° tilt controlled via Casambi App or DALI console from ground level.
• Optical Zoom: Seamless 15° to 55° motorized beam focus without changing physical lenses.
• Scene Recall: Store and activate lighting positions for retail seasonal displays with one tap.
• Architectural Finish: Compact housing hiding all internal motors for sleek gallery aesthetics."""
    },
    {
        "email": "sales@alamalidaa.com",
        "first_name": "Commercial Sales Team",
        "company": "Alam Alidaa Lighting LLC",
        "title": "Wholesaler & Contractor",
        "country": "United Arab Emirates",
        "city": "Abu Dhabi / Sharjah",
        "category": "中东-阿联酋",
        "project_reference": "Al Reem 岛共居公寓 TMP1 & 商业展厅",
        "recommended_product": "48V 磁吸轨道 / Magnetic",
        "subject_step1": "Attn: Commercial Sales — 48V magnetic track system for Abu Dhabi projects",
        "pain_point_opener": "Saw your commercial deliveries across Al Reem Island in Abu Dhabi — on upscale commercial ceilings, do your project clients often seek track systems that merge spots and linear lights in one seamless line?",
        "product_bullets": """Our 48V Low-Voltage Magnetic System features:
• Universal Modular Frame: Spots, linear diffusers, and pendant drops sharing one low-voltage track.
• High Visual Comfort: Black honeycomb louvers preventing side glare in hospitality and apartments.
• Direct Factory Tier-1 Pricing: Protecting your margins against local distributor markups.
• Fast Dispatch: Pre-engineered kits ready for swift GCC delivery."""
    },
    {
        "email": "info@raytecklights.com",
        "first_name": "OEM Sourcing Team",
        "company": "Rayteck Lights",
        "title": "Lighting Brand & Project Supplier",
        "country": "United Arab Emirates",
        "city": "Dubai / Sharjah",
        "category": "中东-阿联酋",
        "project_reference": "商业综合体项目 & 自有品牌 Rayteck Spot 贴牌供货",
        "recommended_product": "48V 磁吸轨道 OEM/ODM",
        "subject_step1": "Attn: OEM & Procurement — OEM magnetic track manufacturing for Rayteck",
        "pain_point_opener": "Noticed Rayteck's growing portfolio of commercial spotlights across the UAE — as you expand your own-brand catalog, are you looking for an agile factory partner capable of custom CNC extrusions and private labeling?",
        "product_bullets": """ENCORE OEM/ODM Manufacturing Capabilities:
• Laser Logo & Custom Packaging: Fully branded under Rayteck with your part numbers and carton marks.
• Stable Optical Yield: Bridgelux & Osram LEDs tested to strict 3-step MacAdam ellipse consistency.
• Flexible Volume: Low MOQ for trial project batches with volume rebates.
• GCC Climate Proofing: Engineered heat-sink dissipation handling 45°C ambient conditions."""
    },
    {
        "email": "info@mk-concept.net",
        "first_name": "Project Engineering Team",
        "company": "MK Lighting Solutions",
        "title": "Architectural Project Contractor",
        "country": "United Arab Emirates",
        "city": "Abu Dhabi",
        "category": "中东-阿联酋",
        "project_reference": "ADNOC 阿布扎比国家石油公司总部大楼完工项目",
        "recommended_product": "ATRO 商业线条灯 + DELLA 防眩筒灯",
        "subject_step1": "ADNOC HQ lighting follow-up — Architectural linear & downlights support",
        "pain_point_opener": "Saw your project delivery at ADNOC Headquarters in Abu Dhabi — on corporate headquarters of this tier, is low UGR (<16) combined with seamless continuous linear runs your primary specification priority?",
        "product_bullets": """Our Corporate Architectural Range provides:
• Continuous Seamless Lines: Light leak-proof interlocking diffusers up to 50 meters continuous run.
• High Visual Comfort: Micro-prismatic louvers achieving certified UGR < 19 for corporate work planes.
• DALI-2 Addressable: Fully compatible with Siemens & Honeywell building management systems.
• Direct Factory Sourcing: High specification standards with responsive Shenzhen engineering turnarounds."""
    },
    {
        "email": "info@lumacia.com",
        "first_name": "Lighting Design Team",
        "company": "Lumacia",
        "title": "Lighting Consultants",
        "country": "United Arab Emirates",
        "city": "Dubai",
        "category": "中东-阿联酋",
        "project_reference": "迪拜高端住宅与商业展厅 Trimless 无边框嵌灯方案",
        "recommended_product": "DELLA Trimless 无边框筒灯",
        "subject_step1": "Attn: Lighting Design Team — Trimless architectural downlights for Dubai schemes",
        "pain_point_opener": "Saw your project mockups across Dubai — noticed your design team places immense focus on immaculate ceiling plastering and discreet trimless apertures. Do traditional fittings ever cause drywall cracking during installation?",
        "product_bullets": """DELLA Trimless Architectural Downlight offers:
• Perforated Mud-in Ring: Heavy-duty die-cast aluminum frame anchoring securely into plasterboard with zero micro-cracks.
• Front-Accessible Engine: Swap drivers, reflectors, or CCT modules from below without damaging finished plaster ceilings.
• Deep Glare Cut-off: UGR < 16 ensuring invisible light sources in luxury Dubai villas.
• Sample Presentation Box: Handcrafted sample kits ready for your client board meetings."""
    },
    {
        "email": "project@flxled.com",
        "first_name": "Trading & Project Team",
        "company": "FLXLED (FLX Light Fittings)",
        "title": "Commercial Lighting Trader",
        "country": "United Arab Emirates",
        "city": "Dubai",
        "category": "中东-阿联酋",
        "project_reference": "阿联酋多处商业综合体与灯具工程进出口",
        "recommended_product": "48V 磁吸轨道 + ATRO 线条灯",
        "subject_step1": "Attn: Project Trading Team — Architectural linear & magnetic supply",
        "pain_point_opener": "Saw your recent commercial project supply across the UAE — on fast-turnaround commercial contracts, do long overseas manufacturer lead times ever eat into your handover penalties?",
        "product_bullets": """ENCORE Direct Project Supply advantages:
• 7-Day Fast Assembly: Pre-stocked profiles and optical components ready for urgent project handovers.
• Complete Project Packages: Supplying track, downlights, and continuous linear fixtures under one consolidated shipment.
• High Profit Margin: Factory-direct pricing designed specifically for project trading houses.
• Full Certification: CE, CB, and SASO-ready compliance documents for local authority approvals."""
    },

    # ================= 中东 - 沙特阿拉伯 (GCC Saudi Arabia) =================
    {
        "email": "m.lightech@gmail.com",
        "first_name": "Projects Director",
        "company": "Light Technologies (Lightech)",
        "title": "Landmark Projects Supplier",
        "country": "Saudi Arabia",
        "city": "Riyadh",
        "category": "中东-沙特",
        "project_reference": "利雅得 KAFD W酒店室内外供货、利雅得地铁 STC 站",
        "recommended_product": "DELLA 筒灯 + VEGA 切光灯",
        "subject_step1": "Attn: Projects Director — High-spec architectural downlights for KAFD & hospitality",
        "pain_point_opener": "Saw your landmark deliveries at KAFD's W Hotel and the Riyadh Metro stations — on mega-projects under Saudi Vision 2030, is securing tier-1 optical specs with low UGR while meeting strict contractor delivery milestones your biggest sourcing focus?",
        "product_bullets": """DELLA & VEGA Specification Grade Series:
• Vision 2030 Standards: CE, CB, SASO ready with certified CRI 95+ and low UGR (<16).
• High-Ambient Heat Dissipation: Heavy-duty die-cast aluminum heat sinks tested under 45°C ambient Gulf temperatures.
• Optical Shaping: Zoomable 15°–50° beam shaping and framing projectors for hospitality features.
• Direct Engineering Support: Dedicated project team in Shenzhen delivering IES files and 7-day prototype mockups."""
    },
    {
        "email": "hello@lambient.sa",
        "first_name": "Eng. Mohammed Al-Tuwaijri",
        "company": "Lambient",
        "title": "CEO & Lead Lighting Consultant",
        "country": "Saudi Arabia",
        "city": "Riyadh",
        "category": "中东-沙特",
        "project_reference": "利雅得高端设计、CEO亲自执教建筑灯光专业课程",
        "recommended_product": "48V 磁吸轨道 + Tunable White 调色温系统",
        "subject_step1": "Attn: Eng. Mohammed Al-Tuwaijri — Tunable-white architectural systems for Riyadh projects",
        "pain_point_opener": "Followed your masterclass lectures on architectural lighting design in Riyadh — noticed your deep advocacy for circadian lighting in upscale residential and corporate schemes. Is finding ultra-smooth dim-to-warm fixtures with zero flicker standard across local suppliers?",
        "product_bullets": """Our Circadian Architectural Range features:
• Ultra-Smooth Dimming: 0.1% to 100% hybrid flicker-free dimming complying with IEEE 1789 standards.
• Tunable White (2700K–6500K): True natural spectral progression tracking daylight rhythms.
• Magnetic Architectural Integration: Minimalist 48V profiles fitting flush into architectural millwork.
• Dedicated Engineer Liaison: We offer direct factory engineering dialog to match your design calculations."""
    },
    {
        "email": "info@trydolight.com",
        "first_name": "Product Development Lead",
        "company": "Trydolight Co. (VIVAX LIGHT)",
        "title": "Brand Owner & OEM Partner",
        "country": "Saudi Arabia",
        "city": "Riyadh",
        "category": "中东-沙特",
        "project_reference": "利雅得王宫地下层工程供货 & 自有品牌 VIVAX LIGHT 运营",
        "recommended_product": "OEM 蜂窝防眩筒灯 + 48V 磁吸轨道",
        "subject_step1": "Attn: Product Development / OEM — OEM honeycomb downlights for VIVAX LIGHT",
        "pain_point_opener": "Saw your prestigious palace deliveries in Riyadh and the expansion of the VIVAX LIGHT brand — as you introduce new specification downlights, are you seeking an agile OEM partner who can deliver custom tooling without exorbitant MOQs?",
        "product_bullets": """ENCORE OEM Services for VIVAX LIGHT:
• Custom Honeycomb Baffles: Precision-molded anti-glare louvers custom laser-marked with VIVAX branding.
• Pre-Wired DALI Components: Compatible with Tridonic and Philips drivers for immediate Gulf site commissioning.
• High Production Capacity: 50,000 units/month supporting Saudi government infrastructure schedules.
• Confidential Manufacturing: Strict IP protection and direct factory FOB/CIF shipping."""
    },
    {
        "email": "midmac.almsharee@gmail.com",
        "first_name": "Specification Team",
        "company": "Midmac Almasharee",
        "title": "Architectural Partner & Contractor",
        "country": "Saudi Arabia",
        "city": "Riyadh",
        "category": "中东-沙特",
        "project_reference": "利雅得北部建筑师方案合作 & 奢华独栋别墅样板工程",
        "recommended_product": "DELLA 深度防眩筒灯",
        "subject_step1": "Attn: Specification Team — Architectural downlights for Riyadh designers",
        "pain_point_opener": "Saw your active partnership programs with architects across northern Riyadh — when specifying lighting for upscale private villas, do clients frequently complain about noticeable downlight glare and ceiling clutter?",
        "product_bullets": """DELLA Miniature Downlight System provides:
• UGR < 16 Glare Protection: Deep recessed baffle ensuring light illuminates floors and art, not eyes.
• Miniature 50mm Footprint: Maximizing clean ceiling negative space.
• 18+ Trim Combinations: Round, square, flanged, trimless sharing one modular core.
• Sample Presentation Cases: Elegantly packaged wooden sample cases ready for VIP client meetings."""
    },
    {
        "email": "a.kabbani@lumitechlux.com.sa",
        "first_name": "A. Kabbani",
        "company": "Lumitech Lux",
        "title": "Project Director",
        "country": "Saudi Arabia",
        "city": "Jeddah",
        "category": "中东-沙特",
        "project_reference": "吉达滨海豪宅与商业照明方案 (Flexible Lighting)",
        "recommended_product": "48V 磁吸柔性轨道系统",
        "subject_step1": "Flexible magnetic track systems for Jeddah projects",
        "pain_point_opener": "Saw your architectural schemes in Jeddah advocating 'Flexible Lighting' — on coastal luxury schemes, do designers often demand track systems that can curve or embed seamlessly without bulky transformers?",
        "product_bullets": """Our 48V Low-Voltage Architectural Track System features:
• Seamless Ceiling Integration: Recessed plaster profiles flush with ceiling planes.
• High Corrosion Resistance: Anodized aluminum housing resilient against Jeddah coastal humidity.
• Modular Optical Choices: Spots, wall-wash, and decorative pendants snap in without wiring.
• Swift Sample Delivery: Direct air freight samples to your Jeddah office in 5 days."""
    },
    {
        "email": "sidereal2024@outlook.com",
        "first_name": "Procurement Team",
        "company": "Sidereal MiddleEast",
        "title": "Hospitality & Commercial Supplier",
        "country": "Saudi Arabia",
        "city": "Riyadh",
        "category": "中东-沙特",
        "project_reference": "利雅得国际品牌酒店与高档餐厅完工合集",
        "recommended_product": "DELLA 筒灯 + GALAXY 筒灯",
        "subject_step1": "Attn: Procurement Team — High-CRI architectural downlights for hospitality",
        "pain_point_opener": "Saw your portfolio of hospitality deliveries in Riyadh — for 5-star dining and lobbies, is sourcing high-CRI (95+) downlights with deep warm dimming (1800K–3000K) a constant contractor priority?",
        "product_bullets": """Our Hospitality Downlight Portfolio offers:
• Dim-to-Warm Natural Curve: Transitions smoothly from 3000K crisp white to 1800K candlelight warmth.
• Museum-Grade Color Fidelity: CRI 95+, Rf 92, Rg 100 rendering interior fabrics luxuriously.
• High Ceiling Atrium Option: GALAXY series up to 50W (5,000 lm) for high-ceiling hotel atriums.
• Competitive Direct Factory Pricing: Giving you a strong margin edge in competitive project bids."""
    },
    {
        "email": "marketing@lunorlighting.com",
        "first_name": "Product Development Team",
        "company": "Lunor Lighting",
        "title": "Commercial Linear Manufacturer",
        "country": "Saudi Arabia",
        "city": "Khobar / Dammam",
        "category": "中东-沙特",
        "project_reference": "沙特东部省自有品牌商业线条吊灯与建筑工程供货",
        "recommended_product": "ATRO 商业线条灯 OEM + 48V 磁吸系统",
        "subject_step1": "Attn: Product Development — OEM architectural linear manufacturing",
        "pain_point_opener": "Saw Lunor Lighting's architectural linear installations across the Eastern Province — as an ambitious Saudi brand expanding your portfolio, are you looking for an agile OEM manufacturing backer for custom aluminum linear extrusions?",
        "product_bullets": """ENCORE OEM Extrusion & Linear Capabilities:
• Seamless Interlocking Extrusions: Precision CNC aluminum channels up to 50m with seamless light diffusers.
• Complete Brand Packaging: Custom printed packaging, manuals, and labels under the Lunor brand.
• Pre-Wired Efficiency: Quick-connect push-in terminals saving 40% on-site contractor installation time.
• Direct Shenzhen Sourcing: Robust supply chain backing your project tenders across the Kingdom."""
    }
]

def sync_database():
    print("=" * 60)
    print("Connecting to trade_mail.db ...")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 1. 清理虚拟示例客户与个人测试邮箱
    print("Cleaning out old sample/test leads...")
    cur.execute("""
        DELETE FROM leads 
        WHERE email LIKE '%example.com' 
           OR email IN ('sales21@encore-tech.com', 'jklvbn598j90@gmail.com', '3348573505@qq.com', '2912281722@qq.com')
    """)
    deleted_old = cur.rowcount
    print(f"Removed {deleted_old} obsolete test leads.")

    # 2. 灌入今天的真实买家名单
    print(f"Syncing {len(TODAY_LEADS)} authentic prospective buyers into leads table...")
    inserted_cnt = 0
    updated_cnt = 0

    for l in TODAY_LEADS:
        custom_note = f"项目背景: {l['project_reference']} | 推荐产品: {l['recommended_product']}"
        cur.execute("SELECT id FROM leads WHERE lower(email) = lower(?)", (l['email'],))
        row = cur.fetchone()
        if row:
            cur.execute("""
                UPDATE leads
                SET first_name = ?, company = ?, country = ?, category = ?, custom_note = ?, status = 'active'
                WHERE id = ?
            """, (l['first_name'], l['company'], l['country'], l['category'], custom_note, row[0]))
            updated_cnt += 1
        else:
            cur.execute("""
                INSERT INTO leads (email, first_name, company, country, category, custom_note, status, current_step)
                VALUES (?, ?, ?, ?, ?, ?, 'active', 0)
            """, (l['email'], l['first_name'], l['company'], l['country'], l['category'], custom_note))
            inserted_cnt += 1

    conn.commit()

    # 查询当前客户总数
    cur.execute("SELECT COUNT(*) FROM leads")
    total_leads = cur.fetchone()[0]
    print(f"Sync finished! Inserted: {inserted_cnt}, Updated: {updated_cnt}, Total active leads in DB: {total_leads}")

    # 打印前 5 家
    cur.execute("SELECT id, email, first_name, company, country, category FROM leads ORDER BY id ASC")
    rows = cur.fetchall()
    print("\nCurrent Leads in DB:")
    for r in rows:
        print(f"ID {r[0]}: {r[1]} | {r[2]} | {r[3]} ({r[4]} - {r[5]})")

    conn.close()

if __name__ == "__main__":
    sync_database()
