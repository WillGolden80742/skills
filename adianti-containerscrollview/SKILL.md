---
name: adianti-containerscrollview
description: Scroll — Tutor Presentation > Containers > Scroll
triggers: ["ContainerScrollView", "Scroll", "Tutor", "Presentation", "Containers"]
---

# Skill Adianti — Scroll — Tutor Presentation > Containers > Scroll

Classe Tutor: `ContainerScrollView`.
Ver no Tutor: `index.php?class=ContainerScrollView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Containers/ContainerScrollView.class.php`.


## Código

```php
<?php
/**
 * ContainerScrollView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class ContainerScrollView extends TPage
{
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        // creates the scroll panel
        $scroll = new TScroll;
        $scroll->setSize('100%','300');
        
        // creates a table for the fields
        $fields_table = new TTable;
        // adds the table inside the scroll 
        $scroll->add($fields_table);
        
        // create the form fields
        $fields = array();
        for ($n=1; $n<=20; $n++)
        {
            $object = new TEntry('field'.$n);
            $fields[$n] = $object;
            
            // adds a row for each form field
            $row=$fields_table->addRow();
            $row->addCell(new TLabel('Field:'.$n));
            $row->addCell($object);
        }
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($scroll);
        
        parent::add($vbox);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
