---
name: adianti-transactioninfo
description: TransactionInfo — código executável dbsamples (Persistence > Connections)
triggers: ["TransactionInfo", "digo", "execut", "vel", "dbsamples", "Persistence", "Connections", "exemplo executavel"]
---

# Skill Adianti — TransactionInfo — código executável dbsamples (Persistence > Connections)

Classe Tutor: `TransactionInfo`.
Ver no Tutor: `index.php?class=TransactionInfo` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/TransactionInfo.class.php`.


## Código

```php
<?php 
class TransactionInfo extends TPage
{ 
    public function __construct() 
    { 
        parent::__construct(); 
        try 
        { 
            TTransaction::open('samples'); // open transaction
            
            print TTransaction::getDatabase(); // current database
            
            echo '<br>';
            
            print_r(TTransaction::getDatabaseInfo()); // current db info
             
            TTransaction::close(); // close transaction 
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
