---
name: criar-novo-skill
description: Cria um novo skill para o opencode a partir de um template padrao.
triggers: ["criar skill", "criar nova skill", "new skill", "criar skill nova", "skill factory", "factory skill", "novo skill", "criar skill opencode", "skill personalizado", "criar trigger", "adicionar skill", "skill template", "novo skill opencode", "cria skill", "crie skill", "gerar skill", "make skill", "create skill", "skill maker", "skill generator", "gerador skill", "fabricar skill", "skill do zero", "criar conhecimento", "skill custom", "opencode skill", "adicionar conhecimento", "registrar skill", "configurar skill", "criar plugin skill", "skill novo"]
---

## What I do
Cria um novo skill no diretorio `~/.config/opencode/skills/` seguindo o template padrao do opencode.

## Usage
1. Execute o skill que chamara o script Python
2. O script aguardara o nome do skill
3. O script aguardara a descricao do skill
4. O script aguardara os triggers (separados por virgula)
5. O script aguardara o conteudo/conhecimento do skill
6. O skill sera criado em `~/.config/opencode/skills/<nome-do-skill>/SKILL.md`

## Estrutura de um Skill
Um skill deve ter:
- **name**: nome interno do skill
- **description**: descricao em uma linha do que o skill faz
- **triggers**: array de palavras/frases que ativam o skill
- **Conteudo**: documentacao de como executar o skill, inputs esperados e outputs

## Comando
```bash
python "~/.config/opencode/skills/criar-novo-skill/skillFactory.py"
```
