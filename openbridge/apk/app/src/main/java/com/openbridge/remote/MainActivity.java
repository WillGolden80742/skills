package com.openbridge.remote;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Build;
import android.os.Bundle;
import android.os.PowerManager;
import android.provider.Settings;
import android.text.format.Formatter;

import androidx.appcompat.app.AppCompatActivity;

import com.google.android.material.chip.Chip;
import com.google.android.material.snackbar.Snackbar;

/** OPENBRIDGE v3 — ONE toggle only: full OpenCode access (resolution is just one aspect via ADB). */
public class MainActivity extends AppCompatActivity {

    android.view.View root;
    android.widget.TextView txtStatus;
    android.widget.TextView txtPin;
    android.widget.TextView txtIp;
    android.widget.TextView txtState;
    Chip chipAdb;
    com.google.android.material.button.MaterialButton btnPower;
    PowerManager.WakeLock wakeLock;
    WifiManager.WifiLock wifiLock;
    SharedPreferences prefs;

    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        setContentView(R.layout.activity_main);

        root = findViewById(android.R.id.content);
        txtStatus = findViewById(R.id.txtStatus);
        txtPin = findViewById(R.id.txtPin);
        txtIp = findViewById(R.id.txtIp);
        txtState = findViewById(R.id.txtState);
        chipAdb = findViewById(R.id.chipAdb);
        btnPower = findViewById(R.id.btnPower);
        prefs = getSharedPreferences("optvbox", MODE_PRIVATE);

        showPin(prefs.getString("pin", null), false);
        savePinFile(prefs.getString("pin", "0000"));
        findViewById(R.id.btnPin).setOnClickListener(v -> showPin(null, true));
        // barra lateral laranja SÓ quando o botão está selecionado (foco do controle)
        final android.view.View barBtn = findViewById(R.id.barBtn);
        findViewById(R.id.btnPin).setOnFocusChangeListener((v, f) ->
                barBtn.setVisibility(f ? android.view.View.VISIBLE : android.view.View.GONE));
        final android.view.View barPower = findViewById(R.id.barPower);
        btnPower.setOnFocusChangeListener((v, f) ->
                barPower.setVisibility(f ? android.view.View.VISIBLE : android.view.View.GONE));

        boolean on = prefs.getBoolean("total", true);
        paintPower(on);
        if (on) enableAll(false);

        btnPower.setOnClickListener(v -> {
            boolean now = !prefs.getBoolean("total", true);
            prefs.edit().putBoolean("total", now).apply();
            paintPower(now);
            if (now) enableAll(true);
            else disableAll();
            refresh();
        });

        refresh();
    }

    void paintPower(boolean on) {
        btnPower.setText(on ? "/TURN_OFF" : "/TURN_ON");
    }

    /** Enables EVERYTHING OpenCode needs for full access. */
    void enableAll(boolean notify) {
        // 0. Fora do Doze: pede liberação de bateria uma vez (usuário confirma no controle)
        try {
            android.os.PowerManager pm0 = (android.os.PowerManager) getSystemService(POWER_SERVICE);
            if (android.os.Build.VERSION.SDK_INT >= 23 && !pm0.isIgnoringBatteryOptimizations(getPackageName())) {
                Intent i = new Intent(android.provider.Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS,
                        android.net.Uri.parse("package:" + getPackageName()));
                startActivity(i);
            }
        } catch (Exception ignored) {}
        // 1. Serviço persistente (boot + reaplica a cada 60s)
        try {
            Intent s = new Intent(this, KeepAliveService.class);
            if (Build.VERSION.SDK_INT >= 26) startForegroundService(s);
            else startService(s);
        } catch (Exception ignored) {}
        // 2. Não dormir + WiFi no máximo
        try {
            Settings.System.putInt(getContentResolver(), Settings.System.SCREEN_OFF_TIMEOUT, Integer.MAX_VALUE);
        } catch (Exception ignored) {}
        try {
            PowerManager pm = (PowerManager) getSystemService(POWER_SERVICE);
            if (wakeLock == null) wakeLock = pm.newWakeLock(PowerManager.SCREEN_BRIGHT_WAKE_LOCK | PowerManager.ON_AFTER_RELEASE, "OPENBRIDGE:total");
            if (!wakeLock.isHeld()) wakeLock.acquire();
        } catch (Exception ignored) {}
        try {
            WifiManager wm = (WifiManager) getApplicationContext().getSystemService(Context.WIFI_SERVICE);
            if (wifiLock == null) wifiLock = wm.createWifiLock(WifiManager.WIFI_MODE_FULL_HIGH_PERF, "OPENBRIDGE:wifi");
            if (!wifiLock.isHeld()) wifiLock.acquire();
        } catch (Exception ignored) {}
        // 3. Settings de depuração (vale com WRITE_SECURE_SETTINGS concedido via adb)
        try { Settings.Global.putInt(getContentResolver(), Settings.Global.DEVELOPMENT_SETTINGS_ENABLED, 1); } catch (Exception ignored) {}
        try { Settings.Global.putInt(getContentResolver(), Settings.Global.ADB_ENABLED, 1); } catch (Exception ignored) {}
        try { Settings.Global.putInt(getContentResolver(), "adb_wifi_enabled", 1); } catch (Exception ignored) {}
        try { Settings.Global.putInt(getContentResolver(), "adb_auto_revoke", 0); } catch (Exception ignored) {}
        try { Settings.Global.putInt(getContentResolver(), "wifi_sleep_policy", 2); } catch (Exception ignored) {}
        try { Settings.Global.putInt(getContentResolver(), "stay_on_while_plugged_in", 3); } catch (Exception ignored) {}
        // 4. Tentativas shell (funcionam com root/shell; sem root só ignoram)
        try { Runtime.getRuntime().exec(new String[]{"sh", "-c", "svc power stayon true"}); } catch (Exception ignored) {}
        try { Runtime.getRuntime().exec(new String[]{"sh", "-c", "setprop service.adb.tcp.port 5555"}); } catch (Exception ignored) {}
        if (notify) snack("Full access ON — all open for OpenCode");
    }

    void disableAll() {
        try { KeepAliveService.cancelAlarm(this); } catch (Exception ignored) {}
        try { stopService(new Intent(this, KeepAliveService.class)); } catch (Exception ignored) {}
        try { if (wakeLock != null && wakeLock.isHeld()) wakeLock.release(); } catch (Exception ignored) {}
        try { if (wifiLock != null && wifiLock.isHeld()) wifiLock.release(); } catch (Exception ignored) {}
        snack("Full access OFF");
    }

    void refresh() {
        try {
            WifiManager wm = (WifiManager) getApplicationContext().getSystemService(Context.WIFI_SERVICE);
            WifiInfo wi = wm.getConnectionInfo();
            String ip = Formatter.formatIpAddress(wi.getIpAddress());
            boolean on = prefs.getBoolean("total", true);
            paintPower(on);
            txtStatus.setText((on ? "> full access ON\n" : "> full access OFF\n")
                    + "> ip " + ip + ":5555\n> adb connect " + ip + ":5555");
            txtIp.setText(ip);
            chipAdb.setText(on ? "opencode • full access • " + ip : "opencode • disabled");
            // estado real do adbd local: socket 127.0.0.1:5555
            new Thread(() -> {
                boolean up = false;
                try {
                    java.net.Socket s = new java.net.Socket();
                    s.connect(new java.net.InetSocketAddress("127.0.0.1", 5555), 2000);
                    s.close();
                    up = true;
                } catch (Exception ignored) {}
                final boolean ok = up;
                runOnUiThread(() -> {
                    txtState.setText(ok ? "device" : "offline");
                    txtState.setTextColor(ok ? 0xFFF5A742 : 0xFF9A9AA0);
                });
            }).start();
        } catch (Exception e) {
            txtStatus.setText("Status unavailable");
        }
    }

    /** Exibe o PIN; se null/vazio gera novo de 4 dígitos, salva e publica. */
    void showPin(String pin, boolean notify) {
        if (pin == null || pin.length() != 4) {
            pin = String.format("%04d", new java.util.Random().nextInt(10000));
            prefs.edit().putString("pin", pin).apply();
            savePinFile(pin);
            android.util.Log.i("OpencodeTV-PIN", "PIN=" + pin);
            if (notify) snack("New code: " + pin);
        }
        txtPin.setText(pin);
    }

    /** Salva o PIN onde o adb alcança (pasta externa do app + legado). */
    void savePinFile(String pin) {
        try {
            java.io.File d = getExternalFilesDir(null);
            if (d != null) {
                java.io.FileWriter w = new java.io.FileWriter(new java.io.File(d, "pin.txt"));
                w.write(pin);
                w.close();
            }
        } catch (Exception ignored) {}
        try {
            java.io.File d2 = new java.io.File("/sdcard/OpencodeTV");
            d2.mkdirs();
            java.io.FileWriter w2 = new java.io.FileWriter(new java.io.File(d2, "pin.txt"));
            w2.write(pin);
            w2.close();
        } catch (Exception ignored) {}
    }

    void snack(String s) {
        try { Snackbar.make(root, s, Snackbar.LENGTH_LONG).show(); }
        catch (Exception ignored) {}
    }
}
