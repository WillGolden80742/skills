---
name: slack-gif-creator
description: Cria GIFs animados otimizados para Slack com ferramentas de validação e conceitos de animação.
triggers: ["gif", "slack", "animacao", "criar gif", "emoji gif", "gif animado", "criar animacao", "gif slack", "gif emoji", "animated gif", "gif builder", "fazer gif", "gerar gif", "gif otimizado", "otimizar gif", "gif cores", "gif fps", "gif tamanho", "gif dimensoes", "gif 128x128", "gif 480x480", "gif validar", "validar gif", "slack ready", "easing animation", "pulse animation", "bounce animation", "shake animation", "spin animation", "fade animation", "slide animation", "explode animation"]
---

# Skill Slack GIF Creator

## Requisitos do Slack

**Dimensões:**
- GIFs de emoji: 128x128 (recomendado)
- GIFs de mensagem: 480x480

**Parâmetros:**
- FPS: 10-30 (menor = arquivo menor)
- Cores: 48-128 (menos = arquivo menor)
- Duração: Mantenha sob 3 segundos para emoji GIFs

## Workflow Core

```python
from core.gif_builder import GIFBuilder
from PIL import Image, ImageDraw

builder = GIFBuilder(width=128, height=128, fps=10)

for i in range(12):
    frame = Image.new('RGB', (128, 128), (240, 248, 255))
    draw = ImageDraw.Draw(frame)
    builder.add_frame(frame)

builder.save('output.gif', num_colors=48, optimize_for_emoji=True)
```

## Desenhando Gráficos

### Imagens Enviadas pelo Usuário
Se usuário enviar imagem:
- **Usar diretamente** ("animate isso")
- **Usar como inspiração** ("faça algo assim")

### Desenhando do Zero
Use primitives do PIL ImageDraw:

```python
draw = ImageDraw.Draw(frame)

# Círculos
draw.ellipse([x1, y1, x2, y2], fill=(r, g, b))

# Polígonos (estrelas, triângulos)
points = [(x1, y1), (x2, y2), (x3, y3)]
draw.polygon(points, fill=(r, g, b))

# Linhas
draw.line([(x1, y1), (x2, y2)], fill=(r, g, b), width=5)

# Retângulos
draw.rectangle([x1, y1, x2, y2], fill=(r, g, b))
```

## Fazendo Gráficos Ficarem Bons

- **Linhas mais grossas** - Use `width=2` ou mais
- **Profundidade visual** - Gradientes, múltiplas camadas
- **Formas interessantes** - Adicione highlights, anéis, padrões
- **Cores vibrantes** - Contraste complementar

## Utilitários Disponíveis

### GIFBuilder
```python
builder = GIFBuilder(width=128, height=128, fps=10)
builder.add_frame(frame)
builder.save('out.gif', num_colors=48)
```

### Validadores
```python
from core.validators import validate_gif, is_slack_ready
passes, info = validate_gif('my.gif', is_emoji=True)
```

### Funções de Ease
```python
from core.easing import interpolate
y = interpolate(start=0, end=400, t=t, easing='ease_out')
```

## Conceitos de Animação

- **Shake/Vibrar** - Use `math.sin()` com índice do frame
- **Pulse** - Escale rhythmicamente com `math.sin()`
- **Bounce** - Use `easing='bounce_out'`
- **Spin/Rotate** - `image.rotate(angle)`
- **Fade In/Out** - Ajuste canal alpha
- **Slide** - Move de fora para posição com `ease_out`
- **Zoom** - Escale e posicione
- **Explode** - Partículas radiando para fora

## Otimização

Para reduzir tamanho de arquivo:
1. Menos frames - FPS menor
2. Menos cores - `num_colors=48`
3. Dimensões menores
4. `remove_duplicates=True`
5. `optimize_for_emoji=True`
