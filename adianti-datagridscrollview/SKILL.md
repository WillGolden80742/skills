---
name: adianti-datagridscrollview
description: Vertical Scrollable Datagrids — Tutor Presentation > Datagrids > Vertical Scrollable Datagrids
triggers: ["DatagridScrollView", "Vertical", "Scrollable", "Datagrids", "Tutor", "Presentation", "Vertical Scrollable Datagrids"]
---

# Skill Adianti — Vertical Scrollable Datagrids — Tutor Presentation > Datagrids > Vertical Scrollable Datagrids

Classe Tutor: `DatagridScrollView`.
Ver no Tutor: `index.php?class=DatagridScrollView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Datagrid/DatagridScrollView.class.php`.


## Código

```php
<?php
/**
 * DatagridScrollView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class DatagridScrollView extends TPage
{
    private $datagrid;
    
    public function __construct()
    {
        parent::__construct();
        
        // creates one datagrid
        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        $this->datagrid->style = 'width: 100%';
        
        // make scrollable and define height
        $this->datagrid->setHeight(300);
        $this->datagrid->makeScrollable();
        
        // create the datagrid columns
        $code       = new TDataGridColumn('code',    'Code',    'right',  '10%');
        $name       = new TDataGridColumn('name',    'Name',    'left',   '30%');
        $address    = new TDataGridColumn('address', 'Address', 'left',   '30%');
        $telephone  = new TDataGridColumn('fone',    'Phone',   'left',   '30%');
        
        // add the columns to the datagrid
        $this->datagrid->addColumn($code);
        $this->datagrid->addColumn($name);
        $this->datagrid->addColumn($address);
        $this->datagrid->addColumn($telephone);
        
        // creates the datagrid model
        $this->datagrid->createModel();
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add(TPanelGroup::pack(_t('Vertical Scrollable Datagrids'), $this->datagrid, 'footer'));

        parent::add($vbox);
    }
    
    /**
     * Load the data into the datagrid
     */
    function onReload()
    {
        $this->datagrid->clear();
        
        for ($n=1; $n<=40; $n++)
        {
            // add an regular object to the datagrid
            $item = new StdClass;
            $item->code     = $n;
            $item->name     = 'Person name';
            $item->address  = 'Person address';
            $item->fone     = '1111-1111';
            $this->datagrid->addItem($item);
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
