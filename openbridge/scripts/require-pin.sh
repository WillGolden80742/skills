#!/bin/bash
[ -f "$HOME/.config/openbridge.env" ] && . "$HOME/.config/openbridge.env"
# Verifica o PIN informado contra o PIN atual da TV.
# Sincroniza primeiro (o PIN MUDA quando o usuário toca GERAR_NOVO_CODIGO).
# Uso: require-pin.sh 1234 [SERIAL]
# Sai 0 se confere, 1 se não confere.
INFORMADO=${1:-}
SERIAL=${2:-${OPENBRIDGE_SERIAL:-192.168.1.100:5555}}
SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
bash "$SKILL_DIR/scripts/pin-sync.sh" "$SERIAL" >/dev/null 2>&1
ATUAL=$(cat "$SKILL_DIR/pin.txt" 2>/dev/null | tr -d '\r\n ')
if [ -z "$INFORMADO" ]; then
  echo "[openbridge] informe os 4 dígitos da tela da TV. PIN atual da TV: $ATUAL"
  exit 2
fi
if [ "$INFORMADO" = "$ATUAL" ]; then
  echo "[openbridge] PIN confere ($ATUAL). Acesso liberado."
  exit 0
else
  echo "[openbridge] PIN NÃO confere (informado=$INFORMADO tv=$ATUAL). Peça novo código na TV."
  exit 1
fi
