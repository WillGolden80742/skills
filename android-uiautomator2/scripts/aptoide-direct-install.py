#!/usr/bin/env python3
"""Instala sem UI: busca Aptoide API, baixa APK, push + pm install. Uso: aptoide-direct-install.py <SERIAL> <query>"""
import os, sys, urllib.request, urllib.parse
import uiautomator2 as u2
import json
serial = sys.argv[1] if len(sys.argv) > 1 else "192.168.15.2:5555"
query = sys.argv[2] if len(sys.argv) > 2 else "tv launcher smart tv box"
api = "https://ws75.aptoide.com/api/7/apps/search?query=" + urllib.parse.quote(query) + "&limit=5"
print(f"[uia2] API: {api}")
with urllib.request.urlopen(api, timeout=30) as r:
    data = json.loads(r.read().decode())
items = data["datalist"]["list"]
it = items[0]
apk_url, pkg = it["file"]["path"], it["package"]
print(f"[uia2] {it['name']} {it['file']['vername']} {pkg} {it['file']['filesize']}B TRUSTED={it['file']['tags']}")
local = f"/tmp/opencode/{pkg}.apk"
os.makedirs("/tmp/opencode", exist_ok=True)
urllib.request.urlretrieve(apk_url, local)
print(f"[uia2] baixado: {local}")
d = u2.connect(serial)
remote = f"/sdcard/{pkg}.apk"
d.push(local, remote)
print(d.shell(["pm", "install", "-r", remote]))
assert d.app_wait(pkg, timeout=20) or pkg in str(d.shell(["pm", "list", "packages"])), "instalação não confirmada"
print(f"[uia2] INSTALADO {pkg}")
d.app_start(pkg)
