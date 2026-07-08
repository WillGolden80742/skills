---
name: graphify-skill-router
description: "Skill router maestro que analisa o codebase via graphify e roteia para skills especializadas. ATIVADO EM QUALQUER TAREFA. Usa o knowledge graph para consultar e encontrar a skill apropriada."
triggers: ["", "*", "codigo", "code", "arquivo", "file", "projeto", "project", "tarefa", "task", "bug", "erro", "error", "feature", "funcao", "function", "classe", "class", "api", "database", "banco", "frontend", "backend", "fullstack", "script", "automacao", "automation", "teste", "test", "deploy", "docker", "git", "github", "wordpress", "theme", "plugin", "react", "vue", "node", "python", "php", "javascript", "typescript", "css", "html", "sql", "query", "refatorar", "refactor", "otimizar", "optimize", "performance", "seguranca", "security", "auth", "login", "crud", "create", "read", "update", "delete", "listar", "list", "mostrar", "show", "buscar", "search", "filtrar", "filter", "ordenar", "sort", "paginar", "pagination", "upload", "download", "export", "import", "pdf", "excel", "csv", "json", "xml", "yaml", "config", "configurar", "configure", "instalar", "install", "setup", "inicializar", "initialize", "build", "compilar", "compile", "run", "executar", "execute", "start", "stop", "restart", "debug", "log", "monitor", "alert", "notification", "email", "webhook", "websocket", "rest", "graphql", "microservico", "microservice", "monorepo", "library", "package", "dependency", "update", "upgrade", "migrate", "migration", "schema", "model", "controller", "service", "route", "middleware", "validator", "serializer", "view", "template", "component", "widget", "layout", "style", "design", "ui", "ux", "mobile", "responsive", "accessibility", "a11y", "seo", "cache", "session", "cookie", "header", "body", "request", "response", "status", "param", "path", "variable", "const", "let", "var", "async", "await", "promise", "callback", "event", "listener", "hook", "effect", "state", "store", "context", "provider", "consumer", "redux", "mobx", "vuex", "pinia", "db", "orm", "eloquent", "prisma", "sequelize", "typeorm", "mongodb", "mysql", "postgresql", "redis", "elasticsearch", "queue", "job", "worker", "cron", "scheduler", "logger", "monitoring", "tracing", "metrics", "ci", "cd", "pipeline", "jenkins", "actions", "gitlab", "docker", "kubernetes", "helm", "terraform", "ansible", "aws", "gcp", "azure", "cloud", "server", "hosting", "domain", "ssl", "tls", "https", "http", "dns", "cdn", "static", "dynamic", "ssr", "csr", "next", "nuxt", "remix", "sveltekit", "laravel", "django", "flask", "fastapi", "spring", "rails", "symfony", "codeigniter", "api", "rest", "graphql", "grpc", "telemetry", "logging", "alerting", "incident", "documentation", "docs", "readme", "changelog", "license", "contributing", "roadmap", "planning", "estimation", "scrum", "kanban", "agile", "vcs", "svn", "git", "branch", "checkout", "merge", "pull", "push", "fetch", "clone", "commit", "status", "diff", "log", "rebase", "reset", "revert", "tag", "release", "hotfix", "patch", "pr", "mr", "pullrequest", "review", "approve", "comment", "suggestion", "fix", "blocker", "critical", "major", "minor", "typo", "grammar", "style", "architecture", "refactor", "performance", "security", "bug", "vulnerability", "exploit", "injection", "xss", "csrf", "sqli", "ssrf", "encryption", "hashing", "tls", "ssl", "https", "ssh", "sftp", "certificate", "ca", "dns", "load", "balancing", "failover", "backup", "dr", "disaster", "recovery", "gc", "garbage", "collection", "memory", "leak", "allocation", "pool", "heap", "stack", "thread", "process", "concurrency", "parallel", "async", "await", "promise", "callback", "event", "listener", "hook", "middleware", "filter", "interceptor", "decorator", "proxy", "adapter", "facade", "singleton", "factory", "builder", "prototype", "observer", "pub/sub", "mvc", "mvvm", "flux", "redux", " CQRS", "event sourcing", "ddd", "domain driven design", "ubiquitous language", "bounded context", "aggregate", "entity", "value object", "repository", "unit of work", "domain event", "application service", "infrastructure", "persistence", "orm", "data mapper", "active record", "transaction", "lock", "semaphore", "mutex", "race condition", "deadlock", "livelock", "starvation", "priority inversion", "wait", "notify", "sleep", "yield", "park", "unpark", "blocking", "non-blocking", "synchronous", "asynchronous", "concurrent", "parallel", "distributed", "local", "remote", "network", "latency", "bandwidth", "throughput", "latency", "response time", "load time", "first byte", "time to", "first paint", "first contentful paint", "largest contentful paint", "cumulative layout shift", "speed index", "time to interactive", "total blocking time", "memory", "cpu", "gpu", "disk", "io", "network", "request", "response", "header", "body", "param", "query", "path", "variable", "constant", "function", "class", "interface", "trait", "enum", "struct", "union", "type", "generic", "template", "lambda", "closure", "curry", "compose", "pipe", "higher order function", "pure function", "side effect", "immutable", "mutable", "state", "副作用", "不可变", "并发", "并行", "分布式", "本地", "远程", "网络", "延迟", "带宽", "吞吐量"]
---

# Graphify Skill Router

Skill router maestro que usa **graphify para navegar pelo knowledge graph** e encontrar a skill mais apropriada para cada tarefa.

## Fluxo de Routing

```
Tarefa → [Graphify Query] → [Analisar Resultados] → [Skill Selection] → [Execute]
```

## Passo 1: Consultar o Knowledge Graph

Para cada tarefa, execute queries no graph para entender o contexto:

```bash
# Query 1: O que é este projeto?
graphify query "What is this project about? What technologies and frameworks does it use?"

# Query 2: Qual a estrutura de diretórios?
graphify query "What is the directory structure? What are the main components?"

# Query 3: Encontrar módulos relacionados à tarefa
graphify query "What files or modules are related to [TASK_KEYWORD]?"

# Query 4: Encontrar padrões existentes similares
graphify query "What patterns or implementations exist for [TASK_KEYWORD]?"

# Query 5: Encontrar dependências e conexões
graphify path "[EXISTING_MODULE]" "[TASK_MODULE]"
```

## Passo 2: Queries Comuns por Tipo de Tarefa

### Para tarefas de CRU D
```bash
graphify query "What are the database models and how are they structured?"
graphify query "What API endpoints exist for [RESOURCE]?"
graphify path "Database" "[RESOURCE]"
```

### Para tarefas de Frontend
```bash
graphify query "What frontend components and pages exist?"
graphify query "What is the state management approach?"
graphify path "Component" "[FEATURE]"
```

### Para tarefas de API/Backend
```bash
graphify query "What API routes and controllers exist?"
graphify query "What services handle business logic?"
graphify path "Controller" "[SERVICE]"
```

### Para tarefas de WordPress
```bash
graphify query "What WordPress theme or plugin files exist?"
graphify query "What custom post types and taxonomies are defined?"
graphify path "WordPress" "[FEATURE]"
```

### Para tarefas de Refatoração
```bash
graphify query "What code smells or technical debt exists?"
graphify query "What are the main classes and their responsibilities?"
graphify path "[OLD_IMPLEMENTATION]" "[NEW_IMPLEMENTATION]"
```

### Para tarefas de Performance
```bash
graphify query "What are the slow queries or bottlenecks?"
graphify query "What caching mechanisms exist?"
graphify path "Cache" "[FEATURE]"
```

### Para tarefas de Segurança
```bash
graphify query "What authentication and authorization mechanisms exist?"
graphify query "What are the security considerations?"
graphify path "Auth" "[FEATURE]"
```

## Passo 3: Mapear Resultados para Skills

Após consultar o graph, mapeie os resultados para skills:

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

## Passo 4: Executar a Skill

1. Carregue a skill recomendada
2. Execute as instruções
3. Retorne o resultado

## Exemplo de Routing

**Tarefa:** "Criar um componente de carousel em React"

```bash
# 1. Query para entender o projeto
$ graphify query "What frontend framework is used? React or Vue?"

# 2. Query para encontrar componentes existentes
$ graphify query "What existing React components exist?"

# 3. Query para padrões de componente
$ graphify query "What component patterns are used?"

# Resultado: Projeto usa React + shadcn/ui
# Skill recomendada: construir-artefatos-react
```

**Tarefa:** "Adicionar autenticação JWT ao WordPress"

```bash
# 1. Query para entender a estrutura WordPress
$ graphify query "What WordPress authentication exists?"

# 2. Query para encontrar ações/hooks
$ graphify query "What WordPress hooks and actions are used?"

# Resultado: WordPress theme com custom auth
# Skill recomendada: tema-marketplace-trokapay + boas-praticas-de-codigo
```

## Comandos de Router

```bash
# Listar todas as skills disponíveis
graphify query "What skills exist in this codebase?"

# Ver contexto do projeto atual
graphify query "What type of project is this? WordPress, React, Node, Python?"

# Encontrar skill para tarefa específica
graphify query "Which skill should I use for [TASK]?"

# Ver todas as conexões de um domínio
graphify path "[DOMAIN]" "[RELATED_DOMAIN]"
```

## Skills por Categoria

### 💻 Desenvolvimento & Frontend
- `construir-artefatos-react` - React components com Tailwind/shadcn
- `design-interface-usuario` - Design de interface
- `design-visual-artistico` - Arte visual e design artístico
- `placeholder-carregamento` - Skeleton screens com shimmer
- `arte-algoritmica-generativa` - Animação algorítmica com p5.js

### 📄 Documentos Office & PDF
- `criar-editar-apresentacao` - Apresentações PowerPoint
- `criar-editar-documento-word` - Documentos Word
- `criar-editar-planilhas-excel` - Planilhas Excel
- `processar-arquivos-pdf` - Processamento de PDFs

### 🗂️ Git, Arquivos & Projetos
- `comitar-alteracoes` - Commits com histórico
- `gerar-historico-commits` - Histórico de commits
- `recuperar-commits-salvos` - Recuperar commits
- `gerar-arvore-diretorios` - Árvore de diretórios
- `mesclar-arquivos-diretorio` - Mesclar arquivos
- `renomear-arquivos-referencias` - Renomear com refs
- `limpar-arquivos-dependencias` - Limpar dependências

### 🔌 Integração & Automação
- `construir-servidor-mcp` - Servidores MCP
- `buscar-grupos-whatsapp` - Bot WhatsApp
- `testar-aplicacoes-web` - Testes Playwright
- `capturar-screenshot-paginas` - Screenshots
- `extrair-conteudo-paginas` - Extrair conteúdo web
- `autenticar-github-device-flow` - GitHub auth

### 📝 Comunicação & Documentação
- `coautoria-documentacao-tecnica` - Documentação técnica
- `comunicados-internos-empresa` - Comunicados internos
- `diretrizes-marca-anthropic` - Marca Anthropic

### 🎨 Design & Visual
- `aplicar-temas-cores-fontes` - Temas de cores e fontes
- `criar-gifs-animados-slack` - GIFs para Slack

### 🛠️ Meta — Gestão de Skills
- `criar-novo-skill` - Criar nova skill
- `gerenciar-remover-skills` - Gerenciar skills

### 🧩 Skills de Projeto Específico
- `tema-marketplace-trokapay` - WordPress marketplace
- `graphify` - Knowledge graph ( sempre disponível)

## Regras de Fallback

1. **Se nenhuma skill específica for encontrada** → Use `graphify update` + `graphify query`
2. **Se o graph não existir** → Execute `graphify update .` primeiro
3. **Se a tarefa for ambígua** → Consulte múltiplas skills em paralelo

## Integração com Buildify

O agente `buildify` já executa `graphify update .` antes de codar. Use o graph já construído para fazer routing inteligente:

```bash
# Verificar se graph existe
ls graphify-out/graph.json

# Fazer query
graphify query "[SUA_PERGUNTA]"
```
