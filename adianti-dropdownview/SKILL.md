---
name: adianti-dropdownview
description: Dropdown — Tutor Presentation > Utilities > Dropdown
triggers: ["DropdownView", "Dropdown", "Tutor", "Presentation", "Utilities"]
---

# Skill Adianti — Dropdown — Tutor Presentation > Utilities > Dropdown

Classe Tutor: `DropdownView`.
Ver no Tutor: `index.php?class=DropdownView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Widgets/DropdownView.class.php`.


## Código

```php
<?php
/**
 * DropdownView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class DropdownView extends TPage
{
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        // creates the dropdown
        $dropdown = new TDropDown('Dropdown test', 'fa:list');
        //$dropdown->setButtonClass('btn btn-info waves-effect dropdown-toggle');
        $dropdown->addAction( 'Show a message', new TAction(array($this, 'onMessage') ));
        $dropdown->addAction( 'Customer list', new TAction(array('CustomerDataGridView', 'onReload') ));
        
        $actions = [];
        $actions[] = ['Sub Action 1', new TAction(array($this, 'onMessage')), 'fa:list' ];
        $actions[] = ['Sub Action 2', new TAction(array($this, 'onMessage')), 'fa:cog' ];
        $dropdown->addActionGroup('Another group', $actions, '');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($dropdown);
        
        parent::add($vbox);
    }
    
    /**
     * Show some message
     * @param $param URL parameters containing key and value
     */
    public function onMessage($param)
    {
        new TMessage('info', 'Test');
    }
}
?>
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
