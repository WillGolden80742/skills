---
name: adianti-objectcomposition
description: ObjectComposition — código executável dbsamples (Persistence > Objects)
triggers: ["ObjectComposition", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — ObjectComposition — código executável dbsamples (Persistence > Objects)

Classe Tutor: `ObjectComposition`.
Ver no Tutor: `index.php?class=ObjectComposition` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ObjectComposition.class.php`.


## Código

```php
<?php
class ObjectComposition extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples'); // abre uma transao
            $customer= new Customer(4); // carrega o cliente 4
            
            $contact1 = new Contact;
            $contact2 = new Contact;

            $contact1->type  = 'fone';
            $contact1->value = '78 2343-4545';
            $contact2->type  = 'fone';
            $contact2->value = '78 9494-0404';
            
            $customer->addContact($contact1);
            $customer->addContact($contact2);
            
            $customer->store();
            
            new TMessage('info', 'Contatos adicionados');
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
