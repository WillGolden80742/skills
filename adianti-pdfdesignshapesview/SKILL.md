---
name: adianti-pdfdesignshapesview
description: Designed shapes — Tutor Presentation > Reports > Designed shapes
triggers: ["PDFDesignShapesView", "Designed", "shapes", "Tutor", "Presentation", "Reports", "Designed shapes"]
---

# Skill Adianti — Designed shapes — Tutor Presentation > Reports > Designed shapes

Classe Tutor: `PDFDesignShapesView`.
Ver no Tutor: `index.php?class=PDFDesignShapesView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Report/PDFDesignShapesView.class.php`.


## Código

```php
<?php
/**
 * PDF Designed Shapes
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class PDFDesignShapesView extends TPage
{
    private $form; // form
    private $pdf;
    
    /**
     * Class constructor
     */
    function __construct()
    {
        parent::__construct();
        
        // creates the form
        $this->form = new BootstrapFormBuilder;
        $this->form->setFormTitle('Designed PDF shapes');
        
        // create the form fields
        $name = new TEntry('name');
        
        $this->form->addFields( [new TLabel('Name', 'red')], [$name] );
        $this->form->addAction('Generate', new TAction(array($this, 'onGenerate')), 'far:check-circle green');
        
        $name->addValidation('Name', new TRequiredValidator);
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);

        parent::add($vbox);
    }

    /**
     * method onGenerate()
     * Executed whenever the user clicks at the generate button
     */
    function onGenerate()
    {
        try
        {
            $data = $this->form->getData();
            $this->form->validate();
            
            $this->pdf = new AdiantiPDFDesigner('L', 'a5');
            $this->pdf->SetMargins(2,2,2); // define margins
            $this->pdf->AddPage();
            $this->pdf->Ln();

            $this->pdf->makeRectangle(84, 52, 350, 210, '#FFF04B', '#000000', 2, 4, '#000000');
            $this->pdf->makeEllipse(294, 210, 194, 104, '#8081CB', '#000000', 5, 4, '#818181');
            $this->pdf->makeRectangle(30, 60, 230, 68, '#FF2D2D', '#000000', 3, 4, '#646464');
            $this->pdf->makeLine(34, 166, 172, 294, 3, '#03FF00');
            $this->pdf->makeText(46, 82, "Hello {$data->name}", 32, 'Arial', '', '#FFFFFF', 3, '#000000');
            $this->pdf->makeText(312, 242, "Your name is {$data->name}", 26, 'Times', '', '#FFFFFF', 2, '#000000');
            $this->pdf->makeLine(200, 310, 464, 64, 4, '#8DF0FF');
            $this->pdf->makeRectangle(95, 137, 306, 62, '#FFFFFF', '#000000', 1, 0, '#000000');
            $this->pdf->makeText(106, 150, "Hello {$data->name}, Hello {$data->name}, Hello {$data->name}, Hello {$data->name}.\nHello {$data->name}, Hello {$data->name}, Hello {$data->name}, Hello {$data->name}.\nHello {$data->name}, Hello {$data->name}, Hello {$data->name}, Hello {$data->name}.", 12, 'Times', '', '#000000', 0, '#000000');
            $this->pdf->makeText(142, 24, "Adianti PDF Designer", 26, 'Times', '', '#3A368C', 2, '#C5C5C5');
            $this->pdf->makeLine(320, 336, 550, 316, 2, '#000000');

            $this->pdf->makeText(292, 74, "'Dynamic text !", 18, 'Arial', 'B', '#FF0000');

            $file = 'app/output/pdf_shapes.pdf';            
            if (!file_exists($file) OR is_writable($file))
            {
                $this->pdf->Output($file);

                $window = TWindow::create(_t('Designed shapes'), 0.8, 0.8);
                $object = new TElement('object');
                $object->data  = $file;
                $object->type  = 'application/pdf';
                $object->style = "width: 100%; height:calc(100% - 10px)";
                $object->add('O navegador não suporta a exibição deste conteúdo, <a style="color:#007bff;" target=_newwindow href="'.$object->data.'"> clique aqui para baixar</a>...');

                $window->add($object);
                $window->show();
            }
            else
            {
                throw new Exception(_t('Permission denied') . ': ' . $file);
            }
        }
        catch (Exception $e) // in case of exception
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
