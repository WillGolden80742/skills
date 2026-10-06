---
name: injecao-graphagy
description: Injeta o agente GraphAgy — coordenador graph-first que gera grafos com graphify (PRIORIDADE) e delega execução ao agy CLI como ESCRAVO via modo print
triggers: ["graphagy", "injecao graphagy", "injetar graphagy", "graphagy agent", "agente coordenador", "agy escravo", "agy slave", "graph + agy", "coordenador graphagy"]
---

# Injeção de GraphAgy

Skill que injeta o agente **GraphAgy** no OpenCode — um agente **exclusivamente coordenador** que tem como **PRIORIDADE ABSOLUTA** gerar/consultar grafos com `graphify` (custo zero, AST-only) e, **só depois**, delega a execução ao `agy` CLI como **ESCRAVO** em modo não-interativo (`agy -p`).

> GraphAgy **NUNCA** executa código diretamente. Ele coordena: mapeia via grafo → monta prompt rico com contexto do grafo → chama `agy` escravo → valida resultado → atualiza grafo.

## O que faz

Esta skill injeta o agente `graphagy` no sistema OpenCode. O agente GraphAgy:

1. **PRIORIDADE 0 — SKILL ROUTER (ANTES DE TUDO)**: pergunta "existe alguma skill para isto?" e busca no grafo do repo de skills:
   `graphify query "<tarefa> which skill handles this?" --graph ~/.config/opencode/skills/graphify-out/graph.json`
2. **PRIORIDADE 1 — GRAFO (SEMPRE PRIMEIRO)**: verifica se `graphify-out/graph.json` existe no projeto; se não existir, roda `graphify update <projeto>` (AST, zero custo); depois `graphify query` + `graphify path` + `graphify explain` para entender estrutura.
3. **SÓ DEPOIS — AGY ESCRAVO**: com o contexto do grafo em mãos, delega a execução ao `agy` via modo print não-interativo. GraphAgy apenas coordena, nunca codifica ele mesmo.
4. **VALIDAÇÃO + UPDATE**: confere o que o escravo fez, roda `graphify update <projeto>` para refrescar o grafo.

## Agente Injetado

O agente GraphAgy é definido em `graphagy-agent.md` nesta skill e instalado em `~/.config/opencode/agents/graphagy.md`:

```yaml
---
description: Coordenador graph-first que gera grafos com graphify e delega execução ao agy CLI como escravo
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

## Workflow do GraphAgy (coordenador → escravo)

```
Tarefa → [STEP 0] skill router via graphify no repo de skills → (se achou Skill: X → skill name="X")
       → [STEP 1] PRIORIDADE GRAFO: graphify-out/graph.json existe?
       │     SIM → graphify query "<tarefa>"
       │     NÃO → graphify update <projeto> → graphify query
       → [STEP 2] graphify path "A" "B" + graphify explain "<símbolo>" (mapear afetados)
       → [STEP 3] AGY ESCRAVO: agy -p "<tarefa + contexto do grafo>" --add-dir <projeto>
       → [STEP 4] validar diff/arquivos → graphify update <projeto>
```

### Regra de ouro

- **GraphAgy = cérebro (coordena). `agy` = mãos (executa).**
- Se alguém pedir para o GraphAgy codificar direto → ele DEVE recusar o modo manual e delegar ao `agy -p`.
- `grep` NUNCA é primeira opção — o grafo é a fonte primária.

## Comandos do Agy como escravo (modo print, sem TTY)

| Comando | Descrição |
|---------|-----------|
| `agy -p "<prompt>" --add-dir <projeto>` | Execução escrava básica (não-interativa, sem TTY) |
| `agy -p "<prompt>" --add-dir <projeto> --agent <nome>` | Escravo com agente específico do agy |
| `agy -p "<prompt>" --add-dir <projeto> --mode accept-edits` | Escravo com permissão de edição |
| `agy -p "<prompt>" --add-dir <projeto> --mode plan` | Escravo só planeja, não edita |
| `agy -p "<prompt>" --output-format json` | Escravo com saída estruturada (parseável) |
| `agy -p "<prompt>" --effort high --model <modelo>` | Escravo com esforço/modelo definidos |
| `agy -c -p "<follow-up>"` | Continuar última conversa do escravo |
| `agy --conversation <ID> -p "<follow-up>"` | Retomar conversa específica do escravo |

### Template de delegação (GraphAgy → agy)

```bash
# 1. GraphAgy já rodou graphify query e tem o contexto. Monta o prompt:
agy -p "CONTEXTO DO GRAFO:
- Arquivos afetados: <lista do graphify query/path>
- Símbolos relevantes: <graphify explain>
- Padrões existentes: <resumo>

TAREFA: <pedido original do usuário>
REGRAS: edite apenas os arquivos listados, siga os padrões acima, não invente arquitetura nova." \
  --add-dir /caminho/do/projeto --mode accept-edits
```

### Quando usar cada modo escravo

- Tarefa de código/edição → `--mode accept-edits`
- Só análise/planejamento → `--mode plan`
- Precisa parsear resposta → `--output-format json`
- Tarefa longa/complexa → `--effort high` (ou `max`)

## Comandos do Graphify (PRIORIDADE)

| Comando | Descrição |
|---------|-----------|
| `graphify query "<t> which skill handles this?" --graph ~/.config/opencode/skills/graphify-out/graph.json` | Skill router (STEP 0, ANTES DE TUDO) |
| `graphify update ~/.config/opencode/skills` | Atualiza grafo do repo de skills |
| `graphify update <projeto>` | Constrói/atualiza grafo do projeto (AST, zero custo) |
| `graphify query "<pergunta>"` | Pergunta ao grafo (MÉTODO PRIMÁRIO) |
| `graphify path "A" "B"` | Menor caminho entre dois conceitos |
| `graphify explain "<símbolo>"` | Explica símbolo/nó específico |
| `graphify prs` | Dashboard de PRs com CI |

## Exemplo de uso

**Tarefa:** "Adicionar autenticação JWT na API"

```
0. SKILL ROUTER:
   graphify query "add authentication jwt which skill handles this?" \
     --graph ~/.config/opencode/skills/graphify-out/graph.json
1. GRAFO (PRIORIDADE):
   graphify update /path/do/projeto   (só se graphify-out/graph.json não existir)
   graphify query "how does authentication work in this codebase?"
   graphify path "auth" "api"
   graphify explain "AuthController"
2. AGY ESCRAVO (SÓ DEPOIS DO GRAFO):
   agy -p "CONTEXTO: AuthController em src/auth/ usa padrão X. TAREFA: adicionar JWT seguindo padrão X." \
     --add-dir /path/do/projeto --mode accept-edits
3. GraphAgy valida o diff, roda graphify update /path/do/projeto.
```

## Custo zero

`graphify update` usa extração AST-only — sem chamadas LLM, zero token. O custo LLM fica concentrado no escravo `agy`, que só é chamado com prompt enxuto e contextualizado pelo grafo.

## Arquivos da skill

- `SKILL.md` — esta documentação (roteador de injeção)
- `graphagy-agent.md` — definição do agente coordenador (fonte para `~/.config/opencode/agents/graphagy.md`)

## Ativação

Quando esta skill é carregada, o agente `graphagy` fica disponível como coordenador primário: ele gera o grafo primeiro e usa o `agy` CLI (`agy -p ...`) como escravo executor.
