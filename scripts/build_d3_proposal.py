import os
import base64
import shutil
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

target_dir = 'D:/marketing/开发信Word库_完整版'
os.makedirs(target_dir, exist_ok=True)
img_dest_dir = os.path.join(target_dir, 'D3_Design_提案配套图片')
os.makedirs(img_dest_dir, exist_ok=True)

img_della = os.path.join(img_dest_dir, '1_DELLA_2.0_Architectural_Downlight.png')
img_magnetic = os.path.join(img_dest_dir, '2_48V_Magnetic_Track_System.png')
img_vega = os.path.join(img_dest_dir, '3_VEGA_InTrack_Spotlight.png')

def to_b64(path):
    with open(path, 'rb') as f:
        ext = 'png' if path.endswith('.png') else 'jpeg'
        return f'data:image/{ext};base64,' + base64.b64encode(f.read()).decode('utf-8')

b64_della = to_b64(img_della)
b64_magnetic = to_b64(img_magnetic)
b64_vega = to_b64(img_vega)

# 1. Generate HTML
html_content = f'''<!DOCTYPE html>
<html lang="bg">
<head>
<meta charset="utf-8">
<title>Encore Lighting - Предложение за D3 Design</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; line-height: 1.6; max-width: 650px; margin: 20px auto; padding: 22px; border: 1px solid #e2e8f0; border-radius: 8px; }}
.subject-box {{ background-color: #f0fdf4; border-left: 4px solid #16a34a; padding: 12px 16px; margin-bottom: 22px; font-weight: bold; color: #166534; font-size: 15px; }}
h3 {{ color: #1e3a8a; margin-top: 26px; margin-bottom: 10px; font-size: 16px; }}
ul {{ margin-top: 6px; padding-left: 20px; }}
li {{ margin-bottom: 7px; font-size: 14.5px; color: #334155; }}
.product-img {{ display: block; max-width: 100%; height: auto; margin: 16px auto; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
.signature {{ margin-top: 30px; border-top: 1px solid #e2e8f0; padding-top: 16px; font-size: 14px; color: #475569; }}
.signature strong {{ color: #0f172a; font-size: 15px; }}
p {{ font-size: 14.5px; margin-bottom: 14px; }}
</style>
</head>
<body>

<div class="subject-box">
Относно: Архитектурно осветление за вашите интериорни проекти в София (Encore)
</div>

<p>Здравейте, Ирен, Николай и екип на D3 Design,</p>

<p>Следя проектите ви и изключително много ценя чистия баланс между функционалност, визуална естетика и детайл, който постигате в интериорния дизайн.</p>

<p>Като дизайнери със сигурност познавате честия проблем при изпълнение на обекти: в 3D визуализацията светлината изглежда перфектна, мека и ненатрапчива, а в реалността масовите осветителни тела често заслепяват или изкривяват естествените тонове на дървото и камъка.</p>

<p>Ние сме фабрика за архитектурно и търговско осветление в Шънджън (Encore Commercial Lighting). Работим директно с интериорни и архитектурни бюра в Европа и подбрахме 3 серии тела, които пасват точно на изчистения стил на вашите интериори:</p>

<h3>1. За жилищни пространства и акцентни стени: Архитектурни луни DELLA 2.0</h3>
<ul>
  <li><strong>Дълбок анти-отблясък (UGR &lt; 10 и Pinhole UGR &lt; 6)</strong>: Окото вижда приятното светлинно петно, а таванът остава визуално спокоен без заслепяване.</li>
  <li><strong>Модулна система с едно ядро</strong>: Едно LED ядро покрива фиксирани луни, 30° насочващи се спотове и wall-wash за равномерно осветяване на картини и текстури.</li>
  <li><strong>Реалистични цветове (CRI 95+, 2700K / 3000K)</strong>: Подчертава естествените текстури на дърво, камък и мазилки точно както във вашите рендери.</li>
</ul>
<img class="product-img" src="{b64_della}" alt="DELLA 2.0 Architectural Downlight">

<h3>2. За съвременни отворени пространства и апартаменти: 48V нисковолтова магнитна шина</h3>
<ul>
  <li><strong>Минималистичен контур</strong>: Вграден монтаж наравно с гипсокартона, открит или висящ монтаж без видими крепежи.</li>
  <li><strong>Гъвкавост с едно движение</strong>: Магнитни спотове, линейни дифузери за обща светлина и стенни шайби се местят свободно без инструменти и без преправяне на кабели.</li>
  <li><strong>Европейски стандарти</strong>: 48V безопасно напрежение с пълен набор от CE &amp; RoHS сертификати.</li>
</ul>
<img class="product-img" src="{b64_magnetic}" alt="48V Magnetic Track System">

<h3>3. За търговски обекти, галерии и високи тавани: VEGA In-Track Spotlight</h3>
<ul>
  <li><strong>Драйвер, скрит в релсата (In-Track Driver)</strong>: Няма обемисти външни кутии – само изчистен, компактен цилиндър.</li>
  <li><strong>Прецизна оптика</strong>: Бърза смяна на ъгъла (15° / 24° / 36° / 50°) и анти-отблясъчна пита (honeycomb) за прецизен светлинен акцент.</li>
  <li><strong>Интелигентен контрол</strong>: Поддържа DALI-2, 0-10V и Casambi Bluetooth управление за светлинни сценарии.</li>
</ul>
<img class="product-img" src="{b64_vega}" alt="VEGA In-Track Spotlight">

<p>За вашите 3D проекти и визуализации предоставяме <strong>безплатни IES фотометрични файлове и 3D модели</strong> на всички осветителни тела.</p>

<p><strong>Ако в момента работите по нов жилищен или обществен интериор, с удоволствие ще ви изпратим мострен комплект (sample kit) до офиса ви в София или ще подготвим ценово предложение директно по ваши чертежи. Имате ли интерес да разгледате мостри?</strong></p>

<div class="signature">
  Поздрави,<br><br>
  <strong>Боб (Bob)</strong><br>
  Encore Commercial Lighting<br>
  Уебсайт: <a href="https://encore-tech.com">encore-tech.com</a><br>
  WhatsApp: +852 57651719<br>
  Email: sales@encore-tech.com
</div>

</body>
</html>'''

html_path = 'D:/marketing/开发信Word库_完整版/Encore_D3_Design保加利亚语专属定制提案(网页一键复制版).html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated HTML successfully at:', html_path)

# 2. Generate DOCX
doc = Document()
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

# Title
title_p = doc.add_paragraph()
title_run = title_p.add_run('Относно: Архитектурно осветление за вашите интериорни проекти в София (Encore)')
title_run.font.name = 'Segoe UI'
title_run.font.size = Pt(13)
title_run.font.bold = True
title_run.font.color.rgb = RGBColor(22, 101, 52)
title_p.paragraph_format.space_after = Pt(14)

def add_p(text, bold=False, space_after=8):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.name = 'Segoe UI'
    r.font.size = Pt(10.5)
    r.font.bold = bold
    r.font.color.rgb = RGBColor(30, 41, 59)
    p.paragraph_format.space_after = Pt(space_after)
    return p

def add_heading(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.font.name = 'Segoe UI'
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(30, 58, 138)
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    return p

def add_bullet(lead, text):
    p = doc.add_paragraph(style='List Bullet')
    r1 = p.add_run(lead + ': ')
    r1.font.name = 'Segoe UI'
    r1.font.size = Pt(10)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(30, 41, 59)
    
    r2 = p.add_run(text)
    r2.font.name = 'Segoe UI'
    r2.font.size = Pt(10)
    r2.font.color.rgb = RGBColor(71, 85, 105)
    p.paragraph_format.space_after = Pt(3)
    return p

def add_img(path):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(12)
    p.add_run().add_picture(path, width=Inches(4.5))

add_p('Здравейте, Ирен, Николай и екип на D3 Design,')
add_p('Следя проектите ви и изключително много ценя чистия баланс между функционалност, визуална естетика и детайл, който постигате в интериорния дизайн.')
add_p('Като дизайнери със сигурност познавате честия проблем при изпълнение на обекти: в 3D визуализацията светлината изглежда перфектна, мека и ненатрапчива, а в реалността масовите осветителни тела често заслепяват или изкривяват естествените тонове на дървото и камъка.')
add_p('Ние сме фабрика за архитектурно и търговско осветление в Шънджън (Encore Commercial Lighting). Работим директно с интериорни и архитектурни бюра в Европа и подбрахме 3 серии тела, които пасват точно на изчистения стил на вашите интериори:')

# Product 1
add_heading('1. За жилищни пространства и акцентни стени: Архитектурни луни DELLA 2.0')
add_bullet('Дълбок анти-отблясък (UGR < 10 и Pinhole UGR < 6)', 'Окото вижда приятното светлинно петно, а таванът остава визуално спокоен без заслепяване.')
add_bullet('Модулна система с едно ядро', 'Едно LED ядро покрива фиксирани луни, 30° насочващи се спотове и wall-wash за равномерно осветяване на картини и текстури.')
add_bullet('Реалистични цветове (CRI 95+, 2700K / 3000K)', 'Подчертава естествените текстури на дърво, камък и мазилки точно както във вашите рендери.')
add_img(img_della)

# Product 2
add_heading('2. За съвременни отворени пространства и апартаменти: 48V нисковолтова магнитна шина')
add_bullet('Минималистичен контур', 'Вграден монтаж наравно с гипсокартона, открит или висящ монтаж без видими крепежи.')
add_bullet('Гъвкавост с едно движение', 'Магнитни спотове, линейни дифузери за обща светлина и стенни шайби се местят свободно без инструменти и без преправяне на кабели.')
add_bullet('Европейски стандарти', '48V безопасно напрежение с пълен набор от CE & RoHS сертификати.')
add_img(img_magnetic)

# Product 3
add_heading('3. За търговски обекти, галерии и високи тавани: VEGA In-Track Spotlight')
add_bullet('Драйвер, скрит в релсата (In-Track Driver)', 'Няма обемисти външни кутии – само изчистен, компактен цилиндър.')
add_bullet('Прецизна оптика', 'Бърза смяна на ъгъла (15° / 24° / 36° / 50°) и анти-отблясъчна пита (honeycomb) за прецизен светлинен акцент.')
add_bullet('Интелигентен контрол', 'Поддържа DALI-2, 0-10V и Casambi Bluetooth управление за светлинни сценарии.')
add_img(img_vega)

add_p('За вашите 3D проекти и визуализации предоставяме безплатни IES фотометрични файлове и 3D модели на всички осветителни тела.')
add_p('Ако в момента работите по нов жилищен или обществен интериор, с удоволствие ще ви изпратим мострен комплект (sample kit) до офиса ви в София или ще подготвим ценово предложение директно по ваши чертежи. Имате ли интерес да разгледате мостри?', bold=True)

# Signature
sig_p = doc.add_paragraph()
sig_p.paragraph_format.space_before = Pt(16)
sig_run = sig_p.add_run('Поздрави,\n\nБоб (Bob)\nEncore Commercial Lighting\nУебсайт: encore-tech.com\nWhatsApp: +852 57651719\nEmail: sales@encore-tech.com')
sig_run.font.name = 'Segoe UI'
sig_run.font.size = Pt(10)
sig_run.font.color.rgb = RGBColor(71, 85, 105)

docx_path = 'D:/marketing/开发信Word库_完整版/Encore_D3_Design保加利亚语专属定制提案(图文版).docx'
doc.save(docx_path)
print('Generated DOCX successfully at:', docx_path)
