---
name: adianti-kanbandatabaseview
description: Kanban — Tutor Organization > Utilities > Kanban
triggers: ["KanbanDatabaseView", "Kanban", "Tutor", "Organization", "Utilities"]
---

# Skill Adianti — Kanban — Tutor Organization > Utilities > Kanban

Classe Tutor: `KanbanDatabaseView`.
Ver no Tutor: `index.php?class=KanbanDatabaseView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/Utilities/KanbanDatabaseView.class.php`.


## Código

```php
<?php
/**
 * KanbanView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Artur Comunello
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    http://www.adianti.com.br/framework-license
 */
class KanbanDatabaseView extends TPage
{
	private $form;
	
	public function __construct()
	{
		parent::__construct();
		
		TTransaction::open('samples');
		$stages = KanbanStage::orderBy('stage_order')->load();
		$items  = KanbanItem::orderBy('item_order')->load();
		TTransaction::close();
		
		$kanban = new TKanban;
		//$kanban->enableTopScrollbar();
		$kanban->setStageHeight('80vh');
		
		foreach ($stages as $key => $stage)
		{
			$kanban->addStage($stage->id, $stage->title, $stage);
		}
		
		foreach ($items as $key => $item)
		{
			$kanban->addItem($item->id, $item->stage_id, $item->title, $item->content, $item->color, $item);
		}
		
		
		$kanban->addStageAction('Edit', new TAction(['KanbanStageForm', 'onEdit']),   'far:edit blue fa-fw');
		$kanban->addStageAction('Add', new TAction(['KanbanItemForm', 'onStartEdit'], ['register_state' => 'false']),   'fa:plus green fa-fw');
		$kanban->addStageShortcut('Add', new TAction(['KanbanItemForm', 'onStartEdit'], ['register_state' => 'false']),   'fa:plus fa-fw');
		
		$kanban->addItemAction('Edit', new TAction(['KanbanItemForm', 'onEdit'], ['register_state' => 'false']), 'far:edit blue');
		$kanban->addItemAction('Delete', new TAction([$this, 'onDelete']), 'far:trash-alt red');
		
        //$kanban->setTemplatePath('app/resources/card.html');
		$kanban->setItemDropAction(new TAction([__CLASS__, 'onUpdateItemDrop']));
		$kanban->setStageDropAction(new TAction([__CLASS__, 'onUpdateStageDrop']));
		
		parent::add($kanban);
	}
	
	public function onLoad($param)
	{
	
	}
	
    /**
     * Update stage on drop
     */
	public static function onUpdateStageDrop($param)
	{
		if (empty($param['order']))
		{
			return;
		}
		
		try
		{
    		TTransaction::open('samples');
    		
    		foreach ($param['order'] as $key => $id)
    		{
    			$sequence = ++ $key;
    
    			$stage = new KanbanStage($id);
    			$stage->stage_order = $sequence;
    
    			$stage->store();
    		}
    		
    		TTransaction::close();
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
        }
	}
	
    /**
     * Update item on drop
     */
	public static function onUpdateItemDrop($param)
	{
		if (empty($param['order']))
		{
			return;
		}

        try
        {
    		TTransaction::open('samples');
    
    		foreach ($param['order'] as $key => $id)
    		{
    			$sequence = ++$key;
    
    			$item = new KanbanItem($id);
    			$item->item_order = $sequence;
    			$item->stage_id = $param['stage_id'];
    			$item->store();
    		}
    		
    		TTransaction::close();
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
        }
	}
	
	/**
	 *
	 */
	public static function onDelete($param)
	{
        // define the delete action
        $action = new TAction(array(__CLASS__, 'Delete'));
        $action->setParameters($param); // pass the key parameter ahead
        
        // shows a dialog to the user
        new TQuestion(AdiantiCoreTranslator::translate('Do you really want to delete ?'), $action);
	}
	
    /**
     * method Delete()
     * Delete a record
     */
    public static function Delete($param)
    {
        try
        {
            // instantiates object and delete
            TTransaction::open('samples');
            $object = new KanbanItem( $param['key'] );
            $object->delete();
            TTransaction::close();
            
            AdiantiCoreApplication::loadPage(__CLASS__, 'onLoad');
        }
        catch (Exception $e) // in case of exception
        {
            new TMessage('error', $e->getMessage());
            TTransaction::rollback();
        }
    }
    
    /**
     * Item click
     */
	public static function onItemClick($param = NULL)
	{
		new TMessage('info', str_replace(',', '<br>', json_encode($param)));
	}
	
    /**
     * Display condition
     */
	public static function teste($param = NULL)
	{
		return TRUE;
	}
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
