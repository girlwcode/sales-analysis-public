import pandas as pd
import re


path='../resource/CleansedData/ModifiedData/'
file_name='Accounts_001_droppedCol_deleted_korean'
csv=pd.read_csv(path+file_name+'.csv')
save_as='../resource/CleansedData/ModifiedData/Accounts_001_filled_territory_by_sales_man.csv'

people=set()
for person in csv['Sales Person']:
        people.add(str(person))


csv.count()


print(people)


mapping=dict()

for person in people:
    mapping[person]=set()


print(mapping)


for i in range(len(csv['Sales Person'])):
    if csv['Sales Person'][i] in people:
        mapping[csv['Sales Person'][i]].add(csv['Territories'][i])

print(mapping)


people=set()
people.add('Mohammad Afnan')
people.add('Dixiata Sharma')
people.add('Gurraj Singh')
people.add('Abhinanda Ghosh') 
people.add('Nasir')
people.add('Puneet Shukla')
people.add('Neelabh Kashyap')

count=0
for i in range(len(csv['Territories'])):
    if csv['Sales Person'][i] in people:
        csv['Territories'][i] = mapping[person]
        count+=1
print(count)
#csv


print(len(csv))
print(csv['Territories'].count())
print(csv['Territories'].notna().sum() + csv['Territories'].isnull().sum())


for person in csv['Sales Person']:
    if person in people:
        csv['Territories'] = mapping[person]
csv = csv.to_csv(save_as,index=False)