---
name: reverter-css-variaveis
description: Reverte um arquivo CSS refatorado com variáveis CSS (:root) de volta para valores diretos.
triggers: ["css-root-reverse", "css root reverse", "reverter css", "reverter variaveis css", "css variables reverse", "desfazer root", "remover var css", "inline css", "css direto", "valores literais css", "reverter refatoracao", "desfazer refatoracao", "css original", "voltar css", "extrair valores css", "substituir var css", "css reverso", "reverter arquivo css", "desfazer variaveis", "remover :root", "tirar variaveis css", "css revertido", "backup css", "css desrefatorado", "reverter estilo", "css inline", "css sem variaveis", "excluir variaveis", "voltar ao normal css", "css original back", "reverse refactoring"]
---

## What I do
Executa um script Python que:
1. Extrai as variáveis declaradas no bloco `:root`.
2. Remove o bloco `:root` do arquivo CSS.
3. Substitui todas as chamadas `var(--nome)` pelos seus valores literais diretos.
4. Gera um novo arquivo com o sufixo `_revertido.css`.

## Usage
O skill usa o comando:
```bash
python "~/.config/opencode/skills/reverter-css-variaveis/cssRootReverse.py"
```

## Input
Quando executado, o script solicitará o caminho completo do arquivo CSS refatorado:
```
Digite o caminho completo do arquivo CSS refatorado (ex: nome_refatorado_tipado.css): C:\projeto\style_refatorado_generico.css
```
O arquivo revertido será salvo como: `C:\projeto\style_revertido.css`.
