import pandas as pd
import matplotlib.pyplot as plt
import dataframe as df

sales_17 = pd.read_csv('../../resource/SalesData/Installation_2017.csv')
sales_18 = pd.read_csv('../../resource/SalesData/Installation_2018.csv',error_bad_lines=False)
sales_19 = pd.read_csv('../../resource/SalesData/Installation_2019.csv')
sales_20 = pd.read_csv('../../resource/SalesData/Installation_2020.csv')
sales_21 = pd.read_csv('../../resource/SalesData/Installation_2021.csv')

# 순 이익 : 17,18 - Actual Value, 19,20,21 - Net
revenue_17 = sales_17.loc[:,['Month','Region','Category','Actual Value']]
revenue_18 = sales_18.loc[:,['Month','Region','Category','Actual Value']]
revenue_19 = sales_19.loc[:,['Month','Region','Category','Net']]
revenue_20 = sales_20.loc[:,['Month','Region','Category','Net']]
revenue_21 = sales_21.loc[:,['Month','Region','Category','Net']]

# 컬럼명 변경
revenue_17.rename(columns = {'Actual Value' : 'Net'}, inplace = True)
revenue_18.rename(columns = {'Actual Value' : 'Net'}, inplace = True)

print(revenue_17)
# Nan 값 0으로
revenue_17 = revenue_17['Net'].fillna(0)
revenue_18 = revenue_18['Net'].fillna(0)
revenue_19 = revenue_19['Net'].fillna(0)
revenue_20 = revenue_20['Net'].fillna(0)
revenue_21 = revenue_21['Net'].fillna(0)

years = [revenue_17, revenue_18, revenue_19, revenue_20, revenue_21]
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

print(revenue_18['Month'].unique())

# revenue_17
year = 2017
for y in years :
    plt.cla()
    print(year)
    revenue = {}
    for m in months :
        r = sum(y[y['Month'] == m]['Net'])
        revenue[m] = r
    print(revenue)
    title = 'Revenue of '+str(year)
    plt.title(title)
    plt.plot(list(revenue.keys()), list(revenue.values()))
    plt.savefig('../../resource/Plot/'+title+'.png')
    year += 1
