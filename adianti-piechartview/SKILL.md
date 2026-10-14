---
name: adianti-piechartview
description: Pie chart — Tutor Presentation > Charts > Pie chart
triggers: ["PieChartView", "Pie", "chart", "Tutor", "Presentation", "Charts", "Pie chart"]
---

# Skill Adianti — Pie chart — Tutor Presentation > Charts > Pie chart

Classe Tutor: `PieChartView`.
Ver no Tutor: `index.php?class=PieChartView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Chart/PieChartView.class.php`.


## Código

```php
<?php
/**
 * Chart
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class PieChartView extends TPage
{
    /**
     * Class constructor
     * Creates the page
     */
    public function __construct( $show_breadcrumb = true )
    {
        parent::__construct();
        
        $chart = new TPieChart;
        $chart->setTitle('Accesses by day');
        $chart->addSlice('Pedro', 80);
        $chart->addSlice('Maria', 60);
        $chart->addSlice('João',  60);
        
        $panel = new TPanelGroup;
        $panel->add($chart);
        
        // add the template to the page
        $container = new TVBox;
        $container->style = 'width: 100%';
        if ($show_breadcrumb)
        {
            $container->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        }
        $container->add($panel);
        parent::add($container);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
