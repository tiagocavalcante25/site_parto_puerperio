# 👶 Plataforma Educacional de Assistência ao Parto e Puerpério
## Nível Ivy League & USMLE Step 2 CK / Step 3 — Guia Interativo Dinâmico
### Baseado no Guia Oficial de Obstetrícia e Ginecologia — Parte 2

Esta plataforma web de alta performance transforma o compêndio médico **Guia Obstetrícia e Ginecologia Parte 2** em uma aplicação dinâmica, interativa, com ilustrações médicas ultrarrealistas em **português**, ferramentas clínicas ativas e arquitetura moderna configurada para **deploy imediato no Netlify**.

---

## 📁 Estrutura de Pastas & Organização Modular

A pasta mãe `site_parto_puerperio` é 100% autônoma e isolada de outros projetos:

```text
site_parto_puerperio/
│
├── 🌐 index.html                       # Aplicação web completa e responsiva
├── ⚙️ netlify.toml                      # Configuração de build, cache e deploy para o Netlify
├── 📄 README.md                        # Documentação completa, instruções de uso e deploy
│
├── 🎨 assets/                          # Recursos estáticos servidos pelo site
│   ├── css/
│   │   └── custom.css                  # Estilos modernos, efeitos glassmorphism e 3D flip
│   ├── js/
│   │   └── app.js                      # Lógica interativa (Canvas, simuladores, quiz, TTS)
│   └── img/                            # 6 Imagens médicas em português e alta resolução
│       ├── mecanismo_parto_movimentos.jpg         # Os 7 Movimentos Cardinais do Parto
│       ├── partograma_oms_curvas.jpg              # Partograma da OMS com Linhas de Alerta/Ação
│       ├── distocia_ombros_mcroberts.jpg          # Manobras de McRoberts, Rubin I & Turtle Sign
│       ├── hemorragia_pos_parto_balao_bakri.jpg    # Tamponamento Uterino com Balão de Bakri
│       ├── involucao_uterina_loquios.jpg          # Cronologia da Involução Uterina e Lóquios
│       └── amamentacao_neuroendocrinologia_pega.jpg # Eixo Prolactina/Ocitocina e Pega Correta
│
├── 🧩 components/                      # Seções modulares do site para fácil manutenção
│   ├── header.html                     # Barra superior, controles de tema, áudio e didática
│   ├── hero.html                       # Seção hero com estatísticas e chamadas clínicas
│   ├── modulos-index.html              # Índice rápido de navegação em cards
│   ├── modulo-12-mecanismo.html        # Módulo 12: Tempos do Parto e Estática Fetal
│   ├── modulo-13-partograma.html       # Módulo 13: Partograma & Simulador em Canvas
│   ├── modulo-16-distocias.html        # Módulo 16: Distócia de Ombros & HELPERR
│   ├── modulo-17-hpp.html              # Módulo 17: Hemorragia Pós-Parto, 4 T's e Bakri
│   ├── modulo-18-puerperio.html        # Módulo 18: Puerpério Fisiológico e Lóquios
│   ├── modulo-19-aleitamento.html      # Módulo 19: Aleitamento Materno e Pega
│   ├── modulo-20-complicacoes.html     # Módulo 20: Infecção Puerperal e Escala EPDS
│   ├── flashcards.html                 # 8 Flashcards 3D Interativos com Rotação
│   ├── quiz-simulado.html              # Simulado USMLE com 10 questões comentadas
│   ├── high-yield-summary.html         # Resumo de Alto Rendimento e Mnemônicos USMLE
│   ├── footer.html                     # Rodapé com créditos acadêmicos e referências
│   └── modals.html                     # Lightbox de imagens e busca rápida (Ctrl+K)
│
├── 📚 guias/                           # Arquivos fonte e compêndios médicos
│   ├── Guia Obstetricia Ginecologia Parte2.pdf
│   └── guia-obstetricia-ginecologia-parte2.md
│
└── 🛠️ scripts/                         # Automação e verificação de integridade
    ├── build_site.py                   # Script de montagem dos componentes no index.html
    ├── extract_components.py           # Extrator modular a partir do index.html
    ├── process_parto_images.py         # Processador de tipografia médica em português
    └── verify_site.py                  # Verificador de integridade de links, CSS e imagens
```

---

## 🎨 Imagens Médicas Ultrarrealistas em Português

Todas as ilustrações contam com diagramação anatômica rigorosa e rotulagem oficial em português:

1. **Mecanismo de Parto & Tempos Cardinais (`mecanismo_parto_movimentos.jpg`)**:
   - Corte sagital pélvico demonstrando os tempos: Insinuação (flexão), Descida, Rotação Interna (pélvica), Extensão (deflexão), Restituição (rotação externa) e Desprendimento do feto.
2. **Partograma da OMS & Curvas de Alerta/Ação (`partograma_oms_curvas.jpg`)**:
   - Gráfico cartesiano de dilatação cervical (cm) vs. tempo (horas), demonstrando a fase latente, fase ativa, linha de alerta e linha de ação a 4 horas de distância.
3. **Distócia de Ombros & Manobra de McRoberts (`distocia_ombros_mcroberts.jpg`)**:
   - Representação anatômica do sinal da tartaruga (*turtle sign*), hiperflexão das coxas sobre o abdome materno (McRoberts) e pressão suprapúbica (Rubin I).
4. **Hemorragia Pós-Parto & Balão de Bakri (`hemorragia_pos_parto_balao_bakri.jpg`)**:
   - Ilustração do tamponamento intrauterino de Bakri inflado com soro fisiológico (300-500 mL) conectado a bolsa coletora para mensuração do sangramento.
5. **Involução Uterina & Lóquios (`involucao_uterina_loquios.jpg`)**:
   - Linha do tempo da altura do fundo uterino (imediatamente pós-parto, 12h, 1º ao 14º dia quando se torna intrapélvico) e evolução das cores dos lóquios (*Rubra*, *Serosa*, *Alba*).
6. **Aleitamento Materno & Pega Correta (`amamentacao_neuroendocrinologia_pega.jpg`)**:
   - Eixo neuroendócrino da sucção (Prolactina para produção nos alvéolos; Ocitocina para ejeção nas células mioepiteliais) e critérios da pega adequada (boca bem aberta, lábio inferior evertido, queixo tocando a mama).

---

## ⚡ Ferramentas Clínicas Interativas Embutidas

* **Simulador Interativo de Partograma (HTML5 Canvas)**:
  - Renderiza curvas de dilatação e descida em tempo real para 4 cenários clínicos:
    - *Evolução Fisiológica*: Parto eutócico padrão.
    - *Fase Ativa Prolongada*: Dilatação < 1 cm/h.
    - *Parada Secundária da Dilatação*: Ausência de dilatação por ≥ 2 horas.
    - *Parto Precipitado (Taquitócico)*: Dilatação e descida completas em < 3 horas.
* **Cronômetro & Checklist HELPERR (Distócia de Ombros)**:
  - Cronômetro de emergência com contagem regressiva em relação ao tempo crítico de anóxia fetal (meta de resolução em < 5 minutos).
  - Checklist passo a passo das manobras: *Help, Evaluate for episiotomy, Legs (McRoberts), Pressure (Suprapubic), Enter maneuvers (Rubin/Woods), Remove posterior arm, Roll (Gaskin)*.
* **Calculadora de Índice de Choque e Protocolo de HPP**:
  - Calcula a razão FC / PAS (Normal < 0,9; Choque Imediato ≥ 0,9).
  - Estimativa de perda volêmica e indicação do protocolo de transfusão maciça (1:1:1).
  - **Validador de Segurança Farmacológica**: Opcional de hipertensão prévia alerta instantaneamente que **Metilergometrina é estritamente contraindicada**, evitando acidentes vasculares graves.
* **Calculadora da Escala de Depressão Pós-Parto de Edinburgh (EPDS)**:
  - Formulário interativo com escore total e alerta automático de risco de suicídio ou necessidade de intervenção psiquiátrica urgente.
* **Flashcards 3D Interativos**:
  - 8 cartões clínicos com efeito de rotação tridimensional abordando pontos de prova do USMLE Step 2/3 e Revalida.
* **Simulado USMLE Step 2 CK & Step 3**:
  - 10 vinhetas clínicas com justificativas detalhadas, explicação da resposta correta e dos distratores errados.
* **Modo Didático ("Explique como para uma criança de 5 anos")**:
  - Alternador global no cabeçalho que traduz termos complexos em analogias simples, perfeitas para fixação rápida da fisiopatologia.
* **Guia em Áudio (Web Speech API)**:
  - Leitura sintetizada em voz alta dos conceitos principais diretamente no navegador.
* **Busca Instantânea Inteligente (Ctrl + K)**:
  - Modal de pesquisa ultrarrápida com indexação de tópicos, procedimentos e termos clínicos.

---

## 🚀 Como Realizar o Deploy no GitHub Pages (Recomendado)

O site é 100% estático, autônomo, utiliza caminhos relativos para todos os assets e já inclui o arquivo `.nojekyll` para evitar o processamento do Jekyll pelo GitHub:

### Passo a Passo para o GitHub Pages:
1. Inicialize ou atualize o seu repositório no GitHub:
   ```bash
   git init
   git add .
   git commit -m "feat: site interativo de parto e puerperio - responsivo e alta legibilidade"
   git branch -M main
   git remote add origin https://github.com/<seu-usuario>/<nome-do-repositorio>.git
   git push -u origin main
   ```
2. Acesse o seu repositório no GitHub e vá em **Settings** (Configurações).
3. No menu lateral esquerdo, clique em **Pages**.
4. Na seção **Build and deployment > Source**, escolha **Deploy from a branch**.
5. No campo **Branch**, selecione `main` (ou `master`) e a pasta raiz `/ (root)`. Clique em **Save**.
6. Aguarde cerca de 1 a 2 minutos. O GitHub Pages publicará o site com certificado SSL automático no endereço:
   `https://<seu-usuario>.github.io/<nome-do-repositorio>/`

---

## ⚡ Como Realizar o Deploy no Netlify (Alternativa)

Você também pode publicar o site no Netlify através de 3 opções:

### Opção 1: Netlify Drop (Mais simples - Sem código)
1. Abra **[app.netlify.com/drop](https://app.netlify.com/drop)** no seu navegador.
2. Faça login na sua conta Netlify.
3. Arraste e solte a pasta **`site_parto_puerperio`** para a área indicada na tela.
4. O site será publicado imediatamente com link seguro HTTPS.

### Opção 2: Pelo Netlify CLI
```bash
cd "c:\Users\Admin\Downloads\INTERNATO GO\site_parto_puerperio"
npx netlify-cli deploy --prod --dir=.
```

### Opção 3: Conexão Git contínua via Netlify
Conecte o mesmo repositório do GitHub no painel do Netlify para deploy contínuo em cada commit.

---

## 🔍 Manutenção & Compilação Modular

Caso queira editar partes específicas do site de forma modular:
1. Altere o arquivo desejado dentro da pasta `components/` (ex: `components/modulo-17-hpp.html`).
2. Execute o script de montagem:
```bash
python scripts/build_site.py
```
3. O arquivo `index.html` será atualizado automaticamente com as alterações.
4. Para verificar se todos os links e imagens continuam íntegros:
```bash
python scripts/verify_site.py
```

---

*Desenvolvido com excelência pedagógica, rigor científico e tecnologia de ponta para a formação médica de alto nível.*
