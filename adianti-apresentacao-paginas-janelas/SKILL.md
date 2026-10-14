---
name: adianti-apresentacao-paginas-janelas
description: TPage, TWindow, modal, cortina lateral, inbox, wizard multi-etapa e PDF/vídeo embutido
triggers: ["TPage", "TWindow", "página comum", "janela modal", "cortina lateral", "side page", "inbox", "wizard", "multi etapa", "embedded pdf", "embedded video", "onDemand window", "page center"]
---

# Skill Adianti — Apresentação: Páginas e Janelas

Fonte: Tutor menu Apresentação > Páginas. Controles em `app/control/Presentation/Pages/`.

## Páginas cobertas

`SinglePageView`, `SidePageView`, `EmbeddedPDFView`, `EmbeddedVideoView`, `ExternalPageView`, `SingleWindowView`, `ModalWindowView`, `WindowPDFView`, `ExternalSystemWindowView`, `OnDemandWindowView`, `PageCenterView`, `InboxView`, `MultiStepMultiFormView`, `MultiStepRegistration1..4View`.

## Padrões

### Página comum
```php
class SinglePageView extends TPage
{
    public function __construct() {
        parent::__construct();
        $vbox = new TVBox; $vbox->style = 'width:100%';
        $vbox->add(new TXMLBreadCrumb('menu.xml', __CLASS__));
        $vbox->add(new TLabel('Conteúdo'));
        parent::add($vbox);
    }
}
```

### Janela modal / comum
```php
class ModalWindowView extends TWindow {
    public function __construct() {
        parent::__construct();
        parent::setSize(0.6, 0.6);
        parent::setTitle('Modal');
        parent::add(new TLabel('Corpo'));
    }
}
// abrir via ação
new TAction(['ModalWindowView', 'onReload']);
```

### Cortina lateral (right panel) — padrão usado no StandardFormDataGridCurtainView
```php
public static function onEditCurtain($param = null) {
    $page = TPage::create();
    $page->setTargetContainer('adianti_right_panel');
    $page->setProperty('override', 'true');
    $page->setPageName(__CLASS__);
    $embed = new self($param);
    $embed->onEdit($param);
    $page->add($embed->form);
    $page->show();
}
// fechar: Template.closeRightPanel();
```

### Janela sob demanda
```php
TWindow::create('Título', 0.8, 0.6)->add($content)->show();
// ou
$win = new TWindow; $win->setSize(800, 600); $win->add($panel); $win->show();
```

### PDF / vídeo embutido
```php
$object = new TElement('iframe');
$object->src = 'files/manual.pdf';
$object->style = 'width:100%;height:600px';
$vbox->add($object);
// vídeo: <video> ou iframe YouTube
```

### Wizard multi-etapa
```php
// MultiStepRegistration1..4: cada etapa é uma TPage com TAction para próxima
// guarda estado em TSession::setValue('step_data', $data)
$form->addAction('Próximo', new TAction([$this, 'onNextStep']), 'fa:arrow-right');
```

### Inbox / PageCenter
```php
// InboxView: TPage com lista interna, clica e carrega detalhe no mesmo container
// PageCenterView: gerencia abas via Template.goFirstPageTab()
```
