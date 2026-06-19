---
name: gerenciar-remover-skills
description: Remove ou atualiza skills que nao ficaram boas o suficiente.
triggers: ["remover skill", "refatorar skill", "deletar skill", "update skill", "remover skill ruim", "skill ruim", "skill broken", "atualize skill", "editar skill", "modificar skill", "deletar skill", "excluir skill", "apagar skill", "remover skill opencode", "atualizar skill", "skill desnecessario", "skill quebrado", "corrigir skill", "fix skill", "skill errado", "skill remove", "skill delete", "skill update", "limpar skills", "gerenciar skills", "listar skills", "skill nao presta", "skill refactory", "refatorar skills", "organizar skills", "skill manager"]
---

## What I do
Lista, remove ou atualiza skills existentes no diretorio `~/.config/opencode/skills/`.

## Usage
1. Execute o skill que chamara o script Python
2. Serao listados todos os skills existentes com numeros
3. Escolha uma acao:
   - Para **remover**: digite o numero do skill
   - Para **atualizar**: digite "u" seguido do numero (ex: u3)
   - Para **sair**: digite "q"

## Acoes disponiveis
- **Remover skill**: Remove completamente o diretorio do skill
- **Atualizar skill**: Abre o skill para edicao no editor padrao

## Comando
```bash
python "~/.config/opencode/skills/gerenciar-remover-skills/skillRefactory.py"
```