---
name: openbridge
description: Acesso total a qualquer Android com o app OpenBridge instalado via ADB USB/WiFi, resolução, screenshot, PIN
triggers: ["openbridge", "acesso remoto android", "controlar android", "android wifi adb", "espelhar android", "adb wifi", "PIN android", "TV BOX", "Allwinner", "1f3a", "resolução tv box", "wm size", "adb tv box", "dolphin_fvd_p1", "acesso total", "opencode tv"]
---

# Skill OPENBRIDGE — Acesso TV BOX Allwinner

TV BOX alvo: `Allwinner TV BOX` / `dolphin_fvd_p1` / serial `85017923031438000092`
- `1f3a:1006` = MODO MTP (só arquivos, SEM adb)
- `1f3a:1007` = MODO ADB (debug liberado, COM adb)

Sempre confira antes: `lsusb | grep 1f3a` + `adb devices -l`

## Regras de ouro (não esquecer)

1. HDMI `notebook -> tv box` NÃO dá vídeo (saída com saída). Use USB + ADB ou `notebook -> TV` direto.
2. Na TV BOX, manter ligado:
   - `Depuração USB` ON
   - `USB0 device mode enable` ON (Enable USB0 device mode to debug)
   - Confirmar popup `Permitir depuração USB / Sempre permitir`
3. No notebook, anti-queda (já aplicado via udev):
   - `/etc/udev/rules.d/51-allwinner-1006.rules`
   - `/etc/udev/rules.d/51-allwinner-1007.rules`
   - `/etc/udev/rules.d/52-allwinner-power.rules` com `ATTR{power/control}="on"`
   - `power/control` em `on`, sem autosuspend no `3-9`
4. Se cair pra 1006: desplugar/plugar firme, confirmar popup, esperar 1007.
5. `scrcpy 3.3.4` já instalado. Abrir com: `scrcpy --window-title "TV BOX" --stay-awake`

## Resoluções usadas

- Nativa: `1280x720` (`adb shell wm size reset` volta pra ela)
- Testadas: `800x600`, `740x700`, `800x700`, `1280x700`, `1280x740`, `960x540`, `1024x576` (1024 largura proporção 16:9)
- Comandos:
  ```
  adb shell wm size
  adb shell wm size 1280x720
  adb shell wm size 1280x700
  adb shell wm size reset
  adb exec-out screencap -p > /tmp/opencode/tvbox.png
  ```

## Trava anti-desativar depuração

```
adb shell settings put global development_settings_enabled 1
adb shell settings put global adb_enabled 1
adb shell settings put global adb_auto_revoke 0
adb shell settings put system screen_off_timeout 2147483647
adb shell svc power stayon true
adb shell setprop persist.sys.usb.config mtp,adb
adb shell getprop persist.sys.usb.config # tem que dar mtp,adb
```

## WiFi — controle sem USB 100% (SALVO 18/10/2026)

- IP fixo visto: `<TV-IP>` (wlan0, rede `<TV-SUBNET>/24`)
- Habilitar uma vez via USB (1007): `adb tcpip 5555`
- Conectar: `adb connect <TV-IP>:5555`
- Usar sempre com `-s`: `adb -s <TV-IP>:5555 shell wm size`, `adb -s <TV-IP>:5555 exec-out screencap -p > /tmp/opencode/tvbox-wifi.png`
- scrcpy sem fio: `scrcpy -s <TV-IP>:5555 --window-title "TV BOX WiFi" --stay-awake`
- Se ficar `offline`: `adb disconnect <TV-IP>:5555` + `adb tcpip 5555` (via USB 1007) + `adb connect <TV-IP>:5555` de novo
- Pode desplugar USB depois que WiFi virar `device` — OpenCode controla só pelo WiFi

## APP definitivo anti-queda (OpenBridge v15 foco branco + PIN) — INSTALADO 18/10/2026

- UI estética terminal OpenCode: preta, cantos quadrados, monospace, laranja; UM toggle `acesso_total`; card de PIN gigante + GERAR_NOVO_CODIGO (foco p/ controle remoto)
- Ícone round dark de opencode-dark.png; nome "Opencode TV"; KeepAlive sempre ativo (foreground ongoing + boot + onTaskRemoved)
- TV é ROOT — `persist.adb.tcp.port=5555` + `persist.sys.usb.config=mtp,adb` gravados via su

## Autenticação Wi-Fi por PIN (4 dígitos) — PIN É DINÂMICO, SEMPRE SINCRONIZAR

- PIN atual em `pin.txt`, mas **ele MUDA** quando o usuário toca GERAR_NOVO_CODIGO na TV
- **NUNCA assuma o valor guardado**: antes de qualquer comando ADB privilegiado (wm size, install, setprop, tcpip),
  rode `scripts/require-pin.sh <4-dígitos-informados>` — ele sincroniza da TV e compara
- Sem PIN informado: peça ao usuário os 4 dígitos da tela da TV
- Se não conferir: não executa, avisa e pede novo código

- PIN atual em `pin.txt` (agora: `1633`, informado pelo usuário via TV)
- Fluxo: mesmo Wi-Fi → app Opencode TV mostra o código grande na tela (botão GERAR_NOVO_CODIGO com controle remoto) → usuário informa os 4 dígitos → agente confere com `pin.txt` (sincronizar via `scripts/pin-sync.sh`, que puxa `/sdcard/OpencodeTV/pin.txt` da TV)
- Regra: antes de qualquer comando ADB privilegiado (wm size, install, setprop), pedir o PIN ao usuário e comparar com `pin.txt`. Se não bater, não executa e pede para gerar novo código na TV.
- Ao gerar novo código na TV, rodar `scripts/pin-sync.sh` para atualizar `pin.txt`.

- UI Material Design 3 com UM toggle só: `Acesso total OpenCode` ON/OFF (print `tvbox-toggle-v3.png` confirma roxo ON)
- ON ativa tudo: wake+wifi lock, ADB USB/WiFi, persist, boot. Resolução o OpenCode ajusta via ADB (só um aspecto)
- TV é ROOT (`uid=0`, test-keys, debuggable=1) — gravado via su: `persist.adb.tcp.port=5555` + `persist.sys.usb.config=mtp,adb` (sobrevive reboot, WiFi volta sozinho, USB nunca mais precisa)
- APK v3 (5,4M, Gradle+M3) instalado via USB 1007 + grant + aberto (PID 4729)

- APK compilado: `OPENBRIDGE.apk` (17K, assinado CN=OPENBRIDGE) — gerado sem Gradle via aapt2+javac+d8+zipalign+apksigner
- Instalado na TV via USB 1007: `adb -s 85017923031438000092 install -r OPENBRIDGE.apk` → Success
- Permissão concedida: `pm grant com.openbridge.remote WRITE_SECURE_SETTINGS` (USB e WiFi)
- App rodando: PID confirmado, print `tvbox-openbridge-app.png` mostra tela com IP + 8 botões
- `KeepAliveService` (foreground sticky): wake lock + wifi lock, reaplica a cada 60s

- `KeepAliveService` (foreground sticky): wake lock + wifi lock, reaplica a cada 60s `development_settings_enabled=1`, `adb_enabled=1`, `adb_wifi_enabled=1`, `adb_auto_revoke=0`, timeout máximo, `wifi_sleep_policy=2`
- `BootReceiver`: sobe sozinho após reboot da TV
- Permissão especial concedida UMA VEZ via notebook (USB 1007):
  `adb shell pm grant com.openbridge.remote android.permission.WRITE_SECURE_SETTINGS`
- Instalação definitiva (uma vez via USB 1007):
  `adb install -r OPENBRIDGE.apk` + grant acima + abrir app 1x + `adb tcpip 5555` + `adb connect IP:5555`
- Depois disso USB pode ficar fora: app segura acordado + `keep-wifi.sh`/systemd reconecta WiFi sozinho
- SDK compilando em background (JDK17 + cmdline-tools + android-34). Saída: `OPENBRIDGE.apk`

## Nunca-cai (persistente)

- Serviço notebook SEMPRE rodando: `systemctl --user status openbridge-keep-wifi.service` (`scripts/keep-wifi.sh <TV-IP>` reconecta a cada 10s)
- Uma vez via USB 1007 rodar: `scripts/persist-nunca-cai.sh` (timeout máximo, stayon, `wifi_sleep_policy=2`, `stay_on_while_plugged_in=3`, `persist.sys.usb.config=mtp,adb`, `service.adb.tcp.port=5555`, `deviceidle disable`)
- Na TV: se existir `ADB pela rede / Wireless debugging`, deixar LIGADO
- No roteador: reservar `<TV-IP>` para o MAC da TV (senão IP muda e cai)
- Cabo: usar porta firme, sem hub vagabundo (1006<->1007 piscando = cabo/energia)
- Recuperação: `scripts/wifi-conectar.sh` refaz `tcpip 5555` + `connect`

## Scripts desta skill

- `scripts/conectar.sh` — espera 1007 e mostra `adb devices`
- `scripts/wifi-conectar.sh` — faz `tcpip 5555` + `connect <TV-IP>:5555` e testa `wm size`
- `scripts/resolucao.sh 1280x720` — aplica resolução + print (aceita `ADB_SERIAL` env, ex: `ADB_SERIAL=<TV-IP>:5555 scripts/resolucao.sh 1280x700`)
- `scripts/screenshot.sh` — tira print pra `/tmp/opencode/`
- `scripts/manter-acordado.sh` — aplica trava anti-queda

## APK OPENBRIDGE

Código-fonte em `apk/` — app `com.openbridge.remote` nome `OPENBRIDGE`:
- Mostra IP WiFi + status ADB USB
- Botão Manter acordado (wake lock, não dorme)
- Botões de resolução (1280x720, 1280x700, 1024x576, 960x540, 800x600)
- Botão Ativar ADB WiFi (tenta `setprop service.adb.tcp.port 5555`, precisa root ou `adb tcpip 5555` pelo notebook)
- Como compilar: ver `apk/README.md`. Saída: `apk/app/build/outputs/apk/debug/app-debug.apk` renomear pra `OPENBRIDGE.apk`
- Instalar: `adb install -r OPENBRIDGE.apk` (com aparelho em 1007)
