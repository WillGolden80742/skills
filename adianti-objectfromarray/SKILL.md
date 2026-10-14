---
name: adianti-objectfromarray
description: ObjectFromArray — código executável dbsamples (Persistence > Objects)
triggers: ["ObjectFromArray", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — ObjectFromArray — código executável dbsamples (Persistence > Objects)

Classe Tutor: `ObjectFromArray`.
Ver no Tutor: `index.php?class=ObjectFromArray` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ObjectFromArray.class.php`.


## Código

```php
<?php 
class ObjectFromArray extends TPage
{ 
    public function __construct() 
    { 
        parent::__construct(); 
        try 
        { 
            TTransaction::open('samples'); // open transaction
            
            // Convert an Active Record into array
            $customer = new Customer(4);
            print_r($customer->toArray());
            
            // Using an array to fill the Active Record
            $test = array();
            $test['name'] = 'Customer from array';
            $test['address'] = 'Address from array';
            $test['category_id'] = 1;
            $test['city_id'] = 1;
            $test['birthdate'] = date('Y-m-d');
            
            $customer2 = new Customer;
            $customer2->fromArray($test);
            $customer2->store(); 
            
            TTransaction::close(); // closes transaction
        } 
        catch (Exception $e) 
        { 
            new TMessage('error', $e->getMessage()); 
        } 
    } 
} 
?>
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
