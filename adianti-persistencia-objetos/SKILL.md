---
name: adianti-persistencia-objetos
description: Active Record, store/load/update/delete, lazy load, hooks, logs e conversão array/JSON no Adianti
triggers: ["Active Record", "TRecord", "store objeto", "load objeto", "update objeto", "delete objeto", "lazy load", "hook method", "TLogger", "encapsulamento", "object to json", "fromArray", "objetos persistência"]
---

# Skill Adianti — Persistência: Objetos

Fonte: Tutor menu Persistência > Objetos. Recursos: `app/resources/Persistence/Objects/*.php`.

## Páginas cobertas

`SetupActiveRecordView`, `ObjectStoreView`, `ObjectCreateView`, `ObjectLoadView`, `ObjectLoad2View`, `ObjectLazyView`, `ObjectRenderView`, `ObjectUpdateView`, `ObjectDeleteView`, `ObjectFirstLastView`, `ObjectFromArrayView`, `ObjectToJsonView`, `HookMethodView`, `EncapsulationView`, `RegisterLogView`, `RegisterLogFunctionView`, `RegisterLogDumpView`.

## Padrões

### Active Record mínimo
```php
class Customer extends TRecord
{
    const TABLENAME = 'customer';
    const PRIMARYKEY = 'id';
    const IDPOLICY = 'max'; // ou serial
    public function __construct($id = NULL) {
        parent::__construct($id);
        parent::addAttribute('name');
        parent::addAttribute('address');
        parent::addAttribute('phone');
        // ...
    }
}
```

### Store
```php
TTransaction::open('samples');
$cli = new Customer;
$cli->name = 'Giovanni Dall Oglio';
$cli->email = 'giovanni@dalloglio.net';
$cli->store();
TTransaction::close();
```

### Load / Load estático / Lazy
```php
TTransaction::open('samples');
$obj = new Customer(1);          // load por PK
$obj2 = Customer::find(1);       // static
echo $obj->name;
echo $obj->category->name;       // lazy: carrega Category sob demanda
TTransaction::close();
```

### Update / Delete
```php
TTransaction::open('samples');
$obj = new Customer(1);
$obj->name = 'Novo nome';
$obj->store();   // update (já tem id)
$obj->delete();  // delete
TTransaction::close();
```

### Hooks (HookMethod.php)
```php
class Product extends TRecord {
    public function onBeforeStore($object) { /* valida */ }
    public function onAfterStore($object) { /* pós-processa */ }
    public function onBeforeDelete($object) {}
}
```

### Log de transação
```php
TTransaction::open('samples');
TTransaction::setLogger(new TLoggerSTD);              // tela
TTransaction::setLogger(new TLoggerTXT('tmp/log.txt')); // arquivo
TTransaction::setLogger(new TLoggerHTML('tmp/log.html'));
TTransaction::log('mensagem custom');
$obj = new Customer(1); $obj->store();
TTransaction::close();
```

### Conversões
```php
$array = $obj->toArray();
$obj->fromArray($array);
$json = $obj->toJson();
```

### First/Last
```php
$first = Customer::firstId();
$last  = Customer::lastId();
```
