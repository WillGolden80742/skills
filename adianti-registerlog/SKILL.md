---
name: adianti-registerlog
description: RegisterLog — código executável dbsamples (Persistence > Objects)
triggers: ["RegisterLog", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — RegisterLog — código executável dbsamples (Persistence > Objects)

Classe Tutor: `RegisterLog`.
Ver no Tutor: `index.php?class=RegisterLog` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/RegisterLog.class.php`.


## Código

```php
<?php
class RegisterLog extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples'); // abre uma transao
            // define o log
            TTransaction::setLogger(new TLoggerTXT('/tmp/log.txt'));
            TTransaction::log("** inserindo cidade");
            
            $cidade = new City; // cria novo objeto
            $cidade->name = 'Porto Alegre';
            $cidade->state_id = '1'; 
            $cidade->store(); // armazena o objeto
            
            new TMessage('info', 'Objeto armazenado com sucesso');
            TTransaction::close(); // fecha a transao.
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
