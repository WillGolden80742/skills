---
name: adianti-objectlazy
description: ObjectLazy — código executável dbsamples (Persistence > Objects)
triggers: ["ObjectLazy", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — ObjectLazy — código executável dbsamples (Persistence > Objects)

Classe Tutor: `ObjectLazy`.
Ver no Tutor: `index.php?class=ObjectLazy` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ObjectLazy.class.php`.


## Código

```php
<?php
class ObjectLazy extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples'); // abre uma transao
            
            $customer= new Customer(4); // carrega o cliente 4
            echo $customer->city->name; // chama get_city()
            echo '<br>';
            echo $customer->city_name;  // chama get_city_name()
            
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
