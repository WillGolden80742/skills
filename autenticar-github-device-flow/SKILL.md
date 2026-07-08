---
name: autenticar-github-device-flow
description: Autentica GitHub via device flow (gh auth login --web) em ambientes OpenVS Code sem token pré-configurado e cria repositórios.
triggers: ["github", "git", "autenticar", "device flow", "login github", "gh auth", "criar repositorio", "criar repo"]
---

# Skill: autenticar-github-device-flow

## O que faz
Autentica no GitHub via **device flow** (`gh auth login --web`) e cria repositórios remotos. Ideal para ambientes OpenVS Code onde o provedor de autenticação do VS Code não expõe tokens diretamente no terminal.

## Fluxo

### 1. Autenticar
```bash
GITHUB_TOKEN="" gh auth login --hostname github.com --web
```
- Isso exibe um código de uso único (ex: `4C74-34CB`)
- O usuário deve acessar `https://github.com/login/device` e inserir o código
- O comando fica aguardando até a autenticação ser concluída no navegador
- Após autenticar, o gh CLI armazena o token em `~/.config/gh/hosts.yml`

### 2. Verificar autenticação
```bash
gh auth status
```
Deve retornar: `✓ Logged in to github.com as <usuario>`

### 3. Criar repositório e commitar
```bash
gh repo create <nome-repo> --public --description "<descricao>" --push --remote origin --source=.
```

## Observações
- O `GITHUB_TOKEN=""` é necessário para forçar o fluxo interativo mesmo em ambientes onde essa variável existe mas está vazia
- Usar `--web` faz o `gh` gerar um device code e exibir no terminal (em vez de tentar abrir navegador)
- Após autenticação bem-sucedida, comandos como `gh repo create`, `gh pr create`, etc. funcionam normalmente
- O token fica salvo em disco (`~/.config/gh/hosts.yml`), então autenticações futuras na mesma máquina não precisam repetir o processo
