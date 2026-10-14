---
name: adianti-formdynamicfilterview
description: Dynamic filtering — Tutor Organization > Field interactions > Dynamic filtering
triggers: ["FormDynamicFilterView", "Dynamic", "filtering", "Tutor", "Organization", "Field", "interactions", "Dynamic filtering", "Field interactions"]
---

# Skill Adianti — Dynamic filtering — Tutor Organization > Field interactions > Dynamic filtering

Classe Tutor: `FormDynamicFilterView`.
Ver no Tutor: `index.php?class=FormDynamicFilterView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/Interactions/FormDynamicFilterView.class.php`.


## Código

```php
<?php
/**
 * FormDynamicFilterView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormDynamicFilterView extends TPage
{
    private $form;
    
    /**
     * Class constructor
     * Creates the page
     */
    function __construct()
    {
        parent::__construct();
        
        // create the form
        $this->form = new BootstrapFormBuilder('form_dynamic_filter');
        $this->form->setFormTitle('Dynamic Filtering');
        
        $check_gender = new TCheckGroup('check_gender');
        $check_gender->addItems( array('M'=>'Male', 'F'=>'Female') );
        $check_gender->setLayout('horizontal');
        
        $combo_status = new TCombo('combo_status');
        $combo_status->addItems(array('S'=>'Single', 'C'=>'Committed', 'M'=>'Married') );
        
        $combo_customers = new TCombo('customers');
        
        // add the fields inside the form
        $this->form->addFields(['Load customers'],  [$check_gender] );
        $this->form->addFields([''],  [$combo_status] );
        $this->form->addFields([''],  [$combo_customers] );
        
        $check_gender->setChangeAction( new TAction( array($this, 'onGenderChange' )) );
        $combo_status->setChangeAction( new TAction( array($this, 'onGenderChange' )) );
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);

        parent::add($vbox);
    }
    
    /**
     * Action to be executed when the user changes the gender or status
     * @param $param Action parameters
     */
    public static function onGenderChange($param)
    {
        TTransaction::open('samples');
        $repo = new TRepository('Customer');
        $criteria = new TCriteria;
        if (isset($param['check_gender']))
        {
            $criteria->add(new TFilter('gender', 'IN',  $param['check_gender']));
        }
        
        if ($param['combo_status'])
        {
            $criteria->add(new TFilter('status', '=', $param['combo_status']));
        }
        
        $customers = $repo->load($criteria);
        TTransaction::close();
        
        $options = array();
        foreach ($customers as $customer)
        {
            $options[ $customer->id] = $customer->name;
        }
        
        TCombo::reload('form_dynamic_filter', 'customers', $options);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
