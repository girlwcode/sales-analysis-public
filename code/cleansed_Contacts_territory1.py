import pandas as pd

contacts = pd.read_csv('../resource/CleansedData/ModifiedData/Contacts_001_droppedCol_deleted_korean.csv')

territories = {}
for i in contacts.index:
    if pd.notnull(contacts.loc[i, 'Sales Person']) and pd.notnull(contacts.loc[i, 'Territories']):
        name = contacts.loc[i, 'Sales Person']
        territory = contacts.loc[i, 'Territories']
        if name not in territories:
            territories[name] = []
        territories[name].append(territory)

name_list = []
for name in territories:
    if len(set(territories[name])) == 1:
        print(name, ':', set(territories[name]))
        name_list.append(name)

for i in contacts.index:
    if contacts.loc[i, 'Sales Person'] in name_list and pd.isnull(contacts.loc[i, 'Territories']):
        person_name = contacts.loc[i, 'Sales Person']
        if person_name in ['Taukheer Ahmed', 'Dixita Sharma']:
            contacts.loc[i, 'Territories'] = 'South'
        elif person_name in ['Ayan', 'Afnan Mohammed', 'Gurraj Singh', 'Neelabh Kashyap', 'Abhinanda Ghosh']:
            contacts.loc[i, 'Territories'] = 'West 1'
        elif person_name == 'Prasad Gosavi':
            contacts.loc[i, 'Territories'] = 'North'

contacts.to_csv('../resource/CleansedData/Contacts_001_fillTerritory_ver1.csv', index=False)
