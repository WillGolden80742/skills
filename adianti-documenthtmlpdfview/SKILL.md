---
name: adianti-documenthtmlpdfview
description: Document HTML->PDF — Tutor Presentation > Reports > Document HTML->PDF
triggers: ["DocumentHtmlPdfView", "Document", "HTML", "PDF", "Tutor", "Presentation", "Reports", "Document HTML->PDF", "Document HTML-"]
---

# Skill Adianti — Document HTML->PDF — Tutor Presentation > Reports > Document HTML->PDF

Classe Tutor: `DocumentHtmlPdfView`.
Ver no Tutor: `index.php?class=DocumentHtmlPdfView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Report/DocumentHtmlPdfView.class.php`.


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
class DocumentHtmlPdfView extends TPage
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
            
            $contents = '<style>' . file_get_contents('app/resources/styles-print-bundle.css') . '</style>';
            $contents .= $this->html->getContents();
            
            $options = new \Dompdf\Options();
            $options->setIsRemoteEnabled(true);
            $options->setChroot(getcwd());
            
            // converts the HTML template into PDF
            $dompdf = new \Dompdf\Dompdf($options);
            $dompdf->loadHtml($contents);
            $dompdf->setPaper('A4', 'portrait');
            $dompdf->render();
            
            // write and open file
            file_put_contents('app/output/document.pdf', $dompdf->output());
            
            // open window to show pdf
            $window = TWindow::create(_t('Document HTML->PDF'), 0.8, 0.8);
            $object = new TElement('object');
            $object->data  = 'app/output/document.pdf';
            $object->type  = 'application/pdf';
            $object->style = "width: 100%; height:calc(100% - 10px)";
            $object->add('O navegador não suporta a exibição deste conteúdo, <a style="color:#007bff;" target=_newwindow href="'.$object->data.'"> clique aqui para baixar</a>...');
            
            $window->add($object);
            $window->show();
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
