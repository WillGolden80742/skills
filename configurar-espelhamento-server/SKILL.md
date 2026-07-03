---
name: configurar-espelhamento-server
description: Configura espelhamento bidirecional seguro entre pasta local Windows e servidor Linux remoto via SSH/SFTP.
triggers: ["espelho", "espelhamento", "mirror", "sincronizar", "sync bidirecional", "espelhar pasta"]
---

# Skill: configurar-espelhamento-server

## O que faz
Configura um espelhamento bidirecional em tempo real entre uma **pasta local (Windows)** e uma **pasta remota (Linux)** via SSH/SFTP, com proteção contra:
- Race condition (watcher local vs poller remoto)
- Upload/download de arquivos de 0 bytes
- Exclusão acidental no servidor (additive-only)
- Pastas `.git` ignoradas automaticamente

## Como usar
Ative este skill e ele executará `configurar_espelho.py` que pergunta:

1. **SSH Host**
2. **SSH Port**
3. **SSH User**
4. **SSH Password** (mascarada)
5. **Caminho local absoluto** (ex: `C:\Projetos\meu-site\wp-content\themes\meu-tema`)
6. **Caminho remoto absoluto** (ex: `/home/user/public_html/wp-content/themes/meu-tema`)

## O que será gerado na pasta local

| Arquivo | Descricao |
|---------|-----------|
| `.sync_theme.py` | Script principal de sincronizacao com SSH paramiko + watchdog |
| `.sync_meta.json` | Cache de metadados dos arquivos remotos |
| `iniciar_espelho.bat` | Atalho para executar o sync (2 horas por padrao) |

## Como usar apos configurar
- Dê dois cliques em `iniciar_espelho.bat` dentro da pasta espelhada
- Ou execute manualmente: `python .sync_theme.py 120` (minutos)
- Logs mostram uploads/downloads/protecoes em tempo real

## Seguranca
- Senha SSH via variavel de ambiente (`BHM_SSH_PW`), nunca em disco
- Nada e deletado no remoto
- Lock de download evita race condition
- `.git` e arquivos do proprio sync (.sync_*) sao ignorados
