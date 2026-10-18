package com.openbridge.remote;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Build;

/** Sobe o KeepAlive sozinho após reboot / boot da TV. */
public class BootReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context c, Intent i) {
        try {
            // Só sobe sozinho se o estado for /ON
            if (!c.getSharedPreferences("optvbox", Context.MODE_PRIVATE).getBoolean("total", true)) return;
            Intent s = new Intent(c, KeepAliveService.class);
            if (Build.VERSION.SDK_INT >= 26) c.startForegroundService(s);
            else c.startService(s);
        } catch (Exception ignored) {}
    }
}
