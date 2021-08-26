import pandas as pd
from sklearn.preprocessing import LabelEncoder

leads = pd.read_csv('../../resource/CleansedData/ZohoCRM/Leads_001_IndustryCleansed.csv')
deals = pd.read_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillIndustry.csv')
for_date_list = pd.read_csv('../../resource/Score/Score_Territory.csv')
score_data = pd.read_csv('../../resource/Model_Input/Monthly_zoho.csv')
google_trend = pd.read_csv('../../resource/GoogleTrends/google_trends_monthly_mean.csv')

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
count = 1
for year in years:
    if year == 2021:
        months = range(1, 8)
    for month in months:
        deal_month = deals[(deals['Created Time'].dt.year == year) & (deals['Created Time'].dt.month == month)]
        lead_month = leads[(leads['Created Time'].dt.year == year) & (leads['Created Time'].dt.month == month)]
        full_month = pd.concat([deal_month, lead_month], ignore_index=True)
        full_month['Quarter'] = count
        count += 1
        df_list.append(full_month)

# numeric
le = LabelEncoder()
full_df = pd.concat(df_list, ignore_index=True)
full_df['IndustryNumeric'] = le.fit_transform(full_df['Industry Fin'])
industry_list = list(full_df['IndustryNumeric'].groupby(full_df['Quarter']).sum())

full_df = full_df.dropna(axis=0)
full_df['TerriNumeric'] = le.fit_transform(full_df['Territory_fin'])
terri_list = list(full_df['TerriNumeric'].groupby(full_df['Quarter']).sum())

result_df = pd.DataFrame()
result_df['Date'] = date_list
result_df['IndustryNumeric'] = industry_list
result_df['TerritoryNumeric'] = terri_list

# DealNum/LeadNum/ConvertedRate 추가하여 데이터 완성
result_df_numeric = pd.concat([result_df, score_data[['ConvertedRate', 'DealNum', 'LeadNum', 'Net']]], axis=1)
result_df_full = pd.concat(
    [result_df, score_data[['DealScore', 'LeadScore', 'ConvertedRate', 'DealNum', 'LeadNum', 'Net']]], axis=1)

# GoogleTrend (2017~) +
google_list = list(google_trend['Interest Level'].iloc[8:])
score_data.insert(6, 'GoogleTrend', google_list)
# print(score_data)

# data parsing
result_df_numeric.to_csv('../../resource/Model_Input/Monthly_zoho_numeric.csv', index=False)
result_df_full.to_csv('../../resource/Model_Input/Monthly_zoho_full.csv', index=False)
score_data.to_csv('../../resource/Model_Input/Monthly_googleTrend.csv', index=False)

'''
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
'''
