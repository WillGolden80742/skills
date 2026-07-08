---
name: comit
description: Cria commits Git com historico timestampado em commits/
triggers: ["comit", "comitar", "commit", "commitar", "git commit", "fazer commit", "criar commit", "enviar commit", "push", "git push", "commit force", "force push", "git force", "commit historico", "salvar alteracoes", "registrar alteracao", "versionar codigo", "git add", "git message", "mensagem commit", "commit arquivos", "commit projeto", "commits pasta", "timestamp commit", "registro commit", "git pull", "rebase", "git rebase", "commit com mensagem", "--force-with-lease", "git salvar", "knowledge", "grafo", "graphify", "grafo de codigo", "registrar", "versionar", "subir", "enviar", "mandar", "commitar agora", "fazer push", "subir alteracoes", "salvar commit", "registrar commit", "criar versao", "atualizar repositorio", "enviar codigo", "git add commit", "git add commit push", "commit tudo", "commitar tudo", "feito", "pronto commit", "pode commit", "comitar", "comitando", "commitando", "registrar mudancas", "salvar mudancas", "enviar mudancas", "subir mudancas", "commit final", "commit rapido"]
---

## What I do
Executa commits Git com as seguintes caracteristicas:
1. **SEMPRE** mostra o diff e pergunta "Deseja commitar?" antes de prosseguir — **NUNCA** comita sem confirmacao
2. Executa o commit Git
3. Cria arquivo de historico do commit em `commits/commit-[id]-[timestamp].md` (com hash correto)
4. Commita o arquivo de historico
5. Atualiza README.md com a estrutura atual do projeto (arvore de diretorios, tabelas de classes)
6. **Atualiza a base de dados graphify-out** (`graphify-out/`) com `graphify . --update`
7. Faz pull --rebase e push (ou --force-with-lease com flag --force)

## Parameters
- `message`: Mensagem do commit
- `files`: Arquivos a serem comitados (separados por espaco, default: todos)
- `project_path`: Caminho base do projeto (default: workspace root)
- `yes`: Pular confirmacao interativa (default: false) — **SÓ use se o usuario pedir explicitamente**
- `force`: Usa --force-with-lease no push (default: false)

## Usage

**Nota:** Use `python3` no lugar de `python` se o `python` nao estiver disponivel.

### Regra de Ouro
**NUNCA comite sem antes mostrar o diff e perguntar ao usuario se ele testou e deseja aprovar o commit.** O comportamento padrao é SEMPRE usar o modo interativo (sem `--yes`).

### Commit padrao com confirmacao (RECOMENDADO):
```
python3 "~/.config/opencode/skills/comit/comit.py" --message "feat: nova funcionalidade"
```

### Commit sem confirmacao interativa (SOMENTE se usuario pedir):
```
python3 "~/.config/opencode/skills/comit/comit.py" --yes --message "fix: corrigido bug"
```

### Commit com arquivos especificos:
```
python3 "~/.config/opencode/skills/comit/comit.py" --message "fix: corrigido bug" --files "src/index.php css/style.css"
```

### Commit forcado (--force-with-lease):
```
python3 "~/.config/opencode/skills/comit/comit.py" --message "fix: reescrevendo historico" --force
```

### Commit em projeto especifico:
```
python3 "~/.config/opencode/skills/comit/comit.py" --message "docs: atualizado documentacao" --project "C:\projeto"
```

## Fluxo de confirmacao
1. Mostrar `git diff --stat` para o usuario ver quais arquivos mudaram
2. Perguntar: "Deseja commitar essas alteracoes?"
3. Se sim, executar o comando SEM `--yes` para que o script tbm peca confirmacao
4. Reportar o hash do commit e status do push

## Formato do Arquivo de Commit
`commits/yyyy-mm/dd/commit-[id]-[yyyy-mm-dd-hh-mm-ss].md`
*(localizado em `commits/` na raiz do projeto)*
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

## Atualizacao da Base Graphify-Out
Apos cada commit bem-sucedido, a base de dados do graphify e atualizada:
1. Executa `graphify . --update` no diretorio do projeto
2. Usa a API key configurada em `graphify-out/.graphify_config`
3. Prioriza modelos free: openseek-v4-free > gpt-4o-mini-free > llama-4-scout-free
4. Atualiza os arquivos em `graphify-out/`:
   - `graph.json` - grafo atualizado com novas entidades
   - `graph.html` - visualizacao interativa
   - `GRAPH_REPORT.md` - relatorio de comunidades
   - Cache de extracão semantica

## Notes
- Cada commit gera um ID unico baseado no hash Git
- Requer Git instalado no sistema
- O README.md reflete sempre a estrutura atual do projeto
- A base graphify-out mantem o historico de conhecimento do codigo
