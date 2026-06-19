---
name: capturar-screenshot-paginas
description: Captura screenshots de paginas web usando Playwright, com suporte a servidor local
triggers: ["printscreen", "screenshot", "capturar tela", "web print", "print tela", "tirar print", "capturar pagina", "screenshot web", "foto site", "captura site", "screenshot full page", "full page screenshot", "playwright screenshot", "print navegador", "capturar url", "imagem site", "thumbnail site", "preview site", "captura tela inteira", "screenshot desktop", "screenshot mobile", "print responsivo", "screenshot viewport", "capturar webapp", "tela site", "salvar imagem site", "screenshot png", "captura servidor local", "with server screenshot", "networkidle screenshot"]
---

# Web PrintScreen

Captura screenshots de paginas web usando Playwright, com suporte opcional a servidor local.

## Stack

Python + Playwright

## Scripts Auxiliares

- `scripts/with_server.py` (do skill webapp-testing) - Gerencia ciclo de vida do servidor

## Passos

1. Se for pagina estatica, va direto para o passo 3
2. Se for webapp com servidor, use `with_server.py` para subir o servidor
3. Escreva script Python com Playwright para:
   - Navegar ate a pagina
   - Aguardar `networkidle`
   - Aguardar seletores especificos se necessario
   - Tirar screenshot com `page.screenshot()`
4. Execute o script

## Template

```python
import sys, time, os
from playwright.sync_api import sync_playwright

URL = "http://localhost:PORTA"
OUT = "caminho/para/screenshot.png"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1280, "height": 900})
    page = ctx.new_page()
    page.goto(URL)
    page.wait_for_load_state("networkidle")
    time.sleep(1)
    page.screenshot(path=OUT, full_page=True)
    browser.close()
```

## Com with_server.py

```bash
python "CAMINHO/skills/webapp-testing/scripts/with_server.py" \
  --server "comando servidor" --port PORTA \
  -- python script.py
```

## Dicas

- Use `full_page=True` para pagina completa
- Use `viewport` para controlar resolucao
- Espere seletores com `wait_for_selector` antes do screenshot
- Evite `time.sleep` fixo; prefira `wait_for_load_state` ou `wait_for_selector`
