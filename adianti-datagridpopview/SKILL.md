---
name: adianti-datagridpopview
description: Datagrids with popover — Tutor Presentation > Extras > Datagrids with popover
triggers: ["DatagridPopView", "Datagrids", "with", "popover", "Tutor", "Presentation", "Extras", "Datagrids with popover"]
---

# Skill Adianti — Datagrids with popover — Tutor Presentation > Extras > Datagrids with popover

Classe Tutor: `DatagridPopView`.
Ver no Tutor: `index.php?class=DatagridPopView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Datagrid/DatagridPopView.class.php`.


## Código

```php
<?php
/**
 * DatagridPopView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class DatagridPopView extends TPage
{
    private $datagrid;
    
    public function __construct()
    {
        parent::__construct();
        
        // creates one datagrid
        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        $this->datagrid->style = 'width: 100%';
        
        $this->datagrid->addColumn( new TDataGridColumn('code',  'Code',  'center', '10%') );
        $this->datagrid->addColumn( new TDataGridColumn('name',  'Name',  'left',   '30%') );
        $this->datagrid->addColumn( new TDataGridColumn('city',  'City',  'left',   '30%') );
        $this->datagrid->addColumn( new TDataGridColumn('state', 'State', 'left',   '30%') );
        
        // creates the datagrid model
        $this->datagrid->createModel();
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add(TPanelGroup::pack(_t('Datagrids with popover'), $this->datagrid, 'footer'));

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
        $row = $this->datagrid->addItem($item);
        
        $row->popover = 'true';
        $row->popside = 'top';
        $row->popcontent = "<table class='popover-table'>
                                <tr><td>Name</td><td>{$item->name}</td></tr>
                                <tr><td>City</td><td>{$item->city}</td></tr>
                            </table>";
        $row->poptitle = 'Item details';
        
        // add an regular object to the datagrid
        $item = new StdClass;
        $item->code   = '2';
        $item->name   = 'Eric Clapton';
        $item->city   = 'Ripley';
        $item->state  = 'Surrey (UK)';
        $row = $this->datagrid->addItem($item);
        
        $row->popover = 'true';
        $row->popside = 'top';
        $row->popcontent = "<table class='popover-table'>
                                <tr><td>Name</td><td>{$item->name}</td></tr>
                                <tr><td>City</td><td>{$item->city}</td></tr>
                            </table>";
        $row->poptitle = 'Item details';
        
        // add an regular object to the datagrid
        $item = new StdClass;
        $item->code   = '3';
        $item->name   = 'B.B. King';
        $item->city   = 'Itta Bena';
        $item->state  = 'Mississippi (US)';
        $row = $this->datagrid->addItem($item);
        
        $row->popover = 'true';
        $row->popside = 'top';
        $row->popcontent = "<table class='popover-table'>
                                <tr><td>Name</td><td>{$item->name}</td></tr>
                                <tr><td>City</td><td>{$item->city}</td></tr>
                            </table>";
        $row->poptitle = 'Item details';
        
        // add an regular object to the datagrid
        $item = new StdClass;
        $item->code   = '4';
        $item->name   = 'Janis Joplin';
        $item->city   = 'Port Arthur';
        $item->state  = 'Texas (US)';
        $row = $this->datagrid->addItem($item);
        
        $row->popover = 'true';
        $row->popside = 'top';
        $row->popcontent = "<table class='popover-table'>
                                <tr><td>Name</td><td>{$item->name}</td></tr>
                                <tr><td>City</td><td>{$item->city}</td></tr>
                            </table>";
        $row->poptitle = 'Item details';
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
