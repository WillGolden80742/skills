---
name: adianti-collectionupdate
description: CollectionUpdate — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionUpdate", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionUpdate — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionUpdate`.
Ver no Tutor: `index.php?class=CollectionUpdate` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionUpdate.class.php`.


## Código

```php
<?php
class CollectionUpdate extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples');
            
            // load customers
            $customers = Customer::where('city_id', '=', '4')->load();
            
            foreach ($customers as $customer)
            {
                // update record
                $customer->phone = '84 '.substr($customer->phone, 3);
                $customer->store();
            }
            new TMessage('info', 'Records updated');
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
