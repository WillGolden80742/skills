---
name: renomear-variaveis-css-genericas
description: Renomeia variaveis CSS customizadas (custom properties) de um diretorio de folhas de estilo para nomes GENERICOS (primary/secondary/tertiary, shadow-big-bigger, purple-dark-light-gray, etc.), usando algoritmo de deteccao de cores predominantes, classificacao por valor (cor/gradiente/sombra/borda/utilitario) e modificadores ordenados alfabeticamente. Substitui em cascata com placeholder de duas fases para evitar bug de renomeacao em cascata, e ordena o bloco :root alfabeticamente.
triggers: ["renomear variaveis css", "renomear variaveis genericas", "renomear custom properties", "css variaveis genericas", "renomear --v- css", "generic css variable names", "renomear variaveis do tema", "primary secondary tertiary css", "renomear tokens de cor css", "refatorar nomes de variaveis css", "css design tokens rename", "renomear var css para nomes genericos"]
---

## What I do
Transforma variaveis CSS (`--algo`) em nomes **genericose semanticos**, aplicando a logica:

1. **Detecta as 3 cores predominantes** do tema somando o uso (`var(--x)`) das familias
   `brand` (inclui `-hover/-light/-soft`), `accent`, `gold`, `green`, `red` em todos os `.css`.
   - Familia 1 -> `--primary`
   - Familia 2 -> `--secondary`
   - Familia 3 -> `--tertiary`
   - `green` -> `--success`, `red` -> `--danger` (cores semanticas).

2. **Classifica CADA variavel pelo valor** e gera um nome generico:
   - Cor simples -> familia de matiz (`red`, `blue`, `green`, `purple`, `gray`, `black`, `white`, `pink`, `orange`, `yellow`, `teal`) + modificadores (`dark`/`light`/`muted`/`soft`).
   - Gradiente -> `gradient-linear-<familias>` / `gradient-radial-<familias>`.
   - Sombra -> `shadow-<tamanho>-<familia>` (box-shadow e drop-shadow).
   - Borda -> `border-<estilo>-<tamanho>-<familia>`.
   - Utilitarios -> `display-`, `position-`, `align-`, `filter-`, `transform-`,
     `transition-`, `animation-`, `calc-`, `grid-`, `cursor-`, `visibility-`,
     `object-`, `whitespace-`, `font-`, `env-`.

3. **Regra de nomenclatura (ate 4 palavras):**
   - A PRIMEIRA palavra tem o MAIOR PESO (tipo/cor).
   - As demais palavras (modificadores) sao ORDENADAS ALFABETICAMENTE.
   - Exemplos: `small-bigger-medium-small` | `purple-dark-light-gray` | `shadow-big-bigger-giant`.
   - Colisoes recebem sufixo `-2`, `-3`, ... para garantir nomes unicos.

4. **Substitui em cascata com PLACEHOLDER DE DUAS FASES** (fase 1: nome antigo ->
   placeholder unico; fase 2: placeholder -> nome novo). Isso evita o bug onde um
   nome novo (`--red`) e re-referenciado por outra chave antiga (`--red` -> `--danger`).

5. **Ordena o bloco `:root` alfabeticamente** em `base-light.css` / `base-dark.css`.

6. **Propaga as novas referencias** em TODOS os `.css` do diretorio.

## Usage
O script recebe o diretorio das folhas de estilo (ou usa o diretorio atual):
```bash
python "~/.config/opencode/skills/renomear-variaveis-css-genericas/rename_css_vars_genericas.py" <diretorio-das-folhas-css>
```

## Input
- Um diretorio contendo os `.css` do tema (ex.: `app/assets/stylesheets`).
- Espera encontrar `base-light.css` e `base-dark.css` (arquivos de tema com `:root`).
- Quaisquer `:root` (ex.: `base.css` com bloco consolidado de `--v-*`) tambem sao
  renomeados e ordenados.

## Caveats / licoes aprendidas
- **NUNCA rode o replace duas vezes sobre o mesmo arquivo ja renomeado** — causa
  cascata (ex.: `--v-c0392b` vira `--red`, e o mapeamento `--red` -> `--danger`
  re-transforma aquele `--red` em `--danger`, gerando definicao duplicada). Por isso
  o script faz o replace GLOBAL primeiro (duas fases) e so DEPOIS reescreve/ordena o
  `:root`, sem chamar replace de novo.
- Referencias `var(--x)` que ja eram "orfas" (ndefinidas) no projeto original permanecem
  orfas apos o rename — o script nao quebra nada que ja nao estivesse quebrado.
- O script e **idempotente o suficiente para um unico pass** sobre arquivos originais;
  rodar duas vezes seguidas sobre a saida pode reclassificar nomes ja genericos.

## Comando
```bash
python "~/.config/opencode/skills/renomear-variaveis-css-genericas/rename_css_vars_genericas.py" "<diretorio>"
```
