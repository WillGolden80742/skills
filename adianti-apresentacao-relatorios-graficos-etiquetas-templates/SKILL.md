---
name: adianti-apresentacao-relatorios-graficos-etiquetas-templates
description: Relatórios tabulares, PDF, Danfe, gráficos, dashboard, barcode/QR, templates HTML e carrossel
triggers: ["relatório tabular", "TabularReport", "HTML para PDF", "PDF design", "Danfe", "gráfico linhas", "gráfico barras", "dashboard", "barcode", "qrcode", "etiquetas", "template básico", "carousel", "jumbotron"]
---

# Skill Adianti — Relatórios, Gráficos, Etiquetas e Templates

Fonte: Tutor menu Apresentação > Relatórios, Gráficos, Etiquetas, Templates. `app/control/Presentation/Report|Chart|Label|Templates|Extending/`.

## Páginas cobertas

Relatórios: `TabularReport`, `TabularReportQueryView`, `TabularReportView`, `TemplateInvoiceView`, `DatagridCashRegisterView`, `DocumentHtmlPdfView`, `PDFDesignShapesView`, `PDFDesignNFEView`.
Gráficos: `LineChartView`, `BarChartView`, `ColumnChartView`, `PieChartView`, `DashboardView`.
Etiquetas: `FormBarcodeView`, `FormQrcodeView`, `FormScreenLabelsView`.
Templates: `TemplateViewBasicView`, `TemplateViewMaskView`, `TemplateRepeatView`, `CircleView`, `CarouselView`, `AccordionView`, `TemplateHtmlManualForm`, `JumbotronView`.

## Padrões

```php
// Relatório tabular sobre coleção
$rep = new TTable; // ou BootstrapDatagridWrapper somente-leitura
TTransaction::open('samples');
$objects = Customer::getObjects($criteria);
foreach ($objects as $o) { /* linha */ }
TTransaction::close();

// Relatório com query manual
$conn = TTransaction::get();
$result = $conn->query('SELECT c.name, SUM(s.value) total FROM sale s JOIN customer c ON ... GROUP BY 1');

// HTML -> PDF (DocumentHtmlPdfView usa dompdf/wkhtmltopdf)
$html = new THtmlRenderer('app/resources/invoice.html');
$html->enableSection('main', ['customer' => $name, 'total' => $total]);
$html->enableTranslation();
$doc = $html->getContents();
// + botão "Gerar PDF" que converte $doc

// PDF desenho (fatura/Danfe)
$pdf = new FPDF; // via TCPDF/FPDF wrapper do Adianti
$pdf->AddPage(); $pdf->SetFont('Arial','B',12); $pdf->Cell(0,10,'DANFE');
$pdf->Output('files/danfe.pdf');

// Gráficos (TChartBase / Google Charts via templates)
$chart = new TBarChart(700, 400);
$chart->addSerie('Vendas', [10,20,30]);
$chart->setLabels(['Jan','Fev','Mar']);
$vbox->add($chart);
// ou THtmlRenderer('app/resources/google_bar_chart.html') com dados

// Dashboard (DashboardView): TNumericIndicator + charts + panels
$ind = new TNumericIndicator('Vendas', 1500, 'fa:cart green');

// Barcode / QRCode
$bar = new TBarcodeDisplay('123456789', 'code128');
$qr  = new TQRCodeDisplay('https://...', 200);
$form->addField(new TBarCodeInputReader('barcode'));
$form->addField(new TQRCodeInputReader('qrcode'));

// Template básico com máscaras e repetição
$tpl = new THtmlRenderer('app/resources/template_masks.html');
$tpl->enableSection('main', $data + ['date' => date('d/m/Y')]);
$tpl->enableSection('details', $items, true); // repeat
$vbox->add($tpl);
```

## Recursos HTML

`app/resources/*.html` (`invoice.html`, `customer.html`, `google_*_chart.html`, `carousel.html`, `jumbotron.html`, `template_masks.html`, `page*.html`).

## Regras

- Relatórios tabulares reaproveitam `TDataGrid` sem ações, só leitura + `TPageNavigation`.
- PDF: gerar HTML primeiro, depois converter — nunca monte PDF na mão se puder usar template.
- Gráficos Google precisam de internet; `TBarChart/TLineChart/TPieChart` são offline (GD).
