---
name: adianti-calendarview
description: Simple calendar — Tutor Presentation > Utilities > Simple calendar
triggers: ["CalendarView", "Simple", "calendar", "Tutor", "Presentation", "Utilities", "Simple calendar"]
---

# Skill Adianti — Simple calendar — Tutor Presentation > Utilities > Simple calendar

Classe Tutor: `CalendarView`.
Ver no Tutor: `index.php?class=CalendarView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Widgets/CalendarView.class.php`.


## Código

```php
<?php
/**
 * CalendarView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class CalendarView extends TPage
{
    private $form;
    private $calendar;
    private $back_action;
    private $next_action;
    
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        // create the calendar
        $this->calendar = new TCalendar;
        $this->calendar->highlightWeekend();
        $this->calendar->setMonth(date('n'));
        $this->calendar->setYear(date('Y'));
        
        $this->calendar->selectDays(array( 8,9,10,11,12 ));
        $this->calendar->setSize(340,250);
        $this->calendar->setAction( new TAction(array($this, 'onSelect')) );
        
        // creates a simple form
        $this->form = new BootstrapFormBuilder('form_test');
        
        // creates the form fields
        $year  = new TEntry('year');
        $month = new TEntry('month');
        $day   = new TEntry('day');
        
        $year->setValue( $this->calendar->getYear() );
        $month->setValue( $this->calendar->getMonth() );
        
        $this->form->addFields([new TLabel('Year')],  [$year])->layout = ['col-sm-4','col-sm-8'];
        $this->form->addFields([new TLabel('Month')], [$month])->layout = ['col-sm-4','col-sm-8'];
        $this->form->addFields([new TLabel('Day')],   [$day])->layout = ['col-sm-4','col-sm-8'];
        
        $this->form->addAction('Back', new TAction(array($this, 'onBack')), 'far:arrow-alt-circle-left orange');
        $this->form->addAction('Next', new TAction(array($this, 'onNext')), 'far:arrow-alt-circle-right blue');
        
        // wrapper
        $hbox = new THBox;
        $hbox->add($this->calendar)->style .= ';vertical-align: top';
        $hbox->add($this->form);
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($hbox);

        parent::add($vbox);
    }
    
    /**
     * Next month
     */
    public function onNext($param)
    {
        $data = $this->form->getData();
        if (!empty($data->month) and !empty($data->year))
        {
            $data->month ++;
            if ($data->month ==13)
            {
                $data->month = 1;
                $data->year ++;
            }
            $this->form->setData( $data );
            $this->calendar->setMonth($data->month);
            $this->calendar->setYear($data->year);
        }
    }
    
    /**
     * Previous month
     */
    public function onBack($param)
    {
        $data = $this->form->getData();
        if (!empty($data->month) and !empty($data->year))
        {
            $data->month --;
            if ($data->month == 0)
            {
                $data->month = 12;
                $data->year --;
            }
            $this->form->setData( $data );
            $this->calendar->setMonth($data->month);
            $this->calendar->setYear($data->year);
        }
    }
    
    /**
     * Executed when the user clicks at a tree node
     * @param $param URL parameters containing key and value
     */
    public static function onSelect($param)
    {
        $obj = new StdClass;
        $obj->year  = $param['year'];
        $obj->month = $param['month'];
        $obj->day   = $param['day'];
        
        $date = $obj->year . '-' . $obj->month . '-' . $obj->day;
        
        // fill the form with this object attributes
        TForm::sendData('form_test', $obj);
        
        new TMessage('info', 'You have selected: '. $date );
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
