---
name: adianti-embeddedpdfview
description: Page with embedded PDF — Tutor Presentation > Pages > Page with embedded PDF
triggers: ["EmbeddedPDFView", "Page", "with", "embedded", "PDF", "Tutor", "Presentation", "Page with embedded PDF", "Pages"]
---

# Skill Adianti — Page with embedded PDF — Tutor Presentation > Pages > Page with embedded PDF

Classe Tutor: `EmbeddedPDFView`.
Ver no Tutor: `index.php?class=EmbeddedPDFView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Pages/EmbeddedPDFView.class.php`.


## Código

```php
<?php
/**
 * EmbeddedPDFView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class EmbeddedPDFView extends TPage
{
    public function __construct()
    {
        parent::__construct();
        
        $object = new TElement('iframe');
        $object->src   = 'https://adiantiframework.com.br/resources/adianti_framework.pdf';
        $object->type  = 'application/pdf';
        $object->style = "width: 100%; height:600px";
        
        parent::add($object);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
