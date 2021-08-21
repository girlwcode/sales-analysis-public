"""
Basic Analysis 분석 파일 (Revenue, deal, lead)
1-1. Territory별  Deal Success Rate

2-1. Industry 별 Deal Success Rate
2-3. Industry 별 Converted Rate
2-4. Industry 별 Sales Success Rate
"""
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
        else:
            months = range(1, 13)
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
industries = [['Hospital','Clinic','Fitness'],['Academic','Private Enterprise','Hotel'],
              ['Others_Others Corporate','Public Association','Others_Aesthetic'],
              ['Military','Others_Individual','Others_etc']]

for industry in industries:
    deal_ids1 = deal[deal['Industry Fin'] == industry[0]]
    deal_ids2 = deal[deal['Industry Fin'] == industry[1]]
    deal_ids3 = deal[deal['Industry Fin'] == industry[2]]
    ids1 = {}
    ids2 = {}
    ids3 = {}
    for year in years:
        if (year == 2021) :
            months = [1, 2, 3, 4, 5, 6, 7]
        else:
            months = range(1, 13)
        for month in months:
            key = str(year) +'-'+ str(month)

            df_industry1 = deal_ids1[(deal_ids1['year'] == year) & (deal_ids1['month'] == month)]
            if not df_industry1.empty :
                rate = len(df_industry1[df_industry1['Stage'].str.contains('5|6|7')]) / len(df_industry1)
                ids1[key] = rate
            else: # 해당 month 데이터 존재하지않음
                ids1[key] = 0

            df_industry2 = deal_ids2[(deal_ids2['year'] == year) & (deal_ids2['month'] == month)]
            if not df_industry2.empty:
                rate = len(df_industry2[df_industry2['Stage'].str.contains('5|6|7')]) / len(df_industry2)
                ids2[key] = rate
            else:  # 해당 month 데이터 존재하지않음
                ids2[key] = 0

            df_industry3 = deal_ids3[(deal_ids3['year'] == year) & (deal_ids3['month'] == month)]
            if not df_industry3.empty:
                rate = len(df_industry3[df_industry3['Stage'].str.contains('5|6|7')]) / len(df_industry3)
                ids3[key] = rate
            else:  # 해당 month 데이터 존재하지않음
                ids3[key] = 0

    fig = plt.figure(figsize=(15, 8))  ## 캔버스 생성
    fig.set_facecolor('white')  ## 캔버스 색상 설정
    ax = fig.add_subplot()  ## 그림 뼈대(프레임) 생성

    ax.plot(list(ids1.keys()), list(ids1.values()), label=industry[0])  ## 선그래프 생성
    ax.plot(list(ids1.keys()), list(ids2.values()), label=industry[1])
    ax.plot(list(ids1.keys()), list(ids3.values()), label=industry[2])

    ax.legend()  ## 범례
    name = industry[0] + ', ' + industry[1] + ', ' + industry[2]
    plt.title('Monthly Deal Success Rate By Industry:' + name + ' (2017-2021)', fontsize=20)
    plt.xticks(rotation=90)
    plt.ylabel('Rs', fontsize=12)
    title = 'Monthly Deal Success Rate By Industry ' + str(name) + ' (2017-2021)'
    save_dir = '../../resource/Plot/' + title
    plt.savefig(save_dir + '.png')
    save_dir = '../../resource/PlotCSV/' + title
    data = {
        'x': list(ids1.keys()),
        industry[0]: list(ids1.values()),
        industry[1]: list(ids2.values()),
        industry[2]: list(ids3.values())
    }
    rev = pd.DataFrame(data)
    rev.to_csv(save_dir + '.csv', index=False)


# 2-3,4. Industry별 Convert Rate, Sales Success Rate
for industry in industries:
    deal_ids1 = deal[deal['Industry Fin'] == industry[0]]
    deal_ids2 = deal[deal['Industry Fin'] == industry[1]]
    deal_ids3 = deal[deal['Industry Fin'] == industry[2]]

    lead_ids1 = lead[lead['Industry Fin'] == industry[0]]
    lead_ids2 = lead[lead['Industry Fin'] == industry[1]]
    lead_ids3 = lead[lead['Industry Fin'] == industry[2]]

    # CR : Converted Rate
    CR1 = {}
    CR2 = {}
    CR3 = {}

    # SS : Sales Success Rate
    SS1 = {}
    SS2 = {}
    SS3 = {}

    for year in years:
        if (year == 2021) :
            months = [1, 2, 3, 4, 5, 6, 7]
        else:
            months = range(1, 13)
        for month in months:
            key = str(year) +'-'+ str(month)

            df_lead1 = lead_ids1[(lead_ids1['year'] == year) & (lead_ids1['month'] == month)]
            df_deal1 = deal_ids1[(deal_ids1['year'] == year) & (deal_ids1['month'] == month)]
            if not df_lead1.empty and not df_deal1.empty :
                rate1 = len(df_deal1) / (len(df_lead1) + len(df_deal1))
                rate2 = rate1 * (len(df_deal1[df_deal1['Stage'].str.contains('5|6|7')]) / len(df_deal1)) * 100
                CR1[key] = rate1
                SS1[key] = rate2
            else: # 해당 month 데이터 존재하지않음
                CR1[key] = 0
                SS1[key] = 0

            df_lead2 = lead_ids2[(lead_ids2['year'] == year) & (lead_ids2['month'] == month)]
            df_deal2 = deal_ids2[(deal_ids2['year'] == year) & (deal_ids2['month'] == month)]
            if not df_lead2.empty and not df_deal2.empty:
                rate1 = len(df_deal2) / (len(df_lead2) + len(df_deal2))
                rate2 = rate1 * (len(df_deal2[df_deal2['Stage'].str.contains('5|6|7')]) / len(df_deal2)) * 100
                CR2[key] = rate1
                SS2[key] = rate2
            else:  # 해당 month 데이터 존재하지않음
                CR2[key] = 0
                SS2[key] = 0

            df_lead3 = lead_ids3[(lead_ids3['year'] == year) & (lead_ids3['month'] == month)]
            df_deal3 = deal_ids3[(deal_ids3['year'] == year) & (deal_ids3['month'] == month)]
            if not df_lead3.empty and not df_deal3.empty:
                rate1 = len(df_deal3) / (len(df_lead3) + len(df_deal3))
                rate2 = rate1 * (len(df_deal3[df_deal3['Stage'].str.contains('5|6|7')]) / len(df_deal3)) * 100
                CR3[key] = rate1
                SS3[key] = rate2
            else:  # 해당 month 데이터 존재하지않음
                CR3[key] = 0
                SS3[key] = 0

    # plot and parsing the converted Rate
    fig = plt.figure(figsize=(15, 8))  ## 캔버스 생성
    fig.set_facecolor('white')  ## 캔버스 색상 설정
    ax = fig.add_subplot()  ## 그림 뼈대(프레임) 생성

    ax.plot(list(CR1.keys()), list(CR1.values()), label=industry[0])  ## 선그래프 생성
    ax.plot(list(CR1.keys()), list(CR2.values()), label=industry[1])
    ax.plot(list(CR1.keys()), list(CR3.values()), label=industry[2])

    ax.legend()  ## 범례
    name = industry[0] + ', ' + industry[1] + ', ' + industry[2]
    plt.title('Monthly Converted Rate By Industry:' + name + ' (2017-2021)', fontsize=20)
    plt.xticks(rotation=90)
    plt.ylabel('Rs', fontsize=12)
    title = 'Monthly Converted Rate By Industry ' + str(name) + ' (2017-2021)'
    save_dir = '../../resource/Plot/' + title
    plt.savefig(save_dir + '.png')
    save_dir = '../../resource/PlotCSV/' + title
    data = {
        'x': list(CR1.keys()),
        industry[0]: list(CR1.values()),
        industry[1]: list(CR2.values()),
        industry[2]: list(CR3.values())
    }
    rev = pd.DataFrame(data)
    rev.to_csv(save_dir + '.csv', index=False)

    # plot and parsing the Sales Success Rate
    fig = plt.figure(figsize=(15, 8))  ## 캔버스 생성
    fig.set_facecolor('white')  ## 캔버스 색상 설정
    ax = fig.add_subplot()  ## 그림 뼈대(프레임) 생성

    ax.plot(list(SS1.keys()), list(SS1.values()), label=industry[0])  ## 선그래프 생성
    ax.plot(list(SS1.keys()), list(SS2.values()), label=industry[1])
    ax.plot(list(SS1.keys()), list(SS3.values()), label=industry[2])

    ax.legend()  ## 범례
    name = industry[0] + ', ' + industry[1] + ', ' + industry[2]
    plt.title('Monthly Sales Success Rate By Industry:' + name + ' (2017-2021)', fontsize=20)
    plt.xticks(rotation=90)
    plt.ylabel('Rs', fontsize=12)
    title = 'Monthly Sales Success Rate By Industry ' + str(name) + ' (2017-2021)'
    save_dir = '../../resource/Plot/' + title
    plt.savefig(save_dir + '.png')
    save_dir = '../../resource/PlotCSV/' + title
    data = {
        'x': list(SS1.keys()),
        industry[0]: list(SS1.values()),
        industry[1]: list(SS2.values()),
        industry[2]: list(SS3.values())
    }
    rev = pd.DataFrame(data)
    rev.to_csv(save_dir + '.csv', index=False)




