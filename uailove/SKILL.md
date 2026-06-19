---
name: uailove
description: Tema WordPress tipo SPA (Single Page Application) para app de relacionamento, usando arquitetura MVC customizada em PHP com WebSocket externo Node.js.
triggers: ["uailove", "tema uailove", "app relacionamento", "dating app", "tema wordpress mvc", "websocket", "moedadetroka", "spa wordpress", "discovery", "matches", "messages", "points", "shop", "mvc wordpress", "tema spa", "single page application", "uailove tema", "perfil usuario", "match", "chat mensagem", "notificacao", "pwa", "service worker", "likes", "fotos perfil", "websocket node", "node websocket", "tempo real", "real time", "long polling", "uailove ws", "app namoro", "site relacionamento", "platfroma dating", "mimos", "presente virtual"]
---

## Arquitetura

O tema usa namespace `UaiLove\MVC` com autoloader PSR-4 customizado em `app/autoloader.php` (não usa Composer para as próprias classes). O backend roda PHP 8.0+ sobre WordPress 5.4+. O frontend é uma SPA em Vanilla JS puro renderizada por PHP views. Comunicação em tempo real via WebSocket externo Node.js, com fallback para long polling AJAX. PWA via `PwaController` + `PwaModel`.

---

## Estrutura de Arquivos

Os arquivos na raiz do tema são wrappers mínimos que delegam para `app/`. Toda a lógica fica dentro da estrutura MVC.

```
wp-content/themes/uailove/
├── functions.php        → app/bootstrap.php
├── index.php            → app/index.php
├── header.php           → app/header.php
├── footer.php           → app/footer.php
├── page.php             → app/page.php
├── single.php           → app/single.php
├── archive.php          → app/archive.php
├── search.php           → app/search.php
├── 404.php              → app/404.php
├── sidebar.php          → app/sidebar.php
├── comments.php         → app/comments.php
└── app/
    ├── bootstrap.php        ← ponto de entrada real
    ├── autoloader.php       ← PSR-4 customizado
    ├── controllers/
    ├── models/
    ├── services/
    ├── views/
    │   ├── home/            ← seções da SPA
    │   ├── layouts/         ← application.php, base.php
    │   ├── shared/          ← fragmentos reutilizáveis
    │   └── landingpage.php
    ├── config/
    │   ├── routes.php       ← mapa URL → Controller → action
    │   ├── database.php     ← credenciais (table_prefix: uailove_)
    │   └── initializers/    ← custom-header, template-tags, customizer, jetpack
    ├── lib/
    │   ├── TemplateHelper.php
    │   ├── tasks/           ← scripts utilitários (seed, mock data, migrate)
    │   └── traits/
    │       └── Singleton.php ← trait usado por todos os controllers
    └── assets/
        ├── javascripts/     ← JS por seção (websocket-service.js, points.js…)
        └── stylesheets/     ← CSS por seção (points.css…)
```

---

## Namespace Map (Autoloader)

| Namespace                    | Diretório físico   |
|------------------------------|--------------------|
| `UaiLove\MVC\Controllers\`   | `app/controllers/` |
| `UaiLove\MVC\Models\`        | `app/models/`      |
| `UaiLove\MVC\Services\`      | `app/services/`    |
| `UaiLove\MVC\Traits\`        | `app/lib/traits/`  |
| `UaiLove\MVC\Config\`        | `app/config/`      |
| `UaiLove\MVC\Lib\`           | `app/lib/`         |

---

## Fluxo de Inicialização

```
functions.php
  └── app/bootstrap.php
        ├── define('_S_VERSION', '1.0.0')
        ├── vendor/autoload.php          ← Composer (opcional)
        ├── app/autoloader.php           ← PSR-4 do tema
        ├── Application::get_instance()  ← instancia controllers e services via Singleton
        ├── uailove_setup()              ← add_action('after_setup_theme')
        │     ├── load_theme_textdomain
        │     ├── add_theme_support (title-tag, post-thumbnails, html5…)
        │     └── register_nav_menus
        ├── uailove_widgets_init()       ← add_action('widgets_init')
        └── config/initializers/
              ├── custom-header.php
              ├── template-tags.php
              ├── template-functions.php
              ├── customizer.php
              └── jetpack.php            ← só se JETPACK__VERSION definido
```

---

## Rotas de URL

Definidas em `config/routes.php`. O `RouterService` lê `$_SERVER['REQUEST_URI']` e determina a seção ativa. O `TemplateRouterController` intercepta o hook `template_include` do WordPress e serve o layout da SPA para todas as rotas, ignorando o sistema padrão de templates.

| URL                  | Controller                  | Seção          |
|----------------------|-----------------------------|----------------|
| `/discovery`         | `DiscoveryController`       | discovery      |
| `/matches`           | `MatchesController`         | matches        |
| `/messages[/:id]`    | `MessagesController`        | messages       |
| `/point`             | `PointsController`          | points         |
| `/profile`           | `ProfileController`         | profile        |
| `/notifications`     | `NotificationsController`   | notifications  |
| `/admin`             | `AdminController`           | admin          |
| `/shop`              | `ShopController`            | shop           |
| *(padrão)*           | `DiscoveryController`       | discovery      |

> Usuários não logados são redirecionados para `/profile`, exceto na rota `/admin`.

---

## Controllers

Todos usam o trait `Singleton` e registram seus hooks no construtor.

| Controller                 | Responsabilidade                                         |
|----------------------------|----------------------------------------------------------|
| `AdminController`          | Endpoints AJAX do painel admin, estatísticas de usuários |
| `AdminSettingsController`  | Salvar e recuperar configurações do admin                |
| `DiscoveryController`      | Feed de perfis para descoberta, registrar likes          |
| `GifController`            | Proxy para APIs de GIF (Giphy/Tenor)                     |
| `MainController`           | Long polling, bootstrap de dados, setup inicial          |
| `MatchesController`        | Recuperar e registrar matches                            |
| `MessagesController`       | Enviar/receber mensagens, listar conversas               |
| `NotificationsController`  | Listar, marcar como lidas e limpar notificações          |
| `PointsController`         | CRUD de pontos de encontro                               |
| `ProfileController`        | Atualizar perfil, fotos, interesses; upload de mídia WP  |
| `PwaController`            | Servir manifest.json e service worker                    |
| `ShopController`           | Processar compra de mimos, listar pedidos                |
| `TemplateRouterController` | Intercepta `template_include` e serve o layout da SPA   |

---

## Models

| Model                         | Responsabilidade                                                              |
|-------------------------------|-------------------------------------------------------------------------------|
| `AdminModel`                  | Queries de dados para o painel admin                                          |
| `AdminSettingsModel`          | Persistência de configurações via Options API                                 |
| `ChatModel`                   | Legado: acesso direto ao CPT `chat` — preferir `ConversationModel`            |
| `ConversationModel`           | Formata conversas com metadata de usuário                                     |
| `DiscoveryModel`              | Filtra e ordena perfis para descoberta                                        |
| `GifModel`                    | Consulta APIs externas de GIF (Tenor/Giphy)                                   |
| `LikeModel`                   | Persiste likes e verifica match mútuo                                         |
| `MatchModel`                  | Gerencia matches confirmados, dispara notificações                            |
| `MessagesModel`               | Lê/escreve mensagens no CPT `chat`                                            |
| `NotificationModel`           | CRUD de notificações do usuário                                               |
| `NotificationQueueModel`      | Fila para push de notificações em tempo real                                  |
| `PhotoModel`                  | Upload e gerenciamento de fotos de perfil                                     |
| `PointModel`                  | CRUD de pontos de encontro no CPT `point`; geocoding via Google Maps          |
| `ProductModel`                | Produtos WooCommerce                                                          |
| `ProfileFieldDefinitionModel` | Define campos dinâmicos do perfil (label, tipo, opções)                       |
| `ProfileModel`                | Persiste e prepara dados de perfil via `get_section_data()`                   |
| `PwaModel`                    | Gera manifest.json e configurações PWA                                        |
| `ShopModel`                   | Pedidos WooCommerce: `get_orders()`, `get_received_orders()`, `get_match_profiles()` |
| `UserProfileModel`            | Leitura e normalização de dados de perfil do usuário                          |

---

## Services

| Service                  | Responsabilidade                                                    |
|--------------------------|---------------------------------------------------------------------|
| `AddressCacheService`    | Cache de endereços geocodificados                                   |
| `CptFactoryService`      | Registra Custom Post Types de forma declarativa                     |
| `EnvService`             | Lê variáveis de ambiente (`.env`, constantes WordPress)             |
| `RouterService`          | Determina seção ativa da SPA a partir do `REQUEST_URI`              |
| `SystemSetupService`     | Registra CPTs, user meta boxes e customiza labels WooCommerce       |
| `UserMetaFactoryService` | Cria meta boxes de usuário no wp-admin de forma declarativa         |
| `WebSocketService`       | Fornece URL do WebSocket via filter `uailove_ws_url`                |

---

## Custom Post Types

O tema registra dois CPTs via `CptFactoryService` + `SystemSetupService`:

- **`chat`** — mensagens trocadas entre usuários
- **`point`** — pontos de encontro físicos

---

## AJAX Actions

O tema usa `wp_ajax_{action}` para usuários logados. Prefixo padrão: `uailove_`.

**Chat / Mensagens**
- `uailove_get_chat_conversations` — lista todas as conversas do usuário
- `uailove_open_chat` — abre ou cria uma conversa específica
- `uailove_send_chat_message` — envia mensagem de texto ou GIF

**Descoberta**
- `uailove_get_discovery_profiles` — retorna perfis para o feed
- `uailove_send_like` — registra like ou super like em um perfil

**Matches**
- `uailove_get_user_matches` — lista matches confirmados do usuário
- `uailove_send_match` — registra match manualmente (admin/debug)

**Perfil**
- `uailove_update_profile` — salva dados do perfil (bio, interesses, etc.)
- `uailove_update_photos_array` — reordena ou atualiza array de fotos
- `uailove_upload_photo` — faz upload de nova foto de perfil
- `uailove_remove_photo` — remove foto do perfil

**Notificações**
- `uailove_get_notifications` — lista notificações do usuário
- `uailove_clear_notifications` — remove todas as notificações
- `uailove_delete_notification` — remove notificação específica
- `uailove_mark_notifications_read` — marca notificações como lidas

**Long Polling**
- `uailove_long_polling` — aguarda novos eventos (mensagens, matches, notificações)

**Loja**
- `uailove_buy_gift` — processa compra e envio de mimo

**REST API**
- `GET  /wp-json/uailove/v1/points` — lista pontos de encontro
- `POST /wp-json/uailove/v1/points/geocode` — geocodifica endereço (requer `X-WP-Nonce`)

---

## WebSocket

O sistema de tempo real usa um servidor Node.js externo com SSL, acessível em:

```
wss://websocket.moedadetroka.com.br/
```

O Nginx do servidor atua como reverse proxy com terminação SSL, repassando conexões para o processo Node.js na porta local. Para configurar a URL no WordPress:

```php
// wp-config.php
define('UAILOVE_WS_URL', 'wss://websocket.moedadetroka.com.br/');
```

O `WebSocketService` expõe a URL via filter `uailove_ws_url`.

**Cliente JS** (`app/assets/javascripts/websocket-service.js`): a classe `WPWebSocketService` é instanciada como singleton global em `window.UaiLoveWS`. Possui reconexão automática (até 5 tentativas, intervalo de 3s), heartbeat keepalive a cada 30s e fallback automático para long polling via `uailove_long_polling`.

O arquivo `app/assets/javascripts/websocket-admin.js` gerencia a conexão WebSocket no painel administrativo.

---

## Frontend (SPA)

O tema é uma SPA — tudo renderizado dentro de uma única página WordPress. Sem framework JS; Vanilla JS puro.

**Seções da SPA:** `discovery`, `matches`, `messages`, `points`, `notifications`, `profile`, `shop`, `admin`.

**Globals JS injetados via `wp_localize_script`:**
- `window.UaiLoveWS` — instância do `WPWebSocketService`
- `window.MEU_TEMA` — dados do tema (nonces, URLs, config)
- `window.wpApiSettings` — nonce do REST API
- `window.realPointData` — pontos carregados via REST

**CSS:** variáveis customizadas (`--bg-input`, `--border-field`, `--radius-huge`, `--primary-purple`, `--text-muted`, `--text-dark`, `--white`, `--shadow-md`, `--shadow-lg`, `--transition-smooth`, `--radius-md`). Fonte principal: `Outfit` (sans-serif). Ícones: Font Awesome (`fa-solid`).

**Mapas:** Leaflet.js — instância global em `window.uailoveMap`; chamar `invalidateSize()` ao exibir o container após transições de layout.

---

## Integrações

- **WooCommerce** — obrigatório; loja de mimos com produtos renomeados para "Mimos" via `SystemSetupService`
- **OpenCage Geocoder** — `composer opencage/geocode ^2.0`; geocoding alternativo
- **Google Maps** — geocoding de pontos via `PointModel`
- **Tenor / Giphy** — proxy de GIFs via `GifController` + `GifModel`
- **Composer** — opcional (só necessário para o OpenCage)

---

## Convenções

Classes em `PascalCase`, métodos em `camelCase`, arquivos PHP em `PascalCase` (ex: `ProfileController.php`), arquivos JS/CSS em `kebab-case` (ex: `websocket-service.js`, `points.css`). Um controller por recurso, um service por domínio, um model por entidade. Todos os controllers são singletons via trait `Singleton`. Prefixo AJAX e tabelas do BD: `uailove_`. Text domain: `_s` (legado do starter theme Underscores).

---

## Scripts de Desenvolvimento

```bash
npm run watch        # node-sass sass/ -o ./ --source-map true -w
npm run compile:css  # compila + stylelint --fix
npm run compile:rtl  # rtlcss style.css style-rtl.css
npm run lint:scss    # wp-scripts lint-style 'sass/**/*.scss'
npm run lint:js      # wp-scripts lint-js 'js/*.js'
npm run bundle       # gera .zip do tema para deploy
```

Linting PHP: `phpcs` com ruleset `WordPress` + `WPThemeReview`. JS: `@wordpress/eslint-plugin/esnext`. CSS: `@wordpress/stylelint-config/scss`.

---

## Tasks Utilitárias

Localizadas em `app/lib/tasks/`. Executadas manualmente conforme necessidade:

`assign-coords.php`, `attach-images.php`, `cleanup-mock-data.php`, `generate-mock-mimos.php`, `generate-mock-users.php`, `generate-more-matches.php`, `generate-points.php`, `import-gifts.php`, `insert-kinoko-marvic.php`, `test-images.php`, `update-interests.php`, `update_assets_path.php`.

---

## Segurança

Autenticação via WordPress nativo (`is_user_logged_in()`). AJAX protegido por `wp_ajax_{action}` (somente usuários logados). REST API exige `X-WP-Nonce` no header. CSRF via nonce WordPress. Usuários não autenticados redirecionados para `/profile` pelo `RouterService`.

---

## Requisitos

| Requisito          | Versão mínima | Observação                               |
|--------------------|---------------|------------------------------------------|
| PHP                | 7.4+          | Recomendado 8.0+                         |
| WordPress          | 5.4+          |                                          |
| WooCommerce        | 5.0+          | Obrigatório para a loja de mimos         |
| Node.js (servidor) | 16+           | Para o servidor WebSocket externo        |
| Nginx              | qualquer      | Reverse proxy com SSL para o WebSocket   |
| Composer           | qualquer      | Opcional; só para OpenCage geocoder      |

---

## Ambiente Local

Path no Local Sites: `C:\Users\willi\Local Sites\uailove\app\public\wp-content\themes\uailove\`

Variáveis de ambiente configuradas via constantes no `wp-config.php`, lidas pelo `EnvService`.