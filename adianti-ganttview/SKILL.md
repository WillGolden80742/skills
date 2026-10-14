---
name: adianti-ganttview
description: Gantt — Tutor Presentation > Utilities > Gantt
triggers: ["GanttView", "Gantt", "Tutor", "Presentation", "Utilities"]
---

# Skill Adianti — Gantt — Tutor Presentation > Utilities > Gantt

Classe Tutor: `GanttView`.
Ver no Tutor: `index.php?class=GanttView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Widgets/GanttView.class.php`.


## Código

```php
<?php
/**
 * GanttView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class GanttView extends TPage
{
    private $gantt;
    private $loaded;
    
    /**
     * Constructor method
     */
    public function __construct($param)
    {
        parent::__construct();
        
        $this->gantt = new TGantt(TGantt::MODE_MONTHS_WITH_DAY, 'xs');
        $this->gantt->enableStripedMonths();
        $this->gantt->enableStripedRows();
        $this->gantt->setReloadAction(new TAction([$this, 'onReload']));
        $this->gantt->setStartDate( $param['start_time'] ?? date('Y-01-01') );
        $this->gantt->setEventClickAction(new TAction([$this, 'onAction']));
        $this->gantt->setDayClickAction(new TAction([$this, 'onAction']));
        
        if (!empty(TSession::getValue('gantt_view_mode')))
        {
            $this->gantt->setViewMode(TSession::getValue('gantt_view_mode'));
        }
        
        if (!empty(TSession::getValue('gantt_size_mode')))
        {
            $this->gantt->setSizeMode(TSession::getValue('gantt_size_mode'));
        }
        
        //$this->gantt->setSizeMode('lg');
        // $this->gantt->setTransformerTimeTitle(function($start, $end, $events){
        //     return 'adsd';
        // });
        
        $this->gantt->setTitle('Eventos');
        $this->gantt->enableFullHours();
        
        $button = $this->gantt->addHeaderAction(new TAction([$this, 'onAction']), 'Ação', new TImage('fa:rocket'));
        $button->{'class'} .= 'btn-success';

        $button = $this->gantt->addHeaderAction(new TAction([$this, 'onAction']), 'Ação 2', new TImage('fa:rocket'));
        $button->{'class'} .= 'btn-danger';

        $this->gantt->enableDragEvent( new TAction([$this, 'onAction'] ), 60  );
        
        $this->gantt->enableViewModeButton(true, true);
        $this->gantt->enableSizeModeButton(true, true);
        
        parent::add($this->gantt);
    }
    
    /**
     * Generic action to show parameters
     */
    public static function onAction($param)
    {
        new TMessage('info', str_replace('","', '",<br>&nbsp;"', json_encode($param)));
    }
    
    /**
     * Load/Reload Gantt Events
     */
    public function onReload($param=NULL)
    {
        if (! empty($param['start_time']))
        {
            $this->gantt->setStartDate($param['start_time']);
        }
        
        if (!empty($param['view_mode']))
        {
            TSession::setValue('gantt_view_mode', $param['view_mode']);
            $this->gantt->setViewMode($param['view_mode']);
        }
        
        if (!empty($param['size_mode']))
        {
            TSession::setValue('gantt_size_mode', $param['size_mode']);
            $this->gantt->setSizeMode($param['size_mode']);
        }
        
        try
        {
            $this->gantt->clearEvents();
            $this->gantt->addRow(1, 'Group 1');
            $this->gantt->addRow(2, 'Group 2');
            $this->gantt->addRow(3, 'Group 3');
            $this->gantt->addEvent(1, 1, 'Event A.1', date('Y-01-01 12:00:00'), date('Y-01-05 12:00:00'), '#C04747', 10);
            $this->gantt->addEvent(2, 1, 'Event A.2', date('Y-01-02 12:00:00'), date('Y-01-06 12:00:00'), '#668BC6', 20);
            $this->gantt->addEvent(3, 2, 'Event B.2', date('Y-01-03 12:00:00'), date('Y-01-07 12:00:00'), '#FF0000', 30);
            $this->gantt->addEvent(4, 2, 'Event B.2', date('Y-01-04 12:00:00'), date('Y-01-08 12:00:00'), '#5AB34B', 40);
            $this->gantt->addEvent(5, 3, 'Event C.2', date('Y-01-05 12:00:00'), date('Y-01-09 12:00:00'), '#668BC6', 50);
            $this->gantt->addEvent(6, 3, 'Event C.2', date('Y-01-06 12:00:00'), date('Y-01-10 12:00:00'), '#FF8C05', 60);
            
            $this->loaded = TRUE;
        }
        catch(Exception $e)
        {
            new TMessage('error', $e->getMessage());
        }
    }
    
    /**
     * Show Gantt
     */
    public function show()
    {
        // check if the gantt is already loaded
        if (!$this->loaded AND (!isset($_GET['method']) || $_GET['method'] !== 'onReload'))
        {
            $this->onReload( func_get_arg(0) );
        }

        parent::show();
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
