---
name: adianti-splitregisterview
description: Side by side Form/DataGrid — Tutor Organization > Standard controls > Side by side Form/DataGrid
triggers: ["SplitRegisterView", "Side", "Form", "DataGrid", "Tutor", "Organization", "Side by side Form/DataGrid", "Standard controls"]
---

# Skill Adianti — Side by side Form/DataGrid — Tutor Organization > Standard controls > Side by side Form/DataGrid

Classe Tutor: `SplitRegisterView`.
Ver no Tutor: `index.php?class=SplitRegisterView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/StandardControls/SplitRegisterView.class.php`.


## Código

```php
<?php
/**
 * SplitRegisterView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class SplitRegisterView extends TPage
{
    public function __construct()
    {
        parent::__construct();
        
        $html = new THtmlRenderer('app/resources/split_view.html');
        $html->enableSection('main');
        
        $params = [];
        $params['register_state'] = 'false'; // avoid update URL with inner page address
        $params['target_container'] = 'left-panel';
        AdiantiCoreApplication::loadPage('SplitLeftRegisterView', null, $params); // load page
        
        $params = [];
        $params['register_state'] = 'false'; // avoid update URL with inner page address
        $params['target_container'] = 'right-panel';
        AdiantiCoreApplication::loadPage('SplitRightRegisterView', null, $params); // load page
        
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
