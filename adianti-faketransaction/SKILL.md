---
name: adianti-faketransaction
description: FakeTransaction — código executável dbsamples (Persistence > Connections)
triggers: ["FakeTransaction", "digo", "execut", "vel", "dbsamples", "Persistence", "Connections", "exemplo executavel"]
---

# Skill Adianti — FakeTransaction — código executável dbsamples (Persistence > Connections)

Classe Tutor: `FakeTransaction`.
Ver no Tutor: `index.php?class=FakeTransaction` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/FakeTransaction.class.php`.


## Código

```php
<?php 
class FakeTransaction extends TPage 
{ 
    public function __construct() 
    { 
        parent::__construct(); 
        try 
        { 
            TTransaction::openFake('samples'); // abre uma transação sem begin/commit
            // ...
            TTransaction::close(); // fecha a transação. 
        } 
        catch (Exception $e) 
        { 
            new TMessage('error', $e->getMessage()); 
        } 
    } 
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
