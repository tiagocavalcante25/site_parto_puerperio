import os
import re

def main():
    base_dir = r"c:\Users\Admin\Downloads\INTERNATO GO\site_parto_puerperio"
    index_path = os.path.join(base_dir, "index.html")
    components_dir = os.path.join(base_dir, "components")
    os.makedirs(components_dir, exist_ok=True)

    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Header (from start of file up to </header>)
    header_match = re.search(r'(<!DOCTYPE html>.*?</header>)', content, re.DOTALL)
    if header_match:
        with open(os.path.join(components_dir, "header.html"), "w", encoding="utf-8") as f:
            f.write(header_match.group(1).strip() + "\n")
        print("Created header.html")

    # 2. Hero
    hero_match = re.search(r'(  <!-- HERO SECTION -->\s*<section.*?</section>)', content, re.DOTALL)
    if hero_match:
        with open(os.path.join(components_dir, "hero.html"), "w", encoding="utf-8") as f:
            f.write(hero_match.group(1).strip() + "\n")
        print("Created hero.html")

    # 3. Modulos Index
    modulos_index_match = re.search(r'(  <!-- QUICK NAVIGATION DRAWER / INDEX -->\s*<section id="modulos-index".*?</section>)', content, re.DOTALL)
    if modulos_index_match:
        with open(os.path.join(components_dir, "modulos-index.html"), "w", encoding="utf-8") as f:
            f.write(modulos_index_match.group(1).strip() + "\n")
        print("Created modulos-index.html")

    # 4. Modulo 12: Mecanismo de Parto
    m12_match = re.search(r'(  <!-- =+ M[^\n]+DULO 12:[^\n]*=+ -->\s*<section id="modulo-12".*?</section>)', content, re.DOTALL)
    if m12_match:
        with open(os.path.join(components_dir, "modulo-12-mecanismo.html"), "w", encoding="utf-8") as f:
            f.write(m12_match.group(1).strip() + "\n")
        print("Created modulo-12-mecanismo.html")

    # 5. Modulo 13: Partograma & Simulador
    m13_match = re.search(r'(  <!-- =+ M[^\n]+DULO 13:[^\n]*=+ -->\s*<section id="modulo-13".*?</section>)', content, re.DOTALL)
    if m13_match:
        with open(os.path.join(components_dir, "modulo-13-partograma.html"), "w", encoding="utf-8") as f:
            f.write(m13_match.group(1).strip() + "\n")
        print("Created modulo-13-partograma.html")

    # 6. Modulo 16: Distocias & HELPERR
    m16_match = re.search(r'(  <!-- =+ M[^\n]+DULO 16:[^\n]*=+ -->\s*<section id="distocia-ombros".*?</section>)', content, re.DOTALL)
    if m16_match:
        with open(os.path.join(components_dir, "modulo-16-distocias.html"), "w", encoding="utf-8") as f:
            f.write(m16_match.group(1).strip() + "\n")
        print("Created modulo-16-distocias.html")

    # 7. Modulo 17: HPP & Choque
    m17_match = re.search(r'(  <!-- =+ M[^\n]+DULO 17:[^\n]*=+ -->\s*<section id="modulo-17".*?</section>)', content, re.DOTALL)
    if m17_match:
        with open(os.path.join(components_dir, "modulo-17-hpp.html"), "w", encoding="utf-8") as f:
            f.write(m17_match.group(1).strip() + "\n")
        print("Created modulo-17-hpp.html")

    # 8. Modulo 18: Puerperio Normal & Involucao
    m18_match = re.search(r'(  <!-- =+ M[^\n]+DULO 18:[^\n]*=+ -->\s*<section id="modulo-18".*?</section>)', content, re.DOTALL)
    if m18_match:
        with open(os.path.join(components_dir, "modulo-18-puerperio.html"), "w", encoding="utf-8") as f:
            f.write(m18_match.group(1).strip() + "\n")
        print("Created modulo-18-puerperio.html")

    # 9. Modulo 19: Aleitamento
    m19_match = re.search(r'(  <!-- =+ M[^\n]+DULO 19:[^\n]*=+ -->\s*<section id="modulo-19".*?</section>)', content, re.DOTALL)
    if m19_match:
        with open(os.path.join(components_dir, "modulo-19-aleitamento.html"), "w", encoding="utf-8") as f:
            f.write(m19_match.group(1).strip() + "\n")
        print("Created modulo-19-aleitamento.html")

    # 10. Modulo 20: Complicacoes Puerperais & EPDS
    m20_match = re.search(r'(  <!-- =+ M[^\n]+DULO 20:[^\n]*=+ -->\s*<section id="modulo-20".*?</section>)', content, re.DOTALL)
    if m20_match:
        with open(os.path.join(components_dir, "modulo-20-complicacoes.html"), "w", encoding="utf-8") as f:
            f.write(m20_match.group(1).strip() + "\n")
        print("Created modulo-20-complicacoes.html")

    # 11. Flashcards 3D
    fc_match = re.search(r'(  <!-- =+ FLASHCARDS 3D INTERATIVOS =+ -->\s*<section id="flashcards-section".*?</section>)', content, re.DOTALL)
    if fc_match:
        with open(os.path.join(components_dir, "flashcards.html"), "w", encoding="utf-8") as f:
            f.write(fc_match.group(1).strip() + "\n")
        print("Created flashcards.html")

    # 12. Quiz Simulado
    quiz_match = re.search(r'(  <!-- =+ SIMULADO USMLE STEP 2 CK / STEP 3 =+ -->\s*<section id="quiz-section".*?</section>)', content, re.DOTALL)
    if quiz_match:
        with open(os.path.join(components_dir, "quiz-simulado.html"), "w", encoding="utf-8") as f:
            f.write(quiz_match.group(1).strip() + "\n")
        print("Created quiz-simulado.html")

    # 13. High-Yield Summary
    hy_match = re.search(r'(  <!-- =+ HIGH-YIELD REVIEW CHEAT SHEET =+ -->\s*<section id="high-yield-summary".*?</section>)', content, re.DOTALL)
    if hy_match:
        with open(os.path.join(components_dir, "high-yield-summary.html"), "w", encoding="utf-8") as f:
            f.write(hy_match.group(1).strip() + "\n")
        print("Created high-yield-summary.html")

    # 14. Footer
    footer_match = re.search(r'(  <!-- FOOTER -->\s*<footer.*?</footer>)', content, re.DOTALL)
    if footer_match:
        with open(os.path.join(components_dir, "footer.html"), "w", encoding="utf-8") as f:
            f.write(footer_match.group(1).strip() + "\n")
        print("Created footer.html")

    # 15. Modals & Lightboxes
    modals_match = re.search(r'(  <!-- =+ MODALS & LIGHTBOXES =+ -->.*)', content, re.DOTALL)
    if modals_match:
        with open(os.path.join(components_dir, "modals.html"), "w", encoding="utf-8") as f:
            f.write(modals_match.group(1).strip() + "\n")
        print("Created modals.html")

    print("\nTodos os 15 componentes foram extraídos com sucesso para components/!")

if __name__ == "__main__":
    main()
