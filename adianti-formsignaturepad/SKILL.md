---
name: adianti-formsignaturepad
description: Signature area — Tutor Presentation > Forms > Signature area
triggers: ["FormSignaturePad", "Signature", "area", "Tutor", "Presentation", "Forms", "Signature area"]
---

# Skill Adianti — Signature area — Tutor Presentation > Forms > Signature area

Classe Tutor: `FormSignaturePad`.
Ver no Tutor: `index.php?class=FormSignaturePad` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormSignaturePad.class.php`.


## Código

```php
<?php
/**
 * FormSignaturePad
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormSignaturePad extends TPage
{
    private $form;
    
    /**
     * Page constructor
     */
    function __construct()
    {
        parent::__construct();
        
        // create the form
        $this->form = new BootstrapFormBuilder;
        $this->form->setFormTitle( _t('Signature area') );
        
        // create the form fields
        $signaturepad = new TSignaturePad('signaturepad');
        $signaturepad->setSize(400, 200);
        $signaturepad->setDrawSize(800, 400);
        $signaturepad->setPenStyle('#0000ff',1);
        
        // $signaturepad->enableBase64();
        // $signaturepad->enableFileHandling();
        
        $this->form->addFields( [new TLabel('Signature Pad')], [$signaturepad] );
        
        $this->form->addAction('Show', new TAction(array($this, 'onShow')), 'far:check-circle green');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);
        parent::add($vbox);
    }
    
    /**
     * Show the form content
     */
    public static function onShow($param)
    {
        // show the message
        new TMessage('info', '<b>Signature Pad</b>: tmp/'. $param['signaturepad'] );
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
