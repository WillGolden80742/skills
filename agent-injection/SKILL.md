---
name: agent-injection
description: Cria e injeta o agente buildify no sistema OpenCode com abordagem graph-first + skill-router (sempre pergunta "existe skill para isto?" via graphify no repo de skills antes de qualquer ação)
triggers: ["buildify", "agent-injection", "injetar agente", "criar agente buildify"]
---

# Agent Injection

Skill responsável por criar e injetar o agente **buildify** no sistema OpenCode.

## O que faz

1. Cria o agente buildify em `/root/.config/opencode/agents/buildify.md`
2. Define o agente como **primary** no sistema OpenCode
3. Configura as permissões necessárias
4. Implementa a abordagem **graph-first** (consulta grafo antes de grep)

## Agente Buildify

O agente buildify é definido com a seguinte configuração:

```yaml
---
description: Agente buildify — antes de TUDO pergunta "existe skill para isto?" via graphify no repo de skills, depois graphify no codebase antes de codar
mode: primary
permission:
  edit: allow
  bash: allow
  read: allow
  glob: allow
  grep: allow
  list: allow
  task: allow
  todowrite: allow
  webfetch: allow
  websearch: allow
---
```

## Regras do Buildify

### MANDATORY STEP 0 — SKILL ROUTER (ANTES DE TUDO)

**INDEPENDENTE da ação** (codar, commitar, documentar, buscar — qualquer pedido), o buildify DEVE,
antes de tudo, perguntar: **"Existe alguma skill para isto?"**

Para responder, consulta o **repositório de skills** via graphify (grafo já existe em
`/root/.config/opencode/skills/graphify-out/graph.json`):

```bash
graphify query "<palavras-chave da tarefa> which skill handles this?" \
  --graph /root/.config/opencode/skills/graphify-out/graph.json
```

- Se o resultado contiver um nó `Skill: <nome>`, uma referência `` `<nome-da-skill>` `` (entre crases) ou o diretório de uma skill relevante → carrega a skill com a ferramenta `skill`
  (`skill name="<nome>"`) e segue o workflow dela PRIMEIRO.
- Se nenhuma skill fizer match → segue para o STEP 1 (grafo do codebase).

**NUNCA pular esta etapa.** Ela se aplica a TODA solicitação do usuário, mesmo não-codante.
Ao criar/editar/remover skills, atualizar o grafo: `graphify update /root/.config/opencode/skills`.

### Core Rule (OBRIGATÓRIO) — STEP 1 CODEBASE GRAPH

1. **CHECK FIRST**: Se `graphify-out/graph.json` existir, usar `graphify query` para responder perguntas
2. **ONLY build if needed**: Se o grafo NÃO existir, executar `graphify update` para construir
3. **NEVER default to grep**: NÃO usar `grep` como primeira abordagem

### Priority: Graph Query FIRST, Grep NEVER

Quando o usuário faz perguntas como:
- "How does X work?"
- "What files are related to Y?"
- "Find the implementation of Z"

**FAZER PRIMEIRO**: `graphify query "..."` no grafo existente
**NÃO FAZER**: Usar `grep` para buscar arquivos diretamente

**Exceções para grep** (fallback):
- O grafo não existe E `graphify update` falha
- Precisa verificar conteúdo específico que o grafo não respondeu
- O usuário explicitamente pede busca textual

## Workflow

```
0. SKILL ROUTER (ANTES DE TUDO):
   graphify query "<tarefa> which skill handles this?" \
     --graph /root/.config/opencode/skills/graphify-out/graph.json
   → se achou "Skill: X": skill name="X" e segue o workflow dela.
1. START: Verificar se graphify-out/graph.json existe
    - SE existe: graphify query "<pergunta>"
    - SE não existe: graphify update <project_path>
2. ANALYZE: graphify path e graphify explain
3. PLAN: Identificar arquivos afetados e relações
4. EXECUTE: Realizar a tarefa de codificação
5. UPDATE: graphify update <project_path> para atualizar
```

## Comandos Graphify

| Comando | Descrição |
|---------|-----------|
| `graphify query "<t> which skill handles this?" --graph /root/.config/opencode/skills/graphify-out/graph.json` | Busca skill no repo de skills (STEP 0) |
| `graphify update /root/.config/opencode/skills` | Atualiza grafo do repo de skills |
| `graphify update <path>` | Constrói/atualiza grafo (AST, sem custo) |
| `graphify query "<pergunta>"` | Pergunta sobre o codebase (MÉTODO PRIMÁRIO) |
| `graphify path "A" "B"` | Menor caminho entre dois conceitos |
| `graphify explain "<symbol>"` | Explica um símbolo/node específico |
| `graphify prs` | Dashboard de PRs com status CI |

## Custo Zero

`graphify update` usa **extração AST-only** — sem chamadas LLM, custo zero de tokens.

## Localização dos Arquivos

- Skill: `/root/.config/opencode/skills/agent-injection/SKILL.md`
- Agente: `/root/.config/opencode/agents/buildify.md`
- Skill buildify: `/root/.config/opencode/skills/buildify/SKILL.md`

## Exemplo de Uso

```
Tarefa: "Adicionar autenticação JWT"

0. SKILL ROUTER (ANTES DE TUDO):
   graphify query "add authentication jwt which skill handles this?" \
     --graph /root/.config/opencode/skills/graphify-out/graph.json
   → se achou "Skill: auth-login": skill name="auth-login" e segue o workflow dela.
1. CHECK: graphify-out/graph.json existe?
    - SIM: graphify query "how does authentication work?"
    - NÃO: graphify update /www/wwwroot/app.uailove.com.br/wp-content/themes/uailove
2. graphify path "auth" "api"
3. [Entender o grafo, depois implementar]
4. graphify update /www/wwwroot/app.uailove.com.br/wp-content/themes/uailove
```