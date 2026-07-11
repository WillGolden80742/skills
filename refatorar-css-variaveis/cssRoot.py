import os
import re
import hashlib

def clean_line_from_comment(line):
    cleaned = re.sub(r'/\*.*?\*/', '', line)
    return cleaned

def is_declaration(line):
    cleaned = clean_line_from_comment(line)
    stripped = cleaned.strip()
    if ':' not in stripped:
        return None
    parts = stripped.split(':', 1)
    prop = parts[0].strip()
    val_part = parts[1].strip()
    
    if not re.match(r'^[a-zA-Z0-9-_]+$', prop):
        return None
    if prop.startswith('--'):
        return None
    if not val_part.endswith(';'):
        return None
    if ';' in val_part[:-1]:
        return None
        
    val = val_part[:-1].strip()
    if 'var(' in val:
        return None
        
    return prop, val

def normalize_value(val):
    val = val.strip().lower()
    val = re.sub(r'\s*,\s*', ', ', val)
    val = val.replace('"', "'")
    return val

def get_var_name(value, existing_mapping, used_var_names):
    norm_val = normalize_value(value)
    if norm_val in existing_mapping:
        return existing_mapping[norm_val]
        
    clean = norm_val
    if 'url(' in clean:
        clean = "url-asset"
    clean = re.sub(r'[^a-zA-Z0-9-_]', '-', clean)
    clean = re.sub(r'[-_]+', '-', clean).strip('-')
    
    prefix = "v-"
    if not clean:
        clean = "val-" + hashlib.md5(norm_val.encode('utf-8')).hexdigest()[:6]
    elif clean[0].isdigit():
        clean = "val-" + clean
        
    var_name = f"--{prefix}{clean}"
    
    if len(var_name) > 45:
        h = hashlib.md5(norm_val.encode('utf-8')).hexdigest()[:6]
        var_name = f"--v-{clean[:30]}-{h}"
        
    base_name = var_name
    counter = 1
    while var_name in used_var_names:
        var_name = f"{base_name}-{counter}"
        counter += 1
        
    return var_name

def parse_existing_base_css_variables(base_css_path):
    existing_mapping = {}
    used_var_names = set()
    
    if not os.path.exists(base_css_path):
        return existing_mapping, used_var_names
        
    with open(base_css_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    match = re.search(r':root\s*\{([^}]+)\}', content, re.DOTALL)
    if match:
        root_content = match.group(1)
        var_pattern = re.compile(r'(--[a-zA-Z0-9-_]+)\s*:\s*([^;]+?);')
        for m in var_pattern.finditer(root_content):
            var_name = m.group(1).strip()
            val = m.group(2).strip()
            norm_val = normalize_value(val)
            existing_mapping[norm_val] = var_name
            used_var_names.add(var_name)
            
    return existing_mapping, used_var_names

def find_var_fallbacks(line):
    results = []
    idx = 0
    while True:
        idx = line.find("var(", idx)
        if idx == -1:
            break
            
        start_idx = idx
        brace_count = 0
        comma_idx = -1
        
        for i in range(idx + 4, len(line)):
            char = line[i]
            if char == '(':
                brace_count += 1
            elif char == ')':
                if brace_count == 0:
                    end_idx = i + 1
                    if comma_idx != -1:
                        var_name = line[idx+4:comma_idx].strip()
                        fallback = line[comma_idx+1:i].strip()
                        if var_name.startswith('--'):
                            results.append({
                                "start": start_idx,
                                "end": end_idx,
                                "var_name": var_name,
                                "fallback": fallback
                            })
                    break
                else:
                    brace_count -= 1
            elif char == ',':
                if brace_count == 0:
                    comma_idx = i
                    
        idx += 4
        
    return results

def replace_var_fallbacks(line, existing_mapping, used_var_names, new_variables):
    fallbacks = find_var_fallbacks(line)
    if not fallbacks:
        return line
        
    modified_line = line
    for f in reversed(fallbacks):
        var_name = f["var_name"]
        fallback = f["fallback"]
        start = f["start"]
        end = f["end"]
        
        if 'var(' in fallback:
            continue
            
        if not fallback:
            continue
            
        norm_fallback = normalize_value(fallback)
        fallback_var = get_var_name(fallback, existing_mapping, used_var_names)
        
        if norm_fallback not in existing_mapping:
            existing_mapping[norm_fallback] = fallback_var
            used_var_names.add(fallback_var)
            new_variables[fallback_var] = fallback
            
        replacement = f"var({var_name}, var({fallback_var}))"
        modified_line = modified_line[:start] + replacement + modified_line[end:]
        
    return modified_line

def process_css_file(file_path, existing_mapping, used_var_names, new_variables):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.splitlines()
    new_lines = []
    changes_count = 0
    
    for line in lines:
        stripped = line.strip()
        if len(stripped) < 4:
            new_lines.append(line)
            continue
            
        if stripped.startswith('/*') or stripped.startswith('@') or stripped == '{' or stripped == '}':
            new_lines.append(line)
            continue
            
        # STEP 1: Process var() fallbacks first using balanced parenthesis parser
        modified_line = replace_var_fallbacks(line, existing_mapping, used_var_names, new_variables)
        if modified_line != line:
            changes_count += 1
            line = modified_line
            
        # STEP 2: Process standard declarations
        decl = is_declaration(line)
        if decl:
            prop, val = decl
            norm_val = normalize_value(val)
            
            if not norm_val:
                new_lines.append(line)
                continue
                
            var_name = get_var_name(val, existing_mapping, used_var_names)
            
            if norm_val not in existing_mapping:
                existing_mapping[norm_val] = var_name
                used_var_names.add(var_name)
                new_variables[var_name] = val
                
            semicolon_idx = line.rfind(';')
            indent = line[:len(line) - len(line.lstrip())]
            
            comment_part = ""
            if semicolon_idx != -1 and semicolon_idx < len(line) - 1:
                comment_part = line[semicolon_idx+1:]
                
            new_line = f"{indent}{prop}: var({var_name});{comment_part}"
            new_lines.append(new_line)
            changes_count += 1
        else:
            new_lines.append(line)
            
    if changes_count > 0:
        updated_content = '\n'.join(new_lines)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
            
    return changes_count

def update_base_css(base_css_path, new_variables):
    if not new_variables:
        print("Nenhuma nova variável para adicionar ao arquivo centralizador.")
        return
        
    if os.path.exists(base_css_path):
        with open(base_css_path, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = ""
        
    match = re.search(r':root\s*\{', content)
    if not match:
        root_block = ":root {\n"
        for var_name, val in sorted(new_variables.items()):
            root_block += f"    {var_name}: {val};\n"
        root_block += "}\n\n"
        content = root_block + content
    else:
        start_idx = match.end()
        brace_count = 1
        closing_idx = -1
        for i in range(start_idx, len(content)):
            if content[i] == '{':
                brace_count += 1
            elif content[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    closing_idx = i
                    break
                    
        if closing_idx != -1:
            new_vars_str = "\n    /* Consolidated custom properties - including fallbacks and layout definitions */\n"
            for var_name, val in sorted(new_variables.items()):
                new_vars_str += f"    {var_name}: {val};\n"
            
            content = content[:closing_idx] + new_vars_str + content[closing_idx:]
        else:
            print("Erro: Não foi possível encontrar a chave de fechamento de :root no arquivo centralizador.")
            return
            
    with open(base_css_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    print("--- CSS Custom Properties Refactoring Tool ---")
    css_dir = input("Digite o caminho do diretório CSS (Enter para o atual): ").strip()
    if not css_dir:
        css_dir = os.getcwd()
        
    base_css_name = input("Digite o nome do arquivo centralizador (padrão: base.css): ").strip()
    if not base_css_name:
        base_css_name = "base.css"
        
    base_css_path = os.path.join(css_dir, base_css_name)
    
    excludes_input = input(f"Digite os arquivos a excluir separados por vírgula (padrão: {base_css_name}, style.css): ").strip()
    if excludes_input:
        excluded_files = [x.strip() for x in excludes_input.split(',')]
    else:
        excluded_files = [base_css_name, "style.css"]
        
    print("\nAnalisando variáveis existentes...")
    existing_mapping, used_var_names = parse_existing_base_css_variables(base_css_path)
    print(f"Carregadas {len(existing_mapping)} variáveis existentes de {base_css_name}.")
    
    new_variables = {}
    
    css_files = [f for f in os.listdir(css_dir) if f.endswith('.css') and f not in excluded_files]
    
    total_changes = 0
    for css_file in css_files:
        file_path = os.path.join(css_dir, css_file)
        print(f"Processando {css_file}...")
        changes = process_css_file(file_path, existing_mapping, used_var_names, new_variables)
        total_changes += changes
        print(f"  Efetuadas {changes} substituições em {css_file}.")
        
    print(f"\nGeradas {len(new_variables)} novas variáveis customizadas (incluindo layouts e fallbacks).")
    print(f"Atualizando {base_css_name} com as novas variáveis...")
    update_base_css(base_css_path, new_variables)
    print(f"{base_css_name} atualizado com sucesso!")
    print(f"Total de linhas CSS modernizadas: {total_changes}")

if __name__ == "__main__":
    main()
