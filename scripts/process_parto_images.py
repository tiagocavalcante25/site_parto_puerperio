import os
from PIL import Image, ImageDraw, ImageFont

def get_font(name_or_size, size=None):
    if size is None:
        size = name_or_size
        name = "arial.ttf"
    else:
        name = name_or_size
    try:
        return ImageFont.truetype(name, size)
    except:
        try:
            return ImageFont.truetype("calibri.ttf", size)
        except:
            return ImageFont.load_default()

def process_all():
    brain = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34"
    out_dir = r"c:\Users\Admin\Downloads\INTERNATO GO\site_parto_puerperio\assets\img"
    os.makedirs(out_dir, exist_ok=True)

    # 1. MECANISMO DO PARTO: labor_stages_1791067708192.jpg
    p1 = os.path.join(brain, "labor_stages_1791067708192.jpg")
    if os.path.exists(p1):
        im = Image.open(p1)
        draw = ImageDraw.Draw(im)

        # Main Title Box
        draw.rectangle([180, 65, 1200, 125], fill="#e8e5dc")
        draw.text((690, 95), "MECANISMO DO PARTO: DESCIDA E MOVIMENTOS CARDINAIS", fill="#111827", font=get_font("arialbd.ttf", 26), anchor="mm")

        # Top labels
        draw.rectangle([250, 160, 370, 190], fill="#ffffff")
        draw.text((310, 175), "Cabeça Fetal", fill="#1f2937", font=get_font("arialbd.ttf", 15), anchor="mm")

        draw.rectangle([540, 155, 680, 185], fill="#ffffff")
        draw.text((610, 170), "Fundo Uterino", fill="#1f2937", font=get_font("arialbd.ttf", 15), anchor="mm")

        draw.rectangle([580, 230, 720, 280], fill="#ffffff")
        draw.text((650, 245), "Colo Uterino", fill="#1f2937", font=get_font("arialbd.ttf", 15), anchor="mm")
        draw.text((650, 265), "(em dilatação)", fill="#4b5563", font=get_font(13), anchor="mm")

        draw.rectangle([220, 275, 360, 305], fill="#ffffff")
        draw.text((290, 290), "Sínfise Púbica", fill="#1f2937", font=get_font("arialbd.ttf", 15), anchor="mm")

        # Engagement Card (Left)
        draw.rectangle([135, 470, 325, 600], fill="#ffffff")
        draw.text((230, 490), "1. INSINUAÇÃO E DESCIDA", fill="#0f766e", font=get_font("arialbd.ttf", 14), anchor="mm")
        draw.text((230, 512), "(1º Período / Planos -2 a 0)", fill="#0d9488", font=get_font("arialbd.ttf", 13), anchor="mm")
        draw.text((230, 535), "Encaixamento no diâmetro", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((230, 555), "transverso/oblíquo e flexão", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((230, 575), "(diâmetro suboccipito: 9,5 cm)", fill="#4b5563", font=get_font(12), anchor="mm")

        # Internal Rotation Card (Upper Right)
        draw.rectangle([680, 155, 875, 350], fill="#ffffff")
        draw.text((777, 180), "2. ROTAÇÃO INTERNA", fill="#0f766e", font=get_font("arialbd.ttf", 15), anchor="mm")
        draw.text((777, 205), "(Fim do 1º / Início do 2º Período)", fill="#0d9488", font=get_font("arialbd.ttf", 12), anchor="mm")
        draw.text((777, 228), "(Planos 0 a +1 de De Lee)", fill="#6b7280", font=get_font(12), anchor="mm")
        draw.text((777, 255), "O occipício gira de transverso", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((777, 275), "para anterior (OEA / OP)", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((777, 295), "alinhando-se com o diâmetro", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((777, 315), "anteroposterior do estreito inferior.", fill="#374151", font=get_font(13), anchor="mm")

        # Sacrum
        draw.rectangle([680, 380, 755, 410], fill="#ffffff")
        draw.text((717, 395), "Sacro", fill="#1f2937", font=get_font("arialbd.ttf", 14), anchor="mm")

        # Extension and Expulsion (Right)
        draw.rectangle([695, 445, 875, 595], fill="#ffffff")
        draw.text((785, 465), "3. EXTENSÃO E DESPRENDIMENTO", fill="#0f766e", font=get_font("arialbd.ttf", 13), anchor="mm")
        draw.text((785, 487), "(2º Período / Expulsão)", fill="#0d9488", font=get_font("arialbd.ttf", 12), anchor="mm")
        draw.text((785, 512), "A cabeça deflete sob a sínfise.", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((785, 532), "Rotação externa (restituição)", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((785, 552), "para alinhar com ombros.", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((785, 575), "Desprendimento dos ombros.", fill="#374151", font=get_font(13), anchor="mm")

        # Bottom Labels
        draw.rectangle([300, 660, 420, 690], fill="#ffffff")
        draw.text((360, 675), "Espinhas Isquiáticas", fill="#1f2937", font=get_font("arialbd.ttf", 13), anchor="mm")

        draw.rectangle([310, 740, 390, 765], fill="#ffffff")
        draw.text((350, 752), "Vagina", fill="#1f2937", font=get_font("arialbd.ttf", 13), anchor="mm")

        draw.rectangle([430, 825, 540, 870], fill="#ffffff")
        draw.text((485, 838), "Músculos do Assoalho", fill="#1f2937", font=get_font("arialbd.ttf", 13), anchor="mm")
        draw.text((485, 856), "Pélvico", fill="#1f2937", font=get_font("arialbd.ttf", 13), anchor="mm")

        draw.rectangle([780, 800, 855, 830], fill="#ffffff")
        draw.text((817, 815), "Expulsão", fill="#0f766e", font=get_font("arialbd.ttf", 13), anchor="mm")

        # Bottom Stage timeline
        draw.rectangle([315, 905, 640, 940], fill="#d1d5db")
        draw.text((477, 922), "1º Período: Dilatação (Fase Latente e Ativa)", fill="#111827", font=get_font("arialbd.ttf", 15), anchor="mm")

        draw.rectangle([645, 905, 860, 940], fill="#d1d5db")
        draw.text((752, 922), "2º Período: Expulsivo", fill="#111827", font=get_font("arialbd.ttf", 15), anchor="mm")

        im.save(os.path.join(out_dir, "mecanismo_parto_movimentos.jpg"), quality=95)
        print("1. Salvo mecanismo_parto_movimentos.jpg")

    # 2. DISTÓCIA DE OMBROS: shoulder_dystocia_1791067730155.jpg
    p2 = os.path.join(brain, "shoulder_dystocia_1791067730155.jpg")
    if os.path.exists(p2):
        im = Image.open(p2)
        draw = ImageDraw.Draw(im)

        # Top Banner
        draw.rectangle([0, 0, 1376, 80], fill="#356c9a")
        draw.text((688, 40), "EMERGÊNCIA OBSTÉTRICA: DISTÓCIA DE OMBROS E MANOBRAS DE MCROBERTS & RUBIN", fill="#ffffff", font=get_font("arialbd.ttf", 24), anchor="mm")

        # Suprapubic pressure
        draw.rectangle([700, 150, 940, 235], fill="#eef6fb")
        draw.text((820, 175), "Pressão Suprapúbica (Rubin I)", fill="#0369a1", font=get_font("arialbd.ttf", 15), anchor="mm")
        draw.text((820, 198), "Empurra o ombro anterior", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((820, 218), "em direção oblíqua (NUNCA fúndica!)", fill="#b91c1c", font=get_font("arialbd.ttf", 12), anchor="mm")

        # McRoberts label
        draw.rectangle([1080, 420, 1350, 500], fill="#eef6fb")
        draw.text((1215, 445), "Manobra de McRoberts", fill="#0369a1", font=get_font("arialbd.ttf", 16), anchor="mm")
        draw.text((1215, 470), "Hiperflexão e abdução das pernas", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((1215, 488), "Retifica o sacro e amplia o diâmetro AP", fill="#4b5563", font=get_font(12), anchor="mm")

        # Impacted shoulder
        draw.rectangle([130, 290, 360, 365], fill="#eef6fb")
        draw.text((245, 310), "Ombro Anterior Impactado", fill="#b91c1c", font=get_font("arialbd.ttf", 15), anchor="mm")
        draw.text((245, 332), "Retido atrás da sínfise púbica", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((245, 350), "(Sinal da Tartaruga / Turtle Sign)", fill="#4b5563", font=get_font(12), anchor="mm")

        # Pubic symphysis
        draw.rectangle([160, 170, 380, 215], fill="#eef6fb")
        draw.text((270, 192), "Sínfise Púbica Materna", fill="#1f2937", font=get_font("arialbd.ttf", 15), anchor="mm")

        # Fetal head
        draw.rectangle([850, 720, 1050, 790], fill="#eef6fb")
        draw.text((950, 742), "Cabeça Fetal Desprendida", fill="#0f766e", font=get_font("arialbd.ttf", 14), anchor="mm")
        draw.text((950, 765), "Face retraída contra o períneo", fill="#4b5563", font=get_font(12), anchor="mm")

        # Maternal Sacrum
        draw.rectangle([130, 810, 330, 855], fill="#eef6fb")
        draw.text((230, 832), "Sacro Materno (Retificado)", fill="#1f2937", font=get_font("arialbd.ttf", 14), anchor="mm")

        # Pelvic inlet
        draw.rectangle([170, 885, 360, 930], fill="#eef6fb")
        draw.text((265, 907), "Estreito Superior da Pelve", fill="#1f2937", font=get_font("arialbd.ttf", 14), anchor="mm")

        im.save(os.path.join(out_dir, "distocia_ombros_mcroberts.jpg"), quality=95)
        print("2. Salvo distocia_ombros_mcroberts.jpg")

    # 3. HEMORRAGIA PÓS-PARTO E BAKRI: pph_management_1791067751578.jpg
    p3 = os.path.join(brain, "pph_management_1791067751578.jpg")
    if os.path.exists(p3):
        im = Image.open(p3)
        draw = ImageDraw.Draw(im)

        # Title
        draw.rectangle([0, 0, 1376, 75], fill="#4f6070")
        draw.text((688, 38), "MANEJO DA HEMORRAGIA PÓS-PARTO (HPP): TAMPONAMENTO COM BALÃO INTRAUTERINO (BAKRI)", fill="#ffffff", font=get_font("arialbd.ttf", 22), anchor="mm")

        # Myometrium / Endometrium / Fundus
        draw.rectangle([390, 130, 520, 165], fill="#eae4dc")
        draw.text((455, 147), "MIOMÉTRIO", fill="#991b1b", font=get_font("arialbd.ttf", 14), anchor="mm")

        draw.rectangle([700, 140, 830, 175], fill="#eae4dc")
        draw.text((765, 157), "ENDOMÉTRIO", fill="#991b1b", font=get_font("arialbd.ttf", 14), anchor="mm")

        draw.rectangle([835, 205, 985, 240], fill="#eae4dc")
        draw.text((910, 222), "FUNDO UTERINO", fill="#1f2937", font=get_font("arialbd.ttf", 14), anchor="mm")

        # Inset labels
        draw.rectangle([890, 270, 1030, 305], fill="#eae4dc")
        draw.text((960, 287), "SÍNFISE PÚBICA", fill="#1f2937", font=get_font("arialbd.ttf", 13), anchor="mm")

        draw.rectangle([980, 350, 1220, 390], fill="#eae4dc")
        draw.text((1100, 370), "BALÃO INSUFLADO (300-500 mL SF)", fill="#0369a1", font=get_font("arialbd.ttf", 14), anchor="mm")

        draw.rectangle([980, 410, 1320, 450], fill="#eae4dc")
        draw.text((1150, 430), "PRESSÃO DIRETA DE TAMPONAMENTO", fill="#0f766e", font=get_font("arialbd.ttf", 14), anchor="mm")

        draw.rectangle([980, 490, 1320, 530], fill="#eae4dc")
        draw.text((1150, 510), "HEMOSTASIA DO SÍTIO PLACENTÁRIO", fill="#991b1b", font=get_font("arialbd.ttf", 14), anchor="mm")

        draw.rectangle([980, 555, 1120, 590], fill="#eae4dc")
        draw.text((1050, 572), "COLO UTERINO", fill="#1f2937", font=get_font("arialbd.ttf", 13), anchor="mm")

        draw.rectangle([980, 610, 1080, 645], fill="#eae4dc")
        draw.text((1030, 627), "VAGINA", fill="#1f2937", font=get_font("arialbd.ttf", 13), anchor="mm")

        draw.rectangle([960, 850, 1070, 885], fill="#eae4dc")
        draw.text((1015, 867), "BEXIGA", fill="#1f2937", font=get_font("arialbd.ttf", 13), anchor="mm")

        draw.rectangle([860, 930, 1020, 965], fill="#eae4dc")
        draw.text((940, 947), "CANAL VAGINAL", fill="#1f2937", font=get_font("arialbd.ttf", 13), anchor="mm")

        # Catheter drainage
        draw.rectangle([1100, 610, 1330, 655], fill="#eae4dc")
        draw.text((1215, 632), "DRENAGEM DE CONTROLE", fill="#0f766e", font=get_font("arialbd.ttf", 14), anchor="mm")

        draw.rectangle([1120, 820, 1260, 870], fill="#eae4dc")
        draw.text((1190, 835), "SAÍDA COLETORA", fill="#1f2937", font=get_font("arialbd.ttf", 13), anchor="mm")
        draw.text((1190, 855), "(Avaliar débito de HPP)", fill="#4b5563", font=get_font(11), anchor="mm")

        draw.rectangle([210, 185, 410, 225], fill="#eae4dc")
        draw.text((310, 205), "ÚTERO PÓS-PARTO (ATONIA)", fill="#991b1b", font=get_font("arialbd.ttf", 14), anchor="mm")

        im.save(os.path.join(out_dir, "hemorragia_pos_parto_balao_bakri.jpg"), quality=95)
        print("3. Salvo hemorragia_pos_parto_balao_bakri.jpg")

    # 4. AMAMENTAÇÃO E PEGA: breastfeeding_latch_1791067780197.jpg
    p4 = os.path.join(brain, "breastfeeding_latch_1791067780197.jpg")
    if os.path.exists(p4):
        im = Image.open(p4)
        draw = ImageDraw.Draw(im)

        # Header Titles
        draw.rectangle([40, 20, 680, 105], fill="#ffffff")
        draw.text((360, 50), "ANATOMIA MATERNA E REGULAÇÃO HORMONAL", fill="#0f766e", font=get_font("arialbd.ttf", 20), anchor="mm")
        draw.text((360, 80), "DA PRODUÇÃO E EJEÇÃO DE LEITE", fill="#0d9488", font=get_font("arialbd.ttf", 18), anchor="mm")

        draw.rectangle([720, 20, 1350, 100], fill="#ffffff")
        draw.text((1035, 60), "TÉCNICA DA PEGA CORRETA: BOCA BEM ABERTA", fill="#0f766e", font=get_font("arialbd.ttf", 22), anchor="mm")

        # Hormone Cards (Left)
        draw.rectangle([400, 140, 680, 180], fill="#ffffff")
        draw.text((540, 160), "PROLACTINA: PRODUÇÃO DO LEITE", fill="#0369a1", font=get_font("arialbd.ttf", 15), anchor="mm")

        draw.rectangle([400, 550, 680, 590], fill="#ffffff")
        draw.text((540, 570), "OCITOCINA: EJEÇÃO DO LEITE", fill="#b45309", font=get_font("arialbd.ttf", 15), anchor="mm")

        # Latch characteristics (Right)
        draw.rectangle([880, 260, 1040, 310], fill="#ffffff")
        draw.text((960, 275), "Nariz Desobstruído", fill="#1f2937", font=get_font("arialbd.ttf", 14), anchor="mm")
        draw.text((960, 295), "(livre para respirar)", fill="#4b5563", font=get_font(12), anchor="mm")

        draw.rectangle([760, 415, 915, 475], fill="#ffffff")
        draw.text((837, 435), "Lábios Evertidos", fill="#0f766e", font=get_font("arialbd.ttf", 15), anchor="mm")
        draw.text((837, 455), '("Boca de Peixinho")', fill="#0d9488", font=get_font("arialbd.ttf", 13), anchor="mm")

        draw.rectangle([800, 545, 940, 600], fill="#ffffff")
        draw.text((870, 562), "Pega Assimétrica", fill="#1f2937", font=get_font("arialbd.ttf", 14), anchor="mm")
        draw.text((870, 582), "Mais aréola visível acima", fill="#4b5563", font=get_font(12), anchor="mm")

        draw.rectangle([940, 820, 1090, 885], fill="#ffffff")
        draw.text((1015, 842), "Queixo Tocando a Mama", fill="#0f766e", font=get_font("arialbd.ttf", 14), anchor="mm")
        draw.text((1015, 865), "Contato firme e estável", fill="#4b5563", font=get_font(12), anchor="mm")

        im.save(os.path.join(out_dir, "amamentacao_neuroendocrinologia_pega.jpg"), quality=95)
        print("4. Salvo amamentacao_neuroendocrinologia_pega.jpg")

    # 5. INVOLUÇÃO UTERINA E LÓQUIOS: uterine_involution_1791067813177.jpg
    p5 = os.path.join(brain, "uterine_involution_1791067813177.jpg")
    if os.path.exists(p5):
        im = Image.open(p5)
        draw = ImageDraw.Draw(im)

        # Main Title
        draw.rectangle([20, 20, 1350, 85], fill="#ffffff")
        draw.text((688, 52), "INVOLUÇÃO UTERINA E EVOLUÇÃO DOS LÓQUIOS NO PUERPÉRIO", fill="#111827", font=get_font("arialbd.ttf", 26), anchor="mm")

        # Subheaders
        draw.rectangle([220, 115, 780, 160], fill="#ffffff")
        draw.text((500, 137), "REGRESSÃO DA ALTURA DO FUNDO UTERINO", fill="#0f766e", font=get_font("arialbd.ttf", 18), anchor="mm")

        draw.rectangle([1050, 115, 1320, 160], fill="#ffffff")
        draw.text((1185, 137), "EVOLUÇÃO DOS LÓQUIOS", fill="#0f766e", font=get_font("arialbd.ttf", 18), anchor="mm")

        # Day descriptions
        draw.rectangle([800, 185, 985, 345], fill="#ffffff")
        draw.text((892, 205), "Dia do Parto (Dia 0)", fill="#991b1b", font=get_font("arialbd.ttf", 14), anchor="mm")
        draw.text((892, 230), "Fundo na cicatriz umbilical", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((892, 250), "ou discretamente acima.", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((892, 275), "Útero contraído e firme:", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((892, 298), "Globo de Segurança de Pinard", fill="#0f766e", font=get_font("arialbd.ttf", 13), anchor="mm")
        draw.text((892, 320), "(prevenção de HPP)", fill="#6b7280", font=get_font(11), anchor="mm")

        draw.rectangle([480, 230, 610, 315], fill="#ffffff")
        draw.text((545, 250), "Dias 1 a 2", fill="#1f2937", font=get_font("arialbd.ttf", 15), anchor="mm")
        draw.text((545, 275), "1 a 2 cm abaixo", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((545, 295), "do umbigo", fill="#374151", font=get_font(13), anchor="mm")

        draw.rectangle([420, 850, 610, 950], fill="#ffffff")
        draw.text((515, 872), "7º Dia Pós-Parto", fill="#1f2937", font=get_font("arialbd.ttf", 14), anchor="mm")
        draw.text((515, 897), "Fundo a meio caminho entre", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((515, 917), "umbigo e sínfise púbica", fill="#374151", font=get_font(13), anchor="mm")

        draw.rectangle([630, 850, 820, 950], fill="#ffffff")
        draw.text((725, 872), "10º ao 14º Dia", fill="#1f2937", font=get_font("arialbd.ttf", 14), anchor="mm")
        draw.text((725, 897), "Órgão intrapélvico:", fill="#0f766e", font=get_font("arialbd.ttf", 13), anchor="mm")
        draw.text((725, 917), "NÃO palpável acima da sínfise", fill="#374151", font=get_font(13), anchor="mm")

        draw.rectangle([830, 850, 1010, 950], fill="#ffffff")
        draw.text((920, 872), "6ª Semana (42d)", fill="#1f2937", font=get_font("arialbd.ttf", 14), anchor="mm")
        draw.text((920, 897), "Retorno completo ao", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((920, 917), "tamanho pré-gravídico", fill="#374151", font=get_font(13), anchor="mm")

        # Right side Lochia cards
        draw.rectangle([1100, 185, 1370, 395], fill="#ffffff")
        draw.text((1235, 205), "1. LÓQUIOS RUBROS (Dias 1 a 3)", fill="#991b1b", font=get_font("arialbd.ttf", 14), anchor="mm")
        draw.text((1235, 230), "Aspecto: Vermelho-vivo / escuro", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((1235, 252), "Composição: Sangue e decídua", fill="#4b5563", font=get_font(12), anchor="mm")
        draw.text((1235, 275), "Odor: Característico (não fétido)", fill="#4b5563", font=get_font(12), anchor="mm")

        draw.rectangle([1100, 435, 1370, 680], fill="#ffffff")
        draw.text((1235, 455), "2. LÓQUIOS SEROSOS (Dias 4 a 10)", fill="#b45309", font=get_font("arialbd.ttf", 14), anchor="mm")
        draw.text((1235, 480), "Aspecto: Rosado / acastanhado", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((1235, 502), "Composição: Exsudato, muco,", fill="#4b5563", font=get_font(12), anchor="mm")
        draw.text((1235, 522), "leucócitos e eritrócitos.", fill="#4b5563", font=get_font(12), anchor="mm")

        draw.rectangle([1100, 740, 1370, 955], fill="#ffffff")
        draw.text((1235, 760), "3. LÓQUIOS ALBOS (Dias 11 a 42)", fill="#0f766e", font=get_font("arialbd.ttf", 14), anchor="mm")
        draw.text((1235, 785), "Aspecto: Esbranquiçado / amarelado", fill="#374151", font=get_font(13), anchor="mm")
        draw.text((1235, 807), "Composição: Leucócitos, muco,", fill="#4b5563", font=get_font(12), anchor="mm")
        draw.text((1235, 827), "células epiteliais e gordura.", fill="#4b5563", font=get_font(12), anchor="mm")

        im.save(os.path.join(out_dir, "involucao_uterina_loquios.jpg"), quality=95)
        print("5. Salvo involucao_uterina_loquios.jpg")

    # 6. PARTOGRAMA DA OMS: partograph_diagram_1791067846818.jpg
    p6 = os.path.join(brain, "partograph_diagram_1791067846818.jpg")
    if os.path.exists(p6):
        im = Image.open(p6)
        draw = ImageDraw.Draw(im)

        # Title
        draw.rectangle([100, 20, 1280, 85], fill="#ffffff")
        draw.text((688, 52), "PARTOGRAMA DA OMS: REGISTRO GRÁFICO DO TRABALHO DE PARTO", fill="#111827", font=get_font("arialbd.ttf", 26), anchor="mm")

        # Hours header
        draw.rectangle([500, 95, 820, 135], fill="#bce0ea")
        draw.text((660, 115), "Tempo de Trabalho de Parto (Horas)", fill="#0f766e", font=get_font("arialbd.ttf", 16), anchor="mm")

        # Alert line and Action line labels
        draw.rectangle([510, 290, 680, 340], fill="#fef3c7")
        draw.text((595, 315), "Linha de Alerta", fill="#b45309", font=get_font("arialbd.ttf", 16), anchor="mm")

        draw.rectangle([860, 310, 1020, 360], fill="#fee2e2")
        draw.text((940, 335), "Linha de Ação (4h)", fill="#b91c1c", font=get_font("arialbd.ttf", 16), anchor="mm")

        # Axis labels
        draw.rectangle([1240, 95, 1360, 185], fill="#ffffff")
        draw.text((1300, 115), "Descida Fetal", fill="#0f766e", font=get_font("arialbd.ttf", 14), anchor="mm")
        draw.text((1300, 140), "(De Lee)", fill="#0f766e", font=get_font("arialbd.ttf", 13), anchor="mm")

        im.save(os.path.join(out_dir, "partograma_oms_curvas.jpg"), quality=95)
        print("6. Salvo partograma_oms_curvas.jpg")

    print("\nProcessamento de todas as 6 imagens concluído com sucesso!")

if __name__ == "__main__":
    process_all()
