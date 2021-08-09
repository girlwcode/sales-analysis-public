import pandas as pd

origin_data_path = '../../resource/OriginalData/'

# Enter the case (contacts = 1 or leads = 2)
case = 2
if case == 1 :
    file_name = 'Contacts_001'
    contacts = pd.read_csv(origin_data_path + file_name + '.csv')
    datas = contacts
elif case == 2 :
    file_name = 'Leads_001'
    leads = pd.read_csv(origin_data_path+file_name+'.csv')
    datas = leads

print('Before dropped: ',len(datas))

drop_col1 = 'Unsubscribed Mode'
drop_col2 = 'Unsubscribed Time'
row = list()

for data in datas.index :
    if (datas[drop_col1][data] == 'Manual') :
        row.append(data)


print(row)
datas = datas.drop(row)

if case == 1 :
    contacts = datas
    print(contacts[drop_col1].unique())
    print(contacts[drop_col2].unique())
    print(len(contacts))
    contacts.to_csv('../resource/CleansedData/ModifiedData/Contacts_001_unsubscribed_row_deleted.csv',index=False)
elif case == 2 :
    leads = datas
    print(leads[drop_col1].unique())
    print(leads[drop_col2].unique())
    print(len(leads))
    leads.to_csv('../resource/CleansedData/ModifiedData/Leads_001_unsubscribed_row_deleted.csv',index=False)



