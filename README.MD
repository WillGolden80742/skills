# OpenCode Skills — Foco Adianti Framework 🇧🇷

> Branch `skills-adianti`: este repositório + **337 skills `adianti-*`** geradas do **Adianti Tutor 8.7** — cobertura total do que o Tutor ensina a fazer, validadas rodando no Tutor real (`228/228` páginas e diálogos verificados via Playwright).

## 🧱 As 337 skills Adianti

| Origem | Qtd | O que é |
|---|---|---|
| Classes do `menu.xml` (Persistência, Apresentação, Organização) | 228 | 1 skill por função do menu: Conexões, Objetos, Coleções, Relacionamentos, Páginas, Contêineres, Diálogos, Formulários, Datagrids, Utilitários, Relatórios, Gráficos, Etiquetas, Templates, Extras, Cadastros, Lote, Checkout, Interações |
| Views ensináveis fora do menu | 47 | CartManagement, HelloWorld×4, QuickForms, MultiStep 2-4, CitySeek, SplitLeft/Right, forms de Kanban/Gantt/Calendário… |
| Exemplos executáveis `dbsamples` | 48 | `Object*`, `Collection*`, `Manual*`, `RegisterLog*` — o código que roda por trás das telas de Persistência |
| Skills agrupadas por tema | 13 | `adianti-persistencia-*`, `adianti-apresentacao-*`, `adianti-organizacao-*` — visão consolidada por assunto |
| Demo | 1 | `adianti-dialog-toast` |

### Cobertura por submenu (cards do Tutor → skills)

Persistência: Conexões 7 · Objetos 17 · Coleções 20 · Relacionamentos 6 — Apresentação: Páginas 14 · Contêineres 14 · Diálogos 7 · Formulários 26 · Datagrids 22 · Utilitários 15 · Relatórios 8 · Gráficos 5 · Etiquetas 3 · Templates 8 · Extras 20 — Organização: Padronizados 6 · Manuais 3 · Completos 7 · Consulta 2 · Lote 6 · Checkout 2 · Interações 3 · Utilitários 7.

### Anatomia de uma skill `adianti-*`

```
adianti-<classe>/
├── SKILL.md    # frontmatter (name/description/triggers) + código-fonte do Tutor + footer prático
└── SKILL.json  # AST do markdown (graphify-skill-router)
```

- `name` sempre com prefixo `adianti-*`; `triggers` incluem a classe (`TToast`, `TDataGrid`…), o caminho do menu e palavras-chave.
- Footer padrão **“Uso no seu projeto”**: copiar para a pasta `app/` (seu sistema decide control/model/etc.), trocar banco `samples` e modelos, testar antes de produzir.
- 5 skills carregam `Nota:` honesta (exigem registro em `menu.xml` ou rename arquivo para rodar standalone).

## 🎯 Skills por Categoria

### 🛠️ Meta — Gestão de Skills

| Skill | Descrição |
|-------|-----------|
| `criar-novo-skill` | Cria um novo skill para o opencode a partir de um template padrão |
| `editar-skill` | Edita uma skill existente — altera conteúdo, triggers, descrição e re-gerencia AST |
| `gerenciar-remover-skills` | Remove ou atualiza skills que não ficaram boas o suficiente |
| `graphify` | Knowledge graph EXCLUSIVO para indexação e busca do repositório de skills |
| `graphify-skill-router` | Router maestro que consulta o grafo de skills para encontrar a skill apropriada |
| `buildify` | Agente buildify — usa graphify-skill-router FIRST antes de tudo e segue procedimento padrão (grep, find, read) para código |

### 💻 Desenvolvimento & Frontend

| Skill | Descrição |
|-------|-----------|
| `construir-artefatos-react` | Cria artefatos HTML complexos com React, Tailwind CSS e shadcn/ui |
| `construir-servidor-mcp` | Cria servidores MCP (Model Context Protocol) para integrar APIs/serviços externos |
| `boas-praticas-de-codigo` | Boas práticas de OOP, Object Calisthenics, MVC e filosofia Rails |
| `placeholder-carregamento` | Gera skeleton screens com shimmer animation para componentes WordPress |
| `testar-aplicacoes-web` | Toolkit para testar aplicações web locais usando Playwright |
| `capturar-screenshot-paginas` | Captura screenshots de páginas web usando Playwright |

### 🎨 Design & Visual

| Skill | Descrição |
|-------|-----------|
| `design-interface-usuario` | Design visual distintivo para UI — estética, tipografia |
| `design-visual-artistico` | Cria designs visuais artístico em PNG e PDF |
| `aplicar-temas-cores-fontes` | Aplica temas de cores e fontes profissionais a slides e artefatos |
| `diretrizes-marca-anthropic` | Aplica cores e tipografia oficial da Anthropic |
| `arte-algoritmica-generativa` | Cria arte algorítmica usando p5.js com aleatoriedade controlada |
| `criar-gifs-animados-slack` | Cria GIFs animados otimizados para Slack |

### 📄 Documentos Office & PDF

| Skill | Descrição |
|-------|-----------|
| `criar-editar-documento-word` | Cria, lê e edita documentos Word (.docx) |
| `criar-editar-planilhas-excel` | Manipula arquivos de planilhas Excel (.xlsx, .xlsm, .csv, .tsv) |
| `criar-editar-apresentacao` | Cria e edita apresentações PowerPoint (.pptx) |
| `processar-arquivos-pdf` | Processa PDFs — ler, extrair texto/tabelas, mesclar, dividir, criar |

### 🗂️ Git, Arquivos & Projetos

| Skill | Descrição |
|-------|-----------|
| `comitar-alteracoes` | Cria commits Git com histórico timestampado em commits/ |
| `gerar-historico-commits` | Gera arquivos de histórico de commits do Git (yyyy/mm/dd/) |
| `recuperar-commits-salvos` | Recupera e exibe os comentários das últimas alterações commitadas |
| `gerar-arvore-diretorios` | Cria árvore de diretórios em Markdown (.md) de um projeto |
| `mesclar-arquivos-diretorio` | Mescla arquivos de um diretório em um único arquivo de saída |
| `renomear-arquivos-referencias` | Renomeia arquivo e atualiza todas as referências no projeto |
| `limpar-arquivos-dependencias` | Remove arquivos, diretórios e dependências de projetos |
| `configurar-espelhamento-server` | Espelhamento bidirecional seguro entre pasta local e servidor Linux |

### 🌐 Web & Extrações

| Skill | Descrição |
|-------|-----------|
| `extrair-conteudo-paginas` | Extrai conteúdo de páginas web usando Mozilla Readability |
| `autenticar-github-device-flow` | Autentica GitHub via device flow em ambientes sem token |

### 📝 Documentação & Comunicação

| Skill | Descrição |
|-------|-----------|
| `coautoria-documentacao-tecnica` | Workflow estruturado para co-autoria de documentação |
| `comunicados-internos-empresa` | Cria comunicações internas — relatórios, newsletters, FAQs |

### 🧩 CSS & Estilização

| Skill | Descrição |
|-------|-----------|
| `refatorar-css-variaveis` | Refatora CSS para usar variáveis CSS (:root) |
| `reverter-css-variaveis` | Reverte CSS com variáveis (:root) de volta para valores diretos |

### ⚙️ Engineering (mattpocock)

| Skill | Descrição |
|-------|-----------|
| `ask-matt` | Faz perguntas ao Matt sobre código/decisões |
| `codebase-design` | Desenhar a arquitetura de um codebase |
| `code-review` | Revisar código com foco em TypeScript/boas práticas |
| `diagnosing-bugs` | Diagnosticar e corrigir bugs em código existente |
| `domain-modeling` | Modelar domínios de negócio com tipos TypeScript |
| `grill-with-docs` | Investigar código usando documentação como referência |
| `implement` | Implementar funcionalidades a partir de specs |
| `improve-codebase-architecture` | Melhorar a arquitetura de codebases existentes |
| `prototype` | Criar protótipos rápidos de funcionalidades |
| `research` | Pesquisar tecnologias, bibliotecas e soluções |
| `resolving-merge-conflicts` | Resolver conflitos de merge no Git |
| `setup-matt-pocock-skills` | Configurar o ambiente de skills do Matt |
| `tdd` | Desenvolvimento orientado a testes (TDD) |
| `to-spec` | Converter requisitos em specifications técnicas |
| `to-tickets` | Converter specs em tickets de tarefa |
| `triage` | Triagem e priorização de issues |
| `wayfinder` | Navegar por codebases desconhecidos |

### 🚀 Productivity (mattpocock)

| Skill | Descrição |
|-------|-----------|
| `grilling` | Fazer perguntas profundas sobre código/arquitetura |
| `grill-me` | Auto-reflexão e revisão de decisões técnicas |
| `handoff` | Entregar trabalho de forma estruturada |
| `teach` | Ensinar conceitos técnicos de forma clara |
| `writing-great-skills` | Escrever skills eficazes para agentes |

### ⚰️ Deprecated (mattpocock)

| Skill | Descrição |
|-------|-----------|
| `design-an-interface` | Desenhar interfaces de usuário |
| `qa` | Quality assurance e testes |
| `request-refactor-plan` | Solicitar planos de refatoração |
| `ubiquitous-language` | Estabelecer linguagem ubíqua no domínio |

## 🔄 Fluxo de Routing (graphify-skill-router)

> **Nota:** Graphify é usado **EXCLUSIVAMENTE** no repositório de skills. Projetos e codebases externos seguem o procedimento padrão (grep, find, leitura direta).

```
Tarefa do usuário
       ↓
[1] Consultar Grafo de Skills (graphify query --graph ~/.config/opencode/skills/graphify-out/graph.json)
       ↓
[2] Encontrou Skill Especializada?
       ├── SIM → Carrega e executa a Skill
       └── NÃO → Segue procedimento padrão de desenvolvimento (grep, find, read, testes)
```

## 🚀 Uso Rápido

```bash
# Skills Adianti:
/skill adianti-dialogtoastview     # Toast com TToast::show
/skill adianti-saleform             # Mestre-detalhe de vendas
/skill adianti-persistencia-colecoes-criteria   # TCriteria/TFilter/TRepository
/skill adianti-apresentacao-datagrids           # Datagrids completas

# Skills Gerais:
/skill criar-editar-documento-word
/skill criar-novo-skill
/skill engineering/domain-modeling
/skill productivity/teach
```

Ou deixe o router achar: `graphify query "toast notification which skill handles this?" --graph ~/.config/opencode/skills/graphify-out/graph.json`.

## 🔄 Regenerar / auditar

```bash
python3 gerar_skill.py --classe DialogToastView --nome adianti-dialog-toast \
  --descricao "..." --triggers "TToast,toast" --dest .
python3 gerar_skill.py --batch --menu-xml menu.xml --min-bytes 1024
graphify update ~/.config/opencode/skills
```

Auditoria: `menu.xml` (228) + SearchBox ao vivo (228, idêntico) + classes declaradas em `app/control` (336). Fora da cobertura, por decisão: `SearchBox`, `HomeView`, `Trash/*`, `util/*` (infraestrutura, não conteúdo ensinável).

---

## 📁 Restante do repositório (base `main`)

Skills originais + [mattpocock/skills](https://github.com/mattpocock/skills) (TypeScript-first): meta (`criar-novo-skill`, `editar-skill`, `graphify-skill-router`, `buildify`), frontend, Office/PDF, git, design, web e engineering/productivity do Matt. Estrutura e categorias originais preservadas da `main`.

## 📊 Estatísticas (branch `skills-adianti`)

- **Skills `adianti-*`**: 337 (228 menu + 47 views + 48 dbsamples + 13 agrupadas + 1 demo)
- **Grafo**: AST-only extraction (zero cost), `SKILL.json` em todas
- **Validação**: 228/228 páginas e view-sources verificados no Tutor real, 0 `Deprecated`
