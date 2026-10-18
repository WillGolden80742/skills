#!/bin/bash
mkdir -p /tmp/opencode
OUT=${1:-/tmp/opencode/tvbox.png}
adb exec-out screencap -p > "$OUT"
ls -lh "$OUT"
echo "[openbridge] print em $OUT"
