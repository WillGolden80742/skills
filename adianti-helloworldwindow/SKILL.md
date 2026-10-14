---
name: adianti-helloworldwindow
description: HelloWorldWindow — Tutor Presentation > Primeiros passos
triggers: ["HelloWorldWindow", "Tutor", "Presentation", "Primeiros", "passos", "Primeiros passos"]
---

# Skill Adianti — HelloWorldWindow — Tutor Presentation > Primeiros passos

Classe Tutor: `HelloWorldWindow`.
Ver no Tutor: `index.php?class=HelloWorldWindow` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/HelloWorldWindow.class.php`.


## Código

```php
<?php 
class HelloWorldWindow extends TWindow 
{ 
    public function __construct() 
    { 
        parent::__construct(); 
        parent::setTitle('Window title');
        parent::setSize(400,200);        
        parent::add(new TLabel('Hello World'));
    } 
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
