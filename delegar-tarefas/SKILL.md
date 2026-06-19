---
name: delegar-tarefas
description: Delega tarefas para o agy com monitoramento via agy-tasks/.
triggers: ["agy", "tarefa", "task", "todo", "delegar", "monitorar", "agy-tasks", "status", "progresso", "andamento", "pendente", "concluir", "finalizar", "criar task", "nova tarefa", "listar tarefas", "minhas tarefas", "quadro de tarefas", "kanban", "board", "prioridade", "urgente", "bloqueio", "impedimento", "nota", "anotar", "agy.py", "init", "inicializar", "adicionar nota"]
---

# AGY - Skill de Gerenciamento de Tarefas

Delega tarefas para o agy com monitoramento via `agy-tasks/`.

## Triggers

会被触发的关键词/模式：

### 任务操作
- "任务" / "tarefa" / "task" / "todo"
- "新任务" / "criar task" / "new task" / "criar tarefa"
- "列任务" / "listar tarefas" / "list tasks" / "minhas tarefas"
- "任务状态" / "status" / "andamento" / "progresso"
- "完成任务" / "done" / "concluir" / "finalizar"
- "看任务" / "ver task" / "show task" / "detalhes da tarefa"

### 操作命令
- "agy" / "agy.py"
- "init" / "inicializar" / "inicia"
- "agy-tasks"
- "task-template"

### 状态相关
- "pending" / "aguardando" / "pendente"
- "in_progress" / "andamento" / "em progresso"
- "completed" / "concluida" / "completa"
- " blockage" / "bloqueio" / "impedimento"

### 任务管理
- "delegar" / "delegar tarefa" / "assign"
- "monitorar" / "monitorar tarefas" / "monitor"
- "atualizar status" / "update status" / "mudar status"
- "adicionar nota" / "add note" / "anotar"
- "prioridade" / "priority" / "urgente"

### 文件操作
- "criar arquivo de task" / "criar task file"
- "ver pastas agy" / "agy folders"
- "diretório de tarefas" / "tasks directory"

### 进度追踪
- "progresso" / "progress" / "como vai" / "how is it going"
- "quadro de tarefas" / "kanban" / "board"
- "estatísticas" / "stats" / "resumo"
- "tarefas pendentes" / "pending tasks" / "backlog"

## Estrutura

```
agy-tasks/
├── current/              # Tasks em execucao
│   ├── <uuid1>.md
│   └── <uuid2>.md
├── templates/
│   └── task-template.md  # Modelo replicavel
└── status.md             # Status geral
```

## Comandos

```bash
agy.py init                      # Inicializa estrutura
agy.py new "Titulo" "Desc"       # Cria nova task
agy.py list                      # Lista tasks
agy.py status                    # Mostra status
agy.py show <id>                 # Ver task especifica
agy.py set <id> <status>         # Atualiza status
agy.py note <id> "nota"          # Adiciona nota
agy.py done <id>                 # Marca concluida
```

## Status Values

- `pending` - Aguardando
- `in_progress` - Em andamento
- `completed` - Concluida

## Uso pelo OpenCode

1. Leia `agy-tasks/status.md` para ver progresso
2. Use `agy.py new` para criar tasks
3. Use `agy.py note` para registrar o que fez
4. Use `agy.py done` para marcar conclusao