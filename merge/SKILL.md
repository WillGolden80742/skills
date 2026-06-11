---
name: merge
description: Mescla todos os arquivos de um diretório em um único arquivo de saída (respeitando regras de exclusão de um arquivo .mergeignore).
triggers: ["merge", "mesclar arquivos", "mesclar pasta", "merge files", "merge directory"]
---

## What I do
Executa um script Python que:
1. Varre recursivamente um diretório informado (ou o diretório atual do script por padrão).
2. Carrega padrões de arquivos a serem ignorados a partir de um arquivo `.mergeignore` (caso exista).
3. Concatena o conteúdo de todos os arquivos não ignorados em um único arquivo chamado `merged_output.txt`.

## Usage
O skill usa o comando:
```bash
python "~/.config/opencode/skills/merge/merge.py" "caminho_diretorio"
```

## Parameters
- `caminho_diretorio`: (Opcional) O diretório cujos arquivos devem ser mesclados. Se omitido, usa o diretório do próprio script.
