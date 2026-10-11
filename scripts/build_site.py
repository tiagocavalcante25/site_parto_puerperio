import os

def build():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    components_dir = os.path.join(base_dir, "components")
    index_file = os.path.join(base_dir, "index.html")

    order = [
        "header.html",
        "hero.html",
        "modulos-index.html",
        "modulo-12-mecanismo.html",
        "modulo-13-partograma.html",
        "modulo-16-distocias.html",
        "modulo-17-hpp.html",
        "modulo-18-puerperio.html",
        "modulo-19-aleitamento.html",
        "modulo-20-complicacoes.html",
        "flashcards.html",
        "quiz-simulado.html",
        "high-yield-summary.html",
        "footer.html",
        "modals.html"
    ]

    print(f"Verificando {len(order)} componentes em {components_dir}...")
    for comp in order:
        p = os.path.join(components_dir, comp)
        if not os.path.exists(p):
            raise FileNotFoundError(f"Componente não encontrado: {comp}")

    # Build index.html from components
    output_parts = []
    
    # 1. Header
    with open(os.path.join(components_dir, "header.html"), "r", encoding="utf-8") as f:
        output_parts.append(f.read().strip())
    
    # 2. Hero
    with open(os.path.join(components_dir, "hero.html"), "r", encoding="utf-8") as f:
        output_parts.append(f.read().strip())
        
    # 3. Modulos Index
    with open(os.path.join(components_dir, "modulos-index.html"), "r", encoding="utf-8") as f:
        output_parts.append(f.read().strip())
        
    # Main container start
    output_parts.append('\n  <!-- MAIN CONTENT CONTAINER -->\n  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-16">\n')

    # Modules & Interactive sections
    modules = [
        "modulo-12-mecanismo.html",
        "modulo-13-partograma.html",
        "modulo-16-distocias.html",
        "modulo-17-hpp.html",
        "modulo-18-puerperio.html",
        "modulo-19-aleitamento.html",
        "modulo-20-complicacoes.html",
        "flashcards.html",
        "quiz-simulado.html",
        "high-yield-summary.html"
    ]
    for m in modules:
        with open(os.path.join(components_dir, m), "r", encoding="utf-8") as f:
            output_parts.append(f.read().strip())

    # Main container end
    output_parts.append('\n  </main>\n')

    # Footer
    with open(os.path.join(components_dir, "footer.html"), "r", encoding="utf-8") as f:
        output_parts.append(f.read().strip())

    # Modals
    with open(os.path.join(components_dir, "modals.html"), "r", encoding="utf-8") as f:
        output_parts.append(f.read().strip())

    full_html = "\n\n".join(output_parts) + "\n"
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Index.html gerado com sucesso a partir dos componentes! Total: {len(full_html)} bytes.")

if __name__ == "__main__":
    build()
