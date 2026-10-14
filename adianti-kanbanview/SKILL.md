---
name: adianti-kanbanview
description: Kanban — Tutor Presentation > Utilities > Kanban
triggers: ["KanbanView", "Kanban", "Tutor", "Presentation", "Utilities"]
---

# Skill Adianti — Kanban — Tutor Presentation > Utilities > Kanban

Classe Tutor: `KanbanView`.
Ver no Tutor: `index.php?class=KanbanView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Widgets/KanbanView.class.php`.


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
 * @license    https://adiantiframework.com.br/license-tutor
 */
class KanbanView extends TPage
{
	private $form;
	
	public function __construct()
	{
		parent::__construct();
		
		$kanban = new TKanban;
		$kanban->setStageHeight('80vh');
		
		$stages = [];
		$stages[] = [ 'id' => 1, 'title' => 'stage 1', 'color' => '#fcfcfd'];
		$stages[] = [ 'id' => 2, 'title' => 'stage 2', 'color' => '#eff6fe'];
		$stages[] = [ 'id' => 3, 'title' => 'stage 3', 'color' => '#fff8e0'];
		$stages[] = [ 'id' => 4, 'title' => 'stage 4', 'color' => '#e7f4ee'];
		
		foreach ($stages as $stage)
		{
		    $kanban->addStage($stage['id'], $stage['title'], null, $stage['color']);
		}
		
		$items = [];
		$items[] = [ 'id' => 101, 'stage_id' => 1, 'title' => 'item 1.1', 'content' => 'item 1.1 content', 'color' => '#FF1818'];
		$items[] = [ 'id' => 102, 'stage_id' => 1, 'title' => 'item 1.2', 'content' => 'item 1.2 content', 'color' => '#57D557'];
		$items[] = [ 'id' => 201, 'stage_id' => 2, 'title' => 'item 2.1', 'content' => 'item 2.1 content', 'color' => '#5950F1'];
		$items[] = [ 'id' => 202, 'stage_id' => 2, 'title' => 'item 2.2', 'content' => 'item 2.2 content', 'color' => '#57D557'];
		$items[] = [ 'id' => 301, 'stage_id' => 3, 'title' => 'item 3.1', 'content' => 'item 3.1 content', 'color' => '#CC2EC9'];
		$items[] = [ 'id' => 302, 'stage_id' => 3, 'title' => 'item 3.2', 'content' => 'item 3.2 content', 'color' => '#5950F1'];
		
		foreach ($items as $key => $item)
		{
			$kanban->addItem($item['id'], $item['stage_id'], $item['title'], $item['content'], $item['color']);
		}
		
		//$kanban->setItemTemplate('<b>Content</b>: {content}');
		$kanban->addStageAction('Action 1', new TAction([$this, 'onEditStage']),   'far:edit blue fa-fw');
		$kanban->addStageAction('Action 2', new TAction([$this, 'onDeleteStage']), 'far:trash-alt red fa-fw');
		
		$kanban->addItemAction('Edit',   new TAction([$this, 'onItemEdit']),   'far:edit blue');
		$kanban->addItemAction('Delete', new TAction([$this, 'onItemDelete']), 'far:trash-alt red');
		
		$kanban->setItemDropAction(new TAction([$this, 'onUpdateItemDrop']));
		$kanban->setStageDropAction(new TAction([$this, 'onUpdateStageDrop']));
		
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($kanban);

        parent::add($vbox);
        
        $style = new TStyle('content');
        $style->background = 'white';
        $style->show();
	}
	
    /**
     * Update stage on drop
     */
	public static function onUpdateStageDrop($param)
	{
		new TMessage('info', '<b>onUpdateStageDrop</b><br>' . str_replace('","', '",<br>&nbsp;"', json_encode($param)));
	}
	
    /**
     * Update item on drop
     */
	public static function onUpdateItemDrop($param)
	{
		new TMessage('info', '<b>onUpdateItemDrop</b><br>' . str_replace('","', '",<br>&nbsp;"', json_encode($param)));
	}
	
    /**
     * Stage edit action
     */
	public static function onEditStage($param = NULL)
	{
		new TMessage('info', '<b>onEditStage</b><br>' . str_replace('","', '",<br>&nbsp;"', json_encode($param)));
	}
	
    /**
     * Stage delete action
     */
	public static function onDeleteStage($param = NULL)
	{
		new TMessage('info', '<b>onDeleteStage</b><br>' . str_replace('","', '",<br>&nbsp;"', json_encode($param)));
	}
	
    /**
     * Item edit action
     */
	public static function onItemEdit($param = NULL)
	{
		new TMessage('info', '<b>onItemEdit</b><br>' . str_replace('","', '",<br>&nbsp;"', json_encode($param)));
	}
	
    /**
     * Item delete action
     */
	public static function onItemDelete($param = NULL)
	{
		new TMessage('info', '<b>onItemDelete</b><br>' . str_replace('","', '",<br>&nbsp;"', json_encode($param)));
	}
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
