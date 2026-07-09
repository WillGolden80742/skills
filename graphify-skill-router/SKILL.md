---
name: graphify-skill-router
description: "Skill router maestro que analisa o codebase via graphify e navega pelos AST JSON de cada .md. Usa o knowledge graph para consultar e encontrar a skill apropriada."
triggers: ["", "*", "codigo", "code", "arquivo", "file", "projeto", "project", "tarefa", "task", "bug", "erro", "error", "feature", "funcao", "function", "classe", "class", "api", "database", "banco", "frontend", "backend", "fullstack", "script", "automacao", "automation", "teste", "test", "deploy", "docker", "git", "github", "wordpress", "theme", "plugin", "react", "vue", "node", "python", "php", "javascript", "typescript", "css", "html", "sql", "query", "refatorar", "refactor", "otimizar", "optimize", "performance", "seguranca", "security", "auth", "login", "crud", "create", "read", "update", "delete", "listar", "list", "mostrar", "show", "buscar", "search", "filtrar", "filter", "ordenar", "sort", "paginar", "pagination", "upload", "download", "export", "import", "pdf", "excel", "csv", "json", "xml", "yaml", "config", "configurar", "configure", "instalar", "install", "setup", "inicializar", "initialize", "build", "compilar", "compile", "run", "executar", "execute", "start", "stop", "restart", "debug", "log", "monitor", "alert", "notification", "email", "webhook", "websocket", "rest", "graphql", "microservico", "microservice", "monorepo", "library", "package", "dependency", "update", "upgrade", "migrate", "migration", "schema", "model", "controller", "service", "route", "middleware", "validator", "serializer", "view", "template", "component", "widget", "layout", "style", "design", "ui", "ux", "mobile", "responsive", "accessibility", "a11y", "seo", "cache", "session", "cookie", "header", "body", "request", "response", "status", "param", "path", "variable", "const", "let", "var", "async", "await", "promise", "callback", "event", "listener", "hook", "effect", "state", "store", "context", "provider", "consumer", "redux", "mobx", "vuex", "pinia", "db", "orm", "eloquent", "prisma", "sequelize", "typeorm", "mongodb", "mysql", "postgresql", "redis", "elasticsearch", "queue", "job", "worker", "cron", "scheduler", "logger", "monitoring", "tracing", "metrics", "ci", "cd", "pipeline", "jenkins", "github actions", "web", "page", "url", "link", "navigation", "menu", "form", "input", "button", "modal", "dropdown", "table", "grid", "chart", "graph", "tree", "modal", "popup", "toast", "notification", "skeleton", "loading", "spinner", "progress", "badge", "tag", "chip", "avatar", "icon", "image", "video", "audio", "upload", "file", "folder", "directory", "path", "skill", "knowledge", "markdown", "docs", "documentation"]
---

# Graphify Skill Router

Skill router maestro que usa **graphify para navegar pelo knowledge graph** e encontrar a skill mais apropriada para cada tarefa. Agora com suporte a **AST JSON** de arquivos markdown.

## Estrutura de AST

Cada arquivo `.md` tem um `.json` correspondente com a estrutura AST:

```
skill.md      →  skill.json
README.MD     →  README.json
dir/file.md   →  dir/file.json
```

### Estrutura do AST JSON

```json
{
  "source": "/path/to/arquivo.md",
  "generated_at": "2026-07-08T21:11:12",
  "nodes": [
    {"id": "md_SKILL_h1_0", "label": "Titulo", "type": "heading", "level": 1, "file": "...", "community": 999},
    {"id": "md_SKILL_h2_1", "label": "Subtitulo", "type": "heading", "level": 2, "file": "...", "community": 999},
    {"id": "md_SKILL_code_2", "label": "Code: python", "type": "code_block", "language": "python", "file": "...", "community": 999},
    {"id": "md_SKILL_link_3", "label": "Link Text", "type": "link", "url": "https://...", "file": "...", "community": 999},
    {"id": "md_SKILL_list_4", "label": "Item de lista", "type": "list_item", "file": "...", "community": 999}
  ],
  "edges": [
    {"from": "md_SKILL_h1_0", "to": "md_SKILL_h2_1", "relation": "section"},
    {"from": "md_SKILL_h1_0", "to": "md_SKILL_code_2", "relation": "contains"}
  ]
}
```

### Tipos de Node

| Type | Descrição |
|------|-----------|
| `heading` | Títulos (# h1 a ###### h6) |
| `code_block` | Blocos de código (```) |
| `link` | Links ([text](url)) |
| `image` | Imagens (![alt](src)) |
| `list_item` | Itens de lista (-, *, +) |

### Relações (Edges)

| Relation | Descrição |
|----------|-----------|
| `section` | Relação hierárquica entre headings (h1 → h2 → h3) |
| `contains` | Elemento contenido em uma seção |

## Fluxo de Routing

```
Tarefa → [Graphify Query] → [Consultar AST JSON] → [Skill Selection] → [Execute]
```

## Passo 1: Atualizar o Knowledge Graph

Execute graphify para construir/atualizar o grafo:

```bash
# Atualizar grafo de código
graphify update .

# Navegar grafo interativo
# Abra: graphify-out/graph.html
```

## Passo 2: Consultar o Knowledge Graph

Para cada tarefa, execute queries no graph:

```bash
# Query 1: O que é este projeto?
graphify query "What is this project about?"

# Query 2: Qual a estrutura de diretórios?
graphify query "What is the directory structure?"

# Query 3: Encontrar módulos relacionados à tarefa
graphify query "What files are related to [TASK_KEYWORD]?"

# Query 4: Encontrar padrões existentes
graphify query "What patterns exist for [TASK_KEYWORD]?"

# Query 5: Encontrar conexões entre módulos
graphify path "[MODULE_A]" "[MODULE_B]"
```

## Passo 3: Consultar AST dos Markdown

Use os JSONs AST para entender estrutura de documentação:

```bash
# Ler AST de um arquivo específico
cat skill/SKILL.json

# Procurar headings específicos
grep '"type": "heading"' **/*.json

# Procurar code blocks
grep '"type": "code_block"' **/*.json

# Procurar por linguagem de código
grep '"language": "python"' **/*.json
```

### Queries Úteis via grep/jq

```bash
# Listar todos os títulos (h1, h2, h3)
grep -r '"type": "heading"' . --include="*.json" | jq -r '.[] | select(.level <= 2) | .label'

# Listar todos os code blocks
grep -r '"type": "code_block"' . --include="*.json"

# Buscar por linguagem específica
grep -r '"language": "python"' . --include="*.json"

# Listar links externos
grep -r '"type": "link"' . --include="*.json" | grep 'http'

# Ver estrutura de uma skill
cat criar-novo-skill/SKILL.json | jq '.nodes[] | select(.type == "heading")'
```

## Passo 4: Mapear Resultados para Skills

| Resultado da Query | Skill Recomendada |
|-------------------|-------------------|
| "React", "Component", "JSX" | `construir-artefatos-react` |
| "WordPress", "theme", "plugin" | `tema-marketplace-trokapay` |
| "database", "model", "ORM" | `boas-praticas-de-codigo` |
| "API", "endpoint", "route" | `boas-praticas-de-codigo` |
| "CSS", "style", "design" | `design-interface-usuario` |
| "document", "report", "spec" | `coautoria-documentacao-tecnica` |
| "Excel", "spreadsheet", "data" | `criar-editar-planilhas-excel` |
| "PDF", "report", "invoice" | `processar-arquivos-pdf` |
| "commit", "git", "history" | `comitar-alteracoes` |
| "test", "spec", "assert" | `testar-aplicacoes-web` |
| "Docker", "container", "deploy" | `limpar-arquivos-dependencias` |
| "mcp", "tool", "integration" | `construir-servidor-mcp` |
| "animation", "canvas", "visual" | `arte-algoritmica-generativa` |
| "WhatsApp", "message", "group" | `buscar-grupos-whatsapp` |
| "skill", "create", "new" | `criar-novo-skill` |
| "skill", "edit", "modify" | `editar-skill` |
| "markdown", "ast", "structure" | `markdown-to-ast` |

## Gerar/Atualizar AST dos Markdown

```bash
# Gerar AST para todos os .md do projeto
python3 markdown-to-ast/md_to_ast.py --path .

# Gerar AST para uma skill específica
python3 markdown-to-ast/md_to_ast.py --path criar-novo-skill/SKILL.md

# Modo verbose
python3 markdown-to-ast/md_to_ast.py --path . --verbose

# Dry-run (ver sem salvar)
python3 markdown-to-ast/md_to_ast.py --path . --dry-run
```

## Exemplo de Routing Completo

**Tarefa:** "Documentar uma nova API REST"

```bash
# 1. Atualizar grafo
graphify update .

# 2. Consultar estrutura existente
graphify query "What API routes and controllers exist?"

# 3. Ver AST dos documentos existentes
cat coautoria-documentacao-tecnica/SKILL.json | jq '.nodes[] | select(.type == "heading")'

# 4. Resultado: Skill recomendada: coautoria-documentacao-tecnica
```

**Tarefa:** "Criar uma nova skill"

```bash
# 1. Ver templates de skills existentes
ls */SKILL.json | head -5

# 2. Ver estrutura de uma skill
cat criar-novo-skill/SKILL.json | jq '.nodes'

# 3. Criar a skill
python3 criar-novo-skill/skillFactory.py

# 4. Gerar AST automaticamente (já integrado)
```

## Skills por Categoria

### 🛠️ Meta — Gestão de Skills
- `criar-novo-skill` - Criar nova skill
- `editar-skill` - Editar skill existente
- `gerenciar-remover-skills` - Gerenciar skills
- `markdown-to-ast` - Gerar AST dos markdown

### 💻 Desenvolvimento & Frontend
- `construir-artefatos-react` - React components
- `testar-aplicacoes-web` - Testes Playwright
- `refatorar-css-variaveis` - CSS variables
- `reverter-css-variaveis` - Reverter CSS

### 📄 Documentos Office & PDF
- `criar-editar-apresentacao` - PowerPoint
- `criar-editar-documento-word` - Word
- `criar-editar-planilhas-excel` - Excel
- `processar-arquivos-pdf` - PDFs

### 🗂️ Git, Arquivos & Projetos
- `comitar-alteracoes` - Commits
- `gerar-historico-commits` - Histórico
- `gerar-arvore-diretorios` - Árvore dir
- `mesclar-arquivos-diretorio` - Mesclar
- `renomear-arquivos-referencias` - Renomear

### 🎨 Design & Visual
- `aplicar-temas-cores-fontes` - Temas
- `design-interface-usuario` - UI design
- `arte-algoritmica-generativa` - Arte p5.js

## Comandos de Router

```bash
# Ver todas as skills disponíveis
graphify query "What skills exist?"

# Ver tipo do projeto
graphify query "What type of project is this?"

# Encontrar skill para tarefa
graphify query "Which skill for [TASK]?"

# Ver conexões de domínio
graphify path "[DOMAIN_A]" "[DOMAIN_B]"

# Listar AST JSONs disponíveis
find . -name "*.json" -path "*/skills/*" | head -20
```

## Regras de Fallback

1. **Se nenhuma skill específica for encontrada** → Use `graphify update` + `graphify query`
2. **Se o graph não existir** → Execute `graphify update .` primeiro
3. **Se a tarefa for ambígua** → Consulte múltiplas skills em paralelo
4. **Se precisar entender estrutura de docs** → Consulte os `.json` AST correspondentes
