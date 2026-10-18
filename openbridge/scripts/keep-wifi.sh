#!/bin/bash
# Mantém ADB WiFi da TV BOX sempre de pé. Roda no notebook.
# Se o IP cair, varre a sub-rede na porta 5555 e reconecta sozinho.
# Uso: keep-wifi.sh [IP]  (padrão $OPENBRIDGE_IP ou 192.168.1.100)
IP=${1:-${OPENBRIDGE_IP:-192.168.1.100}}
PORT=5555
TARGET="$IP:$PORT"
FAIL=0
echo "[openbridge-keep] alvo $TARGET, loop infinito (Ctrl+C para parar)"

scan_subnet() {
  # varredura paralela rápida da ${SUBNET:-192.168.1.0/24} na porta 5555
  NETPREFIX=${NETPREFIX:-${IP%.*}}
  for i in $(seq 1 254); do echo "$NETPREFIX.$i"; done | \
    xargs -P 32 -I{} timeout 1 bash -c "echo > /dev/tcp/{}/$PORT 2>/dev/null && echo {}" 2>/dev/null | head -n 1
}

while true; do
  ST=$(adb devices | grep "^$TARGET" | awk '{print $2}')
  if [ "$ST" != "device" ]; then
    echo "[openbridge-keep] $TARGET = ${ST:-desconectado} -> connect..."
    if ! adb connect "$TARGET" 2>&1 | grep -q "connected to"; then
      FAIL=$((FAIL+1))
      echo "[openbridge-keep] tentativa $FAIL falhou; varrendo sub-rede..."
      FOUND=$(scan_subnet)
      if [ -n "$FOUND" ]; then
        echo "[openbridge-keep] TV achada em $FOUND! Conectando..."
        TARGET="$FOUND:$PORT"
        adb connect "$TARGET" >/dev/null 2>&1 || true
      else
        echo "[openbridge-keep] TV fora da rede. Precisa USB 1007 + 'adb tcpip 5555' uma vez. Tentando via USB..."
        if lsusb | grep -q "1f3a:1007" && adb devices | grep -q "device$"; then
          adb tcpip $PORT >/dev/null 2>&1 || true
          sleep 3
          adb connect "$TARGET" >/dev/null 2>&1 || true
        else
          echo "[openbridge-keep] sem USB 1007 agora. Aguardando..."
        fi
      fi
    else
      FAIL=0
      sleep 2
      ST2=$(adb devices | grep "^$TARGET" | awk '{print $2}')
      echo "[openbridge-keep] agora: ${ST2:-desconectado}"
      if [ "$ST2" = "device" ]; then
        adb -s "$TARGET" shell svc power stayon true >/dev/null 2>&1 || true
      fi
    fi
  else
    FAIL=0
  fi
  sleep 10
done
