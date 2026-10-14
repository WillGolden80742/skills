---
name: adianti-formsessiondataview
description: FormSessionDataView — Tutor Presentation > Extras
triggers: ["FormSessionDataView", "Tutor", "Presentation", "Extras", "FormSessionData"]
---

# Skill Adianti — FormSessionDataView — Tutor Presentation > Extras

Classe Tutor: `FormSessionDataView`.
Ver no Tutor: `index.php?class=FormSessionDataView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extras/FormSessionDataView.class.php`.


## Código

```php
<?php
/**
 * FormSessionDataView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormSessionDataView extends TPage
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
        $this->form = new BootstrapFormBuilder;
        $this->form->style = 'min-width: 200px';
        $this->form->setProperty('style', 'margin:0; border:0');
        $form_id = $this->form->getId();
        
        // create the form fields
        $name  = new TEntry('name');
        $value = new TEntry('value');
        
        // add the fields inside the form
        $row = $this->form->addFields([new TLabel('Name')],  [$name] );
        $row->layout = ['col-sm-4', 'col-sm-8'];
        $row = $this->form->addFields([new TLabel('Value')], [$value] );
        $row->layout = ['col-sm-4', 'col-sm-8'];
        
        // define the form action 
        $this->form->addAction('Send', new TAction(array($this, 'onSend')), 'far:save green');
        
        TScript::create("$('#{$form_id}').closest('.popover-content').css('padding',0)");
        
        parent::add($this->form);
    }
    
    /**
     * Load form with session data
     */
    public function onEdit($param)
    {
        $this->form->setData( (object) TSession::getValue(__CLASS__) );
    }
    
    /**
     * Save form data into session
     */
    public static function onSend($param)
    {
        TSession::setValue(__CLASS__, $param);
        TScript::create("$('.popover').remove();");
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
