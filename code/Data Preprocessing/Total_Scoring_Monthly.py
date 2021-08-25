import pandas as pd

industry_score = pd.read_csv('../../resource/Score/Score_Industry.csv')
territory_score = pd.read_csv('../../resource/Score/Score_Territory.csv')
convert_score = pd.read_csv('../../resource/PlotCSV/Monthly Converted Rate (2017-2021).csv')
leadSource_lead = pd.read_csv('../../resource/Score/Score_Lead_leadSource.csv')
leadSource_deal = pd.read_csv('../../resource/Score/Score_Deal_leadSource.csv')
gdp = pd.read_csv('../../resource/Score/Score_gdp.csv')
hdi = pd.read_csv('../../resource/Score/Score_hdi.csv')
net = pd.read_csv('../../resource/Model_Input/Monthly_net.csv')
deal = pd.read_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillIndustry.csv')
lead = pd.read_csv('../../resource/CleansedData/ZohoCRM/Leads_001_IndustryCleansed.csv')
deal_num = pd.read_csv('../../resource/PlotCSV/Monthly Deal Creation (2017-2021).csv')
lead_num = pd.read_csv('../../resource/PlotCSV/Monthly Lead Creation (2017-2021).csv')


# DealScore = leadSource * stage * territory * industry * gdp * hdi
def oneDealScoring(df, i, date_idx, year_idx):
    oneDeal_score = 1
    stage_dict = {'1':4, '2':5, '3':7, '4':6, '5':8, '6':9, '7':10, '8':3, 'Reject':1, '10':2, 'Deposit':10}
    # leadSource
    source = df['Lead Source'][i]
    oneDeal_score *= leadSource_deal[source][date_idx]
    # stage
    stage = df['Stage'][i]
    for x in stage_dict:
        if x in stage:
            oneDeal_score *= stage_dict[x]
            break
    # territory
    terri = df['Territory_fin'][i]
    oneDeal_score *= territory_score[terri][date_idx]
    # industry
    industry = df['Industry Fin'][i]
    oneDeal_score *= industry_score[industry][date_idx]
    # gdp
    oneDeal_score *= gdp[terri][year_idx]
    # hdi
    oneDeal_score *= hdi[terri][year_idx]

    return oneDeal_score

# LeadScore = leadSource * leadState * industry
def oneLeadScoring(df, i, date_idx):
    oneLead_score = 1
    state_dict = {'1':2, '2':10, '3':4, '4':7, '5':5, '6':1, '7':3, '8':6, '9':8, '10':9}
    # leadSource
    source = df['Lead Source'][i]
    oneLead_score *= leadSource_lead[source][date_idx]
    # leadState
    state = df['Lead Status'][i]
    for x in state_dict:
        if x in state:
            oneLead_score *= state_dict[x]
            break
    # industry
    industry = df['Industry Fin'][i]
    oneLead_score *= industry_score[industry][date_idx]

    return oneLead_score


# Main
result_df = pd.DataFrame()
date_list = list(industry_score['Date'])
result_df['Date'] = date_list

# score 표에서 컬럼이 nan인거 있어서 lead,deal에서 None -> 'nan'으로 수정
lead['Lead Source'] = lead['Lead Source'].fillna('nan')
deal['Lead Source'] = deal['Lead Source'].fillna('nan')

years = range(2017, 2022)
months = range(1, 13)

# DealScore
deal['Created Time'] = pd.to_datetime(deal['Created Time'])
deal_list = []
date_idx = 0
for year_idx, year in enumerate(years):
    if year == 2021:
        months = range(1,8)
    for month in months:
        month_score = 0
        df = deal[(deal['Created Time'].dt.year == year) & (deal['Created Time'].dt.month == month)]
        for i in df.index:
            month_score += (oneDealScoring(df, i, date_idx, year_idx))
        date_idx += 1
        deal_list.append(month_score)
result_df['DealScore'] = deal_list

# LeadScore
months = range(1,13)
lead['Created Time'] = pd.to_datetime(lead['Created Time'])
lead_list = []
date_idx = 0
for year in years:
    if year == 2021:
        months = range(1,8)
    for month in months:
        month_score = 0
        df = lead[(lead['Created Time'].dt.year == year) & (lead['Created Time'].dt.month == month)]
        for i in df.index:
            month_score += (oneLeadScoring(df, i, date_idx))
        date_idx += 1
        lead_list.append(month_score)
result_df['LeadScore'] = lead_list

# Converted Rate (DealNum / Deal+LeadNum)
del deal_num['x']
del lead_num['x']
deal_num['DealAndLead'] = deal_num + lead_num
deal_num['Convert'] = deal_num['y'].div(deal_num['DealAndLead'])
result_df['ConvertedRate'] = list(deal_num['Convert'])

# DealNum/LeadNum
result_df['DealNum'] = list(deal_num['y'])
result_df['LeadNum'] = list(lead_num['y'])

# Net
result_df['Net'] = list(net['Net'])

print(result_df)

result_df.to_csv('../../resource/Model_Input/Monthly_zoho.csv', index=False)
