---
name: adianti-collectionarray
description: CollectionArray — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionArray", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionArray — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionArray`.
Ver no Tutor: `index.php?class=CollectionArray` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionArray.class.php`.


## Código

```php
<?php
class CollectionArray extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            echo '<pre>';
            TTransaction::open('samples'); // abre uma transação
            
            // load an indexed array with all products
            $products = Product::getIndexedArray('id', 'description');
            var_dump($products);
            
            // load an indexed array with all products with masks
            $products = Product::getIndexedArray('key:{id}', 'description:{description}');
            var_dump($products);
            
            // load an indexed array with all products filtered by unity
            $products = Product::where('unity', '=', 'PC')
                               ->orderBy('id')
                               ->getIndexedArray('id', 'description');
            var_dump($products);
            
            // load an indexed array with all products filtered by array of ids
            $products = Product::where('id', 'in', [1,2,3,4])
                               ->orderBy('id')
                               ->getIndexedArray('id', 'description');
            var_dump($products);
            
            echo '</pre>';
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
