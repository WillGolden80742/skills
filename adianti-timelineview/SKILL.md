---
name: adianti-timelineview
description: Timeline — Tutor Presentation > Utilities > Timeline
triggers: ["TimelineView", "Timeline", "Tutor", "Presentation", "Utilities"]
---

# Skill Adianti — Timeline — Tutor Presentation > Utilities > Timeline

Classe Tutor: `TimelineView`.
Ver no Tutor: `index.php?class=TimelineView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Widgets/TimelineView.class.php`.


## Código

```php
<?php
/**
 * TimelineView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class TimelineView extends TPage
{
    public function __construct()
    {
        parent::__construct();
		
		$timeline = new TTimeline;
		
		$obj1 = (object) [ 'name' => 'AAA' ];
		$obj2 = (object) [ 'name' => 'BBB' ];
		$obj3 = (object) [ 'name' => 'CCC' ];
		$obj4 = (object) [ 'name' => 'DDD' ];
		$obj5 = (object) [ 'name' => 'EEE' ];
		
		$timeline->addItem(1, 'Event {id}',  'This is the event id: <b>{id}</b> name: <b>{name}</b>', '2017-12-11 12:01:00',  'fa:arrow-left bg-success',  'left',  $obj1 );
		$timeline->addItem(2, 'Event {id}',  'This is the event id: <b>{id}</b> name: <b>{name}</b>', '2017-12-11 12:02:00',  'fa:arrow-left bg-success',  'left',  $obj2 );
		$timeline->addItem(3, 'Event {id}',  'This is the event id: <b>{id}</b> name: <b>{name}</b>', '2017-12-13 12:03:00',  'fa:arrow-right bg-primary',  'right', $obj3 );
		$timeline->addItem(4, 'Event {id}',  'This is the event id: <b>{id}</b> name: <b>{name}</b>', '2017-12-14 12:04:00',  'fa:arrow-right bg-primary',  'right', $obj4 );
		
		$timeline->setUseBothSides();
		$timeline->setTimeDisplayMask('dd/mm/yyyy');
		$timeline->setFinalIcon( 'fa:flag-checkered bg-red' );
		
		$display_condition = function( $object = false ) {
			if( in_array($object->id, [2,3]))
			{
				return true;
			}
			return false;
		};
		
		$action1 = new TAction([$this, 'onAction1'], ['id' => '{id}', 'name' => '{name}']);
		$action2 = new TAction([$this, 'onAction2'], ['id' => '{id}', 'name' => '{name}']);
		
		$action1->setProperty('btn-class', 'btn btn-primary');
		$action2->setProperty('btn-class', 'btn btn-danger');
		
		$timeline->addAction($action1, 'Action 1', 'fa:bus', $display_condition );
		$timeline->addAction($action2, 'Action 2', 'fa:bus');
		
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($timeline);

        parent::add($vbox);
    }
    
    /**
     * Action 1
     */
    public static function onAction1($param)
    {
        new TMessage('info', 'Action1 on Event '. '<b>' . $param['id'] . '-' . $param['name'] . '</b>' );
    }
    
    /**
     * Action 2
     */
    public static function onAction2($param)
    {
        new TMessage('info', 'Action2 on Event '. '<b>' . $param['id'] . '-' . $param['name'] . '</b>' );
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
