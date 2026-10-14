---
name: adianti-formseekbuttonview
description: Seek button — Tutor Presentation > Forms > Seek button
triggers: ["FormSeekButtonView", "Seek", "button", "Tutor", "Presentation", "Forms", "Seek button"]
---

# Skill Adianti — Seek button — Tutor Presentation > Forms > Seek button

Classe Tutor: `FormSeekButtonView`.
Ver no Tutor: `index.php?class=FormSeekButtonView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormSeekButtonView.class.php`.


## Código

```php
<?php
/**
 * FormSeekButtonView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormSeekButtonView extends TPage
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
        $this->form = new BootstrapFormBuilder('form_seek');
        $this->form->setFormTitle(_t('Seek button'));
        
        $city_id   = new TDBSeekButton('city_id', 'samples', 'form_seek', 'City', 'name');
        $city_name = new TEntry('city_name');
        $city_id->setAuxiliar($city_name);
        
        $criteria = new TCriteria;
        $criteria->add(new TFilter('id', '>=', 1));
        $criteria->add(new TFilter('id', '<=', 10));
        $criteria->setProperty('order', 'id');
        
        $customer_id   = new TDBSeekButton('customer_id', 'samples', 'form_seek', 'Customer', 'name');
        $customer_name = new TEntry('customer_name');
        $customer_id->setDisplayMask('{name} - {city->name} - {city->state->name}');
        $customer_id->setDisplayLabel('Informações do cliente');
        $customer_id->setAuxiliar($customer_name);
        
        $customer_id2   = new TDBSeekButton('product_id2', 'samples', 'form_seek', 'Customer', 'name');
        $customer_name2 = new TEntry('product_name2');
        $customer_id2->setCriteria($criteria);
        $customer_id2->setAuxiliar($customer_name2);
        
        $product_id = new TSeekButton('product_id');
        $product_name = new TEntry('product_name');
        
        
        $product_id->setAction( new TAction(['ProductSeek', 'onReload']) );
        $product_id->setAuxiliar($product_name);
         
        $city_name->setEditable(FALSE);
        $customer_name->setEditable(FALSE);
        $customer_name2->setEditable(FALSE);
        $product_name->setEditable(FALSE);
        
        // adjust grid layout columns
        $this->form->setColumnClasses(2, ['col-sm-3', 'col-sm-9']);
        
        // add form fields
        $this->form->addFields( [new TLabel('Standard Seek')],  [$city_id]);
        $this->form->addFields( [new TLabel('Standard with mask')],   [$customer_id]);
        $this->form->addFields( [new TLabel('Standard with filter')], [$customer_id2]);
        $this->form->addFields( [new TLabel('Custom Seek')], [$product_id]);
        
        $city_id->setSize(80);
        $customer_id->setSize(80);
        $customer_id2->setSize(80);
        $product_id->setSize(80);
        
        $city_name->setSize('calc(100% - 120px)');
        $customer_name->setSize('calc(100% - 120px)');
        $customer_name2->setSize('calc(100% - 120px)');
        $product_name->setSize('calc(100% - 120px)');
        $city_name->style .= ';margin-left:3px';
        $customer_name->style .= ';margin-left:3px';
        $customer_name2->style .= ';margin-left:3px';
        $product_name->style .= ';margin-left:3px';
        
        $this->form->addAction('Save', new TAction(array($this, 'onSave')), 'fa:save');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);

        parent::add($vbox);
    }
    
    /**
     * Simulates an save button
     * Show the form content
     */
    public function onSave($param)
    {
        $data = $this->form->getData(); // optional parameter: active record class
        
        // put the data back to the form
        $this->form->setData($data);
        
        // creates a string with the form element's values
        $message = 'City id : '     . $data->city_id . '<br>';
        $message.= 'Product id : '  . $data->product_id . '<br>';
        $message.= 'Customer id : ' . $data->customer_id . '<br>';
        
        // show the message
        new TMessage('info', $message);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
