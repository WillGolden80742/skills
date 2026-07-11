---
name: buildify
description: Agente buildify que executa graphify update antes de codar E pergunta "existe skill para isto?" via graphify no repo de skills antes de qualquer ação - injeta o agente buildify no OpenCode
triggers: ["buildify", "build agent", "agente build", "graphify before code", "buildify agent", "dev agent", "agente desenvolvimento", "sempre executar graphify", "always run graphify", "graphify update before coding", "skill router", "existe skill para"]
---

# Buildify Skill

Skill que injeta o agente **buildify** no OpenCode — um agente de desenvolvimento que, **ANTES DE TUDO**, pergunta "existe alguma skill para isto?" consultando o repositório de skills via graphify, e só então executa `graphify update` antes de iniciar qualquer tarefa de codificação.

## O que faz

Esta skill injeta o agente `buildify` no sistema OpenCode. O agente buildify:

1. **ANTES DE TUDO**: pergunta "existe alguma skill para isto?" e busca no grafo do repo de skills
   (`graphify query "<tarefa> which skill handles this?" --graph /root/.config/opencode/skills/graphify-out/graph.json`)
2. Se achar uma skill (`Skill: <nome>`), carrega-a com `skill name="<nome>"` e segue o workflow dela
3. **SEMPRE** executa `graphify update .` antes de qualquer tarefa de codificação
4. Usa `graphify query` para entender a estrutura do codebase
5. Só então procede com a tarefa

## Agente Injetado

O agente buildify é definido em `buildify-agent.md` e possui:

```yaml
---
description: Agente de build que sempre executa graphify antes de codar
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

## Workflow do Buildify

```
Tarefa → [STEP 0] graphify query no repo de skills → (se achou Skill: X → skill name="X")
       → [STEP 1] graphify update → graphify query → graphify explain → Implementar → graphify update
```

### Comandos do Graphify

| Comando | Descrição |
|---------|-----------|
| `graphify query "<t> which skill handles this?" --graph /root/.config/opencode/skills/graphify-out/graph.json` | Busca skill no repo de skills (STEP 0, ANTES DE TUDO) |
| `graphify update /root/.config/opencode/skills` | Atualiza grafo do repo de skills |
| `graphify update <path>` | Constroi/atualiza grafo de código (AST, sem custo) |
| `graphify query "<pergunta>"` | Faz perguntas sobre o codebase |
| `graphify path "A" "B"` | Encontra menor caminho entre dois conceitos |
| `graphify explain "<symbol>"` | Explica um símbolo/node específico |
| `graphify prs` | Dashboard de PRs com status CI |

## Exemplo de Uso

**Tarefa:** "Adicionar autenticação JWT"

```
0. SKILL ROUTER (ANTES DE TUDO):
   graphify query "add authentication jwt which skill handles this?" \
     --graph /root/.config/opencode/skills/graphify-out/graph.json
   → se achou "Skill: auth-login": skill name="auth-login"
1. graphify update /path/do/projeto
2. graphify query "how does authentication work?"
3. graphify path "auth" "api"
4. [Entender o grafo, depois implementar]
5. graphify update /path/do/projeto
```

## Custo Zero

`graphify update` usa **extração AST-only** — sem chamadas LLM, custo zero de tokens.

## Arquivos da Skill

- `SKILL.md` - Esta documentação
- `buildify-agent.md` - Definição do agente injetado

## Ativação

Quando esta skill é carregada, o agente `buildify` fica disponível no sistema OpenCode como agente primário para tarefas de desenvolvimento.