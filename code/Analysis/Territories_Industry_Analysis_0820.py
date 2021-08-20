import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

revenue = pd.read_csv('../../resource/SalesData/Whole Revenue_fillTerritory.csv')
lead = pd.read_csv('../../resource/CleansedData/ZohoCRM/Leads_001_IndustryCleansed.csv')
deal_origin = pd.read_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillIndustry.csv')

# deal의 territory 'Amazon/CS'를 Amazon으로 이름 변경
idx = deal_origin[deal_origin['Territory_fin'] == 'Amazon/CS'].index
deal_origin.at[idx,'Territory_fin']= 'Amazon'
deal_origin.to_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillIndustry.csv',index=False)

deal =  pd.read_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillIndustry.csv')

lead = lead.loc[:, ['Created Time', 'Industry Fin']]
deal = deal.loc[:, ['Created Time', 'Stage', 'Territory_fin', 'Industry Fin']]



# 날짜 DateTime으로 변경
lead['Created Time'] = pd.to_datetime(lead['Created Time'])
deal['Created Time'] = pd.to_datetime(deal['Created Time'])

# year, month 열 추가
lead['year'] = pd.DatetimeIndex(lead['Created Time']).year
lead['month'] = pd.DatetimeIndex(lead['Created Time']).month

deal['year'] = pd.DatetimeIndex(deal['Created Time']).year
deal['month'] = pd.DatetimeIndex(deal['Created Time']).month

# Rev 월->숫자 변경
months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,
          'October':10,'November':11,'December':12}
for row in revenue.index :
    for month in months.keys():
        if (revenue['Month'][row] == month):
            revenue['Month'][row] = months[month]


# 1-1. Territory별 Deal Success Rate
West1 = deal[deal['Territory_fin'] == 'West 1']
West2 = deal[deal['Territory_fin'] == 'West 2']
South = deal[deal['Territory_fin'] == 'South']
North = deal[deal['Territory_fin'] == 'North']
East = deal[deal['Territory_fin'] == 'East']
Overseas = deal[deal['Territory_fin'] == 'Overseas']
Amazon = deal[deal['Territory_fin'] == 'Amazon']

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
territories = ['West1','West 2','South','North','East','Overseas','Amazon']
dfs = [West1,West2,South,North,East,Overseas,Amazon]
years = [2017,2018,2019,2020,2021]

cnt = 0
# terri 하나만
for df in dfs:
    terri_dict = {}
    for year in years:
        if (year == 2021) :
            months = [1, 2, 3, 4, 5, 6, 7]
        for month in months:
            key = str(year) +'-'+ str(month)
            df_terri = df[(df['year'] == year) & (df['month'] == month)]
            if not df_terri.empty :
                rate = len(df_terri[df_terri['Stage'].str.contains('5|6|7')]) / len(df_terri)
                terri_dict[key] = rate
            else: # 해당 month 데이터 존재하지않음
                terri_dict[key] = 0
    plt.figure(figsize=(15, 8))
    plt.title('Monthly Deal Success Rate By Territories:' + territories[cnt] + ' (2017-2021)', fontsize=20)
    plt.plot(list(terri_dict.keys()), list(terri_dict.values()))
    plt.xticks(rotation=90)
    plt.ylabel('Rs', fontsize=12)
    title = 'Monthly Deal Success Rate By Territories ' + str(territories[cnt]) + ' (2017-2021)'
    save_dir = '../../resource/Plot/' + title
    plt.savefig(save_dir + '.png')
    save_dir = '../../resource/PlotCSV/' + title
    rev = pd.DataFrame(list(terri_dict.items()),
                       columns=['x', 'y'])
    rev.to_csv(save_dir + '.csv', index=False)
    cnt += 1

# 2-1. Industry별 Deal Success Rate
['Clinic','Fitness','Private Enterprise','Hospital','Others_Others Corporate','Public Association','Others_Individual','Others_Aesthetic' 'Hotel' 'Military' 'Academic' 'Others_etc']