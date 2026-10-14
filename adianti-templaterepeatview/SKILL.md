---
name: adianti-templaterepeatview
description: Template View repeated — Tutor Presentation > Templates > Template View repeated
triggers: ["TemplateRepeatView", "Template", "View", "repeated", "Tutor", "Presentation", "Templates", "Template View repeated"]
---

# Skill Adianti — Template View repeated — Tutor Presentation > Templates > Template View repeated

Classe Tutor: `TemplateRepeatView`.
Ver no Tutor: `index.php?class=TemplateRepeatView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extending/TemplateRepeatView.class.php`.


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
class TemplateRepeatView extends TPage
{
    /**
     * Constructor method
     */
    public function __construct()
    {
        parent::__construct();
        
        // create the HTML Renderer
        $this->html = new THtmlRenderer('app/resources/customer_accounts.html');

        try
        {
            // define replacements for the main section
            $plain_object = new stdClass;
            $plain_object->id   = '001';
            $plain_object->name = 'John';
            
            $replace = array();
            $replace['object']      = $plain_object;
            
            $replace['header']    = [ [ 'name' => 'Field test',
                                        'value' => 'Field value' ] ];
            
            $replace['accounts1'] = [ [ 'date'=>'2016-05-01',
                                        'value'=>100,
                                        'details' => [ [ 'product'=> 'Chocolate',
                                                         'qty'=> 10,
                                                         'value' => 5 ],
                                                       [ 'product'=> 'Milk',
                                                         'qty'=> 5,
                                                         'value' => 10 ] ] ],
                                      [ 'date'  => '2016-05-03',
                                        'value' => 200,
                                        'details' => [ [ 'product' => 'Cofee',
                                                         'qty' => 10,
                                                         'value' => 10 ],
                                                       [ 'product'=> 'Pizza',
                                                         'qty' => 5,
                                                         'value' => 20 ] ] ] ];

            $replace['accounts2'] = [ [ 'date'  => '2016-05-07',
                                        'value' => 100,
                                        'details' => [ [ 'product'=> 'Pendrive',
                                                         'qty' => 10,
                                                         'value' => 5 ],
                                                       [ 'product'=> 'SDCard',
                                                         'qty'=> 5,
                                                         'value' => 10 ] ] ],
                                      [ 'date' => '2016-05-08',
                                        'value' => 200,
                                        'details' => [ [ 'product' => 'DVD-R',
                                                         'qty' => 10,
                                                         'value' => 10 ],
                                                       [ 'product' => 'Mouse',
                                                         'qty' => 5,
                                                         'value' => 20 ] ] ] ];
                                                      
            // replace the main section variables
            $this->html->enableSection('main', $replace);
            
            // wrap the page content using vertical box
            $vbox = new TVBox;
            $vbox->style = 'width: 100%';
            $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
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
