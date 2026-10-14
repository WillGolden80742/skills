---
name: adianti-embeddedvideoview
description: Page with embedded video — Tutor Presentation > Pages > Page with embedded video
triggers: ["EmbeddedVideoView", "Page", "with", "embedded", "video", "Tutor", "Presentation", "Page with embedded video", "Pages"]
---

# Skill Adianti — Page with embedded video — Tutor Presentation > Pages > Page with embedded video

Classe Tutor: `EmbeddedVideoView`.
Ver no Tutor: `index.php?class=EmbeddedVideoView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Pages/EmbeddedVideoView.class.php`.


## Código

```php
<?php
/**
 * EmbeddedVideoView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class EmbeddedVideoView extends TPage
{
    public function __construct()
    {
        parent::__construct();
        
        $object = new TElement('iframe');
        $object->width       = '100%';
        $object->height      = '600px';
        $object->src         = '//www.youtube.com/embed/YEZaF9uixjY';
        $object->frameborder = '0';
        $object->allow       = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture';
        
        parent::add($object);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
