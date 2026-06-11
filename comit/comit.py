#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse
from datetime import datetime

def run_git_command(args, cwd):
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True, shell=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def get_staged_files(cwd):
    stdout, _, _ = run_git_command(["git", "diff", "--cached", "--name-only"], cwd)
    return stdout.split("\n") if stdout else []

def get_commit_hash(cwd):
    stdout, _, _ = run_git_command(["git", "rev-HEAD", "--short"], cwd)
    return stdout

def create_commit_file(project_path, commit_id, message, files, commit_hash):
    commits_dir = os.path.join(project_path, "commits")
    if not os.path.exists(commits_dir):
        os.makedirs(commits_dir)
    
    timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    filename = f"commit-{commit_id}-{timestamp}.md"
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

def update_readme(project_path, message, files):
    readme_path = os.path.join(project_path, "README.md")
    
    changes = []
    for f in files:
        if f and not f.startswith("commits/"):
            if os.path.isfile(os.path.join(project_path, f)):
                try:
                    with open(os.path.join(project_path, f), "r", encoding="utf-8") as file:
                        content = file.read()
                    changes.append(f"### {f}\n```\n{content}\n```\n")
                except:
                    changes.append(f"### {f}\n*(arquivo binario ou nao legivel)*\n")
    
    change_content = "\n---\n".join(changes) if changes else ""
    
    new_section = f"""## Ultimas Alteracoes - {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

**Mensagem:** {message}

{change_content}
"""
    
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        if "## Ultimas Alteracoes" in content:
            lines = content.split("\n")
            start_idx = None
            end_idx = None
            for i, line in enumerate(lines):
                if line.startswith("## Ultimas Alteracoes"):
                    start_idx = i
                if start_idx is not None and line.startswith("## ") and i > start_idx:
                    end_idx = i
                    break
            
            if end_idx is None:
                for i in range(len(lines) - 1, -1, -1):
                    if lines[i].strip() and not lines[i].startswith("```"):
                        end_idx = i + 1
                        break
            
            lines = lines[:start_idx] + [new_section] + (lines[end_idx:] if end_idx else [])
            content = "\n".join(lines)
        else:
            content += f"\n{new_section}"
    else:
        content = f"# Projeto\n\n{new_section}"
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"README.md atualizado")

def main():
    parser = argparse.ArgumentParser(description="Git commit com historico")
    parser.add_argument("--message", required=True, help="Mensagem do commit")
    parser.add_argument("--files", help="Arquivos a comitar (separados por espaco)")
    parser.add_argument("--project", help="Caminho base do projeto")
    
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
    if not staged or all(f == "" for f in staged):
        print("Nenhum arquivo para comitar")
        return
    
    _, stderr, code = run_git_command(["git", "commit", "-m", args.message], project_path)
    
    if code != 0:
        if "nothing to commit" in stderr.lower():
            print("Nenhum arquivo para comitar")
            return
        print(f"Erro ao fazer commit: {stderr}")
        return
    
    commit_hash = get_commit_hash(project_path)
    commit_id = commit_hash[:7]
    
    create_commit_file(project_path, commit_id, args.message, staged, commit_hash)
    update_readme(project_path, args.message, staged)
    
    print(f"Commit realizado: {commit_id}")
    
    print("Fazendo pull antes do push...")
    _, pull_stderr, pull_code = run_git_command(["git", "pull", "--rebase"], project_path)
    if pull_code != 0:
        print(f"Aviso no pull: {pull_stderr}")
    
    print("Fazendo push...")
    _, push_stderr, push_code = run_git_command(["git", "push"], project_path)
    if push_code != 0:
        print(f"Erro no push: {push_stderr}")
    else:
        print("Push realizado com sucesso")

if __name__ == "__main__":
    main()
