#!/usr/bin/env python3
"""Busca termo no Aptoide via UI e instala. Uso: tv-search-install.py <SERIAL> <termo> [PKG-esperado]"""
import sys
import uiautomator2 as u2
serial = sys.argv[1] if len(sys.argv) > 1 else "192.168.15.2:5555"
termo = sys.argv[2] if len(sys.argv) > 2 else "android tv launcher"
pkg_esperado = sys.argv[3] if len(sys.argv) > 3 else ""
d = u2.connect(serial)
d.implicitly_wait(10.0)
d.app_start("cm.aptoide.pt", stop=True)
assert d.xpath('//*[@text="Pesquisar"]').wait(timeout=20), "aba Pesquisar não apareceu"
d.xpath('//*[@text="Pesquisar"]').click()
box = d.xpath('//*[@text="Pesquisar..."]')
assert box.wait(timeout=10), "campo busca não apareceu"
box.click()
d.send_keys(termo)
d.send_action("search")
assert d.xpath(f'//*[@text="{termo}"]').wait(timeout=20), "resultado não carregou"
d.xpath(f'//*[@text="{termo}"]').click()
inst = d.xpath('//*[@text="INSTALAR"]')
assert inst.wait(timeout=30), "botão INSTALAR não apareceu"
inst.click()
if pkg_esperado:
    print(f"[uia2] aguardando {pkg_esperado} ...")
    assert d.app_wait(pkg_esperado, timeout=180), f"{pkg_esperado} não instalou"
print("[uia2] OK busca+instalar via UI")
