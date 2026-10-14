---
name: adianti-formeventspanelview
description: FormEventsPanelView — Tutor Presentation > Extras
triggers: ["FormEventsPanelView", "Tutor", "Presentation", "Extras", "FormEventsPanel"]
---

# Skill Adianti — FormEventsPanelView — Tutor Presentation > Extras

Classe Tutor: `FormEventsPanelView`.
Ver no Tutor: `index.php?class=FormEventsPanelView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Extras/FormEventsPanelView.class.php`.


## Código

```php
<?php
/**
 * FormEventsPanelView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FormEventsPanelView extends TPage
{
    protected $html;
    
    /**
     * Class constructor
     * Creates the page and the registration form
     */
    public function __construct()
    {
        parent::__construct();
        
        parent::setTargetContainer('adianti_right_panel');
        
        // creates the form
        $this->html = new TElement('div');
        $this->html->setProperty('style', 'margin:20px; font-size: 14pt;');
        
        $al = new TActionLink(_t('Close'), new TAction([$this, 'onClose']), null, null, null, 'fa:times red' );
        $al->class = 'btn btn-default';
        $al->style = 'clear:both';
        $this->html->add($al);
        $this->html->add(new TElement('br'));
        $this->html->add(new TElement('br'));
        
        parent::add($this->html);
    }
    
    /**
     * Load content
     */
    public function onLoad($param)
    {
        $this->html->add(base64_decode($param['content']));
    }
    
    /**
     * Close side panel
     */
    public static function onClose($param)
    {
        TScript::create("Template.closeRightPanel()");
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
