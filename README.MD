# Skills - OpenCode

Coleção de **skills para o [OpenCode](https://opencode.ai)** — módulos de conhecimento e automação que estendem o agente com fluxos de trabalho prontos: geração de documentos Office, design visual, automação web, integração com WhatsApp/MCP, gestão de Git e organização de projetos.

Cada skill vive em `~/.config/opencode/skills/<nome-da-skill>/` e é descoberta automaticamente pelo OpenCode através de um arquivo `SKILL.md` com front-matter (`name`, `description`, `triggers`).

## Instalação

Clone o repositório diretamente dentro da pasta de skills do OpenCode:

```bash
# Linux / macOS
git clone https://github.com/WillGolden80742/skills.git ~/.config/opencode/skills

# Windows
git clone https://github.com/WillGolden80742/skills.git "%USERPROFILE%\.config\opencode\skills"
```

Se já existir uma pasta `skills` local, copie apenas as subpastas desejadas para dentro de `~/.config/opencode/skills/`.

## Como funciona uma skill

```
skills/
├── nome-da-skill/
│   ├── SKILL.md           # obrigatório: front-matter + instruções
│   ├── SKILL.json        # AST extraído automaticamente
│   ├── scripts/           # scripts auxiliares (opcional)
│   └── templates/         # templates/exemplos (opcional)
```

`SKILL.md` segue o formato:

```yaml
---
name: nome-da-skill
description: descrição de uma linha sobre o que a skill faz.
triggers: ["palavra-chave-1", "frase gatilho 2", ...]
---

## What I do
...

## Usage
...
```

Quando uma mensagem do usuário casa com algum `trigger`, o OpenCode carrega o conteúdo da skill correspondente como contexto adicional para o agente.

## Agente Buildify

O agente **buildify** executa `graphify update` antes de qualquer tarefa de codificação:

```bash
# Ativar buildify
# O agente automaticamente executa graphify update antes de codar
```

**Workflow:**
```
Tarefa → graphify update → graphify query → Implementar → graphify update
```

## Skills disponíveis

### 🛠️ Meta — Gestão de Skills

| Skill | Descrição |
|-------|-----------|
| `buildify` | Agente buildify que executa graphify antes de codar |
| `criar-novo-skill` | Cria uma nova skill a partir de um template padrão |
| `editar-skill` | Edita uma skill existente — conteúdo, triggers, descrição |
| `gerenciar-remover-skills` | Lista, atualiza ou remove skills existentes |
| `markdown-to-ast` | Converte arquivos .md em AST JSON (mesmo nome/diretório) |
| `graphify-skill-router` | Router que usa graphify para navegar e encontrar skills |

### 💻 Desenvolvimento & Frontend

| Skill | Descrição |
|-------|-----------|
| `graphify` | Knowledge graph persistente (AST-only, zero custo) |
| `construir-artefatos-react` | Cria artefatos HTML com React, Tailwind CSS, shadcn/ui |
| `testar-aplicacoes-web` | Toolkit de testes locais com Playwright |
| `capturar-screenshot-paginas` | Captura screenshots de páginas web via Playwright |
| `refatorar-css-variaveis` | Refatora CSS para usar variáveis CSS no `:root` |
| `reverter-css-variaveis` | Reverte CSS com variáveis `:root` para valores diretos |
| `construir-servidor-mcp` | Guia para criar servidores MCP (Python/Node) |
| `boas-praticas-de-codigo` | Boas práticas de OOP, Object Calisthenics, MVC |

### 📄 Documentos Office & PDF

| Skill | Descrição |
|-------|-----------|
| `criar-editar-apresentacao` | Cria e edita apresentações PowerPoint (.pptx) |
| `criar-editar-documento-word` | Cria e edita documentos Word (.docx) |
| `criar-editar-planilhas-excel` | Manipula planilhas Excel (.xlsx, .xlsm, .csv, .tsv) |
| `processar-arquivos-pdf` | Lê, extrai texto/tabelas, mescla, divide e cria PDFs |

### 🎨 Design & Visual

| Skill | Descrição |
|-------|-----------|
| `aplicar-temas-cores-fontes` | Aplica temas de cores e fontes profissionais (10 temas) |
| `design-interface-usuario` | Design visual distintivo para UI |
| `design-visual-artistico` | Cria designs visuais artísticos em PNG/PDF |
| `diretrizes-marca-anthropic` | Aplica cores e tipografia oficial da Anthropic |
| `arte-algoritmica-generativa` | Cria arte algorítmica com p5.js |
| `criar-gifs-animados-slack` | Cria GIFs animados otimizados para Slack |
| `placeholder-carregamento` | Gera skeleton screens com shimmer animation |

### 🗂️ Git, Arquivos & Projetos

| Skill | Descrição |
|-------|-----------|
| `comitar-alteracoes` | Cria commits Git com histórico timestampado |
| `gerar-historico-commits` | Gera histórico de commits em `commits/yyyy/mm/dd/` |
| `recuperar-commits-salvos` | Recupera e exibe commits salvos |
| `gerar-arvore-diretorios` | Gera árvore de diretórios em Markdown |
| `mesclar-arquivos-diretorio` | Mescla arquivos de um diretório em um único arquivo |
| `renomear-arquivos-referencias` | Renomeia arquivos e atualiza referências |
| `limpar-arquivos-dependencias` | Remove dependências (vendor, npm, etc.) |

### 🔌 Integração & Automação

| Skill | Descrição |
|-------|-----------|
| `autenticar-github-device-flow` | Autentica GitHub via device flow |
| `delegar-tarefas` | Delega tarefas para o agente "agy" |
| `extrair-conteudo-paginas` | Extrai conteúdo de páginas web (Mozilla Readability) |
| `configurar-espelhamento-server` | Espelhamento bidirecional local ↔ servidor via SSH/SFTP |

### 📝 Comunicação & Documentação

| Skill | Descrição |
|-------|-----------|
| `comunicados-internos-empresa` | Cria comunicações internas — relatórios, newsletters, FAQs |
| `coautoria-documentacao-tecnica` | Workflow estruturado de co-autoria de documentação |

### 🛒 E-commerce & Marketplace

| Skill | Descrição |
|-------|-----------|
| `tema-marketplace-trokapay` | Tema WordPress marketplace com WooCommerce e WhatsApp |

## Grafo Interativo

Visualize o grafo de conhecimento do projeto:

```
graphify-out/graph.html
```

Comando para atualizar:
```bash
graphify update .
```

## Criando uma nova skill

```bash
python3 ~/.config/opencode/skills/criar-novo-skill/skillFactory.py
```

O script pede, em sequência:
1. Nome da skill (hífens, sem espaços)
2. Descrição
3. Triggers (separados por vírgula)
4. Conteúdo do skill

Após criar, o AST JSON é gerado automaticamente.

## Editando uma skill existente

```bash
python3 ~/.config/opencode/skills/editar-skill/editSkillFactory.py
```

Lista todas as skills, permite selecionar e editar.

## Gerando AST dos Markdown

```bash
# Gerar AST para todo o projeto
python3 ~/.config/opencode/skills/markdown-to-ast/md_to_ast.py --path .

# Gerar AST para uma skill específica
python3 ~/.config/opencode/skills/markdown-to-ast/md_to_ast.py --path criar-novo-skill/SKILL.md
```

Cada `.md` gera um `.json` correspondente no mesmo diretório.

## Comitar alterações

```bash
python3 ~/.config/opencode/skills/comitar-alteracoes/comit.py --message "feat: nova funcionalidade"
```

Fluxo:
1. Mostra diff e pede confirmação
2. Commita com mensagem
3. Gera AST para todos os `.md`
4. Commita AST gerados
5. Atualiza graphify-out
6. Push

## Licença

Algumas skills (baseadas em ferramentas públicas de criação de documentos, apresentações e artefatos) são distribuídas sob **Apache License 2.0** — veja o `LICENSE.txt` dentro de cada pasta de skill correspondente. As demais skills são de uso pessoal/interno.