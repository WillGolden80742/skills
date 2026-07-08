#!/usr/bin/env python3
"""
model_prices.py — Mostra árvore de modelos gratuitos (prioridade DeepSeek)

Faz fetch da OpenRouter API, filtra apenas modelos com "free" no id/name,
e exibe em formato de árvore organizada por provedor/família.

Usage:
    python model_prices.py                  # árvore colorida
    python model_prices.py --json           # JSON puro
    python model_prices.py --flat           # lista plana
    python model_prices.py --cache-only     # usa cache existente
    python model_prices.py --update         # força refresh do cache
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from collections import defaultdict

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_FILE = os.path.join(SCRIPT_DIR, ".model_prices_cache.json")
CACHE_TTL = 5 * 60  # 5 minutes

# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------
USER_AGENT = "uailove/1.0"
REQUEST_TIMEOUT = 15


def _load_env():
    """Carrega .env se existir (prioridade: OPENAI_API_KEY para OpenRouter)."""
    env_paths = [
        os.path.join(SCRIPT_DIR, "..", "..", "..", "..", "graphify-out", ".env"),
        os.path.join(SCRIPT_DIR, "..", "..", "..", "graphify-out", ".env"),
        os.path.join(SCRIPT_DIR, ".env"),
    ]
    for p in env_paths:
        p = os.path.abspath(p)
        if os.path.isfile(p):
            with open(p) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        os.environ.setdefault(k.strip(), v.strip())
            break


def _fetch_json(url, api_key=None):
    """Fetch URL, return parsed JSON, or None on failure."""
    headers = {"User-Agent": USER_AGENT}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
            if resp.status == 200:
                return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, OSError, json.JSONDecodeError):
        pass
    return None


# ---------------------------------------------------------------------------
# Normalisation
# ---------------------------------------------------------------------------
def _normalise_model_id(model_id):
    """Strip provider prefix, lowercase, dots → hyphens."""
    if "/" in model_id:
        model_id = model_id.split("/", 1)[1]
    return model_id.lower().replace(".", "-")


# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------
def _read_cache():
    try:
        mtime = os.path.getmtime(CACHE_FILE)
        if time.time() - mtime < CACHE_TTL:
            with open(CACHE_FILE) as f:
                return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return None


def _write_cache(data):
    os.makedirs(os.path.dirname(CACHE_FILE) or ".", exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f)


# ---------------------------------------------------------------------------
# Fetch + filter
# ---------------------------------------------------------------------------
def get_free_models(force_refresh=False):
    """
    Retorna lista de modelos gratuitos da OpenRouter, ordenados:
    DeepSeek free → GPT free → outros free.
    Cada item: {id, name, provider, family, context, input, output}
    """
    if not force_refresh:
        cached = _read_cache()
        if cached is not None:
            return cached

    _load_env()
    api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("OPENCODE_API_KEY")

    # Fetch OpenRouter
    or_data = _fetch_json("https://openrouter.ai/api/v1/models", api_key=api_key)
    free_models = []

    if or_data and isinstance(or_data, dict):
        items = or_data.get("data")
        if isinstance(items, list):
            for m in items:
                mid = (m.get("id") or "").lower()
                mname = (m.get("name") or "").lower()

                # Critério: gratuito (contém "free") OU DeepSeek (prioridade do usuário)
                is_free = "free" in mid or "free" in mname
                is_deepseek = "deepseek" in mid or "deepseek" in mname
                if not is_free and not is_deepseek:
                    continue

                pricing = m.get("pricing") or {}
                prompt = pricing.get("prompt")
                completion = pricing.get("completion")

                # Extrair provider (ex: "openai/gpt-4o-free" → "openai")
                provider = mid.split("/")[0] if "/" in mid else "other"

                # Determinar família para prioridade
                if "deepseek" in mid or "deepseek" in mname:
                    family = "deepseek"
                    priority = 0
                elif "gpt" in mid or "openai" in mid or "gpt" in mname:
                    family = "gpt"
                    priority = 1
                else:
                    family = "other"
                    priority = 2

                free_models.append({
                    "id": m.get("id"),
                    "name": m.get("name") or m.get("id"),
                    "provider": provider,
                    "family": family,
                    "priority": priority,
                    "context": m.get("context_length"),
                    "input_price": (float(prompt) * 1_000_000) if prompt is not None else 0,
                    "output_price": (float(completion) * 1_000_000) if completion is not None else 0,
                })

    # Ordenar: priority (DeepSeek=0, GPT=1, other=2) → nome
    free_models.sort(key=lambda x: (x["priority"], x["family"], x["name"]))

    _write_cache(free_models)
    return free_models


# ---------------------------------------------------------------------------
# Display: árvore
# ---------------------------------------------------------------------------
def _print_tree(models):
    """Exibe modelos em formato de árvore por família."""
    if not models:
        print(" Nenhum modelo gratuito encontrado.")
        return

    # Agrupar por família
    tree = defaultdict(list)
    for m in models:
        tree[m["family"]].append(m)

    family_names = {"deepseek": "DeepSeek", "gpt": "GPT / OpenAI", "other": "Outros"}
    family_icons = {"deepseek": "", "gpt": "", "other": ""}

    total = len(models)
    print(f" Modelos gratuitos encontrados: {total}\n")

    for fam_key in ["deepseek", "gpt", "other"]:
        items = tree.get(fam_key, [])
        if not items:
            continue

        label = family_names.get(fam_key, fam_key)
        print(f" {label}")

        for m in items:
            # Provider badge
            prov = m["provider"]
            ctx = m["context"]
            ctx_str = f"ctx={ctx}" if ctx else ""

            # Preço (já multiplicado por 1M = preço por milhão de tokens)
            out = m["output_price"]
            inp = m["input_price"]
            if out == 0 and inp == 0:
                price_str = "Grátis"
            elif out < 0.01:
                price_str = f"${out:.4f}/1M"
            else:
                price_str = f"${out:.2f}/1M"

            print(f"   {m['id']}")
            print(f"       {price_str}  |  {ctx_str}  |  {prov}")

        print()

    print(f" ({total} modelos)")


def _print_flat(models):
    """Lista plana."""
    for m in models:
        print(f"{m['family']:10s}  {m['id']:50s}  Grátis")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    flags = set(sys.argv[1:])

    force = "--update" in flags or "--force" in flags
    as_json = "--json" in flags
    flat = "--flat" in flags
    cache_only = "--cache-only" in flags

    if cache_only and not force:
        models = get_free_models(force_refresh=False)
        if models is None or (isinstance(models, list) and not models):
            # Try reading cache directly
            cached = _read_cache()
            if cached:
                models = cached
    else:
        models = get_free_models(force_refresh=force)

    if as_json:
        print(json.dumps(models, indent=2, ensure_ascii=False))
    elif flat:
        _print_flat(models)
    else:
        _print_tree(models)
