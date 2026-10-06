---
name: matar-opencode-stale
description: Mata todas as instâncias do opencode exceto a sessão atual, liberando memória no VPS. Sobe a árvore de processos para identificar a sessão atual e preserva ancestrais e filhos.
triggers: ["matar opencode", "kill opencode", "limpar opencode", "limpar processos", "matar processos stale", "liberar memoria", "free memory", "kill stale", "opencode processes", "processos opencode", "matar instancias", "kill instances", "cleanup opencode", "opencode cleanup", "reduzir uso memoria", "reduzir ram", "matar sessoes antigas"]
---

# Matar OpenCode Stale

Mata todas as instâncias do opencode exceto a sessão atual, liberando recursos no VPS.

## Como funciona

1. Sobe a árvore de processos a partir do PID atual até encontrar o processo `opencode` desta sessão.
2. Lista todos os processos com `opencode` no cmdline (`pgrep -f`).
3. Preserva: a sessão atual, seus ancestrais (pai/avô) e seus filhos (subagentes, shells).
4. Mata (SIGTERM) todos os demais.

## Uso

### Executar (matar de verdade):
```bash
bash /root/.config/opencode/skills/matar-opencode-stale/kill-stale.sh
```

### Dry-run (só listar o que seria morto, sem matar):
```bash
bash /root/.config/opencode/skills/matar-opencode-stale/kill-stale.sh --dry-run
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
