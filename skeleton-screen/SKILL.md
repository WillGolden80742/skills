---
name: skeleton-screen
description: Gera skeleton screens (placeholder de carregamento) com shimmer animation para componentes WordPress
triggers: ["skeleton", "skeleton screen", "placeholder loading", "shimmer", "esqueleto carregamento", "loading placeholder", "skeleton loader"]
---

## What I Do

Gera skeleton screens (placeholders de carregamento) com animacao shimmer para componentes WordPress do tema uailove. Suporta 3 metodos: CSS direto, HTML estatico via PHP e injecao via JavaScript.

## Estruturas de Skeleton Identificadas no Tema

### 1. CSS Base - Animacao Shimmer

```css
/* Discovery / Chat / Desktop - gradient shimmer */
.skeleton {
    background: linear-gradient(90deg, rgba(255,255,255,0.1) 25%, rgba(255,255,255,0.2) 50%, rgba(255,255,255,0.1) 75%);
    background-size: 200% 100%;
    animation: skeleton-loading 1.5s infinite;
    border-radius: 4px;
    color: transparent !important;
    user-select: none;
    pointer-events: none;
}

@keyframes skeleton-loading {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}
```

```css
/* Admin - pseudo-elemento shimmer */
.skeleton::after {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.4), rgba(255,255,255,0));
    animation: skeletonShimmer 1.5s infinite;
}

@keyframes skeletonShimmer {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}
```

### 2. Variacoes de Skeleton Classes

| Classe | Uso | Dimensoes |
|--------|-----|-----------|
| `.skeleton` | Base generica | herda do container |
| `.skeleton-text` | Linhas de texto | height: 12-14px, border-radius |
| `.skeleton-short` | Texto curto (50% width) | width: 50% |
| `.skeleton-avatar` | Avatar circular | 36x36px, border-radius: 50% |
| `.skeleton-img` | Imagem retangular | 60x40px |
| `.skeleton-btn` | Botao circular | 32x32px, border-radius: 50% |
| `.skeleton-box` | Container generico | herda, border-radius: var(--radius-md) |
| `.skeleton-emoji` | Emoji chat | 32x32px, border-radius: 50% |
| `.skeleton-gif` | GIF grid | aspect-ratio: 1/1, full width |
| `.skeleton-card` | Card wrapper | pointer-events: none |
| `.skeleton-row` | Tabela/admin row | pointer-events: none |
| `.bg-skeleton` | Background cinza solido | background: #eee |

Utility width classes: `.w-40`, `.w-50`, `.w-60`, `.w-70`, `.w-80`, `.w-90`, `.w-100`, `.m-0`.

Utility height classes: `.sk-h14`, `.sk-h18`, `.sk-h20`, `.sk-h24`, `.sk-h40`.

### 3. Metodo PHP - Skeleton Renderizado no Servidor

Usado para secoes que carregam via fetch/JS. O PHP ja renderiza os skeletons, e o JS substitui quando os dados chegam.

**Cards com loop:**
```php
<?php for ($i = 0; $i < 4; $i++): ?>
<div class="point-card skeleton-card points-skeleton-item">
    <div class="point-image-container points-sk-bg"></div>
    <div class="point-info">
        <div class="skeleton-text points-sk-h20" style="width: <?php echo rand(60, 90); ?>%;"></div>
        <div class="skeleton-text points-sk-h14" style="width: <?php echo rand(40, 70); ?>%;"></div>
        <div class="skeleton-text points-sk-h40 w-100"></div>
    </div>
</div>
<?php endfor; ?>
```

**Lista de atividades:**
```php
<div class="mini-activity">
    <div class="activity-dot skeleton-avatar no-border"></div>
    <div class="skeleton-text w-80 m-0"></div>
</div>
```

### 4. Metodo JavaScript - Injecao de Skeleton no Fetch

Usado quando o componente carrega dados via AJAX/fetch.

**Template pattern (notifications.js):**
```javascript
showSkeletons(append = false) {
    const skeletonHtml = `
        <div class="notification-item skeleton-card notif-sk-card">
            <div class="skeleton-avatar notif-sk-avatar"></div>
            <div class="notif-sk-content">
                <div class="skeleton-text notif-sk-text-14 w-90"></div>
                <div class="skeleton-text notif-sk-text-12 w-50"></div>
            </div>
        </div>
    `;
    if (append) {
        this.listElement.insertAdjacentHTML('beforeend', skeletonHtml);
    } else {
        this.listElement.innerHTML = skeletonHtml;
    }
}

// Remocao apos carregar
const skeletons = this.listElement.querySelectorAll('.skeleton-card');
skeletons.forEach(el => el.remove());
```

**Admin table pattern (admin.js):**
```javascript
function setLoading(containerId, isLoading) {
    const container = document.getElementById(containerId);
    if (isLoading) {
        const skeletonHTML = `
            <div class="grid-row skeleton-row">
                <div class="grid-cell"><div class="skeleton skeleton-avatar"></div></div>
                <div class="grid-cell user-info-cell">
                    <div class="skeleton skeleton-text w-70"></div>
                    <div class="skeleton skeleton-text w-40"></div>
                </div>
                <div class="grid-cell"><div class="skeleton skeleton-text w-60"></div></div>
                <div class="grid-cell">
                    <div class="skeleton skeleton-btn"></div>
                    <div class="skeleton skeleton-btn"></div>
                </div>
            </div>
        `;
        container.innerHTML = skeletonHTML.repeat(4);
        container.classList.add('pointer-none');
    } else {
        container.classList.remove('pointer-none');
    }
}
```

**Discovery profile pattern:**
```javascript
// Adicionar skeletons no HTML estatico
document.querySelectorAll('.skeleton-button').forEach(btn => {
    btn.classList.remove('skeleton', 'skeleton-button');
    const icon = btn.querySelector('i');
    if (icon) {
        icon.classList.remove('opacity-0');
        icon.classList.add('opacity-100');
    }
});
```

### 5. Metodo CSS-in-JS ou Inline

Para elementos dinamicos criados via JS (chat.js):
```javascript
const skeleton = document.createElement('div');
skeleton.className = 'skeleton-emoji'; // ou 'skeleton-gif'
emojiGrid.appendChild(skeleton);
```

## Passos para Criar um Skeleton Screen

1. **Identifique o layout** do componente (card, lista, tabela, grid)
2. **Escolha o metodo:**
   - **PHP estatico**: quando o HTML inicial pode conter skeletons (secao carregada via fetch)
   - **JS injecao**: quando o componente carrega dados via AJAX
   - **CSS classes**: para elementos que removem a classe `.skeleton` apos carregar
3. **Crie as classes CSS** especificas (altura, largura) se necessario
4. **Implemente o shimmer** com `linear-gradient` + `background-size: 200% 100%`
5. **Remova os skeletons** apos os dados chegarem (`querySelectorAll('.skeleton-card').forEach(el => el.remove())`)

## Convencoes de Nomenclatura

- Container: `.skeleton-card` (aponta para remocao em massa)
- Itens internos: `.skeleton-text`, `.skeleton-avatar`, etc.
- Prefixo especifico: `notif-sk-*`, `points-sk-*`, `gifts-sk-*` para estilos contextuais
- Altura customizada: `.sk-h{altura-em-px}` (ex: `.sk-h18`)

## Padrao de Remocao

```javascript
// Apos o fetch bem-sucedido OU em caso de erro
const skeletons = container.querySelectorAll('.skeleton-card');
skeletons.forEach(el => el.remove());
// ou via classe:
element.classList.remove('skeleton', 'skeleton-text');
```
