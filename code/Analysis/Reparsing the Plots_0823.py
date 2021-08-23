"""
Sales Trend 분석 파일 (Zoho CRM)
1. Lead Creation
2. Deal Creation
3. Converted Rate
4. Sales Success Rate
"""
import collections
import os
import pandas as pd
import matplotlib.pyplot as plt

sales_dir = '../../resource/SalesData/'

leads = pd.read_csv('../../resource/CleansedData/ZohoCRM/Leads_001_IndustryCleansed.csv')
deals = pd.read_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillTerritories_final.csv')
installed = pd.read_csv('../../resource/SalesData/Install_full.csv')
revenue = pd.read_csv('../../resource/SalesData/Whole Revenue.csv')

# Lead, Deal 월별로 구분
lead = leads.loc[:, ['Lead Source', 'Lead Status', 'Created Time', 'Industry Fin']]
deal = deals.loc[:, ['Amount', 'Stage', 'Lead Source', 'Created Time', 'Territory_fin']]

# Unique key
lead_source = pd.DataFrame(lead['Lead Source'].unique(), columns=['Lead Source'])
lead_Status = pd.DataFrame(lead['Lead Status'].unique(), columns=['Lead Status'])
stage = pd.DataFrame(deal['Stage'].unique(), columns=['Deal Stage'])
deal_source = pd.DataFrame(deal['Lead Source'].unique(), columns=['Deal Lead Source'])
territory = pd.DataFrame(deal['Territory_fin'].unique(), columns=['Territory'])
industry = pd.DataFrame(lead['Industry Fin'].unique(), columns=['Industry'])
df2 = pd.concat([lead_source,lead_Status,stage,deal_source,territory,industry], axis=0, ignore_index=True)
# df2.to_csv('점수.csv',index=False)



# 날짜 DateTime으로 변경
lead['Created Time'] = pd.to_datetime(lead['Created Time'])
deal['Created Time'] = pd.to_datetime(deal['Created Time'])

# year, month 열 추가
lead['year'] = pd.DatetimeIndex(lead['Created Time']).year
lead['month'] = pd.DatetimeIndex(lead['Created Time']).month

deal['year'] = pd.DatetimeIndex(deal['Created Time']).year
deal['month'] = pd.DatetimeIndex(deal['Created Time']).month

# 한 해 Customer
# installed_company = collections.Counter(installed['Year'])
# print(installed_company)

# Rev 월 변경
months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,
          'October':10,'November':11,'December':12}
for row in revenue.index :
    for month in months.keys():
        if (revenue['Month'][row] == month):
            revenue['Month'][row] = months[month]

# 년도/월별 매출
rev_year = {2017:[],2018:[],2019:[],2020:[],2021:[]}
rev_month ={2017:[],2018:[],2019:[],2020:[],2021:[]}

x = []
for y in rev_year.keys() :
    ry = sum(revenue[revenue['Year'] == y]['Net'])
    rev_year[y] = ry
    for m in range (1,13) :
        condition1 = revenue['Year'] == y
        condition2 = revenue['Month'] == m
        x.append(str(y)+"."+str(m))
        rm = round(sum(revenue[condition1 & condition2]['Net']),2)
        rev_month[y].append(rm)
# print(rev_month.values())


# Sales Trend - 1,2. Lead Creation & Deal Creation
number_lead = lead.groupby(['year', 'month']).size().reset_index()
number_deal = deal.groupby(['year', 'month']).size().reset_index()

number_lead.rename(columns = {0 : 'lead'}, inplace = True)
number_deal.rename(columns = {0 : 'deal'}, inplace = True)

# Sales Trend - 3.Converted Rate - Monthly
monthly_num = pd.concat([number_lead,number_deal['deal']],axis=1, ignore_index=True)
monthly_num.rename(columns = {0 : 'year',1 : 'month',2 : 'lead',3 : 'deal'}, inplace = True)
monthly_num['converted Rate'] = round(monthly_num['deal'] / (monthly_num['lead'] + monthly_num['deal']),3)


# Sales Trend - 4.Sales Success Rate = conversion Rate * Deal Final Success Rate
# Stage = 7. Deal Closed (Payment done), 5. Confirmed (Partial Payment), 6. Installation
stages = ['5','6','7']
index_list= []
for s in stages:
    index_list.extend(deal[deal['Stage'].str.contains(s)].index.tolist())


index_list = sorted(index_list)
closed_deal = deal.loc[index_list]

number_closed_deal = closed_deal.groupby(['year', 'month']).size().reset_index()
number_closed_deal.rename(columns = {0 : 'closed deal'}, inplace = True)
new_data = {
    'year' : 2020,
    'month' : 4,
    'closed deal' : 0
}
idx = 47  ## 원하는 인덱스

temp1 = number_closed_deal[number_closed_deal.index < idx]
temp2 = number_closed_deal[number_closed_deal.index >= idx]
number_closed_deal = temp1.append(new_data, ignore_index=True).append(temp2, ignore_index=True)
monthly_num = pd.concat([monthly_num,number_closed_deal['closed deal']],axis=1)

monthly_num = monthly_num[monthly_num['year']!=2016]
monthly_num = monthly_num[['year','month','lead','deal','closed deal','converted Rate']]
monthly_num['sales success Rate'] = round(monthly_num['converted Rate'] * (monthly_num['closed deal']/monthly_num['deal']) * 100,3)
monthly_num.to_csv('../../resource/CleansedData/ZohoCRM/Monthly_Sales_Trend.csv',index=False)

# monthly plot's x
x = []
for row in monthly_num.index:
    date = str(monthly_num['year'][row]) + '-' + str(monthly_num['month'][row])
    x.append(date)

# lead per quarter
quarters =[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
years = [2017,2018,2019,2020,2021]
lead_dict ={}
for year in years:
    for i,quarter in enumerate(quarters):
        key = str(year) +'-' + str(i+1)
        lead_dict[key] = monthly_num[(monthly_num['year']==year) & (monthly_num['month'].isin(quarter))]['lead'].sum()
print(lead_dict)

# deal per quarter
quarters =[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
years = [2017,2018,2019,2020,2021]
deal_dict ={}
for year in years:
    for i,quarter in enumerate(quarters):
        key = str(year) +'-' + str(i+1)
        deal_dict[key] = monthly_num[(monthly_num['year']==year) & (monthly_num['month'].isin(quarter))]['deal'].sum()
print(deal_dict)

# converted rate per quarter
quarters =[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
years = [2017,2018,2019,2020,2021]
converted_dict ={}
for year in years:
    for i,quarter in enumerate(quarters):
        key = str(year) +'-' + str(i+1)
        converted_dict[key] = deal_dict[key]/(deal_dict[key]+lead_dict[key])

# sales success rate per quarter
quarters =[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
years = [2017,2018,2019,2020,2021]
sale_success_dict ={}
for year in years:
    for i,quarter in enumerate(quarters):
        key = str(year) + '-' + str(i + 1)
        deal_success = monthly_num[(monthly_num['year'] == year) & (monthly_num['month'].isin(quarter))]['closed deal'].sum()
        deal_success = deal_success / deal_dict[key]
        sale_success_dict[key] = converted_dict[key] * deal_success * 100

del converted_dict['2021-4']
del deal_dict['2021-4']
del lead_dict['2021-4']
del sale_success_dict['2021-4']
print(converted_dict)
print(sale_success_dict)



# 1. plot the lead creation
plt.figure(figsize=(15,8))
plt.title('Monthly Lead Creation (2017-2021)', fontsize=20)
plt.plot(list(lead_dict.keys()), list(lead_dict.values()))
plt.xticks(rotation=90)
plt.ylabel('Number of Leads')
plt.savefig('../../resource/Plot_Quarter/Monthly Lead Creation (2017-2021).png')

# export data to csv
df = pd.DataFrame({
    'x':list(lead_dict.keys()),
    'y':list(lead_dict.values())
})
df.to_csv('../../resource/PlotCSV_Quarter/Monthly Lead Creation (2017-2021).csv', index=False)


# 2. plot the deal creation
plt.figure(figsize=(15,8))
plt.title('Monthly Deal Creation (2017-2021)', fontsize=20)
plt.plot(list(deal_dict.keys()), list(deal_dict.values()))
plt.xticks(rotation=90)
plt.ylabel('Number of Deals')
plt.savefig('../../resource/Plot_Quarter/Monthly Deal Creation (2017-2021).png')

# export data to csv
df = pd.DataFrame({
    'x':list(deal_dict.keys()),
    'y':list(deal_dict.values())
})
df.to_csv('../../resource/PlotCSV_Quarter/Monthly Deal Creation (2017-2021).csv', index=False)



# 3. plot the converted Rate
plt.figure(figsize=(15,8))
plt.title('Monthly Converted Rate (2017-2021)', fontsize=20)
plt.plot(list(converted_dict.keys()), list(converted_dict.values()))
plt.xticks(rotation=90)
plt.ylabel('Converted Rate')
plt.savefig('../../resource/Plot_Quarter/Monthly Converted Rate (2017-2021).png')

# export data to csv
df = pd.DataFrame({
    'x':list(converted_dict.keys()),
    'y':list(converted_dict.values())
})
df.to_csv('../../resource/PlotCSV_Quarter/Monthly Converted Rate (2017-2021).csv', index=False)


# 4. plot the sales success Rate
plt.figure(figsize=(15,8))
plt.title('Monthly Sales Success Rate (2017-2021)', fontsize=20)
plt.plot(list(sale_success_dict.keys()), list(sale_success_dict.values()))
plt.xticks(rotation=90)
plt.ylabel('sales success Rate')
plt.savefig('../../resource/Plot_Quarter/Monthly Sales Success Rate (2017-2021).png')

# export data to csv
df = pd.DataFrame({
    'x':list(sale_success_dict.keys()),
    'y':list(sale_success_dict.values())
})
df.to_csv('../../resource/PlotCSV_Quarter/Monthly Sales Success Rate (2017-2021).csv', index=False)


"""
Basic Analysis 분석 파일 (Revenue)
1. Territory별 총 매출
2. Industry 별 총 매출
"""
import collections

# territory 결측치 Handling
revenue_origin = pd.read_csv('../../resource/SalesData/Whole Revenue_fillIndustry.csv')

# 6건
# print(revenue['Region'].isnull().sum())

# 직원 선물 5건 삭제 - Net:0
revenue_origin = revenue_origin.drop(revenue_origin[revenue_origin['Category']=='Employee Gift'].index, axis=0)

# Inbody 본사 이벤트 - 본사(West 1)
idx = revenue_origin[revenue_origin['Client'] == 'InBody Challenge'].index
revenue_origin.at[idx,'Region']= 'West 1'
revenue_origin.to_csv('../../resource/SalesData/Whole Revenue_fillTerritory.csv', index=False)


# Whole Sales 분석
revenue = pd.read_csv('../../resource/SalesData/Whole Revenue_fillTerritory.csv')

# Basic Analysis-2. Territory 별 총 Sales
months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,
          'October':10,'November':11,'December':12}

for row in revenue.index :
    for month in months.keys():
        if (revenue['Month'][row] == month):
            revenue['Month'][row] = months[month]


territories = ['West 1','West 2','South','North','East','Overseas','Amazon']
quarters =[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
years = [2017, 2018, 2019, 2020, 2021]

for territory in territories :
    rev_terri = revenue[revenue['Region']==territory]
    rev = {}
    for y in years:
        for i,quarter in enumerate(quarters):
            condition1 = rev_terri['Year'] == y
            condition2 = rev_terri['Month'].isin(quarter)
            r = sum(rev_terri[condition1 & condition2]['Net'])
            key = str(y) + '-' + str(i+1)
            rev[key] = r
    del rev['2021-4']
    plt.figure(figsize=(15, 8))
    plt.title('Monthly Whole Revenue By Territories:' + territory + ' (2017-2021)', fontsize=20)
    plt.plot(list(rev.keys()), list(rev.values()))
    plt.xticks(rotation=90)
    plt.ylabel('Rs', fontsize=12)
    title = 'Monthly Whole Revenue By Territories ' + str(territory) + ' (2017-2021)'
    save_dir = '../../resource/Plot_Quarter/' + title
    plt.savefig(save_dir + '.png')
    save_dir = '../../resource/PlotCSV_Quarter/' + title
    rev = pd.DataFrame(list(rev.items()),
                       columns=['x', 'y'])
    rev.to_csv(save_dir + '.csv', index=False)


# Basic Analysis-3. Industry 별 총 Sales
# [figure1] hopital, clinic, fitness
# [figure2] acdemic, private enterprise, hotel
# [figure3] others-others coporate, public association, others-aesthetic
# [figure4] millitary, others-individual, others-etc

# ['Clinic' 'Fitness' 'Hospital' 'Others_Aesthetic' 'Private Enterprise'
#  'Others_Others Corporate' 'Hotel' 'Others_etc' 'Others_Individual'
#  'Academic' 'Public Association' 'Military']
# print(revenue['Industry Fin'].unique())
import numpy as np

print(collections.Counter(revenue['Industry Fin']))
industries = [['Hospital','Clinic','Fitness'],['Academic','Private Enterprise','Hotel'],
              ['Others_Others Corporate','Public Association','Others_Aesthetic'],
              ['Military','Others_Individual','Others_etc']]


months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ears = [2017, 2018, 2019, 2020, 2021]
for industry in industries:
    rev_ids1 = revenue[revenue['Industry Fin'] == industry[0]]
    rev_ids2 = revenue[revenue['Industry Fin'] == industry[1]]
    rev_ids3 = revenue[revenue['Industry Fin'] == industry[2]]
    rev1 = {}
    rev2 = {}
    rev3 = {}

    for y in years:
        for i,quarter in enumerate(quarters):
            key = str(y) + '-' + str(i+1)
            condition1 = rev_ids1['Year'] == y
            condition2 = rev_ids1['Month'].isin(quarter)
            r = sum(rev_ids1[condition1 & condition2]['Net'])
            rev1[key] = r

            condition1 = rev_ids2['Year'] == y
            condition2 = rev_ids2['Month'].isin(quarter)
            r = sum(rev_ids2[condition1 & condition2]['Net'])
            rev2[key] = r

            condition1 = rev_ids3['Year'] == y
            condition2 = rev_ids3['Month'].isin(quarter)
            r = sum(rev_ids3[condition1 & condition2]['Net'])
            rev3[key] = r
    del rev1['2021-4']
    del rev2['2021-4']
    del rev3['2021-4']
    plt.figure(figsize=(15, 8))
    plt.bar(list(rev1.keys()), list(rev1.values()), color='green', label = industry[0])
    plt.bar(list(rev1.keys()), list(rev2.values()), color='blue',bottom=np.array(list(rev1.values())), label = industry[1])
    plt.bar(list(rev1.keys()), list(rev3.values()), color='red', bottom=np.array(list(rev1.values()))+np.array(list(rev2.values())), label = industry[2])
    plt.legend()
    name = industry[0] +', ' +industry[1] + ', ' +industry[2]
    plt.title('Monthly Whole Revenue By Industry:' + name + ' (2017-2021)', fontsize=20)
    plt.xticks(rotation=90)
    plt.ylabel('Rs', fontsize=12)
    title = 'Monthly Whole Revenue By Industry ' + str(name) + ' (2017-2021)'
    save_dir = '../../resource/Plot_Quarter/' + title
    plt.savefig(save_dir + '.png')
    save_dir = '../../resource/PlotCSV_Quarter/' + title
    data = {
        'x':list(rev1.keys()),
        industry[0]:list(rev1.values()),
        industry[1]: list(rev2.values()),
        industry[2]: list(rev3.values())
    }
    rev = pd.DataFrame(data)
    rev.to_csv(save_dir + '.csv', index=False)







