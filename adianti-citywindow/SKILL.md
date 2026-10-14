---
name: adianti-citywindow
description: CityWindow — Tutor Organization > StandardControls
triggers: ["CityWindow", "Tutor", "Organization", "StandardControls"]
---

# Skill Adianti — CityWindow — Tutor Organization > StandardControls

Classe Tutor: `CityWindow`.
Ver no Tutor: `index.php?class=CityWindow` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/StandardControls/CityWindow.class.php`.


## Código

```php
<?php
/**
 * CityWindow Registration
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class CityWindow extends TWindow
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
        parent::setModal(true);
        parent::removePadding();
        parent::setSize(600, null);
        parent::setTitle('City');
        
        $this->setDatabase('samples');    // defines the database
        $this->setActiveRecord('City');   // defines the active record
        
        // creates the form
        $this->form = new BootstrapFormBuilder('form_City');
        $this->form->setProperty('class', 'card noborder');
        
        // create the form fields
        $id       = new THidden('id');
        $name     = new TEntry('name');
        $state_id = new TDBCombo('state_id', 'samples', 'State', 'id', 'name');
        $id->setEditable(FALSE);
        
        // add the form fields
        $this->form->addFields( [$id] );
        $this->form->addFields( [new TLabel('Name', 'var(--bs-red)')], [$name] );
        $this->form->addFields( [new TLabel('State', 'var(--bs-red)')], [$state_id] );
        
        $name->addValidation( 'Name', new TRequiredValidator);
        $state_id->addValidation( 'State', new TRequiredValidator);
        
        // define the form action
        $btn = $this->form->addAction('Save', new TAction(array($this, 'onSave')), 'fa:check');
        $btn->class = 'btn btn-primary btn-sm';
        
        $this->setAfterSaveAction( new TAction([$this, 'onClose']));
        $this->setUseMessages(false);
        
        parent::add($this->form);
    }
    
    /**
     * Close window after insert
     */
    public static function onClose()
    {
        parent::closeWindow();
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
