---
name: adianti-registerlogfunction
description: RegisterLogFunction — código executável dbsamples (Persistence > Objects)
triggers: ["RegisterLogFunction", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — RegisterLogFunction — código executável dbsamples (Persistence > Objects)

Classe Tutor: `RegisterLogFunction`.
Ver no Tutor: `index.php?class=RegisterLogFunction` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/RegisterLogFunction.class.php`.


## Código

```php
<?php 
class RegisterLogFunction extends TPage
{ 
    public function __construct() 
    { 
        parent::__construct(); 
        try 
        { 
            TTransaction::open('samples'); 
            // define log 
            TTransaction::setLoggerFunction( function($message) {
                                                 echo $message . '<br>';
                                             });
            
            TTransaction::log("inserting city..."); 
            $cidade = new City; 
            $cidade->name = 'Porto Alegre'; 
            $cidade->store();
             
            TTransaction::close(); // close transaction
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
