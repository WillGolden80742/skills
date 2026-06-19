#!/usr/bin/env python3
import os
import sys
import json
import shutil
import argparse
import re

def remove_path(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
        print(f"Removido diretorio: {path}")
    elif os.path.isfile(path):
        os.remove(path)
        print(f"Removido arquivo: {path}")
    else:
        print(f"Aviso: caminho nao encontrado: {path}")

def update_composer_json(project_path, deps_to_remove=None):
    composer_path = os.path.join(project_path, "composer.json")
    if not os.path.exists(composer_path):
        print("composer.json nao encontrado")
        return
    
    with open(composer_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    data = json.loads(content)
    modified = False
    
    if deps_to_remove:
        deps_list = [d.strip() for d in deps_to_remove.split(",")]
        
        if "require" in data:
            for dep in deps_list:
                if dep in data["require"]:
                    del data["require"][dep]
                    print(f"Removida dependencia require: {dep}")
                    modified = True
        
        if "require-dev" in data:
            for dep in deps_list:
                if dep in data["require-dev"]:
                    del data["require-dev"][dep]
                    print(f"Removida dependencia require-dev: {dep}")
                    modified = True
    else:
        keys_to_remove = []
        if "require" in data:
            keys_to_remove = [k for k in data["require"].keys() if k != "php"]
            for k in keys_to_remove:
                del data["require"][k]
                print(f"Removida dependencia require: {k}")
                modified = True
        
        if "require-dev" in data:
            keys_to_remove = list(data["require-dev"].keys())
            for k in keys_to_remove:
                del data["require-dev"][k]
                print(f"Removida dependencia require-dev: {k}")
                modified = True
    
    if modified:
        if "scripts" in data:
            scripts_to_remove = []
            for script, cmd in data.get("scripts", {}).items():
                if "vendor" in cmd:
                    scripts_to_remove.append(script)
            for script in scripts_to_remove:
                del data["scripts"][script]
                print(f"Removido script: {script}")
        
        with open(composer_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            f.write("\n")
        print("composer.json atualizado")

def update_package_json(project_path, deps_to_remove=None):
    package_path = os.path.join(project_path, "package.json")
    if not os.path.exists(package_path):
        print("package.json nao encontrado")
        return
    
    with open(package_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    data = json.loads(content)
    modified = False
    
    if deps_to_remove:
        deps_list = [d.strip() for d in deps_to_remove.split(",")]
        
        if "dependencies" in data:
            for dep in deps_list:
                if dep in data["dependencies"]:
                    del data["dependencies"][dep]
                    print(f"Removida dependencia dependencies: {dep}")
                    modified = True
        
        if "devDependencies" in data:
            for dep in deps_list:
                if dep in data["devDependencies"]:
                    del data["devDependencies"][dep]
                    print(f"Removida dependencia devDependencies: {dep}")
                    modified = True
    else:
        if "dependencies" in data:
            keys = list(data["dependencies"].keys())
            for k in keys:
                del data["dependencies"][k]
                print(f"Removida dependencia dependencies: {k}")
                modified = True
        
        if "devDependencies" in data:
            keys = list(data["devDependencies"].keys())
            for k in keys:
                del data["devDependencies"][k]
                print(f"Removida dependencia devDependencies: {k}")
                modified = True
    
    if modified:
        with open(package_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            f.write("\n")
        print("package.json atualizado")

def main():
    parser = argparse.ArgumentParser(description="Remove arquivos e dependencias")
    parser.add_argument("--path", help="Caminho do arquivo/diretorio a remover")
    parser.add_argument("--project", help="Caminho base do projeto")
    parser.add_argument("--remove-composer", action="store_true", help="Remove todas dependencias do Composer")
    parser.add_argument("--remove-composer-deps", help="Remove dependencias especificas do Composer (separadas por virgula)")
    parser.add_argument("--remove-npm", action="store_true", help="Remove todas dependencias do npm")
    parser.add_argument("--remove-npm-deps", help="Remove dependencias especificas do npm (separadas por virgula)")
    
    args = parser.parse_args()
    
    if args.project:
        os.chdir(args.project)
    
    if args.path:
        remove_path(args.path)
    
    project_path = args.project or os.getcwd()
    
    if args.remove_composer:
        update_composer_json(project_path)
    elif args.remove_composer_deps:
        update_composer_json(project_path, args.remove_composer_deps)
    
    if args.remove_npm:
        update_package_json(project_path)
    elif args.remove_npm_deps:
        update_package_json(project_path, args.remove_npm_deps)

if __name__ == "__main__":
    main()
