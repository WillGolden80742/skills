---
name: gerar-historico-commits
description: Gera arquivos de historico de commits do Git em commits/yyyy/mm/dd/ com diff completo
triggers: ["historico commits", "gerar historico", "commits pasta", "registro commit", "timestamp commit", "commit historico", "documentar commits", "gerar commits", "criar commits pasta", "commits pasta", "historia commit", "log commits", "git log", "commits documentação", "commits docs", "gerar diff", "diff commits", "registrar historico", "historico git", "git history", "export commits"]
---

## What I do
Gera arquivos de historico de commits do Git usando o script `generate_commit_history.py`.

## Script Location
`~/.config/opencode/skills/gerar-historico-commits/generate_commit_history.py`

## Uso

### Gerar todos os historicos de commits (padrão):
```bash
python3 ~/.config/opencode/skills/gerar-historico-commits/generate_commit_history.py
```

### Gerar com caminhos customizados:
```bash
python3 ~/.config/opencode/skills/gerar-historico-commits/generate_commit_history.py --repo /caminho/do/repo --output /caminho/output
```

### Parâmetros:
- `--repo`: Caminho do repositório Git (default: theme WordPress)
- `--output`: Diretório base para salvar os arquivos (default: `/www/wwwroot/sac.moedadetroka.com.br/commits`)

## O que o script faz:
1. Lista todos os commits do repositorio Git
2. Para cada commit, extrai: mensagem, arquivos mudados, hash, diff completo
3. Cria arquivo em `commits/yyyy/mm/dd/commit-[hash-12chars]-[timestamp].md`
4. **Idempotente**: ignora commits ja documentados (verifica se arquivo existe)

## Formato do Arquivo de Commit
```
commits/yyyy/mm/dd/commit-[hash-12chars]-[yyyy-mm-dd-hh-mm-ss].md
```
```markdown
# Commit [hash-12chars] - dd/mm/yyyy hh:mm:ss

## Mensagem
[mensagem do commit]

## Arquivos
- arquivo1.php
- arquivo2.css

## Hash
[hash completo do commit]

## Diff
[diff completo do commit - pode ser muito longo]
```

## Exemplo
```bash
# Gerar historicos
python3 ~/.config/opencode/skills/gerar-historico-commits/generate_commit_history.py

# Saida esperada:
# === Gerador de Histórico de Commits ===
# Repo: /www/wwwroot/sac.moedadetroka.com.br/wp-content/themes/moedadetroka
# Output: /www/wwwroot/sac.moedadetroka.com.br/commits
#
# Total de commits encontrados: 443
# Processando commit 50/443...
# ...
# === Concluído ===
# Arquivos criados: 0
# Arquivos ignorados (já existem): 443
```

## Notes
- O script detecta automaticamente commits ja documentados
- Diff limitado a 500k caracteres por commit para evitar arquivos gigantes
- Para recuperar/ver commits salvos, use a skill "recuperar-commits-salvos"
