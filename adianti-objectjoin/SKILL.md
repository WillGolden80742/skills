---
name: adianti-objectjoin
description: ObjectJoin — código executável dbsamples (Persistence > Objects)
triggers: ["ObjectJoin", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — ObjectJoin — código executável dbsamples (Persistence > Objects)

Classe Tutor: `ObjectJoin`.
Ver no Tutor: `index.php?class=ObjectJoin` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ObjectJoin.class.php`.


## Código

```php
<?php
class ObjectJoin extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples');
            TTransaction::dump();
            echo '<pre>';
            
            // Load Customer + City + State
            var_dump(Customer::select('customer.id', 'customer.name', 'city.id as city_id', 'city.name as city_name')
                             -> join('city', ['customer.city_id' => 'city.id'])
                             ->join('state', ['city.state_id' => 'state.id'])
                             ->load(null, false)); // turn off object load
            
            // count customers by city
            var_dump(Customer::join('city', ['customer.city_id' => 'city.id'])
                             ->join('state', ['city.state_id' => 'state.id'])
                             ->groupBy(['city.id', 'city.name'])
                             ->countBy('customer.id', 'count_alias'));
            
            echo '</pre>';
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
