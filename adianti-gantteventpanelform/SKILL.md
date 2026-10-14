---
name: adianti-gantteventpanelform
description: GanttEventPanelForm — Tutor Organization > Utilities
triggers: ["GanttEventPanelForm", "Tutor", "Organization", "Utilities"]
---

# Skill Adianti — GanttEventPanelForm — Tutor Organization > Utilities

Classe Tutor: `GanttEventPanelForm`.
Ver no Tutor: `index.php?class=GanttEventPanelForm` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/Utilities/GanttEventPanelForm.class.php`.


## Código

```php
<?php
/**
 * GanttEventPanelForm
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class GanttEventPanelForm extends TPage
{
    protected $form; // form
    
    /**
     * Class constructor
     * Creates the page and the registration form
     */
    public function __construct()
    {
        parent::__construct();
        
        parent::setTargetContainer('adianti_right_panel');
        
        // creates the form
        $this->form = new BootstrapFormBuilder('form_event');
        $this->form->setFormTitle('Event');
        $this->form->setProperty('style', 'margin-bottom:0;box-shadow:none');
        
        // create the form fields
        $id             = new TEntry('id');
        $color          = new TColor('color');
        $start_time     = new TDateTime('start_time');
        $end_time       = new TDateTime('end_time');
        $title          = new TEntry('title');
        $description    = new TText('description');
        $group_id       = new TDBUniqueSearch('group_id', 'samples', 'GanttGroup', 'id', 'name');
        $percent        = new TSpinner('percent');
        
        // define the sizes
        $id->setSize(40);
        $id->setEditable(FALSE);
        $color->setSize(120);
        $start_time->setSize(200);
        $end_time->setSize(200);
        $title->setSize('100%');
        $description->setSize('100%', 50);
        $group_id->setSize('100%');
        $color->setValue('#3a87ad');
        $percent->setRange(1,100,1);
        $group_id->setMinLength(0);
        
        // add one row for each form field
        $this->form->addFields( [new TLabel('ID:', null, null, 'b')]);
        $this->form->addFields( [$id] );
        $this->form->addFields( [new TLabel('Color:', null, null, 'b')] );
        $this->form->addFields( [$color] );
        $this->form->addFields( [new TLabel('Start time:', null, null, 'b')]);
        $this->form->addFields( [$start_time] );
        $this->form->addFields( [new TLabel('End time:', null, null, 'b')]);
        $this->form->addFields( [$end_time] );
        $this->form->addFields( [new TLabel('Title:', null, null, 'b')]);
        $this->form->addFields( [$title] );
        $this->form->addFields( [new TLabel('Description:', null, null, 'b')]);
        $this->form->addFields( [$description] );
        $this->form->addFields( [new TLabel('Percent:', null, null, 'b')]);
        $this->form->addFields( [$percent] );
        $this->form->addFields( [new TLabel('Group:', null, null, 'b')]);
        $this->form->addFields( [$group_id] );
        
        $this->form->addAction( _t('Save'),   new TAction(array($this, 'onSave')),   'fa:save green');
        $this->form->addAction( _t('Clear'),  new TAction(array($this, 'onEdit')),   'fa:eraser orange');
        $this->form->addAction( _t('Delete'), new TAction(array($this, 'onDelete')), 'far:trash-alt red');
        $this->form->addHeaderActionLink( _t('Close'), new TAction(array($this, 'onClose')), 'fa:times red');
        
        parent::add($this->form);
    }
    
    /**
     * Fill form from the user selected time
     */
    public function onStartEdit($param)
    {
        $this->form->clear();
        $data = new stdClass;
        $data->color = '#3a87ad';
        
        if ($param['start_time'])
        {
            $data->start_time = $param['start_time'];
            
        }
        
        if ($param['group_id'])
        {
            $data->group_id = $param['group_id'];
        }
        
        $this->form->setData( $data );
    }
    
    /**
     * Close curtain
     */
    public static function onClose($param)
    {
        TScript::create("Template.closeRightPanel()");
    }
    
    /**
     * method onEdit()
     * Executed whenever the user clicks at the edit button da datagrid
     */
    public function onEdit($param)
    {
        try
        {
            if (isset($param['key']))
            {
                // get the parameter $key
                $key = $param['key'];
                
                // open a transaction with database 'samples'
                TTransaction::open('samples');
                
                // instantiates object GanttEvent
                $object = new GanttEvent($key);
                
                // fill the form with the active record data
                $this->form->setData($object);
                
                // close the transaction
                TTransaction::close();
            }
            else
            {
                $this->form->clear();
            }
        }
        catch (Exception $e) // in case of exception
        {
            // shows the exception error message
            new TMessage('error', $e->getMessage());
            
            // undo all pending operations
            TTransaction::rollback();
        }
    }
    
    /**
     * Save the gantt event
     */
    public static function onSave($param)
    {
        try
        {
            // open a transaction with database 'samples'
            TTransaction::open('samples');
            
            $object = new GanttEvent;
            $object->fromArray($param);
            $object->store(); // stores the object
            
            TTransaction::close(); // close the transaction
            
            TScript::create("Template.closeRightPanel()");
            
            $posAction = new TAction(array('GanttDatabaseView', 'onReload'));
            $posAction->setParameter('target_container', 'adianti_div_content');
            //$posAction->setParameter('date', $data->start_date);
            
            // shows the success message
            new TMessage('info', TAdiantiCoreTranslator::translate('Record saved'), $posAction);
        }
        catch (Exception $e) // in case of exception
        {
            // shows the exception error message
            new TMessage('error', $e->getMessage());
            
            // undo all pending operations
            TTransaction::rollback();
        }
    }
    
    /**
     * Delete event
     */
    public static function onDelete($param)
    {
        // define the delete action
        $action = new TAction(array('GanttEventPanelForm', 'Delete'));
        $action->setParameters($param); // pass the key parameter ahead
        
        // shows a dialog to the user
        new TQuestion(AdiantiCoreTranslator::translate('Do you really want to delete ?'), $action);
    }
    
    /**
     * Delete a record
     */
    public static function Delete($param)
    {
        try
        {
            // get the parameter $key
            $key = $param['id'];
            // open a transaction with database
            TTransaction::open('samples');
            
            // instantiates object
            $object = new GanttEvent($key, FALSE);
            
            // deletes the object from the database
            $object->delete();
            
            // close the transaction
            TTransaction::close();
            
            TScript::create("Template.closeRightPanel()");
            
            $posAction = new TAction(array('GanttDatabaseView', 'onReload'));
            $posAction->setParameter('target_container', 'adianti_div_content');
            //$posAction->setParameter('date', $param['start_date']);
            
            // shows the success message
            new TMessage('info', TAdiantiCoreTranslator::translate('Record deleted'), $posAction);
        }
        catch (Exception $e) // in case of exception
        {
            // shows the exception error message
            new TMessage('error', $e->getMessage());
            // undo all pending operations
            TTransaction::rollback();
        }
    }
    
    
    /**
     * Update event. Result of the drag and drop or resize.
     */
    public static function onUpdateEvent($param)
    {
        try
        {
            if (isset($param['id']))
            {
                // get the parameter $key
                $key=$param['id'];
                
                // open a transaction with database 'samples'
                TTransaction::open('samples');
                
                // instantiates object GanttEvent
                $object = new GanttEvent($key);
                $object->start_time = $param['start_time'];
                $object->end_time   = $param['end_time'];
                $object->store();
                                
                // close the transaction
                TTransaction::close();
            }
        }
        catch (Exception $e) // in case of exception
        {
            new TMessage('error', $e->getMessage());
            TTransaction::rollback();
        }
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
