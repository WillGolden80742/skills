#!/usr/bin/env python3
"""
Markdown to AST Converter
Extrai estrutura de arquivos markdown como nós no grafo do graphify.
Cada .md gera um .json correspondente no mesmo diretório.
"""

import os
import re
import json
import argparse
from pathlib import Path
from datetime import datetime


def extract_markdown_structure(content: str, file_path: str) -> dict:
    """Extrai estrutura AST de um arquivo markdown."""
    lines = content.split('\n')
    nodes = []
    edges = []
    current_section = None
    section_stack = []
    section_counter = 0

    # Patterns
    header_pattern = re.compile(r'^(#{1,6})\s+(.+)$')
    code_block_start = re.compile(r'^```(\w*)\s*$')
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')
    list_pattern = re.compile(r'^[\s]*[-*+]\s+(.+)$')
    image_pattern = re.compile(r'!\[([^\]]*)\]\(([^\)]+)\)')

    in_code_block = False
    code_lang = None

    for line_num, line in enumerate(lines, 1):
        # Code blocks
        if match := code_block_start.match(line):
            if not in_code_block:
                in_code_block = True
                code_lang = match.group(1) or 'text'
            else:
                in_code_block = False
                node_id = f"md_{Path(file_path).stem}_code_{section_counter}"
                nodes.append({
                    "id": node_id,
                    "label": f"Code: {code_lang}",
                    "type": "code_block",
                    "language": code_lang,
                    "file": file_path,
                    "community": 999
                })
                if current_section:
                    edges.append({"from": current_section, "to": node_id, "relation": "contains"})
                section_counter += 1
            continue

        if in_code_block:
            continue

        # Headers
        if match := header_pattern.match(line):
            level = len(match.group(1))
            title = match.group(2).strip()

            node_id = f"md_{Path(file_path).stem}_h{level}_{section_counter}"
            nodes.append({
                "id": node_id,
                "label": title[:80],
                "type": "heading",
                "level": level,
                "file": file_path,
                "community": 999
            })

            # Manage hierarchy
            while section_stack and section_stack[-1]['level'] >= level:
                section_stack.pop()

            parent = section_stack[-1]['id'] if section_stack else None
            if parent:
                edges.append({"from": parent, "to": node_id, "relation": "section"})

            section_stack.append({'id': node_id, 'level': level})
            current_section = node_id
            section_counter += 1
            continue

        # Links
        for match in link_pattern.finditer(line):
            link_text = match.group(1)
            link_url = match.group(2)
            node_id = f"md_{Path(file_path).stem}_link_{section_counter}"
            nodes.append({
                "id": node_id,
                "label": link_text[:50],
                "type": "link",
                "url": link_url,
                "file": file_path,
                "community": 999
            })
            if current_section:
                edges.append({"from": current_section, "to": node_id, "relation": "contains"})
            section_counter += 1

        # Images
        for match in image_pattern.finditer(line):
            alt = match.group(1)
            src = match.group(2)
            node_id = f"md_{Path(file_path).stem}_image_{section_counter}"
            nodes.append({
                "id": node_id,
                "label": alt[:50] or 'Image',
                "type": "image",
                "src": src,
                "file": file_path,
                "community": 999
            })
            if current_section:
                edges.append({"from": current_section, "to": node_id, "relation": "contains"})
            section_counter += 1

        # List items
        if match := list_pattern.match(line):
            item = match.group(1).strip()
            node_id = f"md_{Path(file_path).stem}_list_{section_counter}"
            nodes.append({
                "id": node_id,
                "label": item[:80],
                "type": "list_item",
                "file": file_path,
                "community": 999
            })
            if current_section:
                edges.append({"from": current_section, "to": node_id, "relation": "contains"})
            section_counter += 1

    return {"nodes": nodes, "edges": edges}


def find_markdown_files(path: str) -> list:
    """Encontra todos os arquivos .md em um diretório ou arquivo único."""
    if os.path.isfile(path):
        return [path] if path.lower().endswith('.md') else []

    md_files = []
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', 'graphify-out']]
        for file in files:
            if file.lower().endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files


def md_to_json_path(md_path: str) -> str:
    """Converte caminho .md para .json (mesmo diretório, mesmo nome)."""
    base = os.path.splitext(md_path)[0]
    return base + ".json"


def save_per_file_ast(md_file: str, result: dict) -> str:
    """Salva AST de um único arquivo .md como .json no mesmo diretório."""
    json_path = md_to_json_path(md_file)

    data = {
        "source": md_file,
        "generated_at": datetime.now().isoformat(),
        "nodes": result['nodes'],
        "edges": result['edges']
    }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return json_path


def main():
    parser = argparse.ArgumentParser(description='Converte arquivos .md em AST (.json no mesmo dir)')
    parser.add_argument('--path', '-p', default='.', help='Diretório ou arquivo .md')
    parser.add_argument('--verbose', '-v', action='store_true', help='Mostra detalhes')
    parser.add_argument('--dry-run', action='store_true', help='Simula sem salvar')
    args = parser.parse_args()

    path = os.path.abspath(args.path)
    print(f"\n=== Markdown to AST ===")
    print(f"Path: {path}\n")

    md_files = find_markdown_files(path)
    print(f"Encontrados {len(md_files)} arquivo(s) .md\n")

    if not md_files:
        print("Nenhum arquivo .md encontrado!")
        return

    stats = {"files": 0, "headings": 0, "code_blocks": 0, "links": 0,
             "images": 0, "list_items": 0}

    for md_file in md_files:
        if args.verbose:
            print(f"Processando: {md_file}")

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            if args.verbose:
                print(f"  Erro: {e}")
            continue

        result = extract_markdown_structure(content, md_file)

        for node in result['nodes']:
            t = node.get('type', 'unknown')
            if t == 'heading': stats['headings'] += 1
            elif t == 'code_block': stats['code_blocks'] += 1
            elif t == 'link': stats['links'] += 1
            elif t == 'image': stats['images'] += 1
            elif t == 'list_item': stats['list_items'] += 1

        stats['files'] += 1

        if not args.dry_run:
            json_path = save_per_file_ast(md_file, result)
            if args.verbose:
                print(f"  -> {json_path}")

        if args.verbose:
            print(f"  - {len(result['nodes'])} nodes")

    print(f"\n=== Resumo ===")
    print(f"Arquivos processados: {stats['files']}")
    print(f"Headings: {stats['headings']}")
    print(f"Code blocks: {stats['code_blocks']}")
    print(f"Links: {stats['links']}")
    print(f"Images: {stats['images']}")
    print(f"List items: {stats['list_items']}")

    if args.dry_run:
        print("\n[Dry-run] Nenhum arquivo salvo.")
    else:
        print(f"\nASTs salvos como .json no mesmo diretório dos .md originais.")


if __name__ == '__main__':
    main()
