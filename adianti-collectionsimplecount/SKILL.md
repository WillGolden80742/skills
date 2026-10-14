---
name: adianti-collectionsimplecount
description: CollectionSimpleCount — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionSimpleCount", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionSimpleCount — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionSimpleCount`.
Ver no Tutor: `index.php?class=CollectionSimpleCount` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionSimpleCount.class.php`.


## Código

```php
<?php
class CollectionSimpleCount extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples'); // abre uma transação
            // inicia o repositório
            $repository = new TRepository('Customer');
            // conta os clientes
            $count = $repository->where('name', 'like', 'Rafael%', TExpression::OR_OPERATOR)
                                 ->where('name', 'like', 'Ana%', TExpression::OR_OPERATOR)
                                 ->count();
            
            new TMessage('info', "Total de clientes encontrados: {$count} <br>\n");
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
