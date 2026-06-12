---
name: leitor-pagina-node
description: Le conteudo de paginas web usando Mozilla Readability com rotacao de proxies (Node.js).
triggers:
  - "ler pagina"
  - "ler pagina"
  - "scraping "
  - "web scraping"
  - "extrair pagina"
---

# Skill Leitor de Pagina (Node.js)

##Script

O script esta em `script/index.js`.

## Instalacao

```bash
cd script
pnpm install
```

## Uso

```bash
node script/index.js <url>
```

## Exemplo

```bash
node script/index.js https://exemplo.com/artigo
```

## Dependencias

- `@mozilla/readability`
- `jsdom`
- `node-fetch`
