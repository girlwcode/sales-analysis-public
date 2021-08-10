import pandas as pd
import numpy as np

leads = pd.read_csv('../../resource/CleansedData/ParsedData/Leads_001_droppedCol.csv')
accounts = pd.read_csv('../../resource/CleansedData/Zoho CRM/Accounts_001_IndustryCleansed.csv')

leads['Industry Fin'] = 'No'

print(leads['Industry'].nunique(), leads['Industry'].unique())

# 10673
print('row num:',len(leads))

# 257
#print(leads['Industry'].nunique(), leads['Industry'].unique())

# 1054
print('null:',leads['Industry'].isnull().sum())

# Input 이상치(Industry에 상호명, Company에 주소) 먼저 Handling
id_list = ['zcrm_1920545000002266101', 'zcrm_1920545000002266115', 'zcrm_1920545000002266123', 'zcrm_1920545000002266136', 'zcrm_1920545000002266182'
           ,'zcrm_1920545000002266187', 'zcrm_1920545000002266216','zcrm_1920545000002266152']
cnt = 0
for row in leads.index:
    title = str(leads['Company'][row]).lower()
    if (pd.isnull(leads['Sales Person'][row]) and leads['Industry'][row] != 'Private Medical' and leads['Industry'][row] != 'Defense') :
        if (',' in title):
            # 각자 맞는 자리에 넣어줌
            leads['Street'][row] = leads['Company'][row]
            leads['Company'][row] = leads['Industry'][row]
            leads['Industry'][row] = np.nan
            cnt+=1
    if (leads['Record Id'][row] in id_list) :
        # 각자 맞는 자리에 넣어줌
        leads['Street'][row] = leads['Company'][row]
        leads['Company'][row] = leads['Industry'][row]
        leads['Industry'][row] = np.nan
        cnt += 1

print(cnt)

# Accounts 딕셔너리 선언
accounts_dict = {}

for row in accounts.index:
    accounts_dict[accounts['Company Name'][row]] = accounts['Industry Fin'][row]


keywords1 = {'hopital':'Hospital',
            'college':'Academic','university' :'Academic', 'army':'Military', 'team':'Public Association', 'principal':'Public Association', 'diagno':'Clinic', 'obesit':'Clinic', 'diabe':'Clinic','school':'Academic', 'dr ':'Clinic',
            'dr.':'Clinic', 'patho':'Clinic', 'personal':'Others_Individual', 'authority':'Public Association', 'national institute':'Academic'
            ,'commissioner':'Military','rehab':'Clinic', 'vlcc':'Others_Aesthetic','asthe':'Others_Aesthetic', 'aesthe':'Others_Aesthetic',
             'mriu': 'Academic','nutricia':'Others_Others Corporate', 'medanta':'Hospital', 'shape n':'Others_Aesthetic', 'agricultural':'Academic',
             'fitness':'Fitness','hospial':'Hospital','hospital':'Hospital','hotel':'Hotel','clinic':'Clinic', 'gym':'Fitness','academy':'Academic','institution':'Public Association',
             'aseem agencies':'Private Enterprise','president':'Public Association', 'fitnes':'Fitness','seed':'Others_Others Corporate',
             'council':'Public Association'
             }

ids_keywords1 = {'Fitness':'Fitness', 'Hotel':'Hotel', 'Hospitality':'Private Enterprise', 'Corporate wellness':'Others_Aesthetic'
                ,'Corporates':'Others_Others Corporate','Academic':'Academic','Dealer':'Private Enterprise', 'Dealer_FItness':'Private Enterprise',
                'Dealer_Medical':'Private Enterprise','Enterprise':'Others_Others Corporate', 'Health Functional Food sales':'Private Enterprise',
                'Individual':'Others_Individual', 'University':'Academic', 'Public Medical':'Hospital','Public Health Center':'Fitness'
                ,'Pharmacy':'Private Enterprise', 'National and Public Institutions':'Public Association','Military base':'Military',
                'Middle budget Fitness' : 'Fitness','Key man':'Private Enterprise','Individual Fitness':'Fitness','Hospitals':'Hospital',
                'High budget Fitness':'Fitness', 'Government Medical' : 'Hospital', 'Amazon/CS' : 'Others_etc'
                }

keywords2 = {'rcf':'Others_Others Corporate', 'union bar':'Others_Others Corporate','air india':'Others_Others Corporate', 'hygeine':'Academic',
             'wellness':'Others_Aesthetic','air force':'Military','police':'Public Association','self':'Others_Individual','welingkar':'Academic',
             'st. johns':'Academic','hill rom':'Private Enterprise','health- consulting':'Private Enterprise','organisation':'Public Association',
            'subsidiary':'Military','anil awasthi':'Private Enterprise','engineering':'Others_Others Corporate','body fit line':'Fitness',
            'pilot':'Others_Others Corporate','cosco':'Others_Others Corporate','medicare':'Private Enterprise', 'ankush medicare':'Hospital',
             'navy':'Military', 'ksou':'Academic', 'dhanalakshmi srinivasan':'Academic', 'mr.' :'Others_Individual', 'student':'Others_Individual'
}

ids_keywords2 = {'Who runs Exhibition or magazine':'Others_Others Corporate', 'Surgical/medical distributers':'Private Enterprise',
                 'Sports':'Public Association', 'Sports - Hockey':'Public Association','Other':'Others_Others Corporate','Medical Device':'Private Enterprise',
                 'Sport team':'Public Association','Private Medical':'Clinic','Paramilitary':'Military','Packaging':'Others_Others Corporate',
                 'Spa':'Hotel', 'Slimming center':'Others_Aesthetic','Corporate':'Others_Others Corporate','Private Clinic':'Clinic',
                 'Institute of Physical Science':'Private Enterprise','hospitals':'Hospital','Health Center':'Others_Aesthetic','Golf Course':'Hotel',
                 'Education':'Academic','Defense':'Academic','Defence Distributors':'Private Enterprise'
                }

keywords3 = {'fit':'Fitness', 'nutri':'Clinic', 'trust':'Public Association', 'sports':'Fitness', 'officer':'Public Association',
             'food':'Private Enterprise', 'health':'Private Enterprise', 'bodypower':'Fitness'
}
# Classification 1 : Accounts에 있는 상호명이면 그 Industry 넣어주기
for row in leads.index:
    title = str(leads['Company'][row]).lower()
    for key in accounts_dict.keys():
        if title in key :
            leads['Industry Fin'][row] = accounts_dict[key]

# 1st Cleansed: 1931
print('1st Cleansed:',len(leads[leads['Industry Fin']!='No']))

# Classification 2 : Title의 Keywords 검색
for row in leads.index :
    title = str(leads['Company'][row]).lower()
    if (leads['Industry Fin'][row] == 'No'):
        for key in keywords1.keys() :
            if key in title :
                leads['Industry Fin'][row] = keywords1[key]
                #print(accounts['Company Name'][row], accounts['Industry Fin'][row])
    if (leads['Industry Fin'][row] == 'Hospital' and 'hospitality' in title) :
        leads['Industry Fin'][row] = 'Private Enterprise'

# 2nd Cleansed: 4,967
print('2nd Cleansed:',len(leads[leads['Industry Fin']!='No']))

# Classification 3: 원래 Industry로 Keywords 넣어줌
for row in leads.index:
    ids = leads['Industry'][row]
    if (leads['Industry Fin'][row] == 'No' and ids in ids_keywords1.keys()) :
        leads['Industry Fin'][row] = ids_keywords1[ids]

# 3rd Cleansed: 1,926
print('3rd Cleansed:',len(leads[leads['Industry Fin']!='No']))

# 6897
# 8824
# Print Cleansed row
print('Total Cleansed:',len(leads[leads['Industry Fin']!='No']))

# Classification 4 : Title의 Keywords 검색2
for row in leads.index :
    title = str(leads['Company'][row]).lower()
    if (leads['Industry Fin'][row] == 'No'):
        for key in keywords2.keys() :
            if key in title :
                leads['Industry Fin'][row] = keywords2[key]
                #print(accounts['Company Name'][row], accounts['Industry Fin'][row])

# Classification 5 : Industry 재 카테고리화
for row in leads.index:
    ids = leads['Industry'][row]
    if (leads['Industry Fin'][row] == 'No' and ids in ids_keywords2.keys()) :
        leads['Industry Fin'][row] = ids_keywords2[ids]

# Classification 6 : Title의 Keywords 검색2
cnt = 0
for row in leads.index :
    title = str(leads['Company'][row]).lower()
    if (leads['Industry Fin'][row] == 'No'):
        for key in keywords3.keys() :
            if key in title :
                leads['Industry Fin'][row] = keywords3[key]
            else:
                leads['Industry Fin'][row] = 'Others_Others Corporate'

    if (leads['Company'][row] == 'inbody' or leads['Company'][row] == 'In body band' or  leads['Company'][row] == '=-she is job candidate'
    or leads['Company'][row] == 'None'):
        leads = leads.drop(index=row, axis=0)
        cnt +=1

# 이상치 제거 - 9건
print(cnt)

# Print Not Cleansed row
is_not_changed = leads['Industry Fin'] == 'No'
parse = leads[is_not_changed]
print('Not Cleansed:',len(parse))

leads.to_csv('../../resource/CleansedData/Leads_001_IndustryCleansed.csv',index=False)