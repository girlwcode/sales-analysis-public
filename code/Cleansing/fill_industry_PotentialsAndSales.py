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

# 115개 Accounts랑 연결 안됨
'''
none_list = []
for company_id in company_id_dict:
    if company_id_dict[company_id] is None:
        none_list.append(company_id)
industry_none = dict.fromkeys(none_list)
print(len(none_list))
'''

# Potential 채우기
deals['Industry Fin'] = None
for i in deals.index:
    company_id = deals['Company ID'][i]
    deals['Industry Fin'][i] = company_id_dict[company_id]

deals.to_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillIndustry.csv', index=False)

'''
# 2. Sales (Clinet) - Potential_fillIndustry (Deal Name) 연결
deals_industry = pd.read_csv('../../resource/CleansedData/ZohoCRM/Potentials_001_fillIndustry.csv')
# print(len(sales['Client'].unique()))
# 1560

# dictionary 채우기
company_name_dict = dict.fromkeys(list(sales['Client'].unique()))       # key: companyName, value: Industry
for company_name in company_name_dict:
    try:
        if (deals_industry['Deal Name'].str.contains(company_name)).any():
            industry = list(deals_industry[deals_industry['Deal Name'].str.contains(company_name)]['Industry Fin'].unique())
            if np.nan in industry:
                industry.remove(np.nan)
            company_name_dict[company_name] = industry
    except:
        continue

count = 0
for company_name in company_name_dict:
    if company_name_dict[company_name] is None:
        count+=1
print(count)
'''

# 2. Sales 기존 Category로 채우기

print(accounts['Industry Fin'].unique())
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

sales['Industry Fin'] = None
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
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Corporate')
                 & (sales['Client'].str.lower().str.contains('athleti'))].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Fitness'
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
sales.at[idx_list, 'Industry Fin'] = 'Public Association'
idx_list = sales[(sales['Industry Fin'].isna()) & (sales['Category']=='Others')].index.tolist()
sales.at[idx_list, 'Industry Fin'] = 'Others_Individual'
# category == nan


sales.to_csv('../../resource/SalesData/Whole Revenue_fillIndustry.csv', index=False)
