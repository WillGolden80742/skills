import os
import shutil

SKILLS_DIR = os.path.expanduser("~/.config/opencode/skills")

def list_skills():
    if not os.path.exists(SKILLS_DIR):
        print("Diretorio de skills nao encontrado.")
        return []

    skills = [d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))]
    skills.sort()

    print("\n=== Skills Disponiveis ===\n")
    for i, skill in enumerate(skills, 1):
        skill_path = os.path.join(SKILLS_DIR, skill, "SKILL.md")
        description = ""
        if os.path.exists(skill_path):
            with open(skill_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("description:"):
                        description = line.replace("description:", "").strip()
                        break
        print(f"  {i}. {skill}")
        if description:
            print(f"     -> {description}")
    print()
    return skills

def remove_skill(skill_name):
    skill_path = os.path.join(SKILLS_DIR, skill_name)
    if os.path.exists(skill_path):
        confirm = input(f"Tem certeza que deseja remover '{skill_name}'? (s/n): ").strip().lower()
        if confirm == "s":
            shutil.rmtree(skill_path)
            print(f"Skill '{skill_name}' removida com sucesso.")
        else:
            print("Remocao cancelada.")
    else:
        print(f"Skill '{skill_name}' nao encontrada.")

def update_skill(skill_name):
    skill_path = os.path.join(SKILLS_DIR, skill_name, "SKILL.md")
    if os.path.exists(skill_path):
        print(f"Abrindo {skill_path} para edicao...")
        os.startfile(skill_path)
    else:
        print(f"Skill '{skill_name}' nao encontrada.")

def main():
    print("=== Skill Refactory - Gerenciar Skills ===\n")
    print("Comandos:")
    print("  - Digite numero para remover um skill")
    print("  - Digite 'u[numero]' para atualizar (ex: u3)")
    print("  - Digite 'q' para sair\n")

    skills = list_skills()

    if not skills:
        print("Nenhum skill encontrado.")
        return

    while True:
        choice = input("Escolha uma opcao: ").strip()

        if choice == "q":
            print("Saindo...")
            break

        if choice.startswith("u"):
            try:
                idx = int(choice[1:]) - 1
                if 0 <= idx < len(skills):
                    update_skill(skills[idx])
                else:
                    print("Numero invalido.")
            except ValueError:
                print("Entrada invalida.")

        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(skills):
                    remove_skill(skills[idx])
                    skills = list_skills()
                else:
                    print("Numero invalido.")
            except ValueError:
                print("Entrada invalida.")

if __name__ == "__main__":
    main()