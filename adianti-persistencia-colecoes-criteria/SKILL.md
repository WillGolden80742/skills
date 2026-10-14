---
name: adianti-persistencia-colecoes-criteria
description: TCriteria, TFilter, TRepository, coleções, paginação, agregação, joins e subqueries no Adianti
triggers: ["TCriteria", "TFilter", "TRepository", "coleção", "collection load", "paginação coleção", "countObjects", "getObjects", "agregação", "subquery", "join adianti", "criteria api"]
---

# Skill Adianti — Persistência: Coleções e Criteria

Fonte: Tutor (menu Persistência > Coleções implícito + SearchBox). Recursos: `app/resources/Persistence/Collections/*.php`.

## Páginas cobertas

`CriteriaView`, `CollectionLoadView`, `CollectionStaticSimpleLoadView`, `CollectionLoadPropertyView`, `CollectionSimpleLoadPropertyView`, `CollectionGetObjectsView`, `CollectionSubQueryView`, `CollectionUpdateView`, `CollectionBatchUpdateView`, `CollectionStaticBatchUpdateView`, `CollectionAggregationView`, `CollectionArrayView`, `CollectionTransformView`, `CollectionFilterView`, `CollectionDeleteView`, `CollectionStaticSimpleDeleteView`, `CollectionCountView`, `CollectionStaticSimpleCountView`, `CollectionCountObjectsView`, `JoinView`.

## Padrão Criteria (Criteria.php real do Tutor)

```php
$criteria = new TCriteria;
$criteria->add(new TFilter('age', '<', 16), TExpression::OR_OPERATOR);
$criteria->add(new TFilter('age', '>', 60), TExpression::OR_OPERATOR);
echo $criteria->dump(); // (age < 16 OR age > 60)

$criteria = new TCriteria;
$criteria->add(new TFilter('age', 'BETWEEN', 16, 60));

$criteria = new TCriteria;
$criteria->add(new TFilter('nome', 'like', 'pedro%'), TExpression::OR_OPERATOR);
$criteria->add(new TFilter('nome', 'like', 'maria%'), TExpression::OR_OPERATOR);

// IS NOT NULL
$criteria = new TCriteria;
$criteria->add(new TFilter('cellphone', 'IS NOT', NULL));
$criteria->add(new TFilter('gender', '=', 'F'));

// subselect
$criteria = new TCriteria;
$criteria->add(new TFilter('id', 'IN', '(SELECT customer_id FROM purchases)'));

// sem escape
$criteria->add(new TFilter('birthdate', '<=', "NOESC:date(now()) - '2 years'::interval"));

// critérios compostos
$c1 = new TCriteria; $c1->add(new TFilter('gender','=', 'F')); $c1->add(new TFilter('age','>','18'));
$c2 = new TCriteria; $c2->add(new TFilter('gender','=', 'M')); $c2->add(new TFilter('age','<','16'));
$criteria = new TCriteria;
$criteria->add($c1, TExpression::OR_OPERATOR);
$criteria->add($c2, TExpression::OR_OPERATOR);
```

## Repository + coleções

```php
TTransaction::open('samples');
$criteria = new TCriteria;
$criteria->add(new TFilter('status', '=', 'S'));
$criteria->setProperty('order', 'name');
$criteria->setProperty('limit', 10);
$criteria->setProperty('offset', 0);

$repo = new TRepository('Customer');
$collection = $repo->load($criteria); // array de objetos
$count = $repo->count($criteria);

// estático simplificado
$all = Customer::all();
$n = Customer::countObjects($criteria);
$objs = Customer::getObjects($criteria);

foreach ($collection as $obj) { echo $obj->name . "<br>"; }
TTransaction::close();
```

## Batch update / delete / agregação

```php
TTransaction::open('samples');
// update em lote
$objs = Customer::getObjects($criteria);
foreach ($objs as $o) { $o->status = 'I'; $o->store(); }
// delete em lote
foreach ($objs as $o) { $o->delete(); }
// agregação
$criteria = new TCriteria;
$total = $repo->count($criteria);
TTransaction::close();
```

## Join com TSqlSelect

```php
$sql = new TSqlSelect;
$sql->addColumn('customer.name');
$sql->addColumn('city.name as city');
$sql->setEntity('customer INNER JOIN city ON customer.city_id = city.id');
$sql->setCriteria($criteria);
```

## Regras

- `setProperty('order|limit|offset|direction')` controla paginação/ordenação.
- `dump()` mostra SQL gerado — ótimo para debug.
- `NOESC:` desliga escape para funções SQL.
- Filtros de sessão dinâmica: ver skill `adianti-organizacao-operacoes-checkout-interacoes`.
