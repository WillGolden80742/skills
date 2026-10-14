---
name: adianti-formbuildergridview
description: Bootstrap form grid — Tutor Presentation > Forms > Bootstrap form grid
triggers: ["FormBuilderGridView", "Bootstrap", "form", "grid", "Tutor", "Presentation", "Forms", "Bootstrap form grid"]
---

# Skill Adianti — Bootstrap form grid — Tutor Presentation > Forms > Bootstrap form grid

Classe Tutor: `FormBuilderGridView`.
Ver no Tutor: `index.php?class=FormBuilderGridView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Forms/FormBuilderGridView.class.php`.


## Código

```php
<?php
/**
 * FormBuilderGridView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormBuilderGridView extends TPage
{
    private $form;
    
    /**
     * Class constructor
     * Creates the page
     */
    public function __construct()
    {
        parent::__construct();
        
        $this->form = new BootstrapFormBuilder;
        $this->form->setFormTitle(_t('Bootstrap form grid'));
        
        $this->form->appendPage('Automatic form grid');
        
        $this->form->addFields( [ new TLabel('2 slots') ],
                                [ new TEntry('field_1') ] );
        
        $this->form->addFields( [ new TLabel('3 slots') ],
                                [ new TEntry('field_2') ],
                                [ new TEntry('field_3') ] );
                                
        $this->form->addFields( [ new TLabel('4 slots') ],
                                [ new TEntry('field_4') ],
                                [ new TEntry('field_5') ],
                                [ new TEntry('field_6') ] );
                                
        $this->form->addFields( [ new TLabel('5 slots') ],
                                [ new TEntry('field_7') ],
                                [ new TEntry('field_8') ],
                                [ new TEntry('field_9') ],
                                [ new TEntry('field_10') ] );
                                
        $this->form->addFields( [ new TLabel('6 slots') ],
                                [ new TEntry('field_11') ],
                                [ new TEntry('field_12') ],
                                [ new TEntry('field_13') ],
                                [ new TEntry('field_14') ],
                                [ new TEntry('field_15') ] );
                                
        $this->form->appendPage('Manual form grid');
        
        // add the fields inside the form
        $row = $this->form->addFields( [ new TLabel('Custom 1') ],
                                       [ new TEntry('field_16') ],
                                       [ new TEntry('field_17') ],
                                       [ new TEntry('field_18') ] );
        $row->layout = ['col-sm-2 control-label', 'col-sm-4', 'col-sm-4', 'col-sm-2' ];
        
        $row = $this->form->addFields( [ new TLabel('Custom 2') ],
                                       [ new TEntry('field_19') ],
                                       [ new TEntry('field_20') ],
                                       [ new TEntry('field_21') ] );
        $row->layout = ['col-sm-2 control-label', 'col-sm-2', 'col-sm-6', 'col-sm-2' ];
        
        $row = $this->form->addFields( [ new TLabel('Custom 3') ],
                                       [ new TEntry('field_22') ],
                                       [ new TEntry('field_23') ],
                                       [ new TEntry('field_24') ] );
        $row->layout = ['col-sm-2 control-label', 'col-sm-2', 'col-sm-4', 'col-sm-4' ];
        
        $row = $this->form->addFields( [ new TLabel('Custom 4') ],
                                       [ new TEntry('field_25') ],
                                       [ new TEntry('field_26') ],
                                       [ new TEntry('field_27') ],
                                       [ new TEntry('field_28') ],
                                       [ new TEntry('field_29') ],
                                       [ new TEntry('field_30') ] );
        $row->layout = ['col-sm-2 control-label', 'col-sm-2', 'col-sm-2', 'col-sm-2', 'col-sm-2', 'col-sm-1', 'col-sm-1' ];
        
        $row = $this->form->addFields( [ new TLabel('Custom 5') ],
                                       [ new TEntry('field_31') ],
                                       [ new TEntry('field_32') ],
                                       [ new TEntry('field_33') ],
                                       [ new TEntry('field_34') ],
                                       [ new TEntry('field_35') ] );
        $row->layout = ['col-sm-2 control-label', 'col-sm-1', 'col-sm-1', 'col-sm-1', 'col-sm-1', 'col-sm-6' ];
        
        $this->form->addAction('Send', new TAction(array($this, 'onSend')), 'far:check-circle green');
        
        // wrap the page content using vertical box
        $vbox = new TVBox;
        $vbox->style = 'width: 100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add($this->form);

        parent::add($vbox);
    }
    
    /**
     * Post data
     */
    public function onSend($param)
    {
        $data = $this->form->getData();
        $this->form->setData($data);
        
        echo '<pre>';
        print_r($data);
        echo '</pre>';
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
