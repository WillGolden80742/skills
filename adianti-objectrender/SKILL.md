---
name: adianti-objectrender
description: ObjectRender — código executável dbsamples (Persistence > Objects)
triggers: ["ObjectRender", "digo", "execut", "vel", "dbsamples", "Persistence", "Objects", "exemplo executavel"]
---

# Skill Adianti — ObjectRender — código executável dbsamples (Persistence > Objects)

Classe Tutor: `ObjectRender`.
Ver no Tutor: `index.php?class=ObjectRender` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/ObjectRender.php`.


## Código

```php
<?php
class ObjectRender extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            TTransaction::open('samples');
            
            $product = Product::find(4);
            
            // render attributes inside braces
            echo $product->render('The product <b>{id}</b> is <u>{description}</u>');
            
            echo '<br>';
            
            // evaluate attributes inside braces
            echo $product->evaluate('= {sale_price} * {stock}');
            
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
