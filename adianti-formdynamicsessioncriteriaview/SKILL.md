---
name: adianti-formdynamicsessioncriteriaview
description: Dynamic criteria with session variable — Tutor Organization > Field interactions > Dynamic criteria with session variable
triggers: ["FormDynamicSessionCriteriaView", "Dynamic", "criteria", "with", "session", "variable", "Tutor", "Dynamic criteria with session variable", "Organization", "Field interactions"]
---

# Skill Adianti — Dynamic criteria with session variable — Tutor Organization > Field interactions > Dynamic criteria with session variable

Classe Tutor: `FormDynamicSessionCriteriaView`.
Ver no Tutor: `index.php?class=FormDynamicSessionCriteriaView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/Interactions/FormDynamicSessionCriteriaView.class.php`.


## Código

```php
<?php
/**
 * FormDynamicSessionCriteriaView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormDynamicSessionCriteriaView extends TPage
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
        $this->form = new BootstrapFormBuilder('form_hierarchical');
        $this->form->setFormTitle(_t('Hierarchical combo'));
        
        $city_id = new TDBCombo('city_id', 'samples', 'City', 'id', 'name', 'name');
        
        $filter = new TCriteria;
        $filter->add(new TFilter('city_id', '=', "'{session.city_id_filter}'"));
        
        $customer_id = new TDBUniqueSearch('customer_id', 'samples', 'Customer', 'id', 'name', 'name', $filter);
        
        $city_id->enableSearch();
        $customer_id->setMinLength(1);
        
        // add the fields inside the form
        $this->form->addFields( [new TLabel('City')],  [$city_id] );
        $this->form->addFields( [new TLabel('Customer')],  [$customer_id] );
        
        $city_id->setChangeAction( new TAction( array($this, 'onCityChange' )) );
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style='width:100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);

        parent::add($vbox);
    }
    
    /**
     * Action to be executed when the user changes the city
     * @param $param Action parameters
     */
    public static function onCityChange($param)
    {
        if (!empty($param['city_id']))
        {
            TSession::setValue('city_id_filter', $param['city_id']);
        }
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
