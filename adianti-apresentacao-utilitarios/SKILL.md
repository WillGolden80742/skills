---
name: adianti-apresentacao-utilitarios
description: Calendário, Gantt, Kanban, Cards, Timeline, TreeView, Dropdown, Steps e SourceCode
triggers: ["TFullCalendar", "TGantt", "TKanban", "TCardView", "TTimeline", "TTreeView", "TCalendar", "calendar view", "kanban database", "gantt database", "card view", "timeline", "dropdown", "step view"]
---

# Skill Adianti — Apresentação: Utilitários

Fonte: Tutor menu Apresentação > Utilitários + Organização > Utilitários (versões com banco). `app/control/Presentation/Widgets/` e `Organization/Utilities/`.

## Páginas cobertas

`FullCalendarStaticView`, `CalendarView`, `GanttView`, `IconView`, `FilesystemIconView`, `TimelineView`, `KanbanView`, `KanbanCustomView`, `CardView`, `VideoCardView`, `TreeView`, `DropdownView`, `StepView`, `ArrowStepView`, `SourceCodeView`, + com banco: `FullCalendarDatabaseView`, `FullCalendarSplitView`, `GanttDatabaseView`, `KanbanDatabaseView`, `ProductCardView`, `ProductCatalogView`, `AgendaView`.

## Padrões

```php
// FullCalendar estático
$cal = new TFullCalendar(date('Y-m-d'), 'month');
$cal->addEvent(1, 'Reunião', date('Y-m-d'), date('Y-m-d'), '#2c3e50', 'link...');
$vbox->add($cal);

// FullCalendar com banco (FullCalendarDatabaseView)
$cal = new TFullCalendar($date, $view);
$events = CalendarEvent::getObjects($criteria);
foreach ($events as $e) $cal->addEvent($e->id, $e->title, $e->start, $e->end, $e->color);
$cal->setClickAction(new TAction(['CalendarEventPanelForm','onEdit']));

// Gantt
$gantt = new TGantt;
$gantt->addTask(1, 'Análise', date('Y-m-d'), date('Y-m-d', strtotime('+5 days')), 60);
$gantt->setReloadAction(new TAction([$this,'onReload']));

// Kanban
$kanban = new TKanban;
$kanban->addStage(1, 'A fazer');
$kanban->addItem(1, 1, 'Task X', 'detalhe');
$kanban->setItemAction(new TAction(['KanbanItemForm','onEdit']));
$kanban->setStageAction(new TAction(['KanbanStageForm','onEdit']));
// Kanban com banco: estágios e itens vêm de Stage/Item + drag atualiza via onUpdate

// Cards
$card = new TCardView('Título', 'subtítulo', 'files/foto.jpg', new TAction([$this,'onView'],['id'=>1]));
$catalog = new ProductCardView; // grade de cards com busca

// Timeline
$tl = new TTimeline;
$tl->addItem(date('Y-m-d'), 'Evento', 'descrição', 'fa:check blue');

// TreeView
$tree = new TTreeView;
$tree->addItem('1', 'Pai', null);
$tree->addItem('1.1', 'Filho', '1');

// Steps
$step = new TArrowStep;
$step->addItem('1. Pedido', new TAction([$this,'onStep1']));
$step->addItem('2. Pagto', new TAction([$this,'onStep2']));
$step->select('1. Pedido');

// Dropdown
$dd = new TDropDown('Opções', 'fa:list');
$dd->addAction('Editar', new TAction([$this,'onEdit']));
```

## Regras

- Calendário/Kanban/Gantt com banco usam `TTransaction` + `onReload` que recarrega eventos.
- `FullCalendarSplitView` abre form em cortina lateral (`adianti_right_panel`).
- Cards usam `app/resources/card.html` como template — ver `ProductCatalogView` para catálogo com carrinho.
