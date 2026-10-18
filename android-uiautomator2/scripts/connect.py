#!/usr/bin/env python3
"""Conecta via uiautomator2 e imprime infos. Uso: connect.py [SERIAL]"""
import os, sys
import uiautomator2 as u2
serial = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("ANDROID_SERIAL", "192.168.15.2:5555")
try:
    d = u2.connect(serial)
    print("info:", d.info)
    print("device:", d.device_info)
    print("wlan_ip:", d.wlan_ip, "serial:", d.serial)
    print("current:", d.app_current())
except Exception as e:
    print(f"[uia2] FALHA conectar {serial}: {e}")
    print("[uia2] tente: adb disconnect/connect + app Opencode TV > Acesso total")
    sys.exit(1)
