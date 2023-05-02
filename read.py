import pandas as pd

# Open the Excel file
excel_file = pd.ExcelFile('sample.xlsx')

# Check the sheet names
print(excel_file.sheet_names)

# Access a specific worksheet
df = pd.read_excel(excel_file, sheet_name='Sheet1')
for i in df:
    print(i+" ")
