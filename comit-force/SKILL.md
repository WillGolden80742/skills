---
name: comit-force
description: Cria commits Git com force-with-lease, pull, push e historico timestampado em commits/
triggers: ["comit-force", "commit-force", "force commit", "comit forcado"]
---

## What I do
Executa commits Git forçados com as seguintes caracteristicas:
1. Executa o commit Git
2. Cria arquivo de historico do commit em `commits/commit-[id]-[timestamp].md` (com hash correto)
3. Commita o arquivo de historico
4. Atualiza README.md com o historico de commits
5. Faz pull --rebase antes do push
6. Faz push forcado com --force-with-lease

## Parameters
- `message`: Mensagem do commit
- `files`: Arquivos a serem comitados (separados por espaco, default: todos)
- `project_path`: Caminho base do projeto (default: workspace root)

## Usage

### Commit forcado (todos os arquivos):
```
python "~/.config/opencode/skills/comit-force/comit-force.py" --message "fix: reescrevendo historico"
```

### Commit forcado com arquivos especificos:
```
python "~/.config/opencode/skills/comit-force/comit-force.py" --message "reset: corrigido bug" --files "src/index.php"
```

### Commit em projeto especifico:
```
python "~/.config/opencode/skills/comit-force/comit-force.py" --message "rebase: reescrever tudo" --project "C:\projeto"
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
- Usa --force-with-lease para seguranca (nao sobrescreve remoto se houver atualizacoes)
- Cada commit gera um ID unico baseado no hash Git
- Requer Git instalado no sistema
- O README.md mostra sempre as ultimas alteracoes
- AVISO: Use apenas quando necessario reescrever historico Git
