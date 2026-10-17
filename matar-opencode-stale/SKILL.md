---
name: matar-opencode-stale
description: Apaga abas (sessões) stale do opencode via session delete, preservando a aba atual. Nunca mata processos — o daemon serve é compartilhado por todas as abas.
triggers: ["matar opencode", "kill opencode", "limpar opencode", "limpar processos", "matar processos stale", "liberar memoria", "free memory", "kill stale", "opencode processes", "processos opencode", "matar instancias", "kill instances", "cleanup opencode", "opencode cleanup", "reduzir uso memoria", "reduzir ram", "matar sessoes antigas", "limpar abas", "abas inativas", "fechar abas", "stale tabs"]
---

# Matar OpenCode Stale (v2 — abas, não processos)

Apaga as abas (sessões) inativas via `opencode session delete`, preservando a aba atual.

## Por que v2

No modelo atual, um único daemon (`opencode serve --service`) hospeda todas as
abas. A v1 usava `pgrep -f opencode` + SIGTERM, o que tinha dois defeitos após
a atualização:

1. O caminho do próprio script contém "opencode", então o `pgrep`/match se
   auto-identificava como "sessão atual" e liberava o resto para morrer —
   incluindo a janela atual.
2. Matar o processo derruba o daemon compartilhado, fechando todas as abas.

A v2 não mata nenhum processo.

## Como funciona

1. Lê a aba atual de `$OPENCODE_SESSION_ID` (sem ela, aborta sem apagar nada).
2. Lista abas com `opencode session list`.
3. Apaga (`session delete`) todas, menos a atual (e `--keep N` recentes, opcional).

## Uso

### Dry-run (só listar o que seria apagado, sem apagar):
```bash
bash /root/.config/opencode/skills/matar-opencode-stale/kill-stale.sh --dry-run
```

### Executar (apagar abas inativas de verdade, preservando a atual):
```bash
bash /root/.config/opencode/skills/matar-opencode-stale/kill-stale.sh
```

### Preservar além da atual as N abas mais recentes:
```bash
bash /root/.config/opencode/skills/matar-opencode-stale/kill-stale.sh --keep 5
```

## Quando usar

- No **início de toda sessão do agente buildify**, antes do skill router, para liberar memória de sessões anteriores que ficaram presas.
- Quando o VPS está com uso alto de RAM e há sessões antigas do opencode acumuladas.
- Sob demanda, quando o usuário pede para limpar processos.

## Segurança

- **Nunca mata a sessão atual** (identificada via árvore de processos).
- **Nunca mata ancestrais** (o processo pai que lançou o opencode).
- **Nunca mata filhos** (subagentes, shells spawnados pela sessão atual).
- Usa SIGTERM (graceful), não SIGKILL.
- Se não conseguir identificar a sessão atual, aborta sem matar nada.

## Integração com o agente buildify

O agente buildify chama esta skill no **STEP -1** (antes do skill router), automaticamente no início de toda interação:

```bash
bash /root/.config/opencode/skills/matar-opencode-stale/kill-stale.sh
```

Isso garante que sessões stale do opencode não acumulem e consumam RAM do VPS.
