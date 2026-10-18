#!/usr/bin/env python3
"""Dump hierarquia para achar seletor. Uso: dump.py [SERIAL]"""
import os, sys
import uiautomator2 as u2
serial = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("ANDROID_SERIAL", "192.168.15.2:5555")
d = u2.connect(serial)
print(d.dump_hierarchy(compressed=False, pretty=True, max_depth=30))
