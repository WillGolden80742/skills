---
name: adianti-formchecklistview
description: Check list — Tutor Presentation > Forms > Check list
triggers: ["FormCheckListView", "Check", "list", "Tutor", "Presentation", "Forms", "Check list"]
---

# Skill Adianti — Check list — Tutor Presentation > Forms > Check list

Classe Tutor: `FormCheckListView`.
Ver no Tutor: `index.php?class=FormCheckListView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormCheckListView.class.php`.


## Código

```php
<?php
/**
 * FormCheckListView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormCheckListView extends TPage
{
    private $form;
    
    public function __construct()
    {
        parent::__construct();
        
        $this->form = new BootstrapFormBuilder;
        $this->form->setFormTitle('Checklist');
        
        $customer  = new TDBUniqueSearch('customer_id', 'samples', 'Customer', 'id', 'name');
        $date      = new TDate('order_date');
        $orderlist = new TCheckList('order_list');
        
        $orderlist->setSelectAction( new TAction( [$this, 'onSelect'] ) );
        
        $customer->addValidation('Customer', new TRequiredValidator); // cannot be less the 3 characters
        $orderlist->addValidation('Order list', new TRequiredValidator); // cannot be less the 3 characters
        
        $customer->setMinLength(1);
        $orderlist->addColumn('id',          'Id',          'center',  '10%');
        $orderlist->addColumn('description', 'Description', 'left',    '50%');
        $sale_price = $orderlist->addColumn('sale_price',  'Price',       'right',    '40%');
        
        $orderlist->setHeight(250);
        $orderlist->makeScrollable();
        
        $format_value = function($value) {
            if (is_numeric($value)) {
                return 'R$ '.number_format($value, 2, ',', '.');
            }
            return $value;
        };
        
        $sale_price->setTransformer( $format_value );
        
        $this->form->addFields( [ new TLabel('Customer') ], [$customer] );
        $this->form->addFields( [ new TLabel('Date') ],     [$date] );
        
        $input_search = new TEntry('search');
        $input_search->placeholder = _t('Search');
        $input_search->setSize('100%');
        $orderlist->enableSearch($input_search, 'id, description');
        
        $hbox = new THBox;
        $hbox->style = 'border-bottom: 1px solid gray;padding-bottom:10px';
        $hbox->add( new TLabel('Order list') );
        $hbox->add( $input_search )->style = 'float:right;width:30%;';
        
        $total = new TElement('span');
        $total->id = 'total';
        $total->style = 'float:right;margin-right:10px;font-weight:bold;color: blue;font-size: 20pt;';
        $total->add('...');
        
        // load order items
        $orderlist->addItems( Product::allInTransaction('samples') );
        $this->form->addContent( [$hbox] );
        $this->form->addFields( [$orderlist] );
        $this->form->addContent( [$total] );
        
        $this->form->addAction( 'Save', new TAction([$this, 'onSave']), 'fa:save green');
        $this->form->addAction( 'Disable', new TAction([$this, 'onDisable']), 'fas:toggle-off orange');
        $this->form->addAction( 'Enable', new TAction([$this, 'onEnable']), 'fas:toggle-on orange');
        $this->form->addAction( 'Check All', new TAction([$this, 'onCheckAll']), 'fa:check');
        $this->form->addAction( 'Check None', new TAction([$this, 'onCheckNone']), 'far:square');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);

        parent::add($vbox);
    }
    
    /**
     * Enable check list
     */
    public static function onEnable($param)
    {
        TCheckList::enableField('order_list');
    }
    
    /**
     * Disable check list
     */
    public static function onDisable($param)
    {
        TCheckList::disableField('order_list');
    }
    
    /**
     * Check all
     */
    public static function onCheckAll($param)
    {
        TCheckList::checkAll('order_list', true);
    }
    
    /**
     * Check none
     */
    public static function onCheckNone($param)
    {
        TCheckList::checkNone('order_list', true);
    }
    
    /**
     * on select row
     */
    public static function onSelect($param)
    {
        new TMessage('info', str_replace(',', '<br>', json_encode($param)));
        
        $total = 0;
        if (!empty($param['order_list']))
        {
            TTransaction::open('samples');
            foreach ($param['order_list'] as $key)
            {
                $product = Product::find($key);
                if ($product)
                {
                    $total += $product->sale_price;
                }
            }
            TTransaction::close();
            
            $total = 'R$ '.number_format($total, 2, ',', '.');
            TScript::create("$('#total').html('{$total}')");
        }
        else
        {
            $total = 'R$ '.number_format(0, 2, ',', '.');
            TScript::create("$('#total').html('{$total}')");
        }
    }
    
    /**
     * Simulates an save button
     * Show the form content
     */
    public function onSave($param)
    {
        try
        {
            $data = $this->form->getData(); // optional parameter: active record class
            
            $this->form->validate();
            echo '<pre>';
            var_dump($data);
            echo '</pre>';
            
            // put the data back to the form
            $this->form->setData($data);
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
