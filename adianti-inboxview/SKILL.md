---
name: adianti-inboxview
description: Internal pages (inbox) — Tutor Presentation > Pages > Internal pages (inbox)
triggers: ["InboxView", "Internal", "pages", "inbox", "Tutor", "Presentation", "Internal pages (inbox)"]
---

# Skill Adianti — Internal pages (inbox) — Tutor Presentation > Pages > Internal pages (inbox)

Classe Tutor: `InboxView`.
Ver no Tutor: `index.php?class=InboxView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Pages/InboxView.class.php`.


## Código

```php
<?php
/**
 * InboxView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class InboxView extends TPage
{
    private $datagrid;
    
    public function __construct()
    {
        parent::__construct();
        
        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        $this->datagrid->style = 'width: 100%';
        $this->datagrid->addColumn( new TDataGridColumn('folder',  'Folder',  'left') );
        
        $action = new TDataGridAction(array('MessageView', 'onLoad'), ['folder' => '{folder}']);
        $action->setParameter('register_state', 'false');
        $this->datagrid->addAction($action, 'View', 'far:folder-open');
        
        $this->datagrid->createModel();
        
        $this->datagrid->addItem( (object) ['folder' => 'Inbox']);
        $this->datagrid->addItem( (object) ['folder' => 'Sent']);
        
        $panel = new TPanelGroup;
        $panel->add($this->datagrid);
        $panel->style='width:150px;float:left;margin:2px';
        
        // HERE: Prepare an area (message_area) to render MessageView
        $message_area = new TElement('div');
        $message_area->id = 'message_area';
        $message_area->style = "float:left;width:70%;height:200px;border:1px dashed orange";
        
        $div = new TElement('div');
        $div->style = 'width:90%;float:left';
        $div->add( $panel );
        $div->add( $message_area );
        
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
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
