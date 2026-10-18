#!/bin/bash
# Trava pra depuração USB não cair sozinha
adb shell settings put global development_settings_enabled 1
adb shell settings put global adb_enabled 1
adb shell settings put global adb_auto_revoke 0 2>/dev/null || true
adb shell settings put system screen_off_timeout 2147483647
adb shell svc power stayon true
adb shell setprop persist.sys.usb.config mtp,adb
adb shell getprop persist.sys.usb.config
adb shell wm size
echo "[openbridge] trava aplicada"
