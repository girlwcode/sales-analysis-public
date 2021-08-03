import pandas as pd

#143개 채움
path='../resource/CleansedData/ModifiedData/'
file_name='Accounts_001_concat_state'
accounts =pd.read_csv(path+file_name+'.csv')

deal = pd.read_csv()

# territories Unique 값 - 'South' 'South, West 2' 'East' 'West 1' 'West 2' 'North'
#  'South, North' 'North, West 1' 'North, East' 'South, East' 'East, West 1'
#  'North, West 2' 'South, West 1' 'West 1, West 2'
print(accounts['Territories'].unique())

# territories 결측치 - 3134개
print(accounts['Territories'].isna().sum())

# Sales Person Unique 값 - 23개 'Arun Sharma' 'Mahesh Gulwani' 'Taukheer Ahmed' 'Karn Sharma'
#  'Ashwini Dixit' 'Anees Mukhtar' 'Shubham Tonk' 'Ayan' 'CS/Amazon/Other'
#  'Nasir' 'Nihal Pawar' 'Dixiata Sharma' 'Aaruni Sinha' 'Chris Shin'
#  'Mrunal Sardar' 'Mohammad Afnan' 'Gurraj Singh' 'Kenneth Cha'
#  'Prasad Gosavi' 'Ankita' 'Abhinanda Ghosh' 'Puneet Shukla'
#  'Neelabh Kashyap'
print(accounts['Sales Person'].nunique(), accounts['Sales Person'].unique())

# dict
territories = {}
owner_id = {}

# 직원별 territory dict 저장
for i in accounts.index:
    if pd.notnull(accounts.loc[i, 'Sales Person']) and pd.notnull(accounts.loc[i, 'Territories']):
        name = accounts.loc[i, 'Sales Person']
        territory = accounts.loc[i, 'Territories']
        if name not in territories:
            territories[name] = []
        territories[name].append(territory)


# name - territory dict 생성 및 출력 - 8개
name_dict = {}
for name in territories:
    if len(set(territories[name])) == 1:
        print(name, ':', set(territories[name]))
        name_dict[name] = territories[name][0]

# Unique 재 확인
# l = list()
# for row in accounts.index:
#     if accounts['Sales Person'][row] == 'Taukheer Ahmed' :
#         l.append(accounts['Territories'][row])

# id 별 territory
for i in accounts.index:
    if pd.notnull(accounts.loc[i, 'Territories']) :
        id = accounts.loc[i, 'Company Owner ID']
        territory = accounts.loc[i, 'Territories']
        if id not in owner_id:
            owner_id[id] = []
        owner_id[id].append(territory)

# territory dict 출력 - 10개
id_dict = {}
for id in owner_id:
    if len(set(owner_id[id])) == 1:
        print(id, ':', set(owner_id[id]))
        id_dict[id] = owner_id[id][0]
        # name_list.append(name)

# 1. 직원별 territory dict 고유값 채워주기 - 7개
#cnt = 0
for i in accounts.index:
    if accounts.loc[i, 'Sales Person'] in name_dict and pd.isnull(accounts.loc[i, 'Territories']):
        n = accounts.loc[i, 'Sales Person']
        accounts['Territories'][i] = name_dict[n]
        #print(name_dict[accounts.loc[i, 'Sales Person']], accounts['Territories'][i])
        #cnt+=1
#print(cnt)

# 2. id별 territory dict 고유값 채워주기 - 18개
#cnt = 0
for i in accounts.index:
    if accounts.loc[i, 'Company Owner ID'] in id_dict and pd.isnull(accounts.loc[i, 'Territories']):
        n = accounts.loc[i, 'Company Owner ID']
        accounts['Territories'][i] = id_dict[n]
        #print(id_dict[accounts.loc[i, 'Company Owner ID']], accounts['Territories'][i])
        #cnt += 1
#print(cnt)

# Parsing the dataset
#accounts.to_csv('../resource/CleansedData/Contacts_001_fillTerritory_ver1.csv', index=False)