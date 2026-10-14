---
name: adianti-dialogquestionview
description: Question dialog — Tutor Presentation > Dialogs > Question dialog
triggers: ["DialogQuestionView", "Question", "dialog", "Tutor", "Presentation", "Dialogs", "Question dialog"]
---

# Skill Adianti — Question dialog — Tutor Presentation > Dialogs > Question dialog

Classe Tutor: `DialogQuestionView`.
Ver no Tutor: `index.php?class=DialogQuestionView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Dialogs/DialogQuestionView.class.php`.


## Código

```php
<?php
/**
 * DialogQuestionView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class DialogQuestionView extends TPage
{
    public function __construct()
    {
        parent::__construct();
        
        // create two actions
        $action1 = new TAction(array($this, 'onAction1'));
        $action2 = new TAction(array($this, 'onAction2'));

        // define os parâmetros de cada ação
        $action1->setParameter('parameter', 1);
        $action2->setParameter('parameter', 2);
        
        // shows the question dialog
        new TQuestion('Do you really want to perform this operation ?', $action1, $action2);
        
        parent::add(new TXMLBreadCrumb('menu.xml', __CLASS__));
    }
    
    public static function onAction1($param)
    {
        new TMessage('info', "You have choose the first option. Parameter value {$param['parameter']}");
    }
    
    public static function onAction2($param)
    {
        new TMessage('info', "You have choose the second option. Parameter value {$param['parameter']}");
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
