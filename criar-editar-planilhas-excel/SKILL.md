---
name: criar-editar-planilhas-excel
description: Manipula arquivos de planilhas Excel (.xlsx, .xlsm, .csv, .tsv). Use para criar, editar, ler ou converter arquivos de planilhas.
triggers: ["planilha", "excel", "xlsx", "csv", "spreadsheet", "criar planilha", "editar planilha", "arquivo excel", "microsoft excel", "planilha excel", "dados tabela", "tabela excel", "formula excel", "openpyxl", "pandas excel", "ler planilha", "importar csv", "exportar csv", "converter csv", "tsv", "arquivo csv", "planilha calculo", "grafico excel", "formatar celula", "fonte planilha", "cor celula", "borda planilha", "sum excel", "abrir planilha", "modificar planilha", "salvar excel", " workbook", " worksheet"]
---

# Skill XLSX - Manipulação de Planilhas

## Bibliotecas Disponíveis

- **pandas**: Leitura, análise e manipulação de dados tabulares
- **openpyxl**: Criação e edição de arquivos Excel com fórmulas e formatação

## Leitura de Arquivos

```python
import pandas as pd

df = pd.read_excel('arquivo.xlsx')
df = pd.read_csv('arquivo.csv', sep=',')
```

## Criação de Arquivos

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()
sheet = wb.active
sheet['A1'] = 'Dado'
sheet['B1'] = 100
sheet['B2'] = '=SUM(A1:A10)'
wb.save('saida.xlsx')
```

## Regras Importantes

- **Sempre use fórmulas Excel**, nunca calcule valores em Python e hardcode o resultado
- **Texto em azul**: valores fixos inseridos pelo usuário
- **Texto em preto**: fórmulas e cálculos
- **Zeros**: use formatação para exibir "-" ao invés de 0

## Validação de Fórmulas

Execute o script de recalc após criar/editar:
```bash
python scripts/recalc.py arquivo.xlsx
```

## Exemplo Completo

```python
from openpyxl import Workbook
from openpyxl.styles import Font

wb = Workbook()
ws = wb.active
ws.title = "Dados"

ws['A1'] = 'Produto'
ws['B1'] = 'Valor'
ws['A1'].font = Font(bold=True)
ws['B1'].font = Font(bold=True)

ws['A2'] = 'Item A'
ws['B2'] = 100
ws['A3'] = 'Item B'
ws['B3'] = 200
ws['B4'] = '=SUM(B2:B3)'

wb.save('relatorio.xlsx')
```
