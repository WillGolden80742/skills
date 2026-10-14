---
name: adianti-dialogerrorview
description: Error dialog — Tutor Presentation > Dialogs > Error dialog
triggers: ["DialogErrorView", "Error", "dialog", "Tutor", "Presentation", "Dialogs", "Error dialog"]
---

# Skill Adianti — Error dialog — Tutor Presentation > Dialogs > Error dialog

Classe Tutor: `DialogErrorView`.
Ver no Tutor: `index.php?class=DialogErrorView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Dialogs/DialogErrorView.class.php`.


## Código

```php
<?php
/**
 * DialogErrorView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class DialogErrorView extends TPage
{
    public function __construct()
    {
        parent::__construct();
        
        // show the message dialog
        new TMessage('error', 'Error message');
        
        parent::add(new TXMLBreadCrumb('menu.xml', __CLASS__));
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
