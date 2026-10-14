---
name: adianti-kanbanitemform
description: KanbanItemForm — Tutor Organization > Utilities
triggers: ["KanbanItemForm", "Tutor", "Organization", "Utilities"]
---

# Skill Adianti — KanbanItemForm — Tutor Organization > Utilities

Classe Tutor: `KanbanItemForm`.
Ver no Tutor: `index.php?class=KanbanItemForm` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/Utilities/KanbanItemForm.class.php`.


## Código

```php
<?php
/**
 * KanbanItemForm
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class KanbanItemForm extends TPage
{
    protected $form; // form
    
    // trait with onSave, onClear, onEdit
    use Adianti\Base\AdiantiStandardFormTrait;
    
    /**
     * Class constructor
     * Creates the page and the registration form
     */
    public function __construct()
    {
        parent::__construct();
        parent::setTargetContainer("adianti_right_panel");
        
        $this->setDatabase('samples');    // defines the database
        $this->setActiveRecord('KanbanItem');   // defines the active record
        
        // creates the form
        $this->form = new BootstrapFormBuilder('form_City');
        $this->form->setFormTitle('Kanban item');
        
        // create the form fields
        $id          = new THidden('id');
        $title       = new TEntry('title');
        $content     = new THtmlEditor('content');
        $color       = new TColor('color');
        $item_order  = new THidden('item_order');
        $stage_id    = new THidden('stage_id');
        $id->setEditable(FALSE);
        $title->setSize('100%');
        $color->setSize('100%');
        $content->setSize('100%', 250);
        
        // add the form fields
        $this->form->addFields( [$id] );
        $this->form->addFields( [new TLabel('Title',null,null, 'b')], [$title], [new TLabel('Color', null, null, 'b')], [$color] );
        $this->form->addFields( [$content] );
        $this->form->addFields( [$item_order] );
        $this->form->addFields( [$stage_id] );
        
        // define the form action
        $this->form->addAction(_t('Save'), new TAction(array($this, 'onSave')), 'fa:save green');
        $this->form->addHeaderActionLink( _t('Close'), new TAction([$this, 'onClose']), 'fa:times red');
        
        $this->setAfterSaveAction( new TAction( ['KanbanDatabaseView', 'onLoad'] ) );
        $this->setUseMessages(FALSE);
        
        TScript::create('$("body").trigger("click")');
        TScript::create('$("[name=title]").focus()');
        
        parent::add($this->form);
    }
    
    /**
     *
     */
    public function onStartEdit($param)
    {
        $data = new stdClass;
        $data->stage_id = $param['id'];
        $data->item_order = 999;
        $this->form->setData($data);
    }
    
    /**
     * Close side panel
     */
    public static function onClose($param)
    {
        TScript::create("Template.closeRightPanel()");
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
