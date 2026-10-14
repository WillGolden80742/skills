---
name: adianti-containertablecolumnsview
description: Table Columns — Tutor Presentation > Containers > Table Columns
triggers: ["ContainerTableColumnsView", "Table", "Columns", "Tutor", "Presentation", "Containers", "Table Columns"]
---

# Skill Adianti — Table Columns — Tutor Presentation > Containers > Table Columns

Classe Tutor: `ContainerTableColumnsView`.
Ver no Tutor: `index.php?class=ContainerTableColumnsView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Containers/ContainerTableColumnsView.class.php`.


## Código

```php
<?php
/**
 * ContainerTableColumnsView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class ContainerTableColumnsView extends TPage
{
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        // creates a table
        $table = new TTable;
        
        // creates a label with the title
        $title = new TLabel('Table Columns');
        $title->setFontSize(18);
        $title->setFontFace('Arial');
        $title->setFontColor('red');
        
        // adds a row to the table
        $row = $table->addRow();
        $title = $row->addCell($title);
        $title->colspan = 2;
        
        // creates a series of input widgets
        $id         = new TEntry('id');
        $name       = new TEntry('name');
        $address    = new TEntry('address');
        $telephone  = new TEntry('telephone');
        $city       = new TCombo('city');
        $text       = new TText('text');
        
        $items      = array();
        $items['1'] = 'Porto Alegre';
        $items['2'] = 'Lajeado';
        $city->addItems($items);
        
        // adjust the size of the code
        $id->setSize(70);
        
        // add rows for the fields
        $table->addRowSet( new TLabel('Code'),      $id );
        $table->addRowSet( new TLabel('Name'),      $name );
        $table->addRowSet( new TLabel('City'),      $city );
        $table->addRowSet( new TLabel('Address'),   $address );
        $table->addRowSet( new TLabel('Telephone'), $telephone );
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($table);
        
        parent::add($vbox);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
