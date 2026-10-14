---
name: adianti-containerpagewrapper
description: Page Wrapper — Tutor Presentation > Containers > Page Wrapper
triggers: ["ContainerPageWrapper", "Page", "Wrapper", "Tutor", "Presentation", "Containers", "Page Wrapper"]
---

# Skill Adianti — Page Wrapper — Tutor Presentation > Containers > Page Wrapper

Classe Tutor: `ContainerPageWrapper`.
Ver no Tutor: `index.php?class=ContainerPageWrapper` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Containers/ContainerPageWrapper.class.php`.


## Código

```php
<?php
/**
 * ContainerPageWrapper
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class ContainerPageWrapper extends TPage
{
    /**
     * Class constructor
     * Creates the page
     */
    public function __construct()
    {
        parent::__construct();
        
        $pw1 = new TPageWrapper;
        $pw1->setClass('FullCalendarSplitView');
        $pw1->setMethod('onReload');
        $pw1->setSize('100%', 500);
        
        $pw2 = new TPageWrapper;
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
