---
name: adianti-apresentacao-formularios
description: BootstrapFormBuilder, campos, validação, máscaras, seeks, selects DB, upload, assinatura e interações dinâmicas
triggers: ["BootstrapFormBuilder", "TEntry", "TCombo", "validação formulário", "máscara input", "seekbutton", "DBCombo", "htmleditor", "upload imagem", "signature pad", "fieldlist", "formulário bootstrap", "TRequiredValidator"]
---

# Skill Adianti — Apresentação: Formulários

Fonte: Tutor menu Apresentação > Formulários (+ Extras com eventos). `app/control/Presentation/Forms/` e `Extras/`.

## Páginas cobertas (resumo)

`FormCustomView`, `FormBuilderView`, `FormComponentsView`, `FormBuilderGridView`, `FormVerticalBuilderView`, `ModalForm`, `FormNestedBuilderView`, `FormStaticBuilderView`, `FormFieldListView`, `FormCheckListView`, `FormMaskView`, `FormValidationView`, `FormSeekButtonView`, `FormStaticSelectionView`, `FormDBAutoSelectionView`, `FormLikertScaleView`, `FormClientInteractionsView`, `FormInteractionsView`, `FormEnableDisableView`, `FormShowHideRowsView`, `FormSortView`, `FormDBSortView`, `FormHtmlEditorView`, `FormCodeReader`, `FormImageUploader`, `FormSignaturePad`, + Extras (`FormEventsView`, `FormButtonStyleView`, `FormExpanderView`, `FormConditionalView`, `FormReusableControl`, etc).

## Padrão base (FormBuilderView real)

```php
$this->form = new BootstrapFormBuilder;
$this->form->setFormTitle(_t('Bootstrap form'));
$this->form->generateAria();

$id = new TEntry('id');
$description = new TEntry('description');
$password = new TPassword('password');
$created = new TDateTime('created');
$expires = new TDate('expires');
$value = new TEntry('value');
$color = new TColor('color');
$weight = new TSpinner('weight');
$type = new TCombo('type');
$text = new TText('text');

$id->setEditable(FALSE);
$created->setMask('dd/mm/yyyy hh:ii');
$expires->setMask('dd/mm/yyyy');
$created->setDatabaseMask('yyyy-mm-dd hh:ii');
$expires->setDatabaseMask('yyyy-mm-dd');
$value->setNumericMask(2, ',', '.', true);
$weight->setRange(1,100,0.1);
$type->addItems(['a'=>'Type a','b'=>'Type b']);

$this->form->addFields([new TLabel('ID')], [$id]);
$this->form->addFields([new TLabel('Description')], [$description]);
$this->form->addAction('Save', new TAction([$this,'onSave']), 'fa:save green');
parent::add($this->form);
```

## Validação / máscara / seek / DB selects

```php
$name->addValidation('Name', new TRequiredValidator);
$value->addValidation('Value', new TNumericValidator);
$email->addValidation('Email', new TEmailValidator);

// seekbutton (busca com lupa)
$seek = new TSeekButton('customer_id', 'customer_name', 'CustomerDataGridView', 'input_search');
$seek->setSize('100%');

// selects DB automáticos
$combo = new TDBCombo('category_id', 'samples', 'Category', 'id', 'name');
$select = new TDBSelect('city_id', 'samples', 'City', 'id', 'name');
$multi = new TDBMultiSearch('groups', 'samples', 'Group', 'id', 'name');
$unique = new TDBUniqueSearch('customer_id', 'samples', 'Customer', 'id', 'name');
```

## FieldList / CheckList / SortList

```php
$fieldlist = new TFieldList('items');
$fieldlist->addField('<b>Product</b>', new TDBUniqueSearch('product[]','samples','Product','id','description'), ['width'=>'60%']);
$fieldlist->addField('<b>Qtd</b>', new TEntry('qtd[]'), ['width'=>'20%']);
$fieldlist->enableSorting();
$form->addField($fieldlist);
```

## Upload / assinatura / QR/barcode reader

```php
$photo = new TFile('photo'); // ou TMultiFile, TImageCropper
$photo->setAllowedExtensions(['jpg','png']);
$sig = new TSignaturePad('signature');
$barcode = new TBarCodeInputReader('barcode');
$qrcode = new TQRCodeInputReader('qrcode');
```

## Interações dinâmicas

```php
// habilita/desabilita, mostra/esconde, changeAction
$combo->setChangeAction(new TAction([$this, 'onChangeType']));
public static function onChangeType($param) {
    TCombo::reload('form_name', 'city_id', $options);
    TEntry::enableField('form_name', 'other');
    TForm::showField('form_name', 'extra_row');
}
```

## Regras

- Sempre `setSize('100%')` em formulários bootstrap para responsivo.
- `addValidation` roda no `onSave` via `$this->form->validate()`.
- `getData()` retorna stdClass; `setData($obj)` preenche.
- Reutilizável MVC: ver `FormReusableControl` (form como componente).
