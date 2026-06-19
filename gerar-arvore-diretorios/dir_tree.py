import sys
from pathlib import Path

DIRS_TO_SKIP = {
    ".git", "node_modules", "vendor", "__pycache__", ".pnpm",
    ".next", ".nuxt", ".cache", "dist", "build", ".venv", "venv",
}

def generate_tree(path: Path, prefix: str = "", root: str = "") -> str:
    lines = []

    if root == "":
        root = str(path)
        lines.append(f"# Arvore de Diretorio: `{path.name}`\n")
        lines.append("```")

    try:
        entries = sorted(
            [e for e in path.iterdir()],
            key=lambda x: (not x.is_dir(), x.name.lower()),
        )
    except PermissionError:
        return ""

    for i, entry in enumerate(entries):
        connector = "|-- " if i < len(entries) - 1 else "\\-- "
        lines.append(f"{prefix}{connector}{entry.name}")

        if entry.is_dir():
            extension = "|   " if i < len(entries) - 1 else "    "
            if entry.name in DIRS_TO_SKIP:
                continue
            sub = generate_tree(entry, prefix + extension, root)
            lines.append(sub)

    if root == str(path):
        lines.append("```\n")

    return "\n".join(lines)


def save_to_file(content: str, output_path: str) -> None:
    filepath = Path(output_path).resolve()
    filepath.write_text(content, encoding="utf-8")
    print(f"[OK] Arvore salva em: {filepath}")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    args = sys.argv[1:]

    target = Path(args[0]).resolve() if args else Path.cwd()
    output = args[1] if len(args) > 1 else None

    if not target.exists():
        print(f"[ERRO] Diretorio nao encontrado: {target}")
        sys.exit(1)
    if not target.is_dir():
        print(f"[ERRO] Caminho nao e um diretorio: {target}")
        sys.exit(1)

    tree = generate_tree(target)
    print(tree)

    dir_md = target / "dir.md"
    save_to_file(tree, str(dir_md))


if __name__ == "__main__":
    main()
