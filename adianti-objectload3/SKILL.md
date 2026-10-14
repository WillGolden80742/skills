---
name: adianti-objectload3
description: ObjectLoad3 — código executável dbsamples (Persistence > Objects)
triggers: ["ObjectLoad3", "ObjectLoad", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — ObjectLoad3 — código executável dbsamples (Persistence > Objects)

Classe Tutor: `ObjectLoad3`.
Ver no Tutor: `index.php?class=ObjectLoad3` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ObjectLoad3.class.php`.


## Código

```php
<?php
class ObjectLoad3 extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples');
            
            // load customer, returns FALSE if not found
            $customer = Customer::find(4);
            
            if ($customer instanceof Customer)
            {
                echo 'Name      : ' . $customer->name     . "<br>\n";
                echo 'Address   : ' . $customer->address  . "<br>\n";
            }
            
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
