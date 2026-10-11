"""
build_bakri_anatomical.py
Creates the 100% Portuguese, highly detailed, anatomically accurate infographic
for Intrauterine Balloon Tamponade (Bakri) in Postpartum Hemorrhage (HPP),
compliant with Ministério da Saúde / SUS and FEBRASGO guidelines.
"""

import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SRC_PATH = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\bakri_anatomy_v2_1791197673025.jpg"
SITE_TARGET = r"c:\Users\Admin\Downloads\INTERNATO GO\site_parto_puerperio\assets\img\hemorragia_pos_parto_balao_bakri.jpg"
ARTIFACT_TARGET = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\hemorragia_pos_parto_balao_bakri_pt.jpg"

def get_fonts():
    font_bold_path = "C:/Windows/Fonts/segoeuib.ttf"
    font_reg_path = "C:/Windows/Fonts/segoeui.ttf"
    if not os.path.exists(font_bold_path):
        font_bold_path = "C:/Windows/Fonts/arialbd.ttf"
        font_reg_path = "C:/Windows/Fonts/arial.ttf"
        
    return {
        "main_title": ImageFont.truetype(font_bold_path, 18),
        "main_sub": ImageFont.truetype(font_reg_path, 11),
        "badge_title": ImageFont.truetype(font_bold_path, 12),
        "badge_sub": ImageFont.truetype(font_reg_path, 10),
        "sec_title": ImageFont.truetype(font_bold_path, 13),
        "sec_sub": ImageFont.truetype(font_reg_path, 10),
        "card_title": ImageFont.truetype(font_bold_path, 11),
        "card_sub": ImageFont.truetype(font_reg_path, 9),
        "card_header": ImageFont.truetype(font_bold_path, 10),
        "test_pos": ImageFont.truetype(font_bold_path, 10),
        "test_pos_sub": ImageFont.truetype(font_reg_path, 9),
        "test_neg": ImageFont.truetype(font_bold_path, 10),
        "test_neg_sub": ImageFont.truetype(font_reg_path, 9),
        "float_title": ImageFont.truetype(font_bold_path, 10),
        "float_sub": ImageFont.truetype(font_reg_path, 9),
    }

def main():
    print("Reading anatomically accurate pristine source...")
    orig = cv2.imread(SRC_PATH)
    h, w = orig.shape[:2]

    # Convert to PIL Image for rendering typography and graphics
    img_rgb = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img_rgb)
    draw = ImageDraw.Draw(pil_img)
    fonts = get_fonts()

    # =========================================================================
    # 1. TOP HEADER BAR (Navy #0f172a + Amber accent line #d97706)
    # =========================================================================
    draw.rectangle([(0, 0), (w, 84)], fill=(15, 23, 42))
    draw.rectangle([(0, 84), (w, 88)], fill=(217, 119, 6))

    # Main Title & Subtitle (18pt ensures no collision with badge)
    draw.text((25, 16), "MANEJO DA HEMORRAGIA PÓS-PARTO (HPP): BALÃO DE TAMPONAMENTO INTRAUTERINO (BAKRI)", 
              fill=(255, 255, 255), font=fonts["main_title"])
    draw.text((25, 48), "Controle Mecânico da Atonia Uterina Refratária • Anatomia Sagital Pélvica • Diretrizes FEBRASGO & Ministério da Saúde (SUS)", 
              fill=(203, 213, 225), font=fonts["main_sub"])

    # SUS / MS Badge (Top Right)
    badge_x1, badge_y1, badge_x2, badge_y2 = w - 355, 12, w - 25, 72
    draw.rounded_rectangle([(badge_x1, badge_y1), (badge_x2, badge_y2)], radius=8, 
                           fill=(30, 41, 59), outline=(56, 189, 248), width=1)
    draw.text((badge_x1 + 16, badge_y1 + 10), "MINISTÉRIO DA SAÚDE / SUS", 
              fill=(56, 189, 248), font=fonts["badge_title"])
    draw.text((badge_x1 + 16, badge_y1 + 30), "Protocolos de Atenção Hospitalar • HPP", 
              fill=(226, 232, 240), font=fonts["badge_sub"])

    # =========================================================================
    # 2. SECTION SUBHEADERS
    # =========================================================================
    # Left Section Header
    draw.text((25, 96), "ANATOMIA SAGITAL & ATONIA UTERINA", 
              fill=(15, 23, 42), font=fonts["sec_title"])
    draw.text((25, 114), "Fisiopatologia da hipotonia miometrial e ação mecânica hemostática", 
              fill=(100, 116, 139), font=fonts["sec_sub"])

    # Right Section Header
    draw.text((1005, 96), "PROTOCOLO CLÍNICO & CONDUTA (MS / FEBRASGO)", 
              fill=(15, 23, 42), font=fonts["sec_title"])
    draw.text((1005, 114), "Teste do balão, vigilância contínua do débito e tomada de decisão", 
              fill=(100, 116, 139), font=fonts["sec_sub"])

    # Subtle divider lines
    draw.line([(355, 98), (355, 755)], fill=(241, 245, 249), width=1)
    draw.line([(985, 98), (985, 755)], fill=(241, 245, 249), width=1)

    # =========================================================================
    # 3. HELPER FUNCTIONS FOR POINTER CARDS
    # =========================================================================
    def draw_left_card(box_coords, title, sub_line1, sub_line2, target_point, alert_title=False):
        bx1, by1, bx2, by2 = box_coords
        border_col = (239, 68, 68) if alert_title else (203, 213, 225)
        title_col = (220, 38, 38) if alert_title else (15, 23, 42)
        
        draw.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=6, 
                               fill=(255, 255, 255), outline=border_col, width=1)
        draw.text((bx1 + 10, by1 + 6), title, fill=title_col, font=fonts["card_title"])
        draw.text((bx1 + 10, by1 + 24), sub_line1, fill=(71, 85, 105), font=fonts["card_sub"])
        draw.text((bx1 + 10, by1 + 38), sub_line2, fill=(100, 116, 139), font=fonts["card_sub"])

        # Pointer line starts at right edge bx2 and connects to target_point
        tx, ty = target_point
        px = bx2
        py = (by1 + by2) // 2
        draw.line([(px, py), (tx, ty)], fill=(71, 85, 105), width=1)
        draw.ellipse([(tx - 3, ty - 3), (tx + 3, ty + 3)], fill=(220, 38, 38) if alert_title else (15, 23, 42))

    def draw_right_card(box_coords, title, sub_line1, sub_line2, target_point=None, header_ribbon=None):
        bx1, by1, bx2, by2 = box_coords
        draw.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=6, 
                               fill=(255, 255, 255), outline=(203, 213, 225), width=1)
        
        y_offset = by1 + 6
        if header_ribbon:
            draw.rounded_rectangle([(bx1, by1), (bx2, by1 + 22)], radius=6, fill=header_ribbon[1])
            draw.rectangle([(bx1, by1 + 14), (bx2, by1 + 22)], fill=header_ribbon[1])
            draw.text((bx1 + 10, by1 + 4), header_ribbon[0], fill=(255, 255, 255), font=fonts["card_header"])
            y_offset = by1 + 28

        draw.text((bx1 + 10, y_offset), title, fill=(15, 23, 42), font=fonts["card_title"])
        draw.text((bx1 + 10, y_offset + 18), sub_line1, fill=(71, 85, 105), font=fonts["card_sub"])
        draw.text((bx1 + 10, y_offset + 32), sub_line2, fill=(100, 116, 139), font=fonts["card_sub"])

        if target_point:
            tx, ty = target_point
            px = bx1
            py = (by1 + by2) // 2
            draw.line([(px, py), (tx, ty)], fill=(71, 85, 105), width=1)
            draw.ellipse([(tx - 3, ty - 3), (tx + 3, ty + 3)], fill=(15, 23, 42))

    # =========================================================================
    # 4. LEFT COLUMN CARDS & POINTERS
    # =========================================================================
    # Card 1: Fundo Uterino e Miométrio Hipotônico
    draw_left_card(
        (20, 140, 340, 198),
        "Útero Pós-Parto Hipotônico (Atonia)",
        "Falha da contração miometrial fisiológica",
        "Incompetência das 'ligaduras vivas' de Pinard",
        (470, 155), alert_title=True
    )

    # Card 2: Balão de Bakri Insuflado
    draw_left_card(
        (20, 225, 340, 283),
        "Balão Intrauterino Insuflado (Bakri)",
        "Preenchido c/ 300 a 500 mL de SF 0,9% morno",
        "Conforma-se perfeitamente à cavidade uterina",
        (560, 250)
    )

    # Card 3: Hemostasia e Pressão Hidrostática
    draw_left_card(
        (20, 310, 340, 368),
        "Pressão Hidrostática > Pressão Capilar",
        "Compressão mecânica direta dos seios venosos",
        "Oclusão hemostática das artérias espiraladas",
        (540, 350)
    )

    # Card 4: Sínfise Púbica Materna
    draw_left_card(
        (20, 480, 340, 538),
        "Sínfise Púbica (Pelve Anterior)",
        "Referência óssea anterior do estreito superior",
        "Limite anterior do espaço retropúbico",
        (380, 570)
    )

    # Card 5: Bexiga Descomprimida c/ Sonda de Foley
    draw_left_card(
        (20, 565, 340, 623),
        "Bexiga Esvaziada (Sonda de Foley)",
        "Esvaziamento vesical contínuo obrigatório",
        "Permite acomodação do útero e expansão do balão",
        (460, 535), alert_title=True
    )

    # Card 6: Floating Bottom Card for Catheter Ports
    draw.rounded_rectangle([(20, 645), (340, 755)], radius=6, 
                           fill=(255, 255, 255), outline=(56, 189, 248), width=1)
    draw.text((30, 652), "Conexões Externas do Balão", fill=(2, 132, 199), font=fonts["card_title"])
    draw.text((30, 670), "• Via de Insuflação (Torneira Luer-Lock):", fill=(15, 23, 42), font=fonts["float_title"])
    draw.text((38, 684), "Infusão estéril de 300 a 500 mL SF morno", fill=(71, 85, 105), font=fonts["float_sub"])
    draw.text((30, 702), "• Lúmen Central de Drenagem:", fill=(225, 29, 72), font=fonts["float_title"])
    draw.text((38, 716), "Conectado à bolsa coletora graduada", fill=(71, 85, 105), font=fonts["float_sub"])
    draw.text((38, 730), "Vigilância ativa do débito hemorrágico", fill=(100, 116, 139), font=fonts["float_sub"])
    
    # Pointer 1 to Stopcock
    draw.line([(340, 678), (480, 645)], fill=(2, 132, 199), width=1)
    draw.ellipse([(478, 643), (482, 647)], fill=(2, 132, 199))

    # Pointer 2 to Drainage Bag
    draw.line([(340, 720), (510, 710)], fill=(225, 29, 72), width=1)
    draw.ellipse([(508, 708), (512, 712)], fill=(225, 29, 72))

    # =========================================================================
    # 5. RIGHT COLUMN CARDS & "TAMPONADE TEST" (Aligned for zero line crossing)
    # =========================================================================
    # Card 1: Top Right - Reto, Canal Anal e Promontório Sacro
    draw_right_card(
        (1005, 140, 1355, 198),
        "Reto, Canal Anal e Promontório Sacro",
        "Topografia pélvica posterior de referência anatômica",
        "Relação espacial com o fundo de saco de Douglas",
        target_point=(900, 170)
    )

    # Card 2: Farmacoterapia Associada
    draw_right_card(
        (1005, 212, 1355, 288),
        "Terapia Adjuvante Mandatória (MS / FEBRASGO)",
        "Ocitocina contínua em BI (20 a 40 UI em infusão contínua)",
        "Antibioticoprofilaxia (Cefazolina 2g IV) por 24 horas",
        header_ribbon=("FARMACOTERAPIA ASSOCIADA", (14, 116, 144))
    )

    # Card 3: O TESTE DO BALÃO ("TAMPONADE TEST")
    c3_x1, c3_y1, c3_x2, c3_y2 = 1005, 296, 1355, 482
    draw.rounded_rectangle([(c3_x1, c3_y1), (c3_x2, c3_y2)], radius=8, 
                           fill=(255, 255, 255), outline=(13, 148, 136), width=1)
    
    # Header ribbon
    draw.rounded_rectangle([(c3_x1, c3_y1), (c3_x2, c3_y1 + 24)], radius=8, fill=(13, 148, 136))
    draw.rectangle([(c3_x1, c3_y1 + 16), (c3_x2, c3_y1 + 24)], fill=(13, 148, 136))
    draw.text((c3_x1 + 12, c3_y1 + 5), "TESTE DO BALÃO DE BAKRI ('TAMPONADE TEST')", 
              fill=(255, 255, 255), font=fonts["card_header"])

    draw.text((c3_x1 + 12, c3_y1 + 30), "Vigilância do Débito Hemorrágico na Bolsa (15 a 30 min):", 
              fill=(15, 23, 42), font=fonts["card_title"])

    # Box A: Teste Positivo (Sucesso)
    box_a_y = c3_y1 + 50
    draw.rounded_rectangle([(c3_x1 + 10, box_a_y), (c3_x2 - 10, box_a_y + 44)], radius=5, 
                           fill=(240, 253, 244), outline=(34, 197, 94), width=1)
    # Green circle badge
    draw.ellipse([(c3_x1 + 18, box_a_y + 8), (c3_x1 + 30, box_a_y + 20)], fill=(34, 197, 94))
    draw.text((c3_x1 + 21, box_a_y + 8), "+", fill=(255, 255, 255), font=fonts["test_pos"])
    draw.text((c3_x1 + 36, box_a_y + 6), "TESTE POSITIVO: Débito < 50 mL/h (SUCESSO)", 
              fill=(22, 101, 52), font=fonts["test_pos"])
    draw.text((c3_x1 + 36, box_a_y + 24), "Hemorragia controlada • Manter balão 12–24h • Desmame gradual", 
              fill=(21, 128, 61), font=fonts["test_pos_sub"])

    # Box B: Teste Negativo (Falha)
    box_b_y = box_a_y + 52
    draw.rounded_rectangle([(c3_x1 + 10, box_b_y), (c3_x2 - 10, box_b_y + 62)], radius=5, 
                           fill=(254, 242, 242), outline=(239, 68, 68), width=1)
    # Red circle badge
    draw.ellipse([(c3_x1 + 18, box_b_y + 8), (c3_x1 + 30, box_b_y + 20)], fill=(239, 68, 68))
    draw.text((c3_x1 + 22, box_b_y + 8), "-", fill=(255, 255, 255), font=fonts["test_neg"])
    draw.text((c3_x1 + 36, box_b_y + 6), "TESTE NEGATIVO: Débito > 50 mL/h (FALHA)", 
              fill=(153, 27, 27), font=fonts["test_neg"])
    draw.text((c3_x1 + 36, box_b_y + 24), "Sangramento ativo persistente apesar do tamponamento!", 
              fill=(185, 28, 28), font=fonts["test_neg_sub"])
    draw.text((c3_x1 + 36, box_b_y + 40), "Conduta: Laparotomia imediata (B-Lynch, ligaduras, histerectomia)", 
              fill=(153, 27, 27), font=fonts["test_neg"])

    # Card 4: Tamponamento Vaginal com Gaze (Direct short line to vaginal pack)
    draw_right_card(
        (1005, 495, 1355, 555),
        "Tamponamento Vaginal com Gaze",
        "Compressas de retenção na cúpula vaginal",
        "Evita a expulsão e deslocamento caudal do balão",
        target_point=(745, 570)
    )

    # Card 5: Prevenção de Histerectomia Puerperal
    draw.rounded_rectangle([(1005, 570), (1355, 642)], radius=6, 
                           fill=(248, 250, 252), outline=(203, 213, 225), width=1)
    draw.text((1015, 578), "Preservação da Fertilidade Feminina", fill=(15, 23, 42), font=fonts["card_title"])
    draw.text((1015, 596), "• Taxa de sucesso de 80% a 90% no controle da atonia", fill=(71, 85, 105), font=fonts["card_sub"])
    draw.text((1015, 610), "• Medida padrão-ouro de 2ª linha antes de histerectomia", fill=(71, 85, 105), font=fonts["card_sub"])
    draw.text((1015, 624), "• Evita cirurgia mutiladora em pacientes jovens / nulíparas", fill=(13, 148, 136), font=fonts["card_sub"])

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
