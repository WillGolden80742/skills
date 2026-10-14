---
name: adianti-formenabledisableview
description: Enable/disable interactions — Tutor Presentation > Forms > Enable/disable interactions
triggers: ["FormEnableDisableView", "Enable", "disable", "interactions", "Tutor", "Presentation", "Forms", "Enable/disable interactions"]
---

# Skill Adianti — Enable/disable interactions — Tutor Presentation > Forms > Enable/disable interactions

Classe Tutor: `FormEnableDisableView`.
Ver no Tutor: `index.php?class=FormEnableDisableView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormEnableDisableView.class.php`.


## Código

```php
<?php
/**
 * FormEnableDisableView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormEnableDisableView extends TPage
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
        $this->form = new BootstrapFormBuilder('form_enable_disable');
        $this->form->setFormTitle(_t('Enable/disable interactions'));
        
        // create the form fields
        $radio_enable = new TRadioGroup('enable');
        $radio_enable->addItems(array('1'=>'Enable group 1', '2'=>'Enable group 2'));
        $radio_enable->setLayout('horizontal');
        $radio_enable->setValue(1);
        
        $block1_combo   = new TCombo('block1_combo');
        $block1_entry   = new TEntry('block1_entry');
        $block1_spinner = new TSpinner('block1_spinner');
        $block2_date    = new TDate('block2_date');
        $block2_entry   = new TEntry('block2_entry');
        $block2_check   = new TCheckGroup('block2_check');
        
        $block1_combo->addItems(array(1=>'One', 2=>'Two'));
        $block1_spinner->setRange(1,100,10);
        $block2_check->addItems(array('Y'=>'Yes', 'N'=>'No'));
        
        // adjust grid layout columns
        $this->form->setColumnClasses(2, ['col-sm-3', 'col-sm-9']);
        
        // add the fields inside the form
        $this->form->addFields([],                       [$radio_enable] );
        $this->form->addFields([new TLabel('group #1')], [$block1_combo] );
        $this->form->addFields([],                       [$block1_entry] );
        $this->form->addFields([],                       [$block1_spinner] );
        $this->form->addFields([new TLabel('group #2')], [$block2_date] );
        $this->form->addFields([],                       [$block2_entry] );
        $this->form->addFields([],                       [$block2_check] );
        
        $radio_enable->setChangeAction( new TAction( array($this, 'onChangeRadio')) );
        self::onChangeRadio( array('enable'=>1) );
        
        $this->form->addAction( 'Save', new TAction([$this, 'onSend']), 'fa:rocket');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);

        parent::add($vbox);
    }
    
    /**
     * on ChangeRadio change
     * @param $param Action parameters
     */
    public static function onChangeRadio($param)
    {
        if ($param['enable'] == 1)
        {
            TCombo::enableField('form_enable_disable', 'block1_combo');
            TEntry::enableField('form_enable_disable', 'block1_entry');
            TSpinner::enableField('form_enable_disable', 'block1_spinner');
            
            TDate::disableField('form_enable_disable', 'block2_date');
            TEntry::disableField('form_enable_disable', 'block2_entry');
            TCheckGroup::disableField('form_enable_disable', 'block2_check');
            
            TEntry::clearField('form_enable_disable', 'block2_entry');
            TCheckGroup::clearField('form_enable_disable', 'block2_check');
        }
        else
        {
            TCombo::disableField('form_enable_disable', 'block1_combo');
            TEntry::disableField('form_enable_disable', 'block1_entry');
            TSpinner::disableField('form_enable_disable', 'block1_spinner');
            
            TDate::enableField('form_enable_disable', 'block2_date');
            TEntry::enableField('form_enable_disable', 'block2_entry');
            TCheckGroup::enableField('form_enable_disable', 'block2_check');
            
            TEntry::clearField('form_enable_disable', 'block1_entry');
            TSpinner::clearField('form_enable_disable', 'block1_spinner');
        }
    }
    
    public static function onSend($param)
    {
        echo '<pre>';
        var_dump($param);
        echo '</pre>';
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
