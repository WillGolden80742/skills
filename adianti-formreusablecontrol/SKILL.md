---
name: adianti-formreusablecontrol
description: Reusable MVC Forms — Tutor Presentation > Extras > Reusable MVC Forms
triggers: ["FormReusableControl", "Reusable", "MVC", "Forms", "Tutor", "Presentation", "Extras", "Reusable MVC Forms"]
---

# Skill Adianti — Reusable MVC Forms — Tutor Presentation > Extras > Reusable MVC Forms

Classe Tutor: `FormReusableControl`.
Ver no Tutor: `index.php?class=FormReusableControl` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extras/FormReusableControl.class.php`.


## Código

```php
<?php
/**
 * FormReusableControl
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormReusableControl extends TPage
{
    private $form;
    
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        // creates the form view
        $this->form = new FormReusableView;
        
        // add a form action
        $this->form->addAction('Show', new TAction(array($this, 'onShow')), 'far:check-circle');
                               
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);
        parent::add($vbox);
    }
    
    /**
     * Show the form content
     */
    public function onShow($param)
    {
        $data = $this->form->getData();
        $this->form->setData($data);

        new TMessage('info', str_replace('","', '",<br>&nbsp;"', json_encode($data)));
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
