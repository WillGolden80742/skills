---
name: adianti-collectionsimpleload
description: CollectionSimpleLoad — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionSimpleLoad", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionSimpleLoad — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionSimpleLoad`.
Ver no Tutor: `index.php?class=CollectionSimpleLoad` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionSimpleLoad.class.php`.


## Código

```php
<?php
class CollectionSimpleLoad extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples');
            
            $repository = new TRepository('Customer');
            
            $customers = $repository->where('gender', '=', 'M')
                                     ->where('name', 'like', 'A%')
                                     ->load();
            
            foreach ($customers as $customer)
            {
                echo $customer->id . ' - ' . $customer->name . '<br>';
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
