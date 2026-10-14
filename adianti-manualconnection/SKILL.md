---
name: adianti-manualconnection
description: ManualConnection — código executável dbsamples (Persistence > Connections)
triggers: ["ManualConnection", "digo", "execut", "vel", "dbsamples", "Persistence", "Connections", "exemplo executavel"]
---

# Skill Adianti — ManualConnection — código executável dbsamples (Persistence > Connections)

Classe Tutor: `ManualConnection`.
Ver no Tutor: `index.php?class=ManualConnection` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ManualConnection.class.php`.


## Código

```php
<?php
class ManualConnection extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            // connection info
            $db = array();
            $db['host'] = '';
            $db['port'] = '';
            $db['name'] = 'app/database/samples.db';
            $db['user'] = '';
            $db['pass'] = '';
            $db['type'] = 'sqlite';
            
            TTransaction::open(NULL, $db); // open transaction
            $conn = TTransaction::get(); // get PDO connection
            
            // make query
            $result = $conn->query('SELECT id, name from customer order by id');
            
            // iterate results
            foreach ($result as $row)
            {
                print $row['id'] . '-';
                print $row['name'] . "<br>\n";
            }
            TTransaction::close(); // close transaction
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
