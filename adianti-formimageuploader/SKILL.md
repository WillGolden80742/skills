---
name: adianti-formimageuploader
description: Image upload and cropper — Tutor Presentation > Forms > Image upload and cropper
triggers: ["FormImageUploader", "Image", "upload", "and", "cropper", "Tutor", "Presentation", "Image upload and cropper", "Forms"]
---

# Skill Adianti — Image upload and cropper — Tutor Presentation > Forms > Image upload and cropper

Classe Tutor: `FormImageUploader`.
Ver no Tutor: `index.php?class=FormImageUploader` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormImageUploader.class.php`.


## Código

```php
<?php
/**
 * FormImageUploader
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormImageUploader extends TPage
{
    private $form;
    
    /**
     * Page constructor
     */
    function __construct()
    {
        parent::__construct();
        
        // create the form
        $this->form = new BootstrapFormBuilder;
        $this->form->setFormTitle( _t('Image upload and cropper') );
        
        // create the form fields
        $imagecropper = new TImageCropper('imagecropper');
        $imageupload  = new TFile('imageupload');
        $imagecapture = new TImageCapture('imagecapture');
        
        $imagecropper->setSize(400, 200);
        $imagecropper->setCropSize(400, 200);
        $imagecropper->setAllowedExtensions( ['gif', 'png', 'jpg', 'jpeg'] );
        //$imagecropper->enableFileHandling();
        
        $imageupload->setAllowedExtensions( ['gif', 'png', 'jpg', 'jpeg'] );
        //$imageupload->enableFileHandling();
        $imageupload->enableImageGallery();
        
        $imagecapture->setAllowedExtensions( ['gif', 'png', 'jpg', 'jpeg'] );
        $imagecapture->setSize(400, 200);
        $imagecapture->setCropSize(400, 200);
        
        $this->form->addFields( [new TLabel('Image Cropper')], [$imagecropper] );
        $this->form->addFields( [new TLabel('Image Uploader')],[$imageupload] );
        $this->form->addFields( [new TLabel('Image Capture')], [$imagecapture] );
        
        $this->form->addAction('Show', new TAction(array($this, 'onShow')), 'far:check-circle green');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);
        parent::add($vbox);
    }
    
    /**
     * Show the form content
     */
    public static function onShow($param)
    {
        // show the message
        new TMessage('info', '<b>Image Crop</b>: tmp/'. $param['imagecropper'] . '<br>'.
                            ' <b>Image Upload</b>: tmp/' . $param['imageupload'] . '<br>'.
                            ' <b>Image Capture</b>: tmp/' . $param['imagecapture'] );
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
