#!/usr/bin/env python3
"""
add_header_action.py

Automatiza a adição rápida de botões de Ajuda no cabeçalho (addHeaderAction)
e o método onHelp correspondente em controllers Adianti (plataforma_dev / bbshop).

Uso individual:
    python3 add_header_action.py --class SellerStockList --help-id 176

Uso em lote (texto ou arquivo):
    python3 add_header_action.py --batch "165\tCadastros\tGarantia Financeira\tSellerFinancialGuaranteeView\t1\n168\tListagem\tSaldo Estoque\tSellerStockList\t1"
    python3 add_header_action.py --batch-file lista_helps.txt
"""

import sys
import os
import re
import argparse
import subprocess
from pathlib import Path

WORKSPACE_ROOT = Path(os.environ.get("ADIANTI_ROOT", "/opt/ambiente/projetos/plataforma_dev"))
APP_CONTROL = WORKSPACE_ROOT / "app" / "control"

HELP_ACTION_CODE = """
        $Help = $this->form->addHeaderAction("Ajuda", new TAction([$this, 'onHelp']), 'fas:question #00BCD4');
        $this->Help = $Help;"""

def create_onhelp_method(help_id, class_name, routine_id=None):
    routine_val = f"{routine_id}" if routine_id is not None else "null"
    return f"""
    public function onHelp($param = null) 
    {{
        try 
        {{
            //code here
            $param = [];
            $param['help_id'] = {help_id};
            $param['routine_id'] = {routine_val};
            $param['form_name'] = '{class_name}';

            AdiantiCoreApplication::loadPage('FormHelp', 'onShow', $param);

        }}
        catch (Exception $e) 
        {{
            new TMessage('error', $e->getMessage());    
        }}
    }}
"""

def find_controller_file(class_name):
    # Procura em app/control
    for p in APP_CONTROL.rglob(f"{class_name}.php"):
        if p.is_file():
            return p
    # Procura em app/ inteiro se nao achar em control
    for p in (WORKSPACE_ROOT / "app").rglob(f"{class_name}.php"):
        if p.is_file():
            return p
    return None

def process_controller(class_name, help_id, routine_id=None, force=False):
    target_file = find_controller_file(class_name)
    if not target_file:
        print(f"[ERRO] Arquivo para a classe '{class_name}' não foi encontrado em app/.")
        return False

    with open(target_file, "r", encoding="utf-8", errors="ignore", newline="") as f:
        content = f.read()
    original_content = content

    # Normaliza CRLF para LF
    content = content.replace("\r\n", "\n")

    modified = False

    # 1. Verifica se onHelp já existe
    # Ajuda já existente (onHelp ou outro método que abre FormHelp)
    has_onhelp = "function onHelp" in content or re.search(r"loadPage\(\s*['\"]FormHelp['\"]", content) is not None
    if has_onhelp and not force:
        print(f"[INFO] {class_name}: método onHelp já existe.")
    elif has_onhelp and force:
        # Atualiza o help_id existente no onHelp
        content = re.sub(
            r"(\$param\['help_id'\]\s*=\s*)\d+;",
            rf"\g<1>{help_id};",
            content
        )
        modified = True
        print(f"[UPDATE] {class_name}: help_id atualizado para {help_id} no onHelp existente.")
    else:
        # Adiciona o método onHelp antes do último '}' da classe
        last_brace_idx = content.rfind("}")
        if last_brace_idx != -1:
            onhelp_code = create_onhelp_method(help_id, class_name, routine_id)
            content = content[:last_brace_idx] + onhelp_code + "\n}\n"
            modified = True
            print(f"[ADD] {class_name}: método onHelp adicionado com help_id={help_id}.")
        else:
            print(f"[ERRO] {class_name}: não foi possível localizar o fechamento da classe.")
            return False

    # 2. Verifica se addHeaderAction('Ajuda'...) já existe no construtor
    has_header_action = re.search(r"addHeaderAction\(\s*['\"]Ajuda['\"]|addHeaderAction\([^;]*onHelp", content) is not None
    if has_header_action:
        print(f"[INFO] {class_name}: addHeaderAction('Ajuda') já existe no construtor.")
    else:
        # Tenta injetar após o último addAction ou antes do container
        # Padrões comuns:
        # 1. Após último $this->form->addAction(...)
        # 2. Antes de $container = new TVBox; ou parent::add($container);
        # 3. Após parent::__construct($param); em BasePages
        
        injected = False
        
        # Padrão 1: após addAction
        matches = list(re.finditer(r"\$this->form->addAction\([^\)]+\)(?:->addStyleClass\([^\)]+\))?;", content))
        if matches:
            last_match = matches[-1]
            end_pos = last_match.end()
            content = content[:end_pos] + "\n" + HELP_ACTION_CODE + content[end_pos:]
            injected = True
        
        # Padrão 2: antes de $container = new TVBox ou $container->add
        if not injected:
            m = re.search(r"(\s+)(\$container\s*=\s*new\s+TVBox;)", content)
            if m:
                indent = m.group(1)
                content = content[:m.start()] + "\n" + HELP_ACTION_CODE + "\n" + content[m.start():]
                injected = True
                
        # Padrão 3: antes de parent::add($container)
        if not injected:
            m = re.search(r"(\s+)(parent::add\(\$container\);)", content)
            if m:
                content = content[:m.start()] + "\n" + HELP_ACTION_CODE + "\n" + content[m.start():]
                injected = True

        # Padrão 4: logo após parent::__construct($param);
        if not injected:
            m = re.search(r"parent::__construct\([^)]*\);", content)
            if m:
                end_pos = m.end()
                content = content[:end_pos] + "\n" + HELP_ACTION_CODE + content[end_pos:]
                injected = True

        if injected:
            modified = True
            print(f"[ADD] {class_name}: addHeaderAction('Ajuda') injetado no construtor.")
        else:
            print(f"[AVISO] {class_name}: não foi possível injetar addHeaderAction automaticamente no construtor. Verifique manualmente.")

    if modified:
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(content)

        # Validação de sintaxe PHP
        res = subprocess.run(["php", "-l", str(target_file)], capture_output=True, text=True)
        if res.returncode == 0:
            print(f"[OK] {class_name}: sintaxe PHP válida.")
            return True
        else:
            print(f"[ERRO-PHP] {class_name}: erro de sintaxe detectado:\n{res.stderr or res.stdout}")
            with open(target_file, "w", encoding="utf-8", newline="") as f:
                f.write(original_content)
            print(f"[RESTAURADO] {class_name}: arquivo original restaurado.")
            return False
    else:
        print(f"[OK] {class_name}: nenhuma alteração necessária.")
        return True

def parse_batch_text(text):
    """
    Interpreta linhas de help coladas do datagrid ou formatadas:
    Exemplo:
    165	Cadastros	Garantia Financeira	SellerFinancialGuaranteeView	1
    170	Listagem	Importar csv	Tentativa de acesso...	1
    """
    entries = []
    for line in text.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        parts = re.split(r"[\t|]+|\s{2,}", line)
        parts = [p.strip() for p in parts if p.strip()]
        if not parts:
            continue
        
        # Formato: ID ... Controller ...
        # Se primeira coluna for número (help_id)
        if parts[0].isdigit():
            help_id = int(parts[0])
            # Procura qual elemento parece com nome de classe PHP (CamelCase terminando em Form, List, View, etc.)
            controller = None
            for p in parts[1:]:
                if re.match(r"^[A-Z][A-Za-z0-9_]+(Form|List|View|Page|Manager|Dashboard|Window)$", p):
                    controller = p
                    break
                elif re.match(r"^[A-Z][A-Za-z0-9_]+$", p) and len(p) > 3 and not p.isdigit() and p not in ["Cadastros", "Listagem", "Editar", "Status", "Ativo", "Inativo"]:
                    controller = p
            
            # Caso especial: Importar csv com erro de propriedade ou nome mapeado
            if not controller and "Importar" in line:
                controller = "SellerStockImportForm"
                
            if controller:
                entries.append((controller, help_id))
            else:
                print(f"[IGNORADO] Não foi possível identificar o Controller na linha: {line}")
        elif len(parts) >= 2 and parts[1].isdigit():
            controller = parts[0]
            help_id = int(parts[1])
            entries.append((controller, help_id))

    return entries

def main():
    parser = argparse.ArgumentParser(description="Adiciona botão de Ajuda (addHeaderAction) e método onHelp em controllers Adianti.")
    parser.add_argument("--class", dest="class_name", help="Nome da classe do controller (ex: SellerStockList)")
    parser.add_argument("--help-id", dest="help_id", type=int, help="ID do help no HelpCenter")
    parser.add_argument("--routine-id", dest="routine_id", type=int, default=None, help="ID da rotina (opcional)")
    parser.add_argument("--batch", dest="batch_text", help="Texto contendo várias linhas de help")
    parser.add_argument("--batch-file", dest="batch_file", help="Caminho do arquivo contendo lote de helps")
    parser.add_argument("--force", action="store_true", help="Sobrescrever help_id existente")
    parser.add_argument("--root", dest="root", default=None, help="Raiz do projeto Adianti (padrão: $ADIANTI_ROOT ou plataforma_dev)")

    args = parser.parse_args()

    if args.root:
        global WORKSPACE_ROOT, APP_CONTROL
        WORKSPACE_ROOT = Path(args.root).resolve()
        APP_CONTROL = WORKSPACE_ROOT / "app" / "control"

    if args.class_name and args.help_id:
        success = process_controller(args.class_name, args.help_id, args.routine_id, args.force)
        sys.exit(0 if success else 1)

    batch_input = ""
    if args.batch_file:
        with open(args.batch_file, "r", encoding="utf-8") as f:
            batch_input = f.read()
    elif args.batch_text:
        batch_input = args.batch_text.replace("\\n", "\n").replace("\\t", "\t")

    if batch_input:
        entries = parse_batch_text(batch_input)
        if not entries:
            print("[ERRO] Nenhuma entrada válida encontrada no lote.")
            sys.exit(1)
        
        print(f"[INFO] Processando {len(entries)} entrada(s) em lote...")
        success_count = 0
        for class_name, help_id in entries:
            print(f"--- Processando: {class_name} (help_id: {help_id}) ---")
            if process_controller(class_name, help_id, None, args.force):
                success_count += 1
        
        print(f"\n[CONCLUÍDO] {success_count}/{len(entries)} controllers atualizados com sucesso.")
        sys.exit(0 if success_count == len(entries) else 1)

    parser.print_help()
    sys.exit(1)

if __name__ == "__main__":
    main()

