---
name: adianti-messageview
description: MessageView — Tutor Presentation > Extras
triggers: ["MessageView", "Tutor", "Presentation", "Extras", "Message"]
---

# Skill Adianti — MessageView — Tutor Presentation > Extras

Classe Tutor: `MessageView`.
Ver no Tutor: `index.php?class=MessageView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extras/MessageView.class.php`.


## Código

```php
<?php
/**
 * MessageView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class MessageView extends TPage
{
    private $datagrid;
    
    public function __construct()
    {
        parent::__construct();
        
        // HERE: The #id of container of this page view
        parent::setTargetContainer('message_area');
        
        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        $this->datagrid->style = 'width: 100%';;
        
        // add the columns
        $this->datagrid->addColumn( new TDataGridColumn('subject', 'Subject', 'left') );
        $this->datagrid->addColumn( new TDataGridColumn('who',     'From',    'left') );
        $this->datagrid->addColumn( new TDataGridColumn('date',    'Date',    'left') );
        
        $this->datagrid->createModel();
        
        $panel = new TPanelGroup;
        $panel->style='margin:2px';
        $panel->add($this->datagrid);
        
        parent::add($panel);
    }
    
    public function onLoad($param)
    {
        if ($param['folder'] == 'Inbox')
        {
            $this->datagrid->addItem( (object) ['subject' => 'Inbox message 1',
                                                'who' => 'From 1',
                                                'date' => date('Y-m-d')]);
            
            $this->datagrid->addItem( (object) ['subject' => 'Inbox message 2',
                                                'who' => 'From 2',
                                                'date' => date('Y-m-d')]);
        }
        if ($param['folder'] == 'Sent')
        {
            $this->datagrid->addItem( (object) ['subject' => 'Sent message 1',
                                                'who' => 'To 1',
                                                'date' => date('Y-m-d')]);
            
            $this->datagrid->addItem( (object) ['subject' => 'Sent message 2',
                                                'who' => 'To 2',
                                                'date' => date('Y-m-d')]);
        }
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
