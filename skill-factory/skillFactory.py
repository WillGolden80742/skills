import os
import sys

SKILLS_DIR = os.path.expanduser("~/.config/opencode/skills")

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

    print(f"\nSkill criada com sucesso em: {skill_file}")

if __name__ == "__main__":
    main()
