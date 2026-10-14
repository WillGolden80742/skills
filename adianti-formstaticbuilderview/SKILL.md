---
name: adianti-formstaticbuilderview
description: Form with static post — Tutor Presentation > Forms > Form with static post
triggers: ["FormStaticBuilderView", "Form", "with", "static", "post", "Tutor", "Presentation", "Form with static post", "Forms"]
---

# Skill Adianti — Form with static post — Tutor Presentation > Forms > Form with static post

Classe Tutor: `FormStaticBuilderView`.
Ver no Tutor: `index.php?class=FormStaticBuilderView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormStaticBuilderView.class.php`.


## Código

```php
<?php
/**
 * FormStaticBuilderView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormStaticBuilderView extends TPage
{
    private $form;
    
    /**
     * Class constructor
     * Creates the page
     */
    public function __construct()
    {
        parent::__construct();
        
        $this->form = new BootstrapFormBuilder;
        $this->form->setFormTitle(_t('Form with static post'));
        
        $id      = new TEntry('id');
        $name    = new TEntry('name');
        $address = new TEntry('address');
        $date    = new TDate('date');
        $obs     = new TText('obs');
        
        // add a row with 2 slots
        $this->form->addFields( [ new TLabel('Id') ],        [ $id ] );
        $this->form->addFields( [ $lbl=new TLabel('Name') ], [ $name ] );
        $this->form->addFields( [ new TLabel('Address') ],   [ $address ] );
        $this->form->addFields( [ new TLabel('Date') ],      [ $date ] );
        $this->form->addFields( [ new TLabel('Obs') ],       [ $obs ] );
        
        $lbl->setFontColor('red');
        $id->setSize('30%');
        $name->setSize('70%');
        $address->setSize('70%');
        $date->setSize('30%');
        $obs->setSize('70%');
        
        $this->form->addAction('Send', new TAction(array($this, 'onSend')), 'far:check-circle green');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);

        parent::add($vbox);
    }
    
    /**
     * Static post data
     */
    public static function onSend($param)
    {
        try
        {
            if (empty($param['name']))
            {
                throw new Exception('Name cannot be empty');
            }
            
            // show results
            new TMessage('info', str_replace("\n", '<br> ', print_r($param, true)));
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
