#!/bin/bash
# Uso: resolucao.sh 1280x720  | reset para nativa
RES=${1:-1280x720}
mkdir -p /tmp/opencode
adb devices -l
if [ "$RES" = "reset" ]; then
  adb shell wm size reset
else
  adb shell wm size "$RES"
fi
adb shell wm size
adb exec-out screencap -p > "/tmp/opencode/tvbox-$RES.png"
ls -lh "/tmp/opencode/tvbox-$RES.png"
echo "[openbridge] resolução -> $RES"
