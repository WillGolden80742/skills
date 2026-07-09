---
name: comitar-alteracoes
description: Cria commits Git com historico timestampado em commits/
triggers: ["comit", "comitar", "commit", "commitar", "git commit", "fazer commit", "criar commit", "enviar commit", "push", "git push", "commit force", "force push", "git force", "salvar alteracoes", "registrar alteracao", "versionar codigo", "git add", "git message", "mensagem commit", "commit arquivos", "commit projeto", "git pull", "rebase", "git rebase", "commit com mensagem", "--force-with-lease", "git salvar", "knowledge", "grafo", "graphify", "grafo de codigo", "registrar", "versionar", "subir", "enviar", "mandar", "commitar agora", "fazer push", "subir alteracoes", "salvar commit", "registrar commit", "criar versao", "atualizar repositorio", "enviar codigo", "git add commit", "git add commit push", "commit tudo", "commitar tudo", "feito", "pronto commit", "pode commit", "comitar", "comitando", "commitando", "registrar mudancas", "salvar mudancas", "enviar mudancas", "subir mudancas", "commit final", "commit rapido"]
---

## What I do
Executa commits Git com as seguintes caracteristicas:
1. **SEMPRE** mostra o diff e pergunta "Deseja commitar?" antes de prosseguir — **NUNCA** comita sem confirmacao
2. Executa o commit Git
3. **Gera AST JSON para todos os .md modificados** via `markdown-to-ast`
4. Executa `generate_commit_history.py` para gerar arquivo de historico em `commits/yyyy/mm/dd/`
5. Commita o arquivo de historico
6. **Atualiza a base de dados graphify-out** com `graphify update`
7. Faz pull --rebase e push (ou --force-with-lease com flag --force)

## Parameters
- `message`: Mensagem do commit
- `files`: Arquivos a serem comitados (separados por espaco, default: todos)
- `project_path`: Caminho base do projeto (default: workspace root)
- `yes`: Pular confirmacao interativa (default: false) — **SO use se o usuario pedir explicitamente**
- `force`: Usa --force-with-lease no push (default: false)

## Usage

### Commit padrao com confirmacao (RECOMENDADO):
```
python3 ~/.config/opencode/skills/comitar-alteracoes/commit.py --message "feat: nova funcionalidade"
```

### Commit sem confirmacao interativa (SOMENTE se usuario pedir):
```
python3 ~/.config/opencode/skills/comitar-alteracoes/commit.py --yes --message "fix: corrigido bug"
```

### Commit com arquivos especificos:
```
python3 ~/.config/opencode/skills/comitar-alteracoes/commit.py --message "fix: corrigido bug" --files "src/index.php css/style.css"
```

### Commit forcado (--force-with-lease):
```
python3 ~/.config/opencode/skills/comitar-alteracoes/commit.py --message "fix: reescrevendo historico" --force
```

### Commit em projeto especifico:
```
python3 ~/.config/opencode/skills/comitar-alteracoes/commit.py --message "docs: atualizado documentacao" --project "/caminho/do/projeto"
```

## Fluxo de confirmacao
1. Mostrar `git diff --stat` para o usuario ver quais arquivos mudaram
2. Perguntar: "Deseja commitar essas alteracoes?"
3. Se sim, executar o commit
4. Executar `generate_commit_history.py` para gerar o arquivo de historico
5. Commitar o arquivo de historico
6. Reportar o hash do commit e status do push

## Script generate_commit_history.py

Localizado em `~/.config/opencode/skills/gerar-historico-commits/generate_commit_history.py`

Uso:
```bash
python3 ~/.config/opencode/skills/gerar-historico-commits/generate_commit_history.py --repo /caminho/do/repo --output /caminho/output
```

## Skills Relacionadas
- **gerar-historico-commits**: Skill dedicada para gerar/exportar historico de commits
- **recuperar-commits-salvos**: Skill para recuperar e exibir commits salvos

## Notes
- O historico de commits fica em `commits/` na raiz do projeto
- Para gerar/exportar todos os commits, use a skill "gerar-historico-commits"
- Para ver commits ja salvos, use a skill "recuperar-commits-salvos"
