---
name: adianti-formcopymemoryview
description: Copy button — Tutor Presentation > Extras > Copy button
triggers: ["FormCopyMemoryView", "Copy", "button", "Tutor", "Presentation", "Extras", "Copy button"]
---

# Skill Adianti — Copy button — Tutor Presentation > Extras > Copy button

Classe Tutor: `FormCopyMemoryView`.
Ver no Tutor: `index.php?class=FormCopyMemoryView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extras/FormCopyMemoryView.class.php`.


## Código

```php
<?php
/**
 * FormButtonStyleView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormCopyMemoryView extends TPage
{
    public function __construct()
    {
        parent::__construct();
        
        $button = new TButton('bt2a');
        $button->setImage('far:copy');
        $button->setLabel('Click here to copy some content to clipboard');
        $button->addFunction("__adianti_copy_to_clipboard('this is the content');");
        
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($button);
        
        parent::add($vbox);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
