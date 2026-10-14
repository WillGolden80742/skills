---
name: adianti-carouselview
description: Carousel — Tutor Presentation > Templates > Carousel
triggers: ["CarouselView", "Carousel", "Tutor", "Presentation", "Templates"]
---

# Skill Adianti — Carousel — Tutor Presentation > Templates > Carousel

Classe Tutor: `CarouselView`.
Ver no Tutor: `index.php?class=CarouselView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extending/CarouselView.class.php`.


## Código

```php
<?php
/**
 * CarouselView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class CarouselView extends TPage
{
    /**
     * Page constructor
     */
    function __construct()
    {
        parent::__construct();
        
        $images = [];
        $images[] = ['index' => '0', 'image' => "app/images/nature/nature1.jpg", 'caption' => 'Image 1', 'class' => 'active'];
        $images[] = ['index' => '1', 'image' => "app/images/nature/nature2.jpg", 'caption' => 'Image 1', 'class' => ''];
        $images[] = ['index' => '2', 'image' => "app/images/nature/nature3.jpg", 'caption' => 'Image 1', 'class' => ''];
        $images[] = ['index' => '3', 'image' => "app/images/nature/nature4.jpg", 'caption' => 'Image 1', 'class' => ''];
        
        $html = new THtmlRenderer('app/resources/carousel.html');
        $html->enableSection('main', []);
        $html->enableSection('indicator', $images, true);
        $html->enableSection('slide', $images, true);
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        //$vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($html);
        
        parent::add($vbox);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
