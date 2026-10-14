# OpenCode Skills — Foco Adianti Framework 🇧🇷

> Branch `skills-adianti`: este repositório + **337 skills `adianti-*`** geradas do **Adianti Tutor 8.7** — cobertura total do que o Tutor ensina a fazer, validadas rodando no Tutor real (`228/228` páginas e diálogos verificados via Playwright).

## 🧱 As 337 skills Adianti

| Origem | Qtd | O que é |
|---|---|---|
| Classes do `menu.xml` (Persistência, Apresentação, Organização) | 228 | 1 skill por função do menu: Conexões, Objetos, Coleções, Relacionamentos, Páginas, Contêineres, Diálogos, Formulários, Datagrids, Utilitários, Relatórios, Gráficos, Etiquetas, Templates, Extras, Cadastros, Lote, Checkout, Interações |
| Views ensináveis fora do menu | 47 | CartManagement, HelloWorld×4, QuickForms, MultiStep 2-4, CitySeek, SplitLeft/Right, forms de Kanban/Gantt/Calendário… |
| Exemplos executáveis `dbsamples` | 48 | `Object*`, `Collection*`, `Manual*`, `RegisterLog*` — o código que roda por trás das telas de Persistência |
| Skills agrupadas por tema | 13 | `adianti-persistencia-*`, `adianti-apresentacao-*`, `adianti-organizacao-*` — visão consolidada por assunto |
| Demo | 1 | `adianti-dialog-toast` |

### Cobertura por submenu (cards do Tutor → skills)

Persistência: Conexões 7 · Objetos 17 · Coleções 20 · Relacionamentos 6 — Apresentação: Páginas 14 · Contêineres 14 · Diálogos 7 · Formulários 26 · Datagrids 22 · Utilitários 15 · Relatórios 8 · Gráficos 5 · Etiquetas 3 · Templates 8 · Extras 20 — Organização: Padronizados 6 · Manuais 3 · Completos 7 · Consulta 2 · Lote 6 · Checkout 2 · Interações 3 · Utilitários 7.

### Anatomia de uma skill `adianti-*`

```
adianti-<classe>/
├── SKILL.md    # frontmatter (name/description/triggers) + código-fonte do Tutor + footer prático
└── SKILL.json  # AST do markdown (graphify-skill-router)
```

- `name` sempre com prefixo `adianti-*`; `triggers` incluem a classe (`TToast`, `TDataGrid`…), o caminho do menu e palavras-chave.
- Footer padrão **“Uso no seu projeto”**: copiar para a pasta `app/` (seu sistema decide control/model/etc.), trocar banco `samples` e modelos, testar antes de produzir.
- 5 skills carregam `Nota:` honesta (exigem registro em `menu.xml` ou rename arquivo para rodar standalone).

## 🚀 Uso Rápido

```bash
/skill adianti-dialogtoastview     # Toast com TToast::show
/skill adianti-saleform             # Mestre-detalhe de vendas
/skill adianti-persistencia-colecoes-criteria   # TCriteria/TFilter/TRepository
/skill adianti-apresentacao-datagrids           # Datagrids completas
```

Ou deixe o router achar: `graphify query "toast notification which skill handles this?"`.

## 🔄 Regenerar / auditar

```bash
python3 gerar_skill.py --classe DialogToastView --nome adianti-dialog-toast \
  --descricao "..." --triggers "TToast,toast" --dest .
python3 gerar_skill.py --batch --menu-xml menu.xml --min-bytes 1024
graphify update .
```

Auditoria: `menu.xml` (228) + SearchBox ao vivo (228, idêntico) + classes declaradas em `app/control` (336). Fora da cobertura, por decisão: `SearchBox`, `HomeView`, `Trash/*`, `util/*` (infraestrutura, não conteúdo ensinável).

---

## 📁 Restante do repositório (base `main`)

Skills originais + [mattpocock/skills](https://github.com/mattpocock/skills) (TypeScript-first): meta (`criar-novo-skill`, `editar-skill`, `graphify-skill-router`, `buildify`), frontend, Office/PDF, git, design, web e engineering/productivity do Matt. Estrutura e categorias originais preservadas da `main`.

## 🔀 Fluxo de Routing (graphify-skill-router)

```
Tarefa → graphify update → graphify query → AST do markdown → skill executa
```

## 📊 Estatísticas (branch `skills-adianti`)

- **Skills `adianti-*`**: 337 (228 menu + 47 views + 48 dbsamples + 13 agrupadas + 1 demo)
- **Grafo**: AST-only extraction (zero cost), `SKILL.json` em todas
- **Validação**: 228/228 páginas e view-sources verificados no Tutor real, 0 `Deprecated`
