"""
Y (월별 총 매출) Parsing
"""
import pandas as pd
rev = pd.read_csv('../../resource/SalesData/Whole Revenue_fillTerritory.csv')

# Rev 월 변경
months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,
          'October':10,'November':11,'December':12}
for row in rev.index :
    for month in months.keys():
        if (rev['Month'][row] == month):
            rev['Month'][row] = months[month]

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
years = [2017, 2018, 2019, 2020, 2021]
revenue_monthly ={}
for y in years:
    if (y == 2021):
        months= [1, 2, 3, 4, 5, 6, 7]
    for m in months:
        key = str(y) + '-' + str(m)
        revenue_monthly[key] = round(sum(rev[(rev['Year'] == y)&(rev['Month'] == m)]['Net']),2)

revenue_monthly_df = pd.DataFrame(list(revenue_monthly.items()),columns=['Date','Net'])

# 코로나 이전 데이터 (2017.1-2020.2)
revenue_beforeCovid = revenue_monthly_df[pd.DatetimeIndex(revenue_monthly_df['Date']).year != 2021]
revenue_beforeCovid = revenue_beforeCovid.drop(revenue_beforeCovid.index[-10:])

revenue_beforeCovid.to_csv('../../resource/Model_Input/Monthly_Net_BeforeCorona.csv',index=False)
revenue_monthly_df.to_csv('../../resource/Model_Input/Monthly_net.csv',index=False)