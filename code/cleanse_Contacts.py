import pandas as pd
import numpy as np

accounts = pd.read_csv('../resource/CleansedData/ModifiedData/Accounts_001_droppedCol_deleted_korean.csv')
contacts = pd.read_csv('../resource/CleansedData/ModifiedData/Contacts_001_droppedCol_deleted_korean.csv')

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
names = list(contacts['Sales Person'].dropna().unique())
ids = list(contacts['Customer Owner ID'].dropna().unique())

territories = {}
owner_id = {}
unique_id = {}

for name in names :
    territories[name] = []
    owner_id[name] = []


for row in contacts.index :
    for name in names :
        if (contacts['Sales Person'][row] == name) :
            territories[name].append(contacts['Territories'][row])
            owner_id[name].append(contacts['Customer Owner ID'][row])

# print unique data
for id in ids :
    unique_id[id] = []

for row in contacts.index :
    for id in ids :
        if (contacts['Customer Owner ID'][row] == id) :
            unique_id[id].append(contacts['Sales Person'][row])

for id in ids :
    print(id, set(unique_id))




# for row in contacts.index :
