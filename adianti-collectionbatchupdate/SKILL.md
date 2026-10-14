---
name: adianti-collectionbatchupdate
description: CollectionBatchUpdate — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionBatchUpdate", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionBatchUpdate — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionBatchUpdate`.
Ver no Tutor: `index.php?class=CollectionBatchUpdate` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionBatchUpdate.class.php`.


## Código

```php
<?php 
class CollectionBatchUpdate extends TPage
{ 
    public function __construct() 
    { 
        parent::__construct(); 
        try 
        { 
            TTransaction::open('samples'); 
            
            $repos = new TRepository('Customer');
            $criteria = new TCriteria;
            $criteria->add(new TFilter('id', 'IN', [1,2,3,4]));
            $criteria->add(new TFilter('status', '=', 'C'));
            
            $values = array('gender' => 'F');
            $repos->update($values, $criteria);
                    
            new TMessage('info', 'Records updated'); 
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
