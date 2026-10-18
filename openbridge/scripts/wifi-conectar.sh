#!/bin/bash
[ -f "$HOME/.config/openbridge.env" ] && . "$HOME/.config/openbridge.env"
# Conecta TV BOX via WiFi sem precisar de USB 100% do tempo
# Uso: wifi-conectar.sh [IP]  (padrão OPENBRIDGE_IP (ex. 192.168.1.100))
IP=${1:-${OPENBRIDGE_IP:-192.168.1.100}}
set -e
echo "[openbridge-wifi] tcpip 5555 (precisa USB 1007 uma vez, ignora se já estiver no WiFi)..."
adb tcpip 5555 || true
sleep 3
echo "[openbridge-wifi] connect $IP:5555..."
adb connect "$IP:5555"
sleep 4
adb devices -l
echo "[openbridge-wifi] teste via WiFi..."
adb -s "$IP:5555" shell echo WIFI-OK
adb -s "$IP:5555" shell wm size
echo "[openbridge-wifi] pronto. Use: adb -s $IP:5555 shell <cmd>"
echo "[openbridge-wifi] scrcpy: scrcpy -s $IP:5555 --window-title 'TV BOX WiFi' --stay-awake"
