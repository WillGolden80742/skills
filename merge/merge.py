import os
import sys
import fnmatch


def load_ignore_patterns(target_path, script_path):
    patterns = []

    # 1️⃣ tenta no diretório alvo
    target_ignore = os.path.join(target_path, ".mergeignore")

    # 2️⃣ fallback: diretório do script
    script_ignore = os.path.join(script_path, ".mergeignore")

    ignore_file = None

    if os.path.isfile(target_ignore):
        ignore_file = target_ignore
        print(f"Usando .mergeignore do alvo: {ignore_file}")
    elif os.path.isfile(script_ignore):
        ignore_file = script_ignore
        print(f"Usando .mergeignore do script: {ignore_file}")
    else:
        print("Nenhum .mergeignore encontrado.")
        return patterns

    with open(ignore_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                patterns.append(line)

    return patterns


def should_ignore(path, patterns, base_path):
    rel_path = os.path.relpath(path, base_path).replace("\\", "/")

    for pattern in patterns:
        pattern = pattern.rstrip("/")

        # ignora diretórios inteiros
        if rel_path.startswith(pattern):
            return True

        # ignora por wildcard
        if fnmatch.fnmatch(rel_path, pattern):
            return True

    return False


def merge_files_in_directory(base_path, script_path, output_filename="merged_output.txt"):
    print(f"Iniciando em: {base_path}")

    ignore_patterns = load_ignore_patterns(base_path, script_path)
    output_path = os.path.join(base_path, output_filename)

    try:
        with open(output_path, 'w', encoding='utf-8') as outfile:

            for root, dirs, files in os.walk(base_path):

                # 🔥 impede entrar em pastas ignoradas
                dirs[:] = [
                    d for d in dirs
                    if not should_ignore(os.path.join(root, d), ignore_patterns, base_path)
                ]

                for filename in files:
                    file_path = os.path.join(root, filename)

                    if filename == output_filename:
                        continue

                    if should_ignore(file_path, ignore_patterns, base_path):
                        print(f"Ignorado: {file_path}")
                        continue

                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                            outfile.write(f"\n--- {file_path} ---\n\n")
                            outfile.write(infile.read())

                        print(f"OK: {file_path}")

                    except Exception as e:
                        print(f"Erro: {file_path} -> {e}")

        print(f"\nFinalizado: {output_path}")

    except Exception as e:
        print(f"Erro geral: {e}")


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    if len(sys.argv) > 1:
        base_dir = sys.argv[1].strip('"').strip("'")
    else:
        base_dir = script_dir

    if not os.path.isdir(base_dir):
        print(f"Caminho inválido: {base_dir}")
    else:
        merge_files_in_directory(base_dir, script_dir)
