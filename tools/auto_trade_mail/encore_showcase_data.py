# -*- coding: utf-8 -*-
"""
Encore Lighting Project Showcase & AIDA Cadence Data
提供 4 阶段跟进体系模版、真实买家线索库及本地网盘资源对应
"""
import os
import base64

ICONS_DIR = r"\\192.168.1.18\市场部\部门资料\11、社媒运营标准资料\01 标准资料\02 社媒图标"
BANNER_DIR = r"\\192.168.1.18\市场部\市场部——业务部\02 营销资料\06 2026邮件推广图片(邮签)"

# 产品与对应网盘推荐图映射
PRODUCT_BANNER_MAP = {
    "DELLA": os.path.join(BANNER_DIR, r"DELLA\DELLA-mini.jpg"),
    "48V 磁吸轨道 / Magnetic": os.path.join(BANNER_DIR, r"Magnetic\Magnetic-1.jpg") if os.path.exists(os.path.join(BANNER_DIR, r"Magnetic\Magnetic-1.jpg")) else "",
    "VEGA": os.path.join(BANNER_DIR, r"VEGA\VEGA-1.jpg") if os.path.exists(os.path.join(BANNER_DIR, r"VEGA\VEGA-1.jpg")) else "",
    "AVA": os.path.join(BANNER_DIR, r"AVA\AVA-1.jpg") if os.path.exists(os.path.join(BANNER_DIR, r"AVA\AVA-1.jpg")) else "",
    "ELLA": os.path.join(BANNER_DIR, r"ELLA\ELLA-1.jpg") if os.path.exists(os.path.join(BANNER_DIR, r"ELLA\ELLA-1.jpg")) else "",
    "GALAXY": os.path.join(BANNER_DIR, r"GALAXY\GALAXY-1.jpg") if os.path.exists(os.path.join(BANNER_DIR, r"GALAXY\GALAXY-1.jpg")) else "",
}

# 4 阶段自动化跟进体系定义
ENCORE_SEQUENCES = [
    {
        "step_number": 1,
        "step_name": "Step 1: 痛点疑问开场 (轻量纯文本·高进箱率)",
        "delay_days": 0,
        "is_thread_reply": 0,
        "subject": "{subject_step1}",
        "body_template": """Hi {first_name},

{pain_point_opener}

We build architectural fixtures in Shenzhen specifically engineered to solve these optical and installation challenges for commercial contractors and project designers.

Would a quick spec sheet or a couple of project mock-up photos be useful to see how other schemes handle this?

Best regards,

Bob | International Sales Executive@Encore
sales@encore-tech.com | +86(0)755 2322 4735 | www.encore-tech.com
2/F, Bldg 8th, Zhengzhong Industrial Park, Bao'an Dist, Shenzhen, China 518103"""
    },
    {
        "step_number": 2,
        "step_name": "Step 2: AIDA 拳头单品击穿 (Slogan+卖点+样品行动召唤)",
        "delay_days": 3,
        "is_thread_reply": 1,
        "subject": "Re: {subject_step1}",
        "body_template": """Hi {first_name},

Following up on my previous note regarding {company}'s architectural lighting schemes.

Now, you have {recommended_product}, you have the solution!

{product_bullets}

Act today! Samples are available upon confirmation. Would you like a sample kit sent to your office for your upcoming project mock-up?

Best regards,

Bob
International Sales Executive@Encore

T: +86(0)755 2322 4735    M: +86.135.0005.2091 (WhatsApp/WeChat)
E: sales@encore-tech.com    W: www.encore-tech.com
A: 2/F, Bldg 8th, Zhengzhong Industrial Park, Qiaotou Community, Fuyong, Bao'an Dist, Shenzhen, China 518103"""
    },
    {
        "step_number": 3,
        "step_name": "Step 3: 案例与供应链背书 (Nike连锁店/高端展厅实景)",
        "delay_days": 4,
        "is_thread_reply": 1,
        "subject": "Re: {subject_step1}",
        "body_template": """Hi {first_name},

One detail that might give you confidence:

One of our overseas partners won and supplied the lighting for NIKE retail stores across more than 10 states with over 6,000 units of our zoomable architectural fixtures, strictly complying with visual comfort and strict maintenance standards.

In addition, our modular components allow 7-day fast dispatch for project prototypes.

Happy to share our full project case study video and IES files if you are reviewing fittings for current jobs.

Best regards,

Bob | Encore Commercial Lighting"""
    },
    {
        "step_number": 4,
        "step_name": "Step 4: 礼貌收尾 Break-up (转介绍与关闭沟通)",
        "delay_days": 7,
        "is_thread_reply": 1,
        "subject": "Re: {subject_step1}",
        "body_template": """Hi {first_name},

I haven't heard back, so I assume you either have fully satisfied suppliers in place or your hands are full with project delivery. I'll stop following up to keep your inbox clean.

If you are not the right person for lighting specifications at {company}, could you kindly refer me to who manages your fixture sourcing?

Whenever you need reliable architectural samples in the future, my email is always open.

Wishing you and the {company} team continued success!

Best regards,

Bob | Encore Commercial Lighting"""
    }
]

# 精选买家库：阿联酋(9) + 沙特(8) + LiGHT26 精选买家
ENCORE_LEADS = [
    # --- 阿联酋 ---
    {
        "email": "Moissar@pxls.ae",
        "first_name": "Moissar",
        "company": "PXLS Lighting Systems",
        "title": "Procurement / Project Lead",
        "country": "United Arab Emirates",
        "city": "Abu Dhabi",
        "category": "中东-阿联酋",
        "project_reference": "TOTO 卫浴高端展厅 (Abu Dhabi) & Supreme Council 总部",
        "recommended_product": "DELLA",
        "subject_step1": "Saw your TOTO Showroom in Abu Dhabi — architectural glare control",
        "pain_point_opener": "Saw your TOTO showroom project in Abu Dhabi — sleek ceramic displays, but did specular surface glare ever compromise the clean ceiling aesthetics?",
        "product_bullets": """DELLA mini architectural downlight system offers:
• Deep Glare Control: High optical cut-off angle delivering UGR < 16 to keep commercial ceilings exceptionally comfortable.
• Museum-Grade Color: CRI 95+ (R9 > 80) preserving authentic ceramic and architectural textures without distortion.
• Modular Flexibility: Trimless & flanged interchangeable bezels fitting 50mm miniature apertures for a clean architectural finish.
• Anti-Glare Aiming: Precision honeycomb louvers and dual beam options tailored for premium retail & showroom mockups."""
    },
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
        "subject_step1": "Quick question on your BurJuman Mall store fit-out — 48V magnetic track",
        "pain_point_opener": "Saw your recent retail fit-out at BurJuman Mall — on commercial store fit-outs, do clients frequently request track systems that can be re-aimed between seasons without rewiring?",
        "product_bullets": """Our 48V Magnetic Track System provides:
• Tool-Free Snap-in: Spots, linear diffusers, and wall washers click in instantly anywhere along the track.
• Ultra-Slim Architectural Profile: 5.5mm visible edge seamlessly recessing into drywall or surface mounting.
• Precision Commercial Optics: CRI 90+, DALI-2 & 0-10V dimming ready for flexible retail zoning.
• 7-Day Fast Dispatch: Core components pre-assembled for urgent commercial handover deadlines."""
    },
    {
        "email": "info@skyelume.com",
        "first_name": "Lighting Design Team",
        "company": "Skyelume",
        "title": "Lighting Consultant",
        "country": "United Arab Emirates",
        "city": "Dubai",
        "category": "中东-阿联酋",
        "project_reference": "Trèsind 餐厅 & Al Quoz Nestt",
        "recommended_product": "48V 磁吸轨道 + WASH 洗墙模组",
        "subject_step1": "Lighting scheme for Trèsind Dubai — seamless wall washing",
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
        "subject_step1": "Smart lighting for Business Bay schemes — motorized track aiming",
        "pain_point_opener": "Saw your recent commercial project at Business Bay — as a KNX & DALI member, when lighting high ceilings in retail or boardrooms, is manual ladder re-aiming becoming a client headache?",
        "product_bullets": """MOVIA Motorized Architectural Track Spotlight features:
• Remote Pan & Tilt: Precise 360° pan and 90° tilt controlled via Casambi App or DALI console from ground level.
• Optical Zoom: Seamless 15° to 55° motorized beam focus without changing physical lenses.
• Scene Recall: Store and activate lighting positions for retail seasonal displays with one tap.
• Architectural Finish: Compact housing hiding all internal motors for sleek gallery aesthetics."""
    },
    {
        "email": "info@alamalidaa.com",
        "first_name": "Sourcing Team",
        "company": "Alam Alidaa Lighting LLC",
        "title": "Wholesaler & Contractor",
        "country": "United Arab Emirates",
        "city": "Sharjah",
        "category": "中东-阿联酋",
        "project_reference": "沙迦 Al Majaz 沿海高端住宅 & 商业外立面",
        "recommended_product": "DELLA",
        "subject_step1": "Fixtures for Al Majaz residential schemes — miniature deep anti-glare",
        "pain_point_opener": "Saw your lighting projects across Al Majaz in Sharjah — on upscale residential ceilings, do your private clients often complain about noticeable downlight glare and mismatched trims?",
        "product_bullets": """DELLA Mini Downlight System provides:
• UGR < 16 Glare Control: Deep recessed optical chamber ensuring light is seen on surfaces, not in the eyes.
• Universal Modular Frame: 18+ trim designs (round, square, trimless, flanged) sharing one miniature light engine.
• IP54 Moisture Protection: Ideal for coastal climate humidity and bathroom vanity lighting.
• Direct Factory Sourcing: Competitive tier-1 pricing with dependable project MOQ."""
    },
    # --- 沙特阿拉伯 ---
    {
        "email": "info@lumiere.com.sa",
        "first_name": "Sourcing Director",
        "company": "Lumiere Lighting",
        "title": "Architectural Lighting Supplier",
        "country": "Saudi Arabia",
        "city": "Riyadh",
        "category": "中东-沙特",
        "project_reference": "利雅得 KAFD 金融区企业总部 & 奢华展厅",
        "recommended_product": "DELLA",
        "subject_step1": "KAFD project specs — architectural miniature downlights (CRI 95+)",
        "pain_point_opener": "Saw your commercial deliveries across Riyadh's KAFD development — with the high architectural standards required in Saudi Vision 2030 projects, is finding high-CRI compact fittings with low UGR a constant sourcing hurdle?",
        "product_bullets": """DELLA Architectural Downlight System provides:
• Vision 2030 Standards Ready: CE, CB, SASO-ready components with genuine CRI 95+ (R9 > 80).
• Miniature 50mm Aperture: Discreet ceiling footprint with high output up to 800lm.
• Die-Cast Thermal Housing: Engineered for GCC high ambient temperatures ensuring 50,000h lifespan.
• Project Sample Kits: Customized wooden presentation cases ready for consultant board approvals."""
    },
    {
        "email": "projects@al-abdulkarim.com",
        "first_name": "Procurement Team",
        "company": "Al Abdulkarim Lighting",
        "title": "Commercial Distributor & Contractor",
        "country": "Saudi Arabia",
        "city": "Dammam / Khobar",
        "category": "中东-沙特",
        "project_reference": "Dammam 商业中心 & 工业总部大楼",
        "recommended_product": "GALAXY 高天棚商照筒灯",
        "subject_step1": "High-ceiling commercial fit-outs in Eastern Province — 50W anti-glare downlights",
        "pain_point_opener": "Saw your extensive commercial supply across the Eastern Province — when dealing with 6 to 9 meter high commercial atriums, do you find clients caught between ugly industrial high bays and weak commercial downlights?",
        "product_bullets": """GALAXY Architectural High-Ceiling Downlight offers:
• High Output: 10W to 50W delivering up to 5,500 lumens from a refined architectural fixture.
• Cut-Off Comfort: 30° optical cut-off angle keeping high atriums completely free of harsh eye-level glare.
• Multi-Mounting Options: Surface mounted, recessed, or pendant suspended via modular sleeves.
• Bridgelux V13 LED Engine: Long-term lumen maintenance tested under 45°C ambient conditions."""
    },
    {
        "email": "sales@sarhlighting.sa",
        "first_name": "Project Sales Team",
        "company": "Sarh Al-Mamlaka Lighting",
        "title": "Lighting Project Partner",
        "country": "Saudi Arabia",
        "city": "Jeddah",
        "category": "中东-沙特",
        "project_reference": "吉达滨海度假酒店 & 奢华零售精品店",
        "recommended_product": "48V 磁吸轨道 / Magnetic",
        "subject_step1": "Jeddah hospitality schemes — 48V magnetic track & wall wash",
        "pain_point_opener": "Saw your recent hospitality fit-outs in Jeddah — for boutique hotels, do designers frequently demand track fixtures that blend into wooden paneling without visible screws or clunky drivers?",
        "product_bullets": """Our 48V Low-Voltage Magnetic System features:
• Ultra-Compact Track Profile: Fits flush into millwork or drywall slots without structural ceiling drops.
• High Visual Comfort: Black baffle spots with honeycomb louvers tailored for luxury hotel lobbies.
• Tunable White Integration: 2700K to 5000K mood lighting controllable via DALI or wireless app.
• Rapid Lead Time: Factory-direct production in Shenzhen ensuring project handovers meet schedule."""
    },
    # --- 英国 LiGHT26 展会精选买家 ---
    {
        "email": "info@orangelighting.co.uk",
        "first_name": "Andrew",
        "company": "Orange Lighting",
        "title": "Director & Principal Consultant",
        "country": "United Kingdom",
        "city": "London",
        "category": "英国-LiGHT26",
        "project_reference": "LiGHT 26 Review Post & Residential/Hotel Procurement",
        "recommended_product": "DELLA",
        "subject_step1": "Your LiGHT '26 takeaway — meeting new fixture manufacturers",
        "pain_point_opener": "Saw your LiGHT '26 wrap-up post mentioning you were meeting new fixture manufacturers for your project procurement services. For your upscale schemes, what has been the hardest specification gap to fill when dealing with existing brands?",
        "product_bullets": """ENCORE Architectural Fixtures (Shenzhen Factory Direct) offers:
• OEM / Specification-Grade Downlights: DELLA mini architectural series with UGR < 16 and CRI 95+.
• Modular Interchangeability: 18+ trim configurations with tool-free front-loading modules.
• European Compliance: Full CE, RoHS, and UKCA compliance with first-tier European drivers (Tridonic/Osram).
• Fast Custom Prototyping: Dedicated engineering team supporting custom optics and finishes for British schemes."""
    },
    {
        "email": "contact@amdgb.com",
        "first_name": "AMD Team",
        "company": "AMD Interior Architecture",
        "title": "Interior Architecture Studio",
        "country": "United Kingdom",
        "city": "London",
        "category": "英国-LiGHT26",
        "project_reference": "LiGHT '26 'Lights we loved' Reel & Retail Fit-outs",
        "recommended_product": "48V 磁吸轨道 / Magnetic",
        "subject_step1": "Your LIGHT '26 picks — 48V magnetic track for retail fit-outs",
        "pain_point_opener": "Saw your 'Lights we loved at LIGHT '26' reel — on your retail fit-outs, are clients asking more for track systems that can be re-set between seasons without rewiring or specialist tools?",
        "product_bullets": """Our 48V Magnetic Track System provides:
• Snap-In Flexibility: Spot, linear and wall-wash modules click in instantly without breaking ceiling lines.
• Clean Aesthetics: Super slim 48V track made to custom lengths for British retail schemes.
• Optical Excellence: CRI 90+, 2700K–6500K Tunable White, DALI-2 compliant.
• CE / UKCA Certified: Shipped factory-direct from Shenzhen with dedicated trade project support."""
    },
    {
        "email": "sales@lightingservices.com",
        "first_name": "Project Engineering Team",
        "company": "Connected Light",
        "title": "Lighting Consultant & Contractor",
        "country": "United Kingdom",
        "city": "Bristol",
        "category": "英国-LiGHT26",
        "project_reference": "LiGHT 26 Day 1 Review & Fit-out Supply",
        "recommended_product": "DELLA",
        "subject_step1": "Your visit to LiGHT '26 — reliable architectural downlight supply",
        "pain_point_opener": "Saw your post from LiGHT '26 noting new products for upcoming schemes — as you handle both design and turn-key supply, does long manufacturer lead time or high brand markup ever jeopardize your project margins?",
        "product_bullets": """ENCORE Direct Manufacturing Partnership offers:
• High Margin Protection: Direct factory engineering prices without distributor markups.
• DELLA Architectural Series: UGR < 16, 50mm miniature hole, deep anti-glare for hospitality & office fit-outs.
• Fast Prototyping: 7-day turnaround for mock-up samples with your required color temperatures.
• Certified Engineering: UKCA/CE certified, DALI/Casambi smart controls integration."""
    }
]
