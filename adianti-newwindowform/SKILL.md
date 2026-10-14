---
name: adianti-newwindowform
description: NewWindowForm — Tutor Presentation > Extras
triggers: ["NewWindowForm", "Tutor", "Presentation", "Extras"]
---

# Skill Adianti — NewWindowForm — Tutor Presentation > Extras

Classe Tutor: `NewWindowForm`.
Ver no Tutor: `index.php?class=NewWindowForm` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extras/NewWindowForm.class.php`.


## Código

```php
<?php
/**
 * NewWindowForm
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class NewWindowForm extends TWindow
{
    private $form;
    
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        parent::setSize(570, null);
        parent::setTitle('Form inside window');
        
        // create the form
        $this->form = new BootstrapFormWrapper(new TQuickForm);
        $this->form->setFormTitle('Quick form');
        $this->form->style = 'width:90%; padding-top:20px';
        
        // create the form fields
        $code = new TEntry('code');
        $name = new TEntry('name');
        
        // add the fields inside the form
        $this->form->addQuickField('Code', $code, '30%');
        $this->form->addQuickField('Name', $name, '70%');
        
        // define the form action 
        $this->form->addQuickAction('Save', new TAction(array($this, 'onSave')), 'far:check-circle green');
        
        parent::add($this->form);
    }
    
    public function onSave($param)
    {
        $data = $this->form->getData();
        $this->form->setData($data); // put the data back to the form
        
        $objects = TSession::getValue('session_contacts');
        $objects[ $data->code ] = $data;
        
        TSession::setValue('session_contacts', $objects);
        
        // show the message
        new TMessage('info', 'Record added', new TAction(array('DatagridWindowForm', 'onReload')));
    }
    
    public function onLoad()
    {
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
