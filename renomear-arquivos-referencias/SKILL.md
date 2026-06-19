---
name: renomear-arquivos-referencias
description: Renomeia um arquivo e atualiza automaticamente todas as referências em arquivos do projeto (.php, .js, .css, etc.)
triggers: ["renomear", "rename", "renomeia", "file rename", "rename file", "renomear arquivo", "mudar nome", "trocar nome", "renomear classe", "refatorar nome", "alterar nome", "rename class", "mudar nome arquivo", "renomear pasta", "renomear diretorio", "atualizar referencias", "rename references", "mudar nome classe", "renomear projeto", "rename project", "mover arquivo", "file renaming", "renomear php", "rename php file", "renomear js", "rename js file", "alterar nome arquivo", "mudar referencia", "renomear com replace", "rename all", "atualizar imports", "atualizar includes", "refatorar renomear"]
---

## What I do
Executa um script Python que:
1. Renomeia o arquivo especificado
2. Atualiza o nome da classe dentro do próprio arquivo renomeado
3. Busca e atualiza todas as referências ao arquivo em todos os arquivos do projeto

## Parameters
- `original_name`: Nome original do arquivo (ex: PointsController.php)
- `new_name`: Novo nome para o arquivo (ex: EventsController.php)
- `project_path`: Caminho base do projeto
- `update_all`: "true" para todos os tipos de arquivo, "false" para apenas .php

## Usage
O skill usa o comando:
```
python "~/.config/opencode/skills/file-rename/rename.py" "nome_original" "nome_novo" "caminho_projeto" "update_all"
```

## Notes
O script automaticamente desconsidera a extensão .php ao buscar referências (nome da classe). Também atualiza a classe dentro do próprio arquivo renomeado.