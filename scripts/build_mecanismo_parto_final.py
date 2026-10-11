"""
build_mecanismo_parto_final.py
Generates the 100% Portuguese, zero-English, anatomically accurate infographic for:
'Mecanismo do Parto: Descida e Movimentos Cardinais'
Strictly adhering to Ministério da Saúde / SUS, FEBRASGO, Williams Obstetrics, and Rezende guidelines.
"""

import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SRC_PATH = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\labor_mechanisms_v2_1791208881976.jpg"
SITE_TARGET = r"c:\Users\Admin\Downloads\INTERNATO GO\site_parto_puerperio\assets\img\mecanismo_parto_movimentos.jpg"
ARTIFACT_TARGET = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\mecanismo_parto_movimentos_pt.jpg"

def get_fonts():
    font_bold_path = "C:/Windows/Fonts/segoeuib.ttf"
    font_reg_path = "C:/Windows/Fonts/segoeui.ttf"
    if not os.path.exists(font_bold_path):
        font_bold_path = "C:/Windows/Fonts/arialbd.ttf"
        font_reg_path = "C:/Windows/Fonts/arial.ttf"
        
    return {
        "main_title": ImageFont.truetype(font_bold_path, 21),
        "main_sub": ImageFont.truetype(font_reg_path, 11),
        "badge_title": ImageFont.truetype(font_bold_path, 12),
        "badge_sub": ImageFont.truetype(font_reg_path, 10),
        "panel_badge": ImageFont.truetype(font_bold_path, 11),
        "panel_sub": ImageFont.truetype(font_bold_path, 10),
        "card_title": ImageFont.truetype(font_bold_path, 11),
        "card_sub": ImageFont.truetype(font_bold_path, 9),
        "card_body": ImageFont.truetype(font_reg_path, 9),
        "anno_bold": ImageFont.truetype(font_bold_path, 9),
        "anno_reg": ImageFont.truetype(font_reg_path, 8),
    }

def main():
    print("Reading pristine source image...")
    orig = cv2.imread(SRC_PATH)
    h, w = orig.shape[:2]

    cleaned = orig.copy()

    # 1. Clear top area completely (y: 0 to 125) to guarantee clean white header background
    cleaned[0:125, :] = 255

    # 2. Clear bottom text completely (y: 615 to 768)
    cleaned[615:768, :] = 255

    # Convert to PIL Image for rendering
    img_rgb = cv2.cvtColor(cleaned, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_rgb)
    draw = ImageDraw.Draw(pil_img)
    fonts = get_fonts()

    # =========================================================================
    # 3. TOP HEADER BAR (Navy #0f172a + Amber accent line #d97706)
    # =========================================================================
    draw.rectangle([(0, 0), (w, 82)], fill=(15, 23, 42))
    draw.rectangle([(0, 82), (w, 86)], fill=(217, 119, 6))

    # Main Title & Subtitle
    draw.text((25, 14), "MECANISMO DO PARTO: DESCIDA E MOVIMENTOS CARDINAIS", 
              fill=(255, 255, 255), font=fonts["main_title"])
    draw.text((25, 46), "Apresentação Cefálica Fletida • Progressão no Canal de Parto • Planos de De Lee • Diretrizes FEBRASGO & Ministério da Saúde (SUS)", 
              fill=(203, 213, 225), font=fonts["main_sub"])

    # SUS / MS Badge (Top Right)
    badge_x1, badge_y1, badge_x2, badge_y2 = w - 345, 10, w - 25, 72
    draw.rounded_rectangle([(badge_x1, badge_y1), (badge_x2, badge_y2)], radius=8, 
                           fill=(30, 41, 59), outline=(56, 189, 248), width=1)
    draw.text((badge_x1 + 16, badge_y1 + 10), "MINISTÉRIO DA SAÚDE / SUS", 
              fill=(56, 189, 248), font=fonts["badge_title"])
    draw.text((badge_x1 + 16, badge_y1 + 30), "Diretrizes Nacionais de Assistência ao Parto", 
              fill=(226, 232, 240), font=fonts["badge_sub"])

    # =========================================================================
    # 4. PANEL HEADER RIBBONS & TOP DETAILS (y: 95 to 125)
    # =========================================================================
    # Panels horizontal bounds:
    # P1: [20, 350], P2: [355, 685], P3: [690, 1020], P4: [1025, 1355]
    panel_info = [
        (20, 350, "1. INSINUAÇÃO & FLEXÃO", "Planos -2 a -1 de De Lee", (13, 148, 136)),
        (355, 685, "2. DESCIDA & ROTAÇÃO INTERNA", "Plano 0 de De Lee (Espinhas)", (2, 132, 199)),
        (690, 1020, "3. EXTENSÃO & DEFLEXÃO", "Planos +3 a +4 (Coroamento)", (234, 88, 12)),
        (1025, 1355, "4. RESTITUIÇÃO & ESPÁDUAS", "Desprendimento dos Ombros", (5, 150, 105))
    ]

    for (px1, px2, title, subtitle, color) in panel_info:
        # Header banner for each panel
        draw.rounded_rectangle([(px1, 92), (px2, 122)], radius=5, fill=color)
        draw.text((px1 + 10, 95), title, fill=(255, 255, 255), font=fonts["panel_badge"])
        # Right-aligned or subtitle
        draw.text((px1 + 10, 108), subtitle, fill=(240, 253, 250), font=fonts["anno_reg"])

        # Subtle vertical separator line between panels
        if px2 < 1350:
            draw.line([(px2 + 3, 92), (px2 + 3, 755)], fill=(241, 245, 249), width=1)

    # =========================================================================
    # 5. (ANATOMICAL PANELS ARE KEPT 100% PRISTINE & UNCLUTTERED)
    # =========================================================================
    # The visual artwork of the fetal progression and maternal pelvis is completely
    # unobstructed, while the colored ribbons above and detailed clinical cards
    # below provide 100% of the medical and semiological information.

    # =========================================================================
    # 6. BOTTOM DETAILED CLINICAL CARDS (y: 615 to 755)
    # =========================================================================
    def draw_bottom_card(bx1, bx2, num, title, subtitle, bullets, theme_color):
        by1, by2 = 615, 755
        draw.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=6, 
                               fill=(255, 255, 255), outline=theme_color, width=1)
        
        # Pill with number
        draw.rounded_rectangle([(bx1 + 8, by1 + 6), (bx1 + 26, by1 + 22)], radius=3, fill=theme_color)
        draw.text((bx1 + 13, by1 + 7), str(num), fill=(255, 255, 255), font=fonts["panel_sub"])

        # Title
        draw.text((bx1 + 32, by1 + 6), title, fill=(15, 23, 42), font=fonts["card_title"])
        draw.text((bx1 + 10, by1 + 24), subtitle, fill=theme_color, font=fonts["card_sub"])

        # Bullets (4 concise high-yield lines)
        y_text = by1 + 38
        for b in bullets:
            draw.text((bx1 + 10, y_text), b, fill=(71, 85, 105), font=fonts["card_body"])
            y_text += 14

    # Card 1: Insinuação & Flexão
    draw_bottom_card(
        20, 350, 1, "Insinuação & Flexão Cefálica",
        "Penetração no Estreito Superior (Planos -2 a -1)",
        [
            "• DBP (9,5 cm) transpõe o anel do estreito superior.",
            "• Resistência pélvica força a flexão mento-esternal.",
            "• Substitui diâmetro OF (12 cm) por SOB (9,5 cm).",
            "• Variedade de posição oblíqua/transversa (OET/OEA)."
        ],
        (13, 148, 136)
    )

    # Card 2: Descida & Rotação Interna
    draw_bottom_card(
        355, 685, 2, "Descida & Rotação para OP",
        "Passagem pela Escavação (Plano 0 de De Lee)",
        [
            "• Progressão contínua por contrações e prensa materna.",
            "• Rotação interna de 45° a 90° para Occipitopúbica (OP).",
            "• Alinha maior diâmetro ao eixo anteroposterior inferior.",
            "• Vértice atinge o assoalho pélvico (m. puborretal)."
        ],
        (2, 132, 199)
    )

    # Card 3: Extensão & Deflexão
    draw_bottom_card(
        690, 1020, 3, "Extensão (Desprendimento)",
        "Coroamento e Desprendimento (Planos +3 a +4)",
        [
            "• Suboccipício apoia sob a sínfise púbica (hipomóclio).",
            "• Movimento de alavanca (báscula) distendendo períneo.",
            "• Desprendem: bregma, fronte, nariz, boca e mento.",
            "• Proteção perineal ativa (Manobra de Ritgen modificada)."
        ],
        (234, 88, 12)
    )

    # Card 4: Restituição & Ombros
    draw_bottom_card(
        1025, 1355, 4, "Restituição & Ombros",
        "Rotação Externa e Desprendimento Biacromial",
        [
            "• Cabeça gira externamente voltando à coxa materna.",
            "• Ombros realizam rotação interna no diâmetro AP.",
            "• Tração para baixo: desprendimento do ombro anterior.",
            "• Elevação suave: desprendimento do ombro posterior."
        ],
        (5, 150, 105)
    )

    # =========================================================================
    # 7. SAVE OUTPUTS
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
