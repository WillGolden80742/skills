---
name: comit
description: Cria commits Git com historico timestampado em commits/
triggers: ["comit", "commit", "git commit"]
---

## What I do
Executa commits Git com as seguintes caracteristicas:
1. Cria arquivo de historico do commit em `commits/commit-[id]-[timestamp].md`
2. Atualiza README.md com o historico de commits
3. Executa o commit Git

## Parameters
- `message`: Mensagem do commit
- `files`: Arquivos a serem comitados (separados por espaco, default: todos)
- `project_path`: Caminho base do projeto (default: workspace root)

## Usage

### Commit padrao (todos os arquivos):
```
python "~/.config/opencode/skills/comit/comit.py" --message "feat: nova funcionalidade"
```

### Commit com arquivos especificos:
```
python "~/.config/opencode/skills/comit/comit.py" --message "fix: corrigido bug" --files "src/index.php css/style.css"
```

### Commit em projeto especifico:
```
python "~/.config/opencode/skills/comit/comit.py" --message "docs: atualizado documentacao" --project "C:\projeto"
```

## Formato do Arquivo de Commit
`commits/commit-[id]-[dd-mm-yyyy-hh-mm-ss].md`
```
# Commit [id] - [dd/mm/yyyy hh:mm:ss]

## Mensagem
[mensagem do commit]

## Arquivos
[lista de arquivos comitados]

## Hash
[hash do commit Git]
```

## Atualizacao do README.md
A cada commit, o README.md e atualizado com:
- Secao "## Ultimas Alteracoes" contendo a mensagem do commit
- Conteudo dos arquivos alterados (exceto arquivos em commits/)
- Timestamp da alteracao

## Notes
- Cada commit gera um ID unico baseado no hash Git
- Requer Git instalado no sistema
- O README.md mostra sempre as ultimas alteracoes
