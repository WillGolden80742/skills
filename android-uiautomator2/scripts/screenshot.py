#!/usr/bin/env python3
"""Screenshot via u2. Uso: screenshot.py [SERIAL] [saida.png]"""
import os, sys
import uiautomator2 as u2
serial = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("ANDROID_SERIAL", "192.168.15.2:5555")
out = sys.argv[2] if len(sys.argv) > 2 else "/tmp/opencode/uia2.png"
d = u2.connect(serial)
d.screenshot(out)
print(f"[uia2] screenshot: {out}")
