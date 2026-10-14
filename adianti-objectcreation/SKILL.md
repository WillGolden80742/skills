---
name: adianti-objectcreation
description: ObjectCreation — código executável dbsamples (Persistence > Objects)
triggers: ["ObjectCreation", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — ObjectCreation — código executável dbsamples (Persistence > Objects)

Classe Tutor: `ObjectCreation`.
Ver no Tutor: `index.php?class=ObjectCreation` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ObjectCreate.php`.
Nota: Arquivo (ObjectCreate.php) e classe (ObjectCreation) têm nomes diferentes — o autoloader exige igualdade para rodar via ?class=.


## Código

```php
<?php 
class ObjectCreation extends TPage
{ 
    public function __construct() 
    { 
        parent::__construct(); 
        try 
        { 
            TTransaction::open('samples'); // open transaction 
            
            Customer::create( [ 'name' => 'Antonio Dall Oglio',
                                'address' => 'Rua da Conceicao',
                                'phone' => '(51) 8111-2222',
                                'birthdate' => '2013-02-15',
                                'status' => 'S',
                                'email' => 'antonio@dalloglio.net',
                                'gender' => 'M',
                                'category_id' => '1',
                                'city_id' => '1' ]);
                                
            new TMessage('info', 'Object stored successfully'); 
            TTransaction::close(); // Closes the transaction 
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
