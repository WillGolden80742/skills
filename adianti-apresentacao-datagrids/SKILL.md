---
name: adianti-apresentacao-datagrids
description: TDataGrid bootstrap, ações, paginação, busca, exportação, transformação e edição inline
triggers: ["TDataGrid", "datagrid bootstrap", "datagrid actions", "export datagrid", "datagrid search", "datatable", "TDataGridColumn", "TPageNavigation", "datagrid transform", "datagrid input"]
---

# Skill Adianti — Apresentação: Datagrids

Fonte: Tutor menu Apresentação > Datagrids. `app/control/Presentation/Datagrid/`.

## Páginas cobertas

`DatagridCustomView`, `DatagridBootstrapView`, `DatagridActionGroupView`, `DatagridColumnGroupView`, `DatagridConditionalActionView`, `DatagridHScrollView`, `DatagridScrollView`, `DatagridHiddableView`, `DatagridDatatableView`, `DatagridSearchView`, `DatagridRestView`, `DatagridTransformView`, `DatagridLinkView`, `DatagridMathView`, `DatagridImageView`, `DatagridLabelView`, `DatagridProgressView`, `DatagridExportView`, `DatagridInputView`, `DatagridInputDialogView`, `DatagridWindowView`, `DatagridQueryView`, + Extras (`DatagridPopView`, `DatagridDetailView`, `DatagridCheckView`, `DatagridWindowForm`).

## Padrão base (DatagridBootstrapView real)

```php
$this->datagrid = new BootstrapDatagridWrapper(new TDataGrid);
$this->datagrid->enablePopover('Details', '<b>Code:</b> {code} <br> <b>Name:</b> {name}');

$code  = new TDataGridColumn('code', 'Code', 'center', '10%');
$name  = new TDataGridColumn('name', 'Name', 'left', '30%');
$this->datagrid->addColumn($code, new TAction([$this,'onColumnAction'], ['column'=>'code']));
$this->datagrid->addColumn($name);

$action1 = new TDataGridAction([$this,'onView'], ['code'=>'{code}']);
$action1->setUseButton(TRUE);
$this->datagrid->addAction($action1, 'View', 'fa:search blue');
$this->datagrid->addAction(new TDataGridAction([$this,'onDelete'], ['code'=>'{code}']), 'Delete', 'far:trash-alt red');

$this->datagrid->createModel();
$panel = new TPanelGroup(_t('Bootstrap Datagrid'));
$panel->add($this->datagrid)->style = 'overflow-x:auto';
```

## onReload + paginação + busca

```php
public function onReload($param = []) {
    TTransaction::open('samples');
    $repo = new TRepository('Customer');
    $criteria = new TCriteria;
    $criteria->setProperty('order', $param['order'] ?? 'id');
    $criteria->setProperty('limit', 10);
    $criteria->setProperty('offset', ($param['offset'] ?? 0));
    if (!empty($param['search'])) {
        $criteria->add(new TFilter('name', 'like', "%{$param['search']}%"));
    }
    $objects = $repo->load($criteria);
    $this->datagrid->clear();
    foreach ($objects as $o) $this->datagrid->addItem($o);
    $count = $repo->count($criteria);
    $this->pageNavigation->setCount($count);
    $this->pageNavigation->setProperties($param);
    $this->pageNavigation->setLimit(10);
    TTransaction::close();
    $this->loaded = true;
}
```

## Transformadores / links / imagens / progresso

```php
$col->setTransformer(function($value) { return number_format($value, 2, ',', '.'); });
$col->setTransformer([$this, 'formatDate']); // método
// link
$link = new TActionLink('ver', new TAction([$this,'onView'], ['key'=>'{id}']));
// imagem
$col_img = new TDataGridColumn('photo', 'Foto', 'center');
$col_img->setTransformer(function($v){ return "<img src='files/{$v}' width='40'>"; });
// label colorido / progresso
$col->setTransformer(function($v){ return "<span class='badge bg-success'>{$v}</span>"; });
```

## Export / input / busca fuse

```php
$this->datagrid->enableSearch($input_search, 'id, name'); // fuse search client-side
// export
$panel->addHeaderActionLink('CSV', new TAction([$this,'onExportCSV']), 'fa:file-csv');
// datagrid com input editável
$input = new TEntry('price_{id}'); $col_input->setTransformer(...); 
```

## Regras

- Sempre `createModel()` após colunas + ações.
- `addItem($modelOuStdClass)` — propriedades devem bater com nomes das colunas.
- Ordenação por cabeçalho: `setAction(new TAction([$this,'onReload']), ['order'=>'name'])`.
- Para SQL manual: `DatagridQueryView` usa `TTransaction::get()->query()`.
