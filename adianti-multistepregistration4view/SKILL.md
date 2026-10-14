---
name: adianti-multistepregistration4view
description: MultiStepRegistration4View — Tutor Presentation > Pages
triggers: ["MultiStepRegistration4View", "MultiStepRegistration", "View", "Tutor", "Presentation", "Pages", "MultiStepRegistration4"]
---

# Skill Adianti — MultiStepRegistration4View — Tutor Presentation > Pages

Classe Tutor: `MultiStepRegistration4View`.
Ver no Tutor: `index.php?class=MultiStepRegistration4View` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Pages/MultiStepRegistration4View.class.php`.


## Código

```php
<?php
/**
 * Multi Step 4
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class MultiStepRegistration4View extends TPage
{
    /**
     * Constructor method
     */
    public function __construct()
    {
        parent::__construct();
        
        try
        {
            TPage::include_css('app/resources/confirmation.css');
            
            // create the HTML Renderer
            $this->html = new THtmlRenderer('app/resources/confirmation.html');
            
            $confirmation_data = array_merge(TSession::getValue('registration_course'),
                                             TSession::getValue('registration_data'));
            $this->html->enableSection('main', $confirmation_data);
            
            $pagestep = new TPageStep;
            $pagestep->addItem('Welcome');
            $pagestep->addItem('Selection');
            $pagestep->addItem('Complete information');
            $pagestep->addItem('Confirmation');
            $pagestep->select('Confirmation');
            
            // wrap the page content using vertical box
            $vbox = new TVBox;
            $vbox->style = 'width: 100%';
            $vbox->add(new TXMLBreadCrumb('menu.xml', 'MultiStepRegistration1View'));
            $vbox->add( $pagestep );
            $vbox->add($this->html);
            parent::add($vbox);
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
