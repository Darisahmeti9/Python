import pandas as pd

from Modul13.array_manipulation import total_sum

products=['Apples','Bananas','Oranges','Grapes','Pineapples']

seles=[150,200,180,90,60]

sales_series=pd.Series(sales,index=products)
print(sales_series)

print(sales_series['Grapes'])

total_sales=sales_series.sum()
print(total_sales)

best_sell=sales_series.inxmax()
print(best_sell)