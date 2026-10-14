---
name: adianti-datagridqueryview
description: Datagrid SQL query — Tutor Presentation > Datagrids > Datagrid SQL query
triggers: ["DatagridQueryView", "Datagrid", "SQL", "query", "Tutor", "Presentation", "Datagrids", "Datagrid SQL query"]
---

# Skill Adianti — Datagrid SQL query — Tutor Presentation > Datagrids > Datagrid SQL query

Classe Tutor: `DatagridQueryView`.
Ver no Tutor: `index.php?class=DatagridQueryView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Datagrid/DatagridQueryView.class.php`.


## Código

```php
<?php
/**
 * DatagridQueryView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class DatagridQueryView extends TPage
{
    private $datagrid;
    
    public function __construct()
    {
        parent::__construct();
        
        // creates one datagrid
        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        
        // create the datagrid columns
        $id    = new TDataGridColumn('id',       'ID',     'center', '30%');
        $name  = new TDataGridColumn('name',     'Name',   'left',   '40%');
        $total = new TDataGridColumn('total',    'Total',  'right',   '30%');
        
        $total->setTransformer( function($value) {
            return 'R$ ' . number_format($value, 2, '.', '.');
        });
        
        // add the columns to the datagrid, with actions on column titles, passing parameters
        $this->datagrid->addColumn($id);
        $this->datagrid->addColumn($name);
        $this->datagrid->addColumn($total);
        
        // creates two datagrid actions
        $action1 = new TDataGridAction([$this, 'onView'],   ['name'=>'{name}',  'total' => '{total}'] );
        
        // custom button presentation
        $action1->setUseButton(TRUE);
        
        // add the actions to the datagrid
        $this->datagrid->addAction($action1, 'View', 'fa:search blue');
        
        // creates the datagrid model
        $this->datagrid->createModel();
        
        
        
        ############## START POPULATING DATA #######################
        
        $source = TTransaction::open('samples');
        // transformation function
        $double_function  = function ($value, $row) {
                return $value  * 2;
        };
        
        // mapping rules between source query and the target table
        $mapping = [];
        $mapping[] = [ 'customer_id',   'id' ];
        $mapping[] = [ 'customer_name', 'name' ];
        $mapping[] = [ 'valor',         'total', $double_function ];
        
        // define the query
        $query = "SELECT customer_id as \"customer_id\",
                         customer.name as \"customer_name\",
                         sum(total) as \"valor\"
                    FROM sale, customer
                   WHERE sale.customer_id = customer.id
                     AND date >= ?
                GROUP BY 1
                ORDER BY 1";
        
        $return = TDatabase::getData($source, $query, $mapping, ['2015-01-01']);
        
        TTransaction::close();
        
        if ($return)
        {
            foreach ($return as $row)
            {
                // add an regular object to the datagrid
                $item = new StdClass;
                $item->id     = $row['id'];
                $item->name   = $row['name'];
                $item->total  = $row['total'];
                
                $this->datagrid->addItem($item);
            }
        }
        
        
        ############## FINISH POPULATING DATA #######################
        
        
        $panel = new TPanelGroup(_t('Datagrid SQL query'));
        $panel->add($this->datagrid)->style = 'overflow-x:auto';
        $panel->addFooter('footer');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($panel);

        parent::add($vbox);
    }
    
    
    /**
     * Executed when the user clicks at the view button
     */
    public static function onView($param)
    {
        // get the parameter and shows the message
        $name   = $param['name'];
        $total  = number_format($param['total'],2,',', '.');
        new TMessage('info', "The name is: <b>$name</b> <br> The total is : <b>$total</b>");
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
