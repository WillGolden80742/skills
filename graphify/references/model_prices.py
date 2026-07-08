#!/usr/bin/env python3
"""
model_prices.py — Python port of AdminModel::get_model_prices()

Fetches model prices from OpenRouter and OpenCode Zen APIs,
merges, sorts (free DeepSeek → free GPT → free others →
paid MiniMax → paid DeepSeek → paid GPT → paid others),
and caches to a JSON file for 5 minutes.

Usage:
    python model_prices.py              # print JSON result
    python model_prices.py --pretty      # print indented JSON
    python model_prices.py --cache-only  # read cached data (if fresh)
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

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


def _fetch_json(url):
    """Fetch URL, return parsed JSON dict/list, or None on failure."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
            if resp.status == 200:
                return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, OSError, json.JSONDecodeError):
        pass
    return None


# ---------------------------------------------------------------------------
# Normalisation / helpers
# ---------------------------------------------------------------------------
def _normalise_model_id(model_id):
    """Strip provider prefix, lowercase, dots → hyphens."""
    if "/" in model_id:
        model_id = model_id.split("/", 1)[1]
    return model_id.lower().replace(".", "-")


def _is_free_model(model):
    """Check if a model has no prices or all prices are zero/null."""
    prices = model.get("prices")
    if not prices:
        return True
    for provider_prices in prices.values():
        inp = provider_prices.get("input")
        out = provider_prices.get("output")
        if inp is not None and isinstance(inp, (int, float)) and inp > 0:
            return False
        if out is not None and isinstance(out, (int, float)) and out > 0:
            return False
    return True


def _model_sort_score(model):
    """
    Composite sort score (lower = appears first):

      Free:    0 DeepSeek, 1 GPT, 2 others
      Paid:   10 MiniMax, 11 DeepSeek, 12 GPT, 13 others
    """
    mid = (model.get("id") or "").lower()
    name = (model.get("name") or "").lower()

    is_free = _is_free_model(model)

    # Family priority
    if "deepseek" in mid or "deepseek" in name:
        family = 0
    elif "gpt" in mid or "gpt" in name or "openai" in mid:
        family = 1
    else:
        family = 2

    if is_free:
        return family  # 0, 1, or 2

    # Paid — MiniMax gets its own tier
    if "minimax" in mid or "minimax" in name:
        return 10

    return 11 + family  # 11, 12, or 13


# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------
def _read_cache():
    """Return cached data if fresh, else None."""
    try:
        mtime = os.path.getmtime(CACHE_FILE)
        if time.time() - mtime < CACHE_TTL:
            with open(CACHE_FILE, "r") as f:
                return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return None


def _write_cache(data):
    """Persist data to cache file."""
    os.makedirs(os.path.dirname(CACHE_FILE) or ".", exist_ok=True)
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def get_model_prices(cache_only=False):
    """
    Python equivalent of AdminModel::get_model_prices().

    Returns dict with keys:
      - updated_at  (ISO‑8601)
      - models      (list of model dicts)
    """
    # 1) Return cached data if fresh
    if not cache_only:
        cached = _read_cache()
        if cached is not None:
            return cached

    models = []

    # 2) Fetch from OpenCode Zen API
    zen_map = {}
    zen_data = _fetch_json("https://opencode.ai/zen/v1/models")
    if zen_data and isinstance(zen_data, dict):
        zen_items = zen_data.get("data")
        if isinstance(zen_items, list):
            for m in zen_items:
                norm_id = _normalise_model_id(m.get("id", ""))
                zen_map[norm_id] = {"originalId": m.get("id")}

    # 3) Fetch from OpenRouter API
    or_map = {}
    or_data = _fetch_json("https://openrouter.ai/api/v1/models")
    if or_data and isinstance(or_data, dict):
        or_items = or_data.get("data")
        if isinstance(or_items, list):
            for m in or_items:
                norm = _normalise_model_id(m.get("id", ""))
                pricing = m.get("pricing") or {}
                arch = m.get("architecture")

                # Extract family from architecture
                family = None
                if isinstance(arch, dict):
                    family = arch.get("tokenizer") or arch.get("modality")
                    if isinstance(family, str) and "-" in family:
                        family = family.split("-")[0]
                elif isinstance(arch, str):
                    family = arch

                prompt = pricing.get("prompt")
                completion = pricing.get("completion")

                or_map[norm] = {
                    "originalId": m.get("id"),
                    "name": m.get("name") or m.get("id"),
                    "input": (float(prompt) * 1_000_000) if prompt is not None else None,
                    "output": (float(completion) * 1_000_000) if completion is not None else None,
                    "context": m.get("context_length"),
                    "family": family,
                }

    # 4) Merge
    all_ids = sorted(set(list(zen_map.keys()) + list(or_map.keys())))

    for norm_id in all_ids:
        zen = zen_map.get(norm_id)
        or_ = or_map.get(norm_id)

        prices = {}
        if or_ and (or_["input"] is not None or or_["output"] is not None):
            prices["openrouter"] = {"input": or_["input"], "output": or_["output"]}
        if zen:
            prices["zen"] = {"input": None, "output": None}

        providers = []
        if zen:
            providers.append("zen")
        if or_:
            providers.append("openrouter")

        models.append({
            "id": or_["originalId"] if or_ else (zen["originalId"] if zen else norm_id),
            "name": or_["name"] if or_ else norm_id,
            "prices": prices if prices else None,
            "context": or_["context"] if or_ else None,
            "family": or_["family"] if or_ else None,
            "providers": providers,
        })

    # 5) Sort
    models.sort(key=_model_sort_score)

    result = {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "models": models,
    }

    # 6) Cache
    _write_cache(result)

    return result


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    cache_only = "--cache-only" in sys.argv
    pretty = "--pretty" in sys.argv

    data = get_model_prices(cache_only=cache_only)
    kwargs = {"indent": 2, "ensure_ascii": False} if pretty else {}
    print(json.dumps(data, **kwargs))
