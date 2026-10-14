---
name: adianti-collectioncount
description: CollectionCount — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionCount", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionCount — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionCount`.
Ver no Tutor: `index.php?class=CollectionCount` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionCount.class.php`.


## Código

```php
<?php
class CollectionCount extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples'); // abre uma transao
            $criteria = new TCriteria;
            $criteria->add(new TFilter('name', 'like', 'Rafael%'), TExpression::OR_OPERATOR);
            $criteria->add(new TFilter('name', 'like', 'Ana%'), TExpression::OR_OPERATOR);
            
            $repository = new TRepository('Customer');
            $count = $repository->count($criteria);
            
            new TMessage('info', "Total de clientes encontrados: {$count} <br>\n");
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
