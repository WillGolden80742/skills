#!/bin/bash
# Roda UMA VEZ com USB 1007 (ou WiFi device) para TV BOX nunca derrubar ADB/rede.
# Exige replug em 1007 se WiFi estiver offline.
set -x
SERIAL=${ADB_SERIAL:-}
if [ -n "$SERIAL" ]; then S="adb -s $SERIAL"; else S="adb"; fi
$S shell settings put global development_settings_enabled 1
$S shell settings put global adb_enabled 1
$S shell settings put global adb_auto_revoke 0
$S shell settings put system screen_off_timeout 2147483647
$S shell svc power stayon true
$S shell settings put global wifi_sleep_policy 2
$S shell settings put global stay_on_while_plugged_in 3
$S shell setprop persist.sys.usb.config mtp,adb
$S shell setprop service.adb.tcp.port 5555
$S shell dumpsys deviceidle disable || true
$S shell getprop persist.sys.usb.config
$S shell getprop service.adb.tcp.port
$S shell settings list global | grep -i -E "adb|wifi_sleep|stay_on"
echo "[openbridge] persist aplicado. Agora no roteador reserve o IP da TV (OPENBRIDGE_IP) para o MAC da TV + na TV deixe 'ADB pela rede' ligado se existir."
