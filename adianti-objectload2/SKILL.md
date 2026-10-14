---
name: adianti-objectload2
description: ObjectLoad2 — código executável dbsamples (Persistence > Objects)
triggers: ["ObjectLoad2", "ObjectLoad", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — ObjectLoad2 — código executável dbsamples (Persistence > Objects)

Classe Tutor: `ObjectLoad2`.
Ver no Tutor: `index.php?class=ObjectLoad2` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ObjectLoad2.class.php`.


## Código

```php
<?php
class ObjectLoad2 extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples');
            
            $loader = new Customer;
            // load customer, returns FALSE if not found
            $customer = $loader->load(4);
            
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
