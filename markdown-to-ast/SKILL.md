---
name: markdown-to-ast
description: "Converte todos os arquivos .md do projeto em AST nodes no grafo do graphify. Cada .md gera um .json correspondente no mesmo diretório."
triggers: ["markdown ast", "md ast", "extrair ast markdown", "parse markdown ast", "markdown structure", "markdown parser"]
---

## What I do
Converte arquivos markdown (.md) em estrutura AST (.json) no mesmo diretório.
Cada arquivo .md gera um .json com nodes e edges representando a estrutura do documento.

## Output
Cada .md gera um .json correspondente:
- `SKILL.md` → `SKILL.json`
- `README.MD` → `README.json`
- `dir/subdir/file.md` → `dir/subdir/file.json`

O JSON contém:
- **source**: caminho do .md original
- **generated_at**: timestamp da geração
- **nodes**: headings, code blocks, links, images, list items
- **edges**: relações hierárquicas entre nodes

## Uso
```bash
# Processar diretório inteiro
python3 markdown-to-ast/md_to_ast.py --path .

# Processar skill específica
python3 markdown-to-ast/md_to_ast.py --path criar-novo-skill/SKILL.md

# Modo verbose
python3 markdown-to-ast/md_to_ast.py --path . --verbose

# Dry-run (sem salvar)
python3 markdown-to-ast/md_to_ast.py --path . --dry-run
```

## Exemplo de output
```json
{
  "source": "/path/to/SKILL.md",
  "generated_at": "2026-07-08T21:11:12",
  "nodes": [
    {"id": "md_SKILL_h1_0", "label": "Titulo", "type": "heading", "level": 1, ...},
    {"id": "md_SKILL_code_1", "label": "Code: python", "type": "code_block", ...}
  ],
  "edges": [
    {"from": "md_SKILL_h1_0", "to": "md_SKILL_code_1", "relation": "contains"}
  ]
}
```

## Integracao
Usado automaticamente por `criar-novo-skill` e `editar-skill` ao criar/editar skills.
