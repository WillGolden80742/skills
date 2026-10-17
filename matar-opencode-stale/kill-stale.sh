#!/usr/bin/env bash
# kill-stale.sh v2 — Limpa ABAS (sessões) stale do opencode, nunca processos.
#
# Modelo novo do opencode: um único daemon (`opencode serve --service`) hospeda
# todas as abas como sessões. Matar processos (pgrep -f + SIGTERM) derruba o
# daemon e mata a aba atual junto — por isso a v1 quebrava após a atualização.
#
# v2 usa `opencode session delete` por aba, preservando a sessão atual
# (via $OPENCODE_SESSION_ID) e abortando se ela não for identificável.
#
# Uso:
#   bash .../kill-stale.sh [--dry-run] [--keep N]
#     --dry-run : só lista o que seria apagado, sem apagar.
#     --keep N  : além da atual, preserva as N sessões mais recentes (padrão: 0).

set -euo pipefail

DRY_RUN=false
KEEP=0
for arg in "${@:-}"; do
    case "$arg" in
        --dry-run) DRY_RUN=true ;;
        --keep) echo "Uso: $0 [--dry-run] [--keep N]"; exit 1 ;;
        --keep=*) KEEP="${arg#--keep=}" ;;
    esac
done
# Suporta também: --keep N (dois argumentos)
prev=""
for arg in "${@:-}"; do
    if [ "$prev" = "--keep" ]; then KEEP="$arg"; fi
    prev="$arg"
done
[[ "$KEEP" =~ ^[0-9]+$ ]] || { echo "AVISO: --keep inválido: $KEEP"; exit 1; }

# --- 1. Identifica a sessão atual (nunca via pgrep; pgrep se auto-casa
# --- porque o caminho do script contém "opencode") ---
CURRENT_SESSION="${OPENCODE_SESSION_ID:-}"

# Fallback: tenta achar sessão via `opencode session list` + diretório?
# Não há mapeamento PID->sessão confiável; sem env, aborta.
if [ -z "$CURRENT_SESSION" ]; then
    echo "AVISO: OPENCODE_SESSION_ID não definido; não foi possível identificar a aba atual. Nada foi apagado."
    exit 0
fi

echo "Sessão atual (aba preservada): $CURRENT_SESSION"

# --- 2. Lista sessões (abas) ---
LIST_OUT="$(opencode session list 2>/dev/null || true)"
if [ -z "$LIST_OUT" ]; then
    echo "Nenhuma sessão encontrada (ou lista vazia). Nada a fazer."
    exit 0
fi

mapfile -t ALL_IDS < <(printf '%s\n' "$LIST_OUT" | awk -F'\t' '{print $1}' | grep -E '^ses_' || true)

if [ "${#ALL_IDS[@]}" -eq 0 ]; then
    echo "Nenhuma sessão parseável. Nada a fazer."
    exit 0
fi

# --- 3. Monta lista de preservação: atual + N mais recentes ---
declare -A PRESERVE=()
PRESERVE["$CURRENT_SESSION"]=1
if [ "$KEEP" -gt 0 ]; then
    kept=0
    for sid in "${ALL_IDS[@]}"; do
        [ "$kept" -ge "$KEEP" ] && break
        if [ -z "${PRESERVE[$sid]:-}" ]; then
            PRESERVE["$sid"]=1
            kept=$((kept + 1))
        fi
    done
fi

# A atual precisa existir na lista? Não necessariamente (sessão nova ainda
# não listada). Mesmo assim seguimos: apagamos as demais listadas.
if ! printf '%s\n' "${ALL_IDS[@]}" | grep -qx "$CURRENT_SESSION"; then
    echo "Nota: sessão atual ainda não aparece na lista; as demais serão limpas e a atual seguirá intacta."
fi

# --- 4. Apaga as stale ---
DELETED=0
SKIPPED=0
FAILED=0
for sid in "${ALL_IDS[@]}"; do
    if [ -n "${PRESERVE[$sid]:-}" ]; then
        SKIPPED=$((SKIPPED + 1))
        continue
    fi
    if $DRY_RUN; then
        title="$(printf '%s\n' "$LIST_OUT" | awk -F'\t' -v id="$sid" '$1==id{print $2}')"
        echo "[DRY-RUN] Apagaria $sid — ${title:0:80}"
        DELETED=$((DELETED + 1))
    else
        if opencode session delete "$sid" >/dev/null 2>&1; then
            echo "Apagada sessão stale: $sid"
            DELETED=$((DELETED + 1))
        else
            echo "Falha ao apagar $sid (já removida?)"
            FAILED=$((FAILED + 1))
        fi
    fi
done

echo "Resumo: $DELETED abas stale apagadas, $SKIPPED preservadas (atual + recentes), $FAILED falhas."
echo "Nota v2: nenhum processo foi morto; o daemon 'opencode serve' foi preservado de propósito."
