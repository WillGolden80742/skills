---
name: refatorar-css-variaveis
description: Refatora um diretório ou arquivo CSS para usar variáveis CSS no bloco :root (com suporte a layouts, fallbacks e recursão de parênteses), centralizando tudo em base.css.
triggers: ["css-root", "css root", "refatorar css", "variaveis css", "css variables", "root css", "var css", "custom properties", "css custom properties", "refatorar arquivo css", "otimizar css", "repeticao css", "valores repetidos css", "organizar css", "padronizar css", "css :root", "bloco root", "declarar variaveis", "criar variaveis css", "substituir valores css", "css refatorado", "melhorar css", "limpar css", "css pendente", "refatoracao css", "extrair variaveis", "codigo css limpo", "css maintainable", "css manutencao", "css consistente", "automatizar css", "centralizar css", "centralizar root", "centralizar variaveis"]
---

## What I do
Executa um script Python extremamente robusto que:
1. **Analisa e extrai variáveis base**: Lê e indexa as variáveis já existentes no `:root` de um arquivo centralizador (`base.css`).
2. **Substituição inteligente de fallbacks**: Identifica fallbacks hardcoded em funções `var()`, como `var(--light-gray, #f5f5f5)`, e os substitui por variáveis aninhadas `var(--light-gray, var(--bg-light))`, usando um parser recursivo de parênteses balanceados para evitar quebras em funções complexas (ex: `linear-gradient`).
3. **Conversão de declarações estáticas**: Converte declarações estáticas de qualquer tipo (incluindo cores, tamanhos, e regras de layout como `display: flex`, `cursor: pointer`, etc.) em variáveis do `:root`.
4. **Reuso de variáveis**: Reutiliza variáveis base existentes que possuam o mesmo valor antes de gerar novas variáveis, garantindo um código altamente otimizado e DRY.
5. **Centralização e in-place update**: Atualiza todos os arquivos CSS informados e centraliza todas as variáveis (novas e existentes) no `:root` do arquivo `base.css` de forma totalmente automatizada.

## Usage
O skill usa o comando:
```bash
python "~/.config/opencode/skills/refatorar-css-variaveis/cssRoot.py"
```

## Input
Quando executado, o script solicitará o caminho do diretório ou do arquivo original, aplicando as regras de extração recursiva e centralização com suporte completo a parênteses balanceados.
