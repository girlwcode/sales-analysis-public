import collections
import os
import pandas as pd
import matplotlib.pyplot as plt
import dataframe as df

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

print(stage)
# 7. Deal Closed (Payment done), 5. Confirmed (Partial Payment)

# 날짜 DateTime으로 변경
lead['Created Time'] = pd.to_datetime(lead['Created Time'])
deal['Created Time'] = pd.to_datetime(deal['Created Time'])

# year, month 열 추가
lead['year'] = pd.DatetimeIndex(lead['Created Time']).year
lead['month'] = pd.DatetimeIndex(lead['Created Time']).month

deal['year'] = pd.DatetimeIndex(deal['Created Time']).year
deal['month'] = pd.DatetimeIndex(deal['Created Time']).month

# 한 해 Customer
installed_company = collections.Counter(installed['Year'])
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

print(rev_month.values())

# Converted Rate - Monthly
number_lead = lead.groupby(['year', 'month']).size().reset_index()
number_deal = deal.groupby(['year', 'month']).size().reset_index()

number_lead.rename(columns = {0 : 'lead'}, inplace = True)
number_deal.rename(columns = {0 : 'deal'}, inplace = True)

monthly_num = pd.concat([number_lead,number_deal['deal']],axis=1, ignore_index=True)
monthly_num.rename(columns = {0 : 'year',1 : 'month',2 : 'lead',3 : 'deal'}, inplace = True)
monthly_num['converted Rate'] = monthly_num['deal'] / (monthly_num['lead'] + monthly_num['deal']) * 100


monthly_num = monthly_num[monthly_num['year']!=2016]

# monthly plot's x
x = []
for row in monthly_num.index:
    date = str(monthly_num['year'][row]) + '.' + str(monthly_num['month'][row])
    x.append(date)

# plot the lead creation
plt.figure(figsize=(15,8))
plt.title('Monthly Lead Creation (2017-2021)', fontsize=20)
plt.plot(x, monthly_num['lead'])
plt.xticks(rotation=90)
plt.ylabel('Number of Leads')
plt.savefig('../../resource/Plot/Monthly Lead Creation (2017-2021).png')

# plot the deal creation
plt.figure(figsize=(15,8))
plt.title('Monthly Deal Creation (2017-2021)', fontsize=20)
plt.plot(x, monthly_num['deal'])
plt.xticks(rotation=90)
plt.ylabel('Number of Deals')
plt.savefig('../../resource/Plot/Monthly Deal Creation (2017-2021).png')


# plot the conversion Rate
plt.figure(figsize=(15,8))
plt.title('Monthly Converted Rate Creation (2017-2021)', fontsize=20)
plt.plot(x, monthly_num['converted Rate'])
plt.xticks(rotation=90)
plt.ylabel('Converted Rate (%)')
plt.savefig('../../resource/Plot/Monthly Converted Rate Creation (2017-2021).png')



# revenue per month and converted rate
# y1 = list(rev_year.values())
# y2 = list(installed_company.values())
#
# fig, ax1 = plt.subplots()
# ax1.plot(x, y1, color='deeppink', label='Revenue')
# fig.autofmt_xdate(rotation=90)
# ax1.legend(loc='upper right')
#
# ax2 = ax1.twinx()
# ax2.plot(x, y2, color='green', label='Customer')
# ax1.legend(loc='lower right')
#
# plt.title('Whole Revenue and Customer of Inbody, India', fontsize=18)
# plt.legend()
# plt.show()



# revenue and Installed Company
# x = list(rev_year.keys())
# y1 = list(rev_year.values())
# y2 = list(installed_company.values())
#
# fig, ax1 = plt.subplots()
# ax1.plot(x, y1, color='deeppink', label='Revenue')
# fig.autofmt_xdate(rotation=90)
# ax1.legend(loc='upper right')
#
# ax2 = ax1.twinx()
# ax2.plot(x, y2, color='green', label='Customer')
# ax1.legend(loc='lower right')
#
# plt.title('Whole Revenue and Customer of Inbody, India', fontsize=18)
# plt.legend()
# plt.show()


# Deal stage unique
# '10.Archive': 951, '7. Deal Closed (Payment done)': 532, '6. Installation': 431, '9. Rejected': 141, '3. B- Negotiation': 116,
# '1.  D- Qualified Deal': 68, '8. Closed Lost to Competition': 28, '2. C- Consideration': 21, '5. Confirmed (Partial Payment)': 12,
# '4. A- Verbal Approval': 11, 'Rejected': 1, 'DepositReceipt': 1
deal_stage = collections.Counter(deal['Stage'])

# # installed concat
# df_list = []
# for csv_data in os.listdir(sales_dir):
#     if csv_data.startswith('Installation') and csv_data.endswith('.csv'):
#         data = pd.read_csv(sales_dir + csv_data)
#         new_data = data[['Month', 'Client', 'City', 'State']]
#         df_list.append(new_data)
# installed = pd.concat(df_list, ignore_index=True)
# installed = installed.drop_duplicates(['Client', 'City'])
#
# installed['Year'] = 0
# months = ['January','February','March','April','May','June','July','August','September','October','November','December']
#
# year = 2017
# for row in installed.index:
#     if (row == 104) :
#         year = 2018
#     elif (row == 540) :
#         year = 2019
#     elif (row == 1425) :
#         year = 2020
#     elif (row == 2001) :
#         year = 2021
#     installed['Year'][row] = year
#
# installed.to_csv(sales_dir + 'Install_full.csv', index=False)

