---
name: adianti-registerlogdump
description: RegisterLogDump — código executável dbsamples (Persistence > Objects)
triggers: ["RegisterLogDump", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — RegisterLogDump — código executável dbsamples (Persistence > Objects)

Classe Tutor: `RegisterLogDump`.
Ver no Tutor: `index.php?class=RegisterLogDump` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/RegisterLogDump.class.php`.


## Código

```php
<?php
class RegisterLogDump extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples'); // abre uma transação
            // screen dump (uncomment to save file)
            TTransaction::dump( /* '/tmp/log.txt' */ );  
            
            $cidade = new City; // cria novo objeto
            $cidade->name = 'Porto Alegre';
            $cidade->state_id = '1'; 
            $cidade->store(); // armazena o objeto
            
            new TMessage('info', 'Objeto armazenado com sucesso');
            TTransaction::close(); // fecha a transação.
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
