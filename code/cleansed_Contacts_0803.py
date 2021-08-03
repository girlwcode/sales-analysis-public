import pandas as pd

contacts = pd.read_csv('../resource/CleansedData/ModifiedData/Contacts_001_droppedCol_deleted_korean.csv')
accounts = pd.read_csv('../resource/CleansedData/ModifiedData/Accounts_001_concat_state.csv')
deal = pd.read_csv('../resource/CleansedData/ModifiedData/Potentials_001_USDtoINR.csv')

print(accounts['Territories'].unique())

# 3134
print(accounts['Territories'].isna().sum())
# 1408
print(contacts['Territories'].isna().sum())

# 23 'Arun Sharma' 'Mahesh Gulwani' 'Taukheer Ahmed' 'Karn Sharma'
#  'Ashwini Dixit' 'Anees Mukhtar' 'Shubham Tonk' 'Ayan' 'CS/Amazon/Other'
#  'Nasir' 'Nihal Pawar' 'Dixiata Sharma' 'Aaruni Sinha' 'Chris Shin'
#  'Mrunal Sardar' 'Mohammad Afnan' 'Gurraj Singh' 'Kenneth Cha'
#  'Prasad Gosavi' 'Ankita' 'Abhinanda Ghosh' 'Puneet Shukla'
#  'Neelabh Kashyap'
print(accounts['Sales Person'].nunique(),accounts['Sales Person'].unique())

# 22 'Karn Sharma' 'Arun Sharma' 'Mahesh Gulwani' 'Taukheer Ahmed'
#  'Kenneth Cha' 'Anees Mukhtar' 'Shubham Tonk' 'Ashwini Dixit'
#  'Nihal Pawar' 'Nasir' 'Dixita Sharma' 'Ayan' 'Chris Shin' 'Mrunal Sardar'
#  'Afnan Mohammed' 'Gurraj Singh' 'Aaruni Sinha' 'Prasad Gosavi'
#  'Puneet Shukla' 'Ankita' 'Neelabh Kashyap' 'Abhinanda Ghosh'
print(contacts['Sales Person'].nunique(), contacts['Sales Person'].unique())

territories = {}
owner_id = {}

# 1. 직원별 territory dict 저장
for i in contacts.index:
    if pd.notnull(contacts.loc[i, 'Sales Person']) and pd.notnull(contacts.loc[i, 'Territories']):
        name = contacts.loc[i, 'Sales Person']
        territory = contacts.loc[i, 'Territories']
        if name not in territories:
            territories[name] = []
        territories[name].append(territory)

# territory dict 출력 - 8개
name_list = []
for name in territories:
    if len(set(territories[name])) == 1:
        # print(name, ':', set(territories[name]))
        name_list.append(name)


# 2. id 별 territory
for i in contacts.index:
    if pd.notnull(contacts.loc[i, 'Territories']) :
        id = contacts.loc[i, 'Customer Owner ID']
        territory = contacts.loc[i, 'Territories']
        if id not in owner_id:
            owner_id[id] = []
        owner_id[id].append(territory)

# territory dict 출력 - 9개
id_dict = {}
for id in owner_id:
    if len(set(owner_id[id])) == 1:
        print(id, ':', set(owner_id[id]))
        id_dict[id] = owner_id[id][0]

# 1. 직원별 territory dict 고유값 채워주기 - 3개
for i in contacts.index:
    if contacts.loc[i, 'Sales Person'] in name_list and pd.isnull(contacts.loc[i, 'Territories']):
        person_name = contacts.loc[i, 'Sales Person']
        if person_name in ['Taukheer Ahmed', 'Dixita Sharma']:
            contacts.loc[i, 'Territories'] = 'South'
        elif person_name in ['Ayan', 'Afnan Mohammed', 'Gurraj Singh', 'Neelabh Kashyap', 'Abhinanda Ghosh']:
            contacts.loc[i, 'Territories'] = 'West 1'
        elif person_name == 'Prasad Gosavi':
            contacts.loc[i, 'Territories'] = 'North'


# 2. id별 territory dict 고유값 채워주기 - 10개
for i in contacts.index:
    if contacts.loc[i, 'Customer Owner ID'] in id_dict and pd.isnull(contacts.loc[i, 'Territories']):
        contacts['Territories'][i] = id_dict[contacts.loc[i, 'Customer Owner ID']]
        # print(id_dict[contacts.loc[i, 'Customer Owner ID']], contacts['Territories'][i])

# 3. deal의 CompanyID와 연동하여 territory 찾기
company_id = {}
for i in contacts.index:
    if contacts['Territories'][i].isna():
        break


# Parsing the dataset
contacts.to_csv('../resource/CleansedData/Contacts_001_fillTerritory_ver1.csv', index=False)
