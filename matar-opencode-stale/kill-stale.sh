#!/usr/bin/env bash
# kill-stale.sh — Mata todas as instâncias do opencode exceto a sessão atual.
# Sobe a árvore de processos a partir do PID atual para identificar o opencode desta sessão.
# Uso: bash /root/.config/opencode/skills/matar-opencode-stale/kill-stale.sh [--dry-run]

set -euo pipefail

DRY_RUN=false
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=true

# Encontra o PID do processo opencode que é ancestral do PID atual
get_current_opencode_pid() {
    local pid=$$
    while [ "$pid" != "1" ] && [ "$pid" != "0" ] && [ -n "$pid" ]; do
        local cmdline
        cmdline=$(tr '\0' ' ' < "/proc/$pid/cmdline" 2>/dev/null || true)
        if [[ "$cmdline" == *"opencode"* ]]; then
            echo "$pid"
            return 0
        fi
        pid=$(ps -o ppid= -p "$pid" 2>/dev/null | tr -d ' ' || true)
    done
    return 1
}

CURRENT_PID=$(get_current_opencode_pid) || {
    echo "AVISO: não foi possível identificar a sessão atual do opencode. Nenhum processo foi morto."
    exit 0
}

echo "Sessão atual do opencode: PID $CURRENT_PID"

# Coleta todos os PIDs de processos opencode
mapfile -t ALL_PIDS < <(pgrep -f "opencode" 2>/dev/null || true)

if [ ${#ALL_PIDS[@]} -eq 0 ]; then
    echo "Nenhuma instância do opencode encontrada."
    exit 0
fi

KILLED=0
SKIPPED=0

for pid in "${ALL_PIDS[@]}"; do
    # Pula a sessão atual
    if [ "$pid" == "$CURRENT_PID" ]; then
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    # Pula processos filhos da sessão atual (subagentes, shells)
    local_ppid=$(ps -o ppid= -p "$pid" 2>/dev/null | tr -d ' ' || true)
    if [ "$local_ppid" == "$CURRENT_PID" ]; then
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    # Verifica se é ancestral da sessão atual (pai/avô/etc.) — não matar
    is_ancestor=false
    check_pid=$CURRENT_PID
    while [ "$check_pid" != "1" ] && [ "$check_pid" != "0" ] && [ -n "$check_pid" ]; do
        if [ "$check_pid" == "$pid" ]; then
            is_ancestor=true
            break
        fi
        check_pid=$(ps -o ppid= -p "$check_pid" 2>/dev/null | tr -d ' ' || true)
    done

    if $is_ancestor; then
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    # Pula se o processo já terminou
    [ ! -d "/proc/$pid" ] && continue

    # Mata o processo stale
    cmdline=$(tr '\0' ' ' < "/proc/$pid/cmdline" 2>/dev/null | head -c 120 || echo "(desconhecido)")
    if $DRY_RUN; then
        echo "[DRY-RUN] Mataria PID $pid: $cmdline"
    else
        kill -TERM "$pid" 2>/dev/null && {
            echo "Matado PID $pid (stale): ${cmdline:0:80}"
            KILLED=$((KILLED + 1))
        } || {
            echo "Falha ao matar PID $pid (já encerrado?)"
        }
    fi
done

echo "Resumo: $KILLED instâncias stale mortas, $SKIPPED preservadas (sessão atual + ancestrais + filhos)."
