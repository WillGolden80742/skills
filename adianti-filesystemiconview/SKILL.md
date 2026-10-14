---
name: adianti-filesystemiconview
description: Filesystem Icon View — Tutor Presentation > Utilities > Filesystem Icon View
triggers: ["FilesystemIconView", "Filesystem", "Icon", "View", "Tutor", "Presentation", "Utilities", "Filesystem Icon View"]
---

# Skill Adianti — Filesystem Icon View — Tutor Presentation > Utilities > Filesystem Icon View

Classe Tutor: `FilesystemIconView`.
Ver no Tutor: `index.php?class=FilesystemIconView` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/Presentation/Widgets/FilesystemIconView.class.php`.


## Código

```php
<?php
/**
 * FilesystemIconView
 *
 * @version    1.0
 * @package    samples
 * @subpackage tutor
 * @author     Pablo Dall'Oglio
 * @copyright  Copyright (c) 2006 Adianti Solutions Ltd. (http://www.adianti.com.br)
 * @license    https://adiantiframework.com.br/license-tutor
 */
class FilesystemIconView extends TPage
{
    private $iconview;
    
    /**
     * Constructor method
     */
    public function __construct()
    {
        parent::__construct();
        
        $this->iconview = new TIconView;
        
        $dir = new DirectoryIterator( getcwd() );
        
        foreach ($dir as $fileinfo)
        {
            if (!$fileinfo->isDot() && !str_starts_with($fileinfo->getFilename(), '.'))
            {
                $item = new stdClass;
                
                if ($fileinfo->isDir())
                {
                    $item->type = 'folder';
                    $item->icon = 'far:folder blue fa-4x';
                }
                else
                {
                    $item->type = 'file';
                    $item->icon = 'fas:file orange fa-4x';
                }
                
                $item->path = $fileinfo->getPath();
                $item->name = $fileinfo->getFilename();
                
                $this->iconview->addItem($item);
            }
        }
        
        // $this->iconview->enablePopover('', '<b>Name:</b> {name}');
        
        $this->iconview->setIconAttribute('icon');
        $this->iconview->setLabelAttribute('name');
        $this->iconview->setInfoAttributes(['name', 'path']);
        
        $display_condition = function($object) {
            return ($object->type == 'file');
        };
        
        $this->iconview->addContextMenuOption('Options');
        $this->iconview->addContextMenuOption('');
        $this->iconview->addContextMenuOption('Open',   new TAction([$this, 'onOpen']),   'far:folder-open blue');
        $this->iconview->addContextMenuOption('Rename', new TAction([$this, 'onRename']), 'far:edit green');
        $this->iconview->addContextMenuOption('Delete', new TAction([$this, 'onDelete']), 'far:trash-alt red', $display_condition);
        
        parent::add( $this->iconview );
    }
    
    /**
     * Open action
     */
    public static function onOpen($param)
    {
        new TMessage('info', '<b>Name: </b>' . $param['name'] . 
                        '<br> <b>Path: </b>' . $param['path']);
    }
    
    /**
     * Rename action
     */
    public static function onRename($param)
    {
        new TMessage('info', '<b>Name: </b>' . $param['name'] . 
                        '<br> <b>Path: </b>' . $param['path']);
    }
    
    /**
     * Delete action
     */
    public static function onDelete($param)
    {
        new TMessage('info', '<b>Name: </b>' . $param['name'] . 
                        '<br> <b>Path: </b>' . $param['path']);
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
