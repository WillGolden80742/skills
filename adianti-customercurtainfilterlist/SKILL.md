---
name: adianti-customercurtainfilterlist
description: Curtain filters — Tutor Organization > Complete registrations > Curtain filters
triggers: ["CustomerCurtainFilterList", "Curtain", "filters", "Tutor", "Organization", "Complete", "registrations", "Curtain filters", "Complete registrations"]
---

# Skill Adianti — Curtain filters — Tutor Organization > Complete registrations > Curtain filters

Classe Tutor: `CustomerCurtainFilterList`.
Ver no Tutor: `index.php?class=CustomerCurtainFilterList` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/CompleteRegistrations/CustomerCurtainFilterList.class.php`.


## Código

```php
<?php
/**
 * CustomerCurtainFilterList
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class CustomerCurtainFilterList extends TPage
{
    protected $datagrid; // listing
    protected $pageNavigation;
    protected $deleteButton;
    
    use Adianti\base\AdiantiStandardListTrait;
    
    /**
     * Page constructor
     */
    public function __construct()
    {
        parent::__construct();
        
        $this->setDatabase('samples');            // defines the database
        $this->setActiveRecord('Customer');   // defines the active record
        $this->setDefaultOrder('id', 'asc');         // defines the default order
        $this->setLimit(10);
        // $this->setCriteria($criteria) // define a standard filter

        $this->addFilterField('id', '=', 'id'); // filterField, operator, formField
        $this->addFilterField('name', 'like', 'name'); // filterField, operator, formField
        $this->addFilterField('address', 'like', 'address'); // filterField, operator, formField
        $this->addFilterField('gender', 'like', 'gender'); // filterField, operator, formField
        $this->addFilterField('city_id', '=', 'city_id'); // filterField, operator, formField
        
        // creates the form
        $this->form = new BootstrapFormBuilder('form_search_Customer');
        $this->form->setFormTitle('Customer');
        

        // create the form fields
        $id = new TEntry('id');
        $name = new TEntry('name');
        $address = new TEntry('address');
        $gender = new TCombo('gender');
        $city_id = new TDBUniqueSearch('city_id', 'samples', 'City', 'id', 'name');

        $gender->addItems( [ 'M' => 'Male', 'F' => 'Female' ] );
        
        // add the fields
        $this->form->addFields( [ new TLabel('Id') ], [ $id ] );
        $this->form->addFields( [ new TLabel('Name') ], [ $name ] );
        $this->form->addFields( [ new TLabel('Address') ], [ $address ] );
        $this->form->addFields( [ new TLabel('Gender') ], [ $gender ] );
        $this->form->addFields( [ new TLabel('City Id') ], [ $city_id ] );


        // set sizes
        $id->setSize('100%');
        $name->setSize('100%');
        $address->setSize('100%');
        $gender->setSize('100%');
        $city_id->setSize('100%');

        
        // keep the form filled during navigation with session data
        $this->form->setData( TSession::getValue(__CLASS__.'_filter_data') );
        
        // add the search form actions
        $btn = $this->form->addAction(_t('Find'), new TAction([$this, 'onSearch']), 'fa:search');
        $btn->class = 'btn btn-sm btn-primary';
        
        // creates a Datagrid
        $this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
        $this->datagrid->style = 'width: 100%';
        

        // creates the datagrid columns
        $column_id = new TDataGridColumn('id', 'Id', 'center');
        $column_name = new TDataGridColumn('name', 'Name', 'left');
        $column_address = new TDataGridColumn('address', 'Address', 'left');
        $column_phone = new TDataGridColumn('phone', 'Phone', 'left');
        $column_gender = new TDataGridColumn('gender', 'Gender', 'center');
        $column_city_id = new TDataGridColumn('{city->name} ({city->state->name})', 'City Id', 'left');
        
        $column_gender->setTransformer( function ($value) {
            return $value == 'F' ? 'Female' : 'Male';
        });
        
        // add the columns to the DataGrid
        $this->datagrid->addColumn($column_id);
        $this->datagrid->addColumn($column_name);
        $this->datagrid->addColumn($column_address);
        $this->datagrid->addColumn($column_phone);
        $this->datagrid->addColumn($column_gender);
        $this->datagrid->addColumn($column_city_id);

        
        $action1 = new TDataGridAction(['CustomerFormView', 'onEdit'], ['id'=>'{id}', 'register_state' => 'false']);
        $action2 = new TDataGridAction([$this, 'onDelete'], ['id'=>'{id}', 'register_state' => 'false']);
        
        $this->datagrid->addAction($action1, _t('Edit'),   'far:edit blue');
        $this->datagrid->addAction($action2 ,_t('Delete'), 'far:trash-alt red');
        
        // create the datagrid model
        $this->datagrid->createModel();
        
        // creates the page navigation
        $this->pageNavigation = new TPageNavigation;
        $this->pageNavigation->setAction(new TAction([$this, 'onReload']));
        
        $panel = new TPanelGroup('');
        $panel->add($this->datagrid);
        $panel->addFooter($this->pageNavigation);
        
        $panel->addHeaderActionLink(_t('New'), new TAction(['CustomerFormView', 'onEdit'], ['register_state' => 'false']), 'fa:plus green');
        $btn = $panel->addHeaderActionLink('Filtros', new TAction([$this, 'onShowCurtainFilters']), 'fa:filter');
        $btn->class = 'btn btn-primary';
        
        
        // header actions
        $dropdown = new TDropDown(_t('Export'), 'fa:list');
        $dropdown->setPullSide('right');
        $dropdown->setButtonClass('btn btn-default waves-effect dropdown-toggle');
        $dropdown->addAction( _t('Save as CSV'), new TAction([$this, 'onExportCSV'], ['register_state' => 'false', 'static'=>'1']), 'fa:table blue' );
        $dropdown->addAction( _t('Save as PDF'), new TAction([$this, 'onExportPDF'], ['register_state' => 'false', 'static'=>'1']), 'far:file-pdf red' );
        $panel->addHeaderWidget( $dropdown );
        
        // vertical box container
        $container = new TVBox;
        $container->style = 'width: 100%';
        $container->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        //$container->add($this->form);
        $container->add($panel);
        
        parent::add($container);
    }
    
    /**
     *
     */
    public static function onShowCurtainFilters($param = null)
    {
        try
        {
            // create empty page for right panel
            $page = TPage::create();
            $page->setTargetContainer('adianti_right_panel');
            $page->setProperty('override', 'true');
            $page->setPageName(__CLASS__);
            
            $btn_close = new TButton('closeCurtain');
            $btn_close->onClick = "Template.closeRightPanel();";
            $btn_close->setLabel("Fechar");
            $btn_close->setImage('fas:times red');
            
            // instantiate self class, populate filters in construct 
            $embed = new self;
            $embed->form->addHeaderWidget($btn_close);
            
            // embed form inside curtain
            $page->add($embed->form);
            $page->show();
        }
        catch (Exception $e) 
        {
            new TMessage('error', $e->getMessage());    
        }
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
