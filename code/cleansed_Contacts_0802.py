import pandas as pd

contacts = pd.read_csv('../resource/CleansedData/ModifiedData/Contacts_001_droppedCol_deleted_korean.csv')
accounts = pd.read_csv('../resource/CleansedData/ModifiedData/Accounts_001_droppedCol_deleted_korean.csv')

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
ids = {}

# 직원별 territory dict 저장
for i in contacts.index:
    if pd.notnull(contacts.loc[i, 'Sales Person']) and pd.notnull(contacts.loc[i, 'Territories']):
        name = contacts.loc[i, 'Sales Person']
        territory = contacts.loc[i, 'Territories']
        if name not in territories:
            territories[name] = []
        territories[name].append(territory)

# territory dict 출력
name_list = []
for name in territories:
    if len(set(territories[name])) == 1:
        # print(name, ':', set(territories[name]))
        name_list.append(name)

# # 직원별 id dict 저장
# for i in contacts.index:
#     if pd.notnull(contacts.loc[i, 'Sales Person']) :
#         name = contacts.loc[i, 'Sales Person']
#         id = contacts.loc[i, 'Customer Owner ID']
#         if name not in owner_id:
#             owner_id[name] = []
#         owner_id[name].append(id)
#
# # 직원별 id dict - 고유 id 저장
# id_list1 = list()
# for name in owner_id :
#     if len(set(owner_id[name])) == 1:
#         # print(name,':', set(owner_id[name]))
#         a = owner_id[name][0]
#         id_list1.append(a)

# ID 별 직원 dict 저장
for i in contacts.index:
    if pd.notnull(contacts.loc[i, 'Sales Person']) :
        id = contacts.loc[i, 'Customer Owner ID']
        name = contacts.loc[i, 'Sales Person']
        if id not in ids:
            ids[id] = []
        ids[id].append(name)

# ID 별 직원 dict - 고유 ID 저장
id_list2 = list()
for id in ids :
    if len(set(ids[id])) == 1:
        print(id,':', set(ids[id]))
        a = ids[id][0]
        id_list2.append(a)

print(id_list2)
for n in id_list2 :
    cnt = 0
    for id in ids :
        if n in ids[id] :
            cnt += 1
    print(cnt)
    if cnt == 1 :
        print(n)


# 직원별 territory dict 고유값 채워주기
for i in contacts.index:
    if contacts.loc[i, 'Sales Person'] in name_list and pd.isnull(contacts.loc[i, 'Territories']):
        person_name = contacts.loc[i, 'Sales Person']
        if person_name in ['Taukheer Ahmed', 'Dixita Sharma']:
            contacts.loc[i, 'Territories'] = 'South'
        elif person_name in ['Ayan', 'Afnan Mohammed', 'Gurraj Singh', 'Neelabh Kashyap', 'Abhinanda Ghosh']:
            contacts.loc[i, 'Territories'] = 'West 1'
        elif person_name == 'Prasad Gosavi':
            contacts.loc[i, 'Territories'] = 'North'

# contacts.to_csv('../resource/CleansedData/Contacts_001_fillTerritory_ver1.csv', index=False)
