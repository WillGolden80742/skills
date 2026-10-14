---
name: adianti-datagridstyleview
description: DatagridStyleView — Tutor Presentation > Extras
triggers: ["DatagridStyleView", "Tutor", "Presentation", "Extras", "DatagridStyle"]
---

# Skill Adianti — DatagridStyleView — Tutor Presentation > Extras

Classe Tutor: `DatagridStyleView`.
Ver no Tutor: `index.php?class=DatagridStyleView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extras/DatagridStyleView.class.php`.
Nota: Esta página não roda standalone no Tutor — exige registro em menu.xml (TXMLBreadCrumb).


## Código

```php
<?php
/**
 * DatagridStyleView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class DatagridStyleView extends TPage
{
    private $datagrid;
    
    public function __construct()
    {
        parent::__construct();
        
        // creates one datagrid
        $this->datagrid = new TDataGrid;
        $this->datagrid->setHeight(320);
        
        // define the CSS class
        $this->datagrid->class='tdatagrid_table customized-table';
        
        // import the CSS file
        parent::include_css('app/resources/custom-table.css');

        // add the columns
        $this->datagrid->addColumn( new TDataGridColumn('code',  'Code',  'center', '10%') );
        $this->datagrid->addColumn( new TDataGridColumn('name',  'Name',  'left',   '30%') );
        $this->datagrid->addColumn( new TDataGridColumn('city',  'City',  'left',   '30%') );
        $this->datagrid->addColumn( new TDataGridColumn('state', 'State', 'left',   '30%') );
        
        $action1 = new TDataGridAction([$this, 'onView'],   ['name' => '{name}'] );
        $action1->setUseButton(TRUE);
        $action1->setButtonClass('btn btn-default');
        $action1->setImage('fa:search green');
        
        $this->datagrid->addAction($action1, 'View', 'fa:search blue');
        
        // creates the datagrid model
        $this->datagrid->createModel();
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->datagrid);

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
        $item->code   = '1';
        $item->name   = 'Aretha Franklin';
        $item->city   = 'Memphis';
        $item->state  = 'Tennessee (US)';
        $this->datagrid->addItem($item);
        
        // add an regular object to the datagrid
        $item = new StdClass;
        $item->code   = '2';
        $item->name   = 'Eric Clapton';
        $item->city   = 'Ripley';
        $item->state  = 'Surrey (UK)';
        $this->datagrid->addItem($item);
        
        // add an regular object to the datagrid
        $item = new StdClass;
        $item->code   = '3';
        $item->name   = 'B.B. King';
        $item->city   = 'Itta Bena';
        $item->state  = 'Mississippi (US)';
        $this->datagrid->addItem($item);
        
        // add an regular object to the datagrid
        $item = new StdClass;
        $item->code   = '4';
        $item->name   = 'Janis Joplin';
        $item->city   = 'Port Arthur';
        $item->state  = 'Texas (US)';
        $this->datagrid->addItem($item);
    }
    
    /**
     * method onView()
     * Executed when the user clicks at the view button
     */
    function onView($param)
    {
        // get the parameter and shows the message
        $key=$param['key'];
        new TMessage('info', "The name is : $key");
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
