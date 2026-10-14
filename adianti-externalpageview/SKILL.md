---
name: adianti-externalpageview
description: Page with external content — Tutor Presentation > Pages > Page with external content
triggers: ["ExternalPageView", "Page", "with", "external", "content", "Tutor", "Presentation", "Page with external content", "Pages"]
---

# Skill Adianti — Page with external content — Tutor Presentation > Pages > Page with external content

Classe Tutor: `ExternalPageView`.
Ver no Tutor: `index.php?class=ExternalPageView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Pages/ExternalPageView.class.php`.


## Código

```php
<?php
/**
 * ExternalPageView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class ExternalPageView extends TPage
{
    public function __construct()
    {
        parent::__construct();
        
        $iframe = new TElement('iframe');
        $iframe->id = "iframe_external";
        $iframe->src = "https://pt.wikipedia.org/wiki/PHP";
        $iframe->frameborder = "0";
        $iframe->scrolling = "yes";
        $iframe->width = "100%";
        $iframe->height = "700px";
        
        parent::add($iframe);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
