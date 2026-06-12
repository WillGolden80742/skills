# Skill: commit-recover

## What I do
Recupera e exibe os comentarios das ultimas alteracoes commitadas na pasta `commits/` de um projeto. Exibe os commits em ordem cronologica reversa (mais recente primeiro), mostrando mensagem, arquivos e hash de cada commit.

## Usage
Execute o skill passando o caminho do projeto:

```bash
python "C:\Users\willi\.config\opencode\skills\commit-recover\commitRecover.py" --project "C:\caminho\do\projeto"
```

Ou usando o parametro `--count` para limitar o numero de commits (default: 5):

```bash
python "C:\Users\willi\.config\opencode\skills\commit-recover\commitRecover.py" --project "C:\caminho\do\projeto" --count 10
```

## Parameters
- `--project`: Caminho base do projeto (obrigatorio)
- `--count`: Numero de commits a recuperar (default: 5)

## Output
Exibe no chat:
- Hash do commit
- Mensagem do commit
- Data/hora do commit
- Lista de arquivos alterados
- Hash Git associated

## Notes
- Nao reverte codigo, apenas exibe o historico
- Os arquivos de commit devem estar em `<project>/commits/commit-*.md`
- Ordena por data de criacao do arquivo (mais recente primeiro)
- Usa apenas os arquivos .md, nao acessa o Git diretamente