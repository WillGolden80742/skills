---
name: adianti-collectionstaticsimpledelete
description: CollectionStaticSimpleDelete — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionStaticSimpleDelete", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionStaticSimpleDelete — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionStaticSimpleDelete`.
Ver no Tutor: `index.php?class=CollectionStaticSimpleDelete` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionStaticSimpleDelete.class.php`.


## Código

```php
<?php
class CollectionStaticSimpleDelete extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples');
            
            Customer::where('address', 'like', 'Rua Porto%')
                        ->where('gender',  '=', 'M')
                        ->delete();
            
            new TMessage('info', 'Records Deleted'); 
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
