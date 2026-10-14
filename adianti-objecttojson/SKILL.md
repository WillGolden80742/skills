---
name: adianti-objecttojson
description: ObjectToJson — código executável dbsamples (Persistence > Objects)
triggers: ["ObjectToJson", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — ObjectToJson — código executável dbsamples (Persistence > Objects)

Classe Tutor: `ObjectToJson`.
Ver no Tutor: `index.php?class=ObjectToJson` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ObjectToJson.class.php`.


## Código

```php
<?php 
class ObjectToJson extends TPage
{ 
    public function __construct() 
    { 
        parent::__construct(); 
        try 
        { 
            TTransaction::open('samples');
            
            // Load object
            $customer = Customer::find(4);
            
            // if found
            if ($customer)
            {
                // show as JSON
                print_r( str_replace(',', ',<br>', $customer->toJson()));
            }
            
            TTransaction::close();
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
