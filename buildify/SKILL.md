---
name: buildify
description: Agente buildify que executa graphify update antes de codar - injeta o agente buildify no OpenCode
triggers: ["buildify", "build agent", "agente build", "graphify before code", "buildify agent", "dev agent", "agente desenvolvimento", "sempre executar graphify", "always run graphify", "graphify update before coding"]
---

# Buildify Skill

Skill que injeta o agente **buildify** no OpenCode — um agente de desenvolvimento que SEMPRE executa `graphify update` antes de iniciar qualquer tarefa de codificação.

## O que faz

Esta skill injeta o agente `buildify` no sistema OpenCode. O agente buildify:

1. **SEMPRE** executa `graphify update .` antes de qualquer tarefa de codificação
2. Usa `graphify query` para entender a estrutura do codebase
3. Só então procede com a tarefa

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
Tarefa → graphify update → graphify query → graphify explain → Implementar → graphify update
```

### Comandos do Graphify

| Comando | Descrição |
|---------|-----------|
| `graphify update <path>` | Constroi/atualiza grafo de código (AST, sem custo) |
| `graphify query "<pergunta>"` | Faz perguntas sobre o codebase |
| `graphify path "A" "B"` | Encontra menor caminho entre dois conceitos |
| `graphify explain "<symbol>"` | Explica um símbolo/node específico |
| `graphify prs` | Dashboard de PRs com status CI |

## Exemplo de Uso

**Tarefa:** "Adicionar autenticação JWT"

```
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