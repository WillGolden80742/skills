#!/usr/bin/env python3
"""
sync_mirror.py — Sync bidirecional seguro entre pasta local e servidor remoto.
Protecoes: sem delete no remoto, sem push de 0 bytes, sem race condition.
"""

import os
import sys
import json
import time
import stat
import hashlib
import logging
import threading
import argparse
from pathlib import Path
from datetime import datetime

import paramiko
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("sync")

SSH_PASSWORD = os.environ.get("VPS_SSH_PW", "")
REMOTE_HOST = os.environ.get("VPS_REMOTE_HOST", "")
REMOTE_PORT = int(os.environ.get("VPS_REMOTE_PORT", "22"))
REMOTE_USER = os.environ.get("VPS_REMOTE_USER", "")

BASE = Path(__file__).parent.resolve()
REMOTE_BASE = os.environ.get("VPS_REMOTE_BASE", "/remote/path")
META = BASE / ".sync_meta.json"

POLL_INTERVAL = 4
DOWNLOADING_FILES = set()
DOWNLOAD_LOCK = threading.Lock()
MAX_WORKERS = 8

EXCLUDED = {".git", ".gitignore", ".sync_theme.py", ".sync_meta.json", "iniciar_espelho.bat"}
EXCLUDED_PREFIXES = (".git" + os.sep,)


def ssh_exec(cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(REMOTE_HOST, port=REMOTE_PORT, username=REMOTE_USER, password=SSH_PASSWORD, timeout=15)
    stdin, stdout, stderr = client.exec_command(cmd, timeout=30)
    rc = stdout.channel.recv_exit_status()
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    client.close()
    return rc, out, err


def sftp_get(remote_path, local_path):
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(REMOTE_HOST, port=REMOTE_PORT, username=REMOTE_USER, password=SSH_PASSWORD, timeout=15)
    sftp = client.open_sftp()
    try:
        sftp.get(remote_path, local_path)
    finally:
        sftp.close()
        client.close()


def sftp_put(local_path, remote_path):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(REMOTE_HOST, port=REMOTE_PORT, username=REMOTE_USER, password=SSH_PASSWORD, timeout=15)
    sftp = client.open_sftp()
    try:
        remote_dir = os.path.dirname(remote_path)
        _ensure_remote_dir(sftp, remote_dir)
        sftp.put(local_path, remote_path)
    finally:
        sftp.close()
        client.close()


def _ensure_remote_dir(sftp, path):
    parts = path.replace("\\", "/").split("/")
    current = ""
    for p in parts:
        if not p:
            continue
        current += "/" + p
        try:
            sftp.stat(current)
        except FileNotFoundError:
            sftp.mkdir(current)


def remote_list_all():
    exclude_git = r"-not -path '*/\.git' -a -not -path '*/\.git/*' -a -not -path '*/\.gitignore'"
    exclude_extra = r"-a -not -name '.sync_theme.py' -a -not -name '.sync_meta.json' -a -not -name 'iniciar_espelho.bat'"
    cmd = f"find {REMOTE_BASE} -type f {exclude_git} {exclude_extra} -printf '%P\\t%s\\t%T@\\n'"
    rc, out, err = ssh_exec(cmd)
    if rc != 0:
        log.error("Falha ao listar remoto: %s", err)
        return {}
    files = {}
    for line in out.strip().split("\n"):
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) >= 3:
            relpath = parts[0].replace("\\", "/")
            try:
                size = int(parts[1])
                mtime = float(parts[2])
            except ValueError:
                continue
            if size > 0:
                files[relpath] = {"size": size, "mtime": mtime}
    return files


def is_excluded(name):
    if name in EXCLUDED:
        return True
    for p in EXCLUDED_PREFIXES:
        if name.startswith(p):
            return True
    return False


def safe_remove_local(path):
    try:
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.remove(path)
    except OSError:
        pass


class UploadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        self._process(event.src_path)

    def on_created(self, event):
        if event.is_directory:
            return
        time.sleep(0.3)
        self._process(event.src_path)

    def on_moved(self, event):
        if event.is_directory:
            return
        time.sleep(0.3)
        self._process(event.dest_path)

    def _process(self, src_path):
        rel = os.path.relpath(src_path, str(BASE)).replace("\\", "/")
        if is_excluded(rel):
            return
        if not os.path.isfile(src_path):
            return
        size = os.path.getsize(src_path)
        if size == 0:
            log.info("WATCH-SAFE Ignorado envio do arquivo local vazio: %s", rel)
            return
        with DOWNLOAD_LOCK:
            if rel in DOWNLOADING_FILES:
                log.info("WATCH-SAFE Ignorado: %s esta sendo baixado agora", rel)
                return
        remote_path = REMOTE_BASE + "/" + rel
        log.info("UPLOAD %s (%d bytes)", rel, size)
        try:
            sftp_put(src_path, remote_path)
            log.info("UPLOAD OK %s", rel)
        except Exception as e:
            log.error("UPLOAD FAIL %s: %s", rel, e)


def download_worker(rel, remote_path, local_path):
    with DOWNLOAD_LOCK:
        DOWNLOADING_FILES.add(rel)
    try:
        sftp_get(remote_path, local_path)
        size = os.path.getsize(local_path)
        if size == 0:
            safe_remove_local(local_path)
            log.warning("DOWNLOAD-SAFE Removido local vazio: %s", rel)
        else:
            log.info("DOWNLOAD OK %s (%d bytes)", rel, size)
    except Exception as e:
        log.error("DOWNLOAD FAIL %s: %s", rel, e)
    finally:
        with DOWNLOAD_LOCK:
            DOWNLOADING_FILES.discard(rel)


def download_all(remote_files):
    existing = {}
    for root, dirs, fnames in os.walk(str(BASE)):
        for fname in fnames:
            fpath = os.path.join(root, fname)
            rel = os.path.relpath(fpath, str(BASE)).replace("\\", "/")
            existing[rel] = fpath

    to_download = []
    for rel, meta in remote_files.items():
        if rel in existing:
            continue
        local_path = str(BASE / rel)
        to_download.append((rel, REMOTE_BASE + "/" + rel, local_path))

    if not to_download:
        log.info("Nenhum arquivo novo para baixar.")
        return

    log.info("Preparando download de %d arquivos...", len(to_download))

    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        for rel, rpath, lpath in to_download:
            pool.submit(download_worker, rel, rpath, lpath)
    log.info("Downloads concluidos.")


def poll_remote(remote_files):
    local_set = set()
    for root, dirs, fnames in os.walk(str(BASE)):
        for fname in fnames:
            rel = os.path.relpath(os.path.join(root, fname), str(BASE)).replace("\\", "/")
            if not is_excluded(rel):
                local_set.add(rel)

    missing = [r for r in remote_files if r not in local_set]
    if missing:
        log.info("Remoto tem %d arquivos que faltam localmente. Iniciando download...", len(missing))
        for rel in missing:
            rpath = REMOTE_BASE + "/" + rel
            lpath = str(BASE / rel)
            download_worker(rel, rpath, lpath)


def save_meta(data):
    with open(META, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_meta():
    if META.exists():
        with open(META, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def main(runtime_minutes=120):
    if not SSH_PASSWORD:
        log.error("Variavel VPS_SSH_PW nao definida!")
        sys.exit(1)

    log.info("Origem : %s", REMOTE_BASE)
    log.info("Destino: %s", BASE)
    log.info("Carregando metadados...")

    remote_files = remote_list_all()
    if not remote_files:
        log.error("Nao foi possivel obter lista de arquivos remotos!")
        sys.exit(1)
    log.info("Remoto: %d arquivos (%.2f MB)", len(remote_files),
             sum(f["size"] for f in remote_files.values()) / 1e6)

    save_meta(remote_files)
    log.info("Metadados salvos (%d entradas).", len(remote_files))

    download_all(remote_files)

    event_handler = UploadHandler()
    observer = Observer()
    observer.schedule(event_handler, str(BASE), recursive=True)
    observer.start()
    log.info("Observador de arquivos iniciado.")

    end_time = time.time() + runtime_minutes * 60
    poll_counter = 0

    try:
        while time.time() < end_time:
            time.sleep(POLL_INTERVAL)
            poll_counter += 1
            if poll_counter % 15 == 0:
                log.info("Poll #%d — verificando novidades no servidor...", poll_counter)
                try:
                    fresh_remote = remote_list_all()
                    poll_remote(fresh_remote)
                    save_meta(fresh_remote)
                except Exception as e:
                    log.error("Poll error: %s", e)
    except KeyboardInterrupt:
        log.info("Encerrando por solicitacao do usuario...")
    finally:
        observer.stop()
        observer.join()
        log.info("Espelho encerrado.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync bidirecional seguro")
    parser.add_argument("runtime", nargs="?", type=int, default=120,
                        help="Tempo de execucao em minutos (default: 120)")
    args = parser.parse_args()
    main(args.runtime)
