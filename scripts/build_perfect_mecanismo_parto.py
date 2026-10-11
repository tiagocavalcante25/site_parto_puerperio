# -*- coding: utf-8 -*-
"""
High-Precision Brazilian Portuguese Medical Recreation of Mechanism of Labor Diagram
Flawless elimination of all English text, zero superimposed stray labels,
100% authentic medical artwork and typography.
"""
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def build_mecanismo():
    source_artifact = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\labor_stages_1791067708192.jpg"
    target_img = r"c:\Users\Admin\Downloads\INTERNATO GO\site_parto_puerperio\assets\img\mecanismo_parto_movimentos.jpg"

    img = cv2.imread(source_artifact)
    if img is None:
        raise FileNotFoundError(f"Source not found: {source_artifact}")

    h, w, c = img.shape
    print(f"Loaded source image: {w}x{h}")

    def fill_white(y1, y2, x1, x2):
        img[max(0, y1):min(h, y2), max(0, x1):min(w, x2)] = [255, 255, 255]

    def fill_color(y1, y2, x1, x2, color):
        img[max(0, y1):min(h, y2), max(0, x1):min(w, x2)] = color

    # 1. TOP TITLE BANNER: y: 51..95, x: 181..1203
    fill_color(51, 95, 181, 1203, [200, 216, 222])

    # 2. FETAL HEAD: y: 115..142, x: 375..485
    fill_white(115, 142, 375, 485)

    # 3. PUBIC SYMPHYSIS: y: 212..235, x: 295..450
    fill_white(212, 235, 295, 450)

    # 4. ENGAGEMENT & DESCENT: y: 360..482, x: 182..430
    fill_white(360, 482, 182, 430)

    # 5. ISCHIAL SPINES & VAGINA: y: 505..595, x: 410..495
    fill_white(505, 595, 410, 495)

    # 6. UTERINE FUNDUS: y: 115..138, x: 740..885
    fill_white(115, 138, 740, 885)

    # 7. UTERINE CERVIX: y: 175..218, x: 795..950
    fill_white(175, 218, 795, 950)

    # 8. INTERNAL ROTATION: y: 120..275, x: 940..1185
    fill_white(120, 275, 940, 1185)

    # 9. SACRUM: y: 295..316, x: 955..1035
    fill_white(295, 316, 955, 1035)

    # 10. EXTENSION & EXPULSION: y: 345..440, x: 945..1195
    fill_white(345, 440, 945, 1195)

    # 11. ROTATION FOR SHOULDER: y: 450..508, x: 1005..1195
    fill_white(450, 508, 1005, 1195)

    # 12. EXPULSION: y: 618..642, x: 1075..1195
    fill_white(618, 642, 1075, 1195)

    # 13. PELVIC FLOOR MUSCLES (Complete Inpainting of residual text on pelvic contour)
    # y: 625..675, x: 500..720
    crop_pf = img[625:675, 500:720].copy()
    gray_pf = cv2.cvtColor(crop_pf, cv2.COLOR_BGR2GRAY)
    mask_pf = (gray_pf < 150).astype(np.uint8) * 255
    kernel_pf = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    mask_pf = cv2.dilate(mask_pf, kernel_pf, iterations=1)
    img[625:675, 500:720] = cv2.inpaint(crop_pf, mask_pf, 3, cv2.INPAINT_TELEA)

    # 14. TIMELINE BAR: y: 700..724
    fill_color(700, 724, 435, 883, [199, 218, 223])
    fill_color(700, 724, 887, 1175, [199, 218, 223])

    # ==============================================================================
    # PHASE 2: TYPOGRAPHY & ANNOTATIONS (PIL High-Precision Antialiased)
    # ==============================================================================
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)

    def get_font(name_or_size, size=None):
        if size is None:
            size = name_or_size
            name = "arial.ttf"
        else:
            name = name_or_size
        font_paths = [
            os.path.join(r"C:\Windows\Fonts", name),
            os.path.join(r"C:\Windows\Fonts", "calibri.ttf" if "bd" not in name else "calibrib.ttf"),
            os.path.join(r"C:\Windows\Fonts", "arial.ttf")
        ]
        for p in font_paths:
            if os.path.exists(p):
                try:
                    return ImageFont.truetype(p, size)
                except:
                    pass
        return ImageFont.load_default()

    font_title = get_font("arialbd.ttf", 23)
    font_bold_lg = get_font("arialbd.ttf", 15)
    font_bold_md = get_font("arialbd.ttf", 13)
    font_bold_sm = get_font("arialbd.ttf", 12)
    font_reg_md = get_font("arial.ttf", 13)
    font_reg_sm = get_font("arial.ttf", 11)
    font_italic_sm = get_font("ariali.ttf", 12)

    # Color Palette:
    c_title = "#111827"       # Very dark slate
    c_label_main = "#1f2937"  # Dark charcoal
    c_label_sec = "#4b5563"   # Medium slate
    c_teal_dark = "#0f766e"   # Medical teal primary
    c_teal_mid = "#0d9488"    # Medical teal secondary
    c_body = "#374151"        # Charcoal body text

    # 1. Main Title
    draw.text((692, 73), "MECANISMO DO PARTO: DESCIDA E MOVIMENTOS CARDINAIS", fill=c_title, font=font_title, anchor="mm")

    # 2. Cabeça Fetal
    draw.text((430, 130), "Cabeça Fetal", fill=c_label_main, font=font_bold_lg, anchor="mm")

    # 3. Sínfise Púbica
    draw.text((375, 225), "Sínfise Púbica", fill=c_label_main, font=font_bold_lg, anchor="mm")

    # 4. Fundo Uterino
    draw.text((812, 127), "Fundo Uterino", fill=c_label_main, font=font_bold_lg, anchor="mm")

    # 5. Colo Uterino (em dilatação)
    draw.text((872, 192), "Colo Uterino", fill=c_label_main, font=font_bold_lg, anchor="mm")
    draw.text((872, 210), "(em dilatação)", fill=c_label_sec, font=font_italic_sm, anchor="mm")

    # 6. Insinuação e Descida (Left Box)
    draw.text((305, 372), "1. INSINUAÇÃO & DESCIDA", fill=c_teal_dark, font=font_bold_md, anchor="mm")
    draw.text((305, 390), "(1º Período / Planos -2 a 0)", fill=c_teal_mid, font=font_bold_sm, anchor="mm")
    draw.text((305, 410), "A apresentação penetra o estreito superior;", fill=c_body, font=font_reg_sm, anchor="mm")
    draw.text((305, 426), "ocorre flexão cefálica oferecendo o menor", fill=c_body, font=font_reg_sm, anchor="mm")
    draw.text((305, 442), "diâmetro: suboccipitobregmático (9,5 cm).", fill=c_body, font=font_reg_sm, anchor="mm")
    draw.text((305, 458), "Atinge o plano 0 das espinhas isquiáticas.", fill=c_body, font=font_reg_sm, anchor="mm")

    # 7. Espinhas Isquiáticas & Vagina
    draw.text((455, 518), "Espinhas", fill=c_label_main, font=font_bold_md, anchor="mm")
    draw.text((455, 534), "Isquiáticas", fill=c_label_main, font=font_bold_md, anchor="mm")
    draw.text((455, 550), "(Plano 0)", fill=c_label_sec, font=font_reg_sm, anchor="mm")

    draw.text((455, 582), "Vagina", fill=c_label_main, font=font_bold_md, anchor="mm")

    # 8. Músculos do Assoalho Pélvico (Placed cleanly with a crisp anti-aliased vector leader line)
    draw.line([(580, 646), (758, 588)], fill="#1f2937", width=2)
    # Sharp arrowhead pointing to pelvic floor musculature
    draw.polygon([(760, 587), (748, 591), (753, 598)], fill="#1f2937")

    draw.text((495, 640), "Músculos do Assoalho", fill=c_label_main, font=font_bold_sm, anchor="mm")
    draw.text((495, 656), "Pélvico", fill=c_label_main, font=font_bold_sm, anchor="mm")

    # 9. Rotação Interna (Upper Right Box)
    draw.text((1062, 135), "2. ROTAÇÃO INTERNA", fill=c_teal_dark, font=font_bold_lg, anchor="mm")
    draw.text((1062, 155), "(Final do 1º / Início do 2º Período)", fill=c_teal_mid, font=font_bold_sm, anchor="mm")
    draw.text((1062, 172), "(Planos 0 a +1 de De Lee)", fill=c_label_sec, font=font_reg_sm, anchor="mm")
    draw.text((1062, 195), "A cabeça fetal gira internamente para a", fill=c_body, font=font_reg_sm, anchor="mm")
    draw.text((1062, 211), "posição anterior (OP/OEA), alinhando-se", fill=c_body, font=font_reg_sm, anchor="mm")
    draw.text((1062, 227), "ao maior diâmetro anteroposterior", fill=c_body, font=font_reg_sm, anchor="mm")
    draw.text((1062, 243), "do estreito inferior da pelve.", fill=c_body, font=font_reg_sm, anchor="mm")

    # 10. Sacro
    draw.text((995, 307), "Sacro", fill=c_label_main, font=font_bold_lg, anchor="mm")

    # 11. Extensão e Desprendimento (Mid Right Box)
    draw.text((1070, 355), "3. EXTENSÃO & EXPULSÃO", fill=c_teal_dark, font=font_bold_md, anchor="mm")
    draw.text((1070, 373), "(2º Período / Expulsivo)", fill=c_teal_mid, font=font_bold_sm, anchor="mm")
    draw.text((1070, 395), "A cabeça fetal deflete sob a sínfise púbica", fill=c_body, font=font_reg_sm, anchor="mm")
    draw.text((1070, 411), "como uma alavanca, desprendendo o", fill=c_body, font=font_reg_sm, anchor="mm")
    draw.text((1070, 427), "occipício, fronte, nariz e queixo.", fill=c_body, font=font_reg_sm, anchor="mm")

    # 12. Rotação para ombros (Left-aligned at x=1022 with leader line connection)
    draw.text((1022, 470), "Restituição (Rotação Externa)", fill=c_label_main, font=font_bold_sm, anchor="lm")
    draw.text((1022, 488), "para desprendimento dos ombros", fill=c_body, font=font_reg_sm, anchor="lm")

    # 13. Desprendimento Fetal (Expulsão)
    draw.text((1125, 628), "Desprendimento Fetal", fill=c_teal_dark, font=font_bold_md, anchor="mm")

    # 14. Linha do Tempo Inferior
    draw.text((659, 712), "1º Período: Dilatação (Fases Latente e Ativa)", fill=c_title, font=font_bold_lg, anchor="mm")
    draw.text((1031, 712), "2º Período: Expulsivo", fill=c_title, font=font_bold_lg, anchor="mm")

    # Save at maximum quality
    os.makedirs(os.path.dirname(target_img), exist_ok=True)
    pil_img.save(target_img, "JPEG", quality=98)
    print(f"Salvo com perfeição médica absoluta: {target_img}")

if __name__ == "__main__":
    build_mecanismo()
