---
name: adianti-collectiondelete
description: CollectionDelete — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionDelete", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionDelete — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionDelete`.
Ver no Tutor: `index.php?class=CollectionDelete` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionDelete.class.php`.


## Código

```php
<?php
class CollectionDelete extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples'); // abre uma transação
            TTransaction::setLogger(new TLoggerTXT('/tmp/log3.txt'));
            $criteria = new TCriteria;
            $criteria->add(new TFilter('address', 'like', 'Rua Porto%'));
            $criteria->add(new TFilter('gender',  '=', 'M'));
            $repository = new TRepository('Customer');
            $repository->delete($criteria);
            
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
