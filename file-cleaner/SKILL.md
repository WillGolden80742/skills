---
name: file-cleaner
description: Remove arquivos, diretorios e dependencias de projetos (vendor Composer, pacotes npm)
triggers: ["remover", "clean", "limpar", "delete", "remove", "cleaner", "deletar", "remover dependencia", "remove dependency"]
---

## What I do
Executa a remocao de arquivos e dependencias de projetos, suportando:
1. Arquivos e diretorios específicos
2. Dependencias Composer (composer.json)
3. Dependencias npm (package.json)

## Parameters
- `target_path`: Caminho do arquivo ou diretorio a ser removido
- `remove_composer`: "true" para remover dependencias do composer.json
- `remove_npm`: "true" para remover dependencias do package.json
- `project_path`: Caminho base do projeto (default: workspace root)

## Usage

### Remover arquivo/diretorio:
```
python "~/.config/opencode/skills/file-cleaner/clean.py" --path "vendor" --project "C:\projeto"
```

### Remover arquivo e dependencias Composer:
```
python "~/.config/opencode/skills/file-cleaner/clean.py" --path "vendor" --remove-composer --project "C:\projeto"
```

### Remover dependencias especificas do Composer:
```
python "~/.config/opencode/skills/file-cleaner/clean.py" --remove-composer-deps "cboden/ratchet,guzzlehttp/guzzle" --project "C:\projeto"
```

## Notes
- O script automaticamente atualiza composer.json e package.json apos remover dependencias
- Scripts que referenciam vendor tambem sao removidos dos arquivos de configuracao
- Requer PowerShell no Windows ou Bash no Unix/Linux/macOS
