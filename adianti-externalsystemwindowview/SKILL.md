---
name: adianti-externalsystemwindowview
description: Window with external system — Tutor Presentation > Pages > Window with external system
triggers: ["ExternalSystemWindowView", "Window", "with", "external", "system", "Tutor", "Presentation", "Window with external system", "Pages"]
---

# Skill Adianti — Window with external system — Tutor Presentation > Pages > Window with external system

Classe Tutor: `ExternalSystemWindowView`.
Ver no Tutor: `index.php?class=ExternalSystemWindowView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Pages/ExternalSystemWindowView.class.php`.


## Código

```php
<?php
/**
 * ExternalSystemWindowView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class ExternalSystemWindowView extends TWindow
{
    public function __construct()
    {
        parent::__construct();
        parent::setTitle(_t('Window with external system'));
        parent::removePadding();
        parent::setSize(0.8, 650);
        
        $iframe = new TElement('iframe');
        $iframe->id = "iframe_external";
        $iframe->src = "//framework.adianti.me/template";
        $iframe->frameborder = "0";
        $iframe->scrolling = "yes";
        $iframe->width = "100%";
        $iframe->height = "600px";
        
        parent::add($iframe);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
