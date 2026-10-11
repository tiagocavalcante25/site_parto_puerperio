# -*- coding: utf-8 -*-
"""
High-Precision Official Brazilian Ministry of Health / SUS Partograph Diagram - Perfected Version 3
Layout: Ministério da Saúde do Brasil / SUS / FEBRASGO / OMS
100% in Brazilian Portuguese, ultra-sharp vector-grade grid, authentic clinical typography.
Zero overlaps, zero English text, pristine institutional quality.
"""
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def get_font(name_or_size, size=None):
    if size is None:
        size = name_or_size
        name = "segoeui.ttf"
    else:
        name = name_or_size
    font_paths = [
        os.path.join(r"C:\Windows\Fonts", name),
        os.path.join(r"C:\Windows\Fonts", "arial.ttf" if "bd" not in name else "arialbd.ttf"),
        os.path.join(r"C:\Windows\Fonts", "calibri.ttf")
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except:
                pass
    return ImageFont.load_default()

def draw_hatch(draw, x1, y1, x2, y2, mode="weak"):
    if mode == "weak":
        draw.rectangle([x1, y1, x2, y2], fill="#f8fafc", outline="#94a3b8")
        step = 6
        for y in range(int(y1) + 3, int(y2) - 2, step):
            for x in range(int(x1) + 3, int(x2) - 2, step):
                draw.rectangle([x, y, x + 1, y + 1], fill="#64748b")
    elif mode == "mod":
        draw.rectangle([x1, y1, x2, y2], fill="#f1f5f9", outline="#64748b")
        step = 6
        x1_i, y1_i, x2_i, y2_i = int(x1), int(y1), int(x2), int(y2)
        h = y2_i - y1_i
        w = x2_i - x1_i
        for d in range(-h, w + h, step):
            px1 = max(x1_i, min(x2_i, x1_i + d))
            py1 = min(y2_i, max(y1_i, y2_i - (px1 - (x1_i + d))))
            px2 = max(x1_i, min(x2_i, x1_i + d + h))
            py2 = max(y1_i, min(y2_i, y1_i + (px2 - (x1_i + d + h))))
            draw.line([(px1, y2_i), (px2, y1_i)], fill="#334155", width=1)
    elif mode == "strong":
        draw.rectangle([x1, y1, x2, y2], fill="#0f766e", outline="#042f2e")

def build_partograma():
    target_img = r"c:\Users\Admin\Downloads\INTERNATO GO\site_parto_puerperio\assets\img\partograma_oms_curvas.jpg"
    W, H = 1600, 915

    img = Image.new("RGB", (W, H), "#ffffff")
    draw = ImageDraw.Draw(img)

    # Fonts
    f_main_title = get_font("segoeuib.ttf", 17)
    f_hdr_bold = get_font("segoeuib.ttf", 11)
    f_grid_num = get_font("segoeuib.ttf", 10)
    f_lbl_title = get_font("segoeuib.ttf", 11)
    f_lbl_sm = get_font("segoeui.ttf", 9)
    f_legend = get_font("segoeuib.ttf", 10)

    # 1. INSTITUTIONAL TOP BANNER (SUS / MINISTÉRIO DA SAÚDE)
    draw.rectangle([15, 10, W - 15, 68], fill="#0f766e")
    # Left Emblem Badge: SUS
    draw.rounded_rectangle([25, 17, 115, 61], radius=6, fill="#ffffff")
    draw.text((70, 39), "SUS", fill="#005bac", font=get_font("arialbd.ttf", 22), anchor="mm")
    
    # Institution Text Left
    draw.text((128, 28), "MINISTÉRIO DA SAÚDE DO BRASIL", fill="#ffffff", font=get_font("segoeuib.ttf", 13), anchor="lm")
    draw.text((128, 46), "Secretaria de Atenção Primária e Especializada • Diretrizes Nacionais", fill="#ccfbf1", font=get_font("segoeui.ttf", 10), anchor="lm")

    # Center Title
    draw.text((W / 2 + 50, 27), "PARTOGRAMA OFICIAL (MODELO OMS / MINISTÉRIO DA SAÚDE)", fill="#ffffff", font=f_main_title, anchor="mm")
    draw.text((W / 2 + 50, 48), "REGISTRO GRÁFICO DA ASSISTÊNCIA AO TRABALHO DE PARTO • VIGILÂNCIA FETOMATERNA", fill="#fef08a", font=get_font("segoeuib.ttf", 11), anchor="mm")

    # Right Badge
    draw.rounded_rectangle([W - 195, 17, W - 25, 61], radius=6, fill="#042f2e")
    draw.text((W - 110, 29), "FEBRASGO / MS", fill="#ffffff", font=get_font("segoeuib.ttf", 12), anchor="mm")
    draw.text((W - 110, 47), "PADRÃO OURO", fill="#5eead4", font=get_font("segoeuib.ttf", 10), anchor="mm")

    # 2. PATIENT IDENTIFICATION STRIP
    y_pat = 74
    h_pat = 42
    draw.rectangle([15, y_pat, W - 15, y_pat + h_pat], fill="#f8fafc", outline="#cbd5e1", width=1)
    
    draw.text((25, y_pat + 12), "Nome da Parturiente:", fill="#64748b", font=f_hdr_bold)
    draw.text((150, y_pat + 12), "Maria Silva Santos", fill="#0f172a", font=f_hdr_bold)
    
    draw.text((360, y_pat + 12), "Prontuário / CNS:", fill="#64748b", font=f_hdr_bold)
    draw.text((475, y_pat + 12), "894.201-5", fill="#0f172a", font=f_hdr_bold)

    draw.text((580, y_pat + 12), "Idade:", fill="#64748b", font=f_hdr_bold)
    draw.text((625, y_pat + 12), "24 anos", fill="#0f172a", font=f_hdr_bold)

    draw.text((710, y_pat + 12), "Paridade:", fill="#64748b", font=f_hdr_bold)
    draw.text((775, y_pat + 12), "G2 P1 (1 Parto Normal anterior) A0", fill="#0f172a", font=f_hdr_bold)

    draw.text((1050, y_pat + 12), "Data Internação:", fill="#64748b", font=f_hdr_bold)
    draw.text((1155, y_pat + 12), "04/10/2026 às 07:30", fill="#0f172a", font=f_hdr_bold)

    draw.text((25, y_pat + 27), "Hora Início Fase Ativa:", fill="#64748b", font=f_hdr_bold)
    draw.text((165, y_pat + 27), "08:00h (4 cm)", fill="#0f766e", font=f_hdr_bold)

    draw.text((360, y_pat + 27), "Membranas / Bolsa:", fill="#64748b", font=f_hdr_bold)
    draw.text((485, y_pat + 27), "Rota Espontânea às 08:30 (Líquido Claro)", fill="#0f766e", font=f_hdr_bold)

    draw.text((820, y_pat + 27), "Apresentação Fetal:", fill="#64748b", font=f_hdr_bold)
    draw.text((945, y_pat + 27), "Cefálica Fletida (Vértice)", fill="#0f172a", font=f_hdr_bold)

    draw.text((1150, y_pat + 27), "Posição:", fill="#64748b", font=f_hdr_bold)
    draw.text((1205, y_pat + 27), "OEA (Occipito Esquerda Anterior)", fill="#0f172a", font=f_hdr_bold)

    # 3. GRAPH GRID GEOMETRY
    x_start = 220
    x_end = 1440
    total_w = x_end - x_start  # 1220 px
    n_hours = 12
    col_w = total_w / n_hours  # 101.66 px per hour
    subcol_w = col_w / 2       # 50.83 px per 30 min (24 columns)

    # SECTION 1: FREQUÊNCIA CARDÍACA FETAL (FCF)
    y_fcf_top = 122
    y_fcf_bot = 208
    h_fcf = y_fcf_bot - y_fcf_top  # 86 px
    
    draw.rectangle([15, y_fcf_top, x_start - 2, y_fcf_bot], fill="#f0fdfa", outline="#cbd5e1")
    draw.text((105, y_fcf_top + 15), "BATIMENTOS", fill="#0f766e", font=get_font("segoeuib.ttf", 11), anchor="mm")
    draw.text((105, y_fcf_top + 30), "CARDIOFETAIS", fill="#0f766e", font=get_font("segoeuib.ttf", 11), anchor="mm")
    draw.text((105, y_fcf_top + 48), "FCF / BCF (bpm)", fill="#1e293b", font=get_font("segoeuib.ttf", 13), anchor="mm")
    draw.text((105, y_fcf_top + 68), "Normal: 110 - 160", fill="#059669", font=get_font("segoeuib.ttf", 10), anchor="mm")

    draw.rectangle([x_start, y_fcf_top, x_end, y_fcf_bot], fill="#ffffff", outline="#94a3b8")
    
    def fcf_to_y(bpm):
        return y_fcf_bot - ((bpm - 100) / 80.0) * h_fcf

    y_110 = fcf_to_y(110)
    y_160 = fcf_to_y(160)
    draw.rectangle([x_start, y_160, x_end, y_110], fill="#f0fdf4") # soft green safe band

    for bpm in [100, 110, 120, 140, 160, 180]:
        y_val = fcf_to_y(bpm)
        line_color = "#86efac" if bpm in [110, 160] else "#e2e8f0"
        line_w = 2 if bpm in [110, 160] else 1
        draw.line([(x_start, y_val), (x_end, y_val)], fill=line_color, width=line_w)
        draw.text((x_start - 6, y_val), str(bpm), fill="#64748b" if bpm not in [110, 160] else "#059669", font=get_font("segoeuib.ttf", 9), anchor="rm")

    # SECTION 2: LÍQUIDO AMNIÓTICO & CAVALGAMENTO (MOLDAGEM)
    y_la_top = 212
    y_la_bot = 252
    draw.rectangle([15, y_la_top, x_start - 2, y_la_top + 20], fill="#f8fafc", outline="#cbd5e1")
    draw.text((105, y_la_top + 10), "Líquido Amniótico (LA)", fill="#334155", font=f_lbl_title, anchor="mm")
    
    draw.rectangle([15, y_la_top + 20, x_start - 2, y_la_bot], fill="#f8fafc", outline="#cbd5e1")
    draw.text((105, y_la_top + 30), "Moldagem / Cavalgamento", fill="#334155", font=f_lbl_title, anchor="mm")

    draw.rectangle([x_start, y_la_top, x_end, y_la_top + 20], fill="#ffffff", outline="#94a3b8")
    draw.rectangle([x_start, y_la_top + 20, x_end, y_la_bot], fill="#ffffff", outline="#94a3b8")

    # DEDICATED HOUR HEADER BAR (BETWEEN LA AND MAIN GRID)
    y_hr_top = 256
    y_hr_bot = 282
    draw.rectangle([15, y_hr_top, x_start - 2, y_hr_bot], fill="#f1f5f9", outline="#cbd5e1")
    draw.text((105, y_hr_top + 13), "Tempo de Parto (Horas)", fill="#0f766e", font=get_font("segoeuib.ttf", 10), anchor="mm")
    draw.rectangle([x_start, y_hr_top, x_end, y_hr_bot], fill="#f1f5f9", outline="#94a3b8")

    # SECTION 3: CORE GRAPH (DILATAÇÃO CERVICAL & DESCIDA FETAL)
    y_grid_top = 286
    y_grid_bot = 606
    h_grid = y_grid_bot - y_grid_top # 320 px (32 px per cm)

    # Left Y-Axis Header Box
    draw.rectangle([15, y_grid_top, x_start - 2, y_grid_bot], fill="#f8fafc", outline="#cbd5e1")
    draw.text((105, y_grid_top + 25), "DILATAÇÃO", fill="#0f766e", font=get_font("segoeuib.ttf", 14), anchor="mm")
    draw.text((105, y_grid_top + 45), "CERVICAL (cm)", fill="#0f766e", font=get_font("segoeuib.ttf", 14), anchor="mm")
    draw.text((105, y_grid_top + 75), "Símbolo Oficial:", fill="#64748b", font=f_lbl_sm, anchor="mm")
    draw.text((105, y_grid_top + 98), "▲ (Triângulo)", fill="#0f172a", font=get_font("segoeuib.ttf", 12), anchor="mm")
    draw.text((105, y_grid_top + 135), "Velocidade Mínima", fill="#64748b", font=f_lbl_sm, anchor="mm")
    draw.text((105, y_grid_top + 150), "Esperada:", fill="#64748b", font=f_lbl_sm, anchor="mm")
    draw.text((105, y_grid_top + 170), "≥ 1 cm / hora", fill="#0f766e", font=get_font("segoeuib.ttf", 12), anchor="mm")
    draw.text((105, y_grid_top + 190), "(Fase Ativa)", fill="#0f766e", font=f_lbl_sm, anchor="mm")

    # Right Y-Axis Header Box (Planos de De Lee)
    draw.rectangle([x_end + 35, y_grid_top, W - 15, y_grid_bot], fill="#f8fafc", outline="#cbd5e1")
    draw.text((W - 75, y_grid_top + 30), "ALTURA DA", fill="#0f766e", font=get_font("segoeuib.ttf", 13), anchor="mm")
    draw.text((W - 75, y_grid_top + 50), "APRESENTAÇÃO", fill="#0f766e", font=get_font("segoeuib.ttf", 13), anchor="mm")
    draw.text((W - 75, y_grid_top + 70), "(Planos De Lee)", fill="#0f766e", font=get_font("segoeuib.ttf", 11), anchor="mm")
    draw.text((W - 75, y_grid_top + 105), "Símbolo Oficial:", fill="#64748b", font=f_lbl_sm, anchor="mm")
    draw.text((W - 75, y_grid_top + 125), "○ (Círculo)", fill="#0f172a", font=get_font("segoeuib.ttf", 12), anchor="mm")
    draw.text((W - 75, y_grid_top + 165), "Plano 0 =", fill="#64748b", font=f_lbl_sm, anchor="mm")
    draw.text((W - 75, y_grid_top + 185), "Espinhas", fill="#1e293b", font=get_font("segoeuib.ttf", 11), anchor="mm")
    draw.text((W - 75, y_grid_top + 203), "Isquiáticas", fill="#1e293b", font=get_font("segoeuib.ttf", 11), anchor="mm")
    draw.text((W - 75, y_grid_top + 225), "(Insinuação)", fill="#0f766e", font=f_lbl_sm, anchor="mm")

    # Main Grid Background
    draw.rectangle([x_start, y_grid_top, x_end, y_grid_bot], fill="#ffffff", outline="#475569", width=2)

    # SECTION 4: DINÂMICA UTERINA (CONTRAÇÕES / 10 MIN)
    y_du_top = 612
    y_du_bot = 692
    h_du = y_du_bot - y_du_top # 80 px (5 rows of 16 px)
    draw.rectangle([15, y_du_top, x_start - 2, y_du_bot], fill="#f8fafc", outline="#cbd5e1")
    draw.text((105, y_du_top + 18), "DINÂMICA UTERINA", fill="#0f766e", font=get_font("segoeuib.ttf", 12), anchor="mm")
    draw.text((105, y_du_top + 34), "Contrações / 10 min", fill="#1e293b", font=get_font("segoeuib.ttf", 11), anchor="mm")
    draw.text((105, y_du_top + 55), "1 a 5 contrações", fill="#64748b", font=f_lbl_sm, anchor="mm")

    draw.rectangle([x_start, y_du_top, x_end, y_du_bot], fill="#ffffff", outline="#94a3b8")

    # SECTION 5: OCITOCINA & MEDICAÇÃO
    y_med_top = 696
    y_med_bot = 736
    draw.rectangle([15, y_med_top, x_start - 2, y_med_top + 20], fill="#f8fafc", outline="#cbd5e1")
    draw.text((105, y_med_top + 10), "Ocitocina (gotas/min)", fill="#334155", font=f_lbl_title, anchor="mm")
    
    draw.rectangle([15, y_med_top + 20, x_start - 2, y_med_bot], fill="#f8fafc", outline="#cbd5e1")
    draw.text((105, y_med_top + 30), "Medicamentos e Fluidos IV", fill="#334155", font=f_lbl_title, anchor="mm")

    draw.rectangle([x_start, y_med_top, x_end, y_med_top + 20], fill="#ffffff", outline="#94a3b8")
    draw.rectangle([x_start, y_med_top + 20, x_end, y_med_bot], fill="#ffffff", outline="#94a3b8")

    # SECTION 6: SINAIS VITAIS MATERNOS
    y_vit_top = 740
    y_vit_bot = 820
    draw.rectangle([15, y_vit_top, x_start - 2, y_vit_bot], fill="#f8fafc", outline="#cbd5e1")
    draw.text((105, y_vit_top + 16), "SINAIS VITAIS", fill="#0f766e", font=get_font("segoeuib.ttf", 12), anchor="mm")
    draw.text((105, y_vit_top + 32), "MATERNOS", fill="#0f766e", font=get_font("segoeuib.ttf", 12), anchor="mm")
    draw.text((105, y_vit_top + 50), "PA: ↕ (mmHg)", fill="#dc2626", font=get_font("segoeuib.ttf", 10), anchor="mm")
    draw.text((105, y_vit_top + 65), "Pulso: ● (bpm)", fill="#0284c7", font=get_font("segoeuib.ttf", 10), anchor="mm")

    draw.rectangle([x_start, y_vit_top, x_end, y_vit_bot], fill="#ffffff", outline="#94a3b8")

    # -------------------------------------------------------------
    # DRAW GRID LINES & COLUMNS
    # -------------------------------------------------------------
    for c in range(25):
        xc = x_start + c * subcol_w
        is_hour = (c % 2 == 0)
        line_color = "#94a3b8" if is_hour else "#e2e8f0"
        line_width = 2 if is_hour else 1
        
        # Grid vertical lines in all sections
        draw.line([(xc, y_fcf_top), (xc, y_fcf_bot)], fill=line_color, width=line_width)
        draw.line([(xc, y_la_top), (xc, y_la_bot)], fill=line_color, width=line_width)
        draw.line([(xc, y_hr_top), (xc, y_hr_bot)], fill=line_color, width=line_width)
        draw.line([(xc, y_grid_top), (xc, y_grid_bot)], fill=line_color, width=line_width)
        draw.line([(xc, y_du_top), (xc, y_du_bot)], fill=line_color, width=line_width)
        draw.line([(xc, y_med_top), (xc, y_med_bot)], fill=line_color, width=line_width)
        draw.line([(xc, y_vit_top), (xc, y_vit_bot)], fill=line_color, width=line_width)

        # Hour labels inside dedicated bar: H1 + (08:00)
        if is_hour and c < 24:
            hr_val = c // 2
            clock_h = 8 + hr_val
            draw.text((xc + col_w / 2, y_hr_top + 7), f"H{hr_val + 1}", fill="#0f766e", font=get_font("segoeuib.ttf", 9), anchor="mm")
            draw.text((xc + col_w / 2, y_hr_top + 19), f"{clock_h:02d}:00", fill="#475569", font=get_font("segoeui.ttf", 8), anchor="mm")

    # Horizontal Lines in Core Grid (Dilatação: 0 to 10 cm)
    for cm in range(11):
        yc = y_grid_bot - cm * 32.0
        draw.line([(x_start, yc), (x_end, yc)], fill="#cbd5e1" if cm not in [0, 4, 10] else "#64748b", width=2 if cm in [0, 4, 10] else 1)
        # Left label (cm)
        draw.text((x_start - 10, yc), f"{cm} cm", fill="#0f172a" if cm in [4, 10] else "#475569", font=get_font("segoeuib.ttf", 10) if cm in [4, 10] else get_font("segoeui.ttf", 10), anchor="rm")
        
        # Right label (Planos de De Lee) placed in dedicated gutter x_end + 6 to x_end + 32
        de_lee_map = {10: "+3", 9: "+2", 8: "+1", 7: " 0", 6: "-1", 5: "-2", 4: "-3", 3: "-4", 2: "", 1: "", 0: ""}
        dl_num = de_lee_map.get(cm, "")
        if dl_num:
            draw.text((x_end + 8, yc), dl_num, fill="#0f766e" if "0" in dl_num or "+3" in dl_num else "#334155", font=get_font("segoeuib.ttf", 11) if "0" in dl_num else get_font("segoeui.ttf", 10), anchor="lm")

    # Contractions horizontal grid (1 to 5)
    for k in range(1, 6):
        yc = y_du_bot - k * 16.0
        draw.line([(x_start, yc), (x_end, yc)], fill="#cbd5e1", width=1)
        draw.text((x_start - 6, yc + 8), str(k), fill="#64748b", font=get_font("segoeuib.ttf", 9), anchor="rm")

    # -------------------------------------------------------------
    # DRAW LINHA DE ALERTA & LINHA DE AÇÃO
    # -------------------------------------------------------------
    # Starts at 4 cm, Hour 4
    x_alerta_start = x_start + 4 * col_w
    y_alerta_start = y_grid_bot - 4 * 32.0 # 4 cm
    x_alerta_end = x_start + 10 * col_w
    y_alerta_end = y_grid_bot - 10 * 32.0  # 10 cm

    # Action line: 4 hours to the right
    x_acao_start = x_start + 8 * col_w
    y_acao_start = y_grid_bot - 4 * 32.0   # 4 cm
    x_acao_end = x_end                     # clamps strictly at grid border x_end
    y_acao_end = y_acao_start - 4 * 32.0   # 8 cm at hour 12

    # Clamped Shaded Area between Alert and Action lines
    poly_pts = [
        (x_alerta_start, y_alerta_start),
        (x_alerta_end, y_alerta_end),
        (x_end, y_alerta_end),
        (x_acao_end, y_acao_end),
        (x_acao_start, y_acao_start)
    ]
    poly_overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    poly_draw = ImageDraw.Draw(poly_overlay)
    poly_draw.polygon(poly_pts, fill=(254, 240, 138, 65))
    img.paste(Image.alpha_composite(img.convert("RGBA"), poly_overlay).convert("RGB"))
    draw = ImageDraw.Draw(img)

    # Draw crisp Alert and Action Lines
    draw.line([(x_alerta_start, y_alerta_start), (x_alerta_end, y_alerta_end)], fill="#d97706", width=4)
    draw.line([(x_acao_start, y_acao_start), (x_acao_end, y_acao_end)], fill="#dc2626", width=4)

    # Alert Label
    draw.rectangle([x_alerta_start + 110, y_alerta_start - 130, x_alerta_start + 290, y_alerta_start - 106], fill="#fef3c7", outline="#d97706", width=1)
    draw.text((x_alerta_start + 200, y_alerta_start - 118), "LINHA DE ALERTA (1 cm/h)", fill="#b45309", font=get_font("segoeuib.ttf", 10), anchor="mm")

    # Action Label
    draw.rectangle([x_acao_start + 90, y_acao_start - 80, x_acao_start + 295, y_acao_start - 56], fill="#fee2e2", outline="#dc2626", width=1)
    draw.text((x_acao_start + 192, y_acao_start - 68), "LINHA DE AÇÃO (Alerta + 4h)", fill="#b91c1c", font=get_font("segoeuib.ttf", 10), anchor="mm")

    # -------------------------------------------------------------
    # DRAW CLINICAL DATA: DILATAÇÃO (▲) & DESCIDA (○)
    # -------------------------------------------------------------
    dilat_pts = [
        (0.0, 3.0),
        (2.0, 3.0),
        (4.0, 4.0),
        (6.0, 6.2),
        (8.0, 8.5),
        (9.5, 10.0)
    ]
    descent_pts = [
        (0.0, 5.0), # Plano -2
        (2.0, 5.0), # Plano -2
        (4.0, 6.0), # Plano -1
        (6.0, 7.0), # Plano 0 (Insinuado)
        (8.0, 8.5), # Plano +1.5
        (9.5, 10.0) # Plano +3 (Desprendimento)
    ]

    px_dilat = [(x_start + h * col_w, y_grid_bot - d * 32.0) for (h, d) in dilat_pts]
    px_desc = [(x_start + h * col_w, y_grid_bot - (p - 0.0) * 32.0) for (h, p) in descent_pts]

    # Draw continuous Dilatation Curve line (Dark Blue / Teal)
    draw.line(px_dilat, fill="#0f766e", width=3)
    # Draw dashed Descent Curve line
    for i in range(len(px_desc) - 1):
        p1, p2 = px_desc[i], px_desc[i+1]
        draw.line([p1, p2], fill="#475569", width=2)

    # Plot Dilatation Triangles ▲
    for (px, py) in px_dilat:
        r = 7
        draw.polygon([(px, py - r), (px - r, py + r), (px + r, py + r)], fill="#0f766e", outline="#042f2e")

    # Plot Descent Circles ○
    for (px, py) in px_desc:
        r = 6
        draw.ellipse([px - r, py - r, px + r, py + r], fill="#ffffff", outline="#1e293b", width=2)

    # -------------------------------------------------------------
    # DRAW FCF TRACE (DOTS + LINE)
    # -------------------------------------------------------------
    fcf_data = [
        (0.0, 138), (0.5, 140), (1.0, 142), (1.5, 136), (2.0, 134), (2.5, 138),
        (3.0, 140), (3.5, 135), (4.0, 142), (4.5, 140), (5.0, 145), (5.5, 138),
        (6.0, 140), (6.5, 144), (7.0, 138), (7.5, 142), (8.0, 136), (8.5, 140),
        (9.0, 134), (9.5, 130)
    ]
    px_fcf = [(x_start + h * col_w, fcf_to_y(bpm)) for (h, bpm) in fcf_data]
    draw.line(px_fcf, fill="#0284c7", width=2)
    for (px, py) in px_fcf:
        draw.ellipse([px - 3, py - 3, px + 3, py + 3], fill="#0369a1", outline="#082f49")

    # -------------------------------------------------------------
    # DRAW LIQUIDO AMNIOTICO & CAVALGAMENTO DATA
    # -------------------------------------------------------------
    la_vals = ["I", "I", "I", "I", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C"]
    mould_vals = ["0", "0", "0", "0", "0", "0", "+", "+", "+", "+", "+", "+", "+", "+", "+", "++", "++", "++", "++", "++"]
    for idx, (la, mld) in enumerate(zip(la_vals, mould_vals)):
        xc = x_start + idx * subcol_w + subcol_w / 2
        draw.text((xc, y_la_top + 10), la, fill="#0f766e" if la == "C" else "#475569", font=get_font("segoeuib.ttf", 10), anchor="mm")
        draw.text((xc, y_la_top + 30), mld, fill="#b45309" if "++" in mld else "#475569", font=get_font("segoeuib.ttf", 10), anchor="mm")

    # -------------------------------------------------------------
    # DRAW DINÂMICA UTERINA (CONTRAÇÕES COM HACHURAS DO MS/SUS)
    # -------------------------------------------------------------
    for col_idx in range(20):
        xc1 = x_start + col_idx * subcol_w + 2
        xc2 = xc1 + subcol_w - 4
        
        if col_idx < 4:
            n_c = 2
            modes = ["weak", "weak"]
        elif col_idx < 8:
            n_c = 3
            modes = ["mod", "mod", "weak"]
        elif col_idx < 14:
            n_c = 4
            modes = ["strong", "mod", "mod", "mod"]
        else:
            n_c = 5
            modes = ["strong", "strong", "strong", "strong", "strong"]

        for k in range(n_c):
            yc2 = y_du_bot - k * 16.0 - 2
            yc1 = yc2 - 12
            draw_hatch(draw, int(xc1), int(yc1), int(xc2), int(yc2), mode=modes[k])

    # -------------------------------------------------------------
    # DRAW OCITOCINA & MEDICAÇÃO
    # -------------------------------------------------------------
    for col_idx in range(20):
        xc = x_start + col_idx * subcol_w + subcol_w / 2
        oxi_txt = "-" if col_idx < 8 else ("4" if col_idx < 12 else "8")
        draw.text((xc, y_med_top + 10), oxi_txt, fill="#0f766e" if oxi_txt != "-" else "#94a3b8", font=get_font("segoeuib.ttf", 9), anchor="mm")
    
    draw.text((x_start + 10, y_med_top + 30), "Soro Ringer Lactato 500 mL IV  |  Analgesia de Parto solicitada e instalada às 12:30", fill="#1e293b", font=get_font("segoeui.ttf", 10), anchor="lm")

    # -------------------------------------------------------------
    # DRAW SINAIS VITAIS MATERNOS
    # -------------------------------------------------------------
    bp_data = [
        (0.0, 120, 80, 76),
        (2.0, 120, 80, 78),
        (4.0, 115, 75, 80),
        (6.0, 120, 80, 82),
        (8.0, 125, 80, 86),
        (9.5, 120, 80, 84)
    ]
    def vit_to_y(v):
        return y_vit_bot - ((v - 60) / 80.0) * (y_vit_bot - y_vit_top)

    for (h, sys_bp, dia_bp, pulse) in bp_data:
        xc = x_start + h * col_w
        y_sys = vit_to_y(sys_bp)
        y_dia = vit_to_y(dia_bp)
        draw.line([(xc, y_sys), (xc, y_dia)], fill="#dc2626", width=2)
        draw.polygon([(xc, y_sys - 3), (xc - 3, y_sys + 2), (xc + 3, y_sys + 2)], fill="#dc2626")
        draw.polygon([(xc, y_dia + 3), (xc - 3, y_dia - 2), (xc + 3, y_dia - 2)], fill="#dc2626")
        draw.text((xc + 5, y_sys - 2), f"{sys_bp}/{dia_bp}", fill="#dc2626", font=get_font("segoeuib.ttf", 8), anchor="lm")
        
        y_p = vit_to_y(pulse)
        draw.ellipse([xc - 3, y_p - 3, xc + 3, y_p + 3], fill="#0284c7")

    # Clinical note in unused right area of vitals (Hours 10.5 to 12)
    draw.rectangle([x_start + 10 * col_w + 10, y_vit_top + 6, x_end - 10, y_vit_bot - 6], fill="#f8fafc", outline="#cbd5e1")
    draw.text((x_start + 10 * col_w + 18, y_vit_top + 18), "PARTO NORMAL EUTÓCICO ÀS 17:30", fill="#0f766e", font=get_font("segoeuib.ttf", 9))
    draw.text((x_start + 10 * col_w + 18, y_vit_top + 32), "RN Vivo, Feminino, Apgar 9/10, 3.250g", fill="#1e293b", font=get_font("segoeui.ttf", 9))
    draw.text((x_start + 10 * col_w + 18, y_vit_top + 46), "Contato pele a pele imediato na 1ª hora", fill="#059669", font=get_font("segoeui.ttf", 9))
    draw.text((x_start + 10 * col_w + 18, y_vit_top + 60), "Temp. axilar: 36,6 °C • Diurese: espontânea", fill="#64748b", font=get_font("segoeui.ttf", 8))

    # -------------------------------------------------------------
    # 7. OFFICIAL LEGENDA DO MINISTÉRIO DA SAÚDE / SUS (FOOTER)
    # -------------------------------------------------------------
    y_leg = 826
    draw.rectangle([15, y_leg, W - 15, H - 10], fill="#f1f5f9", outline="#cbd5e1", width=1)
    
    draw.text((30, y_leg + 14), "CONVENÇÕES OFICIAIS DO PARTOGRAMA (MINISTÉRIO DA SAÚDE / SUS):", fill="#0f766e", font=get_font("segoeuib.ttf", 11))
    
    draw.text((30, y_leg + 35), "▲  Dilatação Cervical (cm)", fill="#0f172a", font=f_legend)
    draw.text((220, y_leg + 35), "○  Altura da Apresentação (De Lee)", fill="#0f172a", font=f_legend)
    draw.text((470, y_leg + 35), "━  Linha de Alerta (Velocidade ≥ 1 cm/h)", fill="#b45309", font=f_legend)
    draw.text((750, y_leg + 35), "━  Linha de Ação (Alerta + 4 Horas)", fill="#b91c1c", font=f_legend)

    # Contractions Legend
    draw.text((30, y_leg + 56), "Contrações:", fill="#475569", font=f_legend)
    # weak box
    draw.rectangle([105, y_leg + 51, 120, y_leg + 65], fill="#f8fafc", outline="#94a3b8")
    draw_hatch(draw, 105, y_leg + 51, 120, y_leg + 65, mode="weak")
    draw.text((128, y_leg + 58), "< 20 seg (Fraca)", fill="#475569", font=f_legend, anchor="lm")
    # mod box
    draw.rectangle([235, y_leg + 51, 250, y_leg + 65], fill="#f1f5f9", outline="#64748b")
    draw_hatch(draw, 235, y_leg + 51, 250, y_leg + 65, mode="mod")
    draw.text((258, y_leg + 58), "20 - 40 seg (Moderada)", fill="#475569", font=f_legend, anchor="lm")
    # strong box
    draw.rectangle([400, y_leg + 51, 415, y_leg + 65], fill="#0f766e", outline="#042f2e")
    draw.text((423, y_leg + 58), "> 40 seg (Forte)", fill="#475569", font=f_legend, anchor="lm")

    draw.text((540, y_leg + 58), "Líquido Amniótico: I = Íntegro  |  C = Claro  |  M = Meconial  |  S = Sanguinolento", fill="#334155", font=f_legend, anchor="lm")

    # Right Institutional Tag
    draw.text((W - 30, y_leg + 23), "DIRETRIZES NACIONAIS DE ASSISTÊNCIA AO PARTO NORMAL", fill="#0f766e", font=get_font("segoeuib.ttf", 10), anchor="rm")
    draw.text((W - 30, y_leg + 42), "MINISTÉRIO DA SAÚDE • CONITEC • FEBRASGO", fill="#64748b", font=get_font("segoeui.ttf", 10), anchor="rm")
    draw.text((W - 30, y_leg + 62), "DOCUMENTO CLÍNICO OFICIAL SUS", fill="#042f2e", font=get_font("segoeuib.ttf", 9), anchor="rm")

    os.makedirs(os.path.dirname(target_img), exist_ok=True)
    img.save(target_img, "JPEG", quality=98)
    print(f"Partograma no layout oficial do Ministério da Saúde / SUS gerado com sucesso em: {target_img}")

if __name__ == "__main__":
    build_partograma()
