---
name: adianti-manualquery
description: ManualQuery — código executável dbsamples (Persistence > Connections)
triggers: ["ManualQuery", "digo", "execut", "vel", "dbsamples", "Persistence", "Connections", "exemplo executavel"]
---

# Skill Adianti — ManualQuery — código executável dbsamples (Persistence > Connections)

Classe Tutor: `ManualQuery`.
Ver no Tutor: `index.php?class=ManualQuery` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ManualQuery.class.php`.


## Código

```php
<?php
class ManualQuery extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples'); // abre uma transao
            $conn = TTransaction::get(); // obtm a conexo
            
            // realiza a consulta
            $result = $conn->query('SELECT id, name from customer order by id');
            
            // exibe os resultados
            foreach ($result as $row)
            {
                print $row['id'] . '-';
                print $row['name'] . "<br>\n";
            }
            TTransaction::close(); // fecha a transao.
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
