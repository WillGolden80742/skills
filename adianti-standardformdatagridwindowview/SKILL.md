---
name: adianti-standardformdatagridwindowview
description: Standard Form/DataGrid with window — Tutor Organization > Standard controls > Standard Form/DataGrid with window
triggers: ["StandardFormDataGridWindowView", "Standard", "Form", "DataGrid", "with", "window", "Tutor", "Standard Form/DataGrid with window", "Organization", "Standard controls"]
---

# Skill Adianti — Standard Form/DataGrid with window — Tutor Organization > Standard controls > Standard Form/DataGrid with window

Classe Tutor: `StandardFormDataGridWindowView`.
Ver no Tutor: `index.php?class=StandardFormDataGridWindowView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/StandardControls/StandardFormDataGridWindowView.class.php`.


## Código

```php
<?php
/**
 * StandardFormDataGridWindowView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class StandardFormDataGridWindowView extends TPage
{
    protected $form;      // form
    protected $datagrid;  // datagrid
    protected $loaded;
    protected $pageNavigation;  // pagination component
    
    // trait with onSave, onEdit, onDelete, onReload, onSearch...
    use Adianti\Base\AdiantiStandardFormListTrait;
    
    /**
     * Class constructor
     * Creates the page, the form and the listing
     */
    public function __construct()
    {
        parent::__construct();
        
        $this->setDatabase('samples'); // define the database
        $this->setActiveRecord('Category'); // define the Active Record
        $this->setDefaultOrder('id', 'asc'); // define the default order
        $this->setLimit(-1); // turn off limit for datagrid
        
        $this->setAfterSaveAction( new TAction([$this, 'closeWindow' ]) );
        
        // create the form
        $this->form = new BootstrapFormBuilder('form_categories');
        // $this->form->setFormTitle(_t('Standard Form/DataGrid'));
        
        // create the form fields
        $id     = new TEntry('id');
        $name   = new TEntry('name');
        
        // add the form fields
        $this->form->addFields( [new TLabel('ID')],    [$id] );
        $this->form->addFields( [new TLabel('Name', 'red')],  [$name] );
        
        $name->addValidation('Name', new TRequiredValidator);
        
        // define the form actions
        $this->form->addAction( 'Save', new TAction([$this, 'onSave']), 'fa:save green');
        // $this->form->addActionLink( 'Clear',new TAction([$this, 'onClear']), 'fa:eraser red');
        
        // make id not editable
        $id->setEditable(FALSE);
        
        // create the datagrid
        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        $this->datagrid->width = '100%';
        
        // add the columns
        $col_id    = new TDataGridColumn('id', 'Id', 'right', '10%');
        $col_name  = new TDataGridColumn('name', 'Name', 'left', '90%');
        
        $this->datagrid->addColumn($col_id);
        $this->datagrid->addColumn($col_name);
        
        $col_id->setAction( new TAction([$this, 'onReload']),   ['order' => 'id']);
        $col_name->setAction( new TAction([$this, 'onReload']), ['order' => 'name']);
        
        // define row actions
        $action1 = new TDataGridAction([$this, 'onEditCurtain'],   ['key' => '{id}'] );
        $action2 = new TDataGridAction([$this, 'onDelete'], ['key' => '{id}'] );
        
        $this->datagrid->addAction($action1, 'Edit',   'far:edit blue');
        $this->datagrid->addAction($action2, 'Delete', 'far:trash-alt red');
        
        // create the datagrid model
        $this->datagrid->createModel();
        
        // wrap objects inside a table
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        
        //$vbox->add($this->form);
        
        $vbox->add($panel = TPanelGroup::pack('', $this->datagrid));
        
        // search box
        $input_search = new TEntry('input_search');
        $input_search->placeholder = _t('Search');
        $input_search->setSize('100%');
        
        // enable fuse search by column name
        $this->datagrid->enableSearch($input_search, 'id, name');
        $panel->addHeaderWidget($input_search);
        
        $panel->addHeaderActionLink(_t('New'), new TAction([$this, 'onEditCurtain']), 'fa:plus green');
        
        // pack the table inside the page
        parent::add($vbox);
    }
    
    /**
     *
     */
    public static function onEditCurtain($param = null) 
    {
        try
        {
            // create window
            $page = TWindow::create('Edit', 600, null);
            $page->removePadding();
            
            // instantiate self class, run method to populate
            $embed = new self($param);
            $embed->onEdit($param);
            
            // embed form and show window
            $page->add($embed->form);
            $page->setIsWrapped(true);
            $page->show();
        }
        catch (Exception $e) 
        {
            new TMessage('error', $e->getMessage());    
        }
    }
   
   
    /**
     * Close Windows
     */
    public static function closeWindow($param = null)
    {
        TWindow::closeWindow();
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
