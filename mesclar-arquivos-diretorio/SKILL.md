---
name: mesclar-arquivos-diretorio
description: Mescla todos os arquivos de um diretório em um único arquivo de saída (respeitando regras de exclusão de um arquivo .mergeignore).
triggers: ["merge", "mesclar arquivos", "mesclar pasta", "merge files", "merge directory", "juntar arquivos", "unir arquivos", "combinar arquivos", "concatenar arquivos", "merge hidden", "merge ignore", "mergeignore", "arquivo unico", "unir diretorio", "merged output", "concatenar diretorio", "combinar conteudo", "merge codebase", "juncao arquivos", "merge tudo", "merge completo", "unir tudo", "mesclar tudo", "merge pasta", "merge projeto", "mesclar codigo", "combinar pasta", "concatenar pasta", "merge output", "merge script", "merge tool"]
---

## What I do
Executa um script Python que:
1. Primeiro, gera e exibe a árvore de diretório completa usando `dir_tree.py` (sem ignorar nada) para mostrar toda a estrutura do projeto.
2. Carrega padrões de arquivos a serem ignorados a partir de um arquivo `.mergeignore` (caso exista).
3. Concatena o conteúdo de todos os arquivos não ignorados em um único arquivo chamado `merged_output.txt`.

A árvore exibe tudo (sem filtro). O merge usa o `.mergeignore` para decidir o que excluir do arquivo final.

## Usage
O skill usa o comando:
```bash
python "~/.config/opencode/skills/mesclar-arquivos-diretorio/merge.py" "caminho_diretorio"
```

## Parameters
- `caminho_diretorio`: (Opcional) O diretório cujos arquivos devem ser mesclados. Se omitido, usa o diretório do próprio script.
