---
name: adianti-objectfirstlast
description: ObjectFirstLast — código executável dbsamples (Persistence > Objects)
triggers: ["ObjectFirstLast", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — ObjectFirstLast — código executável dbsamples (Persistence > Objects)

Classe Tutor: `ObjectFirstLast`.
Ver no Tutor: `index.php?class=ObjectFirstLast` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ObjectFirstLast.class.php`.


## Código

```php
<?php 
class ObjectFirstLast extends TPage
{ 
    public function __construct() 
    { 
        parent::__construct(); 
        try 
        { 
            TTransaction::open('samples'); // open transaction
            
            $first = Customer::first();
            print '<b>First ID</b>:   ' . $first->id . '<br>';
            print '<b>First Name</b>: ' . $first->name . '<br>';
            
            echo  '<br>';
            $last  = Customer::last();
            print '<b>Last ID</b>:   ' . $last->id . '<br>';
            print '<b>Last Name</b>: ' . $last->name . '<br>';
            
            TTransaction::close(); // closes transaction
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
