/**
 * Plataforma Interativa de Parto e Puerpério - App Logic
 * USMLE Step 2 CK / Step 3 & Ivy League Standard
 */

// ==========================================
// 1. TEMA E MODO DIDÁTICO
// ==========================================
function initTheme() {
  const savedTheme = localStorage.getItem('theme');
  const isDark = savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches);
  if (isDark) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
  updateThemeIcon();
}

function toggleDarkMode() {
  const isDark = document.documentElement.classList.toggle('dark');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
  updateThemeIcon();
  if (window.renderPartograph) {
    window.renderPartograph();
  }
}

function updateThemeIcon() {
  const icon = document.getElementById('theme-icon');
  if (!icon) return;
  const isDark = document.documentElement.classList.contains('dark');
  icon.className = isDark ? 'fa-solid fa-sun text-amber-400' : 'fa-solid fa-moon text-slate-600';
}

function toggleDidacticMode() {
  const toggle = document.getElementById('didactic-toggle');
  if (!toggle) return;
  const isChecked = toggle.checked;
  if (isChecked) {
    document.body.classList.remove('hide-didactic');
  } else {
    document.body.classList.add('hide-didactic');
  }
  localStorage.setItem('didactic-mode', isChecked ? 'true' : 'false');
}

function initDidacticMode() {
  const saved = localStorage.getItem('didactic-mode');
  const toggle = document.getElementById('didactic-toggle');
  if (saved === 'false') {
    if (toggle) toggle.checked = false;
    document.body.classList.add('hide-didactic');
  } else {
    if (toggle) toggle.checked = true;
    document.body.classList.remove('hide-didactic');
  }
}

// ==========================================
// 2. SISTEMA DE TAMANHO DE FONTE (A / A+ / A++)
// ==========================================
function setFontSize(size) {
  const validSizes = ['normal', 'large', 'xlarge'];
  if (!validSizes.includes(size)) size = 'normal';
  
  document.documentElement.setAttribute('data-font-size', size);
  try {
    localStorage.setItem('fontSize', size);
  } catch (e) {}
  
  // Atualiza botões no desktop e navbar fixa
  document.querySelectorAll('[data-font-btn], .font-size-btn').forEach(btn => {
    const target = btn.getAttribute('data-font-btn') || btn.getAttribute('data-font-size-target');
    if (target === size) {
      btn.classList.add('bg-teal-600', 'text-white', 'shadow-sm', 'active', 'font-bold');
      btn.classList.remove('text-slate-600', 'dark:text-slate-300');
      btn.setAttribute('aria-pressed', 'true');
    } else {
      btn.classList.remove('bg-teal-600', 'text-white', 'shadow-sm', 'active', 'font-bold');
      btn.classList.add('text-slate-600', 'dark:text-slate-300');
      btn.setAttribute('aria-pressed', 'false');
    }
  });

  // Atualiza botões no mobile drawer se existirem
  document.querySelectorAll('[data-font-btn-mobile]').forEach(btn => {
    if (btn.getAttribute('data-font-btn-mobile') === size) {
      btn.classList.add('bg-teal-600', 'text-white', 'shadow-sm', 'active');
      btn.classList.remove('text-slate-600', 'dark:text-slate-300');
    } else {
      btn.classList.remove('bg-teal-600', 'text-white', 'shadow-sm', 'active');
      btn.classList.add('text-slate-600', 'dark:text-slate-300');
    }
  });
}

function initFontSize() {
  let savedSize = 'normal';
  try {
    savedSize = localStorage.getItem('fontSize') || 'normal';
  } catch (e) {}
  setFontSize(savedSize);
}

// ==========================================
// 3. MENU NAVEGAÇÃO MOBILE (GAVETA REDUNDANTE REMOVIDA)
// ==========================================
function toggleMobileMenu() {
  const drawer = document.getElementById('mobile-nav-drawer');
  const backdrop = document.getElementById('mobile-nav-backdrop');
  if (!drawer || !backdrop) return;

  const isOpen = drawer.classList.contains('drawer-open');
  if (isOpen) {
    closeMobileMenu();
  } else {
    drawer.classList.remove('drawer-closed');
    drawer.classList.add('drawer-open');
    backdrop.classList.remove('hidden');
    requestAnimationFrame(() => {
      backdrop.classList.remove('opacity-0');
    });
    document.body.style.overflow = 'hidden';
  }
}

function closeMobileMenu() {
  const drawer = document.getElementById('mobile-nav-drawer');
  const backdrop = document.getElementById('mobile-nav-backdrop');
  if (!drawer || !backdrop) return;

  drawer.classList.remove('drawer-open');
  drawer.classList.add('drawer-closed');
  backdrop.classList.add('opacity-0');
  setTimeout(() => {
    backdrop.classList.add('hidden');
    document.body.style.overflow = '';
  }, 300);
}

// ==========================================
// 4. BARRA DE PROGRESSO DE LEITURA
// ==========================================
window.addEventListener('scroll', () => {
  const progressBar = document.getElementById('reading-progress');
  if (!progressBar) return;
  const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
  const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
  progressBar.style.width = scrolled + '%';
});

// ==========================================
// 3. TEXT-TO-SPEECH (WEB SPEECH API)
// ==========================================
let currentUtterance = null;
let isSpeaking = false;

function speakSection(sectionId) {
  if (!('speechSynthesis' in window)) {
    alert('Seu navegador não suporta a Web Speech API.');
    return;
  }

  if (isSpeaking) {
    window.speechSynthesis.cancel();
    isSpeaking = false;
    updateAudioButton(sectionId, false);
    return;
  }

  const sectionEl = document.getElementById(sectionId);
  if (!sectionEl) return;

  const text = sectionEl.innerText;
  currentUtterance = new SpeechSynthesisUtterance(text);
  currentUtterance.lang = 'pt-BR';
  currentUtterance.rate = 1.05;

  currentUtterance.onstart = () => {
    isSpeaking = true;
    updateAudioButton(sectionId, true);
  };

  currentUtterance.onend = () => {
    isSpeaking = false;
    updateAudioButton(sectionId, false);
  };

  currentUtterance.onerror = () => {
    isSpeaking = false;
    updateAudioButton(sectionId, false);
  };

  window.speechSynthesis.speak(currentUtterance);
}

function updateAudioButton(sectionId, speaking) {
  const btn = document.querySelector(`[data-speech-btn="${sectionId}"]`);
  if (!btn) return;
  if (speaking) {
    btn.innerHTML = '<i class="fa-solid fa-stop text-rose-500 animate-pulse"></i> Pausar';
    btn.classList.add('bg-rose-50', 'dark:bg-rose-950/40', 'border-rose-300');
  } else {
    btn.innerHTML = '<i class="fa-solid fa-volume-high text-teal-600 dark:text-teal-400"></i> Ouvir Resumo';
    btn.classList.remove('bg-rose-50', 'dark:bg-rose-950/40', 'border-rose-300');
  }
}

// ==========================================
// 4. LIGHTBOX DE IMAGENS MÉDICAS
// ==========================================
function openLightbox(src, title, caption) {
  const modal = document.getElementById('image-modal');
  const img = document.getElementById('lightbox-img');
  const titleEl = document.getElementById('lightbox-title');
  const captionEl = document.getElementById('lightbox-caption');

  if (!modal || !img) return;

  img.src = src;
  if (titleEl) titleEl.innerText = title || 'Imagem Médica';
  if (captionEl) captionEl.innerText = caption || '';

  modal.classList.remove('hidden');
  modal.classList.add('flex');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  const modal = document.getElementById('image-modal');
  if (!modal) return;
  modal.classList.add('hidden');
  modal.classList.remove('flex');
  document.body.style.overflow = '';
}

// ==========================================
// 5. BUSCA RÁPIDA (CTRL+K)
// ==========================================
const searchDatabase = [
  { title: "Mecanismo do Parto e 7 Movimentos Cardinais", category: "Módulo 12", url: "#modulo-12", keywords: "insinuação encaixamento descida flexão rotação interna extensão restituição expulsão suboccipitobregmático" },
  { title: "Estática Fetal e Apresentações Cefálicas", category: "Módulo 12", url: "#modulo-12-estatica", keywords: "situação apresentação atitude posição fletida bregma fronte face mento" },
  { title: "Partograma da OMS e Linhas de Alerta e Ação", category: "Módulo 13", url: "#modulo-13", keywords: "partograma alerta ação dilatação descida De Lee distocia funcional parada secundária" },
  { title: "Simulador Interativo do Partograma", category: "Ferramenta Interativa", url: "#simulador-partograma", keywords: "curva partograma simulador oms zhang alerta ação cesárea" },
  { title: "Analgesia e Anestesia Obstétrica (Peridural e Raqui)", category: "Módulo 14", url: "#modulo-14", keywords: "epidural raqui cefaleia pós-punção blood patch hipotensão bloqueio pudendo" },
  { title: "Parto Humanizado e Diretrizes da OMS", category: "Módulo 15", url: "#modulo-15", keywords: "humanizado Kristeller episiotomia seletiva clampeamento tardio acompanhante pele a pele" },
  { title: "Distócia de Ombros e Mnemônico HELPERR", category: "Módulo 16", url: "#distocia-ombros", keywords: "distócia ombro McRoberts Rubin Woods braço posterior Gaskin tartaruga plexo braquial Erb" },
  { title: "Parto Operatório: Fórceps e Vácuo-Extrator", category: "Módulo 16", url: "#parto-operatorio", keywords: "fórceps Simpson Kielland vácuo desproporção cefalopélvica indicação" },
  { title: "Hemorragia Pós-Parto (HPP) e os 4 T's", category: "Módulo 17", url: "#modulo-17", keywords: "hpp atonia tônus trauma tecido trombina ocitocina metilergometrina misoprostol tranexâmico Bakri B-Lynch" },
  { title: "Calculadora de Risco de HPP & Índice de Choque", category: "Ferramenta Interativa", url: "#calculadora-hpp", keywords: "índice de choque si 4 ts atonia uterotônicos transfusão 1:1:1" },
  { title: "Acretismo Placentário (Acreta, Increta, Percreta)", category: "Módulo 17", url: "#acretismo", keywords: "acretismo acreta increta percreta placenta prévia cesárea anterior histerectomia" },
  { title: "Puerpério Fisiológico, Involução e Lóquios", category: "Módulo 18", url: "#modulo-18", keywords: "puerpério imediato tardio remoto Pinard lóquios rubros serosos albos LAM contracepção" },
  { title: "Neuroendocrinologia da Lactação e Pega Correta", category: "Módulo 19", url: "#modulo-19", keywords: "amamentação prolactina ocitocina colostro pega fissura mastite abscesso" },
  { title: "Complicações Puerperais: Endometrite, TVP e Depressão", category: "Módulo 20", url: "#modulo-20", keywords: "endometrite clindamicina gentamicina tvp tep heparina baby blues depressão edinburgh psicose Sheehan" },
  { title: "Escala de Edimburgo (EPDS) Interativa", category: "Ferramenta Interativa", url: "#calculadora-epds", keywords: "edinburgh epds depressão pós-parto baby blues psicose" }
];

function openSearchModal() {
  const modal = document.getElementById('search-modal');
  const input = document.getElementById('search-input');
  if (!modal || !input) return;
  modal.classList.remove('hidden');
  modal.classList.add('flex');
  input.value = '';
  input.focus();
  handleSearch('');
  document.body.style.overflow = 'hidden';
}

function closeSearchModal() {
  const modal = document.getElementById('search-modal');
  if (!modal) return;
  modal.classList.add('hidden');
  modal.classList.remove('flex');
  document.body.style.overflow = '';
}

function handleSearch(query) {
  const container = document.getElementById('search-results');
  if (!container) return;

  const q = query.trim().toLowerCase();
  if (!q) {
    container.innerHTML = '<p class="text-xs text-slate-400 text-center py-6">Digite um termo clínico para pesquisar (ex: McRoberts, HPP, Partograma, Endometrite, Lóquios)...</p>';
    return;
  }

  const results = searchDatabase.filter(item => 
    item.title.toLowerCase().includes(q) || 
    item.category.toLowerCase().includes(q) || 
    item.keywords.toLowerCase().includes(q)
  );

  if (results.length === 0) {
    container.innerHTML = '<p class="text-xs text-slate-400 text-center py-6">Nenhum resultado encontrado para "<strong>' + query + '</strong>".</p>';
    return;
  }

  container.innerHTML = results.map(item => `
    <a href="${item.url}" onclick="closeSearchModal()" class="block p-3 rounded-xl hover:bg-teal-50 dark:hover:bg-slate-800 transition-colors border border-transparent hover:border-teal-200 dark:hover:border-teal-800">
      <div class="flex items-center justify-between">
        <span class="text-sm font-bold text-slate-900 dark:text-white">${item.title}</span>
        <span class="text-[10px] uppercase font-semibold px-2 py-0.5 rounded-full bg-teal-100 dark:bg-teal-900/50 text-teal-700 dark:text-teal-300">${item.category}</span>
      </div>
      <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 line-clamp-1">${item.keywords}</p>
    </a>
  `).join('');
}

document.addEventListener('keydown', (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
    e.preventDefault();
    openSearchModal();
  } else if (e.key === 'Escape') {
    closeSearchModal();
    closeLightbox();
  }
});

// ==========================================
// 6. SIMULADOR INTERATIVO DO PARTOGRAMA (OMS)
// ==========================================
const partographScenarios = {
  normal: {
    name: "Parto Eutócico Normal",
    description: "Início da fase ativa em 6 cm. Progressão rápida e constante a ≥ 1 cm/h, mantendo-se sempre à esquerda da Linha de Alerta até a dilatação completa (10 cm).",
    diagnosis: "Evolução Eutócica Fisiológica",
    diagnosisColor: "text-emerald-600 dark:text-emerald-400",
    action: "Manter assistência humanizada de rotina, suporte contínuo e ausculta intermitente da FCF.",
    points: [
      { time: 0, dilation: 6, station: -2 },
      { time: 1, dilation: 7, station: -1 },
      { time: 2, dilation: 8.5, station: 0 },
      { time: 3, dilation: 10, station: 2 }
    ]
  },
  prolonged: {
    name: "Fase Ativa Prolongada (Distocia Funcional)",
    description: "Dilatação progride em velocidade inferior a 1 cm/h. A curva cruza a Linha de Alerta em direção à Linha de Ação.",
    diagnosis: "Fase Ativa Prolongada por Hipoatividade Uterina",
    diagnosisColor: "text-amber-600 dark:text-amber-400",
    action: "Avaliar dinâmica uterina (contrações < 3/10 min). Indicar amniotomia e/ou infusão de ocitocina para otimizar contratilidade miometrial antes que atinja a Linha de Ação.",
    points: [
      { time: 0, dilation: 6, station: -2 },
      { time: 2, dilation: 6.5, station: -2 },
      { time: 4, dilation: 7.5, station: -1 },
      { time: 6, dilation: 8.5, station: 0 },
      { time: 8, dilation: 10, station: 2 }
    ]
  },
  arrest_dilation: {
    name: "Parada Secundária da Dilatação (DCP / Falha de Progressão)",
    description: "A dilatação para completamente em 7 cm por ≥ 4 horas com contrações adequadas (≥ 200 Unidades Montevideo). A curva ultrapassa a Linha de Ação.",
    diagnosis: "Parada Secundária de Dilatação / Desproporção Cefalopélvica",
    diagnosisColor: "text-rose-600 dark:text-rose-400",
    action: "Critérios de parada de progressão preenchidos (≥ 6 cm + bolsa rota + ≥ 4h de contrações adequadas). Indicação formal de Cesariana.",
    points: [
      { time: 0, dilation: 6, station: -2 },
      { time: 1, dilation: 7, station: -1 },
      { time: 2, dilation: 7, station: -1 },
      { time: 4, dilation: 7, station: -1 },
      { time: 6, dilation: 7, station: -1 }
    ]
  },
  arrest_descent: {
    name: "Parada de Descida no 2º Período",
    description: "Dilatação atinge 10 cm, mas a apresentação fetal permanece fixa no plano 0 de De Lee por mais de 2 a 3 horas no período expulsivo.",
    diagnosis: "Parada Secundária de Descida",
    diagnosisColor: "text-rose-600 dark:text-rose-400",
    action: "Avaliar altura e variedade de posição. Se insinuação confirmada e condições preenchidas, considerar fórceps; se DCP ou plano alto, indicar cesariana.",
    points: [
      { time: 0, dilation: 6, station: -2 },
      { time: 2, dilation: 8, station: -1 },
      { time: 3, dilation: 10, station: 0 },
      { time: 5, dilation: 10, station: 0 },
      { time: 6, dilation: 10, station: 0 }
    ]
  }
};

let currentScenarioKey = 'normal';

function selectPartographScenario(key) {
  currentScenarioKey = key;
  document.querySelectorAll('.scenario-btn').forEach(btn => {
    btn.classList.remove('bg-teal-600', 'text-white', 'shadow-md');
    btn.classList.add('bg-white', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-300');
  });
  const activeBtn = document.getElementById(`btn-scenario-${key}`);
  if (activeBtn) {
    activeBtn.classList.remove('bg-white', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-300');
    activeBtn.classList.add('bg-teal-600', 'text-white', 'shadow-md');
  }
  renderPartograph();
}

function renderPartograph() {
  const canvas = document.getElementById('partograph-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const isDark = document.documentElement.classList.contains('dark');

  // Set display resolution
  const width = canvas.width;
  const height = canvas.height;
  ctx.clearRect(0, 0, width, height);

  const padLeft = 60;
  const padRight = 50;
  const padTop = 40;
  const padBottom = 50;
  const graphW = width - padLeft - padRight;
  const graphH = height - padTop - padBottom;

  // Background Grid Colors
  const gridColor = isDark ? 'rgba(255, 255, 255, 0.08)' : 'rgba(0, 0, 0, 0.06)';
  const textColor = isDark ? '#94a3b8' : '#64748b';

  // Draw Grid Lines (Time 0 to 10 hours)
  ctx.lineWidth = 1;
  ctx.strokeStyle = gridColor;
  ctx.font = '11px sans-serif';
  ctx.fillStyle = textColor;
  ctx.textAlign = 'center';

  for (let h = 0; h <= 10; h++) {
    const x = padLeft + (h / 10) * graphW;
    ctx.beginPath();
    ctx.moveTo(x, padTop);
    ctx.lineTo(x, padTop + graphH);
    ctx.stroke();
    ctx.fillText(`${h}h`, x, padTop + graphH + 18);
  }

  // Draw Dilation Grid Lines (0 to 10 cm)
  ctx.textAlign = 'right';
  for (let d = 0; d <= 10; d += 2) {
    const y = padTop + graphH - (d / 10) * graphH;
    ctx.beginPath();
    ctx.moveTo(padLeft, y);
    ctx.lineTo(padLeft + graphW, y);
    ctx.stroke();
    ctx.fillText(`${d} cm`, padLeft - 10, y + 4);
  }

  // Axis Labels
  ctx.save();
  ctx.translate(18, padTop + graphH / 2);
  ctx.rotate(-Math.PI / 2);
  ctx.textAlign = 'center';
  ctx.font = 'bold 12px sans-serif';
  ctx.fillStyle = isDark ? '#cbd5e1' : '#334155';
  ctx.fillText('Dilatação Cervical (cm)', 0, 0);
  ctx.restore();

  ctx.textAlign = 'center';
  ctx.font = 'bold 12px sans-serif';
  ctx.fillText('Tempo de Trabalho de Parto (Horas a partir de 6 cm)', padLeft + graphW / 2, height - 12);

  // 1. Linha de Alerta (Amarela - 1 cm/h a partir de 6 cm na hora 0 até 10 cm na hora 4)
  const xAlertStart = padLeft;
  const yAlertStart = padTop + graphH - (6 / 10) * graphH;
  const xAlertEnd = padLeft + (4 / 10) * graphW;
  const yAlertEnd = padTop + graphH - (10 / 10) * graphH;

  ctx.strokeStyle = '#eab308';
  ctx.lineWidth = 2.5;
  ctx.setLineDash([6, 4]);
  ctx.beginPath();
  ctx.moveTo(xAlertStart, yAlertStart);
  ctx.lineTo(xAlertEnd, yAlertEnd);
  ctx.stroke();

  // 2. Linha de Ação (Vermelha - 4 horas à direita da Linha de Alerta: hora 4 a hora 8)
  const xActionStart = padLeft + (4 / 10) * graphW;
  const yActionStart = padTop + graphH - (6 / 10) * graphH;
  const xActionEnd = padLeft + (8 / 10) * graphW;
  const yActionEnd = padTop + graphH - (10 / 10) * graphH;

  ctx.strokeStyle = '#ef4444';
  ctx.lineWidth = 2.5;
  ctx.setLineDash([]);
  ctx.beginPath();
  ctx.moveTo(xActionStart, yActionStart);
  ctx.lineTo(xActionEnd, yActionEnd);
  ctx.stroke();

  // Legends
  ctx.font = 'bold 11px sans-serif';
  ctx.fillStyle = '#ca8a04';
  ctx.textAlign = 'left';
  ctx.fillText('Linha de Alerta (1 cm/h)', xAlertEnd - 60, yAlertEnd - 10);

  ctx.fillStyle = '#dc2626';
  ctx.fillText('Linha de Ação (+4h)', xActionEnd - 40, yActionEnd - 10);

  // 3. Plot Scenario Curve
  const scenario = partographScenarios[currentScenarioKey];
  if (scenario && scenario.points.length > 0) {
    ctx.strokeStyle = '#0d9488';
    ctx.lineWidth = 3.5;
    ctx.beginPath();

    scenario.points.forEach((pt, idx) => {
      const px = padLeft + (pt.time / 10) * graphW;
      const py = padTop + graphH - (pt.dilation / 10) * graphH;
      if (idx === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    });
    ctx.stroke();

    // Draw Points
    scenario.points.forEach(pt => {
      const px = padLeft + (pt.time / 10) * graphW;
      const py = padTop + graphH - (pt.dilation / 10) * graphH;
      ctx.fillStyle = '#0f766e';
      ctx.beginPath();
      ctx.arc(px, py, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.stroke();
    });
  }

  // Update Diagnostic Panel
  const diagTitle = document.getElementById('parto-diag-title');
  const diagDesc = document.getElementById('parto-diag-desc');
  const diagAction = document.getElementById('parto-diag-action');

  if (diagTitle) {
    diagTitle.innerText = scenario.diagnosis;
    diagTitle.className = `text-lg font-black ${scenario.diagnosisColor}`;
  }
  if (diagDesc) diagDesc.innerText = scenario.description;
  if (diagAction) diagAction.innerText = scenario.action;
}

// ==========================================
// 7. CALCULADORA DE HPP & ÍNDICE DE CHOQUE
// ==========================================
function calculateHPP() {
  const bloodLoss = parseFloat(document.getElementById('hpp-loss-input')?.value || 0);
  const hr = parseFloat(document.getElementById('hpp-hr-input')?.value || 80);
  const sbp = parseFloat(document.getElementById('hpp-sbp-input')?.value || 120);

  const hasHypertension = document.getElementById('has-hypertension-check')?.checked;

  const shockIndex = sbp > 0 ? (hr / sbp).toFixed(2) : 0;
  const shockValueEl = document.getElementById('shock-index-val');
  const shockBadgeEl = document.getElementById('shock-index-badge');
  const shockBarEl = document.getElementById('shock-index-bar');
  const actionAlertEl = document.getElementById('hpp-action-alert');
  const ergometrineWarning = document.getElementById('ergometrine-contraindicated-alert');

  if (shockValueEl) shockValueEl.innerText = shockIndex;

  // Ergometrine Warning Check
  if (ergometrineWarning) {
    if (hasHypertension) {
      ergometrineWarning.classList.remove('hidden');
    } else {
      ergometrineWarning.classList.add('hidden');
    }
  }

  // Evaluate Shock Index Severity
  let badgeText = "Normal (< 0.9)";
  let badgeColor = "bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300";
  let barWidth = "30%";
  let barColor = "bg-emerald-500";
  let actionText = "Parâmetros hemodinâmicos estáveis. Manter vigilância no 4º período de Greenberg.";

  if (shockIndex >= 1.4 || bloodLoss >= 1500) {
    badgeText = "Choque Grave / Alto Risco de Transfusão Maciça (SI ≥ 1.4)";
    badgeColor = "bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 animate-pulse";
    barWidth = "100%";
    barColor = "bg-rose-600";
    actionText = "EMERGÊNCIA CRÍTICA: Ativar Protocolo de Transfusão Maciça (1 CH : 1 PFC : 1 Plaq), Ácido Tranexâmico 1g IV em bolus, tamponamento intrauterino com balão de Bakri ou cirurgia de controle de danos (B-Lynch).";
  } else if (shockIndex >= 0.9 || bloodLoss >= 1000) {
    badgeText = "Choque Iminente / HPP Significativa (SI 0.9 - 1.3)";
    badgeColor = "bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300";
    barWidth = "70%";
    barColor = "bg-amber-500";
    actionText = "Atenção: Acesso venoso duplo calibroso (14G/16G), reposição volêmica com cristaloides aquecidos, massagem bimanual e uterotônicos imediatos.";
  } else if (bloodLoss >= 500) {
    badgeText = "HPP Leve a Moderada (Perda ≥ 500 mL)";
    badgeColor = "bg-yellow-100 text-yellow-800 dark:bg-yellow-950 dark:text-yellow-300";
    barWidth = "50%";
    barColor = "bg-yellow-500";
    actionText = "Iniciar protocolo de 1ª linha: Ocitocina IV em infusão rápida, esvaziamento vesical e massagem uterina contínua.";
  }

  if (shockBadgeEl) {
    shockBadgeEl.innerText = badgeText;
    shockBadgeEl.className = `text-xs px-2.5 py-1 rounded-full font-bold ${badgeColor}`;
  }
  if (shockBarEl) {
    shockBarEl.style.width = barWidth;
    shockBarEl.className = `h-full rounded-full transition-all duration-300 ${barColor}`;
  }
  if (actionAlertEl) {
    actionAlertEl.innerText = actionText;
  }
}

// ==========================================
// 8. SIMULADOR DE EMERGÊNCIA: DISTÓCIA DE OMBROS (HELPERR)
// ==========================================
let helperrTimer = null;
let helperrSeconds = 0;

function toggleHelperrTimer() {
  const timerBtn = document.getElementById('helperr-start-btn');
  const timerDisplay = document.getElementById('helperr-clock');
  const alertBox = document.getElementById('helperr-time-alert');

  if (helperrTimer) {
    clearInterval(helperrTimer);
    helperrTimer = null;
    if (timerBtn) {
      timerBtn.innerHTML = '<i class="fa-solid fa-play"></i> Iniciar Cronômetro de Emergência';
      timerBtn.className = "px-4 py-2 rounded-xl bg-teal-600 hover:bg-teal-700 text-white font-bold text-xs flex items-center gap-2 transition-all shadow-md";
    }
  } else {
    helperrSeconds = 0;
    if (timerBtn) {
      timerBtn.innerHTML = '<i class="fa-solid fa-stop"></i> Parar Cronômetro';
      timerBtn.className = "px-4 py-2 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs flex items-center gap-2 transition-all shadow-md";
    }
    helperrTimer = setInterval(() => {
      helperrSeconds++;
      const mins = Math.floor(helperrSeconds / 60).toString().padStart(2, '0');
      const secs = (helperrSeconds % 60).toString().padStart(2, '0');
      if (timerDisplay) timerDisplay.innerText = `${mins}:${secs}`;

      if (alertBox) {
        if (helperrSeconds >= 300) {
          alertBox.innerText = "CRÍTICO (> 5 minutos): Risco iminente de dano neurológico por anóxia e pH fetal < 7.00. Considerar manobras heróicas (Zavanelli / fratura deliberada de clavícula).";
          alertBox.className = "p-3 rounded-xl bg-rose-600 text-white font-bold text-xs animate-pulse";
        } else if (helperrSeconds >= 120) {
          alertBox.innerText = "ALERTA (> 2 minutos): Se McRoberts e Rubin I falharam, passar imediatamente para manobras internas (Rubin II / Woods) e extração do braço posterior.";
          alertBox.className = "p-3 rounded-xl bg-amber-500 text-white font-bold text-xs";
        } else {
          alertBox.innerText = "Tempo hábil inicial: Foco em McRoberts (hiperflexão) + Pressão Suprapúbica (Rubin I). NUNCA FAZER KRISTELLER!";
          alertBox.className = "p-3 rounded-xl bg-teal-50 dark:bg-teal-950/40 text-teal-800 dark:text-teal-200 border border-teal-200 dark:border-teal-800 text-xs";
        }
      }
    }, 1000);
  }
}

// ==========================================
// 9. AVALIADOR DA ESCALA DE EDINBURGH (EPDS)
// ==========================================
function calculateEPDS() {
  let totalScore = 0;
  const questions = document.querySelectorAll('.epds-select');
  questions.forEach(q => {
    totalScore += parseInt(q.value || 0, 10);
  });

  const selfHarmCheck = document.getElementById('epds-self-harm')?.value;
  const resultScoreEl = document.getElementById('epds-score-val');
  const resultBadgeEl = document.getElementById('epds-badge');
  const resultActionEl = document.getElementById('epds-action');

  if (resultScoreEl) resultScoreEl.innerText = totalScore;

  let badge = "Baixo Risco (Score < 10)";
  let badgeClass = "bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300";
  let action = "Sintomatologia depressiva improvável. Reassegurar apoio familiar habitual e consulta de rotina pós-parto.";

  if (selfHarmCheck === "3" || selfHarmCheck === "2") {
    badge = "ALERTA CRÍTICO: Ideação de Autoextermínio";
    badgeClass = "bg-rose-600 text-white animate-pulse";
    action = "EMERGÊNCIA: Risco de suicídio/infanticídio. Avaliação psiquiátrica imediata em pronto-socorro. Não deixar a paciente desacompanhada.";
  } else if (totalScore >= 13) {
    badge = "Rastreio Positivo para Depressão Pós-Parto (Score ≥ 13)";
    badgeClass = "bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 font-bold";
    action = "Indicação formal de psicoterapia individual e farmacoterapia (Inibidores Seletivos de Recaptação de Serotonina - Sertralina é 1ª linha compatível com aleitamento).";
  } else if (totalScore >= 10) {
    badge = "Risco Moderado / Possível Baby Blues (Score 10-12)";
    badgeClass = "bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300 font-bold";
    action = "Monitoramento rigoroso. Se os sintomas persistirem além de 14 dias pós-parto, reclassificar como Depressão Pós-Parto e iniciar tratamento.";
  }

  if (resultBadgeEl) {
    resultBadgeEl.innerText = badge;
    resultBadgeEl.className = `text-xs px-2.5 py-1 rounded-full font-bold ${badgeClass}`;
  }
  if (resultActionEl) {
    resultActionEl.innerText = action;
  }
}

// ==========================================
// 10. FLASHCARDS INTERATIVOS COM FLIP 3D
// ==========================================
function toggleFlashcard(cardElement) {
  cardElement.classList.toggle('flipped');
}

// ==========================================
// 11. SIMULADO USMLE STEP 2 CK / STEP 3
// ==========================================
const quizAnswers = {
  q1: { correct: 'c', explanation: "A Manobra de McRoberts (hiperflexão e abdução das coxas maternas contra o abdome) é a primeira linha obrigatória, pois retifica a curvatura sacral e alarga o diâmetro anteroposterior da pelve. Deve ser combinada com pressão suprapúbica (Rubin I)." },
  q2: { correct: 'b', explanation: "A paciente preenche todos os critérios de Parada Secundária de Dilatação (≥ 6 cm de dilatação, bolsa rota, e ausência de progressão após ≥ 4 horas com contrações uterinas adequadas ≥ 200 MVU). A conduta mandatória é Cesariana." },
  q3: { correct: 'c', explanation: "A metilergometrina é um potente alcaloide do ergot com ação vasoconstritora sistêmica intensa. É formalmente contraindicada em pacientes com Pré-eclâmpsia ou Hipertensão Arterial pelo risco de crise hipertensiva severa e AVC." },
  q4: { correct: 'b', explanation: "A causa número 1 de Hemorragia Pós-Parto (70% dos casos) é a Atonia Uterina (Tônus no mnemônico dos 4 T's), decorrente de exaustão miometrial pós-trabalho de parto prolongado ou sobredistensão." },
  q5: { correct: 'd', explanation: "A infecção bacteriana da mama (mastite por S. aureus) NÃO é contraindicação para amamentação. Pelo contrário, a manutenção do esvaziamento mamário através das mamadas e ordenha é parte essencial da cura, associada a antibióticos como cefalexina." },
  q6: { correct: 'c', explanation: "O esquema padrão ouro (Gold Standard) para endometrite puerperal pós-cesárea é Clindamicina 900 mg IV 8/8h + Gentamicina 5 mg/kg/dia IV em dose única diária, cobrindo anaeróbios e bactérias Gram-negativas entéricas." },
  q7: { correct: 'a', explanation: "A cefaleia pós-punção dural decorre de fístula liquórica. Se os métodos conservadores (hidratação, cafeína) falharem, o tratamento definitivo de maior eficácia é o Tampão Sanguíneo Peridural (Epidural Blood Patch)." },
  q8: { correct: 'c', explanation: "A Psicose Puerperal é uma emergência psiquiátrica aguda com alto risco de suicídio e infanticídio. A conduta imediata é internação psiquiátrica em enfermaria fechada, afastamento temporário do bebê e antipsicóticos." },
  q9: { correct: 'a', explanation: "A Síndrome de Sheehan consiste em necrose isquêmica da adeno-hipófise secundária a choque hemorrágico grave no parto. O sintoma inicial clássico mais precoce é a agalactia (ausência de produção de leite por deficiência de prolactina)." },
  q10: { correct: 'c', explanation: "A prolactina é sintetizada pela hipófise anterior e estimula a produção láctea nos alvéolos mamários. A ocitocina é liberada pela hipófise posterior e contrai as células mioepiteliais, promovendo a ejeção do leite." }
};

let userScore = 0;
let answeredQuestions = {};

function selectQuizOption(questionId, selectedOption) {
  if (answeredQuestions[questionId]) return;

  answeredQuestions[questionId] = selectedOption;
  const correct = quizAnswers[questionId].correct;
  const feedbackEl = document.getElementById(`${questionId}-feedback`);
  const explanationEl = document.getElementById(`${questionId}-explanation`);

  const buttons = document.querySelectorAll(`[data-quiz-q="${questionId}"]`);
  buttons.forEach(btn => {
    const opt = btn.getAttribute('data-quiz-opt');
    btn.disabled = true;
    if (opt === correct) {
      btn.classList.add('bg-emerald-100', 'border-emerald-500', 'text-emerald-900', 'dark:bg-emerald-950/60', 'dark:text-emerald-200');
    } else if (opt === selectedOption) {
      btn.classList.add('bg-rose-100', 'border-rose-500', 'text-rose-900', 'dark:bg-rose-950/60', 'dark:text-rose-200');
    }
  });

  if (selectedOption === correct) {
    userScore++;
    if (feedbackEl) {
      feedbackEl.innerHTML = '<span class="text-emerald-600 dark:text-emerald-400 font-bold"><i class="fa-solid fa-circle-check"></i> Correto!</span>';
    }
  } else {
    if (feedbackEl) {
      feedbackEl.innerHTML = '<span class="text-rose-600 dark:text-rose-400 font-bold"><i class="fa-solid fa-circle-xmark"></i> Incorreto</span>';
    }
  }

  if (explanationEl) {
    explanationEl.innerText = quizAnswers[questionId].explanation;
    explanationEl.parentElement.classList.remove('hidden');
  }

  updateQuizScore();
}

function updateQuizScore() {
  const scoreDisplay = document.getElementById('quiz-score-display');
  const totalAnswered = Object.keys(answeredQuestions).length;
  if (scoreDisplay) {
    scoreDisplay.innerText = `${userScore} de ${totalAnswered} acertos`;
  }
}

// ==========================================
// 12. INICIALIZAÇÃO GERAL & FAB VOLTAR AO TOPO
// ==========================================
function initFabBackToTop() {
  const fab = document.getElementById('fab-back-to-top');
  if (!fab) return;

  function toggleFab() {
    if (window.scrollY > 350) {
      fab.classList.remove('fab-hidden');
      fab.classList.add('fab-visible');
    } else {
      fab.classList.add('fab-hidden');
      fab.classList.remove('fab-visible');
    }
  }

  window.addEventListener('scroll', toggleFab, { passive: true });
  toggleFab();

  fab.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initFontSize();
  initDidacticMode();
  renderPartograph();
  calculateHPP();
  calculateEPDS();
  initFabBackToTop();
});

