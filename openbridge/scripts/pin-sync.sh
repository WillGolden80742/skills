#!/bin/bash
[ -f "$HOME/.config/openbridge.env" ] && . "$HOME/.config/openbridge.env"
# Sincroniza o PIN de 4 dígitos da TV para a skill.
# Uso: pin-sync.sh [SERIAL]  (padrão tenta WiFi via OPENBRIDGE_SERIAL (ex. 192.168.1.100:5555))
SERIAL=${1:-${OPENBRIDGE_SERIAL:-192.168.1.100:5555}}
SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PIN=$(adb -s "$SERIAL" shell cat /sdcard/Android/data/com.openbridge.remote/files/pin.txt 2>/dev/null | tr -d '\r\n ')
[ "${#PIN}" != "4" ] && PIN=$(adb -s "$SERIAL" shell cat /sdcard/OpencodeTV/pin.txt 2>/dev/null | tr -d '\r\n ')
if [ "${#PIN}" = "4" ]; then
  echo -n "$PIN" > "$SKILL_DIR/pin.txt"
  echo "[openbridge] PIN sincronizado: $PIN"
else
  echo "[openbridge] PIN inválido/ausente (app Opencode TV aberto? botão GERAR_NOVO_CODIGO). Mantido: $(cat "$SKILL_DIR/pin.txt")"
  exit 1
fi
