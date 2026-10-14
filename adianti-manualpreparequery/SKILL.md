---
name: adianti-manualpreparequery
description: ManualPrepareQuery — código executável dbsamples (Persistence > Connections)
triggers: ["ManualPrepareQuery", "digo", "execut", "vel", "dbsamples", "Persistence", "Connections", "exemplo executavel"]
---

# Skill Adianti — ManualPrepareQuery — código executável dbsamples (Persistence > Connections)

Classe Tutor: `ManualPrepareQuery`.
Ver no Tutor: `index.php?class=ManualPrepareQuery` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ManualPrepareQuery.class.php`.


## Código

```php
<?php
class ManualPrepareQuery extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples'); // abre uma transação
            $conn = TTransaction::get(); // obtém a conexão
            
            $sth = $conn->prepare('SELECT id, name from customer
                                   WHERE id >= ? AND id <= ?');
            
            $sth->execute(array(3,12));
            $result = $sth->fetchAll();
            
            // exibe os resultados
            foreach ($result as $row)
            {
                print $row['id'] . '-';
                print $row['name'] . "<br>\n";
            }
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
