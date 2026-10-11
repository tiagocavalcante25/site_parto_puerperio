import os
import re

SITE_DIR = r"c:\Users\Admin\Downloads\INTERNATO GO\site_parto_puerperio"
HTML_FILE = os.path.join(SITE_DIR, "index.html")

def update_html():
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    print(f"Original HTML length: {len(html)}")

    # 1. Update <head>: add FOUC prevention script for theme and font size
    head_fouc_script = r"""  <!-- Previne Flash of Unstyled Content (FOUC) ao carregar tema escuro e escala de fonte -->
  <script>
    (function() {
      try {
        const savedTheme = localStorage.getItem('theme');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
        const savedFontSize = localStorage.getItem('fontSize') || 'normal';
        document.documentElement.setAttribute('data-font-size', savedFontSize);
      } catch (e) {}
    })();
  </script>
"""
    if "data-font-size" not in html[:1000]:
        html = html.replace("  <!-- Tailwind CSS CDN -->", head_fouc_script + "\n  <!-- Tailwind CSS CDN -->")
        print("FOUC prevention script added to <head>")

    # 2. Replace Header (lines 51 to 127) with Fixed 2-Level Header without mobile hamburger
    new_header = r"""  <!-- ======================================================================
       HEADER / NAVBAR FIXA COM DESIGN FLUIDO, NAVEGAÇÃO DIRETA E SEM GAVETA REDUNDANTE
       ====================================================================== -->
  <header class="glass-header border-b border-slate-200/80 dark:border-slate-800/80 shadow-sm transition-colors">
    <!-- Nível 1: Barra Principal Superior -->
    <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-14 sm:h-16 gap-2 sm:gap-4">
        
        <!-- Brand & Title (Responsive: adapts gracefully from 320px to 4K) -->
        <a href="#modulo-12" class="flex items-center gap-2 sm:gap-3 group flex-shrink-0" title="Ir para o início do Guia de Parto & Puerpério">
          <div class="w-8 h-8 sm:w-10 sm:h-10 rounded-xl bg-gradient-to-tr from-teal-600 to-emerald-500 flex items-center justify-center text-white shadow-md shadow-teal-500/20 group-hover:scale-105 transition-transform flex-shrink-0">
            <i class="fa-solid fa-person-breastfeeding text-sm sm:text-base"></i>
          </div>
          <div class="flex flex-col">
            <div class="flex items-center gap-1.5 sm:gap-2">
              <span class="nav-brand-title font-extrabold tracking-tight text-slate-900 dark:text-white leading-none">Parto & Puerpério</span>
              <span class="text-[9px] sm:text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 rounded bg-teal-100 text-teal-800 dark:bg-teal-950 dark:text-teal-300 border border-teal-200 dark:border-teal-800">Parte 2</span>
            </div>
            <span class="text-[10px] sm:text-[11px] text-slate-500 dark:text-slate-400 font-medium hidden sm:block">USMLE Step 2/3 • Residência Médica • FEBRASGO / OMS</span>
          </div>
        </a>

        <!-- Quick Search Trigger Button (Ctrl+K) -->
        <div class="flex items-center flex-1 max-w-xs sm:max-w-sm lg:max-w-md mx-1 sm:mx-4">
          <button onclick="openSearchModal()" title="Pesquisa Rápida (Ctrl+K)" class="w-full px-3 py-1.5 sm:py-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/80 text-slate-500 dark:text-slate-400 hover:border-teal-500 text-xs font-medium flex items-center justify-between transition-all cursor-pointer">
            <div class="flex items-center gap-2">
              <i class="fa-solid fa-magnifying-glass text-teal-500 text-xs sm:text-sm"></i>
              <span class="truncate">Buscar temas, escores, fármacos...</span>
            </div>
            <kbd class="hidden sm:inline-block px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-[10px] text-slate-400 border border-slate-200 dark:border-slate-700">Ctrl K</kbd>
          </button>
        </div>

        <!-- Action Buttons & Utilities -->
        <div class="flex items-center gap-1 sm:gap-2 flex-shrink-0">
          
          <!-- Didactic Mode Toggle (Modo 5 Anos) -->
          <div class="hidden md:flex items-center gap-1.5 px-2.5 py-1 rounded-xl bg-amber-500/10 border border-amber-500/20 text-xs font-bold text-amber-700 dark:text-amber-400" title="Ativa ou destaca analogias didáticas (Modo 5 Anos)">
            <label for="didactic-toggle" class="cursor-pointer flex items-center gap-1.5">
              <span class="text-[11px] hidden lg:inline">🎈 Modo 5 Anos</span>
              <span class="text-[11px] lg:hidden">🎈 5 Anos</span>
              <input type="checkbox" id="didactic-toggle" checked onchange="toggleDidacticMode()" class="sr-only peer">
              <div class="w-7 h-3.5 bg-slate-300 peer-focus:outline-none rounded-full peer dark:bg-slate-700 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-2.5 after:w-2.5 after:transition-all peer-checked:bg-amber-500"></div>
            </label>
          </div>

          <!-- Seletor Dinâmico de Tamanho de Fonte (A / A+ / A++) -->
          <div class="flex items-center bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-0.5" role="group" aria-label="Controle de tamanho de fonte">
            <button type="button" onclick="setFontSize('normal')" data-font-btn="normal" aria-label="Fonte padrão" title="Fonte padrão" class="font-size-btn px-2 py-1 text-xs font-bold rounded-lg transition-colors">A</button>
            <button type="button" onclick="setFontSize('large')" data-font-btn="large" aria-label="Fonte ampliada" title="Fonte ampliada (+15%)" class="font-size-btn px-2 py-1 text-xs font-bold rounded-lg transition-colors">A+</button>
            <button type="button" onclick="setFontSize('xlarge')" data-font-btn="xlarge" aria-label="Fonte máxima" title="Fonte máxima (+30%)" class="font-size-btn px-2 py-1 text-xs font-bold rounded-lg transition-colors">A++</button>
          </div>

          <!-- Dark Mode Toggle -->
          <button onclick="toggleDarkMode()" title="Alternar tema claro/escuro" aria-label="Alternar modo claro/escuro" class="w-8 h-8 sm:w-9 sm:h-9 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 text-slate-600 dark:text-slate-300 hover:text-teal-500 flex items-center justify-center transition-all cursor-pointer">
            <i id="theme-icon" class="fa-solid fa-moon text-xs sm:text-sm"></i>
          </button>

          <!-- Print / PDF Export Button -->
          <button onclick="window.print()" title="Exportar ou Imprimir Resumo" class="hidden sm:flex p-1.5 px-2.5 rounded-xl bg-teal-600 hover:bg-teal-700 text-white text-xs font-bold items-center gap-1.5 transition-all shadow-md shadow-teal-500/20 cursor-pointer">
            <i class="fa-solid fa-file-pdf"></i>
            <span class="hidden md:inline">PDF</span>
          </button>

        </div>
      </div>
    </div>

    <!-- Nível 2: Faixa Subnav de Módulos & Ferramentas (Scroll Horizontal Fluido sem quebra) -->
    <div class="border-t border-slate-200/70 dark:border-slate-800/70 bg-slate-50/80 dark:bg-slate-950/80 backdrop-blur-md">
      <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
        <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1.5 text-xs font-semibold whitespace-nowrap">
          <span class="text-[10px] uppercase font-bold text-slate-400 dark:text-slate-500 mr-1 flex items-center gap-1 flex-shrink-0">
            <i class="fa-solid fa-book-medical text-teal-500"></i> Módulos:
          </span>
          <a href="#modulo-12" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-teal-600 dark:hover:text-teal-400 hover:bg-teal-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-teal-100 dark:bg-teal-950 text-teal-700 dark:text-teal-300 text-[10px] font-bold flex items-center justify-center">12</span>
            Mecanismo do Parto
          </a>
          <a href="#modulo-13" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-teal-600 dark:hover:text-teal-400 hover:bg-teal-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-teal-100 dark:bg-teal-950 text-teal-700 dark:text-teal-300 text-[10px] font-bold flex items-center justify-center">13</span>
            Partograma OMS
          </a>
          <a href="#distocia-ombros" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-teal-600 dark:hover:text-teal-400 hover:bg-teal-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-teal-100 dark:bg-teal-950 text-teal-700 dark:text-teal-300 text-[10px] font-bold flex items-center justify-center">16</span>
            Distócias & McRoberts
          </a>
          <a href="#modulo-17" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-teal-600 dark:hover:text-teal-400 hover:bg-teal-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-teal-100 dark:bg-teal-950 text-teal-700 dark:text-teal-300 text-[10px] font-bold flex items-center justify-center">17</span>
            HPP & Bakri
          </a>
          <a href="#modulo-18" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-teal-600 dark:hover:text-teal-400 hover:bg-teal-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-teal-100 dark:bg-teal-950 text-teal-700 dark:text-teal-300 text-[10px] font-bold flex items-center justify-center">18</span>
            Puerpério & Involução
          </a>
          <a href="#modulo-19" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-teal-600 dark:hover:text-teal-400 hover:bg-teal-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-teal-100 dark:bg-teal-950 text-teal-700 dark:text-teal-300 text-[10px] font-bold flex items-center justify-center">19</span>
            Aleitamento Materno
          </a>
          <a href="#modulo-20" class="subnav-pill px-2.5 py-1 rounded-lg text-slate-700 dark:text-slate-300 hover:text-teal-600 dark:hover:text-teal-400 hover:bg-teal-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1">
            <span class="w-4 h-4 rounded bg-teal-100 dark:bg-teal-950 text-teal-700 dark:text-teal-300 text-[10px] font-bold flex items-center justify-center">20</span>
            Complicações Puerperais
          </a>

          <!-- Separador -->
          <span class="h-4 w-px bg-slate-300 dark:bg-slate-700 mx-1 flex-shrink-0"></span>

          <!-- Ferramentas Clínicas Diretas -->
          <span class="text-[10px] uppercase font-bold text-slate-400 dark:text-slate-500 mr-1 flex items-center gap-1 flex-shrink-0">
            <i class="fa-solid fa-stethoscope text-amber-500"></i> Ferramentas:
          </span>
          <a href="#simulador-partograma" class="subnav-pill px-2.5 py-1 rounded-lg text-cyan-700 dark:text-cyan-400 hover:bg-cyan-50 dark:hover:bg-cyan-950/40 transition-colors flex items-center gap-1">
            <i class="fa-solid fa-chart-line text-xs"></i>
            Partograma Vivo
          </a>
          <a href="#calculadora-hpp" class="subnav-pill px-2.5 py-1 rounded-lg text-rose-700 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/40 transition-colors flex items-center gap-1">
            <i class="fa-solid fa-droplet text-xs"></i>
            Risco HPP
          </a>
          <a href="#calculadora-epds" class="subnav-pill px-2.5 py-1 rounded-lg text-emerald-700 dark:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-950/40 transition-colors flex items-center gap-1">
            <i class="fa-solid fa-heart-pulse text-xs"></i>
            Escala EPDS
          </a>
          <a href="#flashcards-section" class="subnav-pill px-2.5 py-1 rounded-lg text-purple-700 dark:text-purple-400 hover:bg-purple-50 dark:hover:bg-purple-950/40 transition-colors flex items-center gap-1">
            <i class="fa-solid fa-layer-group text-xs"></i>
            Flashcards 3D
          </a>
          <a href="#quiz-section" class="subnav-pill px-2.5 py-1 rounded-lg text-teal-700 dark:text-teal-400 hover:bg-teal-50 dark:hover:bg-teal-950/40 transition-colors flex items-center gap-1">
            <i class="fa-solid fa-graduation-cap text-xs"></i>
            Simulado
          </a>
          <a href="#high-yield-summary" class="subnav-pill px-2.5 py-1 rounded-lg text-amber-700 dark:text-amber-400 hover:bg-amber-50 dark:hover:bg-amber-950/40 transition-colors flex items-center gap-1">
            <i class="fa-solid fa-bolt text-xs"></i>
            High-Yield
          </a>
        </div>
      </div>
    </div>

    <!-- READING PROGRESS BAR - Attached right at header bottom -->
    <div id="reading-progress" class="h-1 bg-gradient-to-r from-teal-400 via-emerald-500 to-cyan-500 transition-all duration-150 pointer-events-none" style="width: 0%"></div>
  </header>"""

    # Replace header: from <header class="sticky ..."> to </header>
    old_header_pattern = r'<header class="sticky top-0 z-50 glass-header border-b border-slate-200/80 dark:border-slate-800/80 shadow-sm relative">.*?</header>'
    html, count_header = re.subn(old_header_pattern, new_header, html, flags=re.DOTALL)
    print(f"Header replaced: {count_header} match")

    # 3. Completely remove the redundant side drawer and its backdrop
    drawer_pattern = r'<!-- 1\. MOBILE NAVIGATION DRAWER \(Slide-over for Smartphones & Tablets\) -->.*?<!-- 2\. IMAGE LIGHTBOX MODAL -->'
    if re.search(drawer_pattern, html, flags=re.DOTALL):
        html = re.sub(drawer_pattern, '<!-- 2. IMAGE LIGHTBOX MODAL -->', html, flags=re.DOTALL)
        print("Mobile navigation drawer completely removed")

    # 4. Add Floating Back-to-Top Button (FAB) before </body>
    if 'id="fab-back-to-top"' not in html:
        fab_html = r"""  <!-- Botão Flutuante Voltar ao Topo (FAB) -->
  <button id="fab-back-to-top" type="button" aria-label="Voltar ao topo da página" title="Voltar ao topo" 
    class="fab-hidden p-3 rounded-full bg-teal-600 hover:bg-teal-700 active:scale-95 text-white shadow-xl shadow-teal-600/30 border border-white/20 flex items-center justify-center transition-all cursor-pointer">
    <i class="fa-solid fa-arrow-up text-base"></i>
  </button>

</body>"""
        html = html.replace('</body>', fab_html)
        print("FAB button added before </body>")

    # 5. Update the 6 clinical images to ensure fluid container and fluid img attributes
    img_configs = {
        "mecanismo_parto_movimentos.jpg": (1600, 880),
        "partograma_oms_curvas.jpg": (1600, 915),
        "distocia_ombros_mcroberts.jpg": (1376, 768),
        "hemorragia_pos_parto_balao_bakri.jpg": (1376, 768),
        "involucao_uterina_loquios.jpg": (1376, 768),
        "amamentacao_neuroendocrinologia_pega.jpg": (1376, 768)
    }

    # Ensure class="img-fluid-container" on outer container
    html = re.sub(
        r'<div class="relative group cursor-pointer overflow-hidden rounded-3xl border border-slate-200 dark:border-slate-800 bg-slate-900"',
        r'<div class="relative group cursor-pointer overflow-hidden rounded-3xl border border-slate-200 dark:border-slate-800 bg-slate-900 img-fluid-container"',
        html
    )

    for img_name, (w, h) in img_configs.items():
        img_pattern = rf'<img src="assets/img/{re.escape(img_name)}"[^>]*>'
        match = re.search(img_pattern, html)
        if match:
            old_tag = match.group(0)
            alt_match = re.search(r'alt="([^"]*)"', old_tag)
            alt = alt_match.group(1) if alt_match else ""
            new_tag = f'<img src="assets/img/{img_name}" alt="{alt}" class="fluid-img w-full h-auto object-cover transform group-hover:scale-[1.01] transition-transform duration-300 max-w-full" width="{w}" height="{h}" loading="lazy" style="aspect-ratio: 16/9;">'
            html = html.replace(old_tag, new_tag)
            print(f"Updated img tag for: {img_name}")

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully updated {HTML_FILE}. New length: {len(html)}")

if __name__ == "__main__":
    update_html()
