# OpenCode Skills

Repositório de skills especializados para o OpenCode — agentes que executam tarefas específicas com expertise especializada.

Inclui skills originais + [mattpocock/skills](https://github.com/mattpocock/skills) (TypeScript-first).

## 📁 Estrutura do Projeto

```
skills/
├── graphify/                          # Knowledge graph do codebase
├── graphify-skill-router/             # Router maestro de skills
├── buildify/                          # Agente buildify (graphify + codificar)
├── editar-skill/                      # Editar skill existente
├── criar-novo-skill/                  # Criar novo skill
├── gerenciar-remover-skills/          # Remover/atualizar skills
│
├── commits/                           # Histórico de commits (yyyy/mm/dd/)
├── graphify-out/                      # Grafo gerado automaticamente
│
├── engineering/                       # mattpocock: engenharia de código
├── productivity/                      # mattpocock: produtividade
├── deprecated/                        # mattpocock: skills depreciados
├── in-progress/                       # mattpocock: em desenvolvimento
├── misc/                              # mattpocock: diversos
├── personal/                          # mattpocock: uso pessoal
│
└── [skills originais]/
```

## 🎯 Skills por Categoria

### 🛠️ Meta — Gestão de Skills

| Skill | Descrição |
|-------|-----------|
| `criar-novo-skill` | Cria um novo skill para o opencode a partir de um template padrão |
| `editar-skill` | Edita uma skill existente — altera conteúdo, triggers, descrição e re-gerencia AST |
| `gerenciar-remover-skills` | Remove ou atualiza skills que não ficaram boas o suficiente |
| `graphify` | Knowledge graph do codebase — query/path/explain AST-only, zero cost |
| `graphify-skill-router` | Router maestro que analisa o codebase via graphify e navega pelos AST JSON |
| `buildify` | Agente buildify que executa graphify update antes de codar |

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

```
Tarefa do usuário
       ↓
[1] Atualizar Knowledge Graph (graphify update)
       ↓
[2] Consultar o Grafo (graphify query)
       ↓
[3] Analisar AST dos Markdown (graphify --markdown-ast)
       ↓
[4] Mapear para Skill Apropriada
       ↓
Skill executa a tarefa
```

## 🚀 Uso Rápido

```bash
# Carregar um skill
/skill <nome-do-skill>

# Exemplos:
/skill criar-editar-documento-word
/skill graphify query "como funciona a autenticação?"
/skill criar-novo-skill
/skill engineering/domain-modeling
/skill productivity/teach
```

## 📊 Estatísticas

- **Total de skills**: 60+
- **Categorias**: 10
- **Origens**: originais + mattpocock/skills
- **Grafo**: AST-only extraction (zero cost)

---

_Fonte: [mattpocock/skills](https://github.com/mattpocock/skills) | Atualizado automaticamente via graphify-skill-router_
