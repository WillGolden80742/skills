---
name: adianti-templatehtmlmanualform
description: HTML manual form — Tutor Presentation > Templates > HTML manual form
triggers: ["TemplateHtmlManualForm", "HTML", "manual", "form", "Tutor", "Presentation", "Templates", "HTML manual form"]
---

# Skill Adianti — HTML manual form — Tutor Presentation > Templates > HTML manual form

Classe Tutor: `TemplateHtmlManualForm`.
Ver no Tutor: `index.php?class=TemplateHtmlManualForm` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extending/TemplateHtmlManualForm.class.php`.


## Código

```php
<?php
/**
 * HTML5 manual form
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class TemplateHtmlManualForm extends TPage
{
    /**
     * Constructor method
     */
    public function __construct()
    {
        parent::__construct();
        
        // create the HTML Renderer
        $this->html = new THtmlRenderer('app/resources/raw_form.html');
        
        try
        {
            // define replacements for the main section
            $replace = array();
            $replace['first_name']  = 'John';
            $replace['last_name']   = 'Scott';
            $replace['user_name']   = 'john';
            
            // replace the main section variables
            $this->html->enableSection('main', $replace);
            
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
    
    /**
     * Send data
     */
    public static function onSend($param)
    {
        echo '<pre>';
        print_r($param);
        echo '</pre>';
    } 
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
