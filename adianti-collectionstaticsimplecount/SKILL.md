---
name: adianti-collectionstaticsimplecount
description: CollectionStaticSimpleCount — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionStaticSimpleCount", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionStaticSimpleCount — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionStaticSimpleCount`.
Ver no Tutor: `index.php?class=CollectionStaticSimpleCount` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionStaticSimpleCount.class.php`.


## Código

```php
<?php
class CollectionStaticSimpleCount extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples');
            
            // count customers
            $count = Customer::where('gender', '=', 'M')
                             ->where('name', 'like', 'A%')
                             ->count();
                                 
            print( $count );
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
