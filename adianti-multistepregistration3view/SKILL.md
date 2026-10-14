---
name: adianti-multistepregistration3view
description: MultiStepRegistration3View — Tutor Presentation > Pages
triggers: ["MultiStepRegistration3View", "MultiStepRegistration", "View", "Tutor", "Presentation", "Pages", "MultiStepRegistration3"]
---

# Skill Adianti — MultiStepRegistration3View — Tutor Presentation > Pages

Classe Tutor: `MultiStepRegistration3View`.
Ver no Tutor: `index.php?class=MultiStepRegistration3View` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Pages/MultiStepRegistration3View.class.php`.


## Código

```php
<?php
/**
 * Multi Step 3
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class MultiStepRegistration3View extends TPage
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
        $this->form->setFormTitle('Personal details');
        
        // create the form fields
        $email        = new TEntry('email');
        $first_name   = new TEntry('first_name');
        $last_name    = new TEntry('last_name');
        $phone        = new TEntry('phone');
        
        // add the fields
        $this->form->addFields(['Email'], [$email] );
        $this->form->addFields(['First name'], [$first_name] );
        $this->form->addFields(['Last name'], [$last_name] );
        $this->form->addFields(['Phone'], [$phone] );
        
        // validations
        $email->addValidation('Email', new TEmailValidator);
        $first_name->addValidation('First name', new TRequiredValidator);
        $last_name->addValidation('Last name', new TRequiredValidator);
        $phone->addValidation('Phone', new TRequiredValidator);

        // add a form action
        $this->form->addAction('Back', new TAction(array($this, 'onBackForm')), 'far:arrow-alt-circle-left red');
        $this->form->addAction('Confirm', new TAction(array($this, 'onConfirm')), 'far:check-circle green');
        
        $pagestep = new TPageStep;
        $pagestep->addItem('Welcome');
        $pagestep->addItem('Selection');
        $pagestep->addItem('Complete information');
        $pagestep->addItem('Confirmation');
        $pagestep->select('Complete information');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', 'MultiStepRegistration1View'));
        $vbox->add( $pagestep );
        $vbox->add( $this->form );
        parent::add($vbox);
    }
    
    /**
     * Load the previous form
     */
    public function onBackForm()
    {
        // Load another page
        AdiantiCoreApplication::loadPage('MultiStepRegistration2View');
    }
    
    /**
     * confirmation screen
     */
    public function onConfirm()
    {
        try
        {
            $this->form->validate();
            $data = $this->form->getData();
            TSession::setValue('registration_data', (array) $data);
            
            AdiantiCoreApplication::loadPage('MultiStepRegistration4View');
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
