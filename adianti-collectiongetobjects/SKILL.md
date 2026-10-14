---
name: adianti-collectiongetobjects
description: CollectionGetObjects — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionGetObjects", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionGetObjects — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionGetObjects`.
Ver no Tutor: `index.php?class=CollectionGetObjects` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionGetObjects.class.php`.


## Código

```php
<?php
class CollectionGetObjects extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples');
            $criteria = new TCriteria;
            $criteria->add( new TFilter( 'gender', '=', 'M' ));
            $criteria->add( new TFilter( 'name', 'like', 'A%' ));
            
            $customers = Customer::getObjects($criteria);
            
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
?>
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
