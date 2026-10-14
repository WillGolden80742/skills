---
name: adianti-collectionfilter
description: CollectionFilter — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionFilter", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionFilter — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionFilter`.
Ver no Tutor: `index.php?class=CollectionFilter` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionFilter.php`.


## Código

```php
<?php
class CollectionFilter extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples');
            
            // load customers
            $list = Customer::where('id', '>', '1')->filter( function($object) {
              return ( (strpos($object->gender, 'F') !== false)
                   AND (strpos($object->birthdate, '1990') !== false) );
            }, false);
                                 
            foreach ($list as $customer)
            {
                echo $customer->id . ' - ' . $customer->name . ' - ' . $customer->address. '<br>';
            }
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
