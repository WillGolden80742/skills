---
name: adianti-breadcrumbview
description: BreadCrumbView — Tutor Presentation > Utilities
triggers: ["BreadCrumbView", "Tutor", "Presentation", "Utilities", "BreadCrumb"]
---

# Skill Adianti — BreadCrumbView — Tutor Presentation > Utilities

Classe Tutor: `BreadCrumbView`.
Ver no Tutor: `index.php?class=BreadCrumbView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Widgets/BreadCrumbView.class.php`.
Nota: Esta página não roda standalone no Tutor — exige registro em menu.xml (TXMLBreadCrumb).


## Código

```php
<?php
/**
 * BreadCrumbView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class BreadCrumbView extends TPage
{
    private $step;
    
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        $this->step = new TBreadCrumb;
        $this->step->addItem('Step 1', FALSE);
        $this->step->addItem('Step 2', FALSE);
        $this->step->addItem('Step 3', TRUE);
        $this->step->select('Step 1');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->step);
        
        parent::add($vbox);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
