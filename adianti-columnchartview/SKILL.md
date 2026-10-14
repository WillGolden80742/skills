---
name: adianti-columnchartview
description: Column chart — Tutor Presentation > Charts > Column chart
triggers: ["ColumnChartView", "Column", "chart", "Tutor", "Presentation", "Charts", "Column chart"]
---

# Skill Adianti — Column chart — Tutor Presentation > Charts > Column chart

Classe Tutor: `ColumnChartView`.
Ver no Tutor: `index.php?class=ColumnChartView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Chart/ColumnChartView.class.php`.


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
class ColumnChartView extends TPage
{
    /**
     * Class constructor
     * Creates the page
     */
    public function __construct( $show_breadcrumb = true )
    {
        parent::__construct();
        
        $chart = new TBarChart;
        $chart->makeHorizontal();
        $chart->setTitle('Accesses by day');
        $chart->setXLabels(['Day 1', 'Day 2', 'Day 3']);
        $chart->addDataset('Value 1', [100,120,140]);
        $chart->addDataset('Value 2', [120,140,160]);
        $chart->addDataset('Value 3', [140,160,180]);
        
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
