---
name: adianti-objectload
description: ObjectLoad — código executável dbsamples (Persistence > Objects)
triggers: ["ObjectLoad", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — ObjectLoad — código executável dbsamples (Persistence > Objects)

Classe Tutor: `ObjectLoad`.
Ver no Tutor: `index.php?class=ObjectLoad` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ObjectLoad.class.php`.


## Código

```php
<?php
class ObjectLoad extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples');
            
            // load customer, throw exception if not found
            $customer = new Customer(4);
            echo 'Name      : ' . $customer->name     . "<br>\n";
            echo 'Address   : ' . $customer->address  . "<br>\n";
            echo "<br>\n";
            
            // load customer, throw exception if not found
            $customer = new Customer(25);
            echo 'Name      : ' . $customer->name     . "<br>\n";
            echo 'Address   : ' . $customer->address  . "<br>\n";
            
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
