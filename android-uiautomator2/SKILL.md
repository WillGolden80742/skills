# Skill Android UI Automator — openatx/uiautomator2

Automação Android via Python usando https://github.com/openatx/uiautomator2 (v3.x, Python 3.8+, Android 4.4+).
Testado na TV Box `dolphin_fvd_p1` (`192.168.15.2:5555`, 1280x720, SDK 24).

## Regras de ouro

1. **PIN OpenBridge antes de tudo privilegiado**: antes de `init`, `install`, `push`, `tcpip`, rode
   `bash ~/.config/opencode/skills/openbridge/scripts/require-pin.sh <4-digitos> <SERIAL>` (ex: `1193 192.168.15.2:5555`).
   Ele sincroniza `pin.txt` da TV e compara. Sem PIN não executa.
2. **WiFi cai sozinho**: se `adb devices` = `offline` ou `uiautomator2 ConnectError not online`,
   faça `adb disconnect <IP>:5555` + `adb connect <IP>:5555`. Se `Connection refused` (ping ok, porta 5555 fechada),
   peça ao usuário reativar no app **Opencode TV** (toggle Acesso total) com o controle remoto.
3. **Trava anti-sono antes de sessão longa**: `svc power stayon true; settings put system screen_off_timeout 2147483647; settings put global wifi_sleep_policy 2`.
4. **TV = D-pad**: prefira `d.press("left/right/up/down/center/back/home/enter")` e `d(text=...).click()` a `tap x y`. Resolução pode mudar (`wm size`), então seletor > coordenada.
5. **Push + pm install > streamed install**: no WiFi instável, `d.push(apk, /sdcard/x.apk)` + `d.shell([pm, install, -r, ...])` é mais estável que `adb install`.

## Instalação (notebook, uma vez)

```
pip install --break-system-packages -q uiautomator2
python3 -m uiautomator2 version  # ex: 3.7.0
```

Opcional inspeção visual: `npx uiautodev -open` (precisa Node) ou `pip install uiautodev`.

## Init no aparelho (uma vez por aparelho, precisa ADB online + PIN)

```
SERIAL=192.168.15.2:5555
bash ~/.config/opencode/skills/openbridge/scripts/require-pin.sh 1193 $SERIAL
python3 -m uiautomator2 init --serial $SERIAL
# instala atx-agent + com.github.uiautomator + com.github.uiautomator.test
# Se falhar com LaunchUiAutomationError server quit: cheque `adb shell pm list packages | grep uiauto`,
# `adb logcat -d | grep -i uiauto`, espaço em /data, e rode init de novo com TV acordada.
```

## Conectar (todo script)

```python
import uiautomator2 as u2
SERIAL = "192.168.15.2:5555"  # ou serial USB ex: 85017923031438000092
d = u2.connect(SERIAL)  # alias connect_usb; respeita ANDROID_SERIAL env
print(d.info)           # pacote atual, displayWidth/Height, sdkInt, screenOn
print(d.device_info)    # arch, brand, model, sdk, serial via getprop
print(d.wlan_ip, d.serial)
```

Porta não-padrão (default 9008): `u2.connect(SERIAL, port=9009)`.

## Seletores (preferir a tap)

```
d.implicitly_wait(10.0)
d(text="Pesquisar").click()
d(textContains="Launcher", className="android.widget.TextView").click()
d(resourceId="com.github.supertvlauncher:id/...").click()
d(descriptionContains="Apps").click()
d(text="Skip").click_exists(timeout=10.0)
d(text="Skip").click_gone(maxretry=10, interval=1.0)
x, y = d(text="Settings").center()
d.screenshot("home.jpg")  # pillow/opencv/raw via format=
xml = d.dump_hierarchy(compressed=False, pretty=True, max_depth=30)
```

XPath (gerar via uiautodev):
```
d.xpath('//*[@text="android tv launcher"]').click()
d.xpath('@resource-id-aqui').click()
el = d.xpath('//*[@text="INSTALAR"]').wait(timeout=15)
el.click()
```

## D-pad / teclas TV

```
for k in ["home","back","left","right","up","down","center","enter","search","recent","volume_up","power"]: d.press(k)
d.screen_on(); d.screen_off(); d.unlock()
d.click(x, y); d.long_click(0.5, 0.5); d.swipe_ext("up", scale=0.8)
d(text="Settings").swipe("right"); d(scrollable=True).scroll.vertical.to(text="Security")
```

## Apps

```
d.app_start("cm.aptoide.pt", stop=True)
d.wait_activity(".view.MainActivity", timeout=10)
d.app_current()  # {'activity':..., 'package':..., 'pid':...}
d.app_wait("com.github.supertvlauncher", front=True, timeout=20.0)
d.app_stop("cm.aptoide.pt"); d.app_clear("cm.aptoide.pt")
d.app_info("com.github.supertvlauncher")  # mainActivity, label, versionName/Code, size
img = d.app_icon("cm.aptoide.pt"); img.save("icon.png")
```

## Instalar APK (padrão estável WiFi)

```
APK_LOCAL="/home/user/Documentos/AntiSpamBot/tv-launcher.apk"
PKG="com.github.supertvlauncher"  # TV Launcher - Smart TV BOX V5.2.29, 16.2MB, Android 7.0+
d.push(APK_LOCAL, "/sdcard/tvlauncher.apk")
d.shell(["pm", "install", "-r", "/sdcard/tvlauncher.apk"])
d.shell(["pm", "list", "packages"])  # conferir PKG
d.app_start(PKG)
```

URL direta Aptoide (sem UI flaky):
`https://pool.apk.aptoide.com/appupdater/com-github-supertvlauncher-102-75368597-ea980ea6ac9ff363b1cc3e52e9c3ad0b.apk`

## Exemplo fim-a-fim: buscar + instalar na TV

```python
import uiautomator2 as u2
d = u2.connect("192.168.15.2:5555")
d.app_start("cm.aptoide.pt", stop=True)
d(text="Pesquisar").click()          # ou d.press até focar + center
d.xpath('//*[@text="Pesquisar..."]').click()
d.send_keys("android tv launcher")   # usa clipboard/IME auxiliar
d.send_action("search")
d.xpath('//*[@text="TV Launcher  - Smart TV BOX"]').click()
d.xpath('//*[@text="INSTALAR"]').click()
d.xpath('//*[@text="ABRIR"]').wait(timeout=120)
```

Fallback sem UI: baixar via API `https://ws75.aptoide.com/api/7/apps/search?query=...` → `file.path` → push + pm install (acima).

## CLI útil

```
python3 -m uiautomator2 --serial 192.168.15.2:5555 screenshot tv.png
python3 -m uiautomator2 --serial 192.168.15.2:5555 current  # pacote + activity atual
```

## Scripts desta skill

- `scripts/connect.py [SERIAL]` — conecta e imprime info/device_info/wlan_ip
- `scripts/screenshot.py [SERIAL] [saida.png]` — screenshot via u2
- `scripts/dump.py [SERIAL]` — dump_hierarchy pretty (para achar seletor)
- `scripts/tv-search-install.py <SERIAL> <termo> [PKG]` — abre Aptoide, busca termo, clica INSTALAR, espera ABRIR
- `scripts/aptoide-direct-install.py <SERIAL> <query>` — busca via API ws75, baixa file.path, push + pm install (sem UI)
- `scripts/requirements.txt` — `uiautomator2>=3.0`

## Troubleshooting TV Box

- `ConnectError not online` → `adb disconnect/connect`, TV dormiu.
- `Connection refused` → daemon ADB caiu; reativar no app Opencode TV.
- `LaunchUiAutomationError server quit` → TV reiniciou uiautomator; `adb shell pm list packages | grep uiauto`, `logcat -d | grep uiauto`, reinit com TV acordada + trava anti-sono.
- Lista vazia/spinner infinito no Aptoide → rede lenta; use `aptoide-direct-install.py`.
- `adb install` streamed fail → push + `pm install -r /sdcard/*.apk`.
