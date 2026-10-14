---
name: adianti-objectupdate
description: ObjectUpdate — código executável dbsamples (Persistence > Objects)
triggers: ["ObjectUpdate", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — ObjectUpdate — código executável dbsamples (Persistence > Objects)

Classe Tutor: `ObjectUpdate`.
Ver no Tutor: `index.php?class=ObjectUpdate` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ObjectUpdate.class.php`.


## Código

```php
<?php 
class ObjectUpdate extends TPage 
{ 
    public function __construct() 
    { 
        parent::__construct(); 
        try 
        { 
            // open transaction 
            TTransaction::open('samples');

            // find customer
            $customer = Customer::find(31);

            // check if found
            if ($customer) 
            { 
                $customer->phone = '51 8111-3333'; // change phone number
                $customer->store(); // stores the object
            } 

            new TMessage('info', 'Object updated'); 
            TTransaction::close(); // close transaction 
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
