#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse
from datetime import datetime

def run_git_command(args, cwd):
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def get_commit_files(project_path):
    commits_dir = os.path.join(project_path, "commits")
    if not os.path.exists(commits_dir):
        return []
    
    files = []
    for root, dirs, filenames in os.walk(commits_dir):
        for f in filenames:
            if f.startswith("commit-") and f.endswith(".md"):
                filepath = os.path.join(root, f)
                mtime = os.path.getmtime(filepath)
                files.append((mtime, filepath))
    
    files.sort(reverse=True)
    return files

def parse_commit_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    lines = content.split("\n")
    commit_id = ""
    message = ""
    files_list = []
    hash_git = ""
    
    section = None
    for line in lines:
        if line.startswith("# Commit "):
            parts = line.split(" - ")
            if len(parts) >= 2:
                commit_id = parts[1].strip()
        elif line.startswith("## Mensagem"):
            section = "message"
        elif line.startswith("## Arquivos"):
            section = "files"
        elif line.startswith("## Hash"):
            section = "hash"
        elif section == "message" and line.strip():
            message = line.strip()
        elif section == "files" and line.startswith("- "):
            files_list.append(line[2:].strip())
        elif section == "hash" and line.strip():
            hash_git = line.strip()
    
    return commit_id, message, files_list, hash_git

def get_git_commits(project_path, count=5):
    stdout, _, _ = run_git_command(["git", "log", f"--pretty=format:%H|%s", f"-{count}"], project_path)
    commits = []
    for line in stdout.split("\n"):
        if "|" in line:
            hash_git, message = line.split("|", 1)
            commits.append({
                "hash": hash_git[:7],
                "message": message.strip(),
                "full_hash": hash_git
            })
    return commits

def create_commit_file(project_path, commit_id, message, files, commit_hash):
    commits_dir = os.path.join(project_path, "commits")
    if not os.path.exists(commits_dir):
        os.makedirs(commits_dir)
    
    timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    filename = f"commit-{commit_id}-{timestamp}.md"
    filepath = os.path.join(commits_dir, filename)
    
    files_list = "\n".join([f"- {f}" for f in files]) if files else "- (todos os arquivos)"
    
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
    
    print(f"Arquivo criado: {filepath}")
    return filepath

def main():
    parser = argparse.ArgumentParser(description="Recuperar comentarios de commits da pasta commits/")
    parser.add_argument("--project", required=True, help="Caminho base do projeto")
    parser.add_argument("--count", type=int, default=5, help="Numero de commits a recuperar (default: 5)")
    parser.add_argument("--generate", action="store_true", help="Gerar arquivos de commit a partir do git log")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.project):
        print(f"Projeto nao encontrado: {args.project}")
        return
    
    files = get_commit_files(args.project)
    
    if args.generate:
        print(f"\n=== Gerando arquivos de commit a partir do git log ({args.count} ultimos) ===\n")
        git_commits = get_git_commits(args.project, args.count)
        
        if not git_commits:
            print("Nenhum commit encontrado no git")
            return
        
        for commit in git_commits:
            create_commit_file(args.project, commit["hash"], commit["message"], [], commit["full_hash"])
        
        print(f"\n{len(git_commits)} arquivos de commit gerados em: {os.path.join(args.project, 'commits')}")
        return
    
    if not files:
        print("Nenhum arquivo de commit encontrado na pasta commits/")
        print("Use --generate para criar arquivos a partir do git log")
        return
    
    count = min(args.count, len(files))
    
    print(f"\n=== Ultimas {count} Alteracoes ===\n")
    
    for i, (mtime, filepath) in enumerate(files[:count], 1):
        commit_id, message, files_list, hash_git = parse_commit_file(filepath)
        
        print(f"Commit #{i}: {commit_id}")
        print(f"Mensagem: {message}")
        if hash_git:
            print(f"Hash: {hash_git}")
        if files_list:
            print(f"Arquivos:")
            for f in files_list:
                print(f"  - {f}")
        print("-" * 50)
    
    print(f"\nTotal de commits registrados: {len(files)}")

if __name__ == "__main__":
    main()