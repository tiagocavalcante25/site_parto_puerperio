# -*- coding: utf-8 -*-
"""
High-Precision Brazilian Portuguese Medical Recreation of Shoulder Dystocia & McRoberts Diagram
- 100% eradication of English text
- Surgical glyph-level inpainting with Telea algorithm (zero block smudges, zero ghosting)
- Preservation of all original anatomical textures, arrows, and leader lines
- Professional Brazilian medical typography (ACOG / FEBRASGO / USMLE Step 2 & 3)
"""
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def build_distocia():
    source_artifact = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\shoulder_dystocia_1791067730155.jpg"
    target_img = r"c:\Users\Admin\Downloads\INTERNATO GO\site_parto_puerperio\assets\img\distocia_ombros_mcroberts.jpg"

    img = cv2.imread(source_artifact)
    if img is None:
        raise FileNotFoundError(f"Source not found: {source_artifact}")

    h, w, c = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 1. Create surgical mask for English text glyphs
    mask = np.zeros((h, w), dtype=np.uint8)

    # (y1, y2, x1, x2)
    # 1. Pubic Symphysis: text is y: 140..165, x: 170..432 (leader line at x=433, y=152)
    mask[140:165, 170:432] = (gray[140:165, 170:432] < 205).astype(np.uint8) * 255

    # 2. Impacted Anterior Shoulder: text is y: 238..308, x: 135..238 (leader line at x=239, y=272)
    mask[238:308, 135:238] = (gray[238:308, 135:238] < 205).astype(np.uint8) * 255

    # 3. Suprapubic Pressure Applied: text is y: 133..222, x: 742..942 (arrow is at x <= 738)
    mask[133:222, 742:942] = (gray[133:222, 742:942] < 205).astype(np.uint8) * 255

    # 4. McRoberts Maneuver: text is y: 324..400, x: 1102..1225 (leader lines at x <= 1098)
    mask[324:400, 1102:1225] = (gray[324:400, 1102:1225] < 205).astype(np.uint8) * 255

    # 5. Fetal Head (Emerged): text is y: 550..610, x: 810..978 (leader line at x=808)
    mask[550:610, 810:978] = (gray[550:610, 810:978] < 205).astype(np.uint8) * 255

    # 6. Maternal Sacrum: text is y: 630..654, x: 140..315 (leader line at x=316)
    mask[630:654, 140:315] = (gray[630:654, 140:315] < 205).astype(np.uint8) * 255

    # 7. Pelvic Inlet: text is y: 688..712, x: 230..355 (leader line at x=356)
    mask[688:712, 230:355] = (gray[688:712, 230:355] < 205).astype(np.uint8) * 255

    # Dilate mask by 2 pixels to cleanly capture anti-aliasing text borders
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Inpaint seamlessly with Telea
    clean_img = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

    # 2. Institutional Top Header Bar (Deep Medical Teal #0f766e)
    # y: 0 to 76
    cv2.rectangle(clean_img, (0, 0), (w, 76), (110, 118, 15), -1) # BGR (110, 118, 15)

    pil_img = Image.fromarray(cv2.cvtColor(clean_img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)

    def get_font(font_name, size):
        p = os.path.join(r"C:\Windows\Fonts", font_name)
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except:
                pass
        return ImageFont.load_default()

    f_title = get_font("segoeuib.ttf", 20)
    f_sub = get_font("segoeuib.ttf", 11)
    f_bold_lg = get_font("segoeuib.ttf", 14)
    f_bold_md = get_font("segoeuib.ttf", 12)
    f_bold_sm = get_font("segoeuib.ttf", 10)
    f_reg_md = get_font("segoeui.ttf", 11)
    f_reg_sm = get_font("segoeui.ttf", 10)
    f_italic = get_font("segoeuii.ttf", 10)

    # Top Institutional Banner
    draw.text((w / 2, 28), "EMERGÊNCIA OBSTÉTRICA: DISTÓCIA DE OMBROS & MANOBRA DE McROBERTS", fill="#ffffff", font=f_title, anchor="mm")
    draw.text((w / 2, 54), "DESIMPACTAÇÃO DO OMBRO ANTERIOR SOB A SÍNFISE PÚBICA • MANOBRA DE RUBIN I (PRESSÃO SUPRAPÚBICA)", fill="#ccfbf1", font=f_sub, anchor="mm")

    # 1. Sínfise Púbica Materna (Top Left, Right-aligned to connect with leader line at x=432, y=152)
    draw.text((430, 144), "Sínfise Púbica Materna", fill="#1e293b", font=f_bold_lg, anchor="rm")
    draw.text((430, 161), "(Osso Púbico Materno)", fill="#64748b", font=f_reg_sm, anchor="rm")

    # 2. Ombro Anterior Impactado (Mid Left, Right-aligned to leader line at x=235, y=272)
    draw.text((235, 245), "Ombro Anterior Impactado", fill="#dc2626", font=f_bold_md, anchor="rm")
    draw.text((235, 262), "(Retido atrás da sínfise púbica)", fill="#991b1b", font=f_bold_sm, anchor="rm")
    draw.text((235, 279), "Sinal da Tartaruga (Turtle Sign)", fill="#4b5563", font=f_italic, anchor="rm")
    draw.text((235, 295), "Retração da cabeça fetal contra o períneo", fill="#64748b", font=f_reg_sm, anchor="rm")

    # 3. Pressão Suprapúbica / Rubin I (Top Center, Left-aligned next to arrow at x=750)
    draw.text((750, 138), "Pressão Suprapúbica (Rubin I)", fill="#0f766e", font=f_bold_md, anchor="lm")
    draw.text((750, 154), "Aplicada em sentido oblíquo/lateral", fill="#1e293b", font=f_reg_md, anchor="lm")
    draw.text((750, 170), "para desimpactar e aduzir o ombro anterior.", fill="#1e293b", font=f_reg_md, anchor="lm")
    draw.text((750, 188), "CONTRAINDICAÇÃO: Nunca realizar Kristeller!", fill="#dc2626", font=f_bold_sm, anchor="lm")
    draw.text((750, 204), "(Pressão fúndica agrava impacção e rotura uterina)", fill="#991b1b", font=f_reg_sm, anchor="lm")

    # 4. Manobra de McRoberts (Right Mid, Left-aligned next to leader lines at x=1105)
    draw.text((1105, 335), "Manobra de McRoberts", fill="#0f766e", font=f_bold_lg, anchor="lm")
    draw.text((1105, 355), "Hiperflexão e abdução das coxas", fill="#1e293b", font=f_bold_md, anchor="lm")
    draw.text((1105, 372), "maternas em direção ao abdome.", fill="#374151", font=f_reg_md, anchor="lm")
    draw.text((1105, 389), "Retifica a curvatura lombossacral", fill="#374151", font=f_reg_md, anchor="lm")
    draw.text((1105, 406), "e amplia o diâmetro conjugado obstétrico.", fill="#374151", font=f_reg_md, anchor="lm")

    # 5. Cabeça Fetal Desprendida (Lower Center-Right, Left-aligned at x=815)
    draw.text((815, 558), "Cabeça Fetal Desprendida", fill="#1e293b", font=f_bold_md, anchor="lm")
    draw.text((815, 574), "(Emerge e retrai contra o períneo)", fill="#4b5563", font=f_italic, anchor="lm")
    draw.text((815, 591), "ALERTA: Evitar tração cefálica excessiva!", fill="#dc2626", font=f_bold_sm, anchor="lm")
    draw.text((815, 607), "(Prevenção de lesão do plexo braquial / Erb-Duchenne)", fill="#991b1b", font=f_reg_sm, anchor="lm")

    # 6. Sacro Materno (Lower Left, Right-aligned to leader line at x=310)
    draw.text((310, 638), "Sacro Materno", fill="#1e293b", font=f_bold_md, anchor="rm")
    draw.text((310, 654), "(Promontório sacral)", fill="#64748b", font=f_reg_sm, anchor="rm")

    # 7. Estreito Superior da Pelve (Bottom Left, Right-aligned to leader line at x=345)
    draw.text((345, 692), "Estreito Superior da Pelve", fill="#1e293b", font=f_bold_md, anchor="rm")
    draw.text((345, 708), "(Plano de entrada pélvico)", fill="#64748b", font=f_reg_sm, anchor="rm")

    # Save final publication-ready image
    os.makedirs(os.path.dirname(target_img), exist_ok=True)
    pil_img.save(target_img, "JPEG", quality=98)
    print(f"Sucesso absoluto: {target_img}")

if __name__ == "__main__":
    build_distocia()
