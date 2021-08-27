import pandas as pd

deal = pd.read_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillIndustry.csv')
source_df = pd.read_csv('../../resource/Score/Score_Deal_leadSource.csv')
industry_df = pd.read_csv('../../resource/Score/Score_Industry.csv')
terri_df = pd.read_csv('../../resource/Score/Score_Territory.csv')

# feature, y(Stage)
deal = deal[['Created Time', 'Lead Source', 'Territory_fin', 'Industry Fin', 'Stage']]

# 2017년2월 ~ 데이터 사용
min_date = '2017-02-01'
date_filter = pd.to_datetime(deal['Created Time'], errors='coerce').ge(min_date)
deal = deal[date_filter]

deal['Created Time'] = pd.to_datetime(deal['Created Time'])
source_df['Date'] = pd.to_datetime(source_df['Date'])
industry_df['Date'] = pd.to_datetime(industry_df['Date'])
terri_df['Date'] = pd.to_datetime(terri_df['Date'])

month_df_list = []  # deal 총 54개월

years = range(2017, 2022)
months = range(1, 13)
for year in years:
    if year == 2021:
        months = range(1, 8)
    for month in months:
        if year == 2017 and month == 1:
            continue
        df = deal[(deal['Created Time'].dt.year == year) & (deal['Created Time'].dt.month == month)]
        month_df_list.append(df)

source_list = []
industry_list = []
terri_list = []

for i, df in enumerate(month_df_list):
    # month_idx i+1
    for j in df.index:
        source = df['Lead Source'][j]
        # source_list.append(source_df[source][i+1])
        if str(source) == 'nan':
            source_list.append(source_df['nan'][i+1])
        else:
            source_list.append(source_df[source][i+1])
        terri = df['Territory_fin'][j]
        terri_list.append(terri_df[terri][i + 1])
        industry = df['Industry Fin'][j]
        industry_list.append(industry_df[industry][i + 1])

stage_list = []
for i in deal.index:
    stage = deal['Stage'][i]
    if '5' in stage or '6' in stage or '7' in stage or 'Deposit' in stage:
        stage_list.append(1)
    else:
        stage_list.append(0)


result_df = pd.DataFrame()
result_df['Year'] = list(deal['Created Time'].dt.year)
result_df['Month'] = list(deal['Created Time'].dt.month)
result_df['Day'] = list(deal['Created Time'].dt.day)
result_df['LeadSource'] = source_list
result_df['Territory'] = terri_list
result_df['Industry'] = industry_list
result_df['Stage'] = stage_list

print(result_df)
result_df.to_csv('../../resource/Model_Input/deal_closed_prediction_data')