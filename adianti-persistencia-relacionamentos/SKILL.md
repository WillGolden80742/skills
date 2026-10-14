---
name: adianti-persistencia-relacionamentos
description: Associação, composição, agregação e atalhos de relacionamento 1-N e N-N no Adianti
triggers: ["relacionamento", "associação objetos", "composição objetos", "agregação objetos", "1-N", "N-N", "get_category", "set_category", "relation shortcuts", "TRecord relacionamento"]
---

# Skill Adianti — Persistência: Relacionamentos

Fonte: Tutor menu Persistência > Relacionamentos. Recursos: `app/resources/Persistence/Relationships/*.php`.

## Páginas cobertas

`RelationShortcutsView`, `AssociationView`, `CompositionView`, `CompositionSimpleView`, `AggregationView`, `AggregationSimpleView`.

Modelos: `Customer (N-1 Category, N-1 City)`, `Sale (1-N SaleItem)`, `Customer (N-N Group via CustomerGroup)`.

## Padrão Associação (N-1) — get/set

```php
class Customer extends TRecord
{
    private $category;
    public function set_category(Category $object) {
        $this->category = $object;
        $this->category_id = $object->id;
    }
    public function get_category() {
        if (empty($this->category))
            $this->category = new Category($this->category_id);
        return $this->category;
    }
}
// uso
TTransaction::open('samples');
$c = new Customer(1);
echo $c->category->name; // lazy via get_category
$c->category = new Category(2); // set_category
$c->store();
TTransaction::close();
```

## Padrão Composição (1-N pai-filho, ex: Sale -> itens)

```php
TTransaction::open('samples');
$sale = new Sale;
$sale->customer_id = 1;
$sale->date = date('Y-m-d');
$sale->store();

foreach ($items as $itemData) {
    $item = new SaleItem;
    $item->sale_id = $sale->id;
    $item->product_id = $itemData['id'];
    $item->amount = $itemData['amount'];
    $item->store();
}
TTransaction::close();

// carregar filhos
$sale = new Sale(1);
$items = $sale->getSaleItems(); // hasMany gerado
```

## Padrão Agregação (N-N via intermediária)

```php
// Customer <-> Group via CustomerGroup
TTransaction::open('samples');
$c = new Customer(1);
$groups = $c->getGroups(); // belongsToMany
$c->addGroup(new Group(2));
TTransaction::close();
```

## Atalhos (RelationShortcutsView)

- `$customer->category` resolve automaticamente `get_category()` (mágico via `__get` do TRecord).
- `$sale->items` / `$customer->contacts` conforme métodos `get*` definidos.
- Versões Simple usam convenção sem método explícito quando FK segue padrão `<tabela>_id`.

## Regras

- Sempre abrir `TTransaction` antes de navegar relacionamentos (lazy precisa de conexão).
- `store()` do pai antes dos filhos para ter o id.
- Apagar filhos antes do pai em composição sem cascade, ou usar `onBeforeDelete`.
