---
name: adianti-objectstore
description: ObjectStore — código executável dbsamples (Persistence > Objects)
triggers: ["ObjectStore", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — ObjectStore — código executável dbsamples (Persistence > Objects)

Classe Tutor: `ObjectStore`.
Ver no Tutor: `index.php?class=ObjectStore` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ObjectStore.class.php`.


## Código

```php
<?php
class ObjectStore extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples'); // abre uma transação
            
            // cria novo objeto
            $giovani = new Customer;
            $giovani->name        = 'Giovanni Dall Oglio';
            $giovani->address     = 'Rua da Conceicao';
            $giovani->phone       = '(51) 8111-2222';
            $giovani->birthdate   = '2013-02-15';
            $giovani->status      = 'S';
            $giovani->email       = 'giovanni@dalloglio.net';
            $giovani->gender      = 'M';
            $giovani->category_id = '1';
            $giovani->city_id     = '1';
            $giovani->store(); // armazena o objeto
            
            new TMessage('info', 'Objeto armazenado com sucesso');
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
