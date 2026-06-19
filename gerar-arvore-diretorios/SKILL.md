---
name: gerar-arvore-diretorios
description: Cria uma representação em Markdown (.md) da árvore de diretórios de um projeto, incluindo subdiretórios recursivamente.
triggers: ["arvore diretorio", "arvore de diretorio", "directory tree", "tree md", "arvore md", "gerar arvore", "gere arvore", "gerar tree", "gere tree", "mostrar arvore", "mostra arvore", "exibir arvore", "exibe arvore", "criar arvore", "cria arvore", "crie arvore", "make tree", "generate tree", "show tree", "estrutura diretorios", "estrutura pastas", "folder tree", "tree view", "diretorio arvore", "lista pastas", "lista diretorios", "ver estrutura", "exibir estrutura", "arvore arquivos", "diretorio estrutura", "mapear pastas", "explorar diretorio", "hierarquia pastas", "arvore projeto"]
---

## What I do
Gera uma árvore de diretórios formatada em Markdown (com caracteres Unicode ├── └──) a partir de um caminho informado.

## Usage
```bash
python "~/.config/opencode/skills/gerar-arvore-diretorios/dir_tree.py" [caminho] [arquivo_saida]
```

- `caminho`: (opcional) Diretório raiz. Padrão: diretório atual.
- `arquivo_saida`: (opcional) Arquivo .md onde salvar a árvore. Se omitido, imprime no terminal.

### Exemplos

Gerar árvore do diretório atual:
```bash
python "~/.config/opencode/skills/gerar-arvore-diretorios/dir_tree.py"
```

Gerar árvore de um diretório específico:
```bash
python "~/.config/opencode/skills/gerar-arvore-diretorios/dir_tree.py" C:/MeuProjeto
```

Gerar e salvar em arquivo .md:
```bash
python "~/.config/opencode/skills/gerar-arvore-diretorios/dir_tree.py" C:/MeuProjeto arvore.md
```

## Observação
A árvore exibe diretórios ignorados (`.git`, `node_modules`, `vendor`, `__pycache__`, etc.) mas **não** desce recursivamente neles — mostra apenas o nome, sem o conteúdo interno. O filtro para o merge é feito pelo `.mergeignore` no skill de merge.

## Exemplo de saída
```
# Árvore de Diretório: `meu-projeto`

```
meu-projeto/
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   └── Footer.js
│   ├── pages/
│   │   └── index.js
│   └── styles/
│       └── main.css
├── public/
│   └── index.html
└── package.json
```
```
