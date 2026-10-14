---
name: adianti-collectionloadproperty
description: CollectionLoadProperty — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionLoadProperty", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionLoadProperty — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionLoadProperty`.
Ver no Tutor: `index.php?class=CollectionLoadProperty` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionLoadProperty.class.php`.


## Código

```php
<?php
class CollectionLoadProperty extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples'); // abre uma transação
            $criteria = new TCriteria;
            $criteria->setProperty('limit' , 10);
            $criteria->setProperty('offset', 20);
            $criteria->setProperty('order' , 'id');
            
            $repository = new TRepository('Customer');
            $customers = $repository->load($criteria);
            
            foreach ($customers as $customer)
            {
                echo $customer->id . ' - ' . $customer->name . '<br>';
            }
            TTransaction::close(); // fecha a transação.
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
