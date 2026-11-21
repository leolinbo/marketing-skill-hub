import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

sys.stdout.reconfigure(encoding='utf-8')

# Output directories
base_out = r'D:\marketing\开发信Word库_完整版'
dir_na = os.path.join(base_out, '01_北美市场(North_America)')
dir_eu = os.path.join(base_out, '02_欧澳成熟市场(Europe_Australia)')
dir_em = os.path.join(base_out, '03_新兴增量市场(东南亚与中东)')
dir_spec = os.path.join(base_out, '04_特种高溢价方案(汽车展厅与高天花)')
dir_all = os.path.join(base_out, '00_总览合集')

for d in [dir_na, dir_eu, dir_em, dir_spec, dir_all]:
    os.makedirs(d, exist_ok=True)

assets_base = r'D:\marketing\assets\products'

def get_images(series_name, max_count=3):
    s_dir = os.path.join(assets_base, series_name)
    if not os.path.exists(s_dir):
        return []
    valid = [os.path.join(s_dir, f) for f in os.listdir(s_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    return valid[:max_count]

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def create_styled_document():
    doc = docx.Document()
    # set page margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
    return doc

def add_header(doc, title, subtitle, market_tag):
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_tag = p_meta.add_run(f"【Encore Commercial Lighting · {market_tag}】")
    r_tag.font.size = Pt(9.5)
    r_tag.font.color.rgb = RGBColor(100, 116, 139)

    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_after = Pt(2)
    p_title.paragraph_format.space_before = Pt(4)
    run_title = p_title.add_run(title)
    run_title.font.size = Pt(20)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(26, 54, 93) # Deep Blue

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(12)
    run_sub = p_sub.add_run(subtitle)
    run_sub.font.size = Pt(11)
    run_sub.font.color.rgb = RGBColor(71, 85, 105)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_section_title(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = RGBColor(37, 99, 235)

def add_callout(doc, title, text, bg_hex="F1F5F9"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, bg_hex)
    cell.width = Inches(6.8)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(4)
    r_t = p.add_run(f"★ {title}\n")
    r_t.font.bold = True
    r_t.font.size = Pt(10.5)
    r_t.font.color.rgb = RGBColor(15, 23, 42)
    r_c = p.add_run(text)
    r_c.font.size = Pt(10)
    r_c.font.color.rgb = RGBColor(51, 65, 85)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_email_box(doc, touch_num, touch_title, subject_lines, body_text):
    add_section_title(doc, f"第 {touch_num} 轮：{touch_title}")
    
    table = doc.add_table(rows=2, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Row 0: Subject lines
    cell_subj = table.cell(0, 0)
    set_cell_background(cell_subj, "E0F2FE") # Light Cyan
    cell_subj.width = Inches(6.8)
    p_s = cell_subj.paragraphs[0]
    p_s.paragraph_format.space_before = Pt(4)
    p_s.paragraph_format.space_after = Pt(4)
    r_sl = p_s.add_run("建议邮件主题（Subject Line 备选）：\n")
    r_sl.font.bold = True
    r_sl.font.size = Pt(10)
    r_sl.font.color.rgb = RGBColor(3, 105, 161)
    for i, s in enumerate(subject_lines, 1):
        r_line = p_s.add_run(f"选项 {i}: {s}\n")
        r_line.font.size = Pt(9.5)
        r_line.font.color.rgb = RGBColor(12, 74, 110)

    # Row 1: Email Body
    cell_body = table.cell(1, 0)
    set_cell_background(cell_body, "F8FAFC")
    cell_body.width = Inches(6.8)
    p_b = cell_body.paragraphs[0]
    p_b.paragraph_format.space_before = Pt(6)
    p_b.paragraph_format.space_after = Pt(6)
    r_b = p_b.add_run(body_text.strip())
    r_b.font.size = Pt(10)
    r_b.font.color.rgb = RGBColor(30, 41, 59)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def insert_product_images(doc, series_name, image_caption="核心产品与实景细节实拍"):
    imgs = get_images(series_name, max_count=2)
    if not imgs:
        return
    add_section_title(doc, f"产品实物与实景展示（{image_caption}）")
    for img_path in imgs:
        try:
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(4)
            p_img.paragraph_format.space_after = Pt(2)
            run_img = p_img.add_run()
            run_img.add_picture(img_path, width=Inches(5.0))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(8)
            r_cap = p_cap.add_run(f"▲ 图示：Encore {series_name} 系列真实工程交付与实物配件图")
            r_cap.font.size = Pt(8.5)
            r_cap.font.color.rgb = RGBColor(148, 163, 184)
        except Exception as e:
            print(f"Error inserting image {img_path}: {e}")

print("Docx generator framework loaded successfully.")

PRODUCTS_DATA = {
    "DELLA": {
        "title": "DELLA 2.0 Architectural Downlight System",
        "cn_name": "DELLA 2.0 旗舰建筑深防眩筒灯系统",
        "specs": "ETL/CE/RoHS 认证 | 模块化设计 | UGR<12 / Pinhole UGR<6 | 固定/摆动/洗墙/IP65防水 | 0-10V/DALI/Triac 调光",
        "persona_na": "美加高端精品零售、五星级酒店、豪宅室内设计工作室及店装工程承包商 (Retail Interior Designers & Fit-out Contractors)",
        "pain_na": "本地照明品牌层层加价（加价3-5倍），样品交期长达6-8周；市场上深防眩防反光等级不足，导致天花杂乱、刺眼。",
        "sol_na": "北美标准 ETL 认证，独家深藏防眩设计，一套模组换环实现80%项目需求；工厂直供2周内送达案头样品，支持$50试样盒。",
        "subjs_na": [
            "ETL architectural downlight sample for [Company Name] (DELLA 2.0)?",
            "zero-glare recessed downlights delivered in 2 weeks (ETL listed)",
            "quick question regarding [Company Name]'s boutique retail lighting"
        ],
        "touch1_na": """Hi [First Name],

Came across [Company Name]’s recent commercial and retail interiors in [City]—really love the clean architectural lines and refined ceiling details.

When specifying recessed downlights for boutique spaces or hospitality, designers often battle two things: harsh direct ceiling glare, or long 6-to-8-week sample lead times from local distributors.

We engineered the DELLA 2.0 Architectural Downlight Family (ETL Listed for North America) to solve this:
• Ultimate Visual Comfort: Deep-regression optics delivering UGR < 12 (with micro-pinhole down to UGR < 6).
• One Engine, Whole Project: One modular LED core adapts to fixed, 30° adjustable, wall-washing, and true IP65 wet locations.
• Fast Factory Turnaround: Custom project samples delivered directly to your desk in under 2 weeks.

We’ve supplied lighting for private art galleries in Ireland, museum spaces, and custom studios in Canada.

Would it be helpful to ship a $50 DELLA 2.0 hands-on sample kit to your office to inspect the optical quality and finish?

Best regards,

[Your Name]
Encore Commercial Lighting
encore-tech.com""",
        "touch2_na": """Hi [First Name],

Following up on my note regarding architectural downlights.

Thought you might appreciate this detail: with DELLA 2.0, your contractors don't have to carry 10 different fixtures on-site. The tool-free magnetic bezel and twist-lock LED core allow them to swap from a 15° pinhole spot to a wide flood or IP65 trim in 10 seconds.

If you have any retail, restaurant, or hotel projects currently on the boards, happy to review your lighting schedule and quote within 24 hours.

Worth a quick look at the cut-sheet?

Best,
[Your Name]""",
        "touch3_na": """Hi [First Name],

I understand your schedule is packed with project deadlines.

If your current lighting vendors are already providing you with museum-grade color rendering (CRI 95+), UGR < 10 visual comfort, and 2-week sample turnarounds, feel free to keep us in mind as a backup.

Whenever you need a reliable factory partner for your next competitive commercial bid, our full architectural catalog is at encore-tech.com.

Would you prefer I check back with your team next quarter?

Best regards,
[Your Name]"""
    },
    "MAGNETIC": {
        "title": "48V Low-Voltage Magnetic Track System",
        "cn_name": "48V 安全低压磁吸轨道照明系统",
        "specs": "48V DC 安全电压 | 嵌入式/明装/吊装 | 磁吸即插即拔 | 射灯/线性泛光/格栅防眩/吊线灯一站式配齐 | 0-10V/DALI/Casambi 调光",
        "persona_na": "商业店铺装修工程商 (Shopfitters)、现代独立咖啡馆与女装店设计师、高端商业空间集成商",
        "pain_na": "高压轨道笨重且施工繁琐；后期业主需要更换陈列时，调整灯具需要断电爬高，灵活性极差。",
        "sol_na": "超窄磁吸极简美学，徒手秒级拆装调换；满足北美电气安全规范，全系列现货模组，2周出样交付。",
        "subjs_na": [
            "flexible 48V magnetic track system for [Company Name]'s fit-outs",
            "quick question on your upcoming retail boutique lighting",
            "magnetic track package delivered in 2 weeks (factory direct)"
        ],
        "touch1_na": """Hi [First Name],

Hope your current fit-out projects in [City] are wrapping up smoothly.

For fast-paced commercial spaces like fashion boutiques, cafes, and open offices, traditional track systems often look bulky and lack the flexibility modern retail owners demand.

Our 48V Low-Voltage Magnetic Track System is designed specifically for high-end boutique environments:
• Tool-Free Flexibility: Snap in spotlights, linear wash lights, micro-grids, and pendant cylinders in seconds without turning off the system.
• Ultra-Slim Ceiling Lines: Minimalist recessed and surface track profiles that disappear into the architecture.
• Reliable North American Compliance: Built for 120-277V systems with smooth 0-10V, DALI-2, or Casambi Bluetooth dimming.
• Fast 14-Day Lead Times: Complete fixture schedules shipped directly from our manufacturing floor in under 2 weeks.

If you have a reflected ceiling plan (RCP) or lighting schedule on your desk, send it over—we’ll generate a full fixture take-off and factory-direct quote within 24 hours.

Open to seeing our 2-page project lookbook?

Best regards,

[Your Name]
Encore Commercial Lighting
encore-tech.com""",
        "touch2_na": """Hi [First Name],

Following up on my message from earlier this week.

One feature our contractor partners love about our 48V system is the mechanical safety lock alongside the magnetic connection—fixtures click securely into place with zero risk of loosening, even in high-vibration commercial spaces.

We recently supplied track and downlight packages for automotive studio spaces in Canada and boutique stores overseas.

Would you be open to receiving a $50 compact track demo kit to test the magnetic snap and dimming quality on-site?

Best,
[Your Name]""",
        "touch3_na": """Hi [First Name],

Closing the loop on this.

If you don't have any commercial projects requiring flexible track lighting right now, no problem at all.

Feel free to bookmark our direct catalog at encore-tech.com for when your next boutique or hospitality fit-out comes up.

Would you like me to stay in touch for your Q2/Q3 bids?

Best regards,
[Your Name]"""
    },
    "VEGA": {
        "title": "VEGA Minimalist Flush In-Track Spotlight",
        "cn_name": "VEGA 隐形驱动极简商业轨道射灯",
        "specs": "一体化隐形嵌入式驱动 (Concealed In-Track Driver) | 告别传统外露驱动盒 | CRI 95+ / R9>80 | 博物馆级光斑 | 15°/24°/38°/60° 及洗墙镜头",
        "persona_na": "高端画廊策展人、艺术馆照明顾问、奢侈品专柜及极简主义零售设计师",
        "pain_na": "普通轨道灯后面拖着一个巨大笨重的电源盒子（Bulky Adapter），在精致天花板上极度扎眼，破坏空间美学。",
        "sol_na": "整机驱动全隐蔽在导轨内部，只露出纯粹圆柱形灯头；传承国家博物馆与爱尔兰艺术馆严苛光学基因，还原真实色彩与零杂散光。",
        "subjs_na": [
            "say goodbye to bulky track adapters: the flush VEGA series",
            "flush-mount track lighting for [Company Name]'s gallery & retail spaces",
            "museum-grade optical spotlights (clean in-track driver)"
        ],
        "touch1_na": """Hi [First Name],

In luxury retail, art galleries, and modern hospitality spaces, nothing compromises a clean architectural ceiling quite like a bulky external driver box hanging below the track.

We engineered the VEGA Track Light Series specifically to eliminate that visual noise:
• Concealed In-Track Driver: The entire electronic driver sits completely flush inside the track. Only the clean, architectural cylindrical fixture is visible.
• True Museum Optics: CRI 95+, R9 > 80, delivering crisp, saturated colors on art pieces, fabrics, and fine finishes with zero glare.
• Proven Track Record: We’ve illuminated world-class cultural spaces including national museums and European private art galleries.

If [Company Name] is designing spaces where every visual detail matters, we’d be delighted to ship a working VEGA sample to your studio.

Worth a brief look at the spec sheet?

Best regards,

[Your Name]
Encore Commercial Lighting
encore-tech.com""",
        "touch2_na": """Hi [First Name],

Following up on the VEGA flush track spotlight.

Many designers also appreciate that VEGA offers interchangeable optical lenses and honeycomb louvers on-site—allowing you to fine-tune beam angles from razor-sharp 15° accents to soft 45° ambient washes in under a minute.

Are you working on any high-end boutique, gallery, or showroom concepts this quarter?

Best,
[Your Name]""",
        "touch3_na": """Hi [First Name],

I know your time is valuable.

If your current track fixtures already provide seamless in-track drivers and museum-grade color rendition at factory direct pricing, keep up the great work!

Should you ever need an agile factory partner capable of custom finishes and 2-week sampling, our door is always open: encore-tech.com.

Best regards,
[Your Name]"""
    },
    "AVA": {
        "title": "AVA Modular MR16 / GU10 Downlight System",
        "cn_name": "AVA 模块化 MR16 / GU10 翻新与降本筒灯系统",
        "specs": "通用 MR16 / GU10 替代标准 | 一芯多环模组化 | 解决老旧卤素灯高能耗易损坏痛点 | 商业酒店改造翻新神级利器",
        "persona_na": "商业空间翻新工程商、连锁酒店/餐厅运维采购经理、机电总包商 (Renovation Contractors / MEP)",
        "pain_na": "大量翻新项目原天花开孔五花八门，传统更换需要重新补天花或大量囤积不同品牌规格筒灯，人工与库存成本高昂。",
        "sol_na": "一颗核心 LED 引擎适配市场 90% 面环，无需重新布线补顶；大幅压低库存与人工成本，极速换装。",
        "subjs_na": [
            "retrofit project? Cut stock & labor costs with AVA MR16/GU10 system",
            "cut installation time on your commercial downlight replacements",
            "universal modular LED engine for hospitality & retail retrofits"
        ],
        "touch1_na": """Hi [First Name],

If your team frequently handles commercial, hotel, or retail renovation and retrofit projects, you know the headache of dealing with legacy MR16 / GU10 fixtures and mismatched ceiling cutouts.

We developed the AVA Modular Downlight System to drastically reduce labor time and inventory risk on upgrade projects:
• Universal Replacement: One high-efficiency LED module that directly upgrades old halogen fixtures while preserving existing ceiling openings.
• Lower Inventory SKUs: A single modular LED core pairs with over 20+ interchangeable trims (round, square, trimless, IP65, deep baffle).
• Rapid Payback: Up to 85% energy reduction, superior thermal management, and reliable 50,000-hour rated lifespan.

We can courier an AVA hands-on contractor sample kit directly to your warehouse or project site for $50.

Would this be helpful for your upcoming renovation bids?

Best regards,

[Your Name]
Encore-Tech Commercial Solutions""",
        "touch2_na": """Hi [First Name],

Checking back on the AVA retrofit system.

Contractors love that AVA requires zero special tools on-site—front-loading modular drivers and magnetic trims let electricians finish room retrofits in half the usual labor time.

Do you have any commercial or hospitality retrofit projects coming up this season?

Best,
[Your Name]""",
        "touch3_na": """Hi [First Name],

No worries if you're not currently running any retrofit jobs.

Feel free to keep our AVA cut-sheet on file whenever a client asks to upgrade their existing space to high-performance LED without tearing down the drywall.

Best regards,
[Your Name]"""
    },
    "NOVA": {
        "title": "NOVA Slim Architectural Pendant Cylinder",
        "cn_name": "NOVA 极简超细圆柱吊灯与明装筒灯",
        "specs": "极细精致管径 | UGR<6 极致深度防眩 | 无外露粗糙螺丝与线锁 | 精密控光不刺眼 | 专为咖啡吧台、接待台、西餐餐桌打造",
        "persona_na": "精品咖啡馆主理人、独立烘焙轻食店设计师、高端买手店收银吧台空间设计师",
        "pain_na": "普通吊线圆柱灯顶部天花接线盒笨重粗糙，吊绳螺丝外露；坐在吧台或餐桌仰头时，灯光极其刺眼眩目。",
        "sol_na": "隐蔽式极简吸顶过渡设计，独家 UGR<6 深孔蜂窝控光，光聚在桌面而不刺眼，出片率极高。",
        "subjs_na": [
            "the $5 detail ruining slim cylinders (and our UGR<6 fix)",
            "architectural pendant cylinders for [Company Name]'s cafe & bar spaces",
            "minimalist pendant lighting with zero glare for hospitality"
        ],
        "touch1_na": """Hi [First Name],

When designing specialty cafes, boutique bars, or hotel reception counters, slim pendant cylinders are often the visual centerpiece above the counter.

However, two common flaws frequently compromise the finish: bulky surface canopy hardware with exposed screws, and harsh glare that blinds customers sitting beneath.

We engineered the NOVA Slim Cylinder Family to perfect these architectural details:
• UGR < 6 Deep Shielding: Ultra-deep optical regression keeps the light source invisible from normal viewing angles—delivering warm, focused illumination onto the counter with zero glare.
• Clean Ceiling Transition: Ultra-minimal canopy kit that sits perfectly flush without ugly exposed wire-locks or visible fasteners.
• Refined Color Finishes: Anodized matte black, architectural white, brushed bronze, and custom champagne gold.

We’d love to send a NOVA display sample to your studio so you can feel the heavy machined aluminum finish in person.

Where should we courier our latest Hospitality Lookbook?

Best regards,

[Your Name]
Encore Commercial Lighting""",
        "touch2_na": """Hi [First Name],

Quick follow-up on the NOVA cylinders.

In addition to pendant mounting, NOVA also comes in surface ceiling mounts and track-mounted versions—allowing you to maintain a consistent cylindrical design language across the entire venue.

Working on any cafe, restaurant, or retail bar spaces right now?

Best,
[Your Name]""",
        "touch3_na": """Hi [First Name],

Just closing the loop on this.

If you don't need decorative or counter accent lighting at the moment, feel free to check out encore-tech.com when your next project begins.

Wishing you continued success on your upcoming designs!

Best,
[Your Name]"""
    },
    "MOVIA": {
        "title": "MOVIA Motorized Track Spotlight with Casambi Control",
        "cn_name": "MOVIA 电动智能变焦遥控轨道射灯",
        "specs": "内置精密微电机 | 水平350° + 垂直90° 电动调节 | 手机 App (Casambi) / 遥控器一键控制 | 场景记忆一键切换 | 挑高展厅免爬梯神作",
        "persona_na": "高端汽车展厅 (Auto Showrooms)、大型博物馆、挑高艺术展厅、高端快闪店运营方",
        "pain_na": "天花板高达 5~8 米，每次展位更换或展车移动，都需要雇工人搭脚手架或爬高梯调角，极度危险且成本极高。",
        "sol_na": "手机点一点，灯头自动旋转对准展品，支持光束角无级缩放；彻底告别人工高空作业，加拿大改装车行与博物馆真实落地案例背书。",
        "subjs_na": [
            "stop climbing ladders: motorized Casambi track spotlight (MOVIA)",
            "remote motorized track lighting for high-ceiling retail & showrooms",
            "re-aim spotlights from your phone in 5 seconds (MOVIA series)"
        ],
        "touch1_na": """Hi [First Name],

In high-ceiling commercial spaces like auto showrooms, art galleries, and multi-brand luxury boutiques, re-aiming spotlights every time the floor layout changes is a massive hassle—requiring ladders, scaffolds, and after-hours labor costs.

We developed the MOVIA Motorized Track Spotlight to eliminate high-altitude manual adjustments completely:
• Smartphone App Control: Smooth motorized pan (350°) and tilt (90°) adjustments directly via Casambi Bluetooth or handheld remote.
• Motorized Optical Zoom: Adjust beam spread from narrow 10° punch to wide 50° flood without touching the ceiling.
• Preset Scene Memory: Save lighting presets for rotating car displays, seasonal runway setups, or new exhibitions and recall them with one click.

We previously equipped luxury automotive studios in Canada and museum galleries with high-precision automated lighting.

Would you be open to a 60-second video demo showing MOVIA in action on-site?

Best regards,

[Your Name]
Encore Commercial Lighting""",
        "touch2_na": """Hi [First Name],

Following up on the MOVIA motorized spotlight.

One client who manages a 6-meter ceiling automotive showroom told us they cut their exhibition turnover labor costs by over 70% in the first quarter alone by using MOVIA.

If you manage or design any spaces with 15+ foot ceilings, this is an instant winner for owners.

Would you like to review the technical cut-sheet and pricing?

Best,
[Your Name]""",
        "touch3_na": """Hi [First Name],

Understood if your current projects don't have high-ceiling motorized requirements right now.

I’ll keep our MOVIA case study on file. Feel free to reach out whenever a client asks for smart, remote-commissioned commercial lighting: encore-tech.com.

Best regards,
[Your Name]"""
    },
    "Digital Display Track Light": {
        "title": "Digital Display Zoomable Track Light",
        "cn_name": "数显智能变焦高精度商业轨道灯",
        "specs": "灯体高清数显屏 (OLED/LCD Display) | 精准直观显示当前光束角/色温/亮度 | 15°-60° 旋转变焦 | CRI 97+ 顶级色彩还原",
        "persona_na": "珠宝钟表奢侈品专柜、专业美术馆、高端画廊、高端私人定制会所照明设计师",
        "pain_na": "传统轨道灯光束角全凭肉眼手感调，一排灯打过去光斑大小不一；珠宝与艺术品对微小色差与光斑边界要求极其苛刻。",
        "sol_na": "数显屏幕精确到度数与流明，所见即所得；完美保持一整排灯具的一致性，顶级国家级文博控光技术降维商用。",
        "subjs_na": [
            "digital screen track light: precision zooming for luxury & galleries",
            "eliminate guesswork in lighting adjustments: digital display spotlight",
            "high-CRI 97 track spotlight with built-in digital readout"
        ],
        "touch1_na": """Hi [First Name],

When lighting high-end galleries, luxury watch/jewelry displays, or premium fashion boutiques, aiming and zooming multiple spotlights by eye almost always leaves inconsistencies across the showroom.

Our Digital Display Zoomable Track Light brings aerospace precision to commercial lighting:
• On-Body Digital Readout: Clear, discreet digital display showing exact beam angle (from 15° to 60°) and dimming percentages.
• Absolute Uniformity: Replicate the exact same beam diameter and lux level across 50 fixtures along a gallery wall with zero guesswork.
• Museum-Grade Spectrum: Powered by ultra-high CRI 97+ (R9 > 90) LED chips, certified for fine art and delicate luxury merchandise.

We’ve supplied cultural institutions including the National Museum of China and private galleries across Europe.

Would you be open to reviewing the product sheet and seeing a hands-on sample?

Best regards,

[Your Name]
Encore Commercial Lighting""",
        "touch2_na": """Hi [First Name],

Following up on the digital display zoomable track spotlight.

Contractors and curators love that they can record exact beam values in their project documentation, making ongoing maintenance and fixture replacements completely foolproof.

Do you have any gallery, jewelry, or luxury retail projects currently in development?

Best,
[Your Name]""",
        "touch3_na": """Hi [First Name],

Wrapping up my note on the Digital Display spotlight.

If you don't have precision exhibition projects right now, no problem at all. We’re always here at encore-tech.com whenever your clients demand next-level optical control.

Best regards,
[Your Name]"""
    },
    "OVEGA": {
        "title": "OVEGA All-in-One Multifunctional Track Light System",
        "cn_name": "OVEGA 百变多功能商业轨道灯系统",
        "specs": "聚光/泛光/洗墙/变焦四位一体 | 磁吸式快拆光学透镜 | 统一家族化外观 | 解决零售店铺多元照明需求",
        "persona_na": "连锁零售品牌工程总监、多业态商业综合体装潢商、商业展示空间设计师",
        "pain_na": "一个店铺既要洗墙打挂件，又要聚光打模特，还要泛光照通道，采购3-4种不同款式的灯导致天花板杂乱无章。",
        "sol_na": "全店只用一款 OVEGA 轨道灯外壳，通过快拆光学配件自由切换重点射灯、均匀洗墙和柔光漫射，大幅压低综合造价。",
        "subjs_na": [
            "still stocking 4 different track lights for one project? OVEGA fix",
            "one track light family for accent, wall-wash & zoom: OVEGA",
            "cut procurement complexity on your retail fit-outs (Encore OVEGA)"
        ],
        "touch1_na": """Hi [First Name],

How many different luminaire families do your teams typically source to finish a single retail fit-out? Usually, you need one spotlight for mannequins, a separate wall-washer for perimeter shelving, and a diffuse light for corridors.

The OVEGA Track Light System consolidates all these functions into one cohesive architectural family:
• Unified Exterior, Multiple Optics: One sleek luminaire body supporting snap-on accent lenses, optical wall-washers, asymmetric optics, and zoom modules.
• Balanced Aesthetics: Keep the ceiling clean and uniform without mismatched fixture shapes and varying paint finishes.
• Direct Supply Advantage: Reduce shipping logistics and vendor friction with one reliable direct factory source.

We can courier an OVEGA multi-optic kit to your office so you can see how easily lenses swap on-site.

Worth sending over the product cut-sheet?

Best regards,

[Your Name]
Encore Commercial Lighting""",
        "touch2_na": """Hi [First Name],

Checking back on the OVEGA all-in-one track system.

Retailers who change merchandise layouts seasonally love OVEGA because in-store visual merchandisers can reconfigure a spotlight into an asymmetric wall-washer in 15 seconds without calling an electrician.

Are you bidding on any commercial retail packages this quarter?

Best,
[Your Name]""",
        "touch3_na": """Hi [First Name],

Closing the loop on OVEGA.

If your current track suppliers have you covered, keep our details handy as an agile alternative when lead times or budget constraints get tight: encore-tech.com.

Best,
[Your Name]"""
    },
    "IMAX": {
        "title": "IMAX High-Power Commercial Track Spotlight",
        "cn_name": "IMAX 大功率高天花商业轨道灯",
        "specs": "40W-60W 超高流明输出 | 专为 5-8 米挑高挑空天花设计 | 航空级锻造铝散热 | 强劲中心光强 CBCP",
        "persona_na": "大中型商业旗舰店、汽车展厅、家具生活馆、双层挑空商场店铺工程商",
        "pain_na": "普通 20W-30W 轨道灯在 6 米高天花上照下来，地面照度完全不足，光线衰减严重，商品显得暗淡无光。",
        "sol_na": "超高中心光强（CBCP），专克挑高天花板；穿透力极强，热量控制优异，保障灯具寿命与光衰稳定。",
        "subjs_na": [
            "high-ceiling lighting problem? 50W punch without the bulk (IMAX)",
            "track spotlights engineered for 18-25ft high ceilings: IMAX",
            "powerful commercial track lighting for large showrooms"
        ],
        "touch1_na": """Hi [First Name],

When designing commercial spaces with 16 to 25-foot ceilings (car showrooms, flagship apparel, two-story retail), standard 25W-30W track lights simply don’t deliver enough punch to the sales floor.

We engineered the IMAX High-Power Track Spotlight for demanding high-ceiling architecture:
• True Punch: High-output 45W-60W packages delivering over 5,000+ lumens with intense center-beam candlepower (CBCP).
• Advanced Heat Dissipation: Cold-forged aluminum chassis engineered for quiet passive cooling and 50,000+ hour continuous commercial operation.
• Clean Optical Control: Anti-glare snoot and honeycomb options ensure bright merchandise without blinding shoppers looking up.

We’ve supplied high-ceiling automotive studios and cultural venues across North America and Europe.

Would you like to review our photometric IES files and high-ceiling fixture schedule?

Best regards,

[Your Name]
Encore Commercial Lighting""",
        "touch2_na": """Hi [First Name],

Following up on high-output track lighting.

If you have any projects with tall ceilings where standard fixtures are failing to hit target lux levels, feel free to send us the floor plan. We’ll run a fast, complimentary DIALux calculation showing exactly how IMAX hits your target foot-candles.

Worth exploring for an active project?

Best,
[Your Name]""",
        "touch3_na": """Hi [First Name],

Just wrapping up. If you don't have large-scale high-ceiling bids currently, feel free to keep our direct line saved for future commercial bids: encore-tech.com.

Best regards,
[Your Name]"""
    },
    "EVO": {
        "title": "EVO Modular Precision Track Spotlight",
        "cn_name": "EVO 模块化高性能商业轨道射灯",
        "specs": "现代极简北欧工业风 | 快拆旋转卡扣滤镜 | 紧凑高光效 | 兼容全球主流 3 线/4 线/低压轨道",
        "persona_na": "独立精品服装店、买手店、连锁咖啡馆设计师与店装承包商",
        "pain_na": "灯具外形千篇一律，笨重廉价；现场需要临时改变光束角或加装防眩网极为繁琐。",
        "sol_na": "极窄边框与高颜值阳极氧化质感，磁吸/快拆配件秒级更换，完美融入精致商业空间。",
        "subjs_na": [
            "architectural track spotlight for modern boutique spaces (EVO)",
            "modular track lighting with instant optical change: EVO series",
            "samples delivered in 2 weeks: Encore EVO commercial spotlights"
        ],
        "touch1_na": """Hi [First Name],

Noticed [Company Name]’s clean interior portfolio in [City]—really love how you balance texture and lighting.

For boutique apparel and specialty hospitality spaces, lighting needs to feel integrated into the design rather than looking like an industrial afterthought.

Our EVO Modular Track Spotlight combines architectural minimalism with practical modularity:
• Compact Proportions: Minimalist cylindrical profile with zero exposed screws or bulky brackets.
• Tool-Free Accessories: Twist-lock front ring allows instant addition of honeycomb louvers, oval diffusers, or colored trims.
• Superior Chromatic Fidelity: CRI 95+, 2700K to 4000K, ensuring clothing colors and wood finishes look true to life.

We ship direct from our manufacturing facility, delivering custom samples to your door in under 14 days.

Could I send a quick 2-page spec card to your team?

Best regards,

[Your Name]
Encore Commercial Lighting""",
        "touch2_na": """Hi [First Name],

Quick follow-up on the EVO track spotlight.

Contractors love that EVO is compatible with standard North American and global track systems, meaning you can upgrade the fixtures without replacing existing installed track rails.

Working on any boutique or cafe fit-outs currently?

Best,
[Your Name]""",
        "touch3_na": """Hi [First Name],

No problem at all if timing isn't right.

Feel free to browse our full commercial product range at encore-tech.com whenever your next project kicks off.

Best,
[Your Name]"""
    },
    "FLEX": {
        "title": "FLEX Multi-Angle Architectural Track Spotlight",
        "cn_name": "FLEX 极致灵活多角度商业轨道灯",
        "specs": "万向双轴精密阻尼调节 | 极小旋转半径 | 适合复杂刁钻角度天花板与立面打光 | 高强度精工转轴",
        "persona_na": "异形商业空间、斜顶阁楼店面、立面商品陈列繁复的精品店设计师",
        "pain_na": "普通轨道灯旋转死角多，遇到斜屋顶或紧贴墙壁的死角无法精准照亮，或者调节后转轴松动下垂。",
        "sol_na": "特制阻尼双万向节，360°+90° 任意角度随心定格，永不下坠；刁钻角度空间照明终极方案。",
        "subjs_na": [
            "track spotlight with zero blind spots: Encore FLEX series",
            "multi-angle architectural spotlights for tricky ceiling geometries",
            "precision aiming track lighting for [Company Name]'s fit-outs"
        ],
        "touch1_na": """Hi [First Name],

In projects with sloped ceilings, irregular structural beams, or tight wall displays, standard track lights often hit mechanical dead ends—leaving dark spots where lighting is needed most.

We engineered the FLEX Multi-Angle Track Spotlight to eliminate aiming limitations:
• Dual-Axis Free Articulation: High-precision damped joints allow smooth 360° horizontal rotation and 90° tilt with zero aiming blind spots.
• Stay-Put Damping: High-friction aerospace-grade hinge design ensures fixtures stay exactly where aimed without sagging over time.
• Crisp Visual Definition: CRI 95+ precision optics designed to sculpt architectural surfaces and merchandise displays.

Would it be helpful to see a sample of FLEX to test the hinge damping and build quality?

Best regards,

[Your Name]
Encore Commercial Lighting""",
        "touch2_na": """Hi [First Name],

Following up on the FLEX series.

If you have any current commercial spaces with sloped ceilings, exposed ducts, or complex architectural soffits, FLEX is the go-to solution for challenging geometry.

Let me know if you'd like a quick cut-sheet.

Best,
[Your Name]""",
        "touch3_na": """Hi [First Name],

Closing the loop on FLEX. You can always check our full range of commercial fixtures at encore-tech.com.

Best regards,
[Your Name]"""
    },
    "MEGA": {
        "title": "MEGA High-Value Commercial Track Light Family",
        "cn_name": "MEGA 家族化高性价比商业轨道灯",
        "specs": "全功率覆盖 (15W-35W) | 极高性价比 | 大规模连锁商铺首选 | 极低不良率 | 结构坚固耐用",
        "persona_na": "预算严格的中端商业连锁品牌、快时尚零售店装承包商、大面积商业展厅采购经理",
        "pain_na": "预算被卡得很紧，高端大牌买不起，买低端中山白牌灯又怕频繁烧灯、光衰严重导致售后扯皮。",
        "sol_na": "大厂工贸一体品控，价格仅为欧美同级品牌 1/3，但保持超低返修率与高光效，连锁快跑利器。",
        "subjs_na": [
            "stretch your retail lighting budget without sacrificing CRI (MEGA)",
            "reliable commercial track lighting for multi-store rollouts: MEGA",
            "cut fixture costs by 40% on your next commercial fit-out"
        ],
        "touch1_na": """Hi [First Name],

Balancing tight commercial fit-out budgets against client demands for premium lighting aesthetics is one of the toughest challenges for contractors and store planners today.

Our MEGA Track Light Family was engineered precisely for high-volume commercial and retail rollouts:
• High Optical Value: Delivers professional CRI 90+/95+ color fidelity at direct factory economics—typically 30-45% below local distributor pricing.
• Proven Durability: Robust thermal management and Tier-1 driver components, resulting in less than 0.2% field failure rates.
• Full Project Scaling: From 15W boutique accenting to 35W main ambient lighting in matching housing designs.

If you're bidding on any retail or commercial projects where budget margins are tight, we can provide a competitive cross-reference quote against your current fixture schedule.

Worth sending over an active schedule to compare?

Best regards,

[Your Name]
Encore Commercial Lighting""",
        "touch2_na": """Hi [First Name],

Following up on the MEGA family.

We can courier a working sample to your estimator or project manager so your team can verify the photometric output and build quality against your existing standard fixtures.

Where should we ship a benchmark sample?

Best,
[Your Name]""",
        "touch3_na": """Hi [First Name],

Wrapping up my note. Feel free to keep encore-tech.com on hand for when you need a competitive edge on your next commercial bid.

Best regards,
[Your Name]"""
    },
    "ELLA": {
        "title": "ELLA Ultra-Compact Architectural Downlight / Spotlight",
        "cn_name": "ELLA 超薄紧凑型商业筒射灯",
        "specs": "超浅吊顶深度需求 (Shallow Plenum) | 极小开孔高流明 | 精巧身段高防眩 | 适合低层高与复杂吊顶",
        "persona_na": "老旧建筑改造、低天花层高商铺、精致精品专卖店空间设计师",
        "pain_na": "商铺天花板内部管道密集，吊顶下沉空间极浅（只有 6-8cm），常规大筒灯根本塞不进去。",
        "sol_na": "超紧凑结构专为超浅吊顶设计，微小体积爆发出色照度与深防眩光斑，救场神器。",
        "subjs_na": [
            "shallow ceiling depth problem? The ultra-compact ELLA series",
            "architectural downlights engineered for tight ceiling plenums",
            "compact, zero-glare spotlights for boutique spaces: ELLA"
        ],
        "touch1_na": """Hi [First Name],

In many urban commercial renovations and low-ceiling retail shops, HVAC ducts and tight structural plenums make it almost impossible to install standard deep-regression downlights.

We designed the ELLA Compact Architectural Downlight Series specifically for spaces with limited ceiling clearance:
• Ultra-Shallow Housing: Requires less than 2.8 inches of ceiling depth while maintaining deep optical shielding.
• Miniature Footprint: Discreet ceiling apertures that preserve a clean, uncluttered visual rhythm.
• Punchy Performance: High-lumen density with precision beam distribution and CRI 95+ fidelity.

If you frequently encounter tight ceiling plenums in your commercial projects, ELLA is an essential problem-solver.

Would you like to see the dimensional cut-sheet?

Best regards,

[Your Name]
Encore Commercial Lighting""",
        "touch2_na": """Hi [First Name],

Quick follow-up on ELLA. We can dispatch a sample unit to your studio within 48 hours so you can test its installation profile in mockups.

Any challenging low-ceiling spaces on your boards right now?

Best,
[Your Name]""",
        "touch3_na": """Hi [First Name],

No problem if you don't have shallow-plenum requirements today. Our complete range is always accessible at encore-tech.com.

Best,
[Your Name]"""
    },
    "GALAXY": {
        "title": "GALAXY High-End Architectural Downlight System",
        "cn_name": "GALAXY 高端商业天花筒射灯系列",
        "specs": "高端五星级酒店/品牌旗舰店级别 | 多重防眩黑光技术 | 纯净光斑边缘过度柔和 | 支持高端智能调光协议",
        "persona_na": "高端商业会所、轻奢品牌专卖店、精品酒店大堂与客房照明设计师",
        "pain_na": "光斑边缘有黄圈、杂散光溢出；调光时低端有频闪或阶梯感跳变，达不到奢华氛围要求。",
        "sol_na": "顶级光学级复眼透镜与黑光防眩技术，极佳的光斑平滑过渡，0.1% 深度平滑无频闪调光。",
        "subjs_na": [
            "premium architectural downlighting for luxury hospitality (GALAXY)",
            "smooth 0.1% flicker-free dimming downlights for boutique projects",
            "museum-grade ceiling fixtures for [Company Name]'s luxury fit-outs"
        ],
        "touch1_na": """Hi [First Name],

For luxury hospitality, fine dining, and premier retail spaces, the difference between an average commercial space and a luxury interior often comes down to the quality of the light beam transition and deep dimming smoothness.

Our GALAXY Architectural Downlight System is engineered for premium environments:
• Velvet Smooth Beam: Multi-faceted optical reflectors eliminate secondary yellow rings and stray halos for a flawless light pool.
• True 0.1% Dim-to-Dark: Flicker-free deep dimming supporting DALI-2, 0-10V, and Lutron ecosystems.
• Tactile Luxury Finishes: Precision CNC-machined baffles available in matte black, specularity gold, and dark-light chrome.

We’ve supplied lighting for premier hotels including the Grand Hotel Hangzhou and cultural institutions across Europe.

Would you like a sample case of GALAXY shipped to your office for an upcoming mock-up?

Best regards,

[Your Name]
Encore Commercial Lighting""",
        "touch2_na": """Hi [First Name],

Checking back on the GALAXY series.

Lighting designers love our Dark-Light baffle technology—even when the luminaire is delivering 1,500 lumens, the ceiling opening remains visually dark from normal vantage points.

Could I send over a PDF lookbook?

Best,
[Your Name]""",
        "touch3_na": """Hi [First Name],

Wrapping up my note. Whenever you have a flagship hospitality or luxury project that demands the highest optical finesse, feel free to connect with us at encore-tech.com.

Best regards,
[Your Name]"""
    }
}

print(f"Loaded {len(PRODUCTS_DATA)} product data profiles.")

# Generator Functions

def generate_na_doc(p_key, p_info):
    filename = f"Encore_北美开发信_{p_key}_{p_info['title'].split()[0]}.docx"
    filepath = os.path.join(dir_na, filename)
    doc = create_styled_document()
    
    add_header(doc, 
               f"{p_info['title']} - 北美专属开发信方案",
               f"产品系列：{p_info['cn_name']} | 目标市场：美国、加拿大 (US / Canada)",
               "北美市场专属")
    
    add_callout(doc, "北美市场定位与买家画像 (Target Buyer Persona)", 
                f"• 核心目标客户：{p_info['persona_na']}\n"
                f"• 北美买家核心痛点：{p_info['pain_na']}\n"
                f"• 我们的核心破局优势：{p_info['sol_na']}\n"
                f"• 关键技术参数：{p_info['specs']}")
    
    insert_product_images(doc, p_key, "北美工程实物配件与高品质出样")
    
    add_email_box(doc, 1, "首触破冰（痛点击穿 + 核心价值 + 样品邀约）", p_info['subjs_na'], p_info['touch1_na'])
    add_email_box(doc, 2, "3-4天后跟进（施工细节 + 加拿大/海外工程背书加码）", [f"Re: {p_info['subjs_na'][0]}"], p_info['touch2_na'])
    add_email_box(doc, 3, "7-10天后价值收尾（免费DIALux方案 + 24小时报价 + 无压力退场）", [f"Re: {p_info['subjs_na'][0]}"], p_info['touch3_na'])
    
    add_callout(doc, "业务员实战建议 (Actionable Sales Tips)", 
                "1. 北美客户极度看重 120-277V 宽压和 ETL/UL 认证，在首封邮件或沟通中务必主动标明已有合规认证。\n"
                "2. 针对美加中小装修承包商 (Shopfitters)，直接提出'免费帮你核算图纸报价 (24h lighting take-off)'通常回复率极高。\n"
                "3. 寄送样品时，建议提供带有精美手提箱或内衬泡沫的 $50 Benchmark Kit，大幅提高设计事务所的实测通过率。",
                "EFF6FF")
    
    doc.save(filepath)
    return filepath

def generate_eu_doc(p_key, p_info):
    filename = f"Encore_欧澳开发信_{p_key}_{p_info['title'].split()[0]}.docx"
    filepath = os.path.join(dir_eu, filename)
    doc = create_styled_document()
    
    add_header(doc, 
               f"{p_info['title']} - 欧澳成熟市场专属方案",
               f"产品系列：{p_info['cn_name']} | 目标市场：欧洲主要国家、澳大利亚 (UK/EU/AU)",
               "欧澳成熟市场专属")
    
    add_callout(doc, "欧澳市场定位与买家画像 (Target Buyer Persona)", 
                f"• 核心目标客户：欧洲与澳洲高端商业/建筑照明设计师、精品画廊与艺术机构策展人、独立设计事务所\n"
                f"• 欧澳买家核心痛点：对视觉纯粹度、眩光 (UGR<16)、显指 (CRI 95+) 极其挑剔；厌恶粗糙外置驱动盒与光斑杂色。\n"
                f"• 我们的核心破局优势：具备 CE/SAA 严苛认证，爱尔兰艺术馆与国家博物馆落地背书，极简隐藏式设计。\n"
                f"• 关键技术参数：{p_info['specs']}")
    
    insert_product_images(doc, p_key, "欧澳工程案例实景与光学结构细节")
    
    # Adapted EU email copy
    eu_subjs = [
        f"architectural lighting for [Company Name]'s gallery & retail fit-outs",
        f"museum-grade optics delivered direct (Irish gallery pedigree)",
        f"clean ceiling aesthetics: Encore {p_key} series"
    ]
    eu_touch1 = p_info['touch1_na'].replace("North America", "Europe & Australia").replace("ETL Listed for North America", "CE / SAA Certified").replace("120-277V", "220-240V DALI-2 & Casambi")
    
    add_email_box(doc, 1, "首触破冰（欧洲美学标准 + 爱尔兰艺术馆案例背书 + 样品邀约）", eu_subjs, eu_touch1)
    add_email_box(doc, 2, "3-4天后跟进（DALI-2/Casambi 调光体验 + 极简光学配件）", [f"Re: {eu_subjs[0]}"], p_info['touch2_na'])
    add_email_box(doc, 3, "7-10天后价值收尾（欧洲设计师专属资料包）", [f"Re: {eu_subjs[0]}"], p_info['touch3_na'])
    
    add_callout(doc, "欧澳业务员实战建议", 
                "1. 欧洲和澳洲设计师对'可持续性 (Eco-design)'和'无目眩感 (Visual Comfort)'极其敏感，多强调模块化可更换核心与 UGR 等级。\n"
                "2. 调光方面，欧澳客户最偏爱 DALI-2 和 Casambi 智能控制生态，报价时可优先推荐该调光方案。",
                "F0FDF4")
    
    doc.save(filepath)
    return filepath

def generate_emerging_doc(p_key, p_info):
    filename = f"Encore_新市场(东南亚与中东)_{p_key}.docx"
    filepath = os.path.join(dir_em, filename)
    doc = create_styled_document()
    
    add_header(doc, 
               f"{p_info['title']} - 东南亚与中东新零售咖啡馆全案方案",
               f"产品系列：{p_info['cn_name']} | 目标市场：曼谷、吉隆坡、胡志明、迪拜、沙特等新兴都会商业",
               "新零售商业新市场")
    
    add_callout(doc, "新兴商业都会区买家画像与打法", 
                f"• 核心目标客户：东南亚及中东的独立精品咖啡馆、潮牌女装买手店、高端清吧主理人及室内装修设计公司\n"
                f"• 买家核心痛点：欧美一线大牌（ERCO/iGuzzini）价格天价，本地小买家预算承受不起；国内低端杂牌又频闪严重、拍照反光泛绿。\n"
                f"• 破局杀手锏：打出'国家博物馆级光学质感 + 高出片率防频闪 + 欧美大牌 1/3 价格 + 极速打样出货'。\n"
                f"• 沟通利器：邮件发送初次邀约，同时建立 WhatsApp 快速通道（发10秒实景小视频比长篇参数管用十倍！）。")
    
    insert_product_images(doc, p_key, "精品商业店铺出片实景与灯光氛围")
    
    em_subjs = [
        f"commercial lighting for your boutique & cafe projects (CRI 95+)",
        f"high-end optics at 1/3 distributor cost: Encore {p_key}",
        f"quick question on [Company Name]'s upcoming retail fit-outs"
    ]
    em_touch1 = f"""Hi [First Name],

Love the design aesthetic and social buzz around [Company Name]’s recent boutique spaces in [City]!

For fashion stores and specialty cafes, lighting either elevates fabrics and interior textures, or causes harsh glare and camera flicker on social media shoots.

We supply the {p_info['title']} engineered with National Museum precision:
• True Color Fidelity (CRI 95+): Makes apparel colors, natural woods, and food textures pop authentically without color distortion.
• Zero-Flicker Dimming: 100% camera-friendly performance tested for smartphones and professional video shoots.
• Factory-Direct Advantage: Museum-grade optical performance delivered directly from our factory floor at 1/3 the price of international brands.

We can produce a complimentary DIALux lighting simulation for your project floor plan, and courier sample units directly to your office.

Can I share our WhatsApp (+86-xxx) to send a 15-second lighting video, or would you prefer a digital lookbook here?

Best regards,

[Your Name]
Encore Commercial Lighting
encore-tech.com"""
    
    add_email_box(doc, 1, "首触破冰（高出片率 + 零频闪 + 博物馆级CRI95+ + WhatsApp链接）", em_subjs, em_touch1)
    add_email_box(doc, 2, "3-4天后跟进（直接给出女装店/咖啡馆灯光搭配方案）", [f"Re: {em_subjs[0]}"], p_info['touch2_na'])
    add_email_box(doc, 3, "7-10天后价值收尾（免费DIALux方案邀约）", [f"Re: {em_subjs[0]}"], p_info['touch3_na'])
    
    add_callout(doc, "东南亚与中东私域跟进 SOP (WhatsApp & Instagram)", 
                "1. 在 Instagram 刷到目标城市的新开咖啡馆或女装店，直接在其官方 Ins 发送简短好评，并私信询问负责设计的团队。\n"
                "2. 获得 WhatsApp 号码后，第一时间发送 2 条 10 秒短视频：一条展示灯具照在真丝面料上的高级色彩，另一条展示平滑无频闪调光。\n"
                "3. 东南亚客户决策迅速，若遇到项目工期紧，主动提出 7-10 天内通过 DHL 空运出样，成单率超 60%。",
                "FEF3C7")
    
    doc.save(filepath)
    return filepath

def generate_specialty_doc():
    filename = "Encore_特种高溢价方案_汽车展厅与高天花博物馆(MOVIA与数显).docx"
    filepath = os.path.join(dir_spec, filename)
    doc = create_styled_document()
    
    add_header(doc, 
               "特种高溢价商业方案：汽车展厅与高天花博物馆照明",
               "核心主打：MOVIA 电动智能遥控轨道灯 + Digital Display 数显精准变焦轨道灯",
               "特种高溢价项目专攻")
    
    add_callout(doc, "特种项目定位与杀手锏", 
                "• 核心目标客户：豪华汽车展厅 (Auto Showrooms / Custom Studios)、挑高 5-8 米艺术展馆、高端珠宝与私人会所\n"
                "• 核心痛点：高天花人工调光极其昂贵危险（需要脚手架与爬梯）；展车或展品轮换频繁，每次更换布局都要调光。\n"
                "• 我们的王炸底牌：加拿大汽车改装展厅落地案例背书 + 手机 App (Casambi) 一键遥控电机变焦调角 + 数显屏精准复位。")
    
    insert_product_images(doc, "MOVIA", "MOVIA 遥控电机与加拿大车行展厅实景")
    insert_product_images(doc, "Digital Display Track Light", "数显屏幕精准刻度与变焦细节")
    
    add_email_box(doc, 1, "汽车展厅与高天花专属开发信（告别爬梯 + 手机一键调光）", 
                  PRODUCTS_DATA["MOVIA"]["subjs_na"], 
                  PRODUCTS_DATA["MOVIA"]["touch1_na"])
    
    add_email_box(doc, 2, "3-4天跟进（加拿大汽车展厅真实客户案例量化降本数据）", 
                  [f"Re: {PRODUCTS_DATA['MOVIA']['subjs_na'][0]}"], 
                  PRODUCTS_DATA["MOVIA"]["touch2_na"])
                  
    doc.save(filepath)
    return filepath

def generate_master_manual():
    filename = "Encore_全系列全市场商业照明开发信实战总揽手册(完整汇编).docx"
    filepath = os.path.join(dir_all, filename)
    doc = create_styled_document()
    
    add_header(doc, 
               "Encore 全系列商业照明开发信实战总揽手册 (Master Manual)",
               "包含 14 大产品系列 · 3 大目标市场战略 · 完整中英双语图文开发信与跟进序列",
               "公司级销售与开发信圣经")
    
    add_callout(doc, "致 Encore 业务团队：本手册使用指南", 
                "本手册根据公司内部 14 个系列（AVA、DELLA、Digital Display、ELLA、EVO、FLEX、GALAXY、IMAX、MAGNETIC、MEGA、MOVIA、NOVA、OVEGA、VEGA）的业务员实战开发信深度迭代而成。\n\n"
                "战略重点：\n"
                "1. 主力攻坚北美市场（美国、加拿大）：全面主打 ETL/UL 认证、2周出样时效、深防眩光斑、加拿大汽车展厅背书。\n"
                "2. 深耕欧澳成熟市场（英国、欧洲、澳洲）：主打 CE/SAA 认证、爱尔兰艺术馆案例、隐形驱动盒美学。\n"
                "3. 抢滩新兴爆发市场（东南亚、中东）：主打新零售女装店、独立咖啡馆整体方案、高出片率、WhatsApp 快速沟通。\n\n"
                "使用方法：业务员开发新客户时，可直接按客户所在的国家和项目类型复制对应章节的主题与正文，按模板替换 [First Name] 和 [Company Name] 即可直接发信。")
    
    for p_key, p_info in PRODUCTS_DATA.items():
        doc.add_page_break()
        add_section_title(doc, f"【系列 {p_key}】{p_info['title']} ({p_info['cn_name']})")
        add_callout(doc, f"{p_key} 核心卖点与北美开发信建议", 
                    f"规格参数：{p_info['specs']}\n"
                    f"目标买家：{p_info['persona_na']}\n"
                    f"买家痛点：{p_info['pain_na']}\n"
                    f"破局亮点：{p_info['sol_na']}")
        
        insert_product_images(doc, p_key, f"{p_key} 系列实物图")
        add_email_box(doc, 1, f"{p_key} 北美首触开发信", p_info['subjs_na'], p_info['touch1_na'])
        add_email_box(doc, 2, f"{p_key} 3-4天跟进信", [f"Re: {p_info['subjs_na'][0]}"], p_info['touch2_na'])
    
    doc.save(filepath)
    return filepath

# Execute all generations
print("Generating North America Word docs...")
na_files = [generate_na_doc(k, v) for k, v in PRODUCTS_DATA.items()]

print("Generating Europe & Australia Word docs...")
eu_files = [generate_eu_doc(k, v) for k, v in PRODUCTS_DATA.items()]

print("Generating Emerging Markets Word docs...")
em_files = [generate_emerging_doc(k, v) for k, v in PRODUCTS_DATA.items()]

print("Generating Specialty Showroom & Museum doc...")
spec_file = generate_specialty_doc()

print("Generating Master Manual...")
master_file = generate_master_manual()

total_count = len(na_files) + len(eu_files) + len(em_files) + 1 + 1
print(f"SUCCESS! Generated {total_count} professional Word documents in D:\\marketing\\开发信Word库_完整版")
