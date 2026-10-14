---
name: adianti-apresentacao-dialogos
description: TMessage, TQuestion, TInputDialog, TToast, TAlert e diálogos de informação/aviso/erro
triggers: ["TMessage", "TQuestion", "diálogo informação", "diálogo aviso", "diálogo erro", "input dialog", "toast", "alert", "TAlert", "pergunta confirmação"]
---

# Skill Adianti — Apresentação: Diálogos

Fonte: Tutor menu Apresentação > Diálogos. `app/control/Presentation/Dialogs/`.

## Páginas cobertas

`DialogInformationView`, `DialogWarningView`, `DialogErrorView`, `DialogQuestionView`, `DialogInputView`, `DialogToastView`, `AlertView`.

## Padrões

```php
// info / warning / error
new TMessage('info', 'Gravado com sucesso');
new TMessage('warning', 'Atenção: verifique os dados');
new TMessage('error', $e->getMessage());

// pergunta com callback
new TQuestion('Deseja excluir?', new TAction([$this, 'onDelete'], ['key' => $id]));

// input dialog
$input = new TEntry('reason');
new TInputDialog('Informe o motivo', $input, new TAction([$this,'onConfirm']));

// toast (canto da tela)
TToast::show('success', 'Salvo!', 'top right', 'fa:check');
// ou new TToast(...)

// alert inline (dentro da página, não modal)
$alert = new TAlert('warning', 'Texto do alerta');
$vbox->add($alert);
```

## Regras

- `TMessage` trava a tela até confirmar; `TToast` não trava.
- `TQuestion` exige `TAction` com parâmetros — o segundo clique executa.
- Em `onDelete`, recarregue com `onReload` após confirmar.
- Template com `use_swal: 1` renderiza diálogos via SweetAlert (ver `Template.configure` no `index.php` do Tutor).
