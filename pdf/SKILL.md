---
name: pdf
description: Processa arquivos PDF - ler, extrair texto/tabelas, mesclar, dividir, criar PDFs.
triggers:
  - "pdf"
  - "convert * to pdf"
  - "converter * para pdf"
  - "merge pdf"
  - "mesclar pdf"
  - "split pdf"
  - "dividir pdf"
  - "extract text from pdf"
  - "extrair texto do pdf"
  - "create pdf"
  - "criar pdf"
  - "read pdf"
  - "ler pdf"
---

# Skill PDF - Processamento de PDFs

## Bibliotecas Python

### pypdf - Operações Básicas

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("documento.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

with open("saida.pdf", "wb") as output:
    writer.write(output)
```

### pdfplumber - Extrair Texto e Tabelas

```python
import pdfplumber

with pdfplumber.open("documento.pdf") as pdf:
    for page in pdf.pages:
        texto = page.extract_text()
        tabelas = page.extract_tables()
```

### reportlab - Criar PDFs

```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf", pagesize=letter)
c.drawString(100, 700, "Olá Mundo!")
c.save()
```

## Ferramentas de Linha de Comando

```bash
pdftotext input.pdf output.txt
qpdf --empty --pages file1.pdf file2.pdf -- merged.pdf
```

## Tarefas Comuns

### Mesclar PDFs
```python
from pypdf import PdfWriter
writer = PdfWriter()
for f in ["doc1.pdf", "doc2.pdf"]:
    reader = PdfReader(f)
    for page in reader.pages:
        writer.add_page(page)
with open("mesclado.pdf", "wb") as out:
    writer.write(out)
```

### Dividir PDF
```python
reader = PdfReader("input.pdf")
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"pagina_{i+1}.pdf", "wb") as out:
        writer.write(out)
```

### Extrair Texto de PDFs Escaneados
```python
from pdf2image import convert_from_path
import pytesseract

images = convert_from_path('scaneado.pdf')
for img in images:
    texto = pytesseract.image_to_string(img)
```

## Referência Rápida

| Tarefa | Melhor Ferramenta |
|--------|------------------|
| Mesclar | pypdf |
| Dividir | pypdf |
| Extrair texto | pdfplumber |
| Extrair tabelas | pdfplumber |
| Criar PDF | reportlab |
