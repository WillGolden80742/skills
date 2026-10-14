---
name: adianti-executesample
description: ExecuteSample — código executável dbsamples (Tutor > Exemplos executáveis)
triggers: ["ExecuteSample", "digo", "execut", "vel", "dbsamples", "Tutor", "Exemplos executáveis", "exemplo executavel"]
---

# Skill Adianti — ExecuteSample — código executável dbsamples (Tutor > Exemplos executáveis)

Classe Tutor: `ExecuteSample`.
Ver no Tutor: `index.php?class=ExecuteSample` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ExecuteSample.class.php`.


## Código

```php
<?php
class ExecuteSample extends TPage
{
    public function __construct()
    {
        parent::__construct();
        
        try
        {
            /**
             * Aqui vai o cdigo
             */
             
            throw new Exception('sdf');
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
