#!/usr/bin/env python3
"""
Script para gerar arquivos de histórico de commits do Git (sem AST por padrão).
Formato: commits/yyyy/mm/dd/commit-[hash]-[timestamp].md
AST (opcional, via --ast) salvo em: commits/yyyy/mm/dd/ast/[hash]-[filename].json

Uso:
    python3 generate_commit_history.py --repo /caminho/do/repo --output /caminho/output
    python3 generate_commit_history.py  # usa caminhos padrão do skill
"""
import subprocess
import os
import argparse
import json
import ast
import re
from datetime import datetime
from pathlib import Path

# Padrão do skill (pode ser sobrescrito por args)
DEFAULT_REPO_PATH = "/www/wwwroot/sac.moedadetroka.com.br/wp-content/themes/moedadetroka"
DEFAULT_OUTPUT_BASE = "/www/wwwroot/sac.moedadetroka.com.br/commits"

# Extensões suportadas para AST
AST_PARSERS = {
    '.py': 'python',
    '.js': 'javascript',
    '.jsx': 'javascript',
    '.ts': 'typescript',
    '.tsx': 'typescript',
    '.php': 'php',
    '.html': 'html',
    '.css': 'css',
}

def run_git(args, cwd=DEFAULT_REPO_PATH):
    result = subprocess.run(
        ["git"] + args,
        cwd=cwd,
        capture_output=True,
        text=True
    )
    return result.stdout.strip(), result.stderr

def extract_python_ast(content):
    """Extrai AST de código Python."""
    try:
        tree = ast.parse(content)
        return extract_node_details(tree)
    except:
        return None

def extract_node_details(node, depth=0):
    """Extrai detalhes de um nó AST recursivamente."""
    if depth > 15:  # Limite de profundidade
        return None
    
    result = {
        "type": type(node).__name__,
        "line": getattr(node, 'lineno', None),
        "col": getattr(node, 'col_offset', None),
    }
    
    # Extrair nomes de funções, classes, variáveis
    if isinstance(node, ast.FunctionDef):
        result['name'] = node.name
        result['args'] = [arg.arg for arg in node.args.args]
    elif isinstance(node, ast.ClassDef):
        result['name'] = node.name
        result['bases'] = [getattr(b, 'id', str(b)) for b in node.bases]
    elif isinstance(node, ast.Assign):
        result['targets'] = [getattr(t, 'id', str(t)) for t in node.targets]
    elif isinstance(node, ast.Call):
        result['func'] = getattr(node.func, 'id', getattr(node.func, 'attr', str(node.func)))
    
    # Filhos
    children = []
    for child in ast.iter_child_nodes(node):
        child_detail = extract_node_details(child, depth + 1)
        if child_detail:
            children.append(child_detail)
    
    if children:
        result['children'] = children
    
    return result

def extract_js_ast(content):
    """Extrai estrutura básica de JavaScript/TypeScript."""
    try:
        # Padrões regex para encontrar funções, classes, variáveis
        functions = re.findall(r'(?:function|const|let|var|class|export|import)[\s\n]+(?:[\w$]+[\s\n]+)?(?:=[\s\n]+)?(?:async[\s\n]+)?(?:function[\s\n]+)?([\w$]+)[\s\n]*\(', content, re.MULTILINE)
        classes = re.findall(r'class[\s]+([\w$]+)', content)
        exports = re.findall(r'export[\s]+(?:default[\s]+)?(?:const|let|var|function|class)[\s]+([\w$]+)', content)
        imports = re.findall(r'import[\s]+(?:{[^}]+}|[^;]+)[\s]+from[\s]+[\'"]([^\'"]+)[\'"]', content)
        
        return {
            "type": "Program",
            "functions": functions,
            "classes": classes,
            "exports": exports,
            "imports": imports,
        }
    except:
        return None

def extract_php_ast(content):
    """Extrai estrutura básica de PHP."""
    try:
        # Padrões para PHP
        functions = re.findall(r'function[\s]+([\w$]+)[\s]*\(', content)
        classes = re.findall(r'class[\s]+([\w$]+)', content)
        methods = re.findall(r'(?:public|private|protected)[\s]+function[\s]+([\w$]+)[\s]*\(', content)
        namespaces = re.findall(r'namespace[\s]+([\w$]+);', content)
        
        return {
            "type": "Program",
            "functions": functions,
            "classes": classes,
            "methods": methods,
            "namespaces": namespaces,
        }
    except:
        return None

def extract_html_ast(content):
    """Extrai estrutura básica de HTML."""
    try:
        tags = re.findall(r'<([a-zA-Z][a-zA-Z0-9]*)', content)
        ids = re.findall(r'id=["\']([^"\']+)["\']', content)
        classes = re.findall(r'class=["\']([^"\']+)["\']', content)
        
        return {
            "type": "Document",
            "tags": list(set(tags)),
            "ids": ids,
            "classes": list(set(classes)),
        }
    except:
        return None

def extract_css_ast(content):
    """Extrai estrutura básica de CSS."""
    try:
        rules = re.findall(r'([^{]+){', content)
        properties = re.findall(r'([a-zA-Z-]+)[\s]*:', content)
        
        return {
            "type": "Stylesheet",
            "selectors": [r.strip() for r in rules if r.strip()],
            "properties": list(set(properties)),
        }
    except:
        return None

def extract_ast(content, filepath):
    """Extrai AST baseado na extensão do arquivo."""
    ext = Path(filepath).suffix.lower()
    
    if ext == '.py':
        return extract_python_ast(content)
    elif ext in ['.js', '.jsx', '.ts', '.tsx']:
        return extract_js_ast(content)
    elif ext == '.php':
        return extract_php_ast(content)
    elif ext == '.html':
        return extract_html_ast(content)
    elif ext == '.css':
        return extract_css_ast(content)
    
    return None

def get_file_content_at_commit(commit_hash, filepath, repo_path):
    """Obtém o conteúdo de um arquivo em um commit específico."""
    full_path = os.path.join(repo_path, filepath)
    output, _ = run_git(["show", f"{commit_hash}:{filepath}"], cwd=repo_path)
    return output

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

def extract_file_ast_content(commit_hash, files, repo_path):
    """Extrai AST de todos os arquivos modificados no commit."""
    ast_data = {}
    
    for filepath in files:
        try:
            content = get_file_content_at_commit(commit_hash, filepath, repo_path)
            if content:
                ast = extract_ast(content, filepath)
                if ast:
                    ast_data[filepath] = ast
        except Exception as e:
            pass  # Ignora arquivos que não podem ser processados
    
    return ast_data

def create_commit_file(commit_info, output_base, ast_data=None):
    """Cria arquivo de histórico para um commit."""
    if not commit_info:
        return False

    dt = commit_info["date"]

    # Create directory: commits/yyyy/mm/dd/
    dir_path = Path(output_base) / f"{dt.year}" / f"{dt.month:02d}" / f"{dt.day:02d}"
    dir_path.mkdir(parents=True, exist_ok=True)

    # Create AST directory: commits/yyyy/mm/dd/ast/ (somente se houver AST)
    if ast_data:
        ast_dir_path = dir_path / "ast"
        ast_dir_path.mkdir(parents=True, exist_ok=True)

    # Filename: commit-[yyyy-mm-dd-hh-mm-ss]-[hash].md
    filename = f"commit-{dt.strftime('%Y-%m-%d-%H-%M-%S')}-{commit_info['hash'][:12]}.md"
    file_path = dir_path / filename

    # Build content
    files_list = "\n".join([f"- {f}" for f in commit_info["files"]]) if commit_info["files"] else "- (no files)"
    
    # AST summary
    ast_summary = []
    for filepath, ast in (ast_data or {}).items():
        if ast:
            ast_summary.append(f"- **{filepath}**: {ast.get('type', 'Unknown')}")

    content = f"""# Commit {commit_info['hash'][:12]} - {dt.strftime('%d/%m/%Y %H:%M:%S')}

## Mensagem
{commit_info['message']}

## Arquivos
{files_list}

## Hash
{commit_info['hash']}

## AST Resumo
{chr(10).join(ast_summary) if ast_summary else "- (sem AST)"}

## Diff
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        if commit_info["diff"]:
            f.write(commit_info["diff"])

    # Save AST files
    ast_files_created = 0
    for filepath, ast in (ast_data or {}).items():
        if ast:
            safe_filename = filepath.replace('/', '_').replace('\\', '_').replace('.', '_')
            ast_filename = f"{commit_info['hash'][:12]}_{safe_filename}.json"
            ast_file_path = ast_dir_path / ast_filename
            
            with open(ast_file_path, "w", encoding="utf-8") as f:
                json.dump({
                    "commit": commit_info['hash'][:12],
                    "file": filepath,
                    "ast": ast
                }, f, indent=2, ensure_ascii=False)
            ast_files_created += 1

    return str(file_path), ast_files_created

def main():
    parser = argparse.ArgumentParser(description="Gera histórico de commits do Git (sem AST por padrão)")
    parser.add_argument("--repo", default=DEFAULT_REPO_PATH, help="Caminho do repositório Git")
    parser.add_argument("--output", default=DEFAULT_OUTPUT_BASE, help="Diretório base para salvar os arquivos")
    parser.add_argument("--ast", action="store_true", help="Habilita geração de AST (desabilitada por padrão)")
    args = parser.parse_args()

    repo_path = args.repo
    output_base = args.output
    generate_ast = args.ast

    print("=== Gerador de Histórico de Commits ===")
    print(f"Repo: {repo_path}")
    print(f"Output: {output_base}")
    print(f"AST: {'Habilitado (via --ast)' if generate_ast else 'Desabilitado'}")
    print()

    # Get all commits
    commits_out, _ = run_git(["rev-list", "--all"], cwd=repo_path)
    all_commits = [c for c in commits_out.split("\n") if c.strip()]

    print(f"Total de commits encontrados: {len(all_commits)}")
    print()

    created = 0
    skipped = 0
    ast_files_total = 0

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
                filename = f"commit-{dt.strftime('%Y-%m-%d-%H-%M-%S')}-{commit_hash[:12]}.md"
                dir_path = Path(output_base) / f"{dt.year}" / f"{dt.month:02d}" / f"{dt.day:02d}"
                file_path = dir_path / filename

                if file_path.exists():
                    skipped += 1
                    continue
            except:
                pass

        details = get_commit_details(commit_hash, repo_path)
        if details:
            # Extrair AST se habilitado
            ast_data = None
            if generate_ast:
                ast_data = extract_file_ast_content(commit_hash, details["files"], repo_path)
            
            result, ast_count = create_commit_file(details, output_base, ast_data)
            if result:
                created += 1
                ast_files_total += ast_count
        else:
            skipped += 1

    print()
    print(f"=== Concluído ===")
    print(f"Arquivos MD criados: {created}")
    print(f"Arquivos ignorados (já existem): {skipped}")
    print(f"Arquivos AST gerados: {ast_files_total}")
    print(f"Total processado: {created + skipped}")

if __name__ == "__main__":
    main()