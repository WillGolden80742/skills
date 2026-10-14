---
name: adianti-helloworldaction2
description: HelloWorldAction2 — Tutor Presentation > Primeiros passos
triggers: ["HelloWorldAction2", "HelloWorldAction", "Tutor", "Presentation", "Primeiros", "passos", "Primeiros passos"]
---

# Skill Adianti — HelloWorldAction2 — Tutor Presentation > Primeiros passos

Classe Tutor: `HelloWorldAction2`.
Ver no Tutor: `index.php?class=HelloWorldAction2` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/HelloWorldAction2.php`.


## Código

```php
<?php 
class HelloWorldAction2 extends TPage 
{ 
    private $label;
    
    public function __construct() 
    { 
        parent::__construct();
        $this->label = new TLabel('');
        parent::add($this->label);
    } 
    
    public function onHelloWorld() 
    { 
         $this->label->setValue('Hello World');
    } 
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
