---
name: docx
description: Cria, lê e edita documentos Word (.docx). Use para criar relatórios, cartas, documentos profissionais com formatação.
triggers: ["word", "docx", "documento word", "relatorio word", "criar documento", "editar docx", "criar docx", "editar word", "microsoft word", "arquivo word", "documento profissional", "carta formal", "relatorio profissional", "documento formatado", "word com tabela", "word com imagem", "cabecalho word", "rodape word", "sumario word", "numero pagina word", "estilos word", "fonte word", "margem word", "formatação word", "pandoc docx", "converter docx", "docx javascript", "criar relatorio", "carta comercial", "documento oficial", "word documento", "edit word", "ler docx", "abrir docx", "gerar word"]
---

# Skill DOCX - Documentos Word

## Visão Geral

Arquivos .docx são arquivos ZIP contendo XML.

## Abordagens

| Tarefa | Ferramenta |
|--------|------------|
| Ler conteúdo | `pandoc` ou descompactar para XML |
| Criar novo | `docx-js` (npm) |
| Editar existente | Descompactar → editar XML → recomprimir |

## Converter .doc para .docx

```bash
python scripts/office/soffice.py --headless --convert-to docx documento.doc
```

## Extração de Texto

```bash
pandoc documento.docx -o saida.md
```

## Criação de Documentos

Instale: `npm install -g docx`

```javascript
const { Document, Packer, Paragraph, TextRun } = require('docx');

const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: [
      new Paragraph({ children: [new TextRun("Título")] })
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => fs.writeFileSync("doc.docx", buffer));
```

## Regras Importantes

- **Definir tamanho da página explicitamente** - docx-js usa A4 por padrão
- **Nunca use `\n`** - use elementos Paragraph separados
- **Nunca use bullets Unicode** - use numeração config com LevelFormat.BULLET
- **PageBreak deve estar dentro de Paragraph**

## Validação

```bash
python scripts/office/validate.py doc.docx
```

## Edição de Documentos Existentes

1. Descompactar: `python scripts/office/unpack.py documento.docx descompactado/`
2. Editar XML em `descompactado/word/`
3. Recomprimir: `python scripts/office/pack.py descompactado/ saida.docx`
