---
name: adianti-formclientinteractionsview
description: Client interactions — Tutor Presentation > Forms > Client interactions
triggers: ["FormClientInteractionsView", "Client", "interactions", "Tutor", "Presentation", "Forms", "Client interactions"]
---

# Skill Adianti — Client interactions — Tutor Presentation > Forms > Client interactions

Classe Tutor: `FormClientInteractionsView`.
Ver no Tutor: `index.php?class=FormClientInteractionsView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormClientInteractionsView.class.php`.


## Código

```php
<?php
/**
 * FormClientInteractionsView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormClientInteractionsView extends TPage
{
    private $form;
    
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        // create the form
        $this->form = new BootstrapFormBuilder('form_bmi');
        $this->form->setFormTitle(_t('Client interactions'));
        
        // create the form fields
        $mass   = new TEntry('mass');
        $height = new TEntry('height');
        $result = new TEntry('result');
        
        $result->setEditable(FALSE);
        
        // add the fields inside the form
        $this->form->addFields( [new TLabel('Mass (Kg)')],  [$mass] );
        $this->form->addFields( [new TLabel('Height (m)')], [$height] );
        $this->form->addFields( [new TLabel('Result')],     [$result] );
        
        $mass->onBlur   = 'calculate_bmi()';
        $height->onBlur = 'calculate_bmi()';
        
        TScript::create('calculate_bmi = function() {
            if (document.form_bmi.mass.value > 0 && document.form_bmi.height.value > 0)
            {
                form_bmi.result.value = parseFloat(form_bmi.mass.value) /
                               Math.pow(parseFloat(form_bmi.height.value),2);
            }
        };');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);

        parent::add($vbox);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
