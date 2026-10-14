---
name: adianti-relationshortcuts
description: RelationShortcuts — código executável dbsamples (Persistence > Relationships)
triggers: ["RelationShortcuts", "digo", "execut", "vel", "dbsamples", "Persistence", "Relationships", "exemplo executavel"]
---

# Skill Adianti — RelationShortcuts — código executável dbsamples (Persistence > Relationships)

Classe Tutor: `RelationShortcuts`.
Ver no Tutor: `index.php?class=RelationShortcuts` + botão view-source (`DocumentationView::onHelp`).
Fonte lida automaticamente: `app/control/dbsamples/RelationShortcuts.class.php`.


## Código

```php
<?php
class RelationShortcuts extends TPage
{
    public function __construct()
    {
        parent::__construct();
        try
        {
            echo '<pre>';
            TTransaction::open('samples'); // abre uma transao
            
            // simplified version, load related objects (1-N)
            $contacts = Customer::find(1)->hasMany('Contact');
            var_dump($contacts);
            
            // complete version, load related objects (1-N)
            $contacts = Customer::find(1)->hasMany('Contact', 'customer_id', 'id', 'type');
            var_dump($contacts);
                        
            // simplified version, filter related objects (1-N), and then load
            $contacts = Customer::find(1)->filterMany('Contact')->where('type', '=', 'phone')->load();
            var_dump($contacts);
            
            // complete version, filter related objects (1-N), and then load
            $contacts = Customer::find(1)->filterMany('Contact', 'customer_id', 'id', 'type')->where('type', '=', 'phone')->load();
            var_dump($contacts);
            
            // simplified version, load related objects (N-N), through associative table (pivot)
            $skills = Customer::find(1)->belongsToMany('Skill');
            var_dump($skills);
            
            // complete version, load related objects (N-N), through associative table (pivot)
            $skills = Customer::find(1)->belongsToMany('Skill', 'CustomerSkill', 'customer_id', 'skill_id');
            var_dump($skills);
            
            echo '</pre>';
            TTransaction::close(); // fecha a transao.
        }
        catch (Exception $e)
        {
            new TMessage('error', $e->getMessage());
        }
    }
}
```

## Uso no seu projeto

- Copie e adapte o bloco acima para o seu projeto, na pasta `app/` — seu sistema decide o lugar certo (control, model e afins, conforme o tipo do código). O código do Tutor é ponto de partida, não versão final.
- Troque banco (`'samples'`), modelos, labels e validações pelos do seu domínio.
- Teste no seu ambiente com seus dados antes de levar para produção.
