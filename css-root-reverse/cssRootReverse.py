import re
import os

def reverter_css_com_variaveis_por_tipo():
    caminho_arquivo_css_refatorado = input("Digite o caminho completo do arquivo CSS refatorado (ex: nome_refatorado_tipado.css): ")

    try:
        with open(caminho_arquivo_css_refatorado, 'r', encoding='utf-8') as f:
            conteudo_refatorado_css = f.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo_css_refatorado}' não foi encontrado.")
        return
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return

    # --- Passo 1: Extrair variáveis do bloco :root ---
    css_variables = {}
    
    # Regex para encontrar o bloco :root e seu conteúdo
    root_block_match = re.search(r':root\s*\{([^}]*)\}', conteudo_refatorado_css, re.DOTALL)

    if not root_block_match:
        print("Erro: Nenhum bloco ':root' com variáveis CSS encontrado no arquivo.")
        return

    root_content = root_block_match.group(1)
    
    # Regex para encontrar declarações de variáveis dentro do bloco :root
    # Ex: --font-size-var-01: 16px; /* Comentário */
    variable_declaration_regex = re.compile(r'(--[a-zA-Z0-9_-]+?)\s*:\s*([^;]+?);', re.IGNORECASE)

    for match in variable_declaration_regex.finditer(root_content):
        var_name = match.group(1).strip()
        var_value = match.group(2).strip()
        css_variables[var_name] = var_value
        print(f"Variável encontrada: {var_name} -> {var_value}")

    if not css_variables:
        print("Nenhuma variável CSS encontrada dentro do bloco ':root'.")
        return

    # --- Passo 2: Remover o bloco :root do conteúdo para processamento ---
    # Remove todo o bloco :root, incluindo o :root { e }
    conteudo_sem_root = re.sub(r':root\s*\{[^}]*\}', '', conteudo_refatorado_css, flags=re.DOTALL)
    
    # Remove linhas em branco extras que podem ter sido criadas pela remoção do :root
    conteudo_sem_root = re.sub(r'\n\s*\n', '\n', conteudo_sem_root).strip()

    # --- Passo 3: Substituir as ocorrências de var() pelos valores diretos ---
    
    conteudo_revertido_css = conteudo_sem_root
    
    # Itera sobre as variáveis encontradas e realiza a substituição
    for var_name, var_value in css_variables.items():
        # Regex para encontrar 'var(--nome-da-variavel)'
        # Assegura que estamos substituindo apenas a chamada da função var()
        var_call_regex = re.compile(r'var\(\s*' + re.escape(var_name) + r'\s*\)', re.IGNORECASE)
        conteudo_revertido_css = var_call_regex.sub(var_value, conteudo_revertido_css)
        print(f"Substituindo todas as ocorrências de var({var_name}) por {var_value}")

    # --- Passo 4: Gerar o novo arquivo CSS revertido ---
    
    # Define o nome do novo arquivo
    base, ext = os.path.splitext(caminho_arquivo_css_refatorado)
    # Garante que o nome base termine com o original antes do "_refatorado_tipado"
    if base.endswith("_refatorado_tipado"):
        base = base[:-len("_refatorado_tipado")]
    
    novo_caminho_arquivo_css_revertido = f"{base}_revertido{ext}"

    try:
        with open(novo_caminho_arquivo_css_revertido, 'w', encoding='utf-8') as f:
            f.write(conteudo_revertido_css)
        print(f"\nArquivo revertido salvo como: '{novo_caminho_arquivo_css_revertido}'")
        print("REVISTA CUIDADOSAMENTE este arquivo para garantir que todas as substituições estão corretas.")

    except Exception as e:
        print(f"Erro ao salvar o arquivo revertido: {e}")

if __name__ == "__main__":
    reverter_css_com_variaveis_por_tipo()
