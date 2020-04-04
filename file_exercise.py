
# insatll pandas
# insatll xlrd

import pandas as pd
file = pd.ExcelFile("/Users/ranjan/Project/learning-python/original.xlsx")

print(file.sheet_names)
print('\n')
sheet_sales = file.parse('sales')
print(sheet_sales)
print('\n')
print('Sheet datatype', type(sheet_sales))

# print column data
print(sheet_sales.Amount)

print('\n')
# print row data

print(sheet_sales.loc[0, 'Amount'])

print(type(sheet_sales['Amount']))

print('\n')

print(sheet_sales.loc[sheet_sales['Amount'] > 2000])
print('\n')
print(sheet_sales.loc[sheet_sales['Amount'] > 200]['Customer'].unique())
print('\n')
for name in sheet_sales.loc[sheet_sales['Amount'] > 200]['Customer'].unique():
    print(name)
