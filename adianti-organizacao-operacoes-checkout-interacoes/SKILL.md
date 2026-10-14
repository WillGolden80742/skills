---
name: adianti-organizacao-operacoes-checkout-interacoes
description: Edição em lote, exclusão massiva, checkout/PDV, combos hierárquicos, filtros dinâmicos e status/gráficos
triggers: ["edição lote", "exclusão lote", "inline edit", "checkout", "PDV", "POSForm", "combo hierárquica", "filtro dinâmico", "dynamic criteria", "customer status", "sales chart", "multicheck"]
---

# Skill Adianti — Organização: Operações, Checkout e Interações

Fonte: Tutor menu Organização > Operações em lote, Telas de checkout, Interações entre campos, Telas de consulta. `app/control/Organization/BatchOperations|Checkout|Interactions|QueryScreens/`.

## Páginas cobertas

Lote: `InlineDataGridView`, `ProductUpdateList`, `ProductInstantUpdateList`, `MassiveDeleteView`, `ProductSelectionList`, `MultiCheckView`.
Checkout: `CheckoutFormView`, `POSFormView`.
Interações: `FormHierarchicalComboView`, `FormDynamicSessionCriteriaView`, `FormDynamicFilterView`.
Consulta: `CustomerStatusView`, `SalesChartView`.

## Padrões

### Edição inline / em lote
```php
// InlineDataGridView: coluna vira TEntry dentro da grid
$col_price->setTransformer(function($v, $obj) {
    $input = new TEntry("price_{$obj->id}");
    $input->setValue($v); $input->setSize('100%');
    return $input->getContents();
});
// onSaveBatch: loop em $param (price_1, price_2...) e store()
// Instant: onChange com TAction ajax por linha
```

### Exclusão massiva / seleção
```php
$check = new TCheckButton('check_{id}');
$datagrid->addColumn(new TDataGridColumn('check','', 'center'));
// onDeleteCollection: explode(',', $param['ids']) e delete cada um
// ProductSelectionList: seleciona e devolve para outro form via TSession
```

### Checkout / PDV
```php
// CheckoutFormView: wizard endereço->pagamento->confirmação com TSession
// POSFormView (mestre/detalhe PDV): busca produto por código, adiciona na FieldList, totaliza, finaliza venda
$seek = new TSeekButton('product_code', 'product_name', 'ProductList', 'search');
$seek->setChangeAction(new TAction([$this,'onAddItem']));
```

### Combo hierárquica + filtro dinâmico
```php
// Estado -> Cidade
$state->setChangeAction(new TAction([$this,'onChangeState']));
public static function onChangeState($param) {
    $cities = City::where('state_id', '=', $param['state_id'])->load();
    TCombo::reload('form', 'city_id', $cities);
}
// Critério dinâmico com sessão
TTransaction::open('samples');
$criteria = new TCriteria;
$criteria->add(new TFilter('city_id', '=', TSession::getValue('user_city')));
$combo = new TDBCombo('customer_id','samples','Customer','id','name', $criteria);
```

### Status / gráfico consulta
```php
// CustomerStatusView: THtmlRenderer('app/resources/customer_status.html') + indicadores
// SalesChartView: TLineChart/TBarChart com dados de Sale agregado por mês
```

## Regras

- Lote sempre confirma com `TQuestion` antes de `store/delete` em massa.
- PDV usa `TSession` para carrinho temporário — limpe em `onFinish`.
- Filtros dinâmicos: `setChangeAction` + `::reload` é o par obrigatório.
