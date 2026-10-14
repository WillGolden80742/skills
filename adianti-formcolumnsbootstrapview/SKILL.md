---
name: adianti-formcolumnsbootstrapview
description: FormColumnsBootstrapView — Tutor Presentation > Forms
triggers: ["FormColumnsBootstrapView", "Tutor", "Presentation", "Forms", "FormColumnsBootstrap"]
---

# Skill Adianti — FormColumnsBootstrapView — Tutor Presentation > Forms

Classe Tutor: `FormColumnsBootstrapView`.
Ver no Tutor: `index.php?class=FormColumnsBootstrapView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormColumnsBootstrapView.class.php`.


## Código

```php
<?php
/**
 * FormColumnsBootstrapView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormColumnsBootstrapView extends TPage
{
    private $form;
    private $alertBox;
    
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        // create the form
        $this->form = new BootstrapFormWrapper( new TQuickForm );
        $this->form->setClientValidation(true);
        
        // create the form fields
        $id          = new TEntry('id');
        $description = new TEntry('description');
        $date       = new TDate('date');
        $color       = new TColor('color');
        $list        = new TCombo('list');
        
        $combo_items = array();
        $combo_items['a'] ='Item a';
        $combo_items['b'] ='Item b';
        $combo_items['c'] ='Item c';
        
        $list->addItems($combo_items);
        
        // define how many columns
        $this->form->setFieldsByRow(2);
        
        // add the fields inside the form
        $this->form->addQuickField('Id',    $id,    40);
        $this->form->addQuickField('Description', $description, 180);
        $this->form->addQuickField('Date', $date, 100);
        $this->form->addQuickField('Color', $color, 100);
        $this->form->addQuickField('List', $list, 120);
        
        $description->addValidation('Description', new TRequiredValidator);
        
        // define the form action
        $btn = $this->form->addQuickAction('Send', new TAction(array($this, 'onSend')), 'far:check-circle');
        $btn->class = 'btn btn-success';
        
        $panel = new TPanelGroup('Bootstrap Column Form');
        $panel->add($this->form);
        
        $this->alertBox = new TElement('div');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        // $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->alertBox);
        $vbox->add($panel);

        parent::add($vbox);
    }
    
    /**
     * Send data
     */
    public function onSend($param)
    {
        $data = $this->form->getData(); // optional parameter: active record class
        
        // put the data back to the form
        $this->form->setData($data);
        
        // creates a string with the form element's values
        $message = 'Id: '           . $data->id . '<br>';
        $message.= 'Description : ' . $data->description . '<br>';
        $message.= 'Date1: '        . $data->date . '<br>';
        $message.= 'Color : '       . $data->color . '<br>';
        $message.= 'List : '        . $data->list . '<br>';
        
        // show the message
        new TMessage('info', $message);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
