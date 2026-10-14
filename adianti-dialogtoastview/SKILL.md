---
name: adianti-dialogtoastview
description: Toast — Tutor Presentation > Dialogs > Toast
triggers: ["DialogToastView", "Toast", "Tutor", "Presentation", "Dialogs"]
---

# Skill Adianti — Toast — Tutor Presentation > Dialogs > Toast

Classe Tutor: `DialogToastView`.
Ver no Tutor: `index.php?class=DialogToastView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Dialogs/DialogToastView.class.php`.


## Código

```php
<?php
/**
 * DialogToastView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class DialogToastView extends TPage
{
    public function __construct()
    {
        parent::__construct();
        
        TToast::show('show', 'Toast test 1', 'top right', 'far:check-circle' );
        TToast::show('info', 'Toast test 2', 'top right', 'far:check-circle' );
        TToast::show('warning', 'Toast test 3', 'top right', 'far:check-circle' );
        TToast::show('error', 'Toast test 4', 'top right', 'far:check-circle' );
        TToast::show('success', 'Toast test 4', 'top right', 'far:check-circle' );
        
        parent::add(new TXMLBreadCrumb('menu.xml', __CLASS__));
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
