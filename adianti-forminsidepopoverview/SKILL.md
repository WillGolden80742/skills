---
name: adianti-forminsidepopoverview
description: Form inside Popover — Tutor Presentation > Extras > Form inside Popover
triggers: ["FormInsidePopoverView", "Form", "inside", "Popover", "Tutor", "Presentation", "Extras", "Form inside Popover"]
---

# Skill Adianti — Form inside Popover — Tutor Presentation > Extras > Form inside Popover

Classe Tutor: `FormInsidePopoverView`.
Ver no Tutor: `index.php?class=FormInsidePopoverView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extras/FormInsidePopoverView.class.php`.


## Código

```php
<?php
/**
 * FormInsidePopoverView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormInsidePopoverView extends TPage
{
    public function __construct()
    {
        parent::__construct();
        //parent::include_css('app/resources/myframe.css');
        
        $button = new TButton('bt4a');
        $button->setImage('far:list-alt blue');
        $button->setLabel('Open form inside popover');
        
        $action = new TAction(array('FormSessionDataView', 'onEdit'));
        // $action->setParameter('key', '1');
        
        $button->popover    = 'true';
        $button->popside    = 'bottom';
        $button->poptitle   = 'Pop title 1';
        $button->poptrigger = 'click';
        $button->popaction  = $action->serialize(FALSE);
        
        parent::add($button);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
