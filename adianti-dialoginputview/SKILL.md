---
name: adianti-dialoginputview
description: Input dialog — Tutor Presentation > Dialogs > Input dialog
triggers: ["DialogInputView", "Input", "dialog", "Tutor", "Presentation", "Dialogs", "Input dialog"]
---

# Skill Adianti — Input dialog — Tutor Presentation > Dialogs > Input dialog

Classe Tutor: `DialogInputView`.
Ver no Tutor: `index.php?class=DialogInputView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Dialogs/DialogInputView.class.php`.


## Código

```php
<?php
/**
 * DialogInputView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class DialogInputView extends TPage
{
    public function __construct()
    {
        parent::__construct();
        
        $button = new TActionLink('Open dialog', new TAction([$this, 'onInputDialog']));
        $button->class='btn btn-default';
        
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($button);
        
        parent::add( $vbox );
    }
    
    /**
     * Open an input dialog
     */
    public static function onInputDialog( $param )
    {
        $form = new BootstrapFormBuilder('input_form');
        
        $login = new TEntry('login');
        $pass  = new TPassword('password');
        
        $form->addFields( [new TLabel('Login')], [$login]);
        $form->addFields( [new TLabel('Password')], [$pass]);
        
        $form->addAction('Confirm 1', new TAction([__CLASS__, 'onConfirm1']), 'fa:save green');
        $form->addAction('Confirm 2', new TAction([__CLASS__, 'onConfirm2']), 'far:check-circle blue');
        
        // show the input dialog
        new TInputDialog('Input dialog title', $form);
    }
    
    /**
     * Show the input dialog data
     */
    public static function onConfirm1( $param )
    {
        new TMessage('info', 'Confirm1 : ' . str_replace('","', '",<br>&nbsp;"', json_encode($param)));
    }
    
    /**
     * Show the input dialog data
     */
    public static function onConfirm2( $param )
    {
        new TMessage('info', 'Confirm2 : ' . str_replace('","', '",<br>&nbsp;"', json_encode($param)));
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
