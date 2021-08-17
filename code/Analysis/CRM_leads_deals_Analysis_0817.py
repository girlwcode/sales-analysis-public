import collections
import os
import pandas as pd
import matplotlib.pyplot as plt
import dataframe as df

sales_dir = '../../resource/SalesData/'

leads = pd.read_csv('../../resource/CleansedData/Zoho CRM/Leads_001_IndustryCleansed.csv')
deals = pd.read_csv('../../resource/CleansedData/Zoho CRM/Potentials_001_fillTerritories_final.csv')
installed = pd.read_csv('../../resource/SalesData/Install_full.csv')

# Lead, Deal 월별로 구분
lead = leads.loc[:, ['Lead Source', 'Lead Status', 'Created Time', 'Industry Fin']]
deal = deals.loc[:, ['Amount', 'Stage', 'Lead Source', 'Created Time', 'Territory_fin']]

# 날짜 DateTime으로 변경
lead['Created Time'] = pd.to_datetime(lead['Created Time'])
deal['Created Time'] = pd.to_datetime(deal['Created Time'])

# year, month 열 추가
lead['year'] = pd.DatetimeIndex(lead['Created Time']).year
lead['month'] = pd.DatetimeIndex(lead['Created Time']).month

deal['year'] = pd.DatetimeIndex(deal['Created Time']).year
deal['month'] = pd.DatetimeIndex(deal['Created Time']).month

deal_closed = collections.Counter(installed['Year'])
print(deal_closed)

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

