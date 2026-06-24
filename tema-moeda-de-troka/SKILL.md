---
name: tema-moeda-de-troka
description: Tema WordPress MoedaDeTroka — marketplace de permutas com WooCommerce, WhatsApp integrado, sistema de comissões e indicações. Inclui snippets locais, PL$ como moeda interna, e integração Uazapi.
level: A
version: 2.0
intelligence: maximum
tags: ["wordpress-theme", "marketplace", "woocommerce", "whatsapp", "ecommerce", "barter", "cryptocurrency", "pl-currency", "commissions", "affiliate", "uazapi", "rest-api", "financial", "multi-currency", "escrow", "anti-fraud", "tax-compliance", "lgpd", "brazil"]
triggers: ["moeda de troka", "moedadetroka", "tema marketplace", "wordpress marketplace", "ofertas", "permutas", "whatsapp woocommerce", "woocommerce troca", "marketplace permuta", "comissao", "indicacao", "afiliado", "voucher", "transacao", "cheque especial", "overdraft", "price split", "saldo pl", "moeda interna", "criar oferta", "produto troca", "associado", "empresa parceira", "uazapi", "whatsapp oferta", "cptfactory", "woocommerce personalizado", "rest api moedadetroka", "shortcode oferta", "wordpress trokapay", "trokapay", "permuta online", "pl$", "trokaui", "marketplace brasil", "ecommerce troca", "voucher trokapay", "comissao promotor", "estorno", "reembolso", "transacao financeira", "saldo usuario", "cartao credito", "boleto", "pix", "pagamento", "gateway", "antifraude", "reconciliacao", "disputa", "escrow", "nf-e", "nota fiscal", "lgpd privacidade", "cache produto", "elasticsearch", "email marketing", "sms fallback", "backup financeiro"]
---

## Arquitetura

O tema usa namespace global (sem PSR-4) com carregamento via `require_once` no `functions.php`. Backend PHP 7.4+ sobre WordPress 5.4+. Frontend tradicional WordPress com templates PHP e shortcodes. Sistema de snippets locais em `snippets/` que substitui WPCode. Integração com servidor Node.js externo para WhatsApp e REST API Uazapi. API REST customizada + factories para CPTs e meta boxes de forma declarativa. Cache distribuído via `TrokaPay Cache Manager` (snippet 22219).

```
┌─────────────────────────────────────────────┐
│              Load Balancer/CDN              │
│          (Cloudflare / BunnyCDN)            │
└──────────┬──────────────────────┬───────────┘
           │                      │
    ┌──────▼──────┐        ┌─────▼──────┐
    │ WordPress   │        │  Node.js   │
    │ (PHP 7.4+)  │        │  WhatsApp  │
    │ + MySQL     │        │  Server    │
    └──────┬──────┘        └─────┬──────┘
           │                     │
    ┌──────▼─────────────────────▼──┐
    │         Redis Cache           │
    │  (produtos, sessões, filas)   │
    └───────────────────────────────┘
```

---

## Estrutura de Arquivos

```
wp-content/themes/moedadetroka/
├── functions.php                ← Ponto de entrada
├── style.css
├── header.php, footer.php
├── 404.php, index.php, page.php, single.php, archive.php, search.php
├── acesso.php                   ← Minha Conta WooCommerce
├── associate.php                ← Associado
├── associates.php               ← Associados
├── associates-new.php           ← Novo Associado
├── buy-offer.php                ← Buy Offer
├── central_de_ofertas.php       ← Central de Ofertas
├── criar-oferta.php             ← Criar Oferta
├── editar-oferta.php            ← Editar Oferta
├── extrato.php                  ← Extrato
├── commission.php               ← Comissões
├── login.php                    ← Login personalizado
├── preferences.php              ← Preferências/Categorias
├── products.php                 ← Listagem de produtos
├── painel.php, relatorios.php, goais.php
├── questionnaire.php, whatsapp_bot.php
├── bot-images.php
├── produto_status.php
├── preferred_categories.php
├── cptscaffold.php
├── mu_factory.php
├── snippets/
│   ├── loader.php               ← Carregador de snippets
│   ├── index.php                ← Índice de snippets ativos
│   └── [80+ snippets]/
├── api/
│   ├── custom-post-type/
│   ├── custom-user-type/
│   ├── endpoints/
│   ├── shortcodes/
│   ├── WooCommerce/
│   ├── payments/                 ← NOVO: Gateways + antifraude
│   ├── reports/                  ← NOVO: Relatórios financeiros
│   ├── compliance/              ← NOVO: LGPD + NF-e
│   ├── cache/                   ← NOVO: Cache strategy
│   ├── search/                  ← NOVO: Elasticsearch integration
│   ├── notifications/           ← NOVO: Email + SMS
│   ├── js/
│   └── css/
├── inc/
├── js/
├── css/
├── images/
├── template-parts/
└── languages/
```

---

## Fluxo de Inicialização

```
functions.php
  ├── define('_S_VERSION', current_time('timestamp'))
  ├── define('MT_CACHE_ENABLED', true)              ← Cache global
  ├── define('MT_RATE_LIMIT', 60)                   ← REST rate limit
  ├── define('MT_ELASTICSEARCH_HOST', 'localhost:9200')
  ├── api/custom-post-type/Instances.php
  ├── api/endpoints/Instances.php
  ├── cptscaffold.php
  ├── mu_factory.php
  ├── api/cache/CacheManager.php                    ← Cache layer
  ├── api/search/SearchManager.php                  ← Elasticsearch
  ├── api/payments/PaymentGateway.php               ← Gateways
  ├── api/payments/AntiFraud.php                    ← Antifraude
  ├── api/payments/EscrowService.php                ← Escrow
  ├── api/payments/ReconciliationService.php        ← Reconciliação
  ├── api/compliance/TaxService.php                 ← NF-e/DAS
  ├── api/compliance/LgpdService.php                ← LGPD
  ├── api/reports/FinancialReports.php              ← Relatórios
  ├── api/notifications/EmailService.php            ← Email marketing
  ├── api/notifications/SmsService.php              ← SMS fallback
  ├── api/WooCommerce/Instances.php
  ├── snippets/loader.php
  ├── moedadetroka_setup()
  └── moedadetroka_widgets_init()
```

---

## Moeda Interna (PL$) — Sistema Financeiro

| Meta Key | Descrição | Tipo | Uso |
|---|---|---|---|
| `currency_balance` | Saldo em PL$ (moeda interna) | float | Trocas entre associados |
| `brl_balance` | Saldo em R$ | float | Taxas e comissões |
| `overdraft` | Saldo do Cheque Especial | float | Limite extra de crédito |
| `custom_cheque_especial` | Limite Cheque Especial Customizado | float | Negociação individual |
| `price_split` | Porcentagem de preço em PL$ | float | Ex: 70% PL$ + 30% R$ |

### Multi-Currency Risk Management

| Risco | Estratégia | Monitoramento |
|-------|------------|---------------|
| Volatilidade PL$ | Lastro em R$ (1 PL$ = R$ 1,00) | Diário |
| Inflação interna | Ajuste trimestral de lastro | Trimestral |
| Fraude de saldo | Audit trail de todas as transações | Tempo real |
| Dupla contagem | Lock otimista + verificação de saldo | Transação |
| Overdraft excessivo | Limite automático por score de crédito | Semanal |

---

## Payment Gateway Integration Patterns

### Arquitetura de Pagamentos

```
Comprador → Checkout WooCommerce
  ├── Saldo PL$ suficiente? → Débito em PL$
  ├── Precisa de R$? → Gateway externo
  │   ├── Cartão de Crédito (Cielo/Rede/Stone)
  │   ├── Boleto (GerenciaNet/PagSeguro)
  │   └── PIX (snippet PLIX 111591)
  └── Price Split? → Divisão automática PL$/R$
      └── Notificação vendedor via WhatsApp
```

### Gateway Adapter Pattern

```php
interface PaymentGatewayInterface {
    public function processPayment($amount, $currency, $paymentData);
    public function refundPayment($transactionId, $amount);
    public function checkStatus($transactionId);
}

class CieloGateway implements PaymentGatewayInterface {
    // Cielo API 3.0
}

class GerenciaNetGateway implements PaymentGatewayInterface {
    // GerenciaNet API
}

// Factory
class PaymentGatewayFactory {
    public static function create($type) {
        return match($type) {
            'cielo' => new CieloGateway(),
            'gerencianet' => new GerenciaNetGateway(),
            'plix' => new PixGateway(),
            default => throw new \Exception("Gateway $type not found"),
        };
    }
}
```

### Gateways Suportados

| Gateway | Meios | Taxa | Status |
|---------|-------|------|--------|
| Cielo | Crédito, Débito | 3.99% | Integrado |
| GerenciaNet | Boleto, PIX | 1.99% | Integrado |
| PLIX (snippet) | PIX direto | 0% | Snippet |
| Stone | Crédito, Débito | 3.49% | Em desenvolvimento |

---

## Anti-Fraud System

### Regras de Fraude

| Regra | Peso | Ação | Gatilho |
|-------|------|------|---------|
| Múltiplas contas mesmo IP | 50 | Flag + revisão manual | 3+ contas |
| Transação valor muito alto | 40 | Hold + verificação | > R$ 10.000 |
| Velocidade de criação de ofertas | 60 | Shadow ban | 10+ ofertas/hora |
| Padrão de login suspeito | 70 | Bloqueio temporário | 5+ logins falhos |
| Dispositivo conhecido como fraudulento | 90 | Bloqueio permanente | Fingerprint match |
| Email recém-criado | 30 | Verificação extra | < 30 dias |
| Telefone não verificado | 25 | Limite de transação | < R$ 500 |
| Endereço geográfico inconsistente | 55 | Hold manual | IP ≠ cadastro |

### Score de Risco

```php
$risk = new AntiFraud();
$score = $risk->evaluate($order_id, $user_id);

if ($score > 80) {
    $risk->blockOrder($order_id, 'high_risk_score');
    $risk->notifyAdmin($order_id, $score);
} elseif ($score > 50) {
    $risk->holdOrder($order_id, 'medium_risk_score');
    $risk->requestVerification($user_id);
}
// score < 50: processa normalmente
```

### Blacklist Compartilhada
```php
// Verifica dispositivos e IPs em blacklist global
$deviceId = $_SERVER['HTTP_USER_AGENT'] . $_SERVER['REMOTE_ADDR'];
$fingerprint = md5($deviceId);
if ($redis->sIsMember('fraud:blacklist:devices', $fingerprint)) {
    $this->blockUser($user_id, 'device_blacklisted');
}
```

---

## Transaction Reconciliation

### Processo Diário de Reconciliação

```
01:00 — Cron job inicia reconciliação
  ├── Carrega transações do dia anterior (WooCommerce orders)
  ├── Compara com registros do CPT `transaction`
  ├── Verifica status no gateway externo
  ├── Identifica discrepâncias:
  │   ├── Pedido pago sem transação → Criar transação
  │   ├── Transação sem pedido → Investigar
  │   ├── Valor diferente → Flag + notificar admin
  │   └── Status inconsistente → Atualizar
  └── Gera relatório de reconciliação
```

### Tabela de Conciliação

```sql
CREATE TABLE IF NOT EXISTS wp_mt_reconciliation (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    reconciliation_date DATE NOT NULL,
    order_id BIGINT UNSIGNED,
    transaction_id BIGINT UNSIGNED,
    expected_amount DECIMAL(15,2),
    actual_amount DECIMAL(15,2),
    gateway_status VARCHAR(50),
    local_status VARCHAR(50),
    discrepancy VARCHAR(255),
    resolved BOOLEAN DEFAULT FALSE,
    resolved_at DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_date (reconciliation_date),
    INDEX idx_resolved (resolved),
    INDEX idx_order (order_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

---

## Escrow System Design

### Fluxo Escrow

```
1. Comprador paga → Valor vai para conta escrow (hold)
2. Vendedor é notificado → Confirma disponibilidade
3. Comprador recebe produto → Marca como "Recebido"
4. Sistema libera pagamento ao vendedor
5. Transação concluída

Disputa:
3a. Comprador abre disputa → Fundos ficam em escrow
3b. Ambas as partes apresentam evidências
3c. Admin/mediação resolve
3d. Liberação parcial ou total
```

### Status Escrow

| Status | Descrição | Ação Possível |
|--------|-----------|---------------|
| `awaiting_payment` | Aguardando pagamento | Cancelar (24h) |
| `in_escrow` | Fundos retidos | Aguardar confirmação |
| `awaiting_delivery` | Pagamento confirmado | Vendedor envia |
| `delivered` | Produto entregue | Comprador confirma |
| `disputed` | Disputa aberta | Mediação |
| `completed` | Liberado ao vendedor | Finalizado |
| `refunded` | Devolvido ao comprador | Reembolso |
| `partial_refund` | Devolução parcial | Acordo |

---

## Dispute Resolution Workflow

```
Disputa Aberta
  ├── Notificação automática para admin + ambas as partes
  ├── Prazo: 7 dias para resolução
  ├── Evidências:
  │   ├── Prints de conversa WhatsApp
  │   ├── Fotos do produto
  │   ├── Comprovante de entrega
  │   └── Histórico de mensagens da plataforma
  ├── Decisões possíveis:
  │   ├── Reembolso total (comprador vence)
  │   ├── Reembolso parcial (acordo)
  │   ├── Liberação ao vendedor (vendedor vence)
  │   └── Ambos perdem (taxa administrativa)
  └── Após decisão:
      ├── Executa liberação/reembolso
      ├── Registra no histórico de confiança
      └── Bloqueia usuário se reincidente
```

---

## Financial Reporting

### Relatórios Disponíveis

| Relatório | Frequência | Formato | Acesso |
|-----------|------------|---------|--------|
| Débito/Crédito diário | Diário | CSV, PDF | Admin |
| Comissões por período | Semanal | CSV, PDF | Admin |
| Extrato de transações | Mensal | CSV, PDF, JSON | Admin + Usuário |
| Relatório fiscal (NF-e) | Mensal | XML (padrão SEFAZ) | Contador |
| DAS (Simples Nacional) | Mensal | PDF | Contador |
| Performance de vendas | Semanal | Dashboard | Admin |
| Taxa de conversão | Mensal | Dashboard | Admin |
| Relatório de estornos | Diário | Dashboard | Admin |
| Custos de gateway | Mensal | CSV | Admin |
| ROI de campanhas | Por campanha | CSV | Marketing |

### Implementação

```php
class FinancialReports {
    public function getDailySummary($date) {
        return [
            'total_sales_pl' => $this->sumPL($date),
            'total_sales_brl' => $this->sumBRL($date),
            'total_commissions' => $this->sumCommissions($date),
            'total_fees' => $this->sumFees($date),
            'total_promoter_commissions' => $this->sumPromoterCommissions($date),
            'new_users' => $this->countNewUsers($date),
            'new_offers' => $this->countNewOffers($date),
            'disputes_opened' => $this->countDisputes($date, 'opened'),
            'disputes_resolved' => $this->countDisputes($date, 'resolved'),
        ];
    }
}
```

---

## Tax Compliance (NF-e / DAS)

### NF-e Integration Flow
```
Pedido faturado → Dados do pedido + empresa
  → API SEFAZ (NF-e)
    ├── Empresa CNPJ → NF-e modelo 55
    ├── Empresa CPF → Nota do Consumidor
    └── Microempreendedor → ISento
  → XML é armazenado no CPT `transaction`
  → DANCE (PDF) é gerado e enviado por email
```

### Cálculo de Impostos

| Tipo | Imposto | Alíquota | Base |
|------|---------|----------|------|
| Simples Nacional | DAS | Variável (anexo I-IV) | Faturamento |
| Lucro Presumido | PIS/COFINS/CSLL/IRPJ | ~11.33% + ISS | Faturamento |
| MEI | Mensal fixo | R$ 67,93 | Fixo |
| CPF | IRPF (venda eventual) | 15% | Ganho de capital |

### Compliance Config
```php
define('MT_TAX_REGIME', 'simples_nacional');
define('MT_SEFAZ_UF', 'MG');
define('MT_SEFAZ_CERT_PATH', '/path/to/cert.pfx');
define('MT_SEFAZ_CERT_PASS', 'cert_password');
define('MT_ISSUE_NFE', true);
```

---

## Audit Trail

### O que é auditado
| Evento | Detalhes | Retenção |
|--------|----------|----------|
| Login/logout | IP, user agent, timestamp | 2 anos |
| Transação financeira | Valor, tipo, status, parties | 5 anos |
| Alteração de saldo | Saldo anterior, novo, delta | 5 anos |
| Alteração de limite | Limite anterior, novo | 5 anos |
| Criação/edição de oferta | Campos alterados | 2 anos |
| Disputa | Decisão, evidências, resultado | 5 anos |
| Report de usuário | Motivo, moderação aplicada | 3 anos |
| Exportação de dados | Admin que exportou, escopo | 1 ano |

### Implementação
```php
class AuditTrail {
    public function log($event, $data) {
        global $wpdb;
        $wpdb->insert("{$wpdb->prefix}mt_audit_log", [
            'event_type' => $event,
            'user_id' => get_current_user_id(),
            'user_ip' => $_SERVER['REMOTE_ADDR'],
            'user_agent' => $_SERVER['HTTP_USER_AGENT'],
            'event_data' => json_encode($data),
            'created_at' => current_time('mysql'),
        ]);
    }
}
```

### Tabela Audit Log
```sql
CREATE TABLE IF NOT EXISTS wp_mt_audit_log (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    event_type VARCHAR(50) NOT NULL,
    user_id BIGINT UNSIGNED,
    user_ip VARCHAR(45),
    user_agent TEXT,
    event_data JSON,
    created_at DATETIME(3) NOT NULL,
    INDEX idx_event (event_type, created_at),
    INDEX idx_user (user_id, created_at),
    INDEX idx_type_date (event_type, created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

---

## Backup Strategy for Financial Data

### Estratégia

| Tipo | Frequência | Retenção | Destino |
|------|------------|----------|---------|
| Banco completo | Diário (03:00) | 30 dias | S3 (B2/DigitalOcean) |
| Transações + Audit | A cada 6h | 90 dias | S3 + Local |
| wp_uploads | Semanal | 30 dias | S3 |
| Snippets + API | A cada deploy | 10 versões | Git + S3 |
| Configurações | A cada alteração | Imediato | Git + S3 |

### Comando de Backup
```bash
#!/bin/bash
# Backup transações
mysqldump -u $DB_USER -p$DB_PASS $DB_NAME \
  wp_mt_transactions wp_mt_reconciliation wp_mt_audit_log \
  wp_postmeta wp_posts \
  --where="post_type IN ('transaction','voucher','used_commission')" \
  | gzip > /backups/mt-financeiro-$(date +%Y%m%d-%H%M).sql.gz

# Upload para S3
aws s3 cp /backups/mt-financeiro-*.sql.gz s3://trokapay-backups/financeiro/
```

---

## GDPR / LGPD Compliance

### LGPD Data Mapping

| Dado Pessoal | Finalidade | Base Legal | Retenção |
|-------------|------------|------------|----------|
| Nome, CPF, RG | Identificação do associado | Contrato | 5 anos após saída |
| Endereço | Entrega de produtos | Execução contratual | 5 anos |
| Telefone | Contato e WhatsApp | Legítimo interesse | Ativo |
| Dados bancários | Pagamento de comissões | Execução contratual | 2 anos após saída |
| Geolocalização | Mapa de associados | Consentimento | Ativo |
| Cookies e IP | Segurança e analytics | Legítimo interesse | 6 meses |
| Histórico de compras | Relatórios fiscais | Obrigação legal | 5 anos |

### Direitos do Titular (Art. 18 LGPD)

```php
class LgpdService {
    public function confirmExistence($user_id) { /* Art. 18.I */ }
    public function exportData($user_id) {       /* Art. 18.II */ }
    public function correctData($user_id, $data) { /* Art. 18.III */ }
    public function anonymizeUser($user_id) {    /* Art. 18.IV */ }
    public function deleteData($user_id) {       /* Art. 18.VI */ }
    public function revokeConsent($user_id) {    /* Art. 18.IX */ }
}
```

### Consentimento Explícito
```php
// Modal de consentimento no cadastro
$consent = [
    'termos_uso' => true,
    'politica_privacidade' => true,
    'comunicacao_whatsapp' => $whatsapp_consent,
    'comunicacao_email' => $email_consent,
    'compartilhamento_dados' => $share_consent,
    'geolocalizacao' => $geo_consent,
    'data' => current_time('mysql'),
    'ip' => $_SERVER['REMOTE_ADDR'],
];
update_user_meta($user_id, 'lgpd_consent', $consent);
```

---

## REST API — Rate Limiting & Cache

### Rate Limiting

| Endpoint | Padrão | Autenticado | Admin |
|----------|--------|-------------|-------|
| `/api/v1/profiles` | 30/min | 60/min | 120/min |
| `/api/v1/offers` | 30/min | 60/min | 120/min |
| `/api/v1/transactions` | 10/min | 30/min | 60/min |
| `/api/v1/vouchers` | 10/min | 20/min | 60/min |
| `moedadetroka/v1/*` | 20/min | 40/min | 100/min |

### Implementação
```php
define('MT_RATE_LIMIT', [
    'default' => ['requests' => 30, 'window' => 60],
    'authenticated' => ['requests' => 60, 'window' => 60],
    'admin' => ['requests' => 120, 'window' => 60],
    'financial' => ['requests' => 10, 'window' => 60],
]);

// Rate limit check
$limiter = new RateLimiter();
if (!$limiter->allow($user_id, 'financial')) {
    wp_send_json_error(['message' => 'Rate limit exceeded'], 429);
}
```

### Cache Strategy for Product Listings

| Estratégia | TTL | Invalidação | Uso |
|------------|-----|-------------|-----|
| Produtos em destaque | 600s | Ao criar/editar oferta | Homepage |
| Busca de ofertas | 300s | Ao criar/editar oferta | Central de Ofertas |
| Perfil de associado | 900s | Ao editar perfil | Página de associado |
| Categorias | 3600s | Ao criar/editar categoria | Menu/filtros |
| Estatísticas | 1800s | Força manual | Dashboard |

```php
class CacheStrategy {
    // Tag-based invalidation
    const TAGS = [
        'offers' => ['prefix' => 'mt_offers_', 'ttl' => 300],
        'profile' => ['prefix' => 'mt_profile_', 'ttl' => 900],
        'categories' => ['prefix' => 'mt_cats_', 'ttl' => 3600],
    ];

    public function invalidateByTag($tag) {
        // Incrementa versão da tag → todos os caches com essa tag expiram
        $version = get_option("mt_cache_tag_{$tag}") ?: 1;
        update_option("mt_cache_tag_{$tag}", $version + 1);
    }

    public function get($key, $tag) {
        $version = get_option("mt_cache_tag_{$tag}") ?: 1;
        return get_transient("{$key}_v{$version}");
    }
}
```

---

## Search Optimization (Elasticsearch)

### Quando Usar Elasticsearch

| Situação | MySQL | Elasticsearch |
|----------|-------|---------------|
| < 10.000 ofertas | ✅ | ⚠️ Opcional |
| 10.000 - 100.000 ofertas | ⚠️ Lento | ✅ |
| > 100.000 ofertas | ❌ | ✅ |
| Filtros multi-campo | ⚠️ Complexo | ✅ Nativo |
| Busca full-text | ⚠️ LIKE lento | ✅ Nativo |
| Geo-search | ✅ ST_Distance | ✅ Geo queries |

### Integração

```php
class SearchManager {
    private $client;

    public function __construct() {
        $this->client = ClientBuilder::create()
            ->setHosts([MT_ELASTICSEARCH_HOST])
            ->build();
    }

    public function indexOffer($product_id) {
        $product = wc_get_product($product_id);
        $params = [
            'index' => 'mt_offers',
            'id' => $product_id,
            'body' => [
                'title' => $product->get_title(),
                'description' => $product->get_description(),
                'price_pl' => (float) get_post_meta($product_id, 'price', true),
                'category' => wp_get_object_terms($product_id, 'product_cat', ['fields' => 'names']),
                'condition' => wp_get_object_terms($product_id, 'offer_product_condition_category', ['fields' => 'names']),
                'city' => get_user_meta($product->get_author_id(), 'company_address_city', true),
                'state' => get_user_meta($product->get_author_id(), 'company_address_state', true),
                'created_at' => get_the_date('c', $product_id),
            ]
        ];
        return $this->client->index($params);
    }

    public function search($query, $filters = [], $page = 1, $perPage = 20) {
        $must = [];
        if ($query) $must[] = ['multi_match' => ['query' => $query, 'fields' => ['title^3', 'description^2', 'category']]];
        if (!empty($filters['state'])) $must[] = ['term' => ['state' => $filters['state']]];
        if (!empty($filters['min_price'])) $must[] = ['range' => ['price_pl' => ['gte' => $filters['min_price']]]];
        if (!empty($filters['max_price'])) $must[] = ['range' => ['price_pl' => ['lte' => $filters['max_price']]]];

        $params = [
            'index' => 'mt_offers',
            'body' => [
                'query' => ['bool' => ['must' => $must]],
                'sort' => ['created_at' => ['order' => 'DESC']],
                'from' => ($page - 1) * $perPage,
                'size' => $perPage,
            ]
        ];
        return $this->client->search($params);
    }
}
```

---

## Email Marketing Automation

### Triggered Emails

| Evento | Email | Delay | Template |
|--------|-------|-------|----------|
| Novo cadastro | Boas-vindas + tutorial | 0 | `welcome` |
| Primeira oferta publicada | Parabéns + dicas | 5 min | `first_offer` |
| 7 dias sem login | "Sentimos sua falta" | 7 dias | `reengagement` |
| Oferta perto de expirar | "Renove sua oferta" | 3 dias antes | `expiry_warning` |
| Venda realizada | Confirmação + avaliação | 0 | `sale_confirmation` |
| Indicação convertida | "Ganhou bônus!" | 0 | `referral_bonus` |
| Carrinho abandonado | "Ainda interessado?" | 24h | `cart_abandonment` |

### Email Service Implementation
```php
class EmailService {
    private $provider;

    public function __construct() {
        $this->provider = new SendGrid(MT_SENDGRID_KEY);
    }

    public function sendTemplate($to, $template, $data) {
        $email = new \SendGrid\Mail\Mail();
        $email->setFrom("naoresponda@moedadetroka.com.br", "MoedaDeTroka");
        $email->setSubject($this->getSubject($template, $data));
        $email->addTo($to);
        $email->addContent("text/html", $this->renderTemplate($template, $data));
        return $this->provider->send($email);
    }
}
```

---

## SMS Notification Fallback

### Quando Usar SMS

| Situação | WhatsApp | Email | SMS |
|----------|----------|-------|-----|
| Confirmação de venda | ✅ Primário | ✅ Backup | ❌ |
| Notificação de compra | ✅ Primário | ⚠️ Backup | ✅ Se WA falhar |
| Recuperação de senha | ❌ | ✅ Primário | ✅ Backup |
| Código 2FA | ❌ | ❌ | ✅ Primário |
| Disputa aberta | ✅ Primário | ✅ Backup | ⚠️ Backup crítico |

### Implementação
```php
class SmsService {
    private $provider;

    public function __construct() {
        $this->provider = new Twilio(MT_TWILIO_SID, MT_TWILIO_TOKEN);
    }

    public function send($to, $message) {
        // Fallback: se WhatsApp falhar, tenta SMS
        try {
            $whatsapp = new WhatsAppService();
            $whatsapp->send($to, $message);
        } catch (\Exception $e) {
            $this->log("WhatsApp falhou, enviando SMS: " . $e->getMessage());
            $this->provider->messages->create($to, [
                'from' => MT_TWILIO_NUMBER,
                'body' => strip_tags($message),
            ]);
        }
    }
}
```

---

## Regras de Negócio — Completo

Configuradas via admin em "Regras de Negócio" (`moedadetroka-business-rules`):

| Configuração | Descrição | Padrão | Tipo |
|---|---|---|---|
| `default_overdraft_cnpj` | Cheque especial padrão (CNPJ) | 5000 | float |
| `default_overdraft_cpf` | Cheque especial padrão (CPF) | 1000 | float |
| `default_overdraft_promoter` | Cheque especial padrão (Promotor) | 3000 | float |
| `default_purchase_tax` | Taxa de compra (%) | 7.5 | float |
| `default_commission_cnpj` | Comissão padrão CNPJ (%) | 3 | float |
| `default_commission_cpf` | Comissão padrão CPF (%) | 5 | float |
| `default_commission_promoter` | Comissão padrão Promotor (%) | 4 | float |
| `default_promoter_brl_commission` | Comissão BRL Promotor (%) | 50 | float |
| `escrow_hold_days` | Dias em escrow | 7 | int |
| `max_dispute_days` | Prazo máximo para disputa | 30 | int |
| `min_price_pl` | Preço mínimo em PL$ | 1 | float |
| `max_overdraft_multiplier` | Multiplicador máximo de cheque especial | 3 | float |

---

## Decision Tree

```
Requisição recebida
├── API REST? → Rate limit check
│   ├── Excedeu? → 429 Too Many Requests
│   └── OK → Processa endpoint
│       ├── GET? → Cache hit? → Serve cache
│       │   └── Cache miss? → Query BD → Cache → Response
│       └── POST/PUT/DELETE? → Invalida cache → Processa
│
├── Compra via WooCommerce?
│   ├── Verificar saldo PL$ + overdraft
│   ├── Price split? → Divisão PL$/R$
│   ├── Gateaway externo (R$)? → Cielo/GerenciaNet/PIX
│   ├── Anti-fraud check
│   │   ├── Score > 80? → Bloqueia
│   │   ├── Score > 50? → Hold + verificação
│   │   └── OK → Processa
│   ├── Escrow → Fundos retidos
│   ├── Criar transação (CPT)
│   ├── Notificar vendedor (WhatsApp)
│   └── Atualizar saldos
│
├── Cadastro de associado?
│   ├── LGPD consent → Salva consentimento
│   ├── Verificar email + telefone
│   ├── Criar user metafields (empresa, CNPJ)
│   ├── Definir limites (overdraft, comissão)
│   └── Email de boas-vindas
│
└── Report/disputa?
    ├── Registra evidências
    ├── Notifica admin + partes
    ├── Escrow: fundos em hold
    └── Inicia cronômetro de resolução
```

---

## Antipadrões a Evitar

| Antipadrão | Problema | Solução |
|------------|----------|---------|
| **Saldo em float sem lock** | Race condition em transações simultâneas | Usar lock otimista ou fila de transações |
| **Cache sem invalidação** | Usuário vê produto vendido como disponível | Tag-based invalidation em cada alteração |
| **REST sem rate limit** | Bot pode consumir toda a API | Rate limiter por IP + user + token |
| **Hardcoded grupo WhatsApp** | Trocar grupo exige deploy | Configurável via admin |
| **Snippets sem versionamento** | Perda de código após atualização | Git + hash de versão em cada snippet |
| **Audit trail em options API** | Performance degradada com poucos logs | Tabela dedicada com índices |
| **Escrow manual** | Erro humano, atraso na liberação | Sistema automático com prazo configurável |
| **Fraude detectada tarde** | Prejuízo financeiro antes do bloqueio | Anti-fraud em tempo real no checkout |
| **LGPD ignorada** | Multa de até 2% do faturamento | Consentimento explícito + DPO + canal de dados |
| **Backup só do BD** | Perda de uploads e snippets | Backup full (BD + arquivos + configs) |
| **Taxa de câmbio PL$ fixa** | Distorção financeira com inflação | Lastro real + auditoria trimestral |
| **Notificar sempre via WhatsApp** | Custo alto se gateway falhar | Fallback automático email → SMS |

---

## Pro Tips

1. **Reconciliação Automática:** Configure cron para rodar reconciliação a cada 6h. Discrepâncias não resolvidas em 24h escalam para o admin financeiro.

2. **PL$ Lastro Real:** Mantenha uma conta bancária separada com saldo equivalente ao total de PL$ em circulação. Auditoria mensal obrigatória.

3. **Elasticsearch Incremental:** Faça indexação em background (WP-Cron), não no momento da criação da oferta. Use bulk API para lotes de 100 documentos.

4. **Snippet Versioning:** Cada snippet tem um header com versão, autor e changelog. Facilita debug e rollback.

5. **Cache Warming:** Para horários de pico (08:00, 12:00, 18:00), pré-aqueça o cache das páginas principais via WP-Cron + `wp_get` ou `wget`.

6. **Rate Limiting Adaptativo:** Aumente limites para associados com bom histórico, diminua para contas novas. Use `user_trust_score` baseado em tempo de conta + transações concluídas.

7. **LGPD Data Deletion Flow:** Quando um usuário solicita exclusão, anonimize (não delete) dados financeiros (obrigação legal de 5 anos). Delete apenas dados não-fiscais.

8. **Webhook de Transações:** Configure webhooks para sistemas externos (ERP, contabilidade) via `moedadetroka/v1/webhooks`. Eventos: `transaction.created`, `transaction.completed`, `dispute.opened`.

9. **Geolocalização com Cache:** Geocode via Nominatim/Google Maps apenas uma vez. Armazene lat/lng no user meta. Cache de 90 dias antes de re-geocode.

10. **Disaster Recovery Test:** Mensalmente, restaure o backup em ambiente de staging e verifique: saldos conferem? Transações íntegras? Relatórios geram corretamente?

---

## Performance Benchmarks

| Operação | MySQL Only | + Redis | + Elasticsearch |
|----------|-----------|---------|-----------------|
| Listar ofertas (50) | 1.2s | 200ms | 80ms |
| Busca full-text | 4.5s (LIKE) | — | 150ms |
| Perfil de associado | 800ms | 100ms | 80ms |
| Dashboard admin | 6s | 800ms | 500ms |
| Criar transação | 900ms | 400ms | 400ms |
| Relatório mensal | 15s | 3s | 2s |

---

## Comparação: Formas de Pagamento

| Método | Taxa | Liquidação | Chargeback | Storno |
|--------|------|------------|------------|--------|
| PL$ (moeda interna) | 0% | Imediata | ❌ | Manual |
| PIX | 0.99% | Instantâneo | ❌ | Difícil |
| Boleto | 1.99% | D+1 | ❌ | Manual |
| Cartão Crédito | 3.99% | D+30 | ✅ (180 dias) | Fácil |
| Débito | 2.49% | D+1 | ⚠️ Limitado | Médio |
| Saldo carteira | 0% | Imediata | ❌ | Manual |

---

## Monitoramento e Alertas

### Alertas Críticos
| Alerta | Canal | Threshold | Ação |
|--------|-------|-----------|------|
| Estorno > 5% do faturamento | Email + WhatsApp | Diário | Revisão antifraude |
| Taxa de erro API > 10% | Email + SMS | 5 min | Rollback ou debug |
| Disputa sem resposta > 48h | Email + WhatsApp | A cada 12h | Escalação |
| Saldo PL$ sem lastro | Email | Diário | Auditoria urgente |
| Backup falhou | Email + SMS | Imediato | Tentar novamente |
| Nova conta suspeita (score > 80) | WhatsApp admin | Imediato | Revisão manual |

---

## Ambiente Local

Path no servidor: `/wp-content/themes/moedadetroka/`
Domínios: `sac.moedadetroka.com.br`, `plataforma.moedadetroka.com.br`

```bash
# Dev environment
composer install
npm install

# Redis
redis-server

# Elasticsearch (opcional)
docker run -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:8.11.0

# Build assets
npm run build
```

---

## Base Directory (Skill)

```
file:///root/.config/opencode/skills/tema-moeda-de-troka
```

Caminhos relativos neste skill (ex: scripts/, reference/) são relativos a este diretório base.
