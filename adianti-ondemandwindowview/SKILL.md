---
name: adianti-ondemandwindowview
description: On demand window — Tutor Presentation > Pages > On demand window
triggers: ["OnDemandWindowView", "demand", "window", "Tutor", "Presentation", "Pages", "On demand window"]
---

# Skill Adianti — On demand window — Tutor Presentation > Pages > On demand window

Classe Tutor: `OnDemandWindowView`.
Ver no Tutor: `index.php?class=OnDemandWindowView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Pages/OnDemandWindowView.class.php`.


## Código

```php
<?php
/**
 * OnDemandWindowView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class OnDemandWindowView extends TPage
{
    public function __construct()
    {
        parent::__construct();
        
        $window = TWindow::create(_t('On demand window'), 0.8, null);
        
        $html = new THtmlRenderer('app/resources/page.html');
        
        $replaces = [];
        $replaces['title']  = 'Panel title';
        $replaces['footer'] = 'Panel footer';
        $replaces['name']   = 'Someone famous';
        
        // replace the main section variables
        $html->enableSection('main', $replaces);
        
        $window->add($html);
        $window->show();
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
