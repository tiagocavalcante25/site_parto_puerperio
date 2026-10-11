"""
build_amamentacao_final.py
Generates the 100% Portuguese, zero-English medical infographic for:
'Anatomia Materna, Neuroendocrinologia da Lactação e Técnica da Pega Correta'
Strictly adhering to Ministério da Saúde / SUS, SBP, FEBRASGO, and IHAC guidelines.
"""

import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SRC_PATH = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\breastfeeding_latch_1791067780197.jpg"
SITE_TARGET = r"c:\Users\Admin\Downloads\INTERNATO GO\site_parto_puerperio\assets\img\amamentacao_neuroendocrinologia_pega.jpg"
ARTIFACT_TARGET = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\amamentacao_neuroendocrinologia_pega_pt.jpg"

def get_fonts():
    font_bold_path = "C:/Windows/Fonts/segoeuib.ttf"
    font_reg_path = "C:/Windows/Fonts/segoeui.ttf"
    if not os.path.exists(font_bold_path):
        font_bold_path = "C:/Windows/Fonts/arialbd.ttf"
        font_reg_path = "C:/Windows/Fonts/arial.ttf"
        
    return {
        "title": ImageFont.truetype(font_bold_path, 23),
        "subtitle": ImageFont.truetype(font_reg_path, 12),
        "badge_title": ImageFont.truetype(font_bold_path, 12),
        "badge_sub": ImageFont.truetype(font_reg_path, 10),
        "section_title": ImageFont.truetype(font_bold_path, 13),
        "section_sub": ImageFont.truetype(font_reg_path, 10),
        "card_header": ImageFont.truetype(font_bold_path, 11),
        "card_title": ImageFont.truetype(font_bold_path, 11),
        "label_title": ImageFont.truetype(font_bold_path, 11),
        "label_body": ImageFont.truetype(font_reg_path, 9),
        "pill_num": ImageFont.truetype(font_bold_path, 11),
        "pill_title": ImageFont.truetype(font_bold_path, 11),
        "pill_desc": ImageFont.truetype(font_reg_path, 9),
        "chart_title": ImageFont.truetype(font_bold_path, 10),
        "chart_label": ImageFont.truetype(font_reg_path, 9),
        "inset_header": ImageFont.truetype(font_bold_path, 10),
        "inset_body": ImageFont.truetype(font_reg_path, 9),
    }

def main():
    print("Reading pristine source...")
    orig = cv2.imread(SRC_PATH)
    h, w = orig.shape[:2]
    gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)

    base = orig.copy()

    # 1. Clear top header area completely (y: 0 to 140) to guarantee zero old title remnants
    base[0:140, :] = 255

    # 2. Extract pristine crops of the Alveolus and Lobule BEFORE clearing center
    alv_crop = orig[160:315, 415:550].copy()
    lob_crop = orig[460:655, 410:615].copy()

    # Inpaint alveolus text
    alv_gray = cv2.cvtColor(alv_crop, cv2.COLOR_BGR2GRAY)
    alv_mask = np.zeros(alv_crop.shape[:2], dtype=np.uint8)
    for (ax1, ay1, ax2, ay2) in [
        (0, 0, 65, 45),
        (65, 0, alv_crop.shape[1], 45),
        (105, 45, alv_crop.shape[1], 140),
        (30, 130, 110, alv_crop.shape[0])
    ]:
        sub = alv_gray[ay1:ay2, ax1:ax2]
        dark = (sub < 140).astype(np.uint8) * 255
        dark = cv2.dilate(dark, np.ones((3,3), np.uint8), iterations=2)
        alv_mask[ay1:ay2, ax1:ax2] = dark
    alv_cleaned = cv2.inpaint(alv_crop, alv_mask, 3, cv2.INPAINT_TELEA)

    # Inpaint lobule text
    lob_gray = cv2.cvtColor(lob_crop, cv2.COLOR_BGR2GRAY)
    lob_mask = np.zeros(lob_crop.shape[:2], dtype=np.uint8)
    for (lx1, ly1, lx2, ly2) in [
        (0, 0, 60, 45),
        (125, 0, lob_crop.shape[1], 80),
        (135, 160, lob_crop.shape[1], lob_crop.shape[0]),
    ]:
        sub = lob_gray[ly1:ly2, lx1:lx2]
        dark = (sub < 140).astype(np.uint8) * 255
        dark = cv2.dilate(dark, np.ones((3,3), np.uint8), iterations=2)
        lob_mask[ly1:ly2, lx1:lx2] = dark
    lob_cleaned = cv2.inpaint(lob_crop, lob_mask, 3, cv2.INPAINT_TELEA)

    # Clean white background around the lobule edges
    lob_cleaned[0:45, 0:60] = 255
    lob_cleaned[0:75, 125:] = 255
    lob_cleaned[160:, 135:] = 255

    # 3. Build precision inpainting mask for all text and pointers in base image
    mask = np.zeros((h, w), dtype=np.uint8)

    text_boxes = [
        # Left breast text & lines outside breast:
        (100, 130, 380, 210),   # upper adipose & line
        (210, 200, 390, 270),   # mammary glands
        (240, 260, 390, 330),   # lobules
        (270, 570, 410, 680),   # ductal system
        (220, 670, 400, 750),   # lower mammary glands
        (100, 680, 320, 765),   # lower adipose tissue
        # Mother's breast on the right (x: 750..1020):
        (800, 320, 940, 380),   # Upper and lower lips or flanged
        (815, 420, 940, 490),   # Deep asymmetric latch
        (850, 550, 950, 585),   # Lower lips
        (860, 180, 1020, 245),  # Nose are not obstructed
        (955, 230, 1005, 305),  # nose pointer line
        (1030, 335, 1205, 375), # Baby cheek (Nose or normucla)
        (980, 355, 1040, 395),  # pointer line on upper lip/cheek
        (920, 620, 1080, 690),  # Chin resting firmly
        (960, 580, 1030, 640),  # chin pointer line
        # Pointers and areola arc on breast:
        (890, 230, 1000, 370),  # upper lip line
        (890, 365, 1030, 535),  # areola arc
        (890, 500, 1000, 580),  # lower lip line
        # Inpaint old angle arrow and text to place unified badge:
        (1030, 380, 1120, 485),
    ]

    for (x1, y1, x2, y2) in text_boxes:
        sub_gray = gray[y1:y2, x1:x2]
        dark = (sub_gray < 145).astype(np.uint8) * 255
        dark = cv2.dilate(dark, np.ones((3,3), np.uint8), iterations=2)
        mask[y1:y2, x1:x2] = np.maximum(mask[y1:y2, x1:x2], dark)

    print("Inpainting text and pointer lines...")
    cleaned = cv2.inpaint(base, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

    # Wipe the center column to pure white
    cleaned[90:768, 395:705] = 255
    # Also wipe the vertical divider line remnant at x=704
    cleaned[0:768, 703:706] = 255

    # Convert to PIL Image for rendering typography and graphics
    img_rgb = cv2.cvtColor(cleaned, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_rgb)
    draw = ImageDraw.Draw(pil_img)
    fonts = get_fonts()

    # =========================================================================
    # 4. TOP HEADER BAR (Navy #0f172a + Orange line #d97706)
    # =========================================================================
    draw.rectangle([(0, 0), (w, 86)], fill=(15, 23, 42))
    draw.rectangle([(0, 86), (w, 90)], fill=(217, 119, 6))

    # Main Title & Subtitle
    draw.text((25, 16), "ANATOMIA MAMÁRIA, NEUROENDOCRINOLOGIA & TÉCNICA DA PEGA CORRETA", 
              fill=(255, 255, 255), font=fonts["title"])
    draw.text((25, 52), "Lactação Humana Fisiológica • Reflexos de Prolactina e Ocitocina • Critérios Clínicos de Pega e Amamentação Eficaz", 
              fill=(203, 213, 225), font=fonts["subtitle"])

    # SUS / MS Badge (Top Right)
    badge_x1, badge_y1, badge_x2, badge_y2 = w - 345, 12, w - 25, 74
    draw.rounded_rectangle([(badge_x1, badge_y1), (badge_x2, badge_y2)], radius=8, 
                           fill=(30, 41, 59), outline=(56, 189, 248), width=1)
    draw.text((badge_x1 + 18, badge_y1 + 12), "MINISTÉRIO DA SAÚDE / SUS", 
              fill=(56, 189, 248), font=fonts["badge_title"])
    draw.text((badge_x1 + 18, badge_y1 + 34), "Diretrizes FEBRASGO • SBP • IHAC", 
              fill=(226, 232, 240), font=fonts["badge_sub"])

    # =========================================================================
    # 5. SECTION HEADERS BELOW HEADER BAR
    # =========================================================================
    # Left Section Header
    draw.text((25, 100), "ANATOMIA DA MAMA & CONTROLE NEUROENDÓCRINO", 
              fill=(15, 23, 42), font=fonts["section_title"])
    draw.text((25, 120), "Parênquima mamário e eixos hipofisários da produção (Prolactina) e ejeção (Ocitocina)", 
              fill=(100, 116, 139), font=fonts["section_sub"])

    # Right Section Header
    draw.text((715, 100), "CRITÉRIOS CLÍNICOS DA PEGA ADEQUADA (SBP / IHAC / OMS)", 
              fill=(15, 23, 42), font=fonts["section_title"])
    draw.text((715, 120), "Semiologia da mamada eficaz: prevenção de dor, fissuras e garantia de transferência láctea", 
              fill=(100, 116, 139), font=fonts["section_sub"])

    # Vertical subtle divider between columns
    draw.line([(395, 105), (395, 755)], fill=(226, 232, 240), width=1)
    draw.line([(705, 105), (705, 755)], fill=(226, 232, 240), width=1)

    # =========================================================================
    # 6. LEFT BREAST LABELS & POINTERS (Clean pointers from left edge bx1)
    # =========================================================================
    def draw_breast_label(box_coords, title, subtitle, target_point):
        bx1, by1, bx2, by2 = box_coords
        draw.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=5, 
                               fill=(255, 255, 255), outline=(203, 213, 225), width=1)
        draw.text((bx1 + 8, by1 + 4), title, fill=(15, 23, 42), font=fonts["label_title"])
        draw.text((bx1 + 8, by1 + 19), subtitle, fill=(100, 116, 139), font=fonts["label_body"])
        
        # Pointer line starts at left edge bx1
        tx, ty = target_point
        px = bx1
        py = (by1 + by2) // 2
        draw.line([(px, py), (tx, ty)], fill=(71, 85, 105), width=1)
        draw.ellipse([(tx - 2, ty - 2), (tx + 2, ty + 2)], fill=(15, 23, 42))

    # Muscle label (on chest wall, left)
    draw.rounded_rectangle([(12, 600), (145, 642)], radius=5, fill=(255, 255, 255), outline=(203, 213, 225), width=1)
    draw.text((18, 605), "Músculo Peitoral", fill=(15, 23, 42), font=fonts["label_title"])
    draw.text((18, 620), "Parede torácica posterior", fill=(100, 116, 139), font=fonts["label_body"])
    draw.line([(85, 600), (80, 560)], fill=(71, 85, 105), width=1)
    draw.ellipse([(78, 558), (82, 562)], fill=(15, 23, 42))

    # Adipose tissue upper
    draw_breast_label((190, 150, 365, 190), "Tecido Adiposo Subcutâneo", "Gordura pré-mamária de proteção", (125, 150))

    # Mammary gland (lobes)
    draw_breast_label((215, 225, 385, 265), "Glândula Mamária (Lobos)", "15 a 20 lobos por mama", (170, 245))

    # Lobules & Acini
    draw_breast_label((225, 310, 385, 350), "Lóbulos e Ácinos", "Unidade secretora de leite", (200, 340))

    # Ducts & Lactiferous Sinuses
    draw_breast_label((235, 480, 390, 520), "Ductos Lactíferos", "Condução em direção à papila", (365, 448))

    # Mammary gland lower
    draw_breast_label((215, 615, 385, 655), "Parênquima Glandular", "Ductos e estroma intralobular", (245, 600))

    # Retromammary fat
    draw_breast_label((145, 695, 335, 735), "Gordura Retromamária", "Espaço retromamário e fáscia", (135, 665))

    # =========================================================================
    # 7. CENTER COLUMN: CARDS FOR PROLACTIN & OXYTOCIN
    # =========================================================================
    # --- CARD 1: PROLACTINA (y: 140 to 440) ---
    c1_x1, c1_y1, c1_x2, c1_y2 = 405, 140, 695, 440
    draw.rounded_rectangle([(c1_x1, c1_y1), (c1_x2, c1_y2)], radius=8, 
                           fill=(255, 255, 255), outline=(186, 230, 253), width=1)
    
    # Header ribbon (Cyan)
    draw.rounded_rectangle([(c1_x1, c1_y1), (c1_x2, c1_y1 + 26)], radius=8, fill=(2, 132, 199))
    draw.rectangle([(c1_x1, c1_y1 + 18), (c1_x2, c1_y1 + 26)], fill=(2, 132, 199))
    draw.text((c1_x1 + 12, c1_y1 + 6), "PROLACTINA (ADENO-HIPÓFISE) • SÍNTESE DO LEITE", 
              fill=(255, 255, 255), font=fonts["card_header"])

    # Subtitle
    draw.text((c1_x1 + 10, c1_y1 + 32), "Produção Contínua nos Ácinos Mamários", 
              fill=(15, 23, 42), font=fonts["card_title"])

    # Paste Alveolus Drawing
    alv_pil = Image.fromarray(cv2.cvtColor(alv_cleaned, cv2.COLOR_BGR2RGB))
    alv_pil = alv_pil.resize((125, 143), Image.LANCZOS)
    pil_img.paste(alv_pil, (c1_x1 + 8, c1_y1 + 52))

    # Alveolus annotations on the right of drawing
    alv_text_x = c1_x1 + 138
    draw.text((alv_text_x, c1_y1 + 55), "Hormônio Prolactina:", fill=(2, 132, 199), font=fonts["pill_num"])
    draw.text((alv_text_x, c1_y1 + 69), "Circulação basal e pós-sucção", fill=(71, 85, 105), font=fonts["chart_label"])

    draw.text((alv_text_x, c1_y1 + 88), "Receptores Alveolares:", fill=(15, 23, 42), font=fonts["pill_num"])
    draw.text((alv_text_x, c1_y1 + 102), "Membrana basal epitelial", fill=(71, 85, 105), font=fonts["chart_label"])

    draw.text((alv_text_x, c1_y1 + 121), "Ação Secretora:", fill=(15, 23, 42), font=fonts["pill_num"])
    draw.text((alv_text_x, c1_y1 + 135), "Síntese de caseína e lactose", fill=(71, 85, 105), font=fonts["chart_label"])

    draw.text((alv_text_x, c1_y1 + 154), "Inibição Central:", fill=(225, 29, 72), font=fonts["pill_num"])
    draw.text((alv_text_x, c1_y1 + 168), "Dopamina hipotalâmica (PIF)", fill=(71, 85, 105), font=fonts["chart_label"])

    # Alveolus label below drawing
    draw.text((c1_x1 + 25, c1_y1 + 200), "Ácino / Alvéolo (Luz Alveolar)", fill=(71, 85, 105), font=fonts["chart_label"])

    # Bottom Vector Bar Chart: Prolactin vs Milk Synthesis
    chart_y = c1_y1 + 218
    draw.line([(c1_x1 + 18, chart_y + 60), (c1_x2 - 18, chart_y + 60)], fill=(203, 213, 225), width=1)
    
    # Basal bar
    draw.rectangle([(c1_x1 + 45, chart_y + 35), (c1_x1 + 80, chart_y + 60)], fill=(251, 113, 133))
    draw.text((c1_x1 + 48, chart_y + 64), "Basal", fill=(100, 116, 139), font=fonts["chart_label"])

    # Arrow indicating surge
    draw.line([(c1_x1 + 95, chart_y + 40), (c1_x1 + 130, chart_y + 20)], fill=(2, 132, 199), width=2)
    draw.polygon([(c1_x1 + 133, chart_y + 16), (c1_x1 + 123, chart_y + 20), (c1_x1 + 127, chart_y + 28)], fill=(2, 132, 199))

    # Peak bar
    draw.rectangle([(c1_x1 + 145, chart_y + 12), (c1_x1 + 180, chart_y + 60)], fill=(56, 189, 248))
    draw.text((c1_x1 + 138, chart_y + 64), "Pós-Sucção", fill=(100, 116, 139), font=fonts["chart_label"])

    # Result note on right
    draw.rounded_rectangle([(c1_x1 + 195, chart_y + 14), (c1_x2 - 12, chart_y + 58)], radius=4, 
                           fill=(240, 249, 255), outline=(186, 230, 253), width=1)
    draw.text((c1_x1 + 202, chart_y + 20), "Produção Láctea ↑", fill=(2, 132, 199), font=fonts["pill_title"])
    draw.text((c1_x1 + 202, chart_y + 36), "Garante próxima mamada", fill=(71, 85, 105), font=fonts["chart_label"])


    # --- CARD 2: OCITOCINA (y: 450 to 750) ---
    c2_x1, c2_y1, c2_x2, c2_y2 = 405, 450, 695, 750
    draw.rounded_rectangle([(c2_x1, c2_y1), (c2_x2, c2_y2)], radius=8, 
                           fill=(255, 255, 255), outline=(254, 215, 170), width=1)
    
    # Header ribbon (Orange)
    draw.rounded_rectangle([(c2_x1, c2_y1), (c2_x2, c2_y1 + 26)], radius=8, fill=(234, 88, 12))
    draw.rectangle([(c2_x1, c2_y1 + 18), (c2_x2, c2_y1 + 26)], fill=(234, 88, 12))
    draw.text((c2_x1 + 12, c2_y1 + 6), "OCITOCINA (NEURO-HIPÓFISE) • EJEÇÃO DO LEITE", 
              fill=(255, 255, 255), font=fonts["card_header"])

    # Subtitle
    draw.text((c2_x1 + 10, c2_y1 + 32), "Reflexo Neuroendócrino da Descida (Apojadura)", 
              fill=(15, 23, 42), font=fonts["card_title"])

    # Paste Lobule Drawing
    lob_pil = Image.fromarray(cv2.cvtColor(lob_cleaned, cv2.COLOR_BGR2RGB))
    lob_pil = lob_pil.resize((150, 142), Image.LANCZOS)
    pil_img.paste(lob_pil, (c2_x1 + 8, c2_y1 + 52))

    # Lobule annotations on the right
    lob_text_x = c2_x1 + 162
    draw.text((lob_text_x, c2_y1 + 55), "Ocitocina Plasmática:", fill=(234, 88, 12), font=fonts["pill_num"])
    draw.text((lob_text_x, c2_y1 + 69), "Liberação pulsátil imediata", fill=(71, 85, 105), font=fonts["chart_label"])

    draw.text((lob_text_x, c2_y1 + 88), "Células Mioepiteliais:", fill=(15, 23, 42), font=fonts["pill_num"])
    draw.text((lob_text_x, c2_y1 + 102), "Envolvem alvéolos e ductos", fill=(71, 85, 105), font=fonts["chart_label"])

    draw.text((lob_text_x, c2_y1 + 121), "Contração Ativa:", fill=(15, 23, 42), font=fonts["pill_num"])
    draw.text((lob_text_x, c2_y1 + 135), "Ordenha o leite aos ductos", fill=(71, 85, 105), font=fonts["chart_label"])

    draw.text((lob_text_x, c2_y1 + 154), "Gatilhos Fisiológicos:", fill=(15, 23, 42), font=fonts["pill_num"])
    draw.text((lob_text_x, c2_y1 + 168), "Sucção, choro, pele a pele", fill=(71, 85, 105), font=fonts["chart_label"])

    # Lobule label below drawing
    draw.text((c2_x1 + 20, c2_y1 + 200), "Lóbulo Mamário & Ejeção Ativa", fill=(71, 85, 105), font=fonts["chart_label"])

    # Bottom Vector Bar Chart: Oxytocin vs Milk Ejection
    chart_y2 = c2_y1 + 218
    draw.line([(c2_x1 + 18, chart_y2 + 60), (c2_x2 - 18, chart_y2 + 60)], fill=(203, 213, 225), width=1)
    
    # Basal bar
    draw.rectangle([(c2_x1 + 45, chart_y2 + 38), (c2_x1 + 80, chart_y2 + 60)], fill=(253, 186, 116))
    draw.text((c2_x1 + 45, chart_y2 + 64), "Repouso", fill=(100, 116, 139), font=fonts["chart_label"])

    # Arrow indicating surge
    draw.line([(c2_x1 + 95, chart_y2 + 40), (c2_x1 + 130, chart_y2 + 20)], fill=(234, 88, 12), width=2)
    draw.polygon([(c2_x1 + 133, chart_y2 + 16), (c2_x1 + 123, chart_y2 + 20), (c2_x1 + 127, chart_y2 + 28)], fill=(234, 88, 12))

    # Peak bar
    draw.rectangle([(c2_x1 + 145, chart_y2 + 10), (c2_x1 + 180, chart_y2 + 60)], fill=(249, 115, 22))
    draw.text((c2_x1 + 130, chart_y2 + 64), "Apojadura ↑", fill=(100, 116, 139), font=fonts["chart_label"])

    # Result note on right
    draw.rounded_rectangle([(c2_x1 + 195, chart_y2 + 14), (c2_x2 - 12, chart_y2 + 58)], radius=4, 
                           fill=(255, 247, 237), outline=(254, 215, 170), width=1)
    draw.text((c2_x1 + 202, chart_y2 + 20), "Ejeção Ativa ↑", fill=(234, 88, 12), font=fonts["pill_title"])
    draw.text((c2_x1 + 202, chart_y2 + 36), "Fluxo contínuo ao mamilo", fill=(71, 85, 105), font=fonts["chart_label"])

    # =========================================================================
    # 8. RIGHT COLUMN: 5 SINAIS CARDINAIS DA PEGA CORRETA (SBP / IHAC)
    # =========================================================================
    # Cards sit between x: 715 and x: 935.
    # Targets sit at tx >= 955. Pointer line goes from bx2 (right edge) to target!
    def draw_latch_card(num, title, body_line1, body_line2, box_coords, pointer_to):
        bx1, by1, bx2, by2 = box_coords
        draw.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=6, 
                               fill=(255, 255, 255), outline=(13, 148, 136), width=1)
        
        # Pill badge with number
        draw.rounded_rectangle([(bx1 + 8, by1 + 6), (bx1 + 28, by1 + 24)], radius=4, fill=(13, 148, 136))
        draw.text((bx1 + 14, by1 + 7), str(num), fill=(255, 255, 255), font=fonts["pill_num"])

        # Title
        draw.text((bx1 + 34, by1 + 8), title, fill=(15, 23, 42), font=fonts["pill_title"])

        # Body (2 compact lines)
        draw.text((bx1 + 10, by1 + 27), body_line1, fill=(71, 85, 105), font=fonts["pill_desc"])
        draw.text((bx1 + 10, by1 + 40), body_line2, fill=(100, 116, 139), font=fonts["pill_desc"])

        # Clean pointer line from bx2 (right edge) directly to target point
        tx, ty = pointer_to
        px = bx2
        py = (by1 + by2) // 2
        draw.line([(px, py), (tx, ty)], fill=(13, 148, 136), width=1)
        draw.ellipse([(tx - 2, ty - 2), (tx + 2, ty + 2)], fill=(13, 148, 136))

    # 1. Nariz Livre e Desobstruído
    draw_latch_card(
        1, "Nariz Livre e Desobstruído", 
        "Narinas afastadas do seio materno", 
        "Respiração espontânea, sucção sem pausas", 
        (715, 148, 935, 204), (975, 245)
    )

    # 2. Lábio Superior Evertido
    draw_latch_card(
        2, "Lábio Superior Evertido", 
        "Lábio voltado amplamente para fora", 
        "Sem pregas para dentro ou sucção da pele", 
        (715, 252, 935, 308), (980, 345)
    )

    # 3. Pega Assimétrica Profunda
    draw_latch_card(
        3, "Pega Assimétrica Profunda", 
        "Mais aréola visível ACIMA do que abaixo", 
        "Mamilo direcionado à junção do palato", 
        (715, 356, 935, 412), (955, 435)
    )

    # 4. Lábio Inferior Evertido
    draw_latch_card(
        4, "Lábio Inferior Evertido", 
        "'Boca de peixinho' amplamente aberta", 
        "Língua em concha para ordenha eficaz", 
        (715, 460, 935, 516), (975, 495)
    )

    # 5. Queixo Apoiado na Mama
    draw_latch_card(
        5, "Queixo Tocando a Mama", 
        "Apoiado firmemente contra a mama", 
        "Estabilidade e manutenção do vácuo", 
        (715, 564, 935, 620), (980, 565)
    )

    # Angle arrow at mouth opening
    draw.line([(1065, 370), (1085, 430)], fill=(15, 23, 42), width=2)
    draw.polygon([(1065, 370), (1067, 378), (1073, 374)], fill=(15, 23, 42))
    draw.polygon([(1085, 430), (1077, 427), (1082, 422)], fill=(15, 23, 42))
    draw.text((1090, 395), ">120°", fill=(15, 23, 42), font=fonts["section_title"])

    # Boca Aberta Badge placed neatly below angle arrow
    draw.rounded_rectangle([(1040, 448), (1118, 496)], radius=5, 
                           fill=(240, 253, 250), outline=(13, 148, 136), width=1)
    draw.text((1046, 452), "Boca Aberta", fill=(13, 148, 136), font=fonts["chart_title"])
    draw.text((1046, 466), "Ângulo Amplo", fill=(15, 23, 42), font=fonts["pill_num"])
    draw.text((1046, 480), "Abertura > 120°", fill=(100, 116, 139), font=fonts["chart_label"])

    # =========================================================================
    # 9. INSET BOX: MECANISMO DA ORDENHA INTRAORAL (Bottom Right)
    # =========================================================================
    # Inset is at x: 1116 to 1350, y: 515 to 745
    # Header banner on top of inset
    draw.rounded_rectangle([(1116, 498), (1350, 524)], radius=4, fill=(15, 23, 42))
    draw.text((1128, 504), "MECANISMO DA ORDENHA INTRAORAL", 
              fill=(255, 255, 255), font=fonts["inset_header"])

    # Footer banner below inset
    draw.rounded_rectangle([(1116, 735), (1350, 762)], radius=4, 
                           fill=(248, 250, 252), outline=(203, 213, 225), width=1)
    draw.text((1124, 738), "• Papila no palato mole (Ponto S de sucção)", 
              fill=(15, 23, 42), font=fonts["inset_body"])
    draw.text((1124, 749), "• Ordenha peristáltica da língua • Sucção indolor", 
              fill=(100, 116, 139), font=fonts["inset_body"])

    # =========================================================================
    # 10. SAVE OUTPUTS
    # =========================================================================
    final_cv = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    
    # Save to site target
    os.makedirs(os.path.dirname(SITE_TARGET), exist_ok=True)
    cv2.imwrite(SITE_TARGET, final_cv, [cv2.IMWRITE_JPEG_QUALITY, 96])
    print(f"Saved to site target: {SITE_TARGET}")

    # Save to artifact target
    os.makedirs(os.path.dirname(ARTIFACT_TARGET), exist_ok=True)
    cv2.imwrite(ARTIFACT_TARGET, final_cv, [cv2.IMWRITE_JPEG_QUALITY, 96])
    print(f"Saved to artifact target: {ARTIFACT_TARGET}")

if __name__ == "__main__":
    main()
