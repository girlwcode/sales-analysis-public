import pandas as pd

sales_18 = pd.read_csv('../../resource/SalesData/Installation_2018.csv')
sales_19 = pd.read_csv('../../resource/SalesData/Installation_2019.csv')


sales_18.at[sales_18[sales_18['Region'] == 'Academia'].index.tolist(),'Region'] = 'West 1'
sales_19.at[sales_19[sales_19['Region'] == 'Region'].index.tolist(),'Region'] = 'West 1'
sales_19.at[sales_19[sales_19['Region'] == 'West '].index.tolist(),'Region'] = 'West 1'

sales_18.to_csv('../../resource/SalesData/Installation_2018.csv')
sales_19.to_csv('../../resource/SalesData/Installation_2019.csv')