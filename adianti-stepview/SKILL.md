---
name: adianti-stepview
description: Steps — Tutor Presentation > Utilities > Steps
triggers: ["StepView", "Steps", "Tutor", "Presentation", "Utilities"]
---

# Skill Adianti — Steps — Tutor Presentation > Utilities > Steps

Classe Tutor: `StepView`.
Ver no Tutor: `index.php?class=StepView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Widgets/StepView.class.php`.


## Código

```php
<?php
/**
 * StepView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class StepView extends TPage
{
    private $step;
    
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        $this->step = new TPageStep;
        $this->step->addItem('Step 1', new TAction(['CustomerDataGridView', 'onReload']));
        $this->step->addItem('Step 2');
        $this->step->addItem('Step 3');
        $this->step->select('Step 2');
        
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
