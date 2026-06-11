import sys
import os
import glob
import shutil

def rename_file(original_name, new_name, project_path, update_all):
    original_base = os.path.splitext(original_name)[0]
    new_base = os.path.splitext(new_name)[0]
    
    original_path = None
    for root, dirs, files in os.walk(project_path):
        if original_name in files:
            original_path = os.path.join(root, original_name)
            break

    if not original_path:
        print(f"Arquivo '{original_name}' não encontrado em '{project_path}'")
        return False

    new_path = os.path.join(os.path.dirname(original_path), new_name)
    shutil.move(original_path, new_path)
    print(f"Arquivo renomeado: {original_path} -> {new_path}")

    with open(new_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    replaced_inside = False
    new_content = content
    
    if original_base in content:
        new_content = new_content.replace(original_base, new_base)
        replaced_inside = True
    
    if original_name in content:
        new_content = new_content.replace(original_name, new_name)
        replaced_inside = True
    
    if replaced_inside:
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Classe atualizada dentro do arquivo: {new_path}")

    refs_updated = 0
    extensions = ['*.php', '*.js', '*.css', '*.html', '*.json', '*.xml', '*.md', '*.txt'] if update_all == 'true' else ['*.php']

    for ext in extensions:
        for filepath in glob.glob(os.path.join(project_path, '**', ext), recursive=True):
            if filepath == new_path:
                continue
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                replaced = False
                new_content = content
                
                if original_base in content:
                    new_content = new_content.replace(original_base, new_base)
                    replaced = True
                
                if original_name in content:
                    new_content = new_content.replace(original_name, new_name)
                    replaced = True
                
                if replaced:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    refs_updated += 1
                    print(f"Atualizado em: {filepath}")
            except Exception as e:
                print(f"Erro ao processar {filepath}: {e}")

    print(f"Total de arquivos atualizados: {refs_updated}")
    return True

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Uso: rename.py \"nome_original\" \"nome_novo\" \"caminho_projeto\" \"true/false\"")
        sys.exit(1)

    original_name = sys.argv[1]
    new_name = sys.argv[2]
    project_path = sys.argv[3]
    update_all = sys.argv[4]

    rename_file(original_name, new_name, project_path, update_all)
