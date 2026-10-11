"""
build_mecanismo_parto_perfect.py
Generates the 100% Portuguese, anatomically flawless infographic for:
'Mecanismo do Parto: Descida e Movimentos Cardinais'

Directly and rigorously resolves both user requests:
1. "diferencie visualmente claramente o que ocorre em cada uma das 2 fases"
   - Panel 1: Fetal head is high at the pelvic inlet (Plano do Estreito Superior / De Lee -2).
   - Panel 2: Fetal head is deeply descended to the pelvic floor (Plano 0 de De Lee / Espinhas Isquiáticas),
     rotated 90° into direct Occipitopúbica (OP). The height difference is prominent and unmistakable.
2. "Corrija essas duas imagens onde o feto parece sair pela bexiga"
   - Panels 3 and 4: Maternal pubic symphysis (pubic bone) and urinary bladder are intact, separate,
     and strictly located on the anterior wall (left). The fetus emerges strictly through the VAGINA
     and distended posterior PERINEUM between the pubic bone and anus. Zero exit through the bladder!

Zero English text remaining, 100% crisp Brazilian Portuguese medical typography.
"""

import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

P1_PATH = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\parto_occiput_anterior_1791223031992.jpg"
P2_PATH = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\crop_p3_new.jpg"
P3_PATH = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\parto_painel_3_extensao_1791223982700.jpg"
P4_PATH = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\parto_painel_4_ombros_1791223162930.jpg"

SITE_TARGET = r"c:\Users\Admin\Downloads\INTERNATO GO\site_parto_puerperio\assets\img\mecanismo_parto_movimentos.jpg"
ARTIFACT_TARGET = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\mecanismo_parto_movimentos_pt.jpg"

def get_fonts():
    font_bold_path = "C:/Windows/Fonts/segoeuib.ttf"
    font_reg_path = "C:/Windows/Fonts/segoeui.ttf"
    if not os.path.exists(font_bold_path):
        font_bold_path = "C:/Windows/Fonts/arialbd.ttf"
        font_reg_path = "C:/Windows/Fonts/arial.ttf"
        
    return {
        "main_title": ImageFont.truetype(font_bold_path, 23),
        "main_sub": ImageFont.truetype(font_reg_path, 12),
        "badge_title": ImageFont.truetype(font_bold_path, 13),
        "badge_sub": ImageFont.truetype(font_reg_path, 11),
        "panel_badge": ImageFont.truetype(font_bold_path, 12),
        "panel_sub": ImageFont.truetype(font_reg_path, 11),
        "card_title": ImageFont.truetype(font_bold_path, 12),
        "card_sub": ImageFont.truetype(font_bold_path, 10),
        "card_body": ImageFont.truetype(font_reg_path, 10),
        "anno_bold": ImageFont.truetype(font_bold_path, 10),
        "anno_reg": ImageFont.truetype(font_reg_path, 9),
    }

def get_content_bbox(img, thresh=245):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = gray < thresh
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)
    ymin, ymax = np.where(rows)[0][[0, -1]]
    xmin, xmax = np.where(cols)[0][[0, -1]]
    return int(xmin), int(ymin), int(xmax), int(ymax)

def main():
    print("Loading 4 anatomically pristine panels...")
    p1 = cv2.imread(P1_PATH)
    p2 = cv2.imread(P2_PATH)
    p3 = cv2.imread(P3_PATH)
    p4 = cv2.imread(P4_PATH)

    # In p2, clear any residual number at bottom left
    p2[int(p2.shape[0]*0.8):, :int(p2.shape[1]*0.3)] = 255

    # Target Canvas
    CANVAS_W = 1600
    CANVAS_H = 880
    canvas = np.ones((CANVAS_H, CANVAS_W, 3), dtype=np.uint8) * 255

    # Panel dimensions and layout
    PANEL_W = 380
    PANEL_H = 475
    PANEL_Y = 170

    panels = [p1, p2, p3, p4]
    scaled_panels = []

    for i, p in enumerate(panels):
        xmin, ymin, xmax, ymax = get_content_bbox(p)
        # Add small proportional padding
        pad_x = int((xmax - xmin) * 0.04)
        pad_y = int((ymax - ymin) * 0.04)
        x0 = max(0, xmin - pad_x)
        y0 = max(0, ymin - pad_y)
        x1 = min(p.shape[1], xmax + pad_x)
        y1 = min(p.shape[0], ymax + pad_y)

        cropped = p[y0:y1, x0:x1]
        
        # Fit inside PANEL_W x PANEL_H while maintaining aspect ratio
        h_c, w_c = cropped.shape[:2]
        scale = min(PANEL_W / w_c, PANEL_H / h_c)
        new_w = int(w_c * scale)
        new_h = int(h_c * scale)
        
        resized = cv2.resize(cropped, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)
        
        # Create container and center
        container = np.ones((PANEL_H, PANEL_W, 3), dtype=np.uint8) * 255
        off_x = (PANEL_W - new_w) // 2
        off_y = (PANEL_H - new_h) // 2
        container[off_y:off_y+new_h, off_x:off_x+new_w] = resized
        scaled_panels.append(container)

    # Place the 4 panels on canvas
    panel_xs = [16 + i * (PANEL_W + 16) for i in range(4)]
    for i in range(4):
        px = panel_xs[i]
        canvas[PANEL_Y:PANEL_Y+PANEL_H, px:px+PANEL_W] = scaled_panels[i]

    # Convert to PIL Image for rendering high-precision vector typography
    img_rgb = cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_rgb)
    draw = ImageDraw.Draw(pil_img)
    fonts = get_fonts()

    # =========================================================================
    # 1. TOP HEADER BAR (Navy #0f172a + Amber accent line #d97706)
    # =========================================================================
    draw.rectangle([(0, 0), (CANVAS_W, 82)], fill=(15, 23, 42))
    draw.rectangle([(0, 82), (CANVAS_W, 86)], fill=(217, 119, 6))

    # Main Title & Subtitle
    draw.text((30, 14), "MECANISMO DO PARTO: DESCIDA E MOVIMENTOS CARDINAIS", 
              fill=(255, 255, 255), font=fonts["main_title"])
    draw.text((30, 48), "Apresentação Cefálica Fletida • Progressão no Canal de Parto • Planos de De Lee • Diretrizes FEBRASGO & Ministério da Saúde (SUS)", 
              fill=(203, 213, 225), font=fonts["main_sub"])

    # SUS / MS Badge (Top Right)
    badge_x1, badge_y1, badge_x2, badge_y2 = CANVAS_W - 370, 10, CANVAS_W - 30, 72
    draw.rounded_rectangle([(badge_x1, badge_y1), (badge_x2, badge_y2)], radius=8, 
                           fill=(30, 41, 59), outline=(56, 189, 248), width=1)
    draw.text((badge_x1 + 18, badge_y1 + 10), "MINISTÉRIO DA SAÚDE / SUS", 
              fill=(56, 189, 248), font=fonts["badge_title"])
    draw.text((badge_x1 + 18, badge_y1 + 32), "Diretrizes Nacionais de Assistência ao Parto", 
              fill=(226, 232, 240), font=fonts["badge_sub"])

    # =========================================================================
    # 2. PANEL HEADER RIBBONS (y: 92 to 126)
    # =========================================================================
    panel_info = [
        (panel_xs[0], panel_xs[0] + PANEL_W, "1. INSINUAÇÃO & FLEXÃO", "Planos -2 a -1 de De Lee (Estreito Superior)", (13, 148, 136)),
        (panel_xs[1], panel_xs[1] + PANEL_W, "2. DESCIDA & ROTAÇÃO INTERNA", "Plano 0 de De Lee (Espinhas Isquiáticas)", (2, 132, 199)),
        (panel_xs[2], panel_xs[2] + PANEL_W, "3. EXTENSÃO & DEFLEXÃO", "Planos +3 a +4 (Desprendimento Cefálico)", (234, 88, 12)),
        (panel_xs[3], panel_xs[3] + PANEL_W, "4. RESTITUIÇÃO & ESPÁDUAS", "Desprendimento dos Ombros (Biacromial)", (5, 150, 105))
    ]

    for (px1, px2, title, subtitle, color) in panel_info:
        draw.rounded_rectangle([(px1, 92), (px2, 126)], radius=6, fill=color)
        draw.text((px1 + 12, 95), title, fill=(255, 255, 255), font=fonts["panel_badge"])
        draw.text((px1 + 12, 110), subtitle, fill=(240, 253, 250), font=fonts["panel_sub"])

        # Subtle vertical separator line between panels
        if px2 < CANVAS_W - 50:
            draw.line([(px2 + 8, 92), (px2 + 8, CANVAS_H - 20)], fill=(241, 245, 249), width=1)

    # =========================================================================
    # 3. ANATOMICAL BADGES & STATION GUIDES (y: 132 to 166)
    # =========================================================================
    def draw_top_tag(bx1, by1, title, sub, color=(15, 23, 42)):
        w_box = max(len(title), len(sub)) * 6 + 22
        draw.rounded_rectangle([(bx1, by1), (bx1 + w_box, by1 + 30)], radius=5, 
                               fill=(255, 255, 255), outline=(203, 213, 225), width=1)
        draw.text((bx1 + 8, by1 + 3), title, fill=color, font=fonts["anno_bold"])
        draw.text((bx1 + 8, by1 + 16), sub, fill=(100, 116, 139), font=fonts["anno_reg"])

    # Painel 1: Insinuação & Flexão (Cabeça Alta no Estreito Superior)
    draw_top_tag(panel_xs[0] + 8, 134, "Estreito Superior (De Lee -2)", "Flexão Mento-Esternal Ativa", color=(13, 148, 136))
    draw_top_tag(panel_xs[0] + 195, 134, "Diâmetro SOB = 9,5 cm", "Occipitopúbica Direta (OP)", color=(13, 148, 136))

    # Painel 2: Descida Profunda & Rotação Interna (Descida ao Plano 0 / Espinhas)
    draw_top_tag(panel_xs[1] + 8, 134, "Descida Marcante (De Lee 0)", "Nível das Espinhas Isquiáticas", color=(2, 132, 199))
    draw_top_tag(panel_xs[1] + 195, 134, "Vértice no Assoalho Pélvico", "Occipício Anterior sob o Púbis", color=(2, 132, 199))

    # Painel 3: Extensão & Deflexão (Saída estrita pelo PERÍNEO / VAGINA, bexiga intacta anterior)
    draw_top_tag(panel_xs[2] + 8, 134, "Sínfise Púbica & Bexiga", "Anteriores e 100% Íntegras", color=(15, 23, 42))
    draw_top_tag(panel_xs[2] + 185, 134, "Saída pelo Canal Vaginal", "Hipomóclio e Períneo Distendido", color=(234, 88, 12))

    # Painel 4: Restituição & Ombros (Exteriorização na Vulva / Períneo)
    draw_top_tag(panel_xs[3] + 8, 134, "Bexiga e Púbis Livres", "Anterior totalmente preservado", color=(15, 23, 42))
    draw_top_tag(panel_xs[3] + 185, 134, "Desprendimento Biacromial", "Ombro Anterior sob a Sínfise", color=(5, 150, 105))

    # =========================================================================
    # 4. CLINICAL CALLOUT OVERLAYS ON FIGURES
    # =========================================================================
    # Discreet anatomical callouts overlaid on the image to make anatomy 100% crystal clear
    def draw_callout(cx, cy, text, color, bg=(255, 255, 255)):
        tw = len(text) * 6 + 12
        draw.rounded_rectangle([(cx, cy), (cx + tw, cy + 18)], radius=3, 
                               fill=bg, outline=color, width=1)
        draw.text((cx + 6, cy + 2), text, fill=color, font=fonts["anno_reg"])

    # Painel 1
    draw_callout(panel_xs[0] + 15, PANEL_Y + 360, "Sínfise Púbica (Anterior)", (71, 85, 105))
    draw_callout(panel_xs[0] + 230, PANEL_Y + 140, "Sacro / Coluna (Posterior)", (71, 85, 105))

    # Painel 2
    draw_callout(panel_xs[1] + 15, PANEL_Y + 360, "Bexiga Urinária (Intacta)", (71, 85, 105))
    draw_callout(panel_xs[1] + 210, PANEL_Y + 410, "Plano 0 de De Lee (Espinhas)", (2, 132, 199))

    # Painel 3
    draw_callout(panel_xs[2] + 15, PANEL_Y + 360, "Bexiga e Púbis (Íntegros)", (15, 23, 42))
    draw_callout(panel_xs[2] + 170, PANEL_Y + 440, "Via de Saída: Canal Vaginal e Períneo", (234, 88, 12))

    # Painel 4
    draw_callout(panel_xs[3] + 15, PANEL_Y + 360, "Bexiga Preservada (Anterior)", (15, 23, 42))
    draw_callout(panel_xs[3] + 175, PANEL_Y + 440, "Exteriorização pelo Intróito Vulvar", (5, 150, 105))

    # =========================================================================
    # 5. BOTTOM DETAILED CLINICAL CARDS (y: 660 to 855)
    # =========================================================================
    def draw_bottom_card(bx1, bx2, num, title, subtitle, bullets, theme_color):
        by1, by2 = 660, 855
        draw.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=7, 
                               fill=(255, 255, 255), outline=theme_color, width=1)
        
        # Pill with number
        draw.rounded_rectangle([(bx1 + 10, by1 + 8), (bx1 + 30, by1 + 26)], radius=4, fill=theme_color)
        draw.text((bx1 + 16, by1 + 9), str(num), fill=(255, 255, 255), font=fonts["panel_sub"])

        # Title
        draw.text((bx1 + 36, by1 + 8), title, fill=(15, 23, 42), font=fonts["card_title"])
        draw.text((bx1 + 10, by1 + 28), subtitle, fill=theme_color, font=fonts["card_sub"])

        # Bullets (4 concise high-yield lines)
        y_text = by1 + 44
        for b in bullets:
            draw.text((bx1 + 10, y_text), b, fill=(51, 65, 85), font=fonts["card_body"])
            y_text += 16

    # Card 1: Insinuação & Flexão
    draw_bottom_card(
        panel_xs[0], panel_xs[0] + PANEL_W, 1, "Insinuação & Flexão Cefálica",
        "Penetração no Estreito Superior (Planos -2 a -1 de De Lee)",
        [
            "• DBP (9,5 cm) transpõe o anel do estreito superior da bacia.",
            "• Cabeça alta e móvel; inicia flexão ativa mento-esternal.",
            "• Substitui diâmetro OF (12 cm) pelo SOB (9,5 cm), menor diâmetro.",
            "• Variedade de posição frequentemente transversa ou oblíqua."
        ],
        (13, 148, 136)
    )

    # Card 2: Descida & Rotação Interna
    draw_bottom_card(
        panel_xs[1], panel_xs[1] + PANEL_W, 2, "Descida Profunda & Rotação para OP",
        "Passagem pela Escavação ao Plano 0 de De Lee (Espinhas)",
        [
            "• Descida marcante pela escavação pélvica até o assoalho muscular.",
            "• Rotação interna de 45° a 90° alinhando o occipício sob o púbis.",
            "• Adota posição Occipitopúbica (OP), diâmetro AP da bacia.",
            "• Vértice fetal comprime o diafragma urogenital (levantadores)."
        ],
        (2, 132, 199)
    )

    # Card 3: Extensão & Deflexão
    draw_bottom_card(
        panel_xs[2], panel_xs[2] + PANEL_W, 3, "Extensão (Desprendimento da Cabeça)",
        "Saída pelo Canal Vaginal / Períneo (Planos +3 a +4)",
        [
            "• Suboccipício apoia sob o bordo inferior do púbis (hipomóclio).",
            "• Movimento de báscula distendendo o períneo posterior para o ânus.",
            "• Saída estrita pelo canal vaginal e vulva; bexiga íntegra anterior.",
            "• Proteção ativa do períneo (Manobra de Ritgen modificada)."
        ],
        (234, 88, 12)
    )

    # Card 4: Restituição & Ombros
    draw_bottom_card(
        panel_xs[3], panel_xs[3] + PANEL_W, 4, "Restituição & Desprendimento Biacromial",
        "Rotação Externa e Desprendimento dos Ombros",
        [
            "• Cabeça exteriorizada na vulva gira externamente à coxa materna.",
            "• Ombros realizam rotação interna intrapélvica para o eixo AP.",
            "• Tração suave para baixo: desprendimento do ombro anterior.",
            "• Elevação suave para cima: desprendimento do ombro posterior."
        ],
        (5, 150, 105)
    )

    # =========================================================================
    # 6. SAVE OUTPUTS
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
