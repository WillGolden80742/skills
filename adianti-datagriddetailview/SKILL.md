---
name: adianti-datagriddetailview
description: Datagrid details — Tutor Presentation > Extras > Datagrid details
triggers: ["DatagridDetailView", "Datagrid", "details", "Tutor", "Presentation", "Extras", "Datagrid details"]
---

# Skill Adianti — Datagrid details — Tutor Presentation > Extras > Datagrid details

Classe Tutor: `DatagridDetailView`.
Ver no Tutor: `index.php?class=DatagridDetailView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extras/DatagridDetailView.class.php`.


## Código

```php
<?php
/**
 * DatagridDetailView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class DatagridDetailView extends TPage
{
    private $datagrid;
    
    public function __construct()
    {
        parent::__construct();
        
        // creates one datagrid
        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        $this->datagrid->setHeight(320);
        
        // add the columns
        $this->datagrid->addColumn( new TDataGridColumn('code',  'Code',  'center', '10%') );
        $this->datagrid->addColumn( new TDataGridColumn('name',  'Name',  'left',   '30%') );
        $this->datagrid->addColumn( new TDataGridColumn('city',  'City',  'left',   '30%') );
        $this->datagrid->addColumn( new TDataGridColumn('state', 'State', 'left',   '30%') );
        
        // creates datagrid action
        $action1 = new TDataGridAction(array($this, 'onShowDetail'), ['code' => '{code}'] );
        $this->datagrid->addAction($action1, 'View', 'fa:search #000000');
        
        // creates the datagrid model
        $this->datagrid->createModel();
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add(TPanelGroup::pack('', $this->datagrid));

        parent::add($vbox);
    }
    
    /**
     * Load the data into the datagrid
     */
    function onReload( $param )
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
     * Show record detail
     */
    public function onShowDetail( $param )
    {
        // get row position
        $pos = $this->datagrid->getRowIndex('code', $param['key']);
        
        // get row by position
        $current_row = $this->datagrid->getRow($pos);
        $current_row->className = "selected";
        
        // create a new row
        $row = new TTableRow;
        $row->addCell('');
        $cell = $row->addCell('In this space, you can add any detail<br> content about the selected record');
        $cell->colspan = 4;
        $cell->style = 'padding:10px;';
        
        // insert the new row
        $this->datagrid->insert($pos +1, $row);
    }
    
    /**
     * shows the page
     */
    function show()
    {
        $this->onReload( func_get_arg(0) );
        parent::show();
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
