#!/usr/bin/env python3
import os
import sys
import uuid
from datetime import datetime
from shutil import copy

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_DIR = os.path.join(SCRIPT_DIR, "agy-tasks")
CURRENT_DIR = os.path.join(TASKS_DIR, "current")
TEMPLATE_FILE = os.path.join(TASKS_DIR, "templates", "task-template.md")

def ensure_dirs():
    os.makedirs(TASKS_DIR, exist_ok=True)
    os.makedirs(CURRENT_DIR, exist_ok=True)
    os.makedirs(os.path.join(TASKS_DIR, "templates"), exist_ok=True)

def read_template():
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        return f.read()

def create_task(title, description=""):
    ensure_dirs()
    task_id = str(uuid.uuid4())[:8]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    content = read_template()
    content = content.replace("{{TASK_ID}}", task_id)
    content = content.replace("{{STATUS}}", "pending")
    content = content.replace("{{TITLE}}", title)
    content = content.replace("{{CREATED}}", now)
    content = content.replace("{{UPDATED}}", now)
    content = content.replace("{{DESCRIPTION}}", description or "Sem descricao")
    content = content.replace("{{NOTES}}", "Nenhuma nota")
    content = content.replace("{{DELIVERABLES}}", "Nenhuma entrega")
    
    filename = f"{task_id}.md"
    filepath = os.path.join(CURRENT_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Criada task: {filename}")
    update_status()
    return task_id, filename

def update_status():
    ensure_dirs()
    tasks = []
    
    for filename in os.listdir(CURRENT_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(CURRENT_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                task_id = filename.replace(".md", "")
                status = "unknown"
                title = "Sem titulo"
                
                for line in content.split("\n"):
                    if "**Status:**" in line:
                        status = line.split("**Status:**")[1].strip().lower()
                    elif "**Titulo:**" in line:
                        title = line.split("**Titulo:**")[1].strip()
                
                tasks.append((task_id, title, status))
    
    completed = sum(1 for _, _, s in tasks if s == "completed")
    in_progress = sum(1 for _, _, s in tasks if s == "in_progress")
    pending = sum(1 for _, _, s in tasks if s == "pending")
    
    content = f"""# Status AGY

**Ultima atualizacao:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Resumo

| Status    | Quantidade |
|-----------|------------|
| Pendente  | {pending}  |
| Andamento | {in_progress} |
| Concluido | {completed} |
| **Total** | **{len(tasks)}** |

## Tasks Ativas

| ID       | Titulo                    | Status       |
|----------|---------------------------|--------------|
"""
    for task_id, title, status in sorted(tasks):
        marker = {"completed": "[X]", "in_progress": "[>]", "pending": "[ ]"}.get(status, "[?]")
        content += f"| {task_id} | {title[:25]:<25} | {marker} {status:<10} |\n"
    
    content += """
## Comandos

```
agy.py new "Titulo" "Descricao"  - Criar nova task
agy.py list                        - Listar todas
agy.py show <id>                   - Ver task especifica
agy.py set <id> <status>           - Atualizar status
agy.py note <id> "nota"            - Adicionar nota
agy.py done <id>                   - Marcar como concluida
```
"""
    
    filepath = os.path.join(TASKS_DIR, "status.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Status atualizado: {len(tasks)} tasks")

def list_tasks():
    ensure_dirs()
    for filename in os.listdir(CURRENT_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(CURRENT_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                task_id = filename.replace(".md", "")
                status = "unknown"
                title = "Sem titulo"
                
                for line in content.split("\n"):
                    if "**Status:**" in line:
                        status = line.split("**Status:**")[1].strip().lower()
                    elif "**Titulo:**" in line:
                        title = line.split("**Titulo:**")[1].strip()
                
                marker = {"completed": "[X]", "in_progress": "[>]", "pending": "[ ]"}.get(status, "[?]")
                print(f"{marker} {task_id} - {title} ({status})")

def show_task(task_id):
    filepath = os.path.join(CURRENT_DIR, f"{task_id}.md")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print(f"Task {task_id} nao encontrada")

def set_status(task_id, status):
    filepath = os.path.join(CURRENT_DIR, f"{task_id}.md")
    if not os.path.exists(filepath):
        print(f"Task {task_id} nao encontrada")
        return
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = content.split("\n")
    new_lines = []
    
    for line in lines:
        if "**Status:**" in line:
            new_lines.append(f"**Status:** {status}")
        elif "**Atualizado em:**" in line:
            new_lines.append(f"**Atualizado em:** {now}")
        else:
            new_lines.append(line)
    
    content = "\n".join(new_lines)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Task {task_id} -> {status}")
    update_status()

def add_note(task_id, note):
    filepath = os.path.join(CURRENT_DIR, f"{task_id}.md")
    if not os.path.exists(filepath):
        print(f"Task {task_id} nao encontrada")
        return
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = content.split("\n")
    new_lines = []
    in_notes = False
    
    for line in lines:
        if line.startswith("## Notas de Execucao"):
            in_notes = True
            new_lines.append(line)
            new_lines.append(f"\n**[{now}]** {note}")
        elif line.startswith("## Entregas"):
            in_notes = False
            new_lines.append("")
        elif in_notes and line.startswith("**["):
            new_lines.append(line)
        else:
            if in_notes and line.strip() == "":
                continue
            new_lines.append(line)
    
    content = "\n".join(new_lines)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Nota adicionada a task {task_id}")

def cmd_init():
    ensure_dirs()
    if not os.path.exists(TEMPLATE_FILE):
        template = """# Task Template

**ID:** {{TASK_ID}}
**Status:** {{STATUS}}
**Titulo:** {{TITLE}}
**Criado em:** {{CREATED}}
**Atualizado em:** {{UPDATED}}

---

## Descricao

{{DESCRIPTION}}

---

## Progresso

- [ ] Pendente
- [ ] Em andamento
- [ ] Concluido

---

## Notas de Execucao

{{NOTES}}

---

## Entregas

{{DELIVERABLES}}"""
        with open(TEMPLATE_FILE, "w", encoding="utf-8") as f:
            f.write(template)
    
    with open(os.path.join(TASKS_DIR, "status.md"), "w", encoding="utf-8") as f:
        f.write("# Status AGY\n\nNenhuma task criada ainda.\n")
    
    print("Estrutura inicializada em agy-tasks/")
    print(f"  - {TASKS_DIR}/")
    print(f"  - {CURRENT_DIR}/")
    print(f"  - {os.path.join(TASKS_DIR, 'templates')}/")

def main():
    ensure_dirs()
    
    if len(sys.argv) < 2:
        update_status()
        return
    
    command = sys.argv[1]
    
    if command == "init":
        cmd_init()
    elif command == "new":
        title = sys.argv[2] if len(sys.argv) > 2 else "Nova Task"
        desc = sys.argv[3] if len(sys.argv) > 3 else ""
        create_task(title, desc)
    elif command == "list":
        list_tasks()
    elif command == "status":
        update_status()
        filepath = os.path.join(TASKS_DIR, "status.md")
        with open(filepath, "r", encoding="utf-8") as f:
            print(f.read())
    elif command == "show":
        if len(sys.argv) < 3:
            print("Uso: agy.py show <id>")
        else:
            show_task(sys.argv[2])
    elif command == "set":
        if len(sys.argv) < 4:
            print("Uso: agy.py set <id> <pending|in_progress|completed>")
        else:
            set_status(sys.argv[2], sys.argv[3])
    elif command == "note":
        if len(sys.argv) < 4:
            print("Uso: agy.py note <id> 'nota text'")
        else:
            add_note(sys.argv[2], sys.argv[3])
    elif command == "done":
        if len(sys.argv) < 3:
            print("Uso: agy.py done <id>")
        else:
            set_status(sys.argv[2], "completed")
    elif command == "help":
        print("""agy.py - Gerenciador de Tasks

Comandos:
  init                          - Inicializa estrutura de pastas
  new "titulo" "descricao"      - Cria nova task
  list                          - Lista todas as tasks
  status                        - Mostra status geral
  show <id>                     - Mostra task especifica
  set <id> <status>             - Atualiza status (pending|in_progress|completed)
  note <id> 'nota'              - Adiciona nota a task
  done <id>                     - Marca task como concluida
  help                          - Mostra esta ajuda""")
    else:
        print(f"Comando desconhecido: {command}")
        print("Use: agy.py help")

if __name__ == "__main__":
    main()