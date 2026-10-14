---
name: adianti-jumbotronview
description: Jumbotron — Tutor Presentation > Templates > Jumbotron
triggers: ["JumbotronView", "Jumbotron", "Tutor", "Presentation", "Templates"]
---

# Skill Adianti — Jumbotron — Tutor Presentation > Templates > Jumbotron

Classe Tutor: `JumbotronView`.
Ver no Tutor: `index.php?class=JumbotronView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extending/JumbotronView.class.php`.


## Código

```php
<?php
/**
 * JumbotronView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class JumbotronView extends TPage
{
    /**
     * Constructor method
     */
    public function __construct()
    {
        parent::__construct();
        
        // create the HTML Renderer
        $this->html = new THtmlRenderer('app/resources/jumbotron.html');
        
        $replaces = [];
        // replace the main section variables
        $this->html->enableSection('main', $replaces);
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->html);
        parent::add($vbox);            
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
