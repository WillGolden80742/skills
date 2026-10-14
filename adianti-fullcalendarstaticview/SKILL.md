---
name: adianti-fullcalendarstaticview
description: Calendar — Tutor Presentation > Utilities > Calendar
triggers: ["FullCalendarStaticView", "Calendar", "Tutor", "Presentation", "Utilities"]
---

# Skill Adianti — Calendar — Tutor Presentation > Utilities > Calendar

Classe Tutor: `FullCalendarStaticView`.
Ver no Tutor: `index.php?class=FullCalendarStaticView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Widgets/FullCalendarStaticView.class.php`.


## Código

```php
<?php
/**
 * FullCalendarStaticView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FullCalendarStaticView extends TPage
{
    private $fc;
    
    /**
     * Page constructor
     */
    public function __construct()
    {
        parent::__construct();
        $this->fc = new TFullCalendar(date('Y-m-d'), 'month');
        $this->fc->setTimeRange( '06:00:00', '20:00:00' );
        $this->fc->enableFullHeight();
        $this->fc->enablePopover( 'Title {title}', '<b>{title}</b> <br> <i class="fa fa-user" aria-hidden="true"></i> {person} <br> {description}');
        
        $today = date("Y-m-d");// current date
        $before_yesterday = (new DateTime(date('Y-m-d')))->sub(new DateInterval("P2D"))->format('Y-m-d');
        $yesterday        = (new DateTime(date('Y-m-d')))->sub(new DateInterval("P1D"))->format('Y-m-d');
        $tomorrow         = (new DateTime(date('Y-m-d')))->add(new DateInterval("P1D"))->format('Y-m-d');
        $after_tomorrow   = (new DateTime(date('Y-m-d')))->add(new DateInterval("P2D"))->format('Y-m-d');
        
        $obj1  = (object) ['title'=>'Event 1',  'person' => 'Mary', 'description' => 'Complementary description'];
        $obj2  = (object) ['title'=>'Event 2',  'person' => 'Joan', 'description' => 'Complementary description'];
        $obj3  = (object) ['title'=>'Event 3',  'person' => 'Pete', 'description' => 'Complementary description'];
        $obj4  = (object) ['title'=>'Event 4',  'person' => 'Paul', 'description' => 'Complementary description'];
        $obj5  = (object) ['title'=>'Event 5',  'person' => 'Mary', 'description' => 'Complementary description'];
        $obj6  = (object) ['title'=>'Event 6',  'person' => 'Joan', 'description' => 'Complementary description'];
        $obj7  = (object) ['title'=>'Event 7',  'person' => 'Pete', 'description' => 'Complementary description'];
        $obj8  = (object) ['title'=>'Event 8',  'person' => 'Paul', 'description' => 'Complementary description'];
        $obj9  = (object) ['title'=>'Event 9',  'person' => 'Mary', 'description' => 'Complementary description'];
        $obj10 = (object) ['title'=>'Event 10', 'person' => 'Joan', 'description' => 'Complementary description'];
        
        $this->fc->addEvent(1, 'Event 1', $before_yesterday.'T08:30:00', $before_yesterday.'T12:30:00', null, '#C04747', $obj1);
        $this->fc->addEvent(2, 'Event 2', $before_yesterday.'T14:30:00', $before_yesterday.'T18:30:00', null, '#668BC6', $obj2);
        $this->fc->addEvent(3, 'Event 3', $yesterday.'T08:30:00', $yesterday.'T12:30:00', null, '#C04747', $obj3);
        $this->fc->addEvent(4, 'Event 4', $yesterday.'T14:30:00', $yesterday.'T18:30:00', null, '#668BC6', $obj4);
        $this->fc->addEvent(5, 'Event 5', $today.'T08:30:00', $today.'T12:30:00', null, '#FF0000', $obj5);
        $this->fc->addEvent(6, 'Event 6', $today.'T14:30:00', $today.'T18:30:00', null, '#5AB34B', $obj6);
        $this->fc->addEvent(7, 'Event 7', $tomorrow.'T08:30:00', $tomorrow.'T12:30:00', null, '#FF0000', $obj7);
        $this->fc->addEvent(8, 'Event 8', $tomorrow.'T14:30:00', $tomorrow.'T18:30:00', null, '#5AB34B', $obj8);
        $this->fc->addEvent(9, 'Event 9', $after_tomorrow.'T08:30:00', $after_tomorrow.'T12:30:00', null, '#FF0000', $obj9);
        $this->fc->addEvent(10, 'Event 10', $after_tomorrow.'T14:30:00', $after_tomorrow.'T18:30:00', null, '#FF8C05', $obj10);
        
        $this->fc->setDayClickAction(new TAction(array($this, 'onDayClick')));
        $this->fc->setEventClickAction(new TAction(array($this, 'onEventClick')));
        
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add(TPanelGroup::pack('', $this->fc));

        parent::add($vbox);
    }
    
    public static function onDayClick($param)
    {
        $date = $param['date'];
        new TMessage('info', "You clicked at date: {$date}");
    }
    
    public static function onEventClick($param)
    {
        $id = $param['id'];
        new TMessage('info', "You clicked at id: {$id}");
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
