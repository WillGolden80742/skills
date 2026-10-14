---
name: adianti-templateviewmaskview
description: Template View masks — Tutor Presentation > Templates > Template View masks
triggers: ["TemplateViewMaskView", "Template", "View", "masks", "Tutor", "Presentation", "Templates", "Template View masks"]
---

# Skill Adianti — Template View masks — Tutor Presentation > Templates > Template View masks

Classe Tutor: `TemplateViewMaskView`.
Ver no Tutor: `index.php?class=TemplateViewMaskView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extending/TemplateViewMaskView.class.php`.


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
class TemplateViewMaskView extends TPage
{
    /**
     * Constructor method
     */
    public function __construct()
    {
        parent::__construct();
        
        // create the HTML Renderer
        $this->html = new THtmlRenderer('app/resources/template_masks.html');
        
        try
        {
            $object = new stdClass;
            $object->id   = 1;
            $object->name = 'Test';
            
            // define replacements for the main section
            $replace = array();
            $replace['object']   = $object;
            $replace['date']     = date('Y-m-d');
            $replace['datetime'] = date('Y-m-d H:i:s');
            $replace['number']   = 123456.78;
            $replace['value1']   = 10;
            $replace['value2']   = 20;
            $replace['value3']   = 2;
            
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
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
