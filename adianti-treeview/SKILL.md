---
name: adianti-treeview
description: Tree View — Tutor Presentation > Utilities > Tree View
triggers: ["TreeView", "Tree", "View", "Tutor", "Presentation", "Utilities", "Tree View"]
---

# Skill Adianti — Tree View — Tutor Presentation > Utilities > Tree View

Classe Tutor: `TreeView`.
Ver no Tutor: `index.php?class=TreeView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Widgets/TreeView.class.php`.


## Código

```php
<?php
/**
 * TreeView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class TreeView extends TPage
{
    private $form;
    
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        // define the tree data
        $data = array();
        $data['Brazil']['RS'][10] = 'Lajeado';
        $data['Brazil']['RS'][20] = 'Cruzeiro do Sul';
        $data['Brazil']['RS'][30] = 'Porto Alegre';
        $data['Brazil']['SP'][40] = 'São Paulo';
        $data['Brazil']['SP'][50] = 'Osasco';
        $data['Brazil']['MG'][60] = 'Belo Horizonte';
        $data['Brazil']['MG'][70] = 'Ipatinga';
        
        // scroll around the treeview
        $scroll = new TScroll;
        $scroll->setSize(300, 400);
        $scroll->style = 'margin-right: 5px';
        
        // creates the treeview
        $treeview = new TTreeView;
        //$treeview->collapse();
        $treeview->setSize(290);
        $treeview->setItemAction(new TAction(array($this, 'onSelect')));
        $treeview->fromArray($data); // fill the treeview
        
        $scroll->add($treeview);
        
        // creates a simple form
        $this->form = new BootstrapFormBuilder('form_test');
        $this->form->setFormTitle('Form');
        
        // creates the form fields
        $key   = new TEntry('key');
        $value = new TEntry('value');
        
        $this->form->addContent( [new TLabel('Key')] );
        $this->form->addFields( [$key] );
        $this->form->addContent( [new TLabel('Value')] );
        $this->form->addFields( [$value] );
        
        // pack treeview and form
        $hbox = THBox::pack($scroll, $this->form);
        $hbox->style = 'display:inline-flex';
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($hbox);

        parent::add($vbox);
    }
    
    /**
     * Executed when the user clicks at a tree node
     * @param $param URL parameters containing key and value
     */
    public static function onSelect($param)
    {
        $obj = new StdClass;
        $obj->key = $param['key']; // get node key (index)
        $obj->value = $param['value']; // get node value (contend)
        
        // fill the form with this object attributes
        TForm::sendData('form_test', $obj);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
