---
name: adianti-datagridlabelview
description: Datagrid with label — Tutor Presentation > Datagrids > Datagrid with label
triggers: ["DatagridLabelView", "Datagrid", "with", "label", "Tutor", "Presentation", "Datagrids", "Datagrid with label"]
---

# Skill Adianti — Datagrid with label — Tutor Presentation > Datagrids > Datagrid with label

Classe Tutor: `DatagridLabelView`.
Ver no Tutor: `index.php?class=DatagridLabelView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Datagrid/DatagridLabelView.class.php`.


## Código

```php
<?php
/**
 * DatagridLabelView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class DatagridLabelView extends TPage
{
    private $datagrid;
    
    public function __construct()
    {
        parent::__construct();
        
        // creates one datagrid
        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        $this->datagrid->style = 'width: 100%';
        
        // add the columns
        $this->datagrid->addColumn( new TDataGridColumn('code',  'Code', 'center', '10%') );
        $this->datagrid->addColumn( new TDataGridColumn('task',  'Task', 'left', '50%') );
        $column = $this->datagrid->addColumn( new TDataGridColumn('status', 'Status', 'center', '40%') );
        
        // define the transformer method over image
        $column->setTransformer( function($value, $object, $row) {
            $div = new TElement('span');
            $div->class="label label-{$value}";
            $div->style="text-shadow:none; font-size:12px";
            $div->add($object->status_value);
            return $div;
        });
        
        // creates the datagrid model
        $this->datagrid->createModel();
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add(TPanelGroup::pack(_t('Datagrid with label'), $this->datagrid, 'footer'));

        parent::add($vbox);
    }
    
    /**
     * Load the data into the datagrid
     */
    function onReload()
    {
        $this->datagrid->clear();
        
        // add an regular object to the datagrid
        $item = new StdClass;
        $item->code         = '1';
        $item->task         = 'Install Ubuntu Server';
        $item->status       = 'primary';
        $item->status_value = 'Started';
        $this->datagrid->addItem($item);
        
        // add an regular object to the datagrid
        $item = new StdClass;
        $item->code         = '2';
        $item->task         = 'Install Apache';
        $item->status       = 'info';
        $item->status_value = 'Almost there';
        $this->datagrid->addItem($item);
        
        // add an regular object to the datagrid
        $item = new StdClass;
        $item->code         = '3';
        $item->task         = 'Install PHP';
        $item->status       = 'success';
        $item->status_value = 'Ready';
        $this->datagrid->addItem($item);
        
        // add an regular object to the datagrid
        $item = new StdClass;
        $item->code         = '4';
        $item->task         = 'Install PostgreSQL';
        $item->status       = 'warning';
        $item->status_value = 'Late';
        $this->datagrid->addItem($item);
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
