---
name: group-search
description: Plugin WordPress Group Search Bot — bot de busca inteligente em grupos WhatsApp via Uazapi com IA think mode, logs detalhados e painel wp-admin.
triggers:
  - group search bot
  - busca whatsapp grupo
  - bot whatsapp woocommerce
  - uazapi busca produtos
  - think mode produtos
  - grupo moeda troka
---

## Visão Geral

Plugin WordPress que integra com **uazapi (WhatsApp API externa)** para escutar mensagens em grupos WhatsApp. Quando um cliente pergunta se "tem" algum produto (ex: "tem capacete", "tem iphone"), o bot usa **IA com think mode retroativo** para entender a intenção, buscar produtos no WooCommerce e responder no grupo com até 5 resultados (máx 10).

**Arquivo principal:** `wp-content/plugins/group-search/group_search.php` (ou copiado para `wp-content/themes/trokapay/group_search.php`)

---

## Como Usar

### 1. Instalação

Copie `C:\Users\willi\OneDrive\Anexos\Desktop\snippets\group_search.php` para `wp-content/plugins/group-search/group_search.php` ou ative via WordPress.

### 2. Configuração no wp-admin

Vá em **Group Search** no menu admin e configure:

#### Aba Uazapi
| Campo | Descrição |
|-------|-----------|
| Domínio | Subdomínio da sua instância uazapi (ex: `meuapp` → `https://meuapp.uazapi.com`) |
| Token | Token da instância uazapi |
| Grupo WhatsApp | ID do grupo para escutar (padrão: `120363403250053293@g.us`) |
| Webhook URL | URL gerada automaticamente — configure no webhook da sua instância uazapi |

#### Aba IA
| Campo | Descrição |
|-------|-----------|
| Provedor | `openrouter` (recomendado), `opencode` ou `gemini` |
| Modelo | Modelo da IA. Pode ser definido no `wp-config.php` com `define('GSB_AI_MODEL', '...')` |
| API Key | Chave da API. Pode ser definida no `wp-config.php` com `define('GSB_AI_KEY', '...')` |
| Think Depth | Profundidade do think mode retroativo (1-10, padrão: 3) |

#### Config via wp-config.php (opcional)
```php
define('GSB_AI_PROVIDER', 'openrouter');
define('GSB_AI_MODEL', 'openrouter/auto');
define('GSB_AI_KEY', 'sua-chave-aqui');
```

### 3. Webhook Uazapi

Configure o webhook da sua instância uazapi com:
- **URL:** `<site>/wp-json/gsb/v1/webhook`
- **Eventos:** `["messages"]`
- O próprio plugin ignora `message.fromMe === true` (evita loop automático)

### 4. Grupo WhatsApp

O bot escuta o grupo configurado no admin (padrão: `120363403250053293@g.us` — grupo MOEDA da Trokapay).

---

## Think Mode (Retroativo)

O think mode funciona em profundidade regressiva:

1. **Análise de Intenção** — IA interpreta a mensagem e extrai termos de busca
2. **Busca Inicial** — WP_Query com os termos extraídos
3. **Expansão Retroativa** — Se < 5 resultados, IA gera termos mais amplos e busca de novo
4. **Até o limite** — Repete até o `think_depth` configurado ou até encontrar 5+ produtos
5. **Resposta** — Formata e envia para o grupo

**Exemplo de fluxo:**
- Usuário: "tem capacete"
- Depth 1: busca "capacete" → 2 resultados
- Depth 2: expande para "capacete, moto, acessório" → 4 resultados
- Depth 3: expande para "capacete, moto, acessório, segurança, piloto" → 7 resultados → responde com 5

---

## Logs

Logs são armazenados no banco (options API) e exibidos no painel admin (Group Search > Logs).

### Níveis de Log
| Nível | Cor | Descrição |
|-------|-----|-----------|
| `INFO` | 🔵 Azul | Eventos gerais (webhook recebido, etc.) |
| `THINK` | 🟠 Laranja | Etapas do think mode (intenção, profundidade) |
| `QUERY` | 🟢 Verde | Consultas WP_Query executadas |
| `RESULT` | 🟣 Roxo | Resultados finais |
| `SEND` | 🔵 Ciano | Envio de mensagens WhatsApp |
| `AI` | 🟠 Vermelho | Chamadas à API de IA |
| `RESPONSE` | 🔵 Ciano | Respostas formatadas |
| `SECURITY` | 🔴 Vermelho | Bloqueios do protection regex |
| `DEBUG` | ⚪ Cinza | Informações de depuração |
| `ERROR` | 🔴 Vermelho | Erros |

Cada log contém:
- Timestamp
- Nível
- Função caller
- Mensagem descritiva
- Contexto (JSON com dados relevantes)

---

## Proteção (Regex)

O plugin possui regex de proteção que bloqueia qualquer conteúdo contendo padrões destrutivos:

```
/\b(UPDATE|DELETE\s+FROM|DROP\s+TABLE|ALTER\s+TABLE|INSERT\s+INTO|
TRUNCATE\s+TABLE|REPLACE\s+INTO|RENAME\s+TABLE|CREATE\s+TABLE|
GRANT\s+|REVOKE\s+|EXEC\s+|EXECUTE\s+|xp_cmdshell|LOAD_FILE|
INTO\s+OUTFILE|INTO\s+DUMPFILE|UNION\s+ALL\s+SELECT|UNION\s+SELECT)\b/is
```

Aplicado em:
- Mensagens recebidas (webhook input)
- Respostas da IA (analyze_intent, expand_intent)
- Argumentos de query (execute_product_query)

Quando bloqueado, o evento é logado com nível `SECURITY` e a operação é abortada.

---

## Produtos WooCommerce

A busca utiliza os campos de produto da Trokapay:
- `title` (meta) — título do produto/oferta
- `price` (meta) — preço em PL$
- `description` (meta) — descrição
- `quantity` (meta) — estoque (> 0)
- `disclosure` (meta) — `public`
- `pickup_location` (meta) — local de retirada
- `offer_product_condition_category` (taxonomia) — novo/usado/brechó
- Dados do autor: `company_name`, `company_phone`, `company_address_state`

**Limite:** 5 produtos por padrão, máximo 10 se solicitado.

---

## Webhook REST API

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/wp-json/gsb/v1/webhook` | Recebe eventos da uazapi |
| `GET` | `/wp-json/gsb/v1/status` | Health check |

Payload real (confirmado via repo uazapi-webhook-events-examples):
```json
{
  "EventType": "messages",
  "instanceName": "eKoB39",
  "owner": "558185464605",
  "token": "xxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "chatSource": "updated",
  "chat": {
    "wa_chatid": "120363324913602723@g.us",
    "wa_isGroup": true,
    "name": "Full Group Teste"
  },
  "message": {
    "fromMe": false,
    "isGroup": true,
    "text": "Oi",
    "type": "text",
    "senderName": "Tito Bahé",
    "sender": "138401042923712@lid",
    "sender_pn": "40723973035@s.whatsapp.net",
    "chatid": "120363324913602723@g.us",
    "groupName": "Full Group Teste",
    "messageType": "ExtendedTextMessage",
    "messageTimestamp": 1770147294000,
    "id": "558185464605:AC4D6F7672164E5C348BA0847D4F55B5",
    "messageid": "AC4D6F7672164E5C348BA0847D4F55B5"
  }
}
```

**Campos usados pelo plugin:**
| Campo | Onde | Descrição |
|-------|------|-----------|
| `EventType` | root | Filtra eventos `"messages"` |
| `message.chatid` | message | ID do grupo (match com config) |
| `message.text` | message | Conteúdo da mensagem |
| `message.fromMe` | message | `false` = mensagem de outro usuário |
| `message.senderName` | message | Nome do remetente |
| `chat.wa_chatid` | chat | Fallback para ID do grupo |
```
