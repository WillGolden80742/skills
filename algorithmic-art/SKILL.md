---
name: algorithmic-art
description: Cria arte algorítmica usando p5.js com aleatoriedade controlada e exploração interativa de parâmetros.
triggers: ["arte algoritmica", "generative art", "p5.js", "particle", "flow field"]
---

# Skill Algorithmic Art

## Filosofia Algorítmica

Crie um movimento algorítmico (não imagens estáticas) que será expressado através de:
- Processos computacionais, comportamento emergente
- Aleatoriedade controlada, campos de ruído, sistemas orgânicos
- Partículas, fluxos, campos, forças
- Variação paramétrica e caos controlado

## Processo

1. **Criar Filosofia Algorítmica** (.md)
2. **Expressar em Código** (.html + .js)

## Requisitos Técnicos

### Aleatoriedade com Seed

```javascript
let seed = 12345;
randomSeed(seed);
noiseSeed(seed);
```

### Estrutura de Parâmetros

```javascript
let params = {
  seed: 12345,
  // Quantidades (quantos?)
  // Escalas (quão grande? quão rápido?)
  // Probabilidades (quão provável?)
  // Proporções
  // Ângulos
  // Limiares
};
```

### Canvas Setup

```javascript
function setup() {
  createCanvas(1200, 1200);
}

function draw() {
  // Algoritmo generativo
}
```

## Filosofias de Exemplo

**"Organic Turbulence"**
Fluxos guiados por ruído Perlin em camadas. Milhares de partículas seguindo forças vetoriais.

**"Quantum Harmonics"**
Partículas com valores de fase que interferem, criando mandalas emergentes.

**"Recursive Whispers"**
Estruturas ramificadas com subdivisão recursiva, sistemas L.
