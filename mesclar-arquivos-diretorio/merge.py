import os
import sys
import fnmatch
import subprocess


SKILLS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_TREE_PY = os.path.join(SKILLS_DIR, "gerar-arvore-diretorios", "dir_tree.py")


def parse_dir_md(base_path):
    dir_md = os.path.join(base_path, "dir.md")
    if not os.path.isfile(dir_md):
        print(f"[AVISO] dir.md nao encontrado em: {dir_md}")
        return None
    files = set()
    stack = []
    with open(dir_md, "r", encoding="utf-8") as f:
        for line in f:
            raw = line.rstrip("\n")
            if not raw or raw.startswith("#") or raw.startswith("```"):
                continue
            if "-- " not in raw:
                continue
            depth = raw.index("-- ") // 4
            name = raw.split("-- ")[-1].strip()
            if not name:
                continue
            stack = stack[:depth]
            stack.append(name)
            rel = "/".join(stack)
            full = os.path.normpath(os.path.join(base_path, rel))
            if os.path.isfile(full):
                files.add(full)
    print(f"[INFO] dir.md: {len(files)} arquivos listados")
    return files


def show_directory_tree(target_path):
    print("\n" + "=" * 60)
    print("ARVORE DE DIRETORIO:")
    print("=" * 60)
    if os.path.isfile(DIR_TREE_PY):
        result = subprocess.run(
            [sys.executable, DIR_TREE_PY, target_path],
            capture_output=True, text=True, encoding="utf-8"
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    else:
        print(f"[AVISO] dir_tree.py nao encontrado em: {DIR_TREE_PY}")
    print("=" * 60 + "\n")


def load_script_base_patterns(script_path):
    patterns = []
    script_ignore = os.path.join(script_path, ".mergeignore")
    if os.path.isfile(script_ignore):
        with open(script_ignore, "r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if line and not line.startswith("#"):
                    patterns.append(line)
    return patterns


def generate_mergeignore(base_path, script_path, manifest):
    mergeignore_path = os.path.join(base_path, ".mergeignore")
    base_patterns = load_script_base_patterns(script_path)

    if manifest is None:
        with open(mergeignore_path, "w", encoding="utf-8") as f:
            f.write("# .mergeignore gerado automaticamente\n")
            for p in base_patterns:
                f.write(f"{p}\n")
        print(f"[INFO] .mergeignore criado com padroes base (sem dir.md)")
        return

    excluded = set()

    for root, dirs, files in os.walk(base_path):
        rel_root = os.path.relpath(root, base_path).replace("\\", "/")

        for f in files:
            file_path = os.path.join(root, f)
            if file_path == mergeignore_path:
                continue
            if file_path not in manifest:
                rel = os.path.relpath(file_path, base_path).replace("\\", "/")
                excluded.add(rel)

        for d in dirs:
            dir_path = os.path.join(root, d)
            has_manifest = any(
                p.startswith(dir_path + os.sep) for p in manifest
            )
            if not has_manifest:
                rel = os.path.relpath(dir_path, base_path).replace("\\", "/")
                excluded.add(rel + "/")

    with open(mergeignore_path, "w", encoding="utf-8") as f:
        f.write("# .mergeignore gerado automaticamente a partir do dir.md\n")
        f.write("# Padroes base (do script):\n")
        for p in base_patterns:
            f.write(f"{p}\n")
        f.write("\n# Auto-gerado: arquivos/diretorios fora do dir.md:\n")
        for item in sorted(excluded):
            f.write(f"{item}\n")

    print(f"[INFO] .mergeignore gerado: {len(base_patterns)} padroes base + {len(excluded)} exclusoes do dir.md")


def load_ignore_patterns(target_path):
    patterns = []
    target_ignore = os.path.join(target_path, ".mergeignore")
    if os.path.isfile(target_ignore):
        with open(target_ignore, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    patterns.append(line)
        print(f"Usando .mergeignore: {target_ignore}")
    else:
        print("Nenhum .mergeignore encontrado.")
    return patterns


def should_ignore(path, patterns, base_path):
    rel_path = os.path.relpath(path, base_path).replace("\\", "/")
    filename = os.path.basename(path)

    for pattern in patterns:
        pattern = pattern.rstrip("/")

        if fnmatch.fnmatch(rel_path, pattern):
            return True

        if fnmatch.fnmatch(filename, pattern):
            return True

        if pattern in rel_path.split("/"):
            return True

    return False


def merge_files_in_directory(base_path, script_path, output_filename="merged_output.txt"):
    print(f"Iniciando merge em: {base_path}")

    manifest = parse_dir_md(base_path)

    generate_mergeignore(base_path, script_path, manifest)

    ignore_patterns = load_ignore_patterns(base_path)

    output_path = os.path.join(base_path, output_filename)

    try:
        with open(output_path, 'w', encoding='utf-8') as outfile:

            for root, dirs, files in os.walk(base_path):

                dirs[:] = [
                    d for d in dirs
                    if not should_ignore(os.path.join(root, d), ignore_patterns, base_path)
                ]

                for filename in files:
                    file_path = os.path.join(root, filename)

                    if filename == output_filename:
                        continue

                    if should_ignore(file_path, ignore_patterns, base_path):
                        print(f"Ignorado (.mergeignore): {file_path}")
                        continue

                    if manifest is not None and file_path not in manifest:
                        print(f"Ignorado (fora do dir.md): {file_path}")
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
        print(f"Caminho invalido: {base_dir}")
    else:
        show_directory_tree(base_dir)
        merge_files_in_directory(base_dir, script_dir)
