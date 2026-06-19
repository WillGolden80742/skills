---
name: trokapay
description: Tema WordPress MoedaDeTroka/Trokapay — marketplace de permutas com WooCommerce, WhatsApp integrado, sistema de comissões e indicações.
triggers: ["trokapay", "moeda de troka", "moedadetroka", "tema marketplace", "wordpress marketplace", "ofertas", "permutas", "whatsapp woocommerce", "woocommerce troca", "marketplace permuta", "comissao", "indicacao", "afiliado", "voucher", "transacao", "cheque especial", "overdraft", "price split", "saldo pl", "moeda interna", "criar oferta", "produto troca", "associado", "empresa parceira", "uazapi trokapay", "whatsapp oferta", "cptfactory", "woocommerce personalizado", "rest api trokapay", "shortcode oferta", "wordpress trokapay", "tema trokapay", "permuta online", "negocio troca", "promotor"]
---

## Arquitetura

O tema usa namespace global (sem PSR-4) com carregamento via `require_once` no `functions.php`. Backend PHP 7.4+ sobre WordPress 5.4+. Frontend tradicional WordPress com templates PHP e shortcodes. Integração com servidor Node.js externo para disparo de mensagens WhatsApp. API REST customizada e factories para CPTs e meta boxes de forma declarativa.

---

## Estrutura de Arquivos

```
wp-content/themes/trokapay/
├── functions.php              ← ponto de entrada real (carrega tudo via require_once)
├── style.css                  ← Theme Name: MoedaDeTroka
├── header.php                 ← Open Graph + args dinâmicos
├── footer.php                 ← MDI icons, banner
├── 404.php, index.php, page.php, single.php, archive.php, search.php, etc.
├── acesso.php                 ← Template: Acesso (Minha Conta WooCommerce)
├── associate.php              ← Template: Associado
├── associates.php             ← Template: Associados
├── associates-new.php         ← Template: Novo Associados
├── buy-offer.php              ← Template: Buy Offer
├── central_de_ofertas.php     ← Template: Central De Ofertas
├── criar-oferta.php           ← Template: Cria Oferta
├── editar-oferta.php          ← Template: Editar Oferta
├── extrato.php                ← Template: Extrato
├── commission.php             ← Template: Comission (cálculo de comissões)
├── login.php                  ← Template personalizado de login
├── preferences.php            ← Popup de preferências/categorias
├── products.php               ← Listagem de produtos
├── painel.php, relatorios.php, goais.php, questionnaire.php, whatsapp_bot.php
├── cptfactory2.php            ← CPTFactory_3 - fábrica de custom post types
├── mu_factory.php             ← UserMetaFactory - fábrica de meta boxes de usuário
├── produto_status.php         ← Utilitário de status de produtos
├── preferred_categories.php   ← Lógica de categorias preferidas
├── api/
│   ├── custom-post-type/
│   │   ├── CPTFactory.php     ← Classe CPTFactory (factory para CPTs)
│   │   └── Instances.php      ← Registro de CPTs: transaction, voucher + taxonomias
│   ├── custom-user-type/
│   │   ├── Instances.php      ← Meta boxes de usuário: dados da empresa, financeiro
│   │   └── save_preferences.php
│   ├── endpoints/
│   │   ├── EndPointsFactory.php ← Factory de endpoints REST
│   │   ├── Instances.php      ← Registro de rotas: /profiles, /offers, /vouchers, /transactions
│   │   └── migration_api.php
│   ├── shortcodes/
│   │   ├── shortcode.php      ← Classe Shortcode (carrosséis, ofertas, formulários)
│   │   └── CWP_Query.php      ← Query builder para shortcodes
│   ├── WooCommerce/
│   │   └── Instances.php      ← Lógica de overdraft, transações, comissões, checkout
│   ├── js/                    ← JS do frontend (ofertas.js, trokapay-core.js, etc.)
│   └── css/                   ← CSS do frontend
├── inc/                       ← Arquivos Underscores (custom-header, template-tags, etc.)
├── js/                        ← navigation.js
├── css/                       ← Estilos adicionais
├── images/                    ← Imagens do tema (banner.png, ícones, etc.)
├── template-parts/            ← Partes de template WordPress
└── languages/                 ← Traduções
```

---

## Fluxo de Inicialização

```
functions.php
  ├── define('_S_VERSION', current_time('timestamp'))
  ├── api/custom-post-type/Instances.php   ← CPTs: transaction, voucher; taxonomias
  ├── produto_status.php                   ← AJAX para status de produtos
  ├── api/endpoints/Instances.php          ← REST API (só se logado)
  ├── cptfactory2.php                      ← CPTFactory_3
  ├── mu_factory.php                       ← UserMetaFactory
  ├── api/shortcodes/shortcode.php         ← Classe Shortcode
  ├── api/custom-user-type/Instances.php   ← Meta boxes de usuário
  ├── api/WooCommerce/Instances.php        ← Integração WooCommerce
  ├── trokapay_setup()                     ← add_action('after_setup_theme')
  │     ├── load_theme_textdomain
  │     ├── add_theme_support (title-tag, post-thumbnails, html5, custom-logo…)
  │     └── register_nav_menus
  ├── trokapay_widgets_init()              ← add_action('widgets_init')
  └── inc/ (custom-header, template-tags, template-functions, customizer, jetpack)
```

---

## Theme Info

| Propriedade     | Valor                      |
|-----------------|----------------------------|
| Theme Name      | MoedaDeTroka               |
| Text Domain     | moedadetroka, trokapay     |
| Versão          | 1.0.0                      |
| PHP mínimo      | 5.6+ (recomendado 7.4+)    |
| Base            | Underscores (_s)           |
| WooCommerce     | 5.0+ (obrigatório)         |

---

## Custom Post Types

Registrados via `CPTFactory` + `CPTFactory_3`:

| CPT            | Descrição                                    |
|----------------|----------------------------------------------|
| `transaction`  | Transações entre comprador/vendedor          |
| `voucher`      | Vouchers de crédito                          |
| `product`      | Produto WooCommerce (renomeado para "Oferta")|
| `question`     | Perguntas e Respostas (CPT do shortcode `[questions]`) |
| `used_commission` | Registro de uso de comissão por promotor  |

**Taxonomias customizadas (associadas a `product`):**

| Taxonomy                           | Descrição               |
|------------------------------------|-------------------------|
| `offer_type_category`              | Tipo de oferta          |
| `offer_class_category`             | Classe de oferta        |
| `offer_product_condition_category` | Condição do produto     |

**Taxonomias (associadas a `product_tag`):**
- Tags com prefixo `porcentagem_` (ex: `porcentagem_50`) definem a divisão de preço entre PL$ e R$

---

## User Meta Fields

Todos os campos de usuário registrados em `api/custom-user-type/Instances.php`. Salvos via formulário de perfil ou AJAX (`trokapay_save_user`).

**Dados da Empresa:**
| Meta Key | Descrição | Tipo |
|---|---|---|
| `company_name` | Nome da empresa | text |
| `company_cnpj` | CNPJ/CPF | text |
| `company_ie` | Inscrição Estadual | text |
| `company_address_street` | Logradouro | text |
| `company_address_number` | Número | text |
| `company_address_complement` | Complemento | text |
| `company_address_neighborhood` | Bairro | text |
| `company_address_city` | Cidade | text |
| `company_address_state` | Estado | text |
| `company_address_zip` | CEP | text |
| `company_address_country` | País | text |
| `company_phone` | Telefone | text |
| `company_website` | Website | url |
| `company_responsible` | Responsável | text |
| `company_logo` | Logotipo (attachment ID) | int |
| `company_description` | Descrição da empresa | textarea |
| `company_category` | Ramo de Atividade (term_id de `product_cat`) | int |
| `company_slide_image` | Imagem para o Slide (attachment ID) | int |
| `company_photos` | Fotos da empresa (array de URLs) | array |
| `company_videos` | Vídeos da empresa (array de URLs) | array |
| `company_instagram` | Instagram | url |
| `company_facebook` | Facebook | url |
| `company_youtube` | YouTube | url |
| `company_tiktok` | TikTok | url |
| `company_latitude` | Latitude (geocoding) | float |
| `company_longitude` | Longitude (geocoding) | float |
| `company_address_state` | Estado (endereço) | text |
| `selected_company_section` | Seção selecionada (`Empresas & Serviços`, `Mercado Feminino`, `Bares & Restaurantes`, `Hoteis & Turismo`) | text |

**Financeiro / Saldos:**
| Meta Key | Descrição | Tipo |
|---|---|---|
| `legal_subjects` | Tipo de Pessoa (`cpf`/`cnpj`) | text |
| `currency_balance` | Saldo em PL$ (moeda interna) | float |
| `brl_balance` | Saldo em R$ | float |
| `overdraft` | Saldo do Cheque Especial | float |
| `custom_cheque_especial` | Limite Cheque Especial Customizado | float |
| `price_split` | Porcentagem de preço em PL$ | float |
| `purchase_tax` | Taxa de Compra (%) | float |
| `commission` | Comissão (%) | float |
| `commission_brl` | Comissão BRL | float |
| `promoter_brl_commission` | Comissão BRL para Promotores (%) | float |

**Controles:**
| Meta Key | Descrição | Tipo |
|---|---|---|
| `is_promoter` | É Promotor? (`1`/`0`) | bool |
| `selling_restriction` | Restrição de Venda (`Sim`/`Não`) | text |
| `buying_restriction` | Restrição de Compra (`Sim`/`Não`) | text |
| `aceita_migracao` | Status de Migração (`0`=perguntar, `1`=aceita, `2`=não perguntar mais) | text |
| `migracao_finalizada` | Migração Finalizada? (`true`/`false`) | bool |
| `reset_finalizado` | Reset Finalizado? (`true`/`false`) | bool |
| `new_associated_notified` | Notificação de associado enviada? (`1`/`0`) | bool |

**Indicação / Referral:**
| Meta Key | Descrição | Tipo |
|---|---|---|
| `referral_code` | Código de Indicação único | text |
| `referred_by` | Indicado por (user ID) | int |
| `meta_author` | Autor do meta (user ID do criador) | int |

**Preferências / Notificações:**
| Meta Key | Descrição | Tipo |
|---|---|---|
| `preferred_categories` | Categorias preferidas (JSON array de IDs) | text |
| `last_preferences_set` | Timestamp da última definição de preferências | int |
| `times_preferences_set` | Vezes que preferências foram definidas | int |
| `times_preferences_prompted` | Vezes que o popup de preferências foi exibido | int |
| `skip_preferences_permanently` | Pular preferências permanentemente (`true`/`false`) | bool |
| `notify_email` | Notificar por email (`1`/`0`) | bool |
| `notify_whatsapp` | Notificar por WhatsApp (`1`/`0`) | bool |

**WooCommerce / Último Acesso:**
| Meta Key | Descrição |
|---|---|
| `wc_last_active` | Timestamp do último acesso (WooCommerce) |
| `wfls-last-login` | Timestamp do último login (Wordfence) |

---

## Post Meta Fields

Campos registrados em `api/custom-post-type/Instances.php` via meta boxes.

**Product (Oferta) — Meta Box "Informações da Oferta":**
| Meta Key | Descrição | Tipo |
|---|---|---|
| `title` | Título da oferta | text |
| `price` | Preço em PL$ | float |
| `quantity` | Quantidade em estoque | int |
| `offer_permanence_date` | Data de Expiração | date |
| `description` | Descrição da oferta | textarea |
| `keywords` | Palavras-chave | text |
| `new_tag` | Nova Tag | text |
| `image_0` | URL da imagem 0 | url |
| `image_1` | URL da imagem 1 | url |
| `image_2` | URL da imagem 2 | url |
| `image_3` | URL da imagem 3 | url |
| `offer_type` | Tipo de Oferta (`buy`/`sell`) | text |
| `disclosure` | Divulgação (`public`/`targeted`) | text |
| `recipient` | Destinatário (user ID, oferta direcionada) | int |
| `youtube_video_url` | URL do vídeo YouTube | url |
| `service_location` | Local de Atendimento (`in_company`/`at_home`) | text |
| `availability_option` | Disponibilidade (`ready_delivery`/`consult_schedule`) | text |
| `buy_without_consulting` | Comprar sem Consultar (`1`/`0`) | bool |
| `pickup_location` | Local de retirada | text |
| `expiration_date` | Data de validade | date |
| `proto_cat` | Categoria protocolar | text |
| `buy_limit` | Limite de compra | int |

**Voucher — Meta Box "Informações do Voucher":**
| Meta Key | Descrição | Tipo |
|---|---|---|
| `code` | Código do voucher | text |
| `amount` | Valor do voucher | float |
| `status` | Status (`resgatado`/`pendente`/`expirado`) | text |

**Transaction — Meta Box "Detalhes da Transação":**
| Meta Key | Descrição | Tipo |
|---|---|---|
| `order_id` | ID do Pedido WooCommerce | int |
| `buyer_id` | ID do comprador | int |
| `seller_id` | ID do vendedor | int |
| `amount` | Valor da transação | float |
| `product_id` | ID do produto | int |
| `status` | Status (`Concluído`/`Reembolsado`/`Pendente`) | text |
| `timestamp` | Data e hora (YYYY-MM-DD HH:MM:SS) | text |
| `comission_rate_brl` | Taxa de Comissão BRL (%) | float |
| `is_promoter` | Envolve promotor? | text |
| `product_tax_id` | ID da taxa do produto | int |
| `commission_rate_brl` | Taxa de comissão BRL | float |
| `_questionnaire_token_buyer_eval_seller` | Token do questionário comprador-avalia-vendedor | text |
| `_questionnaire_token_seller_eval_buyer` | Token do questionário vendedor-avalia-comprador | text |

**Question (Perguntas) — CPT do shortcode `[questions]`:**
| Meta Key | Descrição | Tipo |
|---|---|---|
| `target_user_id` | ID do usuário alvo da pergunta | int |
| `upvotes` | Contagem de votos positivos | int |
| `downvotes` | Contagem de votos negativos | int |
| `user_votes` | Array de votos por usuário (`[user_id => 'upvote'/'downvote']`) | array |
| `answers` | Array de respostas (`[{content, author_id, date}]`) | array |

**Used Commission — CPT de uso de comissão:**
| Meta Key | Descrição | Tipo |
|---|---|---|
| `user_id` | ID do promotor | int |
| `amount_used` | Valor da comissão utilizada | float |
| `order_status` | Status do pedido (`pending`/`completed`) | text |
| `related_order_id` | ID do pedido relacionado | int |

---

## REST API

Registrada via `EndPointsFactory` (namespace `/api/v1`) e manualmente (namespace `trokapay/v1`).

**Namespace `/api/v1` (via factory):**

| Rota            | Methods                          | Post Type      |
|-----------------|----------------------------------|----------------|
| `/profiles`     | GET, POST, PUT, DELETE           | profile        |
| `/offers`       | GET, POST, PUT, DELETE           | product        |
| `/vouchers`     | GET, POST, PUT, DELETE           | voucher        |
| `/transactions` | GET, POST                        | transaction    |

**Namespace `trokapay/v1` (endpoints manuais):**

- `GET /autores-sem-produtos` — clientes sem produtos publicados
- `GET /autores-sem-produtos-cheque` — clientes sem produtos com cheque especial
- `GET /autores-referencias` — dados de indicações
- `GET /sellers-with-orders` — vendedores com pedidos
- `GET /buyers-with-orders` — compradores com pedidos
- `GET /clientes-sem-compras-ou-vendas` — clientes inativos
- `GET /clientes-produtos-sem-thumbnail` — produtos sem imagem
- `GET /clientes-sem-login` — clientes que nunca logaram
- `GET /orders-processing-month` — pedidos em processamento no mês
- `GET /vendedores-sem-vendas` — vendedores sem vendas concluídas
- `GET /products/authors` — autores de produtos
- `POST /send-whatsapp-offer` — envia oferta via WhatsApp
- `POST /test-sales-notification` — testa notificação de venda (admin only)
- `GET /associated/v1/companies/` — empresas associadas
- `GET /custom/v1/get-all-customers/` — lista de clientes
- `POST /custom/v1/create-product/` — cria produto temporário

---

## AJAX Actions

Prefixo: `trokapay_` e `produto_status_`. Protegidas por `wp_ajax_{action}`.

- `trokapay_trigger_send_offers` — dispara envio de ofertas via WhatsApp
- `trokapay_update_user_preference_meta` — atualiza meta de preferências
- `trokapay_update_user_meta_ajax_handler` — handler genérico de meta
- `update_company_info` — atualiza dados da empresa (com upload de fotos/vídeos)
- `produto_status_update_all_products` — força estoque de todos os produtos
- `get_last_product_timestamp` — timestamp do último produto
- `get_category_tree_metadata` — metadata da árvore de categorias

---

## WhatsApp Integration

O tema envia ofertas e notificações via WhatsApp através de um servidor Node.js externo:

**Servidor Node.js:** `http://62.146.170.173:3000/`

**Endpoints do servidor:**
- `POST /new-product` — publica oferta em grupo WhatsApp
- `POST /send-individual-offer` — envia oferta individual

**API Key:** `VCnJB3U52AfnTewHEnY1xT49zgUHpSIz`

**Integração WhatsApp (UAZAPI):**
- `POST /wp-json/uazapi-integration/v1/send-order-payment-custom` — envio de mensagens customizadas

**Fluxo:** Produto criado → Node.js envia para grupo WhatsApp → notificação por email e WhatsApp individual para destinatários (se oferta direcionada) ou para usuários com preferências compatíveis.

---

## WooCommerce Integration

- Produtos renomeados para "Ofertas"
- Checkout customizado com sistema de crédito (currency_balance) e cheque especial (overdraft)
- Comissões por tipo de usuário (CNPJ, CPF, Promotor)
- Taxa de compra configurável (mínimo R$7.50)
- Criação automática de transação (CPT `transaction`) ao finalizar pedido
- Restrições de compra/venda por usuário
- Pedidos em status "processing" como referência principal
- **Price Split:** divisão de preço entre PL$ e R$ via tags `porcentagem_X`
- **Comissão Promotor:** carrinho zerado quando promotor usa comissão para pagar taxa (`pay_tax_with_comission=1`)
- **Notificação Vendedor:** WhatsApp automático ao vendedor quando pedido vai para "processing"
- **Modal de Avaliação:** modal flutuante após compra para avaliar produto/vendedor (1-5 estrelas, opção "produto não chegou")
- **Avaliações:** sistema de reviews com `trokapay_seller_comments` e `company_rating`
- **Ofertas Aceitas:** meta `_wpcp_accepted_product_offers` para preços customizados por usuário

---

## Admin Pages

Registradas via `add_menu_page` / `add_options_page`:

| Menu | Slug | Descrição | Fonte |
|---|---|---|---|
| Regras de Negócio | `trokapay-business-rules` | Configurações globais de comissão, taxa, overdraft | `api/custom-post-type/Instances.php` |
| Envio de Ofertas | `trokapay-enviar-ofertas` | Disparo de ofertas via WhatsApp | `enviar_novas_ofertas.php` |
| Conteúdo Dinâmico - Criação de Oferta | `oferta-dinamica-settings` | Vídeo tutorial e banners rotativos | `functions.php` |
| Slider da Empresa | `company-slider-configuracoes` | Banners e vídeo do slider | `functions.php` |
| Avaliações MoedaDeTroka | `mdts-seller-reviews` | Gerenciador de avaliações de vendedores | Snippet 35013 |
| Usuários sem produtos | `usuarios-sem-produtos` | Lista e exporta CSV de usuários sem produtos | Snippet 150261 |
| Uazapi Config | `uazapi-config` | Configuração de tokens Uazapi (WhatsApp API), QR Code, status, logs | Snippet 24756 |

---

## Regras de Negócio

Configuradas via admin em "Regras de Negócio" (`trokapay-business-rules`):

| Configuração                     | Descrição                              |
|----------------------------------|----------------------------------------|
| `default_overdraft_cnpj`         | Cheque especial padrão (CNPJ)          |
| `default_overdraft_cpf`          | Cheque especial padrão (CPF)           |
| `default_overdraft_promoter`     | Cheque especial padrão (Promotor)      |
| `default_purchase_tax`           | Taxa de compra (%)                     |
| `default_commission_cnpj`        | Comissão padrão CNPJ (%)               |
| `default_commission_promoter`    | Comissão padrão Promotor (%)           |
| `default_commission_cpf`         | Comissão padrão CPF (%)                |
| `default_promoter_brl_commission`| Comissão BRL Promotor (%)              |

---

## Frontend

Tema tradicional WordPress (não é SPA). Templates PHP na raiz + shortcodes.

**Dependências CSS:**
- Font Awesome 5.15.4
- Material Design Icons (MDI) 6.5.95
- Slick Carousel 1.8.1
- Google Fonts: Montserrat

**Dependências JS:**
- jQuery (nativo WordPress)
- Slick Carousel
- Scripts custom em `api/js/`: `trokapay-core.js`, `ofertas.js`, `associados.js`, `ajax-search.js`, `single-offer.js`, `config-users.js`, `admin-users.js`, `associated-ajax-search.js`, `trokapay-media-uploader.js`

**Shortcodes principais (classe `Shortcode`):**
- `[offersForm]` — formulário de criação/edição de oferta
- `[offer_container]` — container de listagem de ofertas
- `[novo_associados]` — listagem de associados
- `[minha_conta user_id='X']` — conta de associado
- `[extrato_transacoes]` — extrato de transações
- `[total_media_block]` — bloco de mídia do total
- `[affiliate_panel]` — painel de afiliado
- `[render_buy_offer_page]` — página de compra de oferta

**Mapas:** OpenStreetMap (Nominatim) para geocoding via `update_company_info` AJAX.

---

## WPCode Snippets (Plugin WPCode)

O site usa o plugin **WPCode** para injetar snippets PHP/HTML sem editar o tema. Arquivos em `wp-content/uploads/wpcode-snippets/`.

**Snippets ativos identificados:**

| Snippet ID | Tipo | Descrição |
|---|---|---|
| 23907 | HTML | Logout link fix: copia href do "Sair" para `.logout_link`, remove item de menu original, remove `.product_cat_and_sub` |
| 192804 | PHP | Comissão promotor (`getCommission`), carrinho zerado com comissão (`add_custom_price_promoter`), `used_commission` CPT update |
| 18675 | HTML | Botão de compartilhar produto via WhatsApp com referral |
| 20272 | PHP | Campo `contrato_moedadetroka` (URL) no perfil do usuário |
| 131242 | PHP | Shortcode `[questions]` — CPT `question`, perguntas/respostas com votação, edição, exclusão, paginação AJAX |
| 116143 | PHP | Propaga `is_admin=true` na URL para links internos |
| 18674 | PHP | `sanitize_file_name` → `mb_strtolower` (nomes de arquivo em minúsculas) |
| 23933 | HTML | Substitui `wp-login.php` → `/acesso/` em todos os links/forms via MutationObserver |
| 150261 | PHP | Admin page "Usuários sem produtos" com filtro e exportação CSV |
| 35013 | PHP | `MdtSrmPlugin` — Gerenciador de Avaliações de Vendedores (admin page com filtros por estrelas) |
| 18679 | PHP | `trokapay_send_seller_sales_notification` — WhatsApp ao vendedor quando pedido vai para "processing" |
| 31145 | PHP | Shortcode `[products_search_form]` — busca com filtro hierárquico de categorias (envia para `/ofertas/`) |
| 18677 | PHP | `MoedaDeTrokaRatingModal` — Modal flutuante de avaliação de pedido após compra |
| 42796 | HTML | Esconde admin bar/menu se `origin=by-iframe` na URL |
| 24756 | PHP | `Uazapi_Integration_Pro` — Integração completa com Uazapi (WhatsApp API), gerenciamento de chaves, logs CPT `uazapi_log`, REST API |

**Uazapi Integration Pro (Snippet 24756):**

Classe `Uazapi_Integration_Pro` — substitui o servidor Node.js externo por integração direta via REST API com Uazapi (WhatsApp Business API).

**Admin Menu:** "Uazapi Config" (slug: `uazapi-config`, ícone: `dashicons-whatsapp`, posição: 6)

**Configurações:**
- `uazapi_tokens_data` — array de tokens (nome, token, instance_url), suporta múltiplas instâncias
- `server_api_key` — chave de servidor para proteger endpoints REST

**REST API Endpoints (namespace `uazapi-integration/v1` e variantes por token):**

| Endpoint | Method | Descrição |
|---|---|---|
| `/new-product` | POST | Publica oferta em grupo WhatsApp (por estado ou website) |
| `/new-associated` | POST | Anuncia novo associado no grupo do estado |
| `/send-oferta-message` | POST | Envia imagem/carrossel para grupo |
| `/send-individual-offer` | POST | Envia oferta individual para número |
| `/send-order-payment-custom` | POST | Mensagem customizada individual |
| `/send-bulk-message` | POST | Mensagem em massa |
| `/send-carousel` | POST | Carrossel de imagens |
| `/genericMsg` | POST | Mensagem genérica polimórfica |
| `/get-group-chats` | GET | Lista grupos WhatsApp |
| `/get-chats` | GET | Lista todos os chats |
| `/status` | GET | Status da sessão WhatsApp |
| `/get-qr-code` | GET | QR Code para autenticação |
| `/start-session` | POST | Inicia sessão WhatsApp |
| `/logout-session` | POST | Encerra sessão WhatsApp |
| `/internal/logs` | GET | Logs internos (admin only) |

**Grupos WhatsApp por estado:**
| Estado | Group ID |
|---|---|
| MG | `120363353535224745@g.us` |
| GO | `120363400016557055@g.us` |
| ES | `120363400175569938@g.us` |
| SP | `120363418341809947@g.us` |
| RJ | `120363399681997024@g.us` |
| MOEDA | `120363403250053293@g.us` |

**Grupos especiais:**
| Grupo | Group ID |
|---|---|
| Portal Estética | `120363417086654231@g.us` |
| TrokaTudo Permutas | `120363398727709275@g.us` |
| Brechó Trokapay | `120363417086654231@g.us` |

**Tipos de mensagem Uazapi suportados:**
- Texto com link preview
- Mídia (imagem, vídeo, áudio, documento)
- Contato (vCard)
- Localização
- Menu interativo (buttons, list, poll)
- Carrossel
- Solicitação de pagamento
- Botão PIX
- Botão de solicitação de localização

**CPT adicional:**
| CPT | Descrição |
|---|---|
| `uazapi_log` | Logs de eventos da integração Uazapi (não público, sem UI) |

**Funções-chave dos snippets:**

- `getCommission($promoter_id, $applyTax, $applyCommissionUse, $month, $year)` — calcula comissão líquida de promotor
- `intendToUseCommission($promoterID, $status)` — verifica intenção de uso de comissão pendente (últimos 2 min)
- `add_custom_price($cart)` — aplica taxa de compra no carrinho (mínimo R$7.50)
- `add_custom_price_promoter($cart)` — zera carrinho se promotor pagou taxa com comissão
- `update_used_commission_on_order_status_change($order_id)` — atualiza CPT `used_commission` ao mudar status do pedido
- `trokapay_register_question_cpt()` — registra CPT `question`
- `render_questions_shortcode($atts)` — shortcode `[questions user_id="X" posts_per_page="10"]`
- `trokapay_get_user_avatar_url($user_id, $size)` — avatar via `company_logo` ou Gravatar
- `trokapay_send_seller_sales_notification($order_id)` — notifica vendedor via WhatsApp
- `trokapay_send_whatsapp_message_to_individual($phone, $message, $image_url)` — helper WhatsApp individual
- `ContratoMoedaTrokaUserMeta` — classe que adiciona campo `contrato_moedadetroka` no perfil
- `MdtSrmPlugin` — gerenciador de avaliações (admin page "Avaliações MoedaDeTroka")
- `MoedaDeTrokaRatingModal` — modal de avaliação de pedido (rating 1-5 estrelas, "produto não chegou")

**AJAX dos snippets:**

- `trokapay_load_questions` — carrega perguntas (paginação AJAX)
- `trokapay_submit_question` — envia nova pergunta
- `trokapay_vote_question` — upvote/downvote em pergunta
- `trokapay_submit_answer` — envia resposta
- `trokapay_edit_answer` — edita resposta
- `trokapay_delete_question` — exclui pergunta
- `trokapay_delete_answer` — exclui resposta
- `trokapay_load_single_question` — carrega dados de uma pergunta específica
- `moedadetroka_get_last_unrated_order` — busca último pedido não avaliado
- `moedadetroka_submit_rating` — submete avaliação de pedido
- `moedadetroka_mark_not_arrived` — marca produto como "não chegou"
- `moedadetroka_modal_closed` — registra fechamento do modal
- `mdts_srm_clear_modal_meta` — limpa meta de fechamento do modal (admin)

**Shortcodes adicionais (WPCode):**

- `[products_search_form]` — formulário de busca com filtro de categorias (envia para `/ofertas/`)
- `[questions user_id="X" posts_per_page="10"]` — perguntas e respostas

---

## User Meta Fields Adicionais (WPCode Snippets)

Campos adicionados via snippets WPCode (além dos já listados em `custom-user-type/Instances.php`):

| Meta Key | Descrição | Tipo | Fonte |
|---|---|---|---|
| `contrato_moedadetroka` | URL do contrato Moeda Troka | url | Snippet 20272 |
| `trokapay_seller_comments` | Avaliações recebidas (array de comentários) | array | Snippet 35013 |
| `company_rating` | Nota média do vendedor (1-5) | float | Snippet 35013 |
| `_trokapay_last_modal_closed` | Timestamp do último fechamento do modal de avaliação | int | Snippet 18677 |
| `_wpcp_accepted_product_offers` | Ofertas aceitas por produto (preço customizado) | array | Snippet 192804 |
| `one_star` | Contagem de avaliações 1 estrela recebidas | int | Snippet 18677 |

**Order Item Meta (woocommerce_order_itemmeta):**

| Meta Key | Descrição |
|---|---|
| `_trokapay_item_is_arrived` | Status de chegada do produto ("chegou"/"não chegou") |

---

## Criptomoeda Interna

O tema possui sistema de moeda própria ("PL$") armazenada em `currency_balance` (user meta). Transações comerciais usam esse saldo + cheque especial (overdraft). Comissões e taxas são descontadas em cada transação.

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

Linting PHP: `phpcs` com ruleset `WordPress` + `WPThemeReview` via Composer.

---

## Convenções

Classes em `PascalCase`, métodos em `camelCase`, arquivos PHP em `kebab-case.php` (ex: `criar-oferta.php`), arquivos JS em `kebab-case.js` (ex: `trokapay-core.js`). Prefixo AJAX: `trokapay_`. Prefixo REST: `trokapay/v1` e `api/v1`. Text domain: `trokapay` e `moedadetroka` (legado). Meta boxes registrados via `UserMetaFactory` e `CPTFactory`.

---

## Segurança

Autenticação via WordPress nativo (`is_user_logged_in()`). AJAX protegido por `wp_ajax_{action}` + nonce verification. REST API endpoints públicos (alguns sem `permission_callback` — cuidado). CSRF via nonce WordPress. Upload de arquivos validado por tipo e tamanho.

---

## Requisitos

| Requisito          | Versão mínima | Observação                                    |
|--------------------|---------------|-----------------------------------------------|
| PHP                | 7.4+          |                                               |
| WordPress          | 5.4+          |                                               |
| WooCommerce        | 5.0+          | Obrigatório                                   |
| Node.js (servidor) | 16+           | Para envio de WhatsApp                        |
| Composer           | qualquer      | Para ferramentas de linting PHP               |

---

## Ambiente Local

Path no servidor: `/wp-content/themes/trokapay/`

Domínios conhecidos: `sac.moedadetroka.com.br`, `plataforma.trokapay.com.br`

Variáveis de ambiente: não usa `.env` — configurações via `wp-config.php` e Options API.
