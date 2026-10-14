---
name: adianti-collectionload
description: CollectionLoad — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionLoad", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionLoad — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionLoad`.
Ver no Tutor: `index.php?class=CollectionLoad` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionLoad.class.php`.


## Código

```php
<?php
class CollectionLoad extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples'); // abre uma transao
            $criteria = new TCriteria;
            $criteria->add(new TFilter('gender', '=', 'F'));
            $criteria->add(new TFilter('status', '=', 'M')); 
            
            $repository = new TRepository('Customer');
            $customers = $repository->load($criteria);
            
            foreach ($customers as $customer)
            {
                echo $customer->id . ' - ' . $customer->name . '<br>';
            }
            TTransaction::close(); // fecha a transao.
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
