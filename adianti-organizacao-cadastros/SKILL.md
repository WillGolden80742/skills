---
name: adianti-organizacao-cadastros
description: Cadastros padronizados, manuais, completos, mestre-detalhe de vendas e filtros em cortina/janela
triggers: ["cadastro padronizado", "StandardForm", "StandardList", "AdiantiStandardFormListTrait", "mestre detalhe", "SaleForm", "filtros cortina", "filtros janela", "CustomerList", "ProductList", "cadastro manual", "cadastro completo"]
---

# Skill Adianti — Organização: Cadastros

Fonte: Tutor menu Organização > Cadastros padronizados, manuais, completos. `app/control/Organization/StandardControls|ManualControls|CompleteRegistrations|ComplexViews/`.

## Páginas cobertas

Padronizados: `StandardFormView`, `StandardDataGridView`, `StandardFormDataGridView`, `StandardFormDataGridCurtainView`, `StandardFormDataGridWindowView`, `SplitRegisterView`.
Manuais: `CompleteFormView`, `CompleteDataGridView`, `CompleteFormDataGridView`.
Completos: `CustomerDataGridView`, `ProductList`, `SaleList`, `CustomerCurtainFilterList`, `CustomerWindowFilterList`, `SaleForm`, `SaleMultiValueForm`, `CustomerFormView`, `ProductForm`.

## Padrão trait padrão (StandardFormDataGridCurtainView real — código completo no Tutor)

```php
class StandardFormDataGridCurtainView extends TPage
{
    protected $form; protected $datagrid; protected $loaded; protected $pageNavigation;
    use Adianti\Base\AdiantiStandardFormListTrait;

    public function __construct() {
        parent::__construct();
        $this->setDatabase('samples');
        $this->setActiveRecord('Category');
        $this->setDefaultOrder('id', 'asc');
        $this->setLimit(-1);

        $this->form = new BootstrapFormBuilder('form_categories');
        $this->form->setFormTitle(_t('Standard Form/DataGrid'));
        $id = new TEntry('id'); $name = new TEntry('name');
        $this->form->addFields([new TLabel('ID')], [$id]);
        $this->form->addFields([new TLabel('Name','red')], [$name]);
        $name->addValidation('Name', new TRequiredValidator);
        $this->form->addAction('Save', new TAction([$this,'onSave']), 'fa:save green');
        $id->setEditable(FALSE);

        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        $this->datagrid->width = '100%';
        $col_id = new TDataGridColumn('id','Id','right','10%');
        $col_name = new TDataGridColumn('name','Name','left','90%');
        $this->datagrid->addColumn($col_id); $this->datagrid->addColumn($col_name);
        $col_id->setAction(new TAction([$this,'onReload']), ['order'=>'id']);
        $action1 = new TDataGridAction([$this,'onEditCurtain'], ['key'=>'{id}']);
        $action2 = new TDataGridAction([$this,'onDelete'], ['key'=>'{id}']);
        $this->datagrid->addAction($action1, 'Edit', 'far:edit blue');
        $this->datagrid->addAction($action2, 'Delete', 'far:trash-alt red');
        $this->datagrid->createModel();

        $vbox = new TVBox; $vbox->style='width:100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($panel = TPanelGroup::pack('', $this->datagrid));

        $input_search = new TEntry('input_search');
        $input_search->placeholder = _t('Search');
        $this->datagrid->enableSearch($input_search, 'id, name');
        $panel->addHeaderWidget($input_search);
        $panel->addHeaderActionLink(_t('New'), new TAction([$this,'onEditCurtain']), 'fa:plus green');
        parent::add($vbox);
    }

    public static function onEditCurtain($param = null) {
        $page = TPage::create();
        $page->setTargetContainer('adianti_right_panel');
        $page->setProperty('override','true');
        $page->setPageName(__CLASS__);
        $btn_close = new TButton('closeCurtain');
        $btn_close->onClick = "Template.closeRightPanel();";
        $btn_close->setLabel("Fechar"); $btn_close->setImage('fas:times');
        $embed = new self($param);
        $embed->form->addHeaderWidget($btn_close);
        $embed->onEdit($param);
        $page->add($embed->form);
        $page->show();
    }
}
```

## Trait provê de graça

`onSave`, `onEdit`, `onDelete`, `onReload`, `onSearch`, `setDatabase`, `setActiveRecord`, `setDefaultOrder`, `setLimit`, `setFilterField`.

## Mestre-detalhe (SaleForm / SaleMultiValueForm)

```php
// cabeçalho Sale + FieldList de SaleItem + total calculado
$items = new TFieldList('items');
$items->addField('Produto', new TDBUniqueSearch('product_id[]','samples','Product','id','description'));
$items->addField('Qtd', new TEntry('amount[]'));
$items->addField('Preço', new TEntry('price[]'));
// onSave: salva Sale, loop nos items, soma total, salva SaleItem[]
```

## Filtros em cortina/janela

`CustomerCurtainFilterList` / `CustomerWindowFilterList`: form de filtro abre em `adianti_right_panel` ou `TWindow`, `onSearch` aplica `TFilter` + `TSession::setValue(__CLASS__.'_filter', $criteria)`.

## Regras

- Comece todo CRUD novo pelo padrão trait — só customize `onEditCurtain/onEditWindow` se precisar.
- `setLimit(-1)` desliga paginação; use `TPageNavigation` se ligar.
- Manuais (`Complete*`) só quando o trait não atende (joins complexos, múltiplas tabelas).
