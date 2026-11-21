# -*- coding: utf-8 -*-
import os
import base64
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

img_dir = r"D:\marketing\开发信Word库_完整版\邮件图片附件_方便直接插入"
imgs = [os.path.join(img_dir, f"Foto_{i}_Carril_Magnetico_48V.jpg") for i in [1, 2, 3]]

# 1. Build Word Document
doc = docx.Document()
for s in doc.sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

# Subject
p_subj = doc.add_paragraph()
p_subj.paragraph_format.space_after = Pt(12)
r_sl = p_subj.add_run("Asunto: ")
r_sl.bold = True
r_sl.font.size = Pt(11)
r_sl.font.color.rgb = RGBColor(3, 105, 161)
r_st = p_subj.add_run("Novedades ópticas para vuestro sistema de carril magnético 48V (Barcelona LED)")
r_st.bold = True
r_st.font.size = Pt(11)

# Greeting
p_g = doc.add_paragraph()
p_g.paragraph_format.space_after = Pt(8)
p_g.add_run("Hola equipo de Barcelona LED,").font.size = Pt(10.5)

# Intro
p_i1 = doc.add_paragraph()
p_i1.paragraph_format.space_after = Pt(8)
p_i1.add_run("He estado siguiendo de cerca vuestro showroom en Cornellà de Llobregat y vuestra sólida gama de iluminación sobre carril magnético de 48V.").font.size = Pt(10.5)

p_i2 = doc.add_paragraph()
p_i2.paragraph_format.space_after = Pt(8)
p_i2.add_run("Al prescribir o suministrar sistemas magnéticos para retail boutique, hostelería o espacios singulares en España, la luminaria es solo una parte de la ecuación. La fiabilidad eléctrica a largo plazo, la consistencia óptica (SDCM < 3) y la facilidad de montaje marcan la verdadera diferencia para los instaladores e interioristas.").font.size = Pt(10.5)

p_i3 = doc.add_paragraph()
p_i3.paragraph_format.space_after = Pt(10)
p_i3.add_run("En ENCORE hemos desarrollado nuestra Plataforma de Carril Magnético 48V desde una perspectiva puramente técnica y de ingeniería:").font.size = Pt(10.5)

# Section 1
p_h1 = doc.add_paragraph()
p_h1.paragraph_format.space_before = Pt(6)
p_h1.paragraph_format.space_after = Pt(4)
r_h1 = p_h1.add_run("1. Flexibilidad Arquitectónica y Modularidad Total")
r_h1.bold = True
r_h1.font.size = Pt(10.5)
r_h1.font.color.rgb = RGBColor(26, 54, 93)

p_b1_1 = doc.add_paragraph(style='List Bullet')
p_b1_1.paragraph_format.space_after = Pt(2)
p_b1_1.add_run("Perfiles de 20 mm, 10 mm y micro-carril: versiones empotradas (trimless), de superficie y suspendidas.").font.size = Pt(10)

p_b1_2 = doc.add_paragraph(style='List Bullet')
p_b1_2.paragraph_format.space_after = Pt(8)
p_b1_2.add_run("Módulos intercambiables al instante: focos orientables con ópticas de corte preciso, bañadores lineales de pared, micro-rejillas antideslumbramiento (UGR < 10) y módulos decorativos colgantes.").font.size = Pt(10)

# Img 1 (width 4.0 inches fits email perfectly)
p_img1 = doc.add_paragraph()
p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_img1.paragraph_format.space_after = Pt(12)
p_img1.add_run().add_picture(imgs[0], width=Inches(4.0))

# Section 2
p_h2 = doc.add_paragraph()
p_h2.paragraph_format.space_before = Pt(6)
p_h2.paragraph_format.space_after = Pt(4)
r_h2 = p_h2.add_run("2. Ingeniería Diseñada para Cero Incidencias en Obra")
r_h2.bold = True
r_h2.font.size = Pt(10.5)
r_h2.font.color.rgb = RGBColor(26, 54, 93)

p_b2_1 = doc.add_paragraph(style='List Bullet')
p_b2_1.paragraph_format.space_after = Pt(2)
p_b2_1.add_run("Conductores de cobre puro de alta sección con mayor superficie de contacto para una conductividad impecable sin caídas de tensión.").font.size = Pt(10)

p_b2_2 = doc.add_paragraph(style='List Bullet')
p_b2_2.paragraph_format.space_after = Pt(2)
p_b2_2.add_run("Perfil de aluminio extruido reforzado de 3 mm para una estabilidad perfecta sin torsión.").font.size = Pt(10)

p_b2_3 = doc.add_paragraph(style='List Bullet')
p_b2_3.paragraph_format.space_after = Pt(2)
p_b2_3.add_run("Doble fijación de seguridad: anclaje magnético asistido por bloqueo mecánico de liberación rápida, garantizando total seguridad sin vibraciones.").font.size = Pt(10)

p_b2_4 = doc.add_paragraph(style='List Bullet')
p_b2_4.paragraph_format.space_after = Pt(8)
p_b2_4.add_run("Conexión sin polaridad para agilizar el montaje y eliminar errores de instalación.").font.size = Pt(10)

# Img 2
p_img2 = doc.add_paragraph()
p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_img2.paragraph_format.space_after = Pt(12)
p_img2.add_run().add_picture(imgs[1], width=Inches(4.0))

# Section 3
p_h3 = doc.add_paragraph()
p_h3.paragraph_format.space_before = Pt(6)
p_h3.paragraph_format.space_after = Pt(4)
r_h3 = p_h3.add_run("3. Máxima Calidad Óptica y Certificación Europea")
r_h3.bold = True
r_h3.font.size = Pt(10.5)
r_h3.font.color.rgb = RGBColor(26, 54, 93)

p_b3_1 = doc.add_paragraph(style='List Bullet')
p_b3_1.paragraph_format.space_after = Pt(2)
p_b3_1.add_run("Motores LED Bridgelux / Citizen COB con CRI 95+ (R9 > 80) y SDCM < 3 para una fidelidad cromática absoluta.").font.size = Pt(10)

p_b3_2 = doc.add_paragraph(style='List Bullet')
p_b3_2.paragraph_format.space_after = Pt(2)
p_b3_2.add_run("Control DALI-2, 0-10V y sistemas inalámbricos Casambi.").font.size = Pt(10)

p_b3_3 = doc.add_paragraph(style='List Bullet')
p_b3_3.paragraph_format.space_after = Pt(8)
p_b3_3.add_run("Certificados CE y RoHS disponibles, con entrega directa de muestras a vuestro showroom en menos de 2 semanas.").font.size = Pt(10)

# Img 3
p_img3 = doc.add_paragraph()
p_img3.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_img3.paragraph_format.space_after = Pt(12)
p_img3.add_run().add_picture(imgs[2], width=Inches(4.0))

# Close & CTA
p_c1 = doc.add_paragraph()
p_c1.paragraph_format.space_after = Pt(8)
p_c1.add_run("Si estáis valorando ampliar vuestra propuesta de carril magnético con una línea arquitectónica de ingeniería superior y precio directo de fábrica, nos encantaría enviaros una muestra física de prueba o un catálogo técnico completo a vuestras instalaciones de Cornellà.").font.size = Pt(10.5)

p_c2 = doc.add_paragraph()
p_c2.paragraph_format.space_after = Pt(14)
r_c2 = p_c2.add_run("¿Tendría sentido coordinar el envío de un maletín de muestras para vuestro departamento técnico o de compras?")
r_c2.bold = True
r_c2.font.size = Pt(10.5)

# Signature with Bob details
p_sign = doc.add_paragraph()
p_sign.add_run("Un cordial saludo,\n\n").font.size = Pt(10)
r_bob = p_sign.add_run("Bob\n")
r_bob.bold = True
r_bob.font.size = Pt(10.5)
p_sign.add_run("Encore Commercial Lighting\nWeb: encore-tech.com\nWhatsApp: +852 57651719\n").font.size = Pt(10)

docx_path = r"D:\marketing\开发信Word库_完整版\Encore_Barcelona_LED专属西语开发信(Bob签名版).docx"
doc.save(docx_path)
print("SUCCESS: Docx saved to", docx_path)

# 2. Build HTML File for 100% Flawless Copy-Paste into Webmail / Outlook
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

b64_img1 = img_to_base64(imgs[0])
b64_img2 = img_to_base64(imgs[1])
b64_img3 = img_to_base64(imgs[2])

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Encore Lighting - Propuesta para Barcelona LED</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #1e293b; line-height: 1.6; max-width: 650px; margin: 20px auto; padding: 20px; border: 1px solid #e2e8f0; border-radius: 8px; }}
.subject-box {{ background-color: #f0f9ff; border-left: 4px solid #0284c7; padding: 10px 14px; margin-bottom: 20px; font-weight: bold; color: #0369a1; }}
h3 {{ color: #1a365d; margin-top: 24px; margin-bottom: 8px; font-size: 16px; }}
ul {{ margin-top: 4px; padding-left: 20px; }}
li {{ margin-bottom: 6px; font-size: 14px; }}
.product-img {{ display: block; max-width: 100%; height: auto; margin: 16px auto; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
.signature {{ margin-top: 28px; border-top: 1px solid #e2e8f0; padding-top: 14px; font-size: 14px; color: #475569; }}
.signature strong {{ color: #0f172a; font-size: 15px; }}
</style>
</head>
<body>

<div class="subject-box">
Asunto: Novedades ópticas para vuestro sistema de carril magnético 48V (Barcelona LED)
</div>

<p>Hola equipo de Barcelona LED,</p>

<p>He estado siguiendo de cerca vuestro showroom en Cornellà de Llobregat y vuestra sólida gama de iluminación sobre carril magnético de 48V.</p>

<p>Al prescribir o suministrar sistemas magnéticos para retail boutique, hostelería o espacios singulares en España, la luminaria es solo una parte de la ecuación. La fiabilidad eléctrica a largo plazo, la consistencia óptica (SDCM &lt; 3) y la facilidad de montaje marcan la verdadera diferencia para los instaladores e interioristas.</p>

<p>En ENCORE hemos desarrollado nuestra Plataforma de Carril Magnético 48V desde una perspectiva puramente técnica y de ingeniería:</p>

<h3>1. Flexibilidad Arquitectónica y Modularidad Total</h3>
<ul>
  <li>Perfiles de 20 mm, 10 mm y micro-carril: versiones empotradas (trimless), de superficie y suspendidas.</li>
  <li>Módulos intercambiables al instante: focos orientables con ópticas de corte preciso, bañadores lineales de pared, micro-rejillas antideslumbramiento (UGR &lt; 10) y módulos decorativos colgantes.</li>
</ul>
<img class="product-img" src="data:image/jpeg;base64,{b64_img1}" alt="Carril Magnético 48V Módulos">

<h3>2. Ingeniería Diseñada para Cero Incidencias en Obra</h3>
<ul>
  <li>Conductores de cobre puro de alta sección con mayor superficie de contacto para una conductividad impecable sin caídas de tensión.</li>
  <li>Perfil de aluminio extruido reforzado de 3 mm para una estabilidad perfecta sin torsión.</li>
  <li>Doble fijación de seguridad: anclaje magnético asistido por bloqueo mecánico de liberación rápida, garantizando total seguridad sin vibraciones.</li>
  <li>Conexión sin polaridad para agilizar el montaje y eliminar errores de instalación.</li>
</ul>
<img class="product-img" src="data:image/jpeg;base64,{b64_img2}" alt="Detalle de conductores y bloqueo mecánico">

<h3>3. Máxima Calidad Óptica y Certificación Europea</h3>
<ul>
  <li>Motores LED Bridgelux / Citizen COB con CRI 95+ (R9 &gt; 80) y SDCM &lt; 3 para una fidelidad cromática absoluta.</li>
  <li>Control DALI-2, 0-10V y sistemas inalámbricos Casambi.</li>
  <li>Certificados CE y RoHS disponibles, con entrega directa de muestras a vuestro showroom en menos de 2 semanas.</li>
</ul>
<img class="product-img" src="data:image/jpeg;base64,{b64_img3}" alt="Óptica antideslumbramiento y proyección">

<p>Si estáis valorando ampliar vuestra propuesta de carril magnético con una línea arquitectónica de ingeniería superior y precio directo de fábrica, nos encantaría enviaros una muestra física de prueba o un catálogo técnico completo a vuestras instalaciones de Cornellà.</p>

<p><strong>¿Tendría sentido coordinar el envío de un maletín de muestras para vuestro departamento técnico o de compras?</strong></p>

<div class="signature">
  Un cordial saludo,<br><br>
  <strong>Bob</strong><br>
  Encore Commercial Lighting<br>
  Web: <a href="https://encore-tech.com">encore-tech.com</a><br>
  WhatsApp: +852 57651719
</div>

</body>
</html>
"""

html_path = r"D:\marketing\开发信Word库_完整版\Encore_Barcelona_LED专属西语开发信(网页一键复制版).html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("SUCCESS: HTML saved to", html_path)
