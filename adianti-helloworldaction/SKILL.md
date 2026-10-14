---
name: adianti-helloworldaction
description: HelloWorldAction — Tutor Presentation > Primeiros passos
triggers: ["HelloWorldAction", "Tutor", "Presentation", "Primeiros", "passos", "Primeiros passos"]
---

# Skill Adianti — HelloWorldAction — Tutor Presentation > Primeiros passos

Classe Tutor: `HelloWorldAction`.
Ver no Tutor: `index.php?class=HelloWorldAction` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/HelloWorldAction.class.php`.


## Código

```php
<?php 
class HelloWorldAction extends TPage 
{ 
    public function __construct() 
    { 
        parent::__construct(); 
    }
    
    public function onHelloWorld()
    {
        parent::add(new TLabel('Hello World'));
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
