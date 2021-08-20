import pandas as pd
import numpy as np

# Potentials, Sales에 Industry 추가
accounts = pd.read_csv('../../resource/CleansedData/ZohoCRM/Accounts_001_IndustryCleansed.csv')
deals = pd.read_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillTerritories_final.csv')
sales = pd.read_csv('../../resource/SalesData/Whole Revenue.csv')

# 1. Potential (Company ID) - Accounts (Record Id) 연결
# print(len(deals['Company ID'].unique()))
# 2121

# dictionary 채우기
company_id_dict = dict.fromkeys(list(deals['Company ID'].unique()))  # key: companyID, value: Industry
for i in accounts.index:
    company_id = accounts['Record Id'][i]
    if company_id in company_id_dict:
        if company_id_dict[company_id] is None:
            industry = accounts['Industry Fin'][i]
            company_id_dict[company_id] = industry

# Potential 채우기 - 115개 연결 안됨
deals['Industry Fin'] = None
for i in deals.index:
    company_id = deals['Company ID'][i]
    deals['Industry Fin'][i] = company_id_dict[company_id]
print(pd.isna(deals['Industry Fin']).sum())

# 2-1. Sales (Client) - Accounts (Company Name) 연결
company_name_dict = dict.fromkeys(list(sales['Client'].unique()))  # key: companyName, value: Industry
for i in accounts.index:
    company_name = accounts['Company Name'][i]
    if company_name in company_name_dict:
        if company_name_dict[company_name] is None:
            industry = accounts['Industry Fin'][i]
            company_name_dict[company_name] = industry

# Sales 채우기
sales['Industry Fin'] = None
for i in sales.index:
    company_name = sales['Client'][i]
    sales['Industry Fin'][i] = company_name_dict[company_name]

# 2-2. Sales 기존 Category로 채우기
# ['Private Enterprise' 'Fitness' 'Hospital' 'Clinic'
#  'Public Association' 'Others_Individual' 'Others_Aesthetic'
#  'Others_Others Corporate' 'Hotel' 'Others_etc' 'Academic' 'Military']

cate_industry_dict = {}
cate_industry_dict['Hospital'] = ['Hospital', 'Hospitals', 'Medical', 'HealthCare Centre', 'Healthcare Centre']
cate_industry_dict['Private Enterprise'] =['Pharmacy', 'Pharma', 'Hospitality', 'Supplement Store']
cate_industry_dict['Fitness'] = ['Fitness/Sports', 'Fitness Club', 'Fitness/Sports(Special)', 'Fitness ', 'Fitness  ', 'Fitness']
cate_industry_dict['Clinic'] = ['Diagnostic Centre', 'Nutrition', 'Wellness Clinic', 'Diet']
cate_industry_dict['Public Association'] = ['Governement', 'Government', 'Research', 'Military/Police']
cate_industry_dict['Hotel'] = ['Hotel', 'Spa', 'Golf club']
cate_industry_dict['Academic'] = ['Police Academy', 'Academy', 'Education', 'University', 'Academia']
cate_industry_dict['Others_Aesthetic'] = ['Health Center', 'Skin&SPA']
cate_industry_dict['Others_Individual'] = ['Personal ', 'Home Health', 'diet']
cate_industry_dict['Others_Others Corporate'] = ['Enterprise', 'Service']
cate_industry_dict['Others_etc'] = ['Employee Gift', 'Amazon']

for industry in cate_industry_dict:
    idx_list = sales[sales['Category'].isin(cate_industry_dict[industry])].index.tolist()
    sales.at[idx_list, 'Industry Fin'] = industry

# category == wellness
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Wellness')
                 & (sales['Client'].str.lower().str.contains('diag|nutri'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Clinic'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Wellness')
                 & (sales['Client'].str.lower().str.contains('multifit'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Fitness'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Wellness')].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Others_Aesthetic'
# category == wellnessCentre
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Wellness Centre')
                 & (sales['Client'].str.lower().str.contains('hospital'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Hospital'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Wellness Centre')].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Others_Aesthetic'
# category == careCenter
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Care Center')
                 & (sales['Client'].str.lower().str.contains('clinic'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Clinic'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Care Center')
                 & (sales['Client'].str.lower().str.contains('remedi'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Others_Others Corporate'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Care Center')
                 & (sales['Client'].str.lower().str.contains('hope'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Private Enterprise'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Care Center')].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Others_Aesthetic'
# category == corporate
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Corporate')
                 & (sales['Client'].str.lower().str.contains('wellness'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Others_Aesthetic'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Corporate')
                 & (sales['Client'].str.lower().str.contains('apollo|medanta'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Hospital'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Corporate')
                 & (sales['Client'].str.lower().str.contains('charita'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Public Association'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Corporate')].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Others_Others Corporate'
# category == Scientific Research Institute
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Scientific Research Institute')
                 & (sales['Client'].str.lower().str.contains('alcon'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Private Enterprise'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Scientific Research Institute')].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Hospital'
# category == dietClinic
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Diet Clinic')
                 & (sales['Client'].str.lower().str.contains('burger'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Hospital'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Diet Clinic')].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Clinic'
# category == other
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Other')
                 & (sales['Client'].str.lower().str.contains('asmita|nakul|portal'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Others_Individual'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Other')
                 & (sales['Client'].str.lower().str.contains('care india'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Public Association'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Other')
                 & (sales['Client'].str.lower().str.contains('homeo'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Clinic'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Other')].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Others_Others Corporate'
# category == convention
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Convention')
                 & (sales['Client'].str.lower().str.contains('sagar|vaishali'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Public Association'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Convention')].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Others_Individual'
# category == others
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Others')
                 & (sales['Client'].str.lower().str.contains('ltd|limited'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Others_Others Corporate'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Others')].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Others_Individual'
# inbody 들어가면 others_etc로
idx_list = sales[sales['Client'].str.lower().str.contains('inbody')].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Others_etc'
# category == nan(마지막 1개)
idx_list = sales[sales['Industry Fin'].isna()].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Fitness'


# 3. Potential 남은 115개 DealName으로 채우기
idx_list = deals[(deals['Industry Fin'].isna()) & (deals['Deal Name'].str.lower().str.contains('amazon|inbody|cs '))].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Others_etc'
idx_list = deals[(deals['Industry Fin'].isna()) &
                 (deals['Deal Name'].str.lower().str.contains('fit|fint|gym|health club|bodyzone|finest|smeeta'))].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Fitness'
idx_list = deals[(deals['Industry Fin'].isna()) & (deals['Deal Name'].str.lower().str.contains('hospital|hoapital|nursing'))].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Hospital'
idx_list = deals[(deals['Industry Fin'].isna()) & (deals['Deal Name'].str.lower().str.contains('dr |dr.|dieti|nutri|food|eatwell'))].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Clinic'
idx_list = deals[(deals['Industry Fin'].isna()) & (deals['Deal Name'].str.lower().str.contains('acade|weill cornel'))].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Academic'
idx_list = deals[(deals['Industry Fin'].isna()) & (deals['Deal Name'].str.lower().str.contains('home use'))].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Others_Individual'
idx_list = deals[(deals['Industry Fin'].isna()) & (deals['Deal Name'].str.lower().str.contains('navy'))].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Military'
idx_list = deals[(deals['Industry Fin'].isna()) & (deals['Deal Name'].str.lower().str.contains('vibes|vlcc|skin|welona'))].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Others_Aesthetic'
idx_list = deals[(deals['Industry Fin'].isna()) & (deals['Deal Name'].str.contains('CIAT'))].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Public Association'
idx_list = deals[(deals['Industry Fin'].isna()) &
                 (deals['Deal Name'].str.lower().str.contains('lifestyle studio|clinic|healtonation|bumb|rajeev|medic centre'))].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Clinic'
idx_list = deals[(deals['Industry Fin'].isna()) & (deals['Deal Name'].str.lower().str.contains('club|the lodhi'))].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Hotel'
idx_list = deals[(deals['Industry Fin'].isna()) & (deals['Deal Name'].str.lower().str.contains('ltd'))].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Others_Others Corporate'
idx_list = deals[(deals['Industry Fin'].isna()) & (deals['Deal Name'].str.lower().str.contains('dummy|kamesh'))].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Others_etc'
idx_list = deals[(deals['Industry Fin'].isna()) &
                 (deals['Deal Name'].str.lower().str.contains('health|instrument|gsk|workout|ankush|mega'))].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Private Enterprise'
# 나머지 individual
idx_list = deals[deals['Industry Fin'].isna()].index.tolist()
deals.at[idx_list, 'Industry Fin'] = 'Others_Individual'

print(pd.isna(deals['Industry Fin']).sum())

# data parsing
sales.to_csv('../../resource/SalesData/Whole Revenue_fillIndustry.csv', index=False)
deals.to_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillIndustry.csv', index=False)

