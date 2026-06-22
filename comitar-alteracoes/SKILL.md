---
name: comitar-alteracoes
description: Cria commits Git com historico timestampado em commits/
triggers: ["comit", "comitar", "commit", "commitar", "git commit", "fazer commit", "criar commit", "enviar commit", "push", "git push", "commit force", "force push", "git force", "commit historico", "salvar alteracoes", "registrar alteracao", "versionar codigo", "git add", "git message", "mensagem commit", "commit arquivos", "commit projeto", "commits pasta", "timestamp commit", "registro commit", "git pull", "rebase", "git rebase", "commit com mensagem", "--force-with-lease", "git salvar"]
---

## What I do
Executa commits Git com as seguintes caracteristicas:
1. Mostra o diff completo das alteracoes e solicita confirmacao antes de prosseguir (ou usa --yes para pular)
2. Executa o commit Git
3. Cria arquivo de historico do commit em `commits/commit-[id]-[timestamp].md` (com hash correto)
4. Commita o arquivo de historico
5. Atualiza README.md com a estrutura atual do projeto (arvore de diretorios, tabelas de classes)
6. Faz pull --rebase e push (ou --force-with-lease com flag --force)

## Parameters
- `message`: Mensagem do commit
- `files`: Arquivos a serem comitados (separados por espaco, default: todos)
- `project_path`: Caminho base do projeto (default: workspace root)
- `yes`: Pular confirmacao interativa (default: false)
- `force`: Usa --force-with-lease no push (default: false)

## Usage

**Nota:** Use `python3` no lugar de `python` se o `python` nao estiver disponivel.

### Commit padrao (todos os arquivos):
```
python3 "~/.config/opencode/skills/comitar-alteracoes/comit.py" --yes --message "feat: nova funcionalidade"
```

### Commit sem confirmacao interativa:
```
python3 "~/.config/opencode/skills/comitar-alteracoes/comit.py" --yes --message "fix: corrigido bug"
```

### Commit com arquivos especificos:
```
python3 "~/.config/opencode/skills/comitar-alteracoes/comit.py" --message "fix: corrigido bug" --files "src/index.php css/style.css"
```

### Commit forcado (--force-with-lease):
```
python3 "~/.config/opencode/skills/comitar-alteracoes/comit.py" --message "fix: reescrevendo historico" --force
```

### Commit em projeto especifico:
```
python3 "~/.config/opencode/skills/comitar-alteracoes/comit.py" --message "docs: atualizado documentacao" --project "C:\projeto"
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
A cada commit, o README.md e atualizado automaticamente:
- Arvore de diretorios em `app/` reflete os arquivos reais no disco
- Tabelas de Controllers, Models e Services listam classes encontradas

## Notes
- Cada commit gera um ID unico baseado no hash Git
- Requer Git instalado no sistema
- O README.md reflete sempre a estrutura atual do projeto
