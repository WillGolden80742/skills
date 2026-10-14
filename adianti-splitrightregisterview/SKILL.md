---
name: adianti-splitrightregisterview
description: SplitRightRegisterView — Tutor Organization > StandardControls
triggers: ["SplitRightRegisterView", "Tutor", "Organization", "StandardControls", "SplitRightRegister"]
---

# Skill Adianti — SplitRightRegisterView — Tutor Organization > StandardControls

Classe Tutor: `SplitRightRegisterView`.
Ver no Tutor: `index.php?class=SplitRightRegisterView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/StandardControls/SplitRightRegisterView.class.php`.


## Código

```php
<?php
/**
 * SplitRightRegisterView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class SplitRightRegisterView extends TPage
{
    protected $form; // form
    
    // trait with onSave, onClear, onEdit
    use Adianti\Base\AdiantiStandardFormTrait;
    
    /**
     * Class constructor
     * Creates the page and the registration form
     */
    function __construct()
    {
        parent::__construct();
        
        $this->setDatabase('samples');    // defines the database
        $this->setActiveRecord('City');   // defines the active record
        
        // creates the form
        $this->form = new BootstrapFormBuilder('form_City');
        $this->form->setFormTitle(_t('Register'));
        
        // create the form fields
        $id       = new TEntry('id');
        $name     = new TEntry('name');
        $state_id = new TDBCombo('state_id', 'samples', 'State', 'id', 'name');
        $id->setEditable(FALSE);
        
        // add the form fields
        $this->form->addFields( [new TLabel('ID')], [$id] );
        $this->form->addFields( [new TLabel('Name', 'red')], [$name] );
        $this->form->addFields( [new TLabel('State', 'red')], [$state_id] );
        
        $name->addValidation( 'Name', new TRequiredValidator);
        $state_id->addValidation( 'State', new TRequiredValidator);
        
        // define the form action
        $this->form->addAction('Save', new TAction(array($this, 'onSave')), 'fa:save green');
        $this->form->addAction('Clear',  new TAction(array($this, 'onClear')), 'fa:eraser red');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add($this->form);

        parent::add($this->form);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
