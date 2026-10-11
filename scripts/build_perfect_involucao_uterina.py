"""
Build Perfect Uterine Involution & Lochia Diagram - Version 2
============================================================
Ministério da Saúde / SUS / FEBRASGO Compliant
Zero English text, zero overlapping labels, flawless typography and layout.
"""

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def create_diagram():
    pristine_path = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\uterine_involution_1791067813177.jpg"
    orig = cv2.imread(pristine_path)
    h, w, _ = orig.shape  # 768, 1376

    # 1. Surgical cleaning of the 4 isolated uteri
    def clean_uterus(crop):
        b, g, r = cv2.split(crop)
        is_neutral = (np.abs(r.astype(int) - b.astype(int)) < 22) & (np.abs(r.astype(int) - g.astype(int)) < 22)
        is_dark = (r < 225) & (g < 225) & (b < 225)
        arrow_mask = is_neutral & is_dark
        diff = np.maximum(r.astype(int) - g.astype(int), r.astype(int) - b.astype(int))
        arrow_mask = arrow_mask & (diff < 15)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        mask = cv2.dilate((arrow_mask * 255).astype(np.uint8), kernel, iterations=1)
        cleaned = cv2.inpaint(crop, mask, 3, cv2.INPAINT_TELEA)
        return cleaned

    u1_crop = clean_uterus(orig[280:490, 460:630].copy())

    # Pristine u2 cleaning
    u2_raw = orig[270:490, 780:960].copy()
    u2_mask = np.zeros_like(u2_raw[:, :, 0])
    cv2.line(u2_mask, (0, -10), (60, 18), 255, 8)
    cv2.line(u2_mask, (55, 12), (78, 30), 255, 4)
    u2_crop = cv2.inpaint(u2_raw, u2_mask, 3, cv2.INPAINT_TELEA)
    u2_crop[120:, :65] = [255, 255, 255]
    u2_crop[90:, 135:] = [255, 255, 255]
    u2_crop[:15, :62] = [255, 255, 255]

    u3_crop = clean_uterus(orig[450:660, 600:790].copy())
    u4_crop = clean_uterus(orig[470:660, 790:970].copy())

    # 2. Surgical cleaning of sagittal diagram on left (x: 0 to 455)
    # A) Inpaint 'Umbilicus' text on sagittal cut (x: 320 to 450, y: 220 to 280)
    sag_crop = orig[220:280, 320:450].copy()
    gray_sag = cv2.cvtColor(sag_crop, cv2.COLOR_BGR2GRAY)
    mask_umb = (gray_sag < 70).astype(np.uint8) * 255
    mask_umb = cv2.dilate(mask_umb, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)
    sag_crop = cv2.inpaint(sag_crop, mask_umb, 3, cv2.INPAINT_TELEA)
    orig[220:280, 320:450] = sag_crop

    # B) Erase erroneous lower label and pointer line at x: 340 to 455, y: 520 to 600
    lower_crop = orig[520:600, 340:455].copy()
    gray_low = cv2.cvtColor(lower_crop, cv2.COLOR_BGR2GRAY)
    mask_low = (gray_low < 90).astype(np.uint8) * 255
    mask_low = cv2.dilate(mask_low, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)
    lower_crop = cv2.inpaint(lower_crop, mask_low, 3, cv2.INPAINT_TELEA)
    orig[520:600, 340:455] = lower_crop

    # C) Clear the white region above the spine / abdomen (y: 0 to 135) to eliminate 'CONTRACTING UTERUS...'
    orig[:135, :] = 255

    # 3. Assemble base canvas
    canvas = np.ones((h, w, 3), dtype=np.uint8) * 255

    # Paste cleaned sagittal diagram on the left
    canvas[135:768, 0:455] = orig[135:768, 0:455]

    # Paste the 4 cleaned uteri in the center column
    canvas[280:490, 460:630] = u1_crop
    canvas[270:490, 780:960] = u2_crop
    canvas[450:660, 600:790] = u3_crop
    canvas[470:660, 790:970] = u4_crop

    # Extract and paste the 3 lochia specimen cups from right side (x: 1005 to 1125)
    canvas[140:300, 1005:1125] = orig[140:300, 1005:1125]
    canvas[350:520, 1005:1125] = orig[350:520, 1005:1125]
    canvas[570:740, 1005:1125] = orig[570:740, 1005:1125]

    # Clean any tiny remnants around u1 top and u2 top
    for y in range(270, 292):
        for x in range(515, 545):
            b, g, r = canvas[y, x]
            if b < 100 and g < 100 and r < 100:
                canvas[y, x] = [255, 255, 255]

    for y in range(265, 290):
        for x in range(830, 865):
            b, g, r = canvas[y, x]
            if (b < 120 and g < 120 and r < 120) or (b > 220 and g > 220 and r > 220 and y > 275):
                canvas[y, x] = [255, 255, 255]

    # Clean old letter remnants to the right of Sínfise Púbica box (x: 440 to 460, y: 690 to 760)
    canvas[690:768, 440:460] = [255, 255, 255]

    # Convert to PIL Image for high-precision institutional typography and vector shapes
    pil_img = Image.fromarray(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)

    # Load system TrueType fonts
    font_title = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 25)
    font_sub = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 13)
    font_sec = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 13)
    font_sec_sub = ImageFont.truetype(r"C:\Windows\Fonts\segoeuii.ttf", 11)
    font_badge = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 11)
    font_badge_sm = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 10)
    font_body_b = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 11)
    font_body = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 10)
    font_body_sm = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 9)
    font_body_sm_b = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 9)
    font_alert = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 8)
    font_alert_b = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 9)

    # 4. Institutional Header Bar (y: 0 to 78)
    draw.rectangle([0, 0, w, 76], fill="#0f172a")
    draw.rectangle([0, 76, w, 78], fill="#f59e0b")  # Gold accent line

    # Header Titles
    draw.text((35, 18), "INVOLUÇÃO UTERINA & EVOLUÇÃO DOS LÓQUIOS NO PUERPÉRIO", fill="#ffffff", font=font_title)
    draw.text((35, 49), "Semiologia Puerperal Fisiológica • Altura de Fundo Uterino (Pinard) • Padrões Macroscópicos e Citológicos dos Lóquios", fill="#94a3b8", font=font_sub)

    # Institutional Badge on Right
    draw.rounded_rectangle([1060, 15, 1345, 61], radius=8, fill="#1e293b", outline="#38bdf8", width=1)
    draw.text((1202, 23), "MINISTÉRIO DA SAÚDE / SUS", fill="#38bdf8", font=font_badge, anchor="mm")
    draw.text((1202, 42), "Protocolo FEBRASGO de Puerpério", fill="#94a3b8", font=font_badge_sm, anchor="mm")

    # 5. Column Headers & Dividers (y: 84 to 125)
    # Left & Center Column Header
    draw.text((35, 86), "CRONOLOGIA DA INVOLUÇÃO UTERINA (MARCOS DE PINARD)", fill="#0f172a", font=font_sec)
    draw.text((35, 105), "Regressão anatômica da altura de fundo (~1 cm/dia) e retração miometrial após o parto", fill="#64748b", font=font_sec_sub)

    # Vertical Column Divider at x=992
    draw.line([(992, 82), (992, 760)], fill="#cbd5e1", width=2)

    # Right Column Header
    draw.text((1008, 86), "EVOLUÇÃO DOS LÓQUIOS (SEMIOLOGIA)", fill="#0f172a", font=font_sec)
    draw.text((1008, 105), "Sequência fisiológica pós-parto e critérios de normalidade", fill="#64748b", font=font_sec_sub)

    # 6. Left Column Annotations (Sagittal Pelvic Cut)
    # Cicatriz Umbilical Callout
    draw.rounded_rectangle([310, 222, 442, 262], radius=6, fill="#f8fafc", outline="#94a3b8", width=1)
    draw.text((376, 234), "Cicatriz Umbilical", fill="#0f172a", font=font_body_b, anchor="mm")
    draw.text((376, 249), "Marco de referência zero", fill="#64748b", font=font_body_sm, anchor="mm")
    draw.line([(442, 242), (448, 293)], fill="#334155", width=1)

    # Dashed line from umbilical black dot (448, 293) across to u1 fundus at (478, 293)
    dash_x = 448
    while dash_x < 535:
        draw.line([(dash_x, 293), (dash_x + 5, 293)], fill="#475569", width=2)
        dash_x += 8

    # Descent badge inside pelvis
    draw.rounded_rectangle([250, 412, 350, 442], radius=5, fill="#ffffff", outline="#cbd5e1", width=1)
    draw.text((300, 420), "Descida pélvica", fill="#0f172a", font=font_body_sm_b, anchor="mm")
    draw.text((300, 433), "(~1 cm a cada 24h)", fill="#64748b", font=font_body_sm, anchor="mm")

    # Sínfise Púbica Callout (Expanded box with optimal breathing room)
    draw.rounded_rectangle([295, 700, 445, 746], radius=6, fill="#f8fafc", outline="#94a3b8", width=1)
    draw.text((370, 714), "Sínfise Púbica (SP)", fill="#0f172a", font=font_body_b, anchor="mm")
    draw.text((370, 732), "Retorno intrapélvico (Dia 10–12)", fill="#64748b", font=font_body_sm, anchor="mm")
    draw.line([(370, 700), (370, 665)], fill="#334155", width=1)

    # 7. Center Column: Cards for the 5 Milestones of Uterine Involution
    def draw_card(box, header_text, header_bg, title, bullets, border_color="#cbd5e1", bg_color="#ffffff", line_spacing=13):
        x1, y1, x2, y2 = box
        draw.rounded_rectangle([x1, y1, x2, y2], radius=7, fill=bg_color, outline=border_color, width=1)
        # Header pill
        draw.rounded_rectangle([x1 + 6, y1 + 6, x2 - 6, y1 + 25], radius=4, fill=header_bg)
        draw.text(((x1 + x2) // 2, y1 + 15), header_text, fill="#ffffff", font=font_badge_sm, anchor="mm")
        # Title
        draw.text((x1 + 10, y1 + 33), title, fill="#0f172a", font=font_body_b)
        # Bullets
        cur_y = y1 + 49
        for b in bullets:
            draw.text((x1 + 10, cur_y), b, fill="#334155", font=font_body_sm)
            cur_y += line_spacing

    # Milestone 1: Pós-Parto Imediato / 1º Dia (Above u1)
    draw_card(
        [455, 130, 630, 268],
        "1º DIA PÓS-PARTO (DIA 0 - 1)",
        "#0284c7",
        "Ao Nível da Cicatriz Umbilical",
        [
            "• Globo de Segurança de Pinard",
            "• Contração miometrial tônica",
            "• Peso uterino: ~1.000 g",
            "• Fundo na cicatriz umbilical (linha)",
            "• Colo hipotônico e pérvio (2 dedos)"
        ],
        border_color="#38bdf8"
    )

    # Milestone 2: 2º ao 6º Dia (Above u2)
    draw_card(
        [770, 130, 975, 268],
        "2º AO 6º DIA PÓS-PARTO",
        "#0369a1",
        "Involução Miometrial Ativa",
        [
            "• Fundo 2 a 5 cm abaixo do umbigo",
            "• Involução diária: ~1 cm a cada 24h",
            "• Miométrio firme e espesso",
            "• Peso uterino: ~700 a 800 g",
            "• Rápida redução da cavidade"
        ],
        border_color="#38bdf8"
    )

    # Transition Arrow 1 -> 2
    draw.line([(635, 360), (765, 360)], fill="#64748b", width=2)
    draw.polygon([(765, 355), (775, 360), (765, 365)], fill="#64748b")
    draw.text((700, 348), "Regressão ~1 cm/dia", fill="#64748b", font=font_body_sm, anchor="mm")

    # Milestone 3: Marco do 7º Dia (Callout Card at x: 450..595, y: 492..758)
    draw_card(
        [450, 492, 595, 758],
        "MARCO DO 7º DIA",
        "#b45309",
        "Meia Distância Umbigo-Púbis",
        [
            "• Fundo uterino exatamente",
            "  à meia distância entre",
            "  o umbigo e a sínfise",
            "  púbica (~10 cm da SP).",
            "",
            "• Marco semiológico clássico",
            "  de Pinard para detecção",
            "  de subinvolução uterina.",
            "",
            "• Se o fundo mantiver-se no",
            "  umbigo: suspeitar de atonia,",
            "  restos ovulares ou infecção!"
        ],
        border_color="#f59e0b",
        bg_color="#fffbeb",
        line_spacing=13
    )

    # Milestone 4: 10º ao 12º Dia (Below u3)
    draw_card(
        [605, 646, 775, 758],
        "10º AO 12º DIA",
        "#0d9488",
        "Retorno Intrapélvico",
        [
            "• Nível da sínfise púbica",
            "• Não palpável pelo abdome",
            "• Peso uterino: ~500 g",
            "• Orifício interno fechado"
        ],
        border_color="#14b8a6",
        line_spacing=12
    )

    # Milestone 5: 6ª Semana (Below u4)
    draw_card(
        [785, 646, 975, 758],
        "6ª SEMANA (42 DIAS)",
        "#7c3aed",
        "Tamanho Pré-Gravídico",
        [
            "• Retorno às dimensões basais",
            "• Peso final: ~60 a 70 g",
            "• Cavidade virtual restaurada",
            "• Término do puerpério tardio"
        ],
        border_color="#a855f7",
        line_spacing=12
    )

    # Transition Arrow 4 -> 5
    draw.line([(775, 560), (795, 560)], fill="#64748b", width=2)
    draw.polygon([(795, 555), (803, 560), (795, 565)], fill="#64748b")

    # Downward transition arrow from Row 1 to Row 2
    draw.line([(880, 480), (880, 490)], fill="#64748b", width=2)

    # 8. Right Column: Lochia Cards & Specimen Explanations
    def draw_lochia_card_v2(box, num_title, phase_badge, badge_bg, badge_fg, aspect_bold, bullets, border_col):
        x1, y1, x2, y2 = box
        draw.rounded_rectangle([x1, y1, x2, y2], radius=6, fill="#ffffff", outline=border_col, width=1)
        # Title (Full width on top line)
        draw.text((x1 + 10, y1 + 7), num_title, fill="#0f172a", font=font_body_b)
        # Phase badge on second line
        badge_w = int(draw.textlength(phase_badge, font=font_badge_sm)) + 14
        draw.rounded_rectangle([x1 + 10, y1 + 24, x1 + 10 + badge_w, y1 + 39], radius=3, fill=badge_bg)
        draw.text((x1 + 10 + badge_w // 2, y1 + 31), phase_badge, fill=badge_fg, font=font_badge_sm, anchor="mm")
        # Aspect line
        draw.text((x1 + 10, y1 + 45), "Aspecto:", fill="#64748b", font=font_body_sm_b)
        draw.text((x1 + 58, y1 + 45), aspect_bold, fill="#0f172a", font=font_body_b)
        # Bullets
        cur_y = y1 + 61
        for label, val in bullets:
            draw.text((x1 + 10, cur_y), label, fill="#64748b", font=font_body_sm_b)
            lbl_w = int(draw.textlength(label, font=font_body_sm_b))
            draw.text((x1 + 12 + lbl_w, cur_y), val, fill="#334155", font=font_body_sm)
            cur_y += 14

    # Lóquios Rubros (y: 135 to 308)
    draw_lochia_card_v2(
        [1125, 136, 1365, 308],
        "1. LÓQUIOS RUBROS (CRUENTOS)",
        "Fase Hemática • Dias 1 a 3 pós-parto",
        "#fee2e2",
        "#991b1b",
        "Vermelho-vivo a escuro",
        [
            ("Composição:", "Sangue, restos deciduais e muco."),
            ("Odor:", "Sui generis (sem fetidez / patologia)."),
            ("Volume:", "Abundante (diminui ao amamentar)."),
            ("Nota:", "Pequenos grumos deciduais são normais.")
        ],
        border_col="#ef4444"
    )

    # Downward arrow between Cup 1 and Cup 2
    draw.line([(1065, 305), (1065, 345)], fill="#78350f", width=3)
    draw.polygon([(1059, 345), (1065, 353), (1071, 345)], fill="#78350f")

    # Lóquios Serosos (y: 338 to 510)
    draw_lochia_card_v2(
        [1125, 338, 1365, 510],
        "2. LÓQUIOS SEROSOS",
        "Fase Serossanguínea • Dias 4 a 10 pós-parto",
        "#ffedd5",
        "#9a3412",
        "Rosado a castanho-claro",
        [
            ("Composição:", "Exsudato seroso, leucócitos, hemácias."),
            ("Evolução:", "Queda acentuada de eritrócitos íntegros."),
            ("Odor:", "Característico (odor fétido = endometrite!)."),
            ("Volume:", "Moderado a escasso, consistência fluida.")
        ],
        border_col="#f97316"
    )

    # Downward arrow between Cup 2 and Cup 3
    draw.line([(1065, 525), (1065, 565)], fill="#475569", width=3)
    draw.polygon([(1059, 565), (1065, 573), (1071, 565)], fill="#475569")

    # Lóquios Alba (y: 538 to 698)
    draw_lochia_card_v2(
        [1125, 538, 1365, 698],
        "3. LÓQUIOS ALBA (BRANCOS)",
        "Fase Leucocitária • Dia 10 à 3ª–6ª semana",
        "#f1f5f9",
        "#334155",
        "Esbranquiçado / amarelado",
        [
            ("Composição:", "Leucócitos, muco, células epiteliais."),
            ("Característica:", "Ausência total de hemácias íntegras."),
            ("Duração:", "Decrescente até cessação completa.")
        ],
        border_col="#94a3b8"
    )

    # 9. Alert Box at Bottom Right (y: 706 to 756, x: 1005 to 1365)
    draw.rounded_rectangle([1005, 706, 1365, 756], radius=6, fill="#fef2f2", outline="#ef4444", width=2)
    draw.text((1018, 716), "SINAIS DE ALERTA NO PUERPÉRIO (SUS / FEBRASGO):", fill="#991b1b", font=font_alert_b)
    draw.text((1018, 732), "• Odor fétido (Endometrite) • Lóquios rubros persistentes >4º dia • Febre puerperal (≥38°C)", fill="#b91c1c", font=font_alert)

    # Save output directly to site assets and artifact directory
    final_cv2 = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

    site_target = r"c:\Users\Admin\Downloads\INTERNATO GO\site_parto_puerperio\assets\img\involucao_uterina_loquios.jpg"
    cv2.imwrite(site_target, final_cv2, [cv2.IMWRITE_JPEG_QUALITY, 96])
    print("Saved to site target:", site_target)

    artifact_target = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34\involucao_uterina_loquios_pt.jpg"
    cv2.imwrite(artifact_target, final_cv2, [cv2.IMWRITE_JPEG_QUALITY, 96])
    print("Saved to artifact target:", artifact_target)

if __name__ == "__main__":
    create_diagram()
