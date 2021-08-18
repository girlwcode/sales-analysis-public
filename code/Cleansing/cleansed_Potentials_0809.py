import pandas as pd
import numpy as np

deal = pd.read_csv('../../resource/CleansedData/ParsedData/Potentials_001_droppedCol.csv')
deal_missing = pd.read_csv('../../resource/SaveCol/potential_missing.csv')

# 원본
contacts = pd.read_csv('../../resource/CleansedData/ParsedData/Contacts_001_droppedCol.csv')
accounts = pd.read_csv('../../resource/CleansedData/ParsedData/Accounts_001_droppedCol.csv')

# 전처리본
contacts_fill = pd.read_csv('../../resource/CleansedData/ZohoCRM/Contacts_001_fillTerritories_ver2.csv')
accounts_fill = pd.read_csv('../../resource/CleansedData/ZohoCRM/Accounts_001_fillTerritories_final.csv')

deal['Territory_fin'] = np.nan

# 결측값 dict - Contacts Handling때 No로 해놓음 (후처리 필요)
no_contact = {'zcrm_1920545000000170005' : 'South', 'zcrm_1920545000000171005' : 'South','zcrm_1920545000000203133' : 'South'
    ,'zcrm_1920545000001815001' : 'East','zcrm_1920545000005790010' : 'West 1','zcrm_1920545000013720001' : 'East'
}

# 원본 dict
contacts_original_dict ={}
for row in contacts.index :
    contacts_original_dict[contacts['Company ID'][row]] = contacts['Territories'][row]

accounts_original_dict ={}
for row in accounts.index :
    contacts_original_dict[accounts['Record Id'][row]] = accounts['Territories'][row]


# 전처리 dict
contacts_dict ={}
for row in contacts_fill.index :
    contacts_dict[contacts_fill['Company ID'][row]] = contacts_fill['Territories'][row]

accounts_dict ={}
for row in accounts_fill.index :
    accounts_dict[accounts_fill['Record Id'][row]] = accounts_fill['Territories'][row]

print('row:', len(deal))
print('Null:', deal['Territory'].isna().sum())

cnt = 0
cnt2 = 0
cnt3 =0
missing_id = list()
m = list()
missing_add = {}

for row in deal.index :
    if (deal['Company ID'][row] in no_contact.keys()) :
        deal['Territory_fin'][row] = no_contact[deal['Company ID'][row]]

    elif (deal['Company ID'][row] in accounts_dict.keys()):
        cnt2 +=1
        deal['Territory_fin'][row] = accounts_dict[deal['Company ID'][row]]

    elif(deal['Company ID'][row] in contacts_dict.keys()):
        cnt3 +=1
        deal['Territory_fin'][row] = contacts_dict[deal['Company ID'][row]]

    elif (deal['Company ID'][row] in deal_missing) :
        deal['Territory_fin'][row] = deal_missing[deal['Company ID'][row]][4]
        cnt +=1

# Contacts 도 후처리
for row in contacts_fill.index:
    if (contacts_fill['Company ID'][row] in no_contact.keys()):
        contacts_fill['Territories'][row] = no_contact[contacts_fill['Company ID'][row]]

contacts_fill.to_csv('../../resource/CleansedData/Contacts_001_fillTerritories_final.csv', index=False)



print('contacts ori:',cnt)
print('accounts fill :',cnt2)
print('contacts fill :',cnt3)



print('Not Cleansed:', deal['Territory_fin'].isnull().sum())
deal.to_csv('../../resource/CleansedData/Potentials_001_fillTerritories_final.csv',index=False)
