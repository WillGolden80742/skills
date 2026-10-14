---
name: adianti-manualdmlcommandsview
description: Low level DML commands — Tutor Persistence > Connections > Low level DML commands
triggers: ["ManualDMLCommandsView", "Low", "level", "DML", "commands", "Tutor", "Persistence", "Low level DML commands", "Connections"]
---

# Skill Adianti — Low level DML commands — Tutor Persistence > Connections > Low level DML commands

Classe Tutor: `ManualDMLCommandsView`.
Ver no Tutor: `index.php?class=ManualDMLCommandsView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Persistence/Setup/ManualDMLCommandsView.php`.


## Código

```php
<?php
/**
 * ManualDMLCommandsView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class ManualDMLCommandsView extends TPage
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
        $wrapper1 = new TElement('div');
        $wrapper2 = new TElement('div');
        $wrapper3 = new TElement('div');
        $wrapper4 = new TElement('div');
        $wrapper5 = new TElement('div');
        
        $wrapper1->class = 'sourcecodewrapper';
        $wrapper2->class = 'sourcecodewrapper';
        $wrapper3->class = 'sourcecodewrapper';
        $wrapper4->class = 'sourcecodewrapper';
        $wrapper5->class = 'sourcecodewrapper';
        
        $source1 = new TSourceCode;
        $source2 = new TSourceCode;
        $source3 = new TSourceCode;
        $source4 = new TSourceCode;
        $source5 = new TSourceCode;
        
        $wrapper1->add($source1);
        $wrapper2->add($source2);
        $wrapper3->add($source3);
        $wrapper4->add($source4);
        $wrapper5->add($source5);
        
        $source1->loadString("<?php
\$source = TTransaction::open('source');

// transformation function
\$double_function  = function (\$value, \$row) {
        return \$value  * 2;
};

// mapping rules between source query and the target table
\$mapping = [];
\$mapping[] = [ 'customer_id', 'cliente_id' ];
\$mapping[] = [ 'valor',       'valor_total', \$double_function ];

// define the query
\$query = \"SELECT customer_id as \\\"customer_id\\\",
                 sum(total) as \\\"valor\\\"
            FROM sale
           WHERE date >= ?
        GROUP BY 1\";

\$raw_data = TDatabase::getData(\$source, \$query, \$mapping, ['2015-01-01']);");
        
        $source2->loadString("<?php
\$conn = TTransaction::open('samples');
TDatabase::insertData(\$conn, 'city', [ 'id' => 1, 'name' => 'New York' ]);
TTransaction::close();");
        
        $source3->loadString("<?php
\$conn = TTransaction::open('samples');
\$criteria = TCriteria::create( [ 'vendor_id' => 10 ] );
\$values = [ 'obs' => 'new obs' ];
TDatabase::updateData(\$conn, 'product', \$values, \$criteria);
TTransaction::close();");
        
        $source4->loadString("<?php
\$conn = TTransaction::open('samples');
TDatabase::clearData(\$conn, 'city');
TTransaction::close();");

        $source5->loadString("<?php
\$conn = TTransaction::open('samples');
TDatabase::execute(\$conn, \"UPDATE product set sale_price = sale_price * 1.3\");
TTransaction::close();");

        // wrap the page content
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add(new TLabel('Get data'));
        $vbox->add($wrapper1);
        $vbox->add(new TLabel('Insert data'));
        $vbox->add($wrapper2);
        $vbox->add(new TLabel('Update data'));
        $vbox->add($wrapper3);
        $vbox->add(new TLabel('Clear data'));
        $vbox->add($wrapper4);
        $vbox->add(new TLabel('Execute'));
        $vbox->add($wrapper5);
        
        parent::add($vbox);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
