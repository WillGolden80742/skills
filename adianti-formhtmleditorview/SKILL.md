---
name: adianti-formhtmleditorview
description: Html Editor — Tutor Presentation > Forms > Html Editor
triggers: ["FormHtmlEditorView", "Html", "Editor", "Tutor", "Presentation", "Forms", "Html Editor"]
---

# Skill Adianti — Html Editor — Tutor Presentation > Forms > Html Editor

Classe Tutor: `FormHtmlEditorView`.
Ver no Tutor: `index.php?class=FormHtmlEditorView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormHtmlEditorView.class.php`.


## Código

```php
<?php
/**
 * FormHtmlEditorView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormHtmlEditorView extends TPage
{
    private $form;
    
    /**
     * Page constructor
     */
    function __construct()
    {
        parent::__construct();
        
        // create the form
        $this->form = new BootstrapFormBuilder('my_html_form');
        $this->form->setFormTitle( _t('Html Editor') );
        
        // create the form fields
        $html = new THtmlEditor('html_text');
        $html->setSize( '100%', 200);
        $html->setOption('placeholder', 'type here...');
        $html->disableXssProtection();
        
        $this->form->addFields( [$html] );
        $this->form->addAction('Show', new TAction(array($this, 'onShow')), 'far:check-circle blue');
        $this->form->addAction('Insert text', new TAction(array($this, 'onInsert')), 'fa:plus green');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);
        parent::add($vbox);
    }
    
    public static function onInsert($param)
    {
        THtmlEditor::insertText('my_html_form', 'html_text', 'Hi there!');
    }
    
    /**
     * Show the form content
     */
    public function onShow($param)
    {
        $data = $this->form->getData();
        $this->form->setData($data); // put the data back to the form
        
        // show the message
        new TMessage('info', $data->html_text);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
