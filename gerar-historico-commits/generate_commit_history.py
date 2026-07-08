#!/usr/bin/env python3
"""
Script para gerar arquivos de histórico de commits do Git.
Formato: commits/yyyy/mm/dd/commit-[hash]-[timestamp].md

Uso:
    python3 generate_commit_history.py --repo /caminho/do/repo --output /caminho/output
    python3 generate_commit_history.py  # usa caminhos padrão do skill
"""
import subprocess
import os
import argparse
from datetime import datetime
from pathlib import Path

# Padrão do skill (pode ser sobrescrito por args)
DEFAULT_REPO_PATH = "/www/wwwroot/sac.moedadetroka.com.br/wp-content/themes/moedadetroka"
DEFAULT_OUTPUT_BASE = "/www/wwwroot/sac.moedadetroka.com.br/commits"

def run_git(args, cwd=DEFAULT_REPO_PATH):
    result = subprocess.run(
        ["git"] + args,
        cwd=cwd,
        capture_output=True,
        text=True
    )
    return result.stdout.strip(), result.stderr

def get_commit_details(commit_hash, repo_path):
    """Extrai detalhes de um commit específico."""
    # Formato: hash|message|author_date
    info, _ = run_git([
        "log", "--format=%H|%s|%ad",
        "--date=format:%Y-%m-%d %H:%M:%S", "-1", commit_hash
    ], cwd=repo_path)

    if not info:
        return None

    parts = info.split("|", 2)
    if len(parts) < 3:
        return None

    hash_val, message, date_str = parts

    # Parse date
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except:
        return None

    # Get files changed
    files_out, _ = run_git(["diff-tree", "--no-commit-id", "--name-only", "-r", commit_hash], cwd=repo_path)
    files = [f for f in files_out.split("\n") if f.strip()]

    # Get diff (limited to first 500k chars for large diffs)
    diff_out, _ = run_git(["diff", f"{commit_hash}~1..{commit_hash}"], cwd=repo_path)

    return {
        "hash": hash_val,
        "message": message,
        "date": dt,
        "files": files,
        "diff": diff_out[:500000] if diff_out else ""
    }

def create_commit_file(commit_info, output_base):
    """Cria arquivo de histórico para um commit."""
    if not commit_info:
        return False

    dt = commit_info["date"]

    # Create directory: commits/yyyy/mm/dd/
    dir_path = Path(output_base) / f"{dt.year}" / f"{dt.month:02d}" / f"{dt.day:02d}"
    dir_path.mkdir(parents=True, exist_ok=True)

    # Filename: commit-[hash]-[yyyy-mm-dd-hh-mm-ss].md
    filename = f"commit-{commit_info['hash'][:12]}-{dt.strftime('%Y-%m-%d-%H-%M-%S')}.md"
    file_path = dir_path / filename

    # Build content
    files_list = "\n".join([f"- {f}" for f in commit_info["files"]]) if commit_info["files"] else "- (no files)"

    content = f"""# Commit {commit_info['hash'][:12]} - {dt.strftime('%d/%m/%Y %H:%M:%S')}

## Mensagem
{commit_info['message']}

## Arquivos
{files_list}

## Hash
{commit_info['hash']}

## Diff
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        if commit_info["diff"]:
            f.write(commit_info["diff"])

    return str(file_path)

def main():
    parser = argparse.ArgumentParser(description="Gera histórico de commits do Git")
    parser.add_argument("--repo", default=DEFAULT_REPO_PATH, help="Caminho do repositório Git")
    parser.add_argument("--output", default=DEFAULT_OUTPUT_BASE, help="Diretório base para salvar os arquivos")
    args = parser.parse_args()

    repo_path = args.repo
    output_base = args.output

    print("=== Gerador de Histórico de Commits ===")
    print(f"Repo: {repo_path}")
    print(f"Output: {output_base}")
    print()

    # Get all commits
    commits_out, _ = run_git(["rev-list", "--all"], cwd=repo_path)
    all_commits = [c for c in commits_out.split("\n") if c.strip()]

    print(f"Total de commits encontrados: {len(all_commits)}")
    print()

    created = 0
    skipped = 0

    for i, commit_hash in enumerate(all_commits):
        if (i + 1) % 50 == 0:
            print(f"Processando commit {i+1}/{len(all_commits)}...")

        # Check if file already exists
        info, _ = run_git([
            "log", "--format=%ad",
            "--date=format:%Y-%m-%d %H:%M:%S", "-1", commit_hash
        ], cwd=repo_path)

        if info:
            try:
                dt = datetime.strptime(info, "%Y-%m-%d %H:%M:%S")
                filename = f"commit-{commit_hash[:12]}-{dt.strftime('%Y-%m-%d-%H-%M-%S')}.md"
                dir_path = Path(output_base) / f"{dt.year}" / f"{dt.month:02d}" / f"{dt.day:02d}"
                file_path = dir_path / filename

                if file_path.exists():
                    skipped += 1
                    continue
            except:
                pass

        details = get_commit_details(commit_hash, repo_path)
        if details:
            result = create_commit_file(details, output_base)
            if result:
                created += 1
        else:
            skipped += 1

    print()
    print(f"=== Concluído ===")
    print(f"Arquivos criados: {created}")
    print(f"Arquivos ignorados (já existem): {skipped}")
    print(f"Total processado: {created + skipped}")

if __name__ == "__main__":
    main()
