---
name: adianti-manualddlcommandsview
description: Low level DDL commands — Tutor Persistence > Connections > Low level DDL commands
triggers: ["ManualDDLCommandsView", "Low", "level", "DDL", "commands", "Tutor", "Persistence", "Low level DDL commands", "Connections"]
---

# Skill Adianti — Low level DDL commands — Tutor Persistence > Connections > Low level DDL commands

Classe Tutor: `ManualDDLCommandsView`.
Ver no Tutor: `index.php?class=ManualDDLCommandsView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Persistence/Setup/ManualDDLCommandsView.php`.


## Código

```php
<?php
/**
 * ManualDDLCommandsView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class ManualDDLCommandsView extends TPage
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
\$conn = TTransaction::open('samples');
TDatabase::dropTable(\$conn, 'city', true);
TTransaction::close();");
        
        $source2->loadString("<?php
\$conn = TTransaction::open('samples');
TDatabase::createTable(\$conn, 'city', [ 'id' => 'int', 'name' => 'varchar(100)']);
TTransaction::close();");
        
        $source3->loadString("<?php
\$conn = TTransaction::open('samples');
TDatabase::addColumn(\$conn, 'city', 'obs', 'varchar(100)', '');
TTransaction::close();");
        
        $source4->loadString("<?php
\$conn = TTransaction::open('samples');
TDatabase::dropColumn(\$conn, 'city', 'obs');
TTransaction::close();");

        $source5->loadString("<?php
\$conn = TTransaction::open('samples');
TDatabase::execute(\$conn, \"CREATE INDEX city_name_idx ON city(name)\");
TTransaction::close();");

        // wrap the page content
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add(new TLabel('Drop table'));
        $vbox->add($wrapper1);
        $vbox->add(new TLabel('Create table'));
        $vbox->add($wrapper2);
        $vbox->add(new TLabel('Add column'));
        $vbox->add($wrapper3);
        $vbox->add(new TLabel('Drop column'));
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
