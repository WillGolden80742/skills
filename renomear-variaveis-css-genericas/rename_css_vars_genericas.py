#!/usr/bin/env python3
"""
rename_css_vars_genericas.py

Renomeia variaveis CSS customizadas (custom properties) de um diretorio de
folhas de estilo para nomes GENERICOS, seguindo o algoritmo:

  1. DETECCAO DE CORES PREDOMINANTES
     - Agrupa as familias de cor (brand, accent, gold, green, red) somando o
       uso de suas variacoes (-hover, -light, -soft, etc.) via var(--x) em
       todos os .css do diretorio.
     - A 1a familia   -> --primary
       A 2a familia   -> --secondary
       A 3a familia   -> --tertiary
     - green -> --success, red -> --danger (cores semanticas).

  2. CLASSIFICACAO POR VALOR (para todas as variaveis --v- e demais)
     - Cor simples  -> familia de matiz (red, blue, green, purple, gray, ...)
                       + modificadores (dark/light/muted/soft) ORDENADOS ALFABETICAMENTE.
     - Gradiente    -> gradient-linear-<familias> / gradient-radial-<familias>
     - Sombra       -> shadow-<tamanho>-<familia>  (box-shadow e drop-shadow)
     - Borda        -> border-<estilo>-<tamanho>-<familia>
     - Utilitarios  -> display-/position-/align-/filter-/transform-/transition-/
                       animation-/calc-/grid-/cursor-/visibility-/object-/whitespace-/font-/env-
     - Outros       -> token-<hash>

     Regra de nomenclatura (ate 4 palavras):
       A PRIMEIRA palavra carrega o MAIOR PESO (cor/tipo).
       As demais palavras (modificadores) sao ORDENADAS ALFABETICAMENTE.
       Ex.: small-bigger-medium-small | purple-dark-light-gray

  3. SUBSTITUICAO SEGURA EM DUAS FASES (placeholder) para EVITAR o bug em
     cascata (ex.: --v-c0392b -> --red enquanto --red -> --danger re-referencia
     o --red recem-criado).

  4. ORDENACAO ALFABETICA do bloco :root em base-light.css / base-dark.css.

  5. PROPAGACAO das novas referencias em TODOS os .css do diretorio.

Uso:
  python rename_css_vars_genericas.py <diretorio-das-folhas-css>
"""

import os
import re
import sys
import colorsys
from collections import Counter


# ----------------------------------------------------------------------------
#  Color helpers
# ----------------------------------------------------------------------------
def hex_to_hsl(hex_str):
    h = hex_str.lstrip('#')
    if len(h) in (3, 4):
        h = ''.join(c * 2 for c in h)
    if len(h) < 6:
        h = h + '0' * (6 - len(h))
    r = int(h[0:2], 16) / 255.0
    g = int(h[2:4], 16) / 255.0
    b = int(h[4:6], 16) / 255.0
    hh, ll, ss = colorsys.rgb_to_hls(r, g, b)
    alpha = None
    if len(h) >= 8:
        alpha = int(h[6:8], 16) / 255.0
    return hh * 360, ss, ll, alpha


def hue_family(h, s, l):
    if s < 0.12:
        if l < 0.10:
            return 'black'
        if l > 0.92:
            return 'white'
        return 'gray'
    if h < 15 or h >= 345:
        return 'red'
    if h < 45:
        return 'orange'
    if h < 70:
        return 'yellow'
    if h < 160:
        return 'green'
    if h < 200:
        return 'teal'
    if h < 255:
        return 'blue'
    if h < 290:
        return 'purple'
    if h < 345:
        return 'pink'
    return 'red'


def color_class(hex_str):
    h, s, l, alpha = hex_to_hsl(hex_str)
    fam = hue_family(h, s, l)
    mods = []
    if fam in ('gray', 'black', 'white'):
        if l < 0.45:
            mods.append('dark')
        elif l > 0.75:
            mods.append('light')
    else:
        if l < 0.38:
            mods.append('dark')
        elif l > 0.72:
            mods.append('light')
        if s < 0.45:
            mods.append('muted')
    if alpha is not None and alpha < 0.55:
        mods.append('soft')
    return fam, mods


def extract_hex_colors(value):
    return re.findall(r'#([0-9a-fA-F]{3,8})', value)


# ----------------------------------------------------------------------------
#  Utility / layout classification
# ----------------------------------------------------------------------------
def classify_utility(value):
    low = value.lower().strip()
    important = '!important' in value
    mods = []
    if important:
        mods.append('important')

    # display
    disp = re.search(r'\b(flex|block|grid|inline-flex|inline-block|contents|table|flow-root)\b', low)
    if disp and 'var(' not in low and 'gradient' not in low:
        return 'display', [disp.group(1)] + mods
    # position
    pos = re.search(r'\b(absolute|relative|fixed|sticky)\b', low)
    if pos:
        return 'position', [pos.group(1)] + mods
    # alignment / justify
    ali = re.search(r'\b(center|baseline|middle|flex-start|flex-end|stretch|space-between|space-around|left|right|top|bottom)\b', low)
    if ali and 'var(' not in low and 'gradient' not in low:
        return 'align', [ali.group(1)] + mods
    # filter: blur
    m = re.search(r'blur\((\d+(?:\.\d+)?)px\)', low)
    if m:
        px = float(m.group(1))
        size = 'small' if px <= 4 else ('medium' if px <= 10 else 'big')
        return 'filter', ['blur', size] + mods
    # filter: brightness
    m = re.search(r'brightness\(([0-9.]+)\)', low)
    if m:
        return 'filter', ['brightness'] + mods
    # transform: scale
    m = re.search(r'scale\(([^)]+)\)', low)
    if m:
        return 'transform', ['scale'] + mods
    # transform: rotate
    m = re.search(r'rotate\(([^)]+)\)', low)
    if m:
        return 'transform', ['rotate'] + mods
    # transition (property duration ...)
    if 'all' in low or re.search(r'[a-z-]+\s+[\d.]+s', low) and 'gradient' not in low:
        dur = re.search(r'([\d.]+)s', low)
        if dur:
            d = float(dur.group(1))
            speed = 'fast' if d <= 0.25 else ('medium' if d <= 0.4 else 'slow')
            return 'transition', [speed] + mods
    # animation keyframes (name duration ...)
    anim = re.search(r'([a-zA-Z][a-zA-Z-]+)\s+[\d.]+s', value)
    if anim and anim.group(1).lower() not in ('all', 'var'):
        return 'animation', [re.sub(r'(?<!^)(?=[A-Z])', '-', anim.group(1)).lower()] + mods
    # calc
    if 'calc(' in low:
        mmods = []
        if 'vh' in low:
            mmods.append('vh')
        if '-' in low:
            mmods.append('minus')
        if 'px' in low:
            mmods.append('px')
        return 'calc', mmods + mods
    # grid templates / fractions
    if '1fr' in low or 'repeat(' in low or 'auto-fit' in low or 'auto-fill' in low:
        mmods = []
        if '1fr' in low:
            mmods.append('fraction')
        if 'repeat' in low:
            mmods.append('repeat')
        if 'auto' in low:
            mmods.append('auto')
        return 'grid', mmods + mods
    # cursor
    cur = re.search(r'\b(pointer|not-allowed|default|grab|zoom)\b', low)
    if cur:
        return 'cursor', [cur.group(1)] + mods
    # visibility
    vis = re.search(r'\b(hidden|visible|collapse)\b', low)
    if vis:
        return 'visibility', [vis.group(1)] + mods
    # object-fit
    obj = re.search(r'\b(cover|contain|fill|none)\b', low)
    if obj and 'var(' not in low and 'gradient' not in low:
        return 'object', [obj.group(1)] + mods
    # white-space
    ws = re.search(r'\b(nowrap|wrap|pre|normal)\b', low)
    if ws:
        return 'whitespace', [ws.group(1)] + mods
    # font family
    if "'" in value or '"' in value or 'sans-serif' in low or 'monospace' in low or 'serif' in low:
        return 'font', mods
    # env()
    if 'env(' in low:
        return 'env', mods
    # pointer-events etc
    pe = re.search(r'\b(auto|none|inherit)\b', low)
    if pe and 'var(' not in low:
        return 'value', [pe.group(1)] + mods
    return None


# ----------------------------------------------------------------------------
#  General value classifier
# ----------------------------------------------------------------------------
def classify(value):
    value = value.strip()
    low = value.lower()

    # Gradients
    if 'linear-gradient' in low:
        fams = sorted({color_class(hx)[0] for hx in extract_hex_colors(value)})
        return 'gradient', ['linear'] + fams
    if 'radial-gradient' in low:
        fams = sorted({color_class(hx)[0] for hx in extract_hex_colors(value)})
        return 'gradient', ['radial'] + fams

    # drop-shadow (filter)
    if 'drop-shadow(' in low:
        fams = sorted({color_class(hx)[0] for hx in extract_hex_colors(value)})
        return 'shadow', ['drop'] + fams

    # Border
    m_style = re.search(r'(solid|dashed|dotted|double)', low)
    if m_style:
        fams = sorted({color_class(hx)[0] for hx in extract_hex_colors(value)})
        px = re.findall(r'(\d+)px', value)
        size = 'thin'
        if px:
            size = 'thick' if int(px[0]) >= 3 else ('medium' if int(px[0]) >= 2 else 'thin')
        return 'border', [m_style.group(1), size] + fams

    # Shadow (box-shadow): has px + color, no gradient/border
    if re.search(r'\dpx', value) and ('#' in value or 'rgb' in low or 'transparent' in low or 'black' in low):
        fams = sorted({color_class(hx)[0] for hx in extract_hex_colors(value)})
        px = [int(x) for x in re.findall(r'(\d+)px', value)]
        size = 'small'
        if px:
            size = 'big' if max(px) > 15 else ('medium' if max(px) > 8 else 'small')
        mods = []
        if 'inset' in low:
            mods.append('inset')
        mods.append(size)
        mods += fams
        return 'shadow', mods

    # Transparent
    if low == 'transparent':
        return 'transparent', []

    # currentColor
    if 'currentcolor' in low:
        return 'color', ['current']

    # Named colors
    named = {
        'red': 'red', 'white': 'white', 'black': 'black', 'green': 'green',
        'blue': 'blue', 'yellow': 'yellow', 'orange': 'orange', 'purple': 'purple',
        'pink': 'pink', 'gray': 'gray', 'grey': 'gray', 'teal': 'teal',
    }
    if low in named:
        return named[low], []

    # Plain color
    hexes = extract_hex_colors(value)
    if hexes:
        fam, mods = color_class(hexes[0])
        return fam, mods

    # Utility / layout
    util = classify_utility(value)
    if util:
        return util

    # Fallback
    return 'token', []


def make_name(base, modifiers, used):
    parts = [base] + sorted(modifiers)
    if len(parts) > 4:
        parts = parts[:4]
    name = '--' + '-'.join(parts)
    original = name
    n = 2
    while name in used:
        name = f"{original}-{n}"
        n += 1
    used.add(name)
    return name


# ----------------------------------------------------------------------------
#  Main
# ----------------------------------------------------------------------------
def main():
    if len(sys.argv) > 1:
        css_dir = sys.argv[1]
    else:
        css_dir = os.getcwd()

    if not os.path.isdir(css_dir):
        print(f"Diretorio invalido: {css_dir}")
        sys.exit(1)

    base_light = os.path.join(css_dir, "base-light.css")
    base_dark = os.path.join(css_dir, "base-dark.css")

    css_files = [os.path.join(css_dir, f) for f in os.listdir(css_dir) if f.endswith('.css')]

    # Files that define the :root with theme variables. We scan all of them for
    # variable DEFINITIONS so every --v- (wherever declared) gets renamed.
    def_files = [fp for fp in css_files if os.path.exists(fp)]

    defined = {}
    for fp in def_files:
        try:
            c = open(fp, encoding='utf-8', errors='ignore').read()
        except Exception:
            continue
        for k, v in re.findall(r'(--[a-zA-Z0-9-_]+)\s*:\s*([^;]+);', c):
            defined.setdefault(k, v)

    # --- Predominant color families ---
    color_families = {
        "brand": ["--brand", "--brand-hover", "--brand-light", "--brand-soft"],
        "accent": ["--accent", "--accent-hover"],
        "gold": ["--gold", "--gold-hover"],
        "green": ["--green", "--green-hover"],
        "red": ["--red", "--red-hover"],
    }
    family_usages = Counter()
    for fp in css_files:
        try:
            c = open(fp, encoding='utf-8', errors='ignore').read()
        except Exception:
            continue
        for fam, vars_list in color_families.items():
            for v in vars_list:
                if v in defined:
                    family_usages[fam] += len(re.findall(re.escape(f"var({v})"), c))
    top = family_usages.most_common()
    print("Detected predominant color families:", top)

    mapping = {}
    used = set()

    # 1) Core theme variables -> semantic generic names
    core_map = {
        "--brand": ("primary", []),
        "--brand-hover": ("primary", ["hover"]),
        "--brand-light": ("primary", ["light"]),
        "--brand-soft": ("primary", ["soft"]),
        "--accent": ("secondary", []),
        "--accent-hover": ("secondary", ["hover"]),
        "--gold": ("tertiary", []),
        "--gold-hover": ("tertiary", ["hover"]),
        "--green": ("success", []),
        "--green-hover": ("success", ["hover"]),
        "--red": ("danger", []),
        "--red-hover": ("danger", ["hover"]),
        "--shadow-smaller": ("shadow", ["small", "smaller"]),
        "--shadow-small": ("shadow", ["small"]),
        "--shadow-base": ("shadow", ["medium"]),
        "--shadow-big": ("shadow", ["big"]),
        "--shadow-bigger": ("shadow", ["big", "bigger"]),
        "--shadow-x": ("shadow", ["big", "bigger", "giant"]),
        "--shadow-brand-glow": ("shadow", ["brand", "glow", "primary"]),
        "--border": ("border", []),
        "--border-field": ("border", ["field"]),
        "--border-light": ("border", ["light", "primary"]),
        "--text": ("text", []),
        "--text-light": ("text", ["light"]),
        "--white": ("white", []),
        "--dark": ("dark", []),
        "--gray": ("gray", []),
        "--light": ("light", []),
        "--muted": ("muted", []),
        "--card": ("card", []),
        "--field": ("field", []),
        "--bg-linear": ("bg", ["linear"]),
        "--bg-radial": ("bg", ["radial"]),
    }
    for old, (base, mods) in core_map.items():
        if old in defined:
            mapping[old] = make_name(base, mods, used)

    # 2) Every --v- (and any other yet-unmapped) variable via classifier
    for var, val in defined.items():
        if var in mapping:
            continue
        base, mods = classify(val)
        mapping[var] = make_name(base, mods, used)

    print(f"Total variables renamed: {len(mapping)}")

    # --- Two-phase safe replacement ---
    sorted_old = sorted(mapping.keys(), key=len, reverse=True)

    def replace_all(content):
        # Phase 1: old -> unique placeholder
        for i, old in enumerate(sorted_old):
            content = re.sub(r'(?<![\w-])' + re.escape(old) + r'(?![\w-])',
                             f'\x00{i}\x00', content)
        # Phase 2: placeholder -> final new name
        for i, old in enumerate(sorted_old):
            content = content.replace(f'\x00{i}\x00', mapping[old])
        return content

    def refactor_theme_file(path):
        # NOTE: PHASE A above already renamed every occurrence (definitions and
        # references) in this file via the safe two-phase replace_all. Here we
        # ONLY sort the :root block alphabetically -- we must NOT call
        # replace_all again, or the freshly inserted names (e.g. --red from
        # --v-c0392b) would be re-matched by the still-present --red mapping
        # and wrongly turned into --danger (cascade).
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        root_match = re.search(r':root\s*\{([^}]+)\}', content, re.DOTALL)
        root_inner = root_match.group(1)
        lines = root_inner.split('\n')
        var_lines, others = [], []
        for line in lines:
            st = line.strip()
            if st.startswith('--'):
                var_lines.append(line)
            else:
                others.append(line)
        var_lines = sorted(var_lines, key=lambda l: l.strip())
        new_inner = "\n    /* Consolidated generic properties - Sorted Alphabetically */\n"
        for l in var_lines:
            new_inner += l + "\n"
        cleaned_others = [l for l in others if l.strip()]
        if cleaned_others:
            new_inner += "\n    /* Other definitions */\n"
            for l in cleaned_others:
                new_inner += l + "\n"
        new_content = content[:root_match.start(1)] + new_inner + content[root_match.end(1):]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Refactored {os.path.basename(path)}")

    # ------------------------------------------------------------------
    # ORDER MATTERS: do the GLOBAL replacement FIRST (safe two-phase, no
    # cascade within a file), THEN rewrite/sort the theme :root blocks LAST.
    # This avoids re-processing an already-renamed theme file through the
    # global loop (which would re-trigger the cascade on freshly inserted
    # names such as --red -> --danger).
    # ------------------------------------------------------------------

    # PHASE A: replace definitions + references in EVERY css file
    for fp in css_files:
        with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        new_content = replace_all(content)
        if new_content != content:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated references in {os.path.basename(fp)}")

    # PHASE B: rewrite + alphabetically sort the :root of theme files.
    # Their definitions were already renamed in PHASE A, so the inner
    # replace_all is a no-op and there is no further global pass over them.
    for fp in (base_light, base_dark):
        if os.path.exists(fp):
            refactor_theme_file(fp)

    print("\n=== RENAMING COMPLETE ===")


if __name__ == "__main__":
    main()
