import pandas as pd
from sklearn.preprocessing import LabelEncoder

leads = pd.read_csv('../../resource/CleansedData/ZohoCRM/Leads_001_IndustryCleansed.csv')
deals = pd.read_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillIndustry.csv')

# Monthly로 deal과 lead의 territory(lead는 없음), industry concat하여 numeric
deals = deals[['Created Time', 'Territory_fin', 'Industry Fin']]
deals['Created Time'] = pd.to_datetime(deals['Created Time'])
leads = leads[['Created Time', 'Industry Fin']]
leads['Created Time'] = pd.to_datetime(leads['Created Time'])

# concat
df_list = []

years = range(2017, 2022)
months = range(1, 13)
for year in years:
    if year == 2021:
        months = range(1, 8)
    for month in months:
        deal_month = deals[(deals['Created Time'].dt.year == year) & (deals['Created Time'].dt.month == month)]
        lead_month = leads[(leads['Created Time'].dt.year == year) & (leads['Created Time'].dt.month == month)]
        full_month = pd.concat([deal_month, lead_month], ignore_index=True)

        df_list.append(full_month)

# numeric
le = LabelEncoder()
result = le.fit_transform(df_list[0]['Industry Fin'])
print(result)
print(le.inverse_transform(result))