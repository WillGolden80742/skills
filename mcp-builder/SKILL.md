---
name: mcp-builder
description: Guia para criar servidores MCP (Model Context Protocol) de alta qualidade que permitem LLMs interagir com serviços externos através de ferramentas bem projetadas. Use ao construir servidores MCP para integrar APIs ou serviços externos, seja em Python (FastMCP) ou Node/TypeScript (MCP SDK).
triggers: ["mcp", "model context protocol", "criar servidor mcp", "mcp server", "fastmcp", "mcp sdk", "servidor mcp", "ferramenta mcp", "tool mcp", "mcp tool", "mcp resource", "mcp prompt", "mcp transporte", "mcp transport", "streamable http", "mcp stdio", "integrar api", "api externa", "mcp typescript", "mcp python", "mcp inspector", "criar ferramenta", "mcp authentication", "mcp pagination", "mcp error handling", "mcp tool design", "mcp avaliação", "mcp evaluation", "mcp zod", "mcp pydantic", "mcp sdk typescript", "mcp sdk python"]
license: Termos completos em LICENSE.txt
---

# Guia de Desenvolvimento de Servidores MCP

## Visão Geral

Crie servidores MCP (Model Context Protocol) que permitem LLMs interagir com serviços externos através de ferramentas bem projetadas. A qualidade de um servidor MCP é medida por quão bem ele permite LLMs accomplishing tarefas do mundo real.

---

# Processo

## 🚀 Fluxo de Trabalho de Alto Nível

Criar um servidor MCP de alta qualidade envolve quatro fases principais:

### Fase 1: Pesquisa Profunda e Planejamento

#### 1.1 Compreender o Design Moderno do MCP

**Cobertura de API vs. Ferramentas de Workflow:**
Equilibre cobertura abrangente de endpoints de API com ferramentas especializadas de workflow. Ferramentas de workflow podem ser mais convenientes para tarefas específicas, enquanto cobertura abrangente dá aos agentes flexibilidade para compor operações. O desempenho varia por cliente — alguns clientes se beneficiam de execução de código que combina ferramentas básicas, enquanto outros funcionam melhor com workflows de alto nível. Quando incerto, priorize cobertura abrangente de API.

**Nomeação e Descoberta de Ferramentas:**
Nomes de ferramentas claros e descritivos ajudam agentes a encontrar as ferramentas rapidamente. Use prefixos consistentes (ex: `github_create_issue`, `github_list_repos`) e nomenclatura orientada a ações.

**Gerenciamento de Contexto:**
Agentes se beneficiam de descrições de ferramentas concisas e capacidade de filtrar/paginar resultados. Desenhe ferramentas que retornam dados focados e relevantes. Alguns clientes suportam execução de código que pode ajudar agentes a filtrar e processar dados eficientemente.

**Mensagens de Erro Açãoáveis:**
Mensagens de erro devem guiar agentes em direção a soluções com sugestões específicas e próximos passos.

#### 1.2 Estudar Documentação do Protocolo MCP

**Navegue pela especificação MCP:**

Comece com o sitemap para encontrar páginas relevantes: `https://modelcontextprotocol.io/sitemap.xml`

Depois busque páginas específicas com sufixo `.md` para formato markdown (ex: `https://modelcontextprotocol.io/specification/draft.md`).

Páginas principais para revisar:
- Visão geral da especificação e arquitetura
- Mecanismos de transporte (streamable HTTP, stdio)
- Definições de ferramentas, recursos e prompts

#### 1.3 Estudar Documentação do Framework

**Stack recomendado:**
- **Linguagem**: TypeScript (suporte SDK de alta qualidade e boa compatibilidade em muitos ambientes de execução)
- **Transporte**: Streamable HTTP para servidores remotos, usando JSON stateless (mais simples de escalar e manter). stdio para servidores locais.

**Carregue documentação do framework:**

- **Melhores Práticas MCP**: [📋 Ver Melhores Práticas](./reference/mcp_best_practices.md) - Diretrizes核心

**Para TypeScript (recomendado):**
- **TypeScript SDK**: Use WebFetch para carregar `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
- [⚡ Guia TypeScript](./reference/node_mcp_server.md) - Padrões e exemplos TypeScript

**Para Python:**
- **Python SDK**: Use WebFetch para carregar `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- [🐍 Guia Python](./reference/python_mcp_server.md) - Padrões e exemplos Python

#### 1.4 Planeje Sua Implementação

**Entenda a API:**
Revise a documentação da API do serviço para identificar endpoints principais, requisitos de autenticação e modelos de dados. Use busca na web e WebFetch conforme necessário.

**Seleção de Ferramentas:**
Priorize cobertura abrangente de API. Liste endpoints a implementar, começando pelas operações mais comuns.

---

### Fase 2: Implementação

#### 2.1 Configure Estrutura do Projeto

Veja guias específicos por linguagem para configuração do projeto:
- [⚡ Guia TypeScript](./reference/node_mcp_server.md) - Estrutura do projeto, package.json, tsconfig.json
- [🐍 Guia Python](./reference/python_mcp_server.md) - Organização de módulos, dependências

#### 2.2 Implemente Infraestrutura Compartilhada

Crie utilitários compartilhados:
- Cliente de API com autenticação
- Helpers de tratamento de erros
- Formatação de resposta (JSON/Markdown)
- Suporte a paginação

#### 2.3 Implemente Ferramentas

Para cada ferramenta:

**Schema de Entrada:**
- Use Zod (TypeScript) ou Pydantic (Python)
- Inclua restrições e descrições claras
- Adicione exemplos nas descrições dos campos

**Schema de Saída:**
- Defina `outputSchema` onde possível para dados estruturados
- Use `structuredContent` em respostas de ferramentas (recurso TypeScript SDK)
- Ajuda clientes a entenderem e processarem saídas de ferramentas

**Descrição da Ferramenta:**
- Resumo conciso da funcionalidade
- Descrições de parâmetros
- Schema do tipo de retorno

**Implementação:**
- Async/await para operações de I/O
- Tratamento de erros adequado com mensagens açãoáveis
- Suporte a paginação onde aplicável
- Retorne tanto conteúdo textual quanto dados estruturados ao usar SDKs modernos

**Anotações:**
- `readOnlyHint`: true/false
- `destructiveHint`: true/false
- `idempotentHint`: true/false
- `openWorldHint`: true/false

---

### Fase 3: Revisão e Teste

#### 3.1 Qualidade do Código

Revise buscando:
- Sem código duplicado (princípio DRY)
- Tratamento de erros consistente
- Cobertura de tipos completa
- Descrições de ferramentas claras

#### 3.2 Compile e Teste

**TypeScript:**
- Execute `npm run build` para verificar compilação
- Teste com MCP Inspector: `npx @modelcontextprotocol/inspector`

**Python:**
- Verifique sintaxe: `python -m py_compile seu_servidor.py`
- Teste com MCP Inspector

Veja guias específicos por linguagem para abordagens de teste detalhadas e checklists de qualidade.

---

### Fase 4: Crie Avaliações

Após implementar seu servidor MCP, crie avaliações abrangentes para testar sua eficácia.

**Carregue [✅ Guia de Avaliação](./reference/evaluation.md) para diretrizes completas de avaliação.**

#### 4.1 Entenda o Propósito da Avaliação

Use avaliações para testar se LLMs podem usar efetivamente seu servidor MCP para responder perguntas complexas e realistas.

#### 4.2 Crie 10 Perguntas de Avaliação

Para criar avaliações eficazes, siga o processo descrito no guia de avaliação:

1. **Inspeção de Ferramentas**: Liste ferramentas disponíveis e entenda suas capacidades
2. **Exploração de Conteúdo**: Use operações apenas leitura para explorar dados disponíveis
3. **Geração de Perguntas**: Crie 10 perguntas complexas e realistas
4. **Verificação de Respostas**: Resolva cada pergunta você mesmo para verificar respostas

#### 4.3 Requisitos da Avaliação

Garanta que cada pergunta seja:
- **Independente**: Não depende de outras perguntas
- **Apenas leitura**: Apenas operações não-destrutivas necessárias
- **Complexa**: Requer múltiplas chamadas de ferramentas e exploração profunda
- **Realista**: Baseada em casos de uso reais que humanos se preocupariam
- **Verificável**: Resposta única e clara que pode ser verificada por comparação de strings
- **Estável**: Resposta não mudará com o tempo

#### 4.4 Formato de Saída

Crie um arquivo XML com esta estrutura:

```xml
<evaluation>
  <qa_pair>
    <question>Encontre discussões sobre lançamentos de modelos AI com codinomes de animais. Um modelo precisava de uma designação de segurança específica que usa o formato ASL-X. Qual número X estava sendo determinado para o modelo nomeado após um gato selvagem manchado?</question>
    <answer>3</answer>
  </qa_pair>
<!-- Mais qa_pairs... -->
</evaluation>
```

---

# Arquivos de Referência

## 📚 Biblioteca de Documentação

Carregue estes recursos conforme necessário durante o desenvolvimento:

### Documentação Principal MCP (Carregue Primeiro)
- **Protocolo MCP**: Comece com sitemap em `https://modelcontextprotocol.io/sitemap.xml`, depois busque páginas específicas com sufixo `.md`
- [📋 Melhores Práticas MCP](./reference/mcp_best_practices.md) - Diretrizes universais MCP incluindo:
  - Convenções de nomeação de servidor e ferramentas
  - Diretrizes de formato de resposta (JSON vs Markdown)
  - Melhores práticas de paginação
  - Seleção de transporte (streamable HTTP vs stdio)
  - Padrões de segurança e tratamento de erros

### Documentação SDK (Carregue Durante Fase 1/2)
- **Python SDK**: Busque de `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- **TypeScript SDK**: Busque de `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`

### Guias de Implementação Específicos por Linguagem (Carregue Durante Fase 2)
- [🐍 Guia de Implementação Python](./reference/python_mcp_server.md) - Guia completo Python/FastMCP com:
  - Padrões de inicialização de servidor
  - Exemplos de modelos Pydantic
  - Registro de ferramentas com `@mcp.tool`
  - Exemplos funcionais completos
  - Checklist de qualidade

- [⚡ Guia de Implementação TypeScript](./reference/node_mcp_server.md) - Guia TypeScript completo com:
  - Estrutura do projeto
  - Padrões de schema Zod
  - Registro de ferramentas com `server.registerTool`
  - Exemplos funcionais completos
  - Checklist de qualidade

### Guia de Avaliação (Carregue Durante Fase 4)
- [✅ Guia de Avaliação](./reference/evaluation.md) - Guia completo de criação de avaliação com:
  - Diretrizes de criação de perguntas
  - Estratégias de verificação de respostas
  - Especificações de formato XML
  - Exemplos de perguntas e respostas
  - Executando uma avaliação com os scripts fornecidos
