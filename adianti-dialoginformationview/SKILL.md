---
name: adianti-dialoginformationview
description: Information dialog — Tutor Presentation > Dialogs > Information dialog
triggers: ["DialogInformationView", "Information", "dialog", "Tutor", "Presentation", "Dialogs", "Information dialog"]
---

# Skill Adianti — Information dialog — Tutor Presentation > Dialogs > Information dialog

Classe Tutor: `DialogInformationView`.
Ver no Tutor: `index.php?class=DialogInformationView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Dialogs/DialogInformationView.class.php`.


## Código

```php
<?php
/**
 * DialogInformationView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class DialogInformationView extends TPage
{
    public function __construct()
    {
        parent::__construct();
        
        // show the message dialog
        new TMessage('info', 'Information message');
        
        parent::add(new TXMLBreadCrumb('menu.xml', __CLASS__));
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
