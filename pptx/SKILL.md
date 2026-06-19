---
name: pptx
description: Cria e edita apresentações PowerPoint (.pptx). Use para criar slides, decks, apresentações.
triggers: ["pptx", "powerpoint", "slides", "apresentacao", "deck", "criar slides", "criar pptx", "editar pptx", "apresentacao slides", "slide deck", "powerpoint presentation", "criar apresentacao", "slide design", "template slides", "slide mestre", "microsoft powerpoint", "editar apresentacao", "paleta slides", "tema slides", "transicao slides", "animacao slides", "slide profissional", "deploy pptx", "converter pptx", "markitdown pptx", "slide imagem", "thumbnail slide", "design slide", "slide titulo", "slide conteudo", "slide grafico", "fonte slides", "tamanho slide"]
---

# Skill PPTX - Apresentações PowerPoint

## Referência Rápida

| Tarefa | Ferramenta |
|--------|------------|
| Ler conteúdo | `python -m markitdown apresentação.pptx` |
| Editar existente | Ver editing.md |
| Criar do zero | Ver pptxgenjs.md |

## Ler Conteúdo

```bash
python -m markitdown apresentação.pptx
python scripts/thumbnail.py apresentação.pptx
```

## Design de Slides

### Paletas de Cores

| Tema | Primária | Secundária | Destaque |
|------|---------|------------|----------|
| Midnight Executive | `1E2761` | `CADCFC` | `FFFFFF` |
| Forest & Moss | `2C5F2D` | `97BC62` | `F5F5F5` |
| Coral Energy | `F96167` | `F9E795` | `2F3C7E` |

### Dicas de Design

- **Não crie slides tediosos** - texto simples em fundo branco não impressiona
- **Use elemento visual** - imagem, gráfico, ícone ou forma
- **Contraste dark/light** - fundos escuros para títulos, claros para conteúdo
- **Nunca use linhas decorativas sob títulos** - é sinal de slides gerados por IA

### Tipografia

| Elemento | Tamanho |
|----------|---------|
| Título do slide | 36-44pt |
| Cabeçalho de seção | 20-24pt |
| Texto do corpo | 14-16pt |

## QA (Verificação Obrigatória)

1. Verifique conteúdo: `python -m markitdown output.pptx`
2. Procure placeholders: `python -m markitdown output.pptx | grep -iE "xxxx|lorem|ipsum"`
3. Converta para imagens e inspecione visualmente

## Converter para Imagens

```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

## Dependências

- `pip install "markitdown[pptx]"`
- `pip install Pillow`
- `npm install -g pptxgenjs`
