---
name: adianti-contactformwindow
description: ContactFormWindow — Tutor Organization > ComplexViews
triggers: ["ContactFormWindow", "Tutor", "Organization", "ComplexViews"]
---

# Skill Adianti — ContactFormWindow — Tutor Organization > ComplexViews

Classe Tutor: `ContactFormWindow`.
Ver no Tutor: `index.php?class=ContactFormWindow` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Organization/ComplexViews/ContactFormWindow.class.php`.


## Código

```php
<?php
/**
 * ContactFormWindow
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class ContactFormWindow extends TWindow
{
    private $form;
    
    public function __construct()
    {
        parent::__construct();
        parent::setSize(400, null);
        parent::disableScrolling();
        parent::setTitle('Add/Edit contact');
        
        $id          = new THidden('id');
        $customer_id = new THidden('customer_id');
        $type        = new TEntry('type');
        $value       = new TEntry('value');
        
        $this->form = new BootstrapFormWrapper(new TQuickForm);
        $this->form->addQuickField('ID', $id);
        $this->form->addQuickField('Customer', $customer_id);
        $this->form->addQuickField('Type',  $type);
        $this->form->addQuickField('Value', $value);
        
        $this->form->addQuickAction('Save', new TAction(array($this, 'onSave')), 'fa:save green');
        
        parent::add($this->form);
    }
    
    /**
     * Pre fill the form with the foreign key (customer_id)
     */
    public function onLoad($param)
    {
        $this->form->setData( (object) $param);
    }
    
    /**
     * Fill the form with contact information for editing
     */
    public function onEdit($param)
    {
        try
        {
            TTransaction::open('samples');
            $key= $param['key'];
            $contact = new Contact($key);
            $this->form->setData($contact);
            TTransaction::close();
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
            TTransaction::rollback();
        }
    }
    
    /**
     * Save the contact information
     */
    public function onSave($param)
    {
        try
        {
            TTransaction::open('samples');
            $object = $this->form->getData('Contact');
            $object->store();
            TTransaction::close();
            AdiantiCoreApplication::loadPage('CustomerStatusView', 'onCheckStatus',
                                       array( 'customer_id' => $object->customer_id));
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
            TTransaction::rollback();
        }
    }
}
?>
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
