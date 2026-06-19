---
name: extrair-conteudo-paginas
description: Le conteudo de paginas web usando Mozilla Readability com rotacao de proxies (Node.js).
triggers: ["ler pagina", "ler pagina web", "web scraping", "scraping", "extrair pagina", "extrair texto", "read page", "readability", "mozilla readability", "extrair conteudo", "parse pagina", "parse html", "extrair artigo", "conteudo web", "baixar pagina", "fetch pagina", "node fetch", "jsdom", "extract content", "web page reader", "coletar texto", "raspagem", "raspar site", "conteudo de pagina", "pagina web", "artigo online", "ler artigo", "extrair noticia", "get page", "ler url", "fetch url", "page content"]
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
