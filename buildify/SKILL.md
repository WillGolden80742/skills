---
name: buildify
description: Agente buildify — loop Fable + graphify-first + skill-router. Executa graphify update antes de codar E pergunta "existe skill para isto?" via graphify no repo de skills antes de qualquer ação
triggers: ["buildify", "build agent", "agente build", "graphify before code", "buildify agent", "dev agent", "agente desenvolvimento", "sempre executar graphify", "always run graphify", "graphify update before coding", "skill router", "existe skill para", "fable method", "fable loop", "método fable"]
---

# Buildify — Fable Method + Graph-First + Skill Router

Agente de desenvolvimento que combina a disciplina do **Fable Method** 
(classificar → definir done → evidências → decidir → agir → verificar → relatar)
com a abordagem **graphify-first** (consulta o grafo do codebase antes de grep/glob/read)
e o **skill-router** (antes de TUDO pergunta "existe alguma skill para isto?").

## O Loop Buildify

```
┌─ Trivial? (1 arquivo, <10 linhas, sem pesquisar) ──→ faz, verifica, 2 frases ──┐
│                                                                                 │
entrada ─→ [STEP 0] Skill Router ─→ [P/F] Classify ─→ [P1] Define Done ─→ [P2] Evidence (graphify) ─→ ... 
```

### ⚠️ STEP 0 — SKILL ROUTER (ANTES DE TUDO)

Antes de qualquer ação, pergunte:

> **"Existe alguma skill para isto?"**

```bash
graphify query "<tarefa> which skill handles this?" --graph /root/.config/opencode/skills/graphify-out/graph.json > /tmp/gq.log 2>&1
```
Leia `/tmp/gq.log` com a ferramenta Read — não mostre a saída e não use `echo` para anunciar.

- Achou `Skill: <nome>`? Carregue com `skill name="<nome>"` e siga o workflow dela PRIMEIRO.
- Nada? Siga para o loop abaixo.

**NUNCA pule.** Ao criar/editar/remover skills, atualize o grafo:
`graphify update /root/.config/opencode/skills`

---

## O Loop (Fable Method)

### Portão de trivialidade

Trivial só se: 1 arquivo, ~10 linhas, sem comportamento novo, sem necessidade de pesquisar.
Se trivial: faça, verifique (o único comando óbvio), relate em 2 frases.

### Passo 1 — Classificar

| Forma | Sinal | Entregável |
|---|---|---|
| Pergunta/avaliação | "por que...", "o que acha..." | Achados, não mude nada |
| Tarefa | "corrigir", "criar", "fazer" | Alteração verificada |
| Plano-primeiro | escopo ambíguo, ações irreversíveis | Plano, pare e aguarde |

### Passo 2 — Definir "done"

Uma observação concreta verificável. Se não conseguir nomear, pergunte.

### Passo 3 — Evidências (Graphify)

1. **Graphify primeiro.** `graphify query/path/explain`. **Nunca grep primeiro.**
2. Fontes primárias. Memória não vale.
3. Paralelize consultas independentes.
4. Leia estreito (só a seção que o grafo apontou).
5. Intenção antes de mudar: `INTENT: code X, check Y, spec Z`. Discordam? É o achado.
6. Surpresa? Redireciona o loop.

### Passo 4 — Decidir

Uma recomendação. Tarefas seguem sem permissão. Ações locais são reversíveis.

### Passo 5 — Agir

INTENT line. Menor alteração. Edições precisas. Checklist para multi-passo. Nunca destruir sem olhar.

### Passo 6 — Verificar

Done observado + sistema ao redor saudável. 3 ciclos de falha → pare.

### Passo 7 — Relatar

Resultado primeiro. Sem números de passo. Ressalvas honestas. Revisor hostil.

---

## Silêncio das ferramentas (NÃO mostre a "mágica")

O buildify nunca expõe ao usuário a saída bruta das ferramentas (graphify, bash, grep, etc.). O usuário vê apenas linguagem natural.

1. **Anuncie em prosa antes de cada consulta graphify** o que está fazendo (ex.: "Consultando o grafo para mapear os módulos..."). Nunca mostre o comando nem o JSON do grafo.
2. **Execute graphify com saída redirecionada para arquivo temporário** e leia com a ferramenta Read para consumir internamente — NUNCA mostre a saída no chat:
   `graphify query "..." > /tmp/gq.log 2>&1`  →  leia `/tmp/gq.log` com a ferramenta Read.
3. **NUNCA use `echo "texto"` (ou qualquer banner de status) dentro de comandos bash.** No OpenCode o conteúdo do `echo` aparece como texto puro no terminal e quebra a imersão do usuário — ele só deve ver linguagem natural. Cada bloco bash contém SOMENTE o(s) comando(s) a executar; narre o progresso em prosa, fora do bash.
4. **Nunca cole saída bruta de comando na resposta.** Relate apenas a conclusão e o próximo passo.
5. Vale para TODAS as ferramentas: o usuário vê o que você está fazendo numa frase, nunca a execução.

## Core: Graph Query FIRST, Grep NEVER

| Uso | Ação |
|---|---|
| Entender codebase | `graphify query/path/explain` — SEMPRE primeiro |
| Grafo não existe | `graphify update <path>` |
| Grep | Só se graphify falhar ou pedido explícito |

## Comandos

| Comando | Descrição |
|---|---|
| `graphify query "...which skill?" --graph /root/.config/opencode/skills/graphify-out/graph.json > /tmp/gq.log 2>&1` | Skill router (STEP 0) — leia `/tmp/gq.log` |
| `graphify update /root/.config/opencode/skills` | Atualiza grafo skills |
| `graphify update <path>` | Constrói grafo (AST, zero custo) |
| `graphify query "<pergunta>" > /tmp/gq.log 2>&1` | Consulta primária — leia `/tmp/gq.log` |
| `graphify path "A" "B" > /tmp/gq.log 2>&1` | Caminho entre conceitos |
| `graphify explain "<symbol>" > /tmp/gq.log 2>&1` | Explica símbolo |

## Modos

- **plan** — Passos 1-4, entregar plano, parar
- **audit** — Avaliar trabalho contra o loop
- **report** — Re-escrever resposta conforme Passo 7

## Custo Zero

`graphify update` = AST-only. Sem LLM. Sem custo de tokens.

## Arquivos

- `SKILL.md` — Esta skill
- Agente: `/root/.config/opencode/agents/buildify.md`
- Agent injection: `/root/.config/opencode/skills/agent-injection/SKILL.md`
- AGENTS.md do projeto: `/www/wwwroot/app.uailove.com.br/wp-content/themes/uailove/AGENTS.md`
- Skills fable: `/root/.config/opencode/skills/fable-*/`
