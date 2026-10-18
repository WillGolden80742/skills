package com.openbridge.remote;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.net.wifi.WifiManager;
import android.os.Build;
import android.os.IBinder;
import android.os.PowerManager;
import android.provider.Settings;

/** Serviço que nunca deixa a TV dormir e mantém ADB/WiFi vivos. */
public class KeepAliveService extends Service {

    PowerManager.WakeLock wl;
    WifiManager.WifiLock wifiLock;

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        // Respeita o estado: se o usuário desligou (/OFF), não liga nada
        if (!getSharedPreferences("optvbox", MODE_PRIVATE).getBoolean("total", true)) {
            stopSelf();
            return START_NOT_STICKY;
        }
        startFg();
        acquire();
        // Alarme exato a cada 60s: se o sistema matar o serviço, ele volta sozinho
        try {
            android.app.PendingIntent pi = android.app.PendingIntent.getService(
                    this, 7, new Intent(this, KeepAliveService.class),
                    android.app.PendingIntent.FLAG_UPDATE_CURRENT | android.app.PendingIntent.FLAG_IMMUTABLE);
            android.app.AlarmManager am = (android.app.AlarmManager) getSystemService(ALARM_SERVICE);
            long next = android.os.SystemClock.elapsedRealtime() + 60000;
            if (android.os.Build.VERSION.SDK_INT >= 23) am.setExactAndAllowWhileIdle(
                    android.app.AlarmManager.ELAPSED_REALTIME_WAKEUP, next, pi);
            else am.setExact(android.app.AlarmManager.ELAPSED_REALTIME_WAKEUP, next, pi);
        } catch (Exception ignored) {}
        // Reaplica travas a cada 60s via thread (para se /OFF)
        new Thread(new Runnable() {
            @Override public void run() {
                while (true) {
                    try {
                        Thread.sleep(60000);
                        if (!getSharedPreferences("optvbox", MODE_PRIVATE).getBoolean("total", true)) {
                            cancelAlarm(KeepAliveService.this);
                            stopSelf();
                            break;
                        }
                        keep();
                    } catch (Exception ignored) { break; }
                }
            }
        }).start();
        return START_STICKY;
    }

    void startFg() {
        try {
            String ch = "openbridge";
            if (Build.VERSION.SDK_INT >= 26) {
                NotificationManager nm = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
                nm.createNotificationChannel(new NotificationChannel(ch, "OpenBridge", NotificationManager.IMPORTANCE_MIN));
                Notification n = new Notification.Builder(this, ch)
                        .setContentTitle("OpenBridge active")
                        .setContentText("Full access always on")
                        .setSmallIcon(android.R.drawable.stat_sys_data_bluetooth)
                        .setOngoing(true)
                        .build();
                startForeground(1, n);
            }
        } catch (Exception ignored) {}
    }

    void acquire() {
        try {
            PowerManager pm = (PowerManager) getSystemService(POWER_SERVICE);
            if (wl == null) wl = pm.newWakeLock(PowerManager.SCREEN_BRIGHT_WAKE_LOCK | PowerManager.ON_AFTER_RELEASE, "OPENBRIDGE:keep");
            if (!wl.isHeld()) wl.acquire();
        } catch (Exception ignored) {}
        try {
            WifiManager wm = (WifiManager) getApplicationContext().getSystemService(Context.WIFI_SERVICE);
            if (wifiLock == null) wifiLock = wm.createWifiLock(WifiManager.WIFI_MODE_FULL_HIGH_PERF, "OPENBRIDGE:wifi");
            if (!wifiLock.isHeld()) wifiLock.acquire();
        } catch (Exception ignored) {}
        keep();
    }

    /** Reaplica settings que seguram depuração (precisa de WRITE_SECURE_SETTINGS concedido uma vez via adb). */
    void keep() {        try {
            Settings.Global.putInt(getContentResolver(), Settings.Global.DEVELOPMENT_SETTINGS_ENABLED, 1);
            Settings.Global.putInt(getContentResolver(), Settings.Global.ADB_ENABLED, 1);
            try { Settings.Global.putInt(getContentResolver(), "adb_wifi_enabled", 1); } catch (Exception ignored) {}
            try { Settings.Global.putInt(getContentResolver(), "adb_auto_revoke", 0); } catch (Exception ignored) {}
            try { Settings.System.putInt(getContentResolver(), Settings.System.SCREEN_OFF_TIMEOUT, Integer.MAX_VALUE); } catch (Exception ignored) {}
            try { Settings.Global.putInt(getContentResolver(), "wifi_sleep_policy", 2); } catch (Exception ignored) {}
            try { Settings.Global.putInt(getContentResolver(), "stay_on_while_plugged_in", 3); } catch (Exception ignored) {}
        } catch (SecurityException se) {
            // Sem WRITE_SECURE_SETTINGS ainda: precisa rodar 1x via notebook:
            // adb shell pm grant com.openbridge.remote android.permission.WRITE_SECURE_SETTINGS
        } catch (Exception ignored) {}
        // Auto-cura do ADB Wi-Fi (TV é root): se a porta sumiu, religa sozinha
        try {
            String port = sh("getprop service.adb.tcp.port").trim();
            if (port.isEmpty()) {
                sh("su -c 'setprop service.adb.tcp.port 5555'");
            }
            // Doze não pode encostar no ADB: tenta desligar o deviceidle (via root)
            sh("su -c 'dumpsys deviceidle disable'");
        } catch (Exception ignored) {}
    }

    static String sh(String cmd) {
        try {
            java.io.InputStream in = Runtime.getRuntime().exec(
                    new String[]{"sh", "-c", cmd}).getInputStream();
            java.io.ByteArrayOutputStream out = new java.io.ByteArrayOutputStream();
            byte[] buf = new byte[512];
            int n;
            while ((n = in.read(buf)) > 0) out.write(buf, 0, n);
            return out.toString("UTF-8");
        } catch (Exception e) {
            return "";
        }
    }

    @Override public IBinder onBind(Intent i) { return null; }

    static void cancelAlarm(Context c) {
        try {
            android.app.PendingIntent pi = android.app.PendingIntent.getService(
                    c, 7, new Intent(c, KeepAliveService.class),
                    android.app.PendingIntent.FLAG_UPDATE_CURRENT | android.app.PendingIntent.FLAG_IMMUTABLE);
            android.app.AlarmManager am = (android.app.AlarmManager) c.getSystemService(ALARM_SERVICE);
            am.cancel(pi);
            pi.cancel();
        } catch (Exception ignored) {}
    }

    /** Se o sistema matar a tarefa, agenda o próprio retorno em 5s (só se /ON). */
    @Override public void onTaskRemoved(Intent rootIntent) {
        try {
            if (!getSharedPreferences("optvbox", MODE_PRIVATE).getBoolean("total", true)) return;
            android.app.PendingIntent pi = android.app.PendingIntent.getService(
                    this, 1, new Intent(this, KeepAliveService.class),
                    android.app.PendingIntent.FLAG_ONE_SHOT | android.app.PendingIntent.FLAG_IMMUTABLE);
            android.app.AlarmManager am = (android.app.AlarmManager) getSystemService(ALARM_SERVICE);
            am.set(android.app.AlarmManager.ELAPSED_REALTIME_WAKEUP,
                    android.os.SystemClock.elapsedRealtime() + 5000, pi);
        } catch (Exception ignored) {}
    }
}
