---
name: adianti-alertview
description: Alerts — Tutor Presentation > Dialogs > Alerts
triggers: ["AlertView", "Alerts", "Tutor", "Presentation", "Dialogs"]
---

# Skill Adianti — Alerts — Tutor Presentation > Dialogs > Alerts

Classe Tutor: `AlertView`.
Ver no Tutor: `index.php?class=AlertView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Dialogs/AlertView.class.php`.


## Código

```php
<?php
/**
 * AlertView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class AlertView extends TPage
{
    public function __construct()
    {
        parent::__construct();
        
        parent::add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TAlert('info', 'Info alert'));
        $vbox->add(new TAlert('success', 'Success alert'));
        $vbox->add(new TAlert('warning', 'Warning alert'));
        $vbox->add(new TAlert('danger', 'Danger alert'));
        
        parent::add($vbox);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
