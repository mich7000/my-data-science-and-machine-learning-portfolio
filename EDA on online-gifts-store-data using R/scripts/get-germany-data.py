import pandas as pd 


xls = pd.ExcelFile('data/Online Retail.xlsx')
data= xls.parse('sheet1')
ger= data[data['Country'].isin(['Germany'])]
ger.to_csv('data/raw-germany.csv')