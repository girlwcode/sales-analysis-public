import pandas as pd

accounts = pd.read_csv('../resource/CleansedData/Accounts_001_fillTerritory_ver1.csv')
contacts = pd.read_csv('../resource/CleansedData/Contacts_001_fillTerritory_ver1.csv')

dict_accounts = {}
dict_contacts = {}

for i in accounts.index:
    if pd.notnull(accounts['Territories'][i]):
        id = accounts['Record Id'][i]
        dict_accounts[id] = accounts['Territories'][i]

for i in contacts.index:
    if pd.notnull(contacts['Territories'][i]):
        id = contacts['Company ID'][i]
        dict_contacts[id] = contacts['Territories'][i]


# account territory 채움 (9개)
for i in accounts.index:
    if accounts['Record Id'][i] in dict_contacts.keys() and pd.isnull(accounts['Territories'][i]):
        accounts['Territories'][i] = dict_contacts[accounts['Record Id'][i]]


# contacts territory 채움 (20개)
for i in contacts.index:
    if contacts['Company ID'][i] in dict_accounts.keys() and pd.isnull(contacts['Territories'][i]):
        contacts['Territories'][i] = dict_accounts[contacts['Company ID'][i]]

# 3081
print(accounts['Territories'].isna().sum())
# 1301
print(contacts['Territories'].isna().sum())

accounts=accounts.dropna(subset=['Territories'],axis=0)
contacts=contacts.dropna(subset=['Territories'],axis=0)

print(accounts['Territories'].isna().sum())
print(contacts['Territories'].isna().sum())

# data pharsing
accounts.to_csv('../resource/CleansedData/Accounts_001_fillTerritories_final.csv', index=False)
contacts.to_csv('../resource/CleansedData/Contacts_001_fillTerritories_final.csv', index=False)







