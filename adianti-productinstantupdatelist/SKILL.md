---
name: adianti-productinstantupdatelist
description: Batch instant update list — Tutor Organization > Batch operations > Batch instant update list
triggers: ["ProductInstantUpdateList", "Batch", "instant", "update", "list", "Tutor", "Organization", "Batch instant update list", "Batch operations"]
---

# Skill Adianti — Batch instant update list — Tutor Organization > Batch operations > Batch instant update list

Classe Tutor: `ProductInstantUpdateList`.
Ver no Tutor: `index.php?class=ProductInstantUpdateList` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/BatchOperations/ProductInstantUpdateList.class.php`.


## Código

```php
<?php
/**
 * ProductUpdateList
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class ProductInstantUpdateList extends TPage
{
    protected $datagrid; // listing
    protected $pageNavigation;
    
    use Adianti\Base\AdiantiStandardListTrait;
    
    /**
     * Page constructor
     */
    public function __construct()
    {
        parent::__construct();
        
        $this->setDatabase('samples');
        $this->setActiveRecord('Product');
        $this->setDefaultOrder('id', 'asc');
        // add the filter (filter field, operator, form field)
        $this->addFilterField('description', 'like', 'description');
        
        // creates the form
        $this->form = new BootstrapFormBuilder('form_search_Product');
        $this->form->setFormTitle(_t('Batch instant update list'));
        
        // create the form fields
        $description = new TEntry('description');
        $this->form->addFields( [new TLabel('Description')], [$description] );
        
        $this->form->addAction(_t('Find'), new TAction(array($this, 'onSearch')), 'fa:search');
        
        // keep the form filled with session data
        $this->form->setData( TSession::getValue('Product_filter_data') );
        
        // creates the datagrid
        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        $this->datagrid->style = 'width: 100%';
        
        // create the datagrid columns
        $column_id = new TDataGridColumn('id', 'Id', 'left');
        $column_description = new TDataGridColumn('description', 'Description', 'left');
        $column_unity = new TDataGridColumn('unity', 'Unity', 'center');
        $column_stock = new TDataGridColumn('stock', 'Stock', 'right');
        $column_sale_price = new TDataGridColumn('sale_price_widget', 'Sale Price', 'right');

        $column_sale_price->setTransformer( function($value, $object, $row) {
            $widget = new TEntry('sale_price' . '_' . $object->id);
            
            $widget->setNumericMask(2,',','.', true);
            $widget->setValue( $object->sale_price );
            
            $widget->setSize(120);
            $widget->setFormName('form_search_Product');
            
            $action = new TAction( [$this, 'onSaveInline'],
                                   ['column' => 'sale_price'] );
            
            $widget->setExitAction( $action );
            return $widget;
        });
        $this->datagrid->addColumn($column_id);
        $this->datagrid->addColumn($column_description);
        $this->datagrid->addColumn($column_unity);
        $this->datagrid->addColumn($column_stock);
        $this->datagrid->addColumn($column_sale_price);

        // create the datagrid model
        $this->datagrid->createModel();
        
        // creates the pagination
        $this->pageNavigation = new TPageNavigation;
        $this->pageNavigation->setAction(new TAction(array($this, 'onReload')));
        
        $this->datagrid->disableDefaultClick();
        
        // vertical box container
        $container = new TVBox;
        $container->style = 'width: 100%';
        $container->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $container->add($this->form);
        $container->add(TPanelGroup::pack('', $this->datagrid, $this->pageNavigation));
        
        parent::add($container);
    }
    
    /**
     * Save the datagrid objects
     */
    public static function onSaveInline($param)
    {
        $name   = $param['_field_name'];
        $value  = $param['_field_value'];
        $column = $param['column'];
        
        $parts  = explode('_', $name);
        $id     = end($parts);
        
        try
        {
            // open transaction
            TTransaction::open('samples');
            
            $object = Product::find($id);
            if ($object)
            {
                $object->$column = str_replace(['.', ','],['', '.'],$value);
                $object->store();
            }
            
            TToast::show('success', '<b>'.$object->description . '</b> updated',
                         'bottom center', 'far:check-circle');
            
            // close transaction
            TTransaction::close();
        }
        catch (Exception $e)
        {
            // show the exception message
            TToast::show('error', $e->getMessage(), 'bottom center', 'fa:exclamation-triangle');
        }
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
