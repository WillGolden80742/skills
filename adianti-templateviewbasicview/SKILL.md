---
name: adianti-templateviewbasicview
description: Template View basic — Tutor Presentation > Templates > Template View basic
triggers: ["TemplateViewBasicView", "Template", "View", "basic", "Tutor", "Presentation", "Templates", "Template View basic"]
---

# Skill Adianti — Template View basic — Tutor Presentation > Templates > Template View basic

Classe Tutor: `TemplateViewBasicView`.
Ver no Tutor: `index.php?class=TemplateViewBasicView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extending/TemplateViewBasicView.class.php`.


## Código

```php
<?php
/**
 * Template View pattern implementation
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class TemplateViewBasicView extends TPage
{
    /**
     * Constructor method
     */
    public function __construct()
    {
        parent::__construct();
        
        // create the HTML Renderer
        $this->html = new THtmlRenderer('app/resources/customer.html');
        
        try
        {
            // look for customer 1
            TTransaction::open('samples');
            $customer = new Customer(1);
            
            // define replacements for the main section
            $replace = array();
            $replace['code']    = $customer->id;
            $replace['name']    = $customer->name;
            $replace['address'] = $customer->address;
            
            // replace the main section variables
            $this->html->enableSection('main', $replace);
            
            // define the replacements based on customer contacts
            $replace = array();
            foreach ($customer->getContacts() as $contact)
            {
                $replace[] = array('type' => $contact->type,
                                   'value'=> $contact->value);
            }
            
            // define with sections will be enabled
            $this->html->enableSection('contacts');
            $this->html->enableSection('contacts-detail', $replace, TRUE);
            
            // wrap the page content using vertical box
            $vbox = new TVBox;
            $vbox->style = 'width: 100%';
            $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
            $vbox->add($this->html);
    
            parent::add($vbox);            
            TTransaction::close();
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
