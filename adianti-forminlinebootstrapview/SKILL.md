---
name: adianti-forminlinebootstrapview
description: FormInlineBootstrapView — Tutor Presentation > Forms
triggers: ["FormInlineBootstrapView", "Tutor", "Presentation", "Forms", "FormInlineBootstrap"]
---

# Skill Adianti — FormInlineBootstrapView — Tutor Presentation > Forms

Classe Tutor: `FormInlineBootstrapView`.
Ver no Tutor: `index.php?class=FormInlineBootstrapView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormInlineBootstrapView.class.php`.


## Código

```php
<?php
/**
 * FormInlineBootstrapView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormInlineBootstrapView extends TPage
{
    private $form;
    
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        // create the form
        $this->form = new BootstrapFormBuilder;
        $this->form->setFormTitle(_t('Bootstrap 1 line form'));
        
        // create the form fields
        $input1      = new TEntry('input1');
        $input2      = new TEntry('input2');
        $input3      = new TEntry('input3');
        $input4      = new TEntry('input4');
        $input5      = new TEntry('input5');
        $input6      = new TEntry('input6');
        $input7      = new TEntry('input7');
        $input8      = new TEntry('input8');
        
        $input1->placeholder = 'sm1';
        $input2->placeholder = 'sm2';
        $input3->placeholder = 'sm1';
        $input4->placeholder = 'sm2';
        $input5->placeholder = 'sm1';
        $input6->placeholder = 'sm2';
        $input7->placeholder = 'sm1';
        $input8->placeholder = 'sm2';
        
        // add the fields inside the form
        $row = $this->form->addFields( [$input1], [$input2], [$input3], [$input4] ,[$input5], [$input6], [$input7], [$input8] );
        $row->layout = ['col-sm-1', 'col-sm-2', 'col-sm-1', 'col-sm-2', 'col-sm-1', 'col-sm-2', 'col-sm-1', 'col-sm-2' ];
        
        // define the form action
        $btn = $this->form->addAction('Send', new TAction(array($this, 'onSend')), 'far:check-circle');
        $btn->class = 'btn btn-success';
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        // $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);
        
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
        
        // show the message
        new TMessage('info', str_replace('","', '",<br>&nbsp;"', json_encode($data)));
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
