---
name: adianti-formscreenlabelsview
description: Screen labels — Tutor Presentation > Labels > Screen labels
triggers: ["FormScreenLabelsView", "Screen", "labels", "Tutor", "Presentation", "Screen labels"]
---

# Skill Adianti — Screen labels — Tutor Presentation > Labels > Screen labels

Classe Tutor: `FormScreenLabelsView`.
Ver no Tutor: `index.php?class=FormScreenLabelsView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Label/FormScreenLabelsView.class.php`.


## Código

```php
<?php
/**
 * FormScreenLabelsView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormScreenLabelsView extends TPage
{
    public function __construct()
    {
        parent::__construct();
        
        $barcode1 = new TBarcodeDisplay('1231723897');
        $barcode1->setType('code128');
        $barcode1->setHeight(100);
        
        $barcode2 = new TBarcodeDisplay('4096526265371');
        $barcode2->setType('ean13');
        $barcode2->setHeight(100);
        
        $qrcode1 = new TQRCodeDisplay('Hello World');
        $qrcode1->setHeight(350);
        
        $panel = new TPanelGroup('Barcodes and QRCodes');
        $panel->add(new TLabel('CODE 128'));
        $panel->add('<br>');
        $panel->add($barcode1);
        $panel->add('<br><br>');
        $panel->add(new TLabel('EAN 13'));
        $panel->add('<br>');
        $panel->add($barcode2);
        $panel->add('<br><br>');
        $panel->add(new TLabel('QR CODE'));
        $panel->add('<br>');
        $panel->add($qrcode1);
        
        parent::add($panel);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
