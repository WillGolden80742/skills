---
name: adianti-containerpanelgroupview
description: Panel group — Tutor Presentation > Containers > Panel group
triggers: ["ContainerPanelGroupView", "Panel", "group", "Tutor", "Presentation", "Containers", "Panel group"]
---

# Skill Adianti — Panel group — Tutor Presentation > Containers > Panel group

Classe Tutor: `ContainerPanelGroupView`.
Ver no Tutor: `index.php?class=ContainerPanelGroupView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Containers/ContainerPanelGroupView.class.php`.


## Código

```php
<?php
/**
 * ContainerPanelGroupView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class ContainerPanelGroupView extends TPage
{
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        // creates a panel
        $panel = new TPanelGroup('Panel group title');
        $table = new TTable;
        $table->style = 'border-collapse:collapse';
        $table->width = '100%';
        $table->addRowSet('a1','a2');
        $table->addRowSet('b1','b2');
        $panel->add($table);
        $panel->addFooter('Panel group footer');
        
        $panel2 = new TPanelGroup('Collapsable Panel group');
        $panel2->collapse();
        $table2 = new TTable;
        $table2->style = 'border-collapse:collapse';
        $table2->width = '100%';
        $table2->addRowSet('a1','a2');
        $table2->addRowSet('b1','b2');
        $panel2->add($table2);
        $panel2->addFooter('Panel group footer');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($panel);
        $vbox->add($panel2);
        parent::add($vbox);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
