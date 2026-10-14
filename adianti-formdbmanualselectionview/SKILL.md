---
name: adianti-formdbmanualselectionview
description: Manual database selections — Tutor Presentation > Extras > Manual database selections
triggers: ["FormDBManualSelectionView", "Manual", "database", "selections", "Tutor", "Presentation", "Extras", "Manual database selections"]
---

# Skill Adianti — Manual database selections — Tutor Presentation > Extras > Manual database selections

Classe Tutor: `FormDBManualSelectionView`.
Ver no Tutor: `index.php?class=FormDBManualSelectionView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormDBManualSelectionView.class.php`.


## Código

```php
<?php
/**
 * FormDBManualSelectionView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormDBManualSelectionView extends TPage
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
        $this->form = new BootstrapFormBuilder;
        $this->form->setFormTitle(_t('Manual database selections'));
        
        // create the form fields
        $radio    = new TRadioGroup('radio');
        $check    = new TCheckGroup('check');
        $combo    = new TCombo('combo');
        $select   = new TSelect('select');
        $search   = new TMultiSearch('search');
        $autocomp = new TEntry('autocomplete');
        
        $search->setMinLength(1);
        $radio->setLayout('horizontal');
        $check->setLayout('horizontal');
        
        // open database transaction
        TTransaction::open('samples');

        // load items from repository
        $collection = Category::all();
        
        // add the combo items
        $items = array();
        foreach ($collection as $object)
        {
            $items[$object->id] = $object->name;
        }
        TTransaction::close();
        
        $radio->addItems($items);
        $check->addItems($items);
        $combo->addItems($items);
        $select->addItems($items);
        $search->addItems($items);
        $autocomp->setCompletion( array_values( $items ));
        
        // adjust grid layout columns
        $this->form->setColumnClasses(2, ['col-sm-4', 'col-sm-8']);
        
        // add the fields to the form
        $this->form->addFields( [new TLabel('TRadioGroup:')],  [$radio] );
        $this->form->addFields( [new TLabel('TCheckGroup:')],  [$check] );
        $this->form->addFields( [new TLabel('TCombo:')],       [$combo] );
        $this->form->addFields( [new TLabel('TSelect:')],      [$select] );
        $this->form->addFields( [new TLabel('TMultiSearch (minlen 1):')], [$search] );
        $this->form->addFields( [new TLabel('Autocomplete:')], [$autocomp] );
        
        $select->setSize('100%', 70);
        $search->setSize('100%', 50);
        
        $this->form->addAction('Send', new TAction(array($this, 'onSend')), 'far:check-circle green');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);

        parent::add($vbox);
    }
    
    /**
     * Send data
     */
    public function onSend($param)
    {
        $data = $this->form->getData(); // optional parameter: active record class
        
        // put the data back to the form
        $this->form->setData($data);
        
        // creates a string with the form element's values
        $message = 'Radio : ' . $data->radio . '<br>';
        $message.= 'Check : ' . print_r($data->check, TRUE) . '<br>';
        $message.= 'Combo : ' . $data->combo . '<br>';
        $message.= 'Select : ' . print_r($data->select, TRUE) . '<br>';
        $message.= 'MultiSearch: ' . print_r($data->search, TRUE) . '<br>';
        $message.= 'Autocomplete: ' . $data->autocomplete;
        
        // show the message
        new TMessage('info', $message);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
