#!/usr/bin/env python3
"""
Edit Skill Factory - Editor de skills existentes.
Lista skills, permite selecionar e editar conteudo/triggers/descricao.
Re-executa AST automaticamente apos edicao.
"""

import os
import sys
import subprocess
import tempfile

SKILLS_DIR = os.path.expanduser("~/.config/opencode/skills")
MD_TO_AST_SCRIPT = os.path.join(SKILLS_DIR, "markdown-to-ast", "md_to_ast.py")


def list_skills() -> list:
    """Lista todas as skills existentes."""
    skills = []
    if not os.path.isdir(SKILLS_DIR):
        return skills

    for name in sorted(os.listdir(SKILLS_DIR)):
        skill_path = os.path.join(SKILLS_DIR, name)
        skill_file = os.path.join(skill_path, "SKILL.md")

        if os.path.isdir(skill_path) and os.path.isfile(skill_file):
            # Extrai description do frontmatter
            description = ""
            try:
                with open(skill_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Parse frontmatter
                    lines = content.split('\n')
                    in_frontmatter = False
                    for line in lines:
                        if line.strip() == '---':
                            if not in_frontmatter:
                                in_frontmatter = True
                            else:
                                break
                        elif in_frontmatter and line.startswith('description:'):
                            description = line.split(':', 1)[1].strip()
                            break
            except:
                pass

            skills.append({"name": name, "path": skill_file, "description": description})
    return skills


def read_skill_content(skill_file: str) -> tuple:
    """Le o conteudo de uma skill. Retorna (frontmatter_dict, body_content)."""
    try:
        with open(skill_file, 'r', encoding='utf-8') as f:
            content = f.read()

        lines = content.split('\n')
        frontmatter = {}
        body_lines = []
        in_frontmatter = False
        frontmatter_done = False

        for i, line in enumerate(lines):
            if line.strip() == '---':
                if not in_frontmatter:
                    in_frontmatter = True
                else:
                    frontmatter_done = True
                    continue
            elif in_frontmatter and not frontmatter_done:
                if ':' in line:
                    key, val = line.split(':', 1)
                    frontmatter[key.strip()] = val.strip()
            elif frontmatter_done:
                body_lines.append(line)

        return frontmatter, "\n".join(body_lines)
    except Exception as e:
        return {}, ""


def write_skill(skill_file: str, frontmatter: dict, body: str):
    """Escreve o conteudo da skill com frontmatter."""
    with open(skill_file, 'w', encoding='utf-8') as f:
        f.write("---\n")
        for key, val in frontmatter.items():
            f.write(f"{key}: {val}\n")
        f.write("---\n")
        f.write(body)
        f.write("\n")


def run_md_to_ast(file_path: str, verbose: bool = True):
    """Roda o script md_to_ast.py para um arquivo."""
    try:
        args = ["python3", MD_TO_AST_SCRIPT, "--path", file_path]
        if verbose:
            args.append("--verbose")
        result = subprocess.run(args, capture_output=True, text=True, timeout=30)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def main():
    print("=== Edit Skill Factory - Editor de Skills ===\n")

    # Lista skills
    skills = list_skills()
    if not skills:
        print("Nenhuma skill encontrada!")
        return

    print(f"Encontradas {len(skills)} skill(s):\n")
    for i, skill in enumerate(skills, 1):
        desc = skill['description'][:60] + "..." if len(skill['description']) > 60 else skill['description']
        print(f"  {i:2d}. {skill['name']}")
        if desc:
            print(f"      {desc}")
        print()

    # Seleciona skill
    try:
        choice = input(f"Numero da skill para editar (1-{len(skills)}): ").strip()
        if not choice:
            print("Cancelado.")
            return
        idx = int(choice) - 1
        if idx < 0 or idx >= len(skills):
            print("Indice invalido.")
            return
    except ValueError:
        print("Entrada invalida.")
        return

    skill = skills[idx]
    skill_file = skill['path']

    print(f"\nEditando: {skill['name']}")

    # Le conteudo atual
    frontmatter, body = read_skill_content(skill_file)

    # Edita campos
    print("\n--- Dados do Frontmatter ---")
    print("(Pressione Enter para manter o valor atual)\n")

    # Name (apenas visual, nao pode mudar)
    current_name = frontmatter.get('name', skill['name'])
    print(f"Nome atual: {current_name}")
    print("(Nome nao pode ser alterado. Use 'renomear-arquivos-referencias' para renomear.)\n")

    # Description
    current_desc = frontmatter.get('description', '')
    new_desc = input(f"Descricao atual: {current_desc}\nNova descricao: ").strip()
    if new_desc:
        frontmatter['description'] = new_desc

    # Triggers
    current_triggers = frontmatter.get('triggers', '[]')
    print(f"Triggers atual: {current_triggers}")
    new_triggers = input("Novos triggers (Enter para manter, 'list' para ver lista): ").strip()
    if new_triggers.lower() == 'list':
        # Mostra triggers atuais
        print(f"\nTriggers atuais: {current_triggers}")
        new_triggers = input("Novos triggers (ou Enter para manter): ").strip()
    if new_triggers:
        frontmatter['triggers'] = new_triggers

    # Conteudo
    print("\n--- Conteudo do Skill ---")
    print("(O conteudo sera aberto no editor de texto padrao)\n")

    # Usa editor padrao ou fallback
    editor = os.environ.get('EDITOR', 'nano' if os.path.exists('/bin/nano') else 'vim')
    if editor == 'nano' and not os.path.exists('/bin/nano'):
        editor = 'vim'

    # Salva body temporario para editar
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as tf:
        tf.write(body)
        temp_file = tf.name

    try:
        # Abre editor
        subprocess.run([editor, temp_file], check=True)

        # Le resultado
        with open(temp_file, 'r', encoding='utf-8') as f:
            new_body = f.read()
    finally:
        os.unlink(temp_file)

    # Confirma salvamento
    print("\n--- Preview do conteudo (primeiras 10 linhas) ---")
    preview = new_body.split('\n')[:10]
    for line in preview:
        print(line)
    print("...")

    confirm = input("\nSalvar alteracoes? (s/n): ").strip().lower()
    if confirm != 's':
        print("Alteracoes descartadas.")
        return

    # Salva skill
    write_skill(skill_file, frontmatter, new_body)
    print(f"\nSkill salva: {skill_file}")

    # Re-gera AST
    print("\nRe-gerando AST...")
    success, stdout, stderr = run_md_to_ast(skill_file, verbose=True)
    if success:
        print("AST atualizado com sucesso!")
    else:
        print(f"Erro ao gerar AST: {stderr}")

    print("\nPara atualizar o grafo global:")
    print(f"  graphify update {SKILLS_DIR}")


if __name__ == "__main__":
    main()
