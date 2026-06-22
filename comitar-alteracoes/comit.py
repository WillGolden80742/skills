#!/usr/bin/env python3
import os
import re
import subprocess
import argparse
from datetime import datetime

BASE_DIRS = ['app']
IGNORE_DIRS = {'vendor', 'node_modules', '.git', 'commits'}
IGNORE_FILES = {'.', '..'}

def run_git_command(args, cwd):
    if isinstance(args, list):
        result = subprocess.run(args, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    else:
        result = subprocess.run(args, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace', shell=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def get_staged_files(cwd):
    stdout, _, _ = run_git_command(["git", "diff", "--cached", "--name-only"], cwd)
    return [f for f in stdout.split("\n") if f] if stdout else []

def get_commit_hash(cwd):
    stdout, _, _ = run_git_command(["git", "rev-parse", "--short", "HEAD"], cwd)
    return stdout

def create_commit_file(project_path, commit_id, message, files, commit_hash):
    commits_dir = os.path.join(project_path, "commits")
    if not os.path.exists(commits_dir):
        os.makedirs(commits_dir)
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"commit-{timestamp}-{commit_id}.md"
    filepath = os.path.join(commits_dir, filename)
    files_list = "\n".join([f"- {f}" for f in files if f]) if files else "- (todos os arquivos)"
    content = f"""# Commit {commit_id} - {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

## Mensagem
{message}

## Arquivos
{files_list}

## Hash
{commit_hash}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Arquivo de commit criado: {filepath}")
    return filepath

def scan_directory(path, prefix=""):
    """Gera a árvore de diretórios em formato ASCII"""
    lines = []
    entries = sorted([e for e in os.listdir(path) if e not in IGNORE_DIRS and not e.startswith('.')])
    for i, entry in enumerate(entries):
        full = os.path.join(path, entry)
        is_last = i == len(entries) - 1
        connector = "└── " if is_last else "├── "
        lines.append(f"{prefix}{connector}{entry}")
        if os.path.isdir(full):
            extension = "    " if is_last else "│   "
            lines.extend(scan_directory(full, prefix + extension))
    return lines

def generate_dir_tree(project_path):
    """Gera a árvore de diretórios do projeto a partir de app/"""
    app_path = os.path.join(project_path, 'app')
    if not os.path.isdir(app_path):
        return None
    lines = [f"app/                                   # Aplicação principal (Rails-style)"]
    lines.extend(scan_directory(app_path, ""))
    return lines

def scan_php_classes(project_path, subdir):
    """Escaneia um diretório app/{subdir} e retorna lista de arquivos .php"""
    d = os.path.join(project_path, 'app', subdir)
    if not os.path.isdir(d):
        return []
    files = sorted([f for f in os.listdir(d) if f.endswith('.php') and f not in IGNORE_FILES])
    result = []
    for f in files:
        name = f"`{f.replace('.php', '')}`"
        fp = os.path.join(d, f)
        description = ""
        with open(fp, 'r', encoding='utf-8', errors='ignore') as fh:
            content = fh.read()
            m = re.search(r'class\s+\w+\s+', content)
            if m:
                desc_match = re.search(r'/\*\*\s*\*\s*(.*?)\s*\*/', content, re.DOTALL)
                if desc_match:
                    desc_line = desc_match.group(1).split('\n')[0].strip('* ')
                    description = desc_line
                else:
                    single = re.search(r'//\s*(.+)', content)
                    if single:
                        description = single.group(1)
        result.append((name, description))
    return result

def make_table(rows, headers):
    """Gera tabela markdown"""
    lines = []
    sep = "| " + " | ".join(["---"] * len(headers)) + " |"
    lines.append("| " + " | ".join(headers) + " |")
    lines.append(sep)
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(lines)

def replace_section(content, marker_start, marker_end, new_text):
    """Substitui conteúdo entre marcadores (incluindo os marcadores)"""
    pattern = re.escape(marker_start) + r".*?" + re.escape(marker_end)
    replacement = marker_start + "\n" + new_text + "\n" + marker_end
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def update_readme_structure(project_path):
    """Atualiza as seções estruturais do README.md: árvore de diretórios e tabelas de classes"""
    readme_path = os.path.join(project_path, "README.MD")
    if not os.path.exists(readme_path):
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False

    # 1. Atualizar árvore de diretórios
    tree = generate_dir_tree(project_path)
    if tree:
        tree_text = "\n".join(tree)
        tree_marker_start = "## Estrutura de Diretórios"
        tree_marker_end = "## Entrypoints WordPress"
        if tree_marker_start in content and tree_marker_end in content:
            old_tree_section = content[content.index(tree_marker_start):content.index(tree_marker_end)]
            new_tree_section = f"{tree_marker_start}\n\n```\nuailove/                                   # Raiz do tema WordPress\n│\n{tree_text}\n```\n\n"
            content = content.replace(old_tree_section, new_tree_section)
            changed = True

    # 2. Atualizar tabelas de Controllers, Models, Services
    sections = {
        'Controllers': scan_php_classes(project_path, 'controllers'),
        'Models': scan_php_classes(project_path, 'models'),
        'Services': scan_php_classes(project_path, 'services'),
    }

    table_configs = [
        ('Controllers', '### Controllers', '### Models',
         ["Controller", "Responsabilidade"]),
        ('Models', '### Models', '### Services',
         ["Model", "Responsabilidade"]),
        ('Services', '### Services', '## AJAX Actions',
         ["Service", "Responsabilidade"]),
    ]

    for section_name, section_header, next_header, headers in table_configs:
        if section_header not in content or next_header not in content:
            continue
        rows = [(name, desc[:60]) for name, desc in sections[section_name]]
        new_table = make_table(rows, headers)
        section_start = content.index(section_header)
        search_area = content[section_start:content.index(next_header)]
        table_match = re.search(r'^\| ' + re.escape(headers[0]) + r'\s+\|', search_area, re.MULTILINE)
        if table_match:
            table_start = section_start + table_match.start()
            table_end = content.index(next_header)
            old = content[table_start:table_end]
            content = content.replace(old, new_table + "\n\n", 1)
            changed = True

    if changed:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("README.md atualizado com a estrutura do projeto")

def main():
    parser = argparse.ArgumentParser(description="Git commit com historico")
    parser.add_argument("--message", required=True, help="Mensagem do commit")
    parser.add_argument("--files", help="Arquivos a comitar (separados por espaco)")
    parser.add_argument("--project", help="Caminho base do projeto")
    parser.add_argument("--force", action="store_true", help="Usa --force-with-lease no push")

    args = parser.parse_args()

    project_path = args.project or os.getcwd()
    os.chdir(project_path)

    if args.files:
        files_list = args.files.split()
        for f in files_list:
            run_git_command(["git", "add", f], project_path)
    else:
        run_git_command(["git", "add", "-A"], project_path)

    staged = get_staged_files(project_path)
    if not staged:
        print("Nenhum arquivo para comitar")
        return

    print("\n=== DAS ALTERACOES QUE SERAO COMMITADAS ===\n")
    diff_stdout, _, _ = run_git_command(["git", "diff", "--cached", "--stat"], project_path)
    if diff_stdout:
        print(diff_stdout)
    print()
    diff_content, _, _ = run_git_command(["git", "diff", "--cached"], project_path)
    if diff_content:
        print(diff_content[:3000])
        if len(diff_content) > 3000:
            print("... (diff truncado, mostrando primeiras 3000 linhas)")
    print("\n==========================================\n")

    confirm = input("Confirmar commit? (s/n): ").strip().lower()
    if confirm != "s":
        print("Commit cancelado.")
        return

    print("Fazendo commit...")
    _, stderr, code = run_git_command(["git", "commit", "-m", args.message], project_path)

    if code != 0:
        if "nothing to commit" in stderr.lower():
            print("Nenhum arquivo para comitar")
            return
        print(f"Erro ao fazer commit: {stderr}")
        return

    commit_hash = get_commit_hash(project_path)
    commit_id = commit_hash[:7] if commit_hash else "0000000"

    print(f"Commit realizado: {commit_hash[:7]}")

    print("Criando arquivo de commit em commits/...")
    create_commit_file(project_path, commit_id, args.message, staged, commit_hash)

    print("Fazendo commit do historico...")
    run_git_command(["git", "add", "commits/"], project_path)
    _, _, commit_hist_code = run_git_command(["git", "commit", "-m", f"chore: historico commit {commit_id}"], project_path)
    if commit_hist_code == 0:
        commit_hash = get_commit_hash(project_path)
        print(f"Commit do historico realizado: {commit_hash[:7]}")

    print("Atualizando README com estrutura do projeto...")
    update_readme_structure(project_path)

    print("Fazendo pull antes do push...")
    _, pull_stderr, pull_code = run_git_command(["git", "pull", "--rebase"], project_path)
    if pull_code != 0:
        print(f"Aviso no pull: {pull_stderr}")

    push_cmd = ["git", "push"]
    if args.force:
        push_cmd.append("--force-with-lease")
        print("Usando --force-with-lease...")

    print("Fazendo push...")
    _, push_stderr, push_code = run_git_command(push_cmd, project_path)
    if push_code != 0:
        print(f"Erro no push: {push_stderr}")
    else:
        print("Push realizado com sucesso")

if __name__ == "__main__":
    main()
