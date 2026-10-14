---
name: adianti-modalform
description: Modal form — Tutor Presentation > Forms > Modal form
triggers: ["ModalForm", "Modal", "form", "Tutor", "Presentation", "Forms", "Modal form"]
---

# Skill Adianti — Modal form — Tutor Presentation > Forms > Modal form

Classe Tutor: `ModalForm`.
Ver no Tutor: `index.php?class=ModalForm` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/ModalForm.class.php`.


## Código

```php
<?php
/**
 * ModalForm
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class ModalForm extends TPage
{
    protected $form; // modal form
    
    /**
     * Constructor
     */
    function __construct($param)
    {
        parent::__construct();
        
        // creates the form
        $this->form = new TModalForm('form_login');
        $this->form->setFormTitle('Login');
        
        // create the form fields
        $login     = new TEntry('login');
        $password  = new TPassword('password');
        
        $login->disableAutoComplete();
        $password->disableAutoComplete();
        $login->setSize('100%');
        $password->setSize('100%');
        $login->placeholder = 'Login';
        $password->placeholder = 'Password';
        $password->disableToggleVisibility();
        $login->autofocus = 'autofocus';
        
        $this->form->addRowField('Login', $login, true );
        $this->form->addRowField('Password', $password, true );
        
        $this->form->addAction('Log in', new TAction([$this, 'onLogin']), '' );
        
        $this->form->addFooterAction('Create account', new TAction([$this, 'test']), '');
        
        // add the form to the page
        parent::add($this->form);
    }
    
    /**
     * show form data
     */
    public static function onLogin($param)
    {
        new TMessage('info', str_replace('","', '",<br>&nbsp;"', json_encode($param)));
    }
    
    public function test($para)
    {
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
