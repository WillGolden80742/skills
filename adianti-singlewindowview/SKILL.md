---
name: adianti-singlewindowview
description: Common window — Tutor Presentation > Pages > Common window
triggers: ["SingleWindowView", "Common", "window", "Tutor", "Presentation", "Pages", "Common window"]
---

# Skill Adianti — Common window — Tutor Presentation > Pages > Common window

Classe Tutor: `SingleWindowView`.
Ver no Tutor: `index.php?class=SingleWindowView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Pages/SingleWindowView.class.php`.


## Código

```php
<?php
/**
 * SingleWindowView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class SingleWindowView extends TWindow
{
    /**
     * Constructor method
     */
    public function __construct()
    {
        parent::__construct();
        parent::setTitle('Window');
        
        // with: 500, height: automatic
        parent::setSize(0.6, null); // use 0.6, 0.4 (for relative sizes 60%, 40%)
        
        // create the HTML Renderer
        $this->html = new THtmlRenderer('app/resources/page.html');
        
        $replaces = [];
        $replaces['title']  = 'Panel title';
        $replaces['footer'] = 'Panel footer';
        $replaces['name']   = 'Someone famous';
        
        // replace the main section variables
        $this->html->enableSection('main', $replaces);
        
        parent::add($this->html);            
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
