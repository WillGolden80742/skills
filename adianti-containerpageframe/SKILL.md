---
name: adianti-containerpageframe
description: Page Frame — Tutor Presentation > Containers > Page Frame
triggers: ["ContainerPageFrame", "Page", "Frame", "Tutor", "Presentation", "Containers", "Page Frame"]
---

# Skill Adianti — Page Frame — Tutor Presentation > Containers > Page Frame

Classe Tutor: `ContainerPageFrame`.
Ver no Tutor: `index.php?class=ContainerPageFrame` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Containers/ContainerPageFrame.class.php`.


## Código

```php
<?php
/**
 * ContainerPageFrame
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class ContainerPageFrame extends TPage
{
    /**
     * Class constructor
     * Creates the page
     */
    public function __construct()
    {
        parent::__construct();
        
        $pw1 = new TPageFrame;
        $pw1->setClass('FullCalendarSplitView');
        $pw1->setMethod('onReload');
        $pw1->setSize('100%', 500);
        
        $pw2 = new TPageFrame;
        $pw2->setClass('KanbanDatabaseView');
        $pw2->setMethod('onReload');
        $pw2->setSize('100%', 500);
        
        // creates the vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($pw1);
        $vbox->add($pw2);
        
        parent::add($vbox);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
