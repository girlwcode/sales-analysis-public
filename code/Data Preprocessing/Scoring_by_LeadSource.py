import pandas as pd

for_date_list = pd.read_csv('../../resource/PlotCSV/Monthly Deal Success Rate By Territories Amazon (2017-2021).csv')
deals_plus = pd.read_csv('../../resource/Score/Deal_leadSource_Plus_Count.csv')
deals_minus = pd.read_csv('../../resource/Score/Deal_leadSource_Minus_Count.csv')
leads_plus = pd.read_csv('../../resource/Score/Lead_leadSource_Plus_Count.csv')
leads_minus = pd.read_csv('../../resource/Score/Lead_leadSource_Minus_Count.csv')

date_list = list(for_date_list['x'])

## Deals
# 가중치+ (비율*100)
del deals_plus['Date']
deals_plus['Sum'] = deals_plus.sum(axis=1)

for col in deals_plus.columns:
    deals_plus[col] = deals_plus[col].div(deals_plus['Sum'])
del deals_plus['Sum']
deals_plus = deals_plus.fillna(0)
deals_plus = (deals_plus + 1) * 5
# deals_plus = deals_plus.fillna(5)
# deals_plus.to_csv('1.csv', index=False)

# 가중치-
del deals_minus['Date']
deals_minus['Sum'] = deals_minus.sum(axis=1)

for col in deals_minus.columns:
    deals_minus[col] = deals_minus[col].div(deals_minus['Sum'])
del deals_minus['Sum']
deals_minus = deals_minus.fillna(0)
deals_minus = deals_minus.replace(1,0.99999)
deals_minus = (1 - deals_minus) * 5
# deals_minus = deals_minus.fillna(5)
# deals_minus.to_csv('2.csv', index=False)

deals_full = deals_plus * deals_minus
deals_full.insert(0, 'Date', date_list)
deals_full.to_csv('../../resource/Score/Score_Deal_leadSource.csv', index=False)

## Leads
# 가중치+
del leads_plus['Date']
leads_plus['Sum'] = leads_plus.sum(axis=1)

for col in leads_plus.columns:
    leads_plus[col] = leads_plus[col].div(leads_plus['Sum'])
del leads_plus['Sum']
leads_plus = leads_plus.fillna(0)
leads_plus = (leads_plus + 1) * 5
# leads_plus = leads_plus.fillna(5)

# 가중치-
del leads_minus['Date']
leads_minus['Sum'] = leads_minus.sum(axis=1)

for col in leads_minus.columns:
    leads_minus[col] = leads_minus[col].div(leads_minus['Sum'])
del leads_minus['Sum']
leads_minus = leads_minus.fillna(0)
leads_minus = leads_minus.replace(1,0.99999)
leads_minus = (1 - leads_minus) * 5
# leads_minus = leads_minus.fillna(5)

leads_full = leads_plus * leads_minus
leads_full.insert(0, 'Date', date_list)
leads_full.to_csv('../../resource/Score/Score_Lead_leadSource.csv', index=False)