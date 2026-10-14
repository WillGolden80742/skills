---
name: adianti-multicheck2view
description: MultiCheck2View — Tutor Organization > BatchOperations
triggers: ["MultiCheck2View", "MultiCheck", "View", "Tutor", "Organization", "BatchOperations", "MultiCheck2"]
---

# Skill Adianti — MultiCheck2View — Tutor Organization > BatchOperations

Classe Tutor: `MultiCheck2View`.
Ver no Tutor: `index.php?class=MultiCheck2View` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/BatchOperations/MultiCheck2View.class.php`.


## Código

```php
<?php
/**
 * Multi Step 2
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class MultiCheck2View extends TPage
{
    private $datagrid;
    
    public function __construct()
    {
        parent::__construct();
        
        // creates one datagrid
        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        $this->datagrid->setHeight(320);
        $this->datagrid->style = 'width: 100%';
        
        // add the columns
        $this->datagrid->addColumn( new TDataGridColumn('id',  'Code',  'right', '70') );
        $this->datagrid->addColumn( new TDataGridColumn('description',  'Description',  'left') );
        
        // creates the datagrid model
        $this->datagrid->createModel();
        
        $back = new TElement('a');
        $back->href = (new TAction(array('MultiCheckView', 'onReload')))->serialize();
        $back->class = 'btn btn-default';
        $back->generator = 'adianti';
        $back->add('<i class="fa fa-backward blue"></i> Back');
        
        $panel = new TPanelGroup('Selected items');
        $panel->add( $this->datagrid );
        $panel->addFooter( $back );
        
        // wrap the page content
        parent::add($panel);
    }
    
    /**
     * Load the data into the datagrid
     */
    function onReload()
    {
        $this->datagrid->clear();
        $selected_products = TSession::getValue('selected_products');
        
        if ($selected_products)
        {
            TTransaction::open('samples');
            foreach ($selected_products as $selected_product)
            {
                $this->datagrid->addItem( new Product($selected_product) );
            }
            TTransaction::close();
        }
    }
    
    /**
     * shows the page
     */
    function show()
    {
        $this->onReload();
        parent::show();
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
