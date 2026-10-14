---
name: adianti-customerformwindow
description: CustomerFormWindow — Tutor Organization > CompleteRegistrations
triggers: ["CustomerFormWindow", "Tutor", "Organization", "CompleteRegistrations"]
---

# Skill Adianti — CustomerFormWindow — Tutor Organization > CompleteRegistrations

Classe Tutor: `CustomerFormWindow`.
Ver no Tutor: `index.php?class=CustomerFormWindow` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/CompleteRegistrations/CustomerFormWindow.class.php`.


## Código

```php
<?php
/**
 * CustomerFormWindow
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class CustomerFormWindow extends TWindow
{
    public function __construct($param)
    {
        parent::__construct($param);
        parent::setSize(0.5, null);
        parent::setMinWidth(0.5, 700);
        parent::removePadding();
        parent::disableEscape();
        parent::setTitle('Customer');
        
        $this->form = new CustomerFormView($param, true);
        $this->form->setTargetContainer('');
        parent::add($this->form);
    }
    
    /**
     * Redirect calls to decorated object
     */
    public function onEdit($param)
    {
        $this->form->onEdit($param);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
