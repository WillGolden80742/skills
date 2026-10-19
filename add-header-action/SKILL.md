---
name: add-header-action
description: Adiciona o botão de Ajuda no cabeçalho ($this->form->addHeaderAction) e o método onHelp em controllers Adianti (plataforma_dev / bbshop), vinculando o help_id do HelpCenter (FormHelp). Aceita linhas coladas do HelpList em lote. Use quando o usuário mencionar: addHeaderAction, add header action, adicionar ajuda, adicionar onhelp, botao ajuda, botão de ajuda, helpcenter tela, help_id, adicionar help, add help, header action, onHelp, ajuda tela, FormHelp.
---

# add-header-action — Botão de Ajuda + onHelp (Adianti / HelpCenter)

Injeta em controllers Adianti:
1. No construtor: `$this->form->addHeaderAction("Ajuda", new TAction([$this, 'onHelp']), 'fas:question #00BCD4');`
2. Na classe: o método `onHelp` que abre `FormHelp::onShow` com `help_id` e `form_name`.

Script: `~/.claude/skills/add-header-action/scripts/add_header_action.py`
(raiz padrão `/opt/ambiente/projetos/plataforma_dev`; troque com `--root <dir>` ou `ADIANTI_ROOT=<dir>`).

## Workflow

1. **Entrada** — o usuário passa `Classe + help_id`, ou cola linhas do HelpList/datagrid
   (`165<TAB>Cadastros<TAB>Garantia Financeira<TAB>SellerFinancialGuaranteeView<TAB>1`).
   Se uma linha não tiver nome de controller identificável, pergunte qual é a classe — não chute
   (o script tem um fallback que mapeia "Importar" → `SellerStockImportForm`; confirme antes).
2. **Executar o script** (ele localiza o arquivo em `app/control/`, normaliza CRLF→LF, injeta e roda `php -l`):

   Individual:
   ```bash
   python3 ~/.claude/skills/add-header-action/scripts/add_header_action.py --class SellerStockList --help-id 176
   ```
   Atualizar help_id existente:
   ```bash
   python3 ~/.claude/skills/add-header-action/scripts/add_header_action.py --class SellerStockList --help-id 176 --force
   ```
   Lote (prefira arquivo no scratchpad para preservar TABs):
   ```bash
   python3 ~/.claude/skills/add-header-action/scripts/add_header_action.py --batch-file /caminho/lista_helps.txt
   # ou inline: --batch "165\tCadastros\tGarantia Financeira\tSellerFinancialGuaranteeView\t1\n168\tListagem\tSaldo Estoque\tSellerStockList\t1"
   ```
3. **Verificar** — para cada arquivo alterado, confira o diff/trecho: o botão ficou dentro do
   `__construct` (após o último `$this->form->addAction(...)`) e `onHelp` antes do `}` final da classe.
   Se aparecer `[AVISO] ... não foi possível injetar addHeaderAction`, edite manualmente (padrão abaixo).
   Se aparecer `[ERRO-PHP]`, o script já restaurou o original — corrija manualmente.
4. **Relatar** — liste classe → help_id → resultado (ADD / UPDATE / já existia / falha).

## Padrão manual (referência)

No `__construct`, após as ações do formulário e antes de empacotar no container:
```php
        $Help = $this->form->addHeaderAction("Ajuda", new TAction([$this, 'onHelp']), 'fas:question #00BCD4');
        $this->Help = $Help;
```

Antes da última chave da classe:
```php
    public function onHelp($param = null) 
    {
        try 
        {
            //code here
            $param = [];
            $param['help_id'] = {HELP_ID};
            $param['routine_id'] = null;
            $param['form_name'] = '{CLASS_NAME}';

            AdiantiCoreApplication::loadPage('FormHelp', 'onShow', $param);

        }
        catch (Exception $e) 
        {
            new TMessage('error', $e->getMessage());    
        }
    }
```

## Regras críticas

- **NUNCA execute SQL** (INSERT/UPDATE em MySQL/Postgres). O cadastro no HelpCenter é feito pelo usuário/migração.
- **CRLF**: arquivos legados podem ter `\r\n`. O script normaliza; em edição manual rode `sed -i 's/\r$//' <arquivo>` antes.
- **Callbacks**: `TAction`/`TDataGridAction` validam `is_callable` — classe/método apontado precisa existir
  (e estar em `application.ini` se for página pública), senão a tela lança exceção fatal.
- O script assume `$this->form`. Em telas sem `$this->form` (ex.: só datagrid/painel), ajuste manualmente para o objeto correto.
- Sempre `php -l <arquivo>` após qualquer alteração manual.
