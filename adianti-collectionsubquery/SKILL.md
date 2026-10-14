---
name: adianti-collectionsubquery
description: CollectionSubQuery — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionSubQuery", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionSubQuery — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionSubQuery`.
Ver no Tutor: `index.php?class=CollectionSubQuery` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionSubQuery.class.php`.


## Código

```php
<?php
class CollectionSubQuery extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples');
            
            $skill_id = 1;
        	$customers = Customer::where('id', 'in',
        	    "(SELECT customer_id FROM customer_skill WHERE skill_id = :[{$skill_id}]:)")->load();
        	
        	if ($customers)
        	{
        	    foreach ($customers as $customer)
        	    {
        	        print $customer->id . '-' . $customer->name . "\n<br>";
        	    }
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
