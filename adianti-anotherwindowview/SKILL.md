---
name: adianti-anotherwindowview
description: AnotherWindowView — Tutor Presentation > Containers
triggers: ["AnotherWindowView", "Tutor", "Presentation", "Containers", "AnotherWindow"]
---

# Skill Adianti — AnotherWindowView — Tutor Presentation > Containers

Classe Tutor: `AnotherWindowView`.
Ver no Tutor: `index.php?class=AnotherWindowView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Containers/AnotherWindowView.class.php`.


## Código

```php
<?php
/**
 * AnotherWindowView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class AnotherWindowView extends TWindow
{
    private $form;
    
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        parent::setTitle('New Window');
        parent::setSize(800, 400);
        
        parent::add(new TLabel('Another Window'));
    }
    public function xyz()
    {
    }
}
?>
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
