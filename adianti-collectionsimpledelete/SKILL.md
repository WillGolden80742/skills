---
name: adianti-collectionsimpledelete
description: CollectionSimpleDelete — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionSimpleDelete", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionSimpleDelete — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionSimpleDelete`.
Ver no Tutor: `index.php?class=CollectionSimpleDelete` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionSimpleDelete.class.php`.


## Código

```php
<?php
class CollectionSimpleDelete extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples'); // abre uma transação
            
            // inicia o repositório
            $repository = new TRepository('Customer');
            // deleta os clientes
            $repository->where('address', 'like', 'Rua Porto%')
                        ->where('gender',  '=', 'M')
                        ->delete();
            
            new TMessage('info', 'Registros excluídos');
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
