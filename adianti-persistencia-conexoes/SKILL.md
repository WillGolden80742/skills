---
name: adianti-persistencia-conexoes
description: Transações, conexões manuais, DDL/DML baixo nível, prepared queries e logs no Adianti Tutor
triggers: ["TTransaction", "transação banco", "conexão manual", "DDL", "DML", "prepared query", "FakeTransaction", "TransactionInfo", "SetupTransaction", "ManualConnection", "persistência conexões"]
---

# Skill Adianti — Persistência: Conexões

Fonte: Adianti Tutor 8.7 (`http://localhost:6677`), menu Persistência > Conexões.
Ver código: página do exemplo + botão flutuante `</>` (`DocumentationView::onHelp`, já corrigido para `.php` e `.class.php`).

## Páginas do Tutor cobertas

| Classe Tutor | URL | O que ensina |
|---|---|---|
| `SetupTransactionView` | `index.php?class=SetupTransactionView` | `TTransaction::open('samples')`, `$conn = TTransaction::get()`, `$conn->query()`, `TTransaction::close()` |
| `ManualConnectionView` | `index.php?class=ManualConnectionView` | `TConnection` manual sem `TTransaction` |
| `ManualDDLCommandsView` | `index.php?class=ManualDDLCommandsView` | `CREATE TABLE`, `DROP` via PDO baixo nível |
| `ManualDMLCommandsView` | `index.php?class=ManualDMLCommandsView` | `INSERT/UPDATE/DELETE` manual |
| `ManualPrepareQueryView` | `index.php?class=ManualPrepareQueryView` | `prepare()` + `bindValue` |
| `FakeTransactionView` | `index.php?class=FakeTransactionView` | Transação somente-leitura |
| `TransactionInfoView` | `index.php?class=TransactionInfoView` | `TTransaction::getDatabaseInfo()`, driver, nome banco |
| `SetupActiveRecordView` | `index.php?class=SetupActiveRecordView` | Registro de Active Record |

Recursos-fonte: `app/resources/Persistence/Setup/*.php` (`SetupTransaction.php`, `ManualConnection.php`, `ManualPrepareQuery.php`, `FakeTransaction.php`, `TransactionInfo.php`, `SetupActiveRecord.php`).

## Padrão 1 — Transação padrão (SetupTransaction.php)

```php
class ManualQuery extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try {
            TTransaction::open('samples'); // abre transação
            $conn = TTransaction::get();   // PDO

            $result = $conn->query('SELECT id, name from customer order by id');
            foreach ($result as $row) {
                print $row['id'] . '-';
                print $row['name'] . "<br>\n";
            }
            TTransaction::close(); // fecha/commit
        }
        catch (Exception $e) {
            new TMessage('error', $e->getMessage());
        }
    }
}
```

## Padrão 2 — Prepared query manual

```php
TTransaction::open('samples');
$conn = TTransaction::get();
$stmt = $conn->prepare('SELECT id, name FROM customer WHERE id = :id');
$stmt->bindValue(':id', 1);
$stmt->execute();
$row = $stmt->fetch(PDO::FETCH_ASSOC);
TTransaction::close();
```

## Padrão 3 — Conexão manual sem transação

```php
$conn = TConnection::open('samples'); // ou new PDO(...)
$result = $conn->query('SELECT * FROM customer');
// fechar manualmente, sem TTransaction::close()
```

## Regras

- Sempre `try { open ... close } catch { TMessage('error', ...) }`.
- `TTransaction::get()` retorna PDO ativo — use `query()`, `prepare()`, `exec()`.
- `samples` é o banco de exemplo do Tutor (`app/config/samples.ini`).
- Para ver o fonte real: `app/control/Persistence/Setup/<Classe>.php` mostra o viewer; `app/resources/Persistence/Setup/<Exemplo>.php` tem o código executável.
- Bug corrigido: `TSourceCode::show()` agora faz cast `(string)` e `DocumentationView::onHelp()` aceita `.php` + `.class.php` (antes só `.class.php`, por isso o diálogo vinha vazio com `highlight_string(null)` deprecated).
