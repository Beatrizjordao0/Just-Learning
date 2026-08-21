import pandas as pd
from openpyxl import workbook

arquivo = pd.read_excel('Planilha-Clarity.xlsx', sheet_name=3)

print(arquivo.head(8))