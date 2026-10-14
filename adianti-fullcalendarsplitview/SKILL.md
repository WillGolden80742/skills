---
name: adianti-fullcalendarsplitview
description: Calendar Split View — Tutor Organization > Utilities > Calendar Split View
triggers: ["FullCalendarSplitView", "Calendar", "Split", "View", "Tutor", "Organization", "Utilities", "Calendar Split View"]
---

# Skill Adianti — Calendar Split View — Tutor Organization > Utilities > Calendar Split View

Classe Tutor: `FullCalendarSplitView`.
Ver no Tutor: `index.php?class=FullCalendarSplitView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/Utilities/FullCalendarSplitView.class.php`.


## Código

```php
<?php
/**
 * FullCalendarDatabaseView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FullCalendarSplitView extends TPage
{
    private $fc;
    
    /**
     * Page constructor
     */
    public function __construct()
    {
        parent::__construct();
        
        $options = ['register_state' => 'false'];
        
        $this->fc = new TFullCalendar(date('Y-m-d'), 'month');
        $this->fc->setReloadAction(new TAction(array($this, 'getEvents')));
        $this->fc->setDayClickAction(new TAction(array('CalendarEventPanelForm', 'onStartEdit'), $options));
        $this->fc->setEventClickAction(new TAction(array('CalendarEventPanelForm', 'onEdit'), $options));
        $this->fc->setEventUpdateAction(new TAction(array('CalendarEventPanelForm', 'onUpdateEvent'), $options));
        $this->fc->enableFullHeight();
        
        $this->fc->setOption('businessHours', [ [ 'dow' => [ 1, 2, 3, 4, 5 ], 'start' => '08:00', 'end' => '18:00' ]]);
        //$this->fc->setTimeRange('10:00', '18:00');
        //$this->fc->disableDragging();
        //$this->fc->disableResizing();
        parent::add( TPanelGroup::pack('', $this->fc) );
    }
    
    /**
     * Output events as an json
     */
    public static function getEvents($param=NULL)
    {
        $return = array();
        try
        {
            TTransaction::open('samples');
            
            $events = CalendarEvent::where('start_time', '>=', $param['start'])
                                   ->where('end_time',   '<=', $param['end'])->load();
            if ($events)
            {
                foreach ($events as $event)
                {
                    $event_array = $event->toArray();
                    $event_array['start'] = str_replace( ' ', 'T', $event_array['start_time']);
                    $event_array['end']   = str_replace( ' ', 'T', $event_array['end_time']);
                    
                    $popover_content = $event->render("<b>Title</b>: {title} <br> <b>Description</b>: {description}");
                    $event_array['title'] = TFullCalendar::renderPopover($event_array['title'], 'Popover title', $popover_content);
                    
                    $return[] = $event_array;
                }
            }
            TTransaction::close();
            echo json_encode($return);
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
        }
    }
    
    /**
     * Reconfigure the callendar
     */
    public function onReload($param = null)
    {
        if (isset($param['view']))
        {
            $this->fc->setCurrentView($param['view']);
        }
        
        if (isset($param['date']))
        {
            $this->fc->setCurrentDate($param['date']);
        }
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
