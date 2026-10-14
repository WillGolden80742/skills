---
name: adianti-formdbsortview
description: Sort DB List — Tutor Presentation > Forms > Sort DB List
triggers: ["FormDBSortView", "Sort", "List", "Tutor", "Presentation", "Forms", "Sort DB List"]
---

# Skill Adianti — Sort DB List — Tutor Presentation > Forms > Sort DB List

Classe Tutor: `FormDBSortView`.
Ver no Tutor: `index.php?class=FormDBSortView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormDBSortView.class.php`.


## Código

```php
<?php
/**
 * FormDBSortView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormDBSortView extends TPage
{
    private $form;
    
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        $this->form = new BootstrapFormBuilder;
        $this->form->setFormTitle(_t('Sort DB List'));
        
        $list1 = new TDBSortList('list1', 'samples', 'Customer', 'id', '{name} (#{id})', 'id');
        $list2 = new TSortList('list2');
        
        $list1->setSize(200, 200);
        $list2->setSize(200, 200);
        
        $list1->connectTo($list2);
        $list2->connectTo($list1);
        
        $this->form->addFields([$list1, $list2]);
        $this->form->addAction( 'Send', new TAction(array($this, 'onSend')), 'far:check-circle');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);

        parent::add($vbox);
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
