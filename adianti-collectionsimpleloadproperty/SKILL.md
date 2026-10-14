---
name: adianti-collectionsimpleloadproperty
description: CollectionSimpleLoadProperty — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionSimpleLoadProperty", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionSimpleLoadProperty — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionSimpleLoadProperty`.
Ver no Tutor: `index.php?class=CollectionSimpleLoadProperty` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionSimpleLoadProperty.class.php`.


## Código

```php
<?php 
class CollectionSimpleLoadProperty extends TPage 
{ 
    public function __construct() 
    { 
        parent::__construct(); 
        try 
        { 
            TTransaction::open('samples'); // open transaction 
            
            // load odered by id, limit 10 offset 20
            $customers = Customer::orderBy('id')->take(10)->skip(20)->load();
            if ($customers)
            {
                foreach ($customers as $customer) 
                { 
                    echo $customer->id . ' - ' . $customer->name . '<br>'; 
                } 
            }
            
            echo '<br>';
            
            // get the first, and converts to array
            var_dump( Customer::orderBy('id')->first()->toArray() );
            
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
