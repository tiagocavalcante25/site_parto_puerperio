import os
import re

SITE_DIR = r"c:\Users\Admin\Downloads\INTERNATO GO\site_parto_puerperio"
HTML_FILE = os.path.join(SITE_DIR, "index.html")
CSS_FILE = os.path.join(SITE_DIR, "assets", "css", "custom.css")
JS_FILE = os.path.join(SITE_DIR, "assets", "js", "app.js")

def test_fluid_design():
    print("=== INICIANDO TESTES DO MOTOR DE RESPONSIVIDADE E FLUID DESIGN (PARTO & PUERPÉRIO) ===")
    
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    with open(CSS_FILE, "r", encoding="utf-8") as f:
        css = f.read()

    with open(JS_FILE, "r", encoding="utf-8") as f:
        js = f.read()

    # 1. Teste do Reset e Overflow-X Hidden
    print("\n[TESTE 1] Reset Universal & Prevenção de Rolagem Horizontal (overflow-x: hidden)")
    assert "overflow-x: hidden !important;" in css, "CSS deve conter overflow-x: hidden !important;"
    assert "overflow-wrap: break-word" in css, "CSS deve conter overflow-wrap: break-word"
    assert "word-wrap: break-word" in css, "CSS deve conter word-wrap: break-word"
    assert "box-sizing: border-box" in css, "CSS deve ter box-sizing: border-box global"
    print("  -> OK: overflow-x: hidden, word-wrap e box-sizing aplicados.")

    # 2. Teste dos Contêineres e Larguras em Porcentagem / Max-Width: 100%
    print("\n[TESTE 2] Contêineres com max-width: 100% e Larguras em Porcentagem")
    assert "max-width: 100% !important;" in css, "CSS deve conter max-width: 100% !important;"
    assert "width: 100% !important;" in css, "CSS deve conter width: 100% !important;"
    print("  -> OK: Contêineres globais (.container, .max-w-*, main, section, etc.) possuem 100% e max-width 100%.")

    # 3. Teste de Imagens Fluidas
    print("\n[TESTE 3] Imagens Fluidas (100% largura máxima, altura proporcional, aspect-ratio)")
    assert "max-width: 100% !important;" in css, "CSS de imagens deve ter max-width: 100%"
    assert "aspect-ratio: 16 / 9;" in css, "CSS deve garantir aspect-ratio 16 / 9 nas imagens"
    
    # Checar se todas as 6 imagens clínicas no HTML têm fluid-img e max-w-full
    img_matches = re.findall(r'<img[^>]+src=["\'](assets/img/[^"\']+)["\'][^>]*>', html)
    assert len(img_matches) == 6, f"Esperadas 6 imagens de infográficos, encontradas {len(img_matches)}"
    for img_tag in re.finditer(r'<img[^>]+src=["\'](assets/img/[^"\']+)["\'][^>]*>', html):
        tag_str = img_tag.group(0)
        assert "fluid-img" in tag_str, f"Tag <img> deve ter classe fluid-img: {tag_str}"
        assert "max-w-full" in tag_str, f"Tag <img> deve ter classe max-w-full: {tag_str}"
        assert "loading=\"lazy\"" in tag_str, f"Tag <img> deve ter loading lazy: {tag_str}"
        assert "aspect-ratio: 16/9;" in tag_str, f"Tag <img> deve ter inline style aspect-ratio: {tag_str}"
    print(f"  -> OK: Todas as {len(img_matches)} imagens contêm classes e atributos fluidos.")

    # 4. Teste da Tipografia e Escala de Fonte
    print("\n[TESTE 4] Tipografia Fluida (clamp()) e Acessibilidade Dinâmica de Fonte")
    assert "clamp(" in css, "CSS deve utilizar clamp() para tipografia responsiva"
    assert "data-font-size" in css, "CSS deve suportar seletor data-font-size"
    assert "font-size-btn" in html, "HTML deve conter botões de controle de tamanho de fonte"
    assert "setFontSize" in js, "app.js deve conter a função setFontSize"
    assert "initFontSize" in js, "app.js deve conter a função initFontSize"
    print("  -> OK: Tipografia fluida com clamp() e switcher de fonte normal/grande/extra grande.")

    # 5. Teste do Menu Fixo no Topo (position: fixed) e Remoção da Gaveta Redundante
    print("\n[TESTE 5] Navbar Fixa no Topo (position: fixed) e Remoção de Gaveta Redundante")
    assert "position: fixed !important;" in css, "CSS deve fixar header no topo"
    assert "id=\"mobile-nav-drawer\"" not in html, "Gaveta redundante mobile-nav-drawer deve ser removida do HTML"
    assert "id=\"mobile-nav-backdrop\"" not in html, "Backdrop redundante mobile-nav-backdrop deve ser removido do HTML"
    assert "id=\"reading-progress\"" in html, "Barra de progresso de leitura deve estar presente"
    assert "id=\"fab-back-to-top\"" in html, "Botão flutuante voltar ao topo deve estar presente"
    assert "initFabBackToTop" in js, "app.js deve ter initFabBackToTop"
    print("  -> OK: Navbar fixa no topo, gaveta redundante removida, progress bar e FAB ativos.")

    # 6. Teste de Prontidão para o GitHub Pages
    print("\n[TESTE 6] Otimização e Deploy para GitHub Pages")
    assert os.path.exists(os.path.join(SITE_DIR, ".nojekyll")), ".nojekyll deve existir na raiz"
    assert "http://localhost" not in html, "HTML não deve conter referências a localhost"
    assert "file:///" not in html, "HTML não deve conter referências a file:///"
    print("  -> OK: .nojekyll presente e caminhos relativos prontos para o GitHub Pages.")

    print("\n=== TODOS OS 6 TESTES DE RESPONSIVIDADE E DESIGN FLUIDO FORAM APROVADOS! ===")

if __name__ == "__main__":
    test_fluid_design()
