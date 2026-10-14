---
name: adianti-dashboardview
description: Dashboard — Tutor Presentation > Charts > Dashboard
triggers: ["DashboardView", "Dashboard", "Tutor", "Presentation", "Charts"]
---

# Skill Adianti — Dashboard — Tutor Presentation > Charts > Dashboard

Classe Tutor: `DashboardView`.
Ver no Tutor: `index.php?class=DashboardView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Chart/DashboardView.class.php`.


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
class DashboardView extends TPage
{
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        
        $div = new TElement('div');
        $div->class = "row";
        
        $indicator1 = new TNumericIndicator;
        $indicator2 = new TNumericIndicator;
        
        $indicator1->setTitle('Access');
        $indicator1->setValue(100);
        $indicator1->setIcon('sign-in-alt');
        $indicator1->setColor('green');
        $indicator1->setNumericMask(0, ',', '.');
        
        $indicator2->setTitle('Users');
        $indicator2->setValue(200);
        $indicator2->setIcon('users');
        $indicator2->setColor('orange');
        $indicator2->setNumericMask(0, ',', '.');
        
        $div->add( $i1 = TElement::tag('div', $indicator1) );
        $div->add( $i2 = TElement::tag('div', $indicator2) );
        
        $div->add( $g1 = new BarChartView(false) );
        $div->add( $g2 = new LineChartView(false) );
        $div->add( $g3 = new ColumnChartView(false) );
        $div->add( $g4 = new PieChartView(false) );
        
        $i1->class = 'col-sm-6';
        $i2->class = 'col-sm-6';
        $g1->class = 'col-sm-6';
        $g2->class = 'col-sm-6';
        $g3->class = 'col-sm-6';
        $g4->class = 'col-sm-6';
        
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($div);
        
        parent::add($vbox);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
