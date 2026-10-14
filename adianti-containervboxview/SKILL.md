---
name: adianti-containervboxview
description: Vertical Box — Tutor Presentation > Containers > Vertical Box
triggers: ["ContainerVBoxView", "Vertical", "Box", "Tutor", "Presentation", "Containers", "Vertical Box"]
---

# Skill Adianti — Vertical Box — Tutor Presentation > Containers > Vertical Box

Classe Tutor: `ContainerVBoxView`.
Ver no Tutor: `index.php?class=ContainerVBoxView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Containers/ContainerVBoxView.class.php`.


## Código

```php
<?php
/**
 * ContainerVBoxView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class ContainerVBoxView extends TPage
{
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        $notebook1 = new TNotebook;
        $notebook2 = new TNotebook;
        
        $notebook1->appendPage('page1', new TLabel('Page 1'));
        $notebook1->appendPage('page2', new TLabel('Page 2'));
        
        $notebook2->appendPage('page1', new TLabel('Page 1'));
        $notebook2->appendPage('page2', new TLabel('Page 2'));
        
        $notebook1->setSize(null,100);
        $notebook2->setSize(null,100);
        
        // creates the vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($notebook1);
        $vbox->add($notebook2);
        
        parent::add(TPanelGroup::pack('',$vbox));
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
