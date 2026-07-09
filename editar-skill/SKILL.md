---
name: editar-skill
description: Edita uma skill existente - altera conteudo, triggers, descricao e re-gerencia AST.
triggers: ["editar skill", "editar knowledge", "alterar skill", "modificar skill", "edit skill", "atualizar skill", "update skill", "mudar skill", "ajustar skill", "refinar skill"]
---

## What I do
Edita uma skill existente no diretorio `~/.config/opencode/skills/`. Permite alterar nome, descricao, triggers e conteudo. Apos editar, re-executa o AST.

## Usage
1. Execute o skillFactory.py
2. Sera mostrada lista de skills existentes
3. Selecione o numero da skill a editar
4. Altere os campos desejados (pressione Enter para manter atual)
5. O conteudo sera aberto no editor padrao
6. Ao salvar, o AST sera re-gerado automaticamente

## Estrutura de um Skill
Um skill deve ter:
- **name**: nome interno do skill
- **description**: descricao em uma linha do que o skill faz
- **triggers**: array de palavras/frases que ativam o skill
- **Conteudo**: documentacao de como executar o skill

## Comando
```bash
python "~/.config/opencode/skills/editar-skill/editSkillFactory.py"
```
