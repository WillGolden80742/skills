---
name: adianti-collectionstaticbatchupdate
description: CollectionStaticBatchUpdate — código executável dbsamples (Persistence > Collections)
triggers: ["CollectionStaticBatchUpdate", "digo", "execut", "vel", "dbsamples", "Persistence", "Collections", "exemplo executavel"]
---

# Skill Adianti — CollectionStaticBatchUpdate — código executável dbsamples (Persistence > Collections)

Classe Tutor: `CollectionStaticBatchUpdate`.
Ver no Tutor: `index.php?class=CollectionStaticBatchUpdate` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/CollectionStaticBatchUpdate.class.php`.


## Código

```php
<?php 
class CollectionStaticBatchUpdate extends TPage
{ 
    public function __construct() 
    { 
        parent::__construct(); 
        try 
        { 
            TTransaction::open('samples'); 
            
            // batch update
            Customer::where('id', 'IN', [1,2,3,4])
                    ->where('status', '=', 'C')
                    ->set('gender', 'M')
                    ->update();
            
            // batch update using replace function
            $find = 'João';
            $replace = 'Joao';
            Customer::set('nome', "replace(nome, :[{$find}]:, :[{$replace}]:)")->update();
            
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
