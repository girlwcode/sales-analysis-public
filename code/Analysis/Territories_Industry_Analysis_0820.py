import pandas as pd
import matplotlib.pyplot as plt

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

# deal
number_deal = deal.groupby(['year', 'month','Territory_fin']).size().reset_index()
number_deal.rename(columns = {0 : 'deal number'}, inplace = True)

# closed deal - Stage = 7. Deal Closed (Payment done), 5. Confirmed (Partial Payment), 6. Installation
stages = ['5','6','7']
index_list= []
for s in stages:
    index_list.extend(deal[deal['Stage'].str.contains(s)].index.tolist())

index_list = sorted(index_list)
closed_deal = deal.loc[index_list]
number_closed_deal = closed_deal.groupby(['year', 'month','Territory_fin']).size().reset_index()
number_closed_deal.rename(columns = {0 : 'closed deal'}, inplace = True)

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
territories = ['West 1','West 2','South','North','East','Overseas','Amazon']
years = [2017,2018,2019,2020,2021]

superSet_terri = {'Territory':[],'Year':[],'Month':[],'deal number':[],'closed deal number':[],'Deal Success Rate':[],'Rev/no':[]}


for territory in territories:
    deal_terri = number_deal[number_deal['Territory_fin']==territory]
    closed_deal_terri = number_closed_deal[number_closed_deal['Territory_fin']==territory]
    for year in years:
        if (year == 2021) :
            months = [1, 2, 3, 4, 5, 6, 7]
        for month in months :
            condition1 = deal_terri['year'] == year
            condition2 = deal_terri['month'] == month
             = deal_terri[condition1 & condition2]['deal number'].index
            deal_num

            condition1 = closed_deal_terri['year'] == year
            condition2 = closed_deal_terri['month'] == month
            close_deal_num = closed_deal_terri[condition1 & condition2]['closed deal']

            superSet_terri['Territory'].append(territory)
            superSet_terri['Year'].append(year)
            superSet_terri['Month'].append(month)
            superSet_terri['deal number'].append(deal_num)
            superSet_terri['closed deal number'].append(close_deal_num)

print(superSet_terri)

