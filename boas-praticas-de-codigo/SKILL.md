---
name: boas-praticas-de-codigo
description: Boas práticas de OOP, Object Calisthenics, MVC e filosofia Rails — a forma de pensar e estruturar código, não sintaxe.
triggers: ["boas praticas", "boa pratica", "object calisthenics", "calistenics", "mvc", "model view controller", "rails", "ruby on rails", "filosofia rails", "convention over configuration", "convencao sobre configuracao", "dry", "don't repeat yourself", "solidao", "orientacao a objetos", "oop", "encapsulamento", "coesao", "baixo acoplamento", "separacao de concerns", "principios solid", "single responsibility", "responsabilidade unica", "composicao sobre heranca", "codigo limpo", "clean code", "arquitetura rails", "convenções rails", "fat model thin controller", "skinny controller", "service object", "poro", "ruby way", "mvc rails", "rails way", "design de classes", "organizacao codigo", "estrutura projeto", "arquitetura mvc", "boas praticas ruby", "boas praticas rails", "design oop", "coesao alta", "acoplamento baixo", "tell don't ask", "principio tell", "law of demeter", "lei de demeter", "demeter", "open closed", "aberto fechado", "liskov", "segregacao interface", "inversao dependencia", "injeção dependencia", "sandi metz", "poo", "modelos mentais codigo", "filosofia programacao", "como pensar codigo"]
---

# Skill: Boas Práticas — Object Calisthenics, MVC e Filosofia Rails

## Abordagem

Este skill não ensina sintaxe de Ruby/Rails. Ensina **modelos mentais**, princípios e a **forma de pensar** que leva a código sustentável e expressivo. Sirva como um mentor ao lado do usuário, explicando o *porquê* das práticas, não apenas o *como*.

---

## 1. Filosofia Ruby on Rails (O Rails Way)

### Convenção sobre Configuração (CoC)

- O framework já sabe o que você quer na maioria das vezes. Siga as convenções de nomenclatura e o framework infere o resto.
- **Como pensar:** "Qual é o caminho óbvio? O nome da tabela é o plural do modelo. O controller chama igual ao modelo no plural. A view segue o nome da action. Não force o framework a adivinhar; seja previsível."
- **Resultado:** Menos arquivos de configuração, menos decisões triviais, mais foco no que é único do seu domínio.

### DRY — Don't Repeat Yourself

- Todo conhecimento deve ter uma representação única, não ambígua e autoritária dentro do sistema.
- **Como pensar:** "Se eu precisar mudar isso, quantos lugares vou ter que tocar? Se > 1, extraia."
- **Aplicação:** Extraia lógica duplicada para métodos, partials, helpers, concerns ou service objects. Mas DRY não é dogma — duplicação deliberada às vezes vence abstração prematura (veja DHH sobre "duplication over wrong abstraction").

### Fat Model, Skinny Controller

- **Controller:** Só orquestra: recebe a requisição, chama o model, renderiza a view. Não contém regras de negócio.
- **Model:** É a **camada de dados** (shameless copy do ActiveRecord do Rails). Contém persistência, regras de negócio, validações, associações, callbacks. Tudo em um lugar só.
- **A regra de ouro:** Controller não sabe SQL. Controller não sabe onde os dados estão. Controller só pergunta ao Model: "me dá o que eu preciso", e o Model resolve.
- **Como pensar:** "Se uma action do controller tem mais de 4-5 linhas, a lógica pertence ao model."
- **Estrutura no Rails:**
  ```
  app/
    controllers/    → orquestração fina (pergunta ao model, devolve view)
    models/         → camada DE DADOS + regras de negócio (ActiveRecord)
    views/          → apresentação simples
  ```
- **Não existe camada Service em Rails clássico.** O Model é o dono dos dados. Se o model cresce, você extrai para concerns, query objects, value objects — mas o model CONTINUA sendo a porta de entrada dos dados.
- **Cópia descarada do Rails:** No Rails, você nunca cria um `UserService` para buscar usuários. Você chama `User.find(1)`, `User.where(active: true)`. O Model É a API de dados. Faça o mesmo em qualquer linguagem.
- **Como pensar:** "O Controller conversa com o Model. O Model conversa com o banco. O Controller NUNCA conversa com o banco."
- **Exemplo concreto (PHP seguindo Rails):**
  ```php
  // RUIM: Service layer separada
  class UserController {
      public function show(int $id) {
          $service = new UserService();
          $data = $service->getUserWithOrders($id);
          $this->render('show', $data);
      }
  }
  class UserService {
      public function getUserWithOrders(int $id) {
          $user = UserModel::find($id);
          $orders = OrderModel::where('user_id', $id);
          return ['user' => $user, 'orders' => $orders];
      }
  }

  // BOM: Model como camada de dados (Rails way)
  class UserController {
      public function show(int $id) {
          $user = User::find($id); // Model É a camada de dados
          $this->render('show', ['user' => $user]);
      }
  }
  class User {
      public static function find(int $id): ?self { /* SQL aqui */ }
      public function orders(): array { return Order::where('user_id', $this->id); }
  }
  ```

### Aplicativo Ruby, não Aplicativo Rails

- Rails é um framework, mas você escreve Ruby. Não force tudo a ser uma concern do ActiveSupport.
- **Como pensar:** "Isso é uma regra de negócio pura? Então é uma classe Ruby comum (PORO), sem herdar de ActiveRecord."
- **PORO (Plain Old Ruby Object):** Use classes Ruby simples sempre que possível. Elas são mais fáceis de testar, entender e manter.

### Testes São Cidadãos de Primeira Classe

- Rails nasceu com testing em mente. Escreva testes primeiro (TDD) ou pelo menos junto.
- **Como pensar:** "Se eu não sei testar, não sei o que o código deveria fazer. Teste não é extra; é especificação executável."

### Minúsculo (Tiny) é Lindo

- Métodos pequenos, classes pequenas, arquivos pequenos.
- **Como pensar:** "Se um método não cabe na tela sem scroll, ele faz mais de uma coisa."

---

## 2. Object Calisthenics (9 Regras)

Criado por Jeff Bay, são **exercícios rigorosos** para treinar o cérebro a escrever OOP melhor. Não são regras absolutas para produção — são *pesos na academia*. Quando você treina com elas, seu código natural fica melhor.

### Regra 1 — Apenas Um Nível de Indentação por Método

- **O que:** Todo método deve ter no máximo um nível de indentação. Sem `if` dentro de `loop` dentro de `if`.
- **Como pensar:** "Se eu preciso de indentação aninhada, esse método deveria delegar a outro método."
- **Por quê:** Força a extrair lógica, revela a verdadeira estrutura do problema.

### Regra 2 — Não Use `else`

- **O que:** Elimine `else`. Use early returns, polimorfismo, guard clauses ou Hash de dispatch.
- **Como pensar:** "Cada `else` é um caminho condicional escondido. Extraia para um método que retorna cedo ou use um objeto que já sabe o que fazer."
- **Exemplo:**
  ```ruby
  # Ruim
  def status
    if active?
      "ativo"
    else
      "inativo"
    end
  end

  # Bom
  def status
    return "ativo" if active?
    "inativo"
  end

  # Melhor (polimorfismo)
  # Cada objeto sabe seu próprio status
  ```

### Regra 3 — Wrappe Todos os Primitivos e Strings

- **O que:** Não use `int`, `string`, `boolean` soltos como parâmetros ou atributos. Crie classes que os envolvam.
- **Como pensar:** "CPF não é string. Money não é float. Email não é string. O valor só existe no contexto do seu tipo."
- **Por quê:** Primitivos são anêmicos. Um objeto `CPF` pode validar, formatar, extrair dígitos. Um `String` solto não diz nada.

### Regra 4 — Objetos com Primeira Classe / Coleções

- **O que:** Toda coleção deve ser a única propriedade de sua própria classe.
- **Como pensar:** "Uma lista de itens não é só array — é um `Carrinho`, `Fila`, `Inventario`. Crie a classe que a envolve com métodos de domínio."
- **Por quê:** Coleções soltas espalham lógica de filtragem/busca pelo sistema.

### Regra 5 — Apenas Um Ponto por Linha

- **O que:** Nunca encadeie mais de um `.` por linha (uma exceção: DSLs).
- **Como pensar:** "Cada ponto é um acoplamento. `cliente.ultimoPedido.total` quebra a Lei de Demeter."
- **Lei de Demeter:** Fale apenas com seus amigos imediatos. Não atravesse a hierarquia de objetos.
- **Como pensar:** "Não pergunte ao cliente qual o último pedido para somar o total. Peça ao cliente `total_ultimo_pedido`."

### Regra 6 — Não Abrevie Nomes

- **O que:** Nomes devem ser completos, expressivos e revelar intenção.
- **Como pensar:** "`calc_val_tot` não diz nada. `calcular_valor_total_pedido` diz exatamente o que faz. 3 palavras > 3 letras."
- **Tamanho ideal:** Quanto maior o escopo, maior o nome. `i` para índice de loop de 3 linhas. `calculate_monthly_subscription_total` para método público.

### Regra 7 — Mantenha Todas as Entidades Pequenas

- **O que:** Nenhuma classe > 50 linhas. Nenhum pacote > 10 arquivos. Nenhum arquivo sozinho > 50 linhas.
- **Como pensar:** "Se passou de 50 linhas, tem responsabilidade demais. Extraia."
- **Efeito colateral:** Força composição, coesão, e previne God Classes.

### Regra 8 — Nenhuma Classe com Mais de 2 Atributos de Instância

- **O que:** Cada classe pode ter no máximo 2 variáveis de instância. Se precisar de mais, crie objetos de valor.
- **Como pensar:** "Endereço com rua, numero, bairro, cidade, cep não são 5 atributos. São 1 objeto `Endereco` com 5 atributos internos."
- **Efeito:** Força composição profundamente. Uma `Pessoa` não tem `nome, idade, rua, numero, bairro, cidade, cep, telefone, email`. `Pessoa` tem `nome, idade, endereco, contato`.

### Regra 9 — Não Use Getters/Setters (Tell, Don't Ask)

- **O que:** Não exponha estado interno. Não pergunte ao objeto seu estado para decidir por ele.
- **Princípio Tell, Don't Ask:** Diga ao objeto *o que fazer*, não pergunte seus dados para fazer você mesmo.
- **Como pensar:**
  - Ruim: `if carro.gasolina > 0 then carro.acelerar`
  - Bom: `carro.acelerar` (ele mesmo decide se tem gasolina)
  - Ruim: `if usuario.idade >= 18 then ...`
  - Bom: `usuario.pode_votar?`

---

## 3. MVC — Model-View-Controller (Além do Rails)

### A Essência

MVC é uma **separação de preocupações** em 3 camadas:

| Camada | O Que É | O Que NÃO É |
|--------|---------|-------------|
| **Model** | **Camada de dados + regras de negócio** (ActiveRecord no Rails). É quem sabe buscar, salvar, validar e executar regras. | Uma classe anêmica com só getters/setters |
| **View** | Apresentação dos dados ao usuário | Lógica condicional complexa |
| **Controller** | Orquestração: entrada → saída. Pergunta ao Model, devolve a View. | Onde moram as regras de negócio OU consultas ao banco |

### A Regra Mais Importante do MVC no Rails

**O Controller NUNCA acessa o banco de dados diretamente.** Ele sempre pergunta ao Model.

```ruby
# RUIM — Controller acessa dados
class UsersController < ApplicationController
  def index
    @users = User.where(active: true).order(created_at: :desc)
    #            ^^^^ O controller não deveria saber SQL
  end
end

# BOM — Controller pergunta ao Model
class UsersController < ApplicationController
  def index
    @users = User.active_recent # O Model encapsula a consulta
  end
end
```

### Como Pensar MVC

- **O Controller é um recepcionista:** Ele recebe o pedido, CHAMA O MODEL, entrega a view. Ele não cozinha a comida E NEM BUSCA OS INGREDIENTES.
- **O Model é o especialista + despensa:** Ele sabe as regras, validações, E também SAI ONDE OS DADOS ESTÃO. No Rails, Model herda de ActiveRecord — ele É a ponte com o banco.
- **A View é o cardápio/apresentação:** Ela só exibe. Se tem `if` na view, provavelmente pertence a um helper, decorator ou presenter.

### Model é a Camada de Dados (Cópia Descarada do Rails)

No Rails, não existe `UserService` ou `UserRepository`. O próprio `User` (que herda de `ActiveRecord::Base`) é quem faz:

```ruby
# Isto é Rails puro — o Model É a camada de dados
user = User.find(1)                    # SELECT * FROM users WHERE id = 1
user.update(name: 'João')              # UPDATE users SET name = 'João' WHERE id = 1
user.orders.each { |o| puts o.total }  # SELECT * FROM orders WHERE user_id = 1
```

**Tradução para outras linguagens:** Crie classes Model que encapsulam consultas como métodos estáticos ou de classe. O Controller chama `User::find($id)`, `User::activeUsers()`, `User::withRecentOrders()` — nunca SQL solto no controller.

### Onde Colocar Lógica no Rails

```
app/
  controllers/    → orquestração fina (chama Model, ponto)
  models/         → **camada de dados + regras de negócio** (shameless copy do ActiveRecord)
  views/          → apresentação simples
  concerns/       → módulos compartilhados entre models (não services!)
  queries/        → consultas complexas que poluem o model (Query Objects)
  forms/          → validação de formulários que não mapeiam 1:1 com model (Form Objects)
  presenters/     → lógica de exibição que a view não deveria ter
  policies/       → autorização (ex: Pundit)
  values/         → objetos de valor (Value Objects)

# ⚠️ NÃO CRIE uma camada Service a menos que seja estritamente necessário.
# O Model já é a camada de dados. Service layer é anti-padrão no Rails clássico.
```

### Princípios Relacionados

| Princípio | Máxima |
|-----------|--------|
| **Single Responsibility** | Cada classe tem uma razão para mudar |
| **Open/Closed** | Aberta para extensão, fechada para modificação |
| **Liskov** | Subtipos devem substituir seus tipos base sem quebrar |
| **Interface Segregation** | Muitas interfaces específicas > uma interface genérica |
| **Dependency Inversion** | Dependa de abstrações, não de concretos |
| **Composição > Herança** | Herança é acoplamento. Composição é flexibilidade |
| **Lei de Demeter** | Só fale com seus vizinhos imediatos |

---

## 4. Modelos Mentais para o Dia a Dia

### "Programação Orientada a Objetos é sobre Mensagens"

— Alan Kay, inventor do OOP.

Objetos não são cápsulas de dados. São **entidades que se comunicam por mensagens**. A pergunta não é "o que esse objeto tem?" mas "o que esse objeto faz?".

### "Duplicação é Melhor que Abstração Prematura"

— DHH, criador do Rails.

Nem toda repetição deve ser extraída imediatamente. Às vezes duas coisas parecem iguais mas mudarão em direções diferentes. Espere até ver o padrão 3 vezes antes de abstrair.

### "Testar é Projetar"

Testes não são segurança. São **feedback de design**. Se uma classe é difícil de testar, o design está errado — não o teste.

### "Código é Escrito uma Vez, Lido Muitas"

O tempo de leitura domina. Otimize para legibilidade. Nomes descritivos > comentários. Extrair métodos > código inline denso.

### "Ser Expressivo > Ser Curto"

Ruby é uma linguagem feita para programadores felizes. Use `unless` em vez de `if !`. Use `until` em vez de `while !`. O código deve fluir como inglês.

---

## Como Usar Este Skill no Contexto do Projeto

Quando revisar código ou projetar uma nova feature:

1. **Identifique os objetos do domínio** — quais são as entidades e seus papéis?
2. **Aplique MVC** — cada regra de negócio sabe onde mora?
3. **Treine com Object Calisthenics** — especialmente as regras 1 (indentação), 5 (um ponto), e 9 (tell, don't ask)
4. **Pergunte-se:** "Se eu ler isso daqui 6 meses, vou entender?"
5. **Pergunte-se:** "Qual é o caminho mais simples que funciona?"

## Leituras Recomendadas

- *Practical Object-Oriented Design in Ruby* — Sandi Metz (POODR)
- *99 Bottles of OOP* — Sandi Metz & Katrina Owen
- *The Rails Doctrine* — rubyonrails.org/doctrine (em português: doutrina Rails)
- *Object Calisthenics* — Jeff Bay (PDF original, parte do livro *ThoughtWorks Anthology*)
