---
name: adianti-circleview
description: Circle plugin — Tutor Presentation > Templates > Circle plugin
triggers: ["CircleView", "Circle", "plugin", "Tutor", "Presentation", "Templates", "Circle plugin"]
---

# Skill Adianti — Circle plugin — Tutor Presentation > Templates > Circle plugin

Classe Tutor: `CircleView`.
Ver no Tutor: `index.php?class=CircleView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extending/CircleView.class.php`.


## Código

```php
<?php
/**
 * CircleView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class CircleView extends TPage
{
    /**
     * Page constructor
     */
    function __construct()
    {
        parent::__construct();
        
        TScript::importFromFile('app/lib/include/circle/circle.js');
        TStyle::importFromFile('app/lib/include/circle/circle.css');
        
        $html = new THtmlRenderer('app/resources/circle.html');
        $html->enableSection('main', ['value' => 50]);
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($html);
        
        parent::add($vbox);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
