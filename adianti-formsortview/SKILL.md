---
name: adianti-formsortview
description: Sort List — Tutor Presentation > Forms > Sort List
triggers: ["FormSortView", "Sort", "List", "Tutor", "Presentation", "Forms", "Sort List"]
---

# Skill Adianti — Sort List — Tutor Presentation > Forms > Sort List

Classe Tutor: `FormSortView`.
Ver no Tutor: `index.php?class=FormSortView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormSortView.class.php`.


## Código

```php
<?php
/**
 * FormSortView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormSortView extends TPage
{
    private $form;
    
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        $this->form = new BootstrapFormBuilder('form_sort');
        $this->form->setFormTitle(_t('Sort List'));
        
        $list1 = new TSortList('list1');
        $list2 = new TSortList('list2');
        
        $list1->addItems( ['1' => 'One', '2' => 'Two', '3' => 'Three'] );
        $list2->addItems( ['a' => 'A', 'b' => 'B', 'c' => 'C'] );
        
        $list1->setSize(200, 200);
        $list2->setSize(200, 200);
        
        $list1->connectTo($list2);
        $list2->connectTo($list1);
        
        // connect the change method
        $list1->setChangeAction(new TAction(array($this, 'onChangeAction')));
        
        $this->form->addFields([$list1, $list2]);
        $this->form->addAction( 'Send', new TAction(array($this, 'onSend')), 'far:check-circle');
        $this->form->addAction( 'Reload', new TAction(array($this, 'onReload')), 'fa:sync');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);

        parent::add($vbox);
    }
    
    /**
     * Executed when a user change some item in list
     */
    public static function onChangeAction($param)
    {
        new TMessage('info', 'Change action<br>'.
                             'List1: ' . implode(',', isset($param['list1'])? $param['list1'] : []) . '<br>' .
                             'List2: ' . implode(',', isset($param['list2'])? $param['list2'] : []) );
    }
    
    /**
     * Reload items
     */
    public static function onReload($param)
    {
        $items = ['1' => 'One - reloaded', '2' => 'Two - reloaded', '3' => 'Three - reloaded'];
        TSortList::reload('form_sort', 'list1', $items);
    }
    
    /**
     * Send data
     */
    public function onSend($param)
    {
        // get form data
        $data = $this->form->getData();
        
        // put the data back to the form
        $this->form->setData($data);
        
        // creates a string with the form element's values
        $message = 'List 1: '  . implode(',', $data->list1) . '<br>';
        $message.= 'List 2 : ' . implode(',', $data->list2) . '<br>';
        
        // show the message
        new TMessage('info', $message);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
