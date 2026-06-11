import re
import os
from collections import Counter, defaultdict
import hashlib

def refatorar_css_com_variaveis_genericas():
    caminho_arquivo_css = input("Digite o caminho completo do arquivo CSS original: ")

    try:
        with open(caminho_arquivo_css, 'r', encoding='utf-8') as f:
            conteudo_original_css = f.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo_css}' não foi encontrado.")
        return
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return

    # --- Passo 1: Análise para identificar todos os valores repetidos, independentemente da propriedade ---

    # Remove comentários CSS e normaliza espaços para a fase de análise
    conteudo_analise = re.sub(r'/\*.*?\*/', '', conteudo_original_css, flags=re.DOTALL)
    conteudo_analise = re.sub(r'\s+', ' ', conteudo_analise)

    # Regex genérico para capturar PROPRIEDADE e VALOR
    # Grupo 1: Captura o nome da propriedade (ex: 'font-family', 'margin-left')
    # Grupo 2: Captura o valor da propriedade (ex: 'Arial, sans-serif', '10px')
    property_value_regex = re.compile(r'([a-zA-Z-]+?)\s*:\s*([^;{}]+?)(?:;|(?=\}))', re.IGNORECASE)

    # Counter para armazenar a contagem de TODOS os valores, independentemente da propriedade
    # Ex: Counter({'Arial, sans-serif': 5, '10px': 8, 'red': 10, '#333': 12})
    all_values_counts = Counter()

    # Encontra todas as propriedades e seus valores para contagem
    for match in property_value_regex.finditer(conteudo_analise):
        value = match.group(2).strip()

        # Ignora valores que raramente seriam variáveis ou são muito genéricos,
        # ou que são considerados 'default' para muitas propriedades
        if value and value.lower() not in ['initial', 'inherit', 'auto', 'none', 'unset', '0', '0px', '0em', '0%', 'transparent']:
            all_values_counts[value] += 1

    # Dicionário para armazenar apenas os valores que se repetem > 2 vezes
    # Ex: { 'Arial, sans-serif': 5, '10px': 8, 'red': 10 }
    repeated_values = {v: c for v, c in all_values_counts.items() if c > 2}

    if not repeated_values:
        print("Nenhum valor repetido mais de 2 vezes encontrado. Nenhum arquivo foi gerado.")
        return

    print("\n--- Valores Repetidos (mais de 2 vezes) em todo o CSS ---")
    # Ordena e imprime para melhor leitura
    sorted_repeated_values = sorted(repeated_values.items(), key=lambda item: item[1], reverse=True)
    for value, count in sorted_repeated_values:
        print(f"  Valor: '{value}' - Repetições: {count}")

    # --- Passo 2: Gerar as variáveis CSS e o mapeamento valor -> nome_da_variavel ---

    css_variables_output = []
    css_variables_output.append(":root {")

    # Dicionário para mapear valor_original -> nome_da_variavel
    # Ex: {'Arial, sans-serif': '--value-font-arial', '10px': '--value-spacing-small'}
    value_to_var_name = {}

    # Função para sanitizar o valor e tentar criar um nome de variável descritivo
    def sanitize_value_for_var_name(value):
        # Remove caracteres problemáticos e substitui espaços por hífens
        sanitized = re.sub(r'[^a-zA-Z0-9-]', '', value.lower().replace(' ', '-').replace('/', '-')).strip('-')
        if not sanitized: # Se o valor ficar vazio após a sanitização, usa um hash
            sanitized = hashlib.sha1(value.encode('utf-8')).hexdigest()[:8]
        return sanitized

    # Contador global para garantir unicidade em nomes de variáveis se a sanitização for igual
    var_name_suffix_counter = defaultdict(int)

    for value, count in sorted_repeated_values:
        base_var_name = sanitize_value_for_var_name(value)
        
        # Prefixo genérico para a variável
        var_prefix = "--value-"
        
        # Evita nomes de variáveis muito longos ou genéricos demais que podem ser idênticos
        # Ex: 'red' -> --value-red, 'blue' -> --value-blue
        # Mas '10px' e '10px solid' seriam diferentes
        
        # Verifica se já existe um nome de variável mapeado para este valor
        # (Isso é crucial para a reutilização)
        if value not in value_to_var_name:
            final_var_name = f"{var_prefix}{base_var_name}"
            
            # Se já existir uma variável com este nome (por colisão na sanitização ou hash), adiciona um contador
            while final_var_name in value_to_var_name.values():
                var_name_suffix_counter[base_var_name] += 1
                final_var_name = f"{var_prefix}{base_var_name}-{var_name_suffix_counter[base_var_name]:02d}"
                
            value_to_var_name[value] = final_var_name
            css_variables_output.append(f"  {final_var_name}: {value}; /* Repetições: {count} */")

    css_variables_output.append("}")

    # --- Passo 3: Substituir as ocorrências originais no CSS ---
    
    new_content_lines = []
    
    # Itera linha por linha para preservar a formatação original tanto quanto possível
    for line_num, line in enumerate(conteudo_original_css.splitlines()):
        modified_line = line
        
        # Este regex encontra a declaração completa 'propriedade: valor;'
        # Grupo 1: Captura o nome da propriedade (ex: 'font-size')
        # Grupo 2: Captura o ':' e os espaços seguintes
        # Grupo 3: Captura o valor da declaração (pode incluir funções como calc(), url())
        # Grupo 4: Captura o terminador (';', '}' ou fim da linha)
        declaration_pattern = re.compile(r'([a-zA-Z-]+?)(\s*:\s*)([^;{}]+?)(;|$|})')
        
        # Usamos uma função de substituição para `re.sub` para ter controle
        def replace_value_in_declaration(match):
            prop_name_in_line = match.group(1).strip().lower() # Nome da propriedade
            separator_and_space = match.group(2) # ': '
            current_value_in_declaration = match.group(3).strip() # O valor atual
            terminator = match.group(4) # ';' ou '}'

            # Verifica se o valor está no nosso mapa de variáveis
            if current_value_in_declaration in value_to_var_name:
                var_name = value_to_var_name[current_value_in_declaration]
                return f"{prop_name_in_line}{separator_and_space}var({var_name}){terminator}"
            else:
                return match.group(0) # Retorna a declaração original se o valor não for mapeado

        modified_line = declaration_pattern.sub(replace_value_in_declaration, modified_line)
        new_content_lines.append(modified_line)
        
    # Juntar as linhas novamente
    conteudo_modificado_css = "\n".join(new_content_lines)

    # --- Passo 4: Gerar o novo arquivo CSS ---
    
    # Adiciona as variáveis no topo do arquivo modificado
    final_css_content = "\n".join(css_variables_output) + "\n\n" + conteudo_modificado_css

    # Define o nome do novo arquivo
    base, ext = os.path.splitext(caminho_arquivo_css)
    novo_caminho_arquivo_css = f"{base}_refatorado_generico{ext}"

    try:
        with open(novo_caminho_arquivo_css, 'w', encoding='utf-8') as f:
            f.write(final_css_content)
        print(f"\nArquivo refatorado salvo como: '{novo_caminho_arquivo_css}'")
        print("REVISTA CUIDADOSAMENTE este arquivo para garantir que todas as substituições estão corretas.")
        print("Substituições dentro de funções (ex: calc(), url()) ou valores múltiplos (ex: padding: 10px 20px) foram tratadas, mas a complexidade do CSS pode levar a casos não esperados.")

    except Exception as e:
        print(f"Erro ao salvar o arquivo refatorado: {e}")

if __name__ == "__main__":
    refatorar_css_com_variaveis_genericas()
