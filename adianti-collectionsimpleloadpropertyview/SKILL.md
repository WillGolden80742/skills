---
name: adianti-collectionsimpleloadpropertyview
description: Collection simple paginated load — Tutor Persistence > Collections > Collection simple paginated load
triggers: ["CollectionSimpleLoadPropertyView", "Collection", "simple", "paginated", "load", "Tutor", "Persistence", "Collection simple paginated load", "Collections"]
---

# Skill Adianti — Collection simple paginated load — Tutor Persistence > Collections > Collection simple paginated load

Classe Tutor: `CollectionSimpleLoadPropertyView`.
Ver no Tutor: `index.php?class=CollectionSimpleLoadPropertyView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Persistence/Collections/CollectionSimpleLoadPropertyView.class.php`.


## Código

```php
<?php
/**
 * CollectionSimpleLoadPropertyView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class CollectionSimpleLoadPropertyView extends TPage
{
    public function __construct()
    {
        // parent classs constructor
        parent::__construct();
        
        $config = AdiantiApplicationConfig::get();
        ini_set('highlight.comment', $config['highlight']['comment']);
        ini_set('highlight.default', $config['highlight']['default']);
        ini_set('highlight.html',    $config['highlight']['html']);
        ini_set('highlight.keyword', $config['highlight']['keyword']);
        ini_set('highlight.string',  $config['highlight']['string']);
        
        // scroll to put the source inside
        $wrapper = new TElement('div');
        $wrapper->class = 'sourcecodewrapper';
        
        $source = new TSourceCode;
        $source->loadFile('app/resources/Persistence/Collections/CollectionSimpleLoadProperty.php');
        $wrapper->add($source);
        
        // wrap the page content
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($wrapper);
        parent::add($vbox);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
