---
name: adianti-kanbanstageform
description: KanbanStageForm — Tutor Organization > Utilities
triggers: ["KanbanStageForm", "Tutor", "Organization", "Utilities"]
---

# Skill Adianti — KanbanStageForm — Tutor Organization > Utilities

Classe Tutor: `KanbanStageForm`.
Ver no Tutor: `index.php?class=KanbanStageForm` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/Utilities/KanbanStageForm.class.php`.


## Código

```php
<?php
/**
 * KanbanStageForm
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class KanbanStageForm extends TWindow
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
        parent::setSize(400, null);
        parent::removePadding();
        parent::setTitle('Kanban Stage');
        
        $this->setDatabase('samples');    // defines the database
        $this->setActiveRecord('KanbanStage');   // defines the active record
        
        // creates the form
        $this->form = new BootstrapFormBuilder('form_City');
        $this->form->setProperty('class','card panel noborder');
        $this->form->setProperty('style', 'margin-bottom:0');
        
        // create the form fields
        $id          = new THidden('id');
        $title       = new TEntry('title');
        $stage_order = new THidden('stage_order');
        $id->setEditable(FALSE);
        
        // add the form fields
        $this->form->addFields( [$id] );
        $this->form->addFields( [new TLabel('Title', 'red')], [$title] );
        $this->form->addFields( [$stage_order] );
        
        // define the form action
        $this->form->addAction(_t('Save'), new TAction(array($this, 'onSave')), 'fa:save green');
        
        $this->setAfterSaveAction( new TAction( ['KanbanDatabaseView', 'onLoad'] ) );
        $this->setUseMessages(FALSE);
        
        TScript::create('$("body").trigger("click")');
        TScript::create('$("[name=title]").focus()');
        
        parent::add($this->form);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
