---
name: css-root
description: Refatora um arquivo CSS comum para usar variáveis CSS no bloco :root, criando variáveis para valores que se repetem mais de 2 vezes.
triggers: ["css-root", "css root", "refatorar css", "variaveis css", "css variables", "root css", "var css", "custom properties", "css custom properties", "refatorar arquivo css", "otimizar css", "repeticao css", "valores repetidos css", "organizar css", "padronizar css", "css :root", "bloco root", "declarar variaveis", "criar variaveis css", "substituir valores css", "css refatorado", "melhorar css", "limpar css", "css pendente", "refatoracao css", "extrair variaveis", "codigo css limpo", "css maintainable", "css manutencao", "css consistente", "automatizar css"]
---

## What I do
Executa um script Python que:
1. Analisa um arquivo CSS para identificar todos os valores repetidos mais de 2 vezes.
2. Cria variáveis CSS correspondentes no bloco `:root`.
3. Substitui os valores originais pela função `var()`.
4. Gera um novo arquivo com o sufixo `_refatorado_generico.css`.

## Usage
O skill usa o comando:
```bash
python "~/.config/opencode/skills/css-root/cssRoot.py"
```

## Input
Quando executado, o script solicitará o caminho completo do arquivo CSS original:
```
Digite o caminho completo do arquivo CSS original: C:\projeto\style.css
```
O arquivo refatorado será salvo como: `C:\projeto\style_refatorado_generico.css`.
