---
name: adianti-multistepregistration1view
description: Multi Step Wizard — Tutor Presentation > Pages > Multi Step Wizard
triggers: ["MultiStepRegistration1View", "Multi", "Step", "Wizard", "Tutor", "Presentation", "Pages", "Multi Step Wizard"]
---

# Skill Adianti — Multi Step Wizard — Tutor Presentation > Pages > Multi Step Wizard

Classe Tutor: `MultiStepRegistration1View`.
Ver no Tutor: `index.php?class=MultiStepRegistration1View` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Pages/MultiStepRegistration1View.class.php`.


## Código

```php
<?php
/**
 * Multi Step 1
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class MultiStepRegistration1View extends TPage
{
    /**
     * Constructor method
     */
    public function __construct()
    {
        parent::__construct();
        
        try
        {
            // create the HTML Renderer
            $this->html = new THtmlRenderer('app/resources/welcome.html');
            $this->html->enableSection('main');
            
            $pagestep = new TPageStep;
            $pagestep->addItem('Welcome');
            $pagestep->addItem('Selection');
            $pagestep->addItem('Complete information');
            $pagestep->addItem('Confirmation');
            $pagestep->select('Welcome');
            
            // wrap the page content using vertical box
            $vbox = new TVBox;
            $vbox->style = 'width: 100%';
            $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
            $vbox->add( $pagestep );
            $vbox->add( $this->html );
            parent::add($vbox);
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
        }
    }
    
    function loadPage()
    {}
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
