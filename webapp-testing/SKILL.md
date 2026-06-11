---
name: webapp-testing
description: Toolkit para testar aplicações web locais usando Playwright. Verifica funcionalidade frontend, debug UI, screenshots.
triggers: ["testar", "testing", "playwright", "webapp", "automacao", "debug"]
---

# Skill Webapp Testing

## Scripts Auxiliares

- `scripts/with_server.py` - Gerencia ciclo de vida do servidor

**Sempre rode scripts com `--help` primeiro.**

## Árvore de Decisão

```
Usuário → É HTML estático?
    ├─ Sim → Leia HTML para identificar seletores
    │         └─ Sucesso → Escreva script Playwright
    │
    └─ Não (webapp dinâmico) → Servidor já está rodando?
        ├─ Não → Use: python scripts/with_server.py --help
        │
        └─ Sim → Reconnaissance-then-action:
            1. Navegue e espere networkidle
            2. Tire screenshot ou inspecione DOM
            3. Identifique seletores
            4. Execute ações
```

## Exemplo: with_server.py

**Servidor único:**
```bash
python scripts/with_server.py --server "npm run dev" --port 5173 -- python automacao.py
```

**Múltiplos servidores:**
```bash
python scripts/with_server.py \
  --server "cd backend && python server.py" --port 3000 \
  --server "cd frontend && npm run dev" --port 5173 \
  -- python automacao.py
```

## Script de Automação

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:5173')
    page.wait_for_load_state('networkidle')
    # ... sua lógica
    browser.close()
```

## Armadilha Comum

❌ **Não** inspecione DOM antes de esperar `networkidle`
✅ **Faça** `page.wait_for_load_state('networkidle')` antes

## Melhores Práticas

- Use seletores descritivos: `text=`, `role=`, CSS, IDs
- Adicione waits apropriados
- Sempre feche o browser
- Use `sync_playwright()`
