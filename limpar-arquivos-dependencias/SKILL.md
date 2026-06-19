---
name: limpar-arquivos-dependencias
description: Remove arquivos, diretorios e dependencias de projetos (vendor Composer, pacotes npm)
triggers: ["remover", "clean", "limpar", "delete", "remove", "cleaner", "deletar", "remover dependencia", "remove dependency", "limpar projeto", "remover vendor", "remover node_modules", "composer remove", "npm remove", "limpar composer", "limpar npm", "desinstalar pacote", "remover pacote", "clean projeto", "limpar cache", "remover diretorio", "remover pasta", "delete folder", "remove directory", "excluir dependencia", "desinstalar dependencia", "composer clean", "npm clean", "limpar dependencias", "remover composer package", "remover npm package", "cleaner projeto", "file cleaner", "limpeza projeto", "limpar workspace"]
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
python "~/.config/opencode/skills/limpar-arquivos-dependencias/clean.py" --path "vendor" --project "C:\projeto"
```

### Remover arquivo e dependencias Composer:
```
python "~/.config/opencode/skills/limpar-arquivos-dependencias/clean.py" --path "vendor" --remove-composer --project "C:\projeto"
```

### Remover dependencias especificas do Composer:
```
python "~/.config/opencode/skills/limpar-arquivos-dependencias/clean.py" --remove-composer-deps "cboden/ratchet,guzzlehttp/guzzle" --project "C:\projeto"
```

## Notes
- O script automaticamente atualiza composer.json e package.json apos remover dependencias
- Scripts que referenciam vendor tambem sao removidos dos arquivos de configuracao
- Requer PowerShell no Windows ou Bash no Unix/Linux/macOS
