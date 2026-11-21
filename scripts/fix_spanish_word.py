# -*- coding: utf-8 -*-
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = docx.Document()
for s in doc.sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

# 1. Asunto
p_subj = doc.add_paragraph()
p_subj.paragraph_format.space_after = Pt(12)
r_s_label = p_subj.add_run("Asunto: ")
r_s_label.bold = True
r_s_label.font.size = Pt(12)
r_s_label.font.color.rgb = RGBColor(3, 105, 161)
r_s_text = p_subj.add_run("Novedades ópticas para vuestro sistema de carril magnético 48V (Barcelona LED)")
r_s_text.bold = True
r_s_text.font.size = Pt(12)

# 2. Saludo
p_g = doc.add_paragraph()
p_g.paragraph_format.space_after = Pt(8)
r_g = p_g.add_run("Hola equipo de Barcelona LED,")
r_g.font.size = Pt(11)

# 3. Introducción
p_i1 = doc.add_paragraph()
p_i1.paragraph_format.space_after = Pt(8)
p_i1.add_run("He estado siguiendo de cerca vuestro showroom en Cornellà de Llobregat y vuestra sólida gama de iluminación sobre carril magnético de 48V.").font.size = Pt(10.5)

p_i2 = doc.add_paragraph()
p_i2.paragraph_format.space_after = Pt(8)
p_i2.add_run("Al prescribir o suministrar sistemas magnéticos para retail boutique, hostelería o espacios singulares en España, la luminaria es solo una parte de la ecuación. La fiabilidad eléctrica a largo plazo, la consistencia óptica (SDCM < 3) y la facilidad de montaje marcan la verdadera diferencia para los instaladores e interioristas.").font.size = Pt(10.5)

p_i3 = doc.add_paragraph()
p_i3.paragraph_format.space_after = Pt(12)
p_i3.add_run("En ENCORE hemos desarrollado nuestra Plataforma de Carril Magnético 48V desde una perspectiva puramente técnica y de ingeniería:").font.size = Pt(10.5)

# 4. Sección 1
p_h1 = doc.add_paragraph()
p_h1.paragraph_format.space_before = Pt(8)
p_h1.paragraph_format.space_after = Pt(4)
r_h1 = p_h1.add_run("1. Flexibilidad Arquitectónica y Modularidad Total")
r_h1.bold = True
r_h1.font.size = Pt(11)
r_h1.font.color.rgb = RGBColor(26, 54, 93)

p_b1_1 = doc.add_paragraph(style='List Bullet')
p_b1_1.paragraph_format.space_after = Pt(3)
p_b1_1.add_run("Perfiles de 20 mm, 10 mm y micro-carril: versiones empotradas (trimless), de superficie y suspendidas.").font.size = Pt(10)

p_b1_2 = doc.add_paragraph(style='List Bullet')
p_b1_2.paragraph_format.space_after = Pt(10)
p_b1_2.add_run("Módulos intercambiables al instante: focos orientables con ópticas de corte preciso, bañadores lineales de pared, micro-rejillas antideslumbramiento (UGR < 10) y módulos decorativos colgantes.").font.size = Pt(10)

# Imagen 1
m_dir = r"D:\marketing\assets\products\MAGNETIC"
imgs = [os.path.join(m_dir, f) for f in os.listdir(m_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if len(imgs) > 0:
    p_img1 = doc.add_paragraph()
    p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img1.paragraph_format.space_after = Pt(12)
    p_img1.add_run().add_picture(imgs[0], width=Inches(5.2))

# 5. Sección 2
p_h2 = doc.add_paragraph()
p_h2.paragraph_format.space_before = Pt(8)
p_h2.paragraph_format.space_after = Pt(4)
r_h2 = p_h2.add_run("2. Ingeniería Diseñada para Cero Incidencias en Obra")
r_h2.bold = True
r_h2.font.size = Pt(11)
r_h2.font.color.rgb = RGBColor(26, 54, 93)

p_b2_1 = doc.add_paragraph(style='List Bullet')
p_b2_1.paragraph_format.space_after = Pt(3)
p_b2_1.add_run("Conductores de cobre puro de alta sección con mayor superficie de contacto para una conductividad impecable sin caídas de tensión.").font.size = Pt(10)

p_b2_2 = doc.add_paragraph(style='List Bullet')
p_b2_2.paragraph_format.space_after = Pt(3)
p_b2_2.add_run("Perfil de aluminio extruido reforzado de 3 mm para una estabilidad perfecta sin torsión.").font.size = Pt(10)

p_b2_3 = doc.add_paragraph(style='List Bullet')
p_b2_3.paragraph_format.space_after = Pt(3)
p_b2_3.add_run("Doble fijación de seguridad: anclaje magnético asistido por bloqueo mecánico de liberación rápida, garantizando total seguridad sin vibraciones.").font.size = Pt(10)

p_b2_4 = doc.add_paragraph(style='List Bullet')
p_b2_4.paragraph_format.space_after = Pt(10)
p_b2_4.add_run("Conexión sin polaridad para agilizar el montaje y eliminar errores de instalación.").font.size = Pt(10)

# Imagen 2
if len(imgs) > 1:
    p_img2 = doc.add_paragraph()
    p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img2.paragraph_format.space_after = Pt(12)
    p_img2.add_run().add_picture(imgs[1], width=Inches(5.2))

# 6. Sección 3
p_h3 = doc.add_paragraph()
p_h3.paragraph_format.space_before = Pt(8)
p_h3.paragraph_format.space_after = Pt(4)
r_h3 = p_h3.add_run("3. Máxima Calidad Óptica y Certificación Europea")
r_h3.bold = True
r_h3.font.size = Pt(11)
r_h3.font.color.rgb = RGBColor(26, 54, 93)

p_b3_1 = doc.add_paragraph(style='List Bullet')
p_b3_1.paragraph_format.space_after = Pt(3)
p_b3_1.add_run("Motores LED Bridgelux / Citizen COB con CRI 95+ (R9 > 80) y SDCM < 3 para una fidelidad cromática absoluta.").font.size = Pt(10)

p_b3_2 = doc.add_paragraph(style='List Bullet')
p_b3_2.paragraph_format.space_after = Pt(3)
p_b3_2.add_run("Control DALI-2, 0-10V y sistemas inalámbricos Casambi.").font.size = Pt(10)

p_b3_3 = doc.add_paragraph(style='List Bullet')
p_b3_3.paragraph_format.space_after = Pt(10)
p_b3_3.add_run("Certificados CE y RoHS disponibles, con entrega directa de muestras a vuestro showroom en menos de 2 semanas.").font.size = Pt(10)

# Imagen 3
if len(imgs) > 2:
    p_img3 = doc.add_paragraph()
    p_img3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img3.paragraph_format.space_after = Pt(12)
    p_img3.add_run().add_picture(imgs[2], width=Inches(5.2))

# 7. Cierre & CTA
p_c1 = doc.add_paragraph()
p_c1.paragraph_format.space_after = Pt(8)
p_c1.add_run("Si estáis valorando ampliar vuestra propuesta de carril magnético con una línea arquitectónica de ingeniería superior y precio directo de fábrica, nos encantaría enviaros una muestra física de prueba o un catálogo técnico completo a vuestras instalaciones de Cornellà.").font.size = Pt(10.5)

p_c2 = doc.add_paragraph()
p_c2.paragraph_format.space_after = Pt(16)
r_c2 = p_c2.add_run("¿Tendría sentido coordinar el envío de un maletín de muestras para vuestro departamento técnico o de compras?")
r_c2.bold = True
r_c2.font.size = Pt(10.5)

# 8. Firma
p_sign = doc.add_paragraph()
p_sign.add_run("Un cordial saludo,\n\n[Tu Nombre]\nEncore Commercial Lighting\nWeb: encore-tech.com\nWhatsApp: +86-xxx").font.size = Pt(10)

out_file = r"D:\marketing\开发信Word库_完整版\Encore_Barcelona_LED专属西语开发信(高清图文定稿版).docx"
doc.save(out_file)
print("SUCCESS_ENCODING_FIXED")
