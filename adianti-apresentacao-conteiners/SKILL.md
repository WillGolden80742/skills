---
name: adianti-apresentacao-conteiners
description: Tabelas, painéis, notebooks, scroll, frames, VBox/HBox e wrappers no Adianti
triggers: ["TTable", "TPanel", "TNotebook", "TScroll", "TFrame", "TVBox", "THBox", "TPanelGroup", "container", "notebook bootstrap", "page frame", "page wrapper"]
---

# Skill Adianti — Apresentação: Contêineres

Fonte: Tutor menu Apresentação > Contêineres. `app/control/Presentation/Containers/`.

## Páginas cobertas

`ContainerTableView`, `ContainerTableColumnsView`, `ContainerPanelView`, `ContainerNotebookView`, `ContainerNotebookBootstrapView`, `ContainerNotebookPillsView`, `ContainerNotebookStyleView`, `ContainerPanelGroupView`, `ContainerScrollView`, `ContainerFrameView`, `ContainerVBoxView`, `ContainerHBoxView`, `ContainerPageFrame`, `ContainerPageWrapper`, + `AnotherWindowView`.

## Padrões

```php
// Tabela
$table = new TTable; $table->style = 'width:100%';
$row = $table->addRow();
$row->addCell(new TLabel('A'))->width = '50%';
$row->addCell(new TLabel('B'));

// Painel + grupo
$panel = new TPanelGroup('Título');
$panel->add($datagrid);
$panel->addHeaderWidget($searchInput);
$panel->addHeaderActionLink('Novo', new TAction([$this,'onEdit']), 'fa:plus green');
$panel->addFooter('rodapé');

// Notebook clássico e bootstrap
$nb = new TNotebook;
$nb->appendPage('Aba 1', $content1);
$nb->appendPage('Aba 2', $content2);
// bootstrap: BootstrapNotebookWrapper ou TNotebook com style pills

// Scroll
$scroll = new TScroll;
$scroll->setSize('100%', 400);
$scroll->add($longContent);

// Frame / VBox / HBox
$frame = new TFrame; $frame->setLegend('Grupo'); $frame->add($form);
$vbox = new TVBox; $vbox->style = 'width:100%'; $vbox->add($a); $vbox->add($b);
$hbox = new THBox; $hbox->add($left)->width='50%'; $hbox->add($right);

// PageFrame / PageWrapper (embelezam TPage)
$page = TPage::create();
$page->setTargetContainer('adianti_right_panel');
```

## Regras

- Todo exemplo do Tutor embrulha em `TVBox(width:100%) + TXMLBreadCrumb + conteúdo + parent::add($vbox)`.
- `TPanelGroup::pack('', $datagrid)` é o atalho mais usado nas datagrids.
- Notebook events: ver `ContainerNotebookStyleView` (`onLeavePage`, tabs desabilitadas).
