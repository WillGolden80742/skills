# APK OPENBRIDGE — com.openbridge.remote

App para TV BOX Allwinner (dolphin_fvd_p1) deixar acesso WiFi fácil.

## O que faz
- Mostra IP WiFi para `adb connect IP:5555` + scrcpy sem fio
- Botão Manter acordado (wake lock + timeout máximo, segura ADB USB)
- Botões de resolução: 1280x720, 1280x700, 1024x576, 960x540, 800x600
  (no aparelho sem root o `wm size` pode negar; nesse caso use pelo notebook: `adb shell wm size ...`)
- Botão ADB WiFi 5555 (funciona com root ou após `adb tcpip 5555` pelo USB)

## Compilar (notebook com JDK 17 + SDK)
```
cd apk
# primeira vez:
sdkmanager "platform-tools" "platforms;android-34" "build-tools;34.0.0"
./gradlew :app:assembleDebug
# saída:
cp app/build/outputs/apk/debug/app-debug.apk ../OPENBRIDGE.apk
```

Sem gradle wrapper ainda? Gere com `gradle wrapper` ou use `gradle :app:assembleDebug`.

## Instalar na TV BOX (em modo 1007)
```
adb devices -l   # tem que mostrar 1f3a:1007 device
adb install -r OPENBRIDGE.apk
adb shell monkey -p com.openbridge.remote -c android.intent.category.LAUNCHER 1
```

## Acesso remoto via WiFi (sem cabo)
1. Notebook e TV BOX no mesmo WiFi
2. Uma vez via USB: `adb tcpip 5555`
3. Descubra IP na tela do OPENBRIDGE
4. `adb connect IP:5555` + `scrcpy --window-title "TV BOX"`
