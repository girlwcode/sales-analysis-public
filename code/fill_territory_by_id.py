import pandas as pd
import re
#143개 채움
path='../resource/CleansedData/ModifiedData/'
file_name='Accounts_001_droppedCol_deleted_korean'
csv=pd.read_csv(path+file_name+'.csv')
save_as='../resource/CleansedData/ModifiedData/Accounts_001_unique_id.csv'
ids=set()
cnt=0
for id in csv['Company Owner ID']:
        ids.add(id)
len(ids)

print(ids)

mapping={}
for id in ids:
    mapping[id]=set()

for i in range(len(csv['Company Owner ID'])):
    if csv['Company Owner ID'][i] in ids:
            mapping[csv['Company Owner ID'][i]].add(csv['Territories'][i])
print(mapping)

#zcrm_1920545000011182001,
# zcrm_1920545000000243029,
# zcrm_1920545000004627001,
# zcrm_1920545000000243023,
# zcrm_1920545000018425001,
# zcrm_1920545000012187001,
# zcrm_1920545000008102001,
# zcrm_1920545000015984001
#zcrm_1920545000015984001,
# zcrm_1920545000012076001

only_ids=set()

only_ids.add('zcrm_1920545000011182001')
only_ids.add( 'zcrm_1920545000000243029')
only_ids.add( 'zcrm_1920545000004627001')
only_ids.add( 'zcrm_1920545000000243023')
only_ids.add( 'zcrm_1920545000018425001')
only_ids.add( 'zcrm_1920545000012187001')
only_ids.add( 'zcrm_1920545000008102001')
only_ids.add( 'zcrm_1920545000015984001')
only_ids.add('zcrm_1920545000015984001')
only_ids.add( 'zcrm_1920545000012076001')


cnt=0
for i in range(len(csv['Territories'])):
    if csv['Company Owner ID'][i] in only_ids:
            csv['Territories'][i]=str(mapping[csv['Company Owner ID'][i]])
            cnt+=1
print(cnt)

csv.to_csv('cleansed_id_torritory.csv',index=False)