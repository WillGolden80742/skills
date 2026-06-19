---
name: web-artifacts-builder
description: Cria artefatos HTML complexos com React, Tailwind CSS e shadcn/ui para exibir no chat.
triggers: ["html", "react", "artifact", "shadcn", "webapp", "componente", "artefato web", "componente react", "tailwind css", "react typescript", "vite", "parcel", "bundle html", "web artifact", "criar artefato", "html bundle", "react componente", "shadcn ui", "ui component", "artefato html", "frontend react", "react app", "criar webapp", "componente ui", "single html", "self contained html", "html unico", "bundle react", "aplicacao react", "interface react", "gerar html"]
---

# Skill Web Artifacts Builder

## Stack

React 18 + TypeScript + Vite + Parcel + Tailwind CSS + shadcn/ui

## Passos

1. Inicialize o projeto: `bash scripts/init-artifact.sh <nome-projeto>`
2. Desenvolva editando os arquivos gerados
3. Bundle para HTML: `bash scripts/bundle-artifact.sh`
4. Exiba ao usuário

## Inicializar Projeto

```bash
bash scripts/init-artifact.sh meu-projeto
cd meu-projeto
```

Isso cria projeto configurado com:
- React + TypeScript
- Tailwind CSS 3.4.1
- shadcn/ui
- 40+ componentes pré-instalados

## Bundlar para HTML

```bash
bash scripts/bundle-artifact.sh
```

Cria `bundle.html` - arquivo autossuficiente com todo JavaScript e CSS inline.

## Design

**IMPORTANTE**: Evite "AI slop" - layouts centrados excessivos, gradientes roxos, cantos arredondados uniformes, e fonte Inter.
