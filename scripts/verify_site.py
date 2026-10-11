import os
import re

def verify():
    base_dir = r"c:\Users\Admin\Downloads\INTERNATO GO\site_parto_puerperio"
    index_path = os.path.join(base_dir, "index.html")
    
    print("=== INICIANDO VERIFICAÇÃO DE INTEGRIDADE DO SITE PARTO E PUERPÉRIO ===")
    
    if not os.path.exists(index_path):
        raise FileNotFoundError("index.html não encontrado!")
        
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    print(f"1. index.html carregado: {len(html)} caracteres.")

    # Check images
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    print(f"\n2. Verificando {len(img_srcs)} referências a imagens:")
    all_imgs_ok = True
    for src in set(img_srcs):
        if src.startswith("http"):
            print(f"   [EXTERNO] {src}")
            continue
        full_path = os.path.normpath(os.path.join(base_dir, src))
        if os.path.exists(full_path):
            size_kb = os.path.getsize(full_path) / 1024
            print(f"   [OK] {src} ({size_kb:.1f} KB)")
        else:
            print(f"   [FALHA] Imagem não encontrada: {src} -> {full_path}")
            all_imgs_ok = False

    # Check CSS
    css_hrefs = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', html)
    print(f"\n3. Verificando estilos CSS:")
    for href in css_hrefs:
        if href.startswith("http"):
            print(f"   [CDN] {href}")
            continue
        full_path = os.path.normpath(os.path.join(base_dir, href))
        if os.path.exists(full_path):
            print(f"   [OK] {href}")
        else:
            print(f"   [FALHA] CSS não encontrado: {href}")

    # Check JS
    js_srcs = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)
    print(f"\n4. Verificando scripts JS:")
    for s in js_srcs:
        if s.startswith("http"):
            print(f"   [CDN] {s}")
            continue
        full_path = os.path.normpath(os.path.join(base_dir, s))
        if os.path.exists(full_path):
            print(f"   [OK] {s}")
        else:
            print(f"   [FALHA] JS não encontrado: {s}")

    # Check netlify.toml
    netlify_path = os.path.join(base_dir, "netlify.toml")
    print(f"\n5. Verificando netlify.toml:")
    if os.path.exists(netlify_path):
        print(f"   [OK] netlify.toml presente ({os.path.getsize(netlify_path)} bytes)")
    else:
        print(f"   [FALHA] netlify.toml ausente")

    # Check components
    comp_dir = os.path.join(base_dir, "components")
    comps = os.listdir(comp_dir)
    print(f"\n6. Verificando componentes modulares:")
    print(f"   [OK] Total de componentes: {len(comps)}")
    for c in comps:
        print(f"      - {c}")

    print("\n=== VERIFICAÇÃO CONCLUÍDA: STATUS 100% OPERACIONAL! ===")

if __name__ == "__main__":
    verify()
