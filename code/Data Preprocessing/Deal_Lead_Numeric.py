import pandas as pd
from sklearn.preprocessing import LabelEncoder

leads = pd.read_csv('../../resource/CleansedData/ZohoCRM/Leads_001_IndustryCleansed.csv')
deals = pd.read_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillIndustry.csv')
for_date_list = pd.read_csv('../../resource/Score/Score_Territory.csv')
score_data = pd.read_csv('../../resource/Model_Input/Monthly_zoho.csv')

# Monthly로 deal과 lead의 territory(lead는 없음), industry concat하여 numeric
deals = deals[['Created Time', 'Territory_fin', 'Industry Fin']]
deals['Created Time'] = pd.to_datetime(deals['Created Time'])
leads = leads[['Created Time', 'Industry Fin']]
leads['Created Time'] = pd.to_datetime(leads['Created Time'])

date_list = list(for_date_list['Date'])

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
industry_list =[]
terri_list = []
le = LabelEncoder()
for df in df_list:
    industry_month = le.fit_transform(df['Industry Fin'])
    industry_list.append(industry_month.sum())
    terri_month = le.fit_transform(df['Territory_fin'])
    terri_list.append(terri_month.sum())
    # print(result)
    # print(le.inverse_transform(result))

full_df = pd.DataFrame()
full_df['Date'] = date_list
full_df['Territory'] = terri_list
full_df['Industry'] = industry_list

# DealNum/LeadNum/ConvertedRate 추가하여 데이터 완성
score_data = score_data[['ConvertedRate','DealNum','LeadNum','Net']]
result_df = pd.concat([full_df, score_data], axis=1)


result_df.to_csv('../../resource/Model_Input/Monthly_zoho_numeric.csv', index=False)

