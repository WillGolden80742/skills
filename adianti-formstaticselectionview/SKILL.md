---
name: adianti-formstaticselectionview
description: Static selections — Tutor Presentation > Forms > Static selections
triggers: ["FormStaticSelectionView", "Static", "selections", "Tutor", "Presentation", "Forms", "Static selections"]
---

# Skill Adianti — Static selections — Tutor Presentation > Forms > Static selections

Classe Tutor: `FormStaticSelectionView`.
Ver no Tutor: `index.php?class=FormStaticSelectionView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormStaticSelectionView.class.php`.


## Código

```php
<?php
/**
 * FormStaticSelectionView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormStaticSelectionView extends TPage
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
        $this->form = new BootstrapFormBuilder('form_selectors');
        $this->form->setFormTitle(_t('Static selections'));
        $this->form->generateAria();
        
        // create the form fields
        $radio    = new TRadioGroup('radio');
        $radio2   = new TRadioGroup('radio2');
        $check    = new TCheckGroup('check');
        $check2   = new TCheckGroup('check2');
        $check3   = new TCheckButton('check3');
        $combo    = new TCombo('combo');
        $combo2   = new TCombo('combo2');
        $select   = new TSelect('select');
        $mcombo   = new TMultiCombo('mcombo');
        $search   = new TMultiSearch('search');
        $unique   = new TUniqueSearch('unique');
        $multi    = new TMultiEntry('multi');
        $autocomp = new TEntry('autocomplete');
        
        $radio->setLayout('horizontal');
        $radio2->setLayout('horizontal');
        $check->setLayout('horizontal');
        $check2->setLayout('horizontal');
        $radio2->setUseButton();
        $check2->setUseButton();
        $combo2->enableSearch();
        $search->setMinLength(1);
        $unique->setMinLength(1);
        $search->setMaxSize(3);
        $multi->setMaxSize(3);
        $check3->setIndexValue(1);
        $check3->setUseSwitch(true, 'blue');
        
        $items = ['a'=>'Item a', 'b'=>'Item b', 'c'=>'Item c'];
        
        $radio->addItems($items);
        $check->addItems($items);
        $radio2->addItems($items);
        $check2->addItems($items);
        $combo->addItems($items);
        $combo2->addItems($items);
        $select->addItems($items);
        $mcombo->addItems($items);
        $search->addItems($items);
        $unique->addItems($items);
        $autocomp->setCompletion( array_values( $items ));
        
        foreach ($radio2->getLabels() as $key => $label)
        {
            $label->setTip("Radio $key");
        }
        foreach ($check2->getLabels() as $key => $label)
        {
            $label->setTip("Check $key");
        }
        
        // define default values
        $radio->setValue('b');
        $radio2->setValue('b');
        $check->setValue( array('a', 'c'));
        $check2->setValue( array('a', 'c'));
        $combo->setValue('b');
        $combo2->setValue('b');
        $select->setValue(array('a', 'b'));
        $mcombo->setValue(array('a', 'b'));
        $search->setValue(array('a', 'c'));
        $unique->setValue(array('b'));
        $multi->setValue(array('aaa','bbb'));
        $select->setSize('100%',100);
        $mcombo->setSize('100%');
        $search->setSize('100%',70);
        $multi->setSize('100%');
        
        // adjust grid layout columns
        $this->form->setColumnClasses(2, ['col-sm-4', 'col-sm-8']);
        
        $this->form->addFields( [new TLabel('TRadioGroup:')],  [$radio] );
        $this->form->addFields( [new TLabel('TCheckGroup:')],  [$check] );
        $this->form->addFields( [new TLabel('TRadioGroup (use button):')], [$radio2] );
        $this->form->addFields( [new TLabel('TCheckGroup (use button):')], [$check2] );
        $this->form->addFields( [new TLabel('TCheckButton (switch):')], [$check3] );
        $this->form->addFields( [new TLabel('TCombo:')],      [$combo] );
        $this->form->addFields( [new TLabel('TCombo (with search):')], [$combo2] );
        $this->form->addFields( [new TLabel('TSelect:')],      [$select] );
        $this->form->addFields( [new TLabel('TMultiCombo:')],  [$mcombo] );
        $this->form->addFields( [new TLabel('TMultiSearch:')], [$search] );
        $this->form->addFields( [new TLabel('TUniqueSearch:')],[$unique] );
        $this->form->addFields( [new TLabel('TMultiEntry:')],  [$multi] );
        $this->form->addFields( [new TLabel('Autocomplete:')], [$autocomp] );
        
        $this->form->addAction('Send', new TAction(array($this, 'onSend')), 'far:check-circle green');
        $this->form->addAction('Change options', new TAction(array($this, 'onChangeOptions')), 'fas:sync orange');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);

        parent::add($vbox);
    }
    
    /**
     * Reload options
     */
    public static function onChangeOptions($param)
    {
        $items = ['a'=>'Item a', 'b'=>'Item b', 'c'=>'Item c', 'd' => 'Item d'];
        TRadioGroup::reload('form_selectors', 'radio', $items, ['layout'=> 'horizontal']);
        TCheckGroup::reload('form_selectors', 'check', $items, ['layout'=> 'horizontal']);
        TRadioGroup::reload('form_selectors', 'radio2', $items, ['layout'=> 'horizontal', 'useButton' => true]);
        TCheckGroup::reload('form_selectors', 'check2', $items, ['layout'=> 'horizontal', 'useButton' => true]);
        TCombo::reload('form_selectors', 'combo', array_merge([ '' => ''], $items));
        TCombo::reload('form_selectors', 'combo2', array_merge([ '' => ''], $items));
        TSelect::reload('form_selectors', 'select', array_merge([ '' => ''], $items));
        TMultiCombo::reload('form_selectors', 'mcombo', $items);
    }
     
    /**
     * Send data
     */
    public function onSend($param)
    {
        $data = $this->form->getData(); // optional parameter: active record class
        //echo '<pre>';var_dump($data);echo '</pre>';
        
        // put the data back to the form
        $this->form->setData($data);
        
        // creates a string with the form element's values
        $message = 'Radio : ' . $data->radio . '<br>';
        $message.= 'Check : ' . print_r($data->check, TRUE) . '<br>';
        $message.= 'Radio (button) : ' . $data->radio2 . '<br>';
        $message.= 'Check (button) : ' . print_r($data->check2, TRUE) . '<br>';
        $message.= 'Check (switch) : ' . $data->check3 . '<br>';
        $message.= 'Combo : ' . $data->combo . '<br>';
        $message.= 'Combo2 : '. $data->combo2 . '<br>';
        $message.= 'Select: ' . print_r($data->select, TRUE) . '<br>';
        $message.= 'Multi combo: ' . print_r($data->mcombo, TRUE) . '<br>';
        $message.= 'Search: ' . print_r($data->search, TRUE) . '<br>';
        $message.= 'Unique: '. print_r($data->unique, TRUE) . '<br>';
        $message.= 'Multi: ' . print_r($data->multi, TRUE) . '<br>';
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
