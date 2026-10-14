---
name: adianti-formfieldlisteventsview
description: Field list events — Tutor Presentation > Extras > Field list events
triggers: ["FormFieldListEventsView", "Field", "list", "events", "Tutor", "Presentation", "Extras", "Field list events"]
---

# Skill Adianti — Field list events — Tutor Presentation > Extras > Field list events

Classe Tutor: `FormFieldListEventsView`.
Ver no Tutor: `index.php?class=FormFieldListEventsView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extras/FormFieldListEventsView.class.php`.


## Código

```php
<?php
/**
 * FormFieldListEventsView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormFieldListEventsView extends TPage
{
    private $form;
    private $fieldlist;
    
    /**
     * Constructor
     */
    public function __construct()
    {
        parent::__construct();
        
        // create form and table container
        $this->form = new BootstrapFormBuilder('my_form');
        $this->form->setFormTitle(_t('Form field list'));
        
        $uniq = new THidden('uniq[]');
        
        $combo = new TCombo('combo[]');
        $combo->enableSearch();
        $combo->addItems(['1'=>'<b>One</b>','2'=>'<b>Two</b>','3'=>'<b>Three</b>','4'=>'<b>Four</b>','5'=>'<b>Five</b>']);
        $combo->setSize('100%');
        
        $text = new TEntry('text[]');
        $text->setSize('100%');
        
        $number = new TEntry('number[]');
        $number->setNumericMask(2,',','.', true);
        $number->setSize('100%');
        $number->style = 'text-align: right';
        
        $date = new TDate('date[]');
        $date->setSize('100%');
        
        $this->fieldlist = new TFieldList;
        $this->fieldlist->generateAria();
        $this->fieldlist->width = '100%';
        $this->fieldlist->name  = 'my_field_list';
        $this->fieldlist->addField( '<b>Unniq</b>',  $uniq,   ['width' => '0%', 'uniqid' => true] );
        $this->fieldlist->addField( '<b>Combo</b>',  $combo,  ['width' => '25%'] );
        $this->fieldlist->addField( '<b>Text</b>',   $text,   ['width' => '25%'] );
        $this->fieldlist->addField( '<b>Number</b>', $number, ['width' => '25%', 'sum' => true] );
        $this->fieldlist->addField( '<b>Date</b>',   $date,   ['width' => '25%'] );
        
        $this->fieldlist->setTotalUpdateAction(new TAction([$this, 'onTotalUpdate']));
        
        $this->fieldlist->enableSorting();
        
        $this->form->addField($combo);
        $this->form->addField($text);
        $this->form->addField($number);
        $this->form->addField($date);
        
        $text->addValidation( 'text', new TRequiredListValidator );
        
        $this->fieldlist->addButtonFunction("__adianti_message('Row data', JSON.stringify(tfieldlist_get_row_data(this)))", 'fa:info-circle blue', 'Show "Text" field');
        
        $this->fieldlist->addButtonAction(new TAction([$this, 'showRow']), 'fa:info-circle purple', 'Show text');
        //$this->fieldlist->disableRemoveButton();
        $this->fieldlist->setRemoveAction( new TAction([$this, 'actionX']));
        
        
        $this->fieldlist->addHeader();
        $this->fieldlist->addDetail( new stdClass );
        $this->fieldlist->addDetail( new stdClass );
        $this->fieldlist->addDetail( new stdClass );
        $this->fieldlist->addDetail( new stdClass );
        $this->fieldlist->addDetail( new stdClass );
        //$this->fieldlist->addCloneAction();
        $this->fieldlist->addCloneAction( new TAction([$this, 'actionX'] ));
        
        // add field list to the form
        $this->form->addContent( [$this->fieldlist] );
        
        // form actions
        $this->form->addAction( 'Save', new TAction([$this, 'onSave'], [ 'static' => '1']), 'fa:save blue');
        $this->form->addAction( 'Clear', new TAction([$this, 'onClear']), 'fa:eraser red');
        $this->form->addAction( 'Fill', new TAction([$this, 'onFill']), 'fas:pencil-alt green');
        $this->form->addAction( 'Clear/Fill', new TAction([$this, 'onClearFill']), 'fas:pencil-alt orange');
        $this->form->addAction( 'Disable', new TAction([$this, 'onDisable']), 'fas:toggle-off orange');
        $this->form->addAction( 'Enable', new TAction([$this, 'onEnable']), 'fas:toggle-on orange');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);
        
        parent::add($vbox);
    }
    
    /**
     * Enable field list
     */
    public static function onEnable($param)
    {
        // name $this->fieldlist->name
        TFieldList::enableField('my_field_list');
    }
    
    /**
     * Disable field list
     */
    public static function onDisable($param)
    {
        // name $this->fieldlist->name
        TFieldList::disableField('my_field_list');
    }
    
    public static function actionX($param)
    {
        $win = TWindow::create('test', 0.6, 0.8);
        $win->add( '<pre>'.str_replace("\n", '<br>', print_r($param, true) ).'</pre>'  );
        $win->show();
    }
    
    /**
     * Show row
     */
    public static function showRow($param)
    {
        new TMessage('info', str_replace('","', '",<br>&nbsp;"', json_encode($param)));
    }
    
    /**
     * Clear form
     */
    public static function onClear($param)
    {
        TFieldList::clear('my_field_list');
        TFieldList::addRows('my_field_list', 4);
    }
    
    /**
     * Fill data
     */
    public static function onFill($param)
    {
        $data = new stdClass;
        $data->combo  = [ 1,2,3,4,5 ];
        $data->text   = [ 'Part. One', 'Part. Two', 'Part. Three', 'Part. Four', 'Part. Five' ];
        $data->number = [ '10,10','20,20', '30,30', '40,40', '50,50' ];
        $data->date   = [ date('Y-m-d'),
                          date('Y-m-d', strtotime("+1 days")),
                          date('Y-m-d', strtotime("+2 days")),
                          date('Y-m-d', strtotime("+3 days")),
                          date('Y-m-d', strtotime("+4 days")) ];
        TForm::sendData('my_form', $data);
    }
    
    /**
     * Fill data
     */
    public static function onClearFill($param)
    {
    
        TFieldList::clear('my_field_list');
        TFieldList::addRows('my_field_list', 4);
        
        $data = new stdClass;
        $data->combo  = [ 1,2,3,4,5 ];
        $data->text   = [ 'Part. One', 'Part. Two', 'Part. Three', 'Part. Four', 'Part. Five' ];
        $data->number = [ '10,10','20,20', '30,30', '40,40', '50,50' ];
        $data->date   = [ date('Y-m-d'),
                          date('Y-m-d', strtotime("+1 days")),
                          date('Y-m-d', strtotime("+2 days")),
                          date('Y-m-d', strtotime("+3 days")),
                          date('Y-m-d', strtotime("+4 days")) ];
        
        TForm::sendData('my_form', $data, false, true, 200); // 200 ms of timeout after recreate rows!
    }
    
    /**
     * on Update Total event
     */
    public static function onTotalUpdate($param)
    {
        // echo '<pre>';
        // var_dump($param);
        // echo '</pre>';
        
        $grandtotal = 0;
        
        if ($param['list_data'])
        {
            foreach ($param['list_data'] as $row)
            {
                $grandtotal += floatval( str_replace(['.', ','], ['', '.'], $row['number']));
            }
        }        
        
        TToast::show('info', '<b>Total</b>: '.number_format($grandtotal,2,',','.'), 'bottom right');
    }
    
    /**
     * Save simulation
     */
    public function onSave($param)
    {
        try
        {
            $data = $this->fieldlist->getPostData();
            $this->form->validate();
            // show form values inside a window
            $win = TWindow::create('test', 0.6, 0.8);
            $win->add( '<pre>'.str_replace("\n", '<br>', print_r($data, true) ).'</pre>'  );
            $win->show();
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
        }
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
