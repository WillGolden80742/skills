#!/bin/bash
# Espera TV BOX entrar em modo ADB 1007
set -e
echo "[openbridge] lsusb:"
lsusb | grep 1f3a || echo "sem 1f3a plugado"
for i in $(seq 1 30); do
  L=$(lsusb | grep 1f3a || true)
  echo "[$i] $L"
  if echo "$L" | grep -q "1007"; then
    sleep 1
    adb devices -l
    if adb devices | grep -q "device$"; then
      echo "[openbridge] CONECTADO 1007 + adb device"
      adb shell wm size
      exit 0
    fi
  fi
  sleep 2
done
echo "[openbridge] NÃO achou 1007. Replugue o USB e confirme 'Permitir depuração USB' na TV."
exit 1
