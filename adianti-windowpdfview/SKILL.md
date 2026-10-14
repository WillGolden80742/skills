---
name: adianti-windowpdfview
description: Window with embedded PDF — Tutor Presentation > Pages > Window with embedded PDF
triggers: ["WindowPDFView", "Window", "with", "embedded", "PDF", "Tutor", "Presentation", "Window with embedded PDF", "Pages"]
---

# Skill Adianti — Window with embedded PDF — Tutor Presentation > Pages > Window with embedded PDF

Classe Tutor: `WindowPDFView`.
Ver no Tutor: `index.php?class=WindowPDFView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Pages/WindowPDFView.class.php`.


## Código

```php
<?php
/**
 * WindowPDFView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class WindowPDFView extends TWindow
{
    public function __construct()
    {
        parent::__construct();
        parent::setTitle(_t('Window with embedded PDF'));
        parent::setSize(0.8, 0.8);
        
        $object = new TElement('object');
        $object->data  = 'https://adiantiframework.com.br/resources/adianti_framework.pdf';
        $object->type  = 'application/pdf';
        $object->style = "width: 100%; height:calc(100% - 10px)";
        $object->add('O navegador não suporta a exibição deste conteúdo, <a style="color:#007bff;" target=_newwindow href="'.$object->data.'"> clique aqui para baixar</a>...');
        
        parent::add($object);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
