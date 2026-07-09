import os
import sys
import subprocess

SKILLS_DIR = os.path.expanduser("~/.config/opencode/skills")
MD_TO_AST_SCRIPT = os.path.join(SKILLS_DIR, "markdown-to-ast", "md_to_ast.py")


def run_md_to_ast(file_path: str):
    """Roda o script md_to_ast.py para um arquivo específico."""
    try:
        result = subprocess.run(
            ["python3", MD_TO_AST_SCRIPT, "--path", file_path, "--dry-run"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def main():
    print("=== Skill Factory - Criador de Skills ===\n")

    name = input("Nome do skill (sem espacos, use hifens): ").strip().lower()
    if not name:
        print("Nome nao pode ser vazio.")
        return

    description = input("Descricao do skill: ").strip()
    if not description:
        print("Descricao nao pode ser vazia.")
        return

    triggers_input = input("Triggers (separados por virgula): ").strip()
    triggers = [t.strip() for t in triggers_input.split(",") if t.strip()]

    print("\nCole o conteudo/conhecimento do skill (linha vazia para terminar):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    content = "\n".join(lines)

    skill_dir = os.path.join(SKILLS_DIR, name)
    os.makedirs(skill_dir, exist_ok=True)

    skill_file = os.path.join(skill_dir, "SKILL.md")
    with open(skill_file, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"name: {name}\n")
        f.write(f"description: {description}\n")
        f.write(f"triggers: {triggers}\n")
        f.write("---\n\n")
        f.write(content)
        f.write("\n")

    print(f"\nSkill criada: {skill_file}")

    # Rodar md_to_ast.py para extrair AST
    print("\nExtraindo AST do markdown...")
    try:
        result = subprocess.run(
            ["python3", MD_TO_AST_SCRIPT, "--path", skill_file, "--verbose"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            print(result.stdout)
            print(f"\nAST gerado com sucesso!")
        else:
            print(f"Erro ao gerar AST: {result.stderr}")
    except subprocess.TimeoutExpired:
        print("Timeout ao gerar AST")
    except Exception as e:
        print(f"Erro: {e}")

    print("\nPara atualizar o grafo global:")
    print(f"  graphify update {SKILLS_DIR}")


if __name__ == "__main__":
    main()
