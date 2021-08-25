import pandas as pd

for_date_q_list = pd.read_csv('../../resource/PlotCSV_Quarter/Monthly Deal Creation (2017-2021).csv')
for_date_list = pd.read_csv('../../resource/Score/Total_Score_monthly.csv')
deals_plus = pd.read_csv('../../resource/Score/Deal_leadSource_Plus_Count.csv')
deals_minus = pd.read_csv('../../resource/Score/Deal_leadSource_Minus_Count.csv')
leads_plus = pd.read_csv('../../resource/Score/Lead_leadSource_Plus_Count.csv')
leads_minus = pd.read_csv('../../resource/Score/Lead_leadSource_Minus_Count.csv')

date_list_q = list(for_date_q_list['x'])
date_list = list(for_date_list['Date'])

years = range(2017, 2022)
months = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

df_list = [deals_plus, deals_minus, leads_plus, leads_minus]
title_list = ['Deal_leadSource_Plus_Count_Q','Deal_leadSource_Minus_Count_Q','Lead_leadSource_Plus_Count_Q','Lead_leadSource_Minus_Count_Q']

# deal 가중치+
df = deals_plus
df['x'] = date_list
df['x'] = pd.to_datetime(df['x'])
del df['Date']

result_df = pd.DataFrame()
for year in years:
    for i, quarter in enumerate(months):
        df_new = df[(df['x'].dt.year == year) & df['x'].dt.month.isin(quarter)]
        if not df_new.empty:
            del df_new['x']
            q_dict = {}
            for col in df_new.columns:
                q_dict[col] = df_new[col].sum()
            result_df = result_df.append(q_dict, ignore_index=True)
result_df.insert(0, 'Date', date_list_q)
result_df.to_csv('../../resource/Score/'+title_list[0]+'.csv', index=False)

# deal 가중치-
df = deals_minus
df['x'] = date_list
df['x'] = pd.to_datetime(df['x'])
del df['Date']

result_df = pd.DataFrame()
for year in years:
    for i, quarter in enumerate(months):
        df_new = df[(df['x'].dt.year == year) & df['x'].dt.month.isin(quarter)]
        if not df_new.empty:
            del df_new['x']
            q_dict = {}
            for col in df_new.columns:
                q_dict[col] = df_new[col].sum()
            result_df = result_df.append(q_dict, ignore_index=True)
result_df.insert(0, 'Date', date_list_q)
result_df.to_csv('../../resource/Score/'+title_list[1]+'.csv', index=False)

# lead 가중치+
df = leads_plus
df['x'] = date_list
df['x'] = pd.to_datetime(df['x'])
del df['Date']

result_df = pd.DataFrame()
for year in years:
    for i, quarter in enumerate(months):
        df_new = df[(df['x'].dt.year == year) & df['x'].dt.month.isin(quarter)]
        if not df_new.empty:
            del df_new['x']
            q_dict = {}
            for col in df_new.columns:
                q_dict[col] = df_new[col].sum()
            result_df = result_df.append(q_dict, ignore_index=True)
result_df.insert(0, 'Date', date_list_q)
result_df.to_csv('../../resource/Score/'+title_list[2]+'.csv', index=False)

# lead 가중치-
df = leads_minus
df['x'] = date_list
df['x'] = pd.to_datetime(df['x'])
del df['Date']

result_df = pd.DataFrame()
for year in years:
    for i, quarter in enumerate(months):
        df_new = df[(df['x'].dt.year == year) & df['x'].dt.month.isin(quarter)]
        if not df_new.empty:
            del df_new['x']
            q_dict = {}
            for col in df_new.columns:
                q_dict[col] = df_new[col].sum()
            result_df = result_df.append(q_dict, ignore_index=True)
result_df.insert(0, 'Date', date_list_q)
result_df.to_csv('../../resource/Score/'+title_list[3]+'.csv', index=False)
