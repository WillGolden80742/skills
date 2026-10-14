---
name: adianti-multistepmultiformview
description: Multi Step Form — Tutor Presentation > Pages > Multi Step Form
triggers: ["MultiStepMultiFormView", "Multi", "Step", "Form", "Tutor", "Presentation", "Pages", "Multi Step Form"]
---

# Skill Adianti — Multi Step Form — Tutor Presentation > Pages > Multi Step Form

Classe Tutor: `MultiStepMultiFormView`.
Ver no Tutor: `index.php?class=MultiStepMultiFormView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Pages/MultiStepMultiFormView.class.php`.


## Código

```php
<?php
/**
 * MultiStepMultiFormView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class MultiStepMultiFormView extends TPage
{
    protected $form; // form
    
    /**
     * Class constructor
     * Creates the page and the registration form
     */
    function __construct()
    {
        parent::__construct();
        
        // creates the form
        $this->form = new BootstrapFormBuilder('form_account');
        $this->form->setFormTitle('Create account');
        $this->form->setColumnClasses(2, ['col-sm-3', 'col-sm-9']);
        
        // create the form fields
        $email       = new TEntry('email');
        $password    = new TPassword('password');
        $confirm     = new TPassword('confirm');

        $this->form->addFields(['Email'], [$email] );
        $this->form->addFields(['Password'], [$password] );
        $this->form->addFields(['Confirm password'], [$confirm] );

        // validations
        $email->addValidation('Email', new TRequiredValidator);
        $email->addValidation('Email', new TEmailValidator);
        $password->addValidation('Password', new TRequiredValidator);
        $confirm->addValidation('Confirm password', new TRequiredValidator);

        // add a form action
        $this->form->addAction('Next', new TAction(array($this, 'onNextForm')), 'fa:chevron-circle-right green');
        
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);
        
        // add the form to the page
        parent::add($vbox);
    }
    
    /**
     * Load form from session
     */
    public function onLoadFromSession()
    {
        $data = TSession::getValue('form_step1_data');
        $this->form->setData($data);
    }
    
    /**
     * onNextForm
     */
    public function onNextForm()
    {
        try
        {
            $this->form->validate();
            $data = $this->form->getData();
            
            if ($data->password !== $data->confirm)
            {
                throw new Exception('Passwords do not match');
            }
            // store data in the session
            TSession::setValue('form_step1_data', $data);
            
            // Load another page
            AdiantiCoreApplication::loadPage('MultiStepMultiForm2View', 'onLoadFromForm1', (array) $data);
            
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
