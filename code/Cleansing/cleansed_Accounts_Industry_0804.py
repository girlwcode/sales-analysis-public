import pandas as pd
import numpy as np

# Industry Cleansing
accounts = pd.read_csv('../../resource/CleansedData/ZohoCRM/Accounts_001_fillTerritories_final.csv')
deal = pd.read_csv('../../resource/CleansedData/ParsedData/Potentials_001_droppedCol.csv')
peoples = pd.read_csv('../../resource/SaveCol/upper_names.txt', header=None)

peoples = list(np.array(peoples[0].tolist()))

print(peoples)

accounts['Industry Fin'] = 'No'

#print(deal.columns)
#'Industry', 'Sub industry'
#print(accounts.columns)

# 34개, ['Hospitality' 'Fitness' 'Government Medical' 'Health Center' 'Others'
#  'Sport team' 'Public Medical' 'Individual Fitness' 'Dealer_FItness'
#  'Defense' 'Enterprise' 'University' 'Hotel' 'Dealer' 'Private Medical'
#  'National and Public Institutions' 'Military base'
#  'Health Functional Food sales' 'Key man' 'Public Health Center' 'Sports'
#  'Dealer_Medical' 'Pharmacy' 'High budget Fitness' 'Middle budget Fitness'
#  'Individual' 'Diagnostic center' 'Spa' 'Corporate wellness' 'Corporates'
#  'Academic' 'Hospitals' 'Amazon/CS' 'Aarti Diagnostic Centre']
#print(accounts['Industry'].nunique(), accounts['Industry'].unique())

industry1 = pd.DataFrame(accounts['Industry'].unique())
industry2 = pd.DataFrame(accounts['Sub industry'].unique())
# 1433개
#print(accounts['Industry'].isnull().sum())

# 19개,'Dietician' 'Medical' 'Bariatric' 'Medium Budget Fitness'
#  'Corporates' 'High Budget Fitness' 'Low Budget Fitness'
#  'Slimming Centers' 'Wellness' 'Fitness' 'Other' 'Endocrinologist'
#  'Diabetic' 'Nephrology' 'Corporate Wellness' 'Dietitian' 'Academic'
#  'General Medicine' 'Pediatric'
#print(accounts['Sub industry'].nunique(), accounts['Sub industry'].unique())
print('row num:',len(accounts))
# 3899개
#print(accounts['Sub industry'].isnull().sum())
industry = pd.concat([industry1,industry2])
#industry.to_csv('Industry.csv')

keywords1 = {'hospital':'Hospital','hotel':'Hotel','clinic':'Clinic', 'gym':'Fitness','academy':'Academic',
            'college':'Academic','university' :'Academic', 'army':'Military', 'team':'Public Association', 'institution':'Public Association'
               , 'principal':'Public Association', 'diagno':'Clinic', 'obesit':'Clinic', 'diabe':'Clinic','school':'Academic', 'dr ':'Clinic',
            'dr.':'Clinic', 'patho':'Clinic', 'personal':'Others_Individual', 'authority':'Public Association', 'national institute':'Academic'
            ,'commissioner':'Military','rehab':'Clinic', 'vlcc':'Others_Aesthetic','asthe':'Others_Aesthetic', 'aesthe':'Others_Aesthetic',
             'mriu': 'Academic','nutricia':'Others_Others Corporate', 'medanta':'Hospital', 'shape n':'Others_Aesthetic', 'agricultural':'Academic','fitness':'Fitness'}

ids_keywords = {'Fitness':'Fitness', 'Hotel':'Hotel', 'Hospitality':'Private Enterprise', 'Corporate wellness':'Others_Aesthetic'
                ,'Corporates':'Others_Others Corporate','Academic':'Academic','Dealer':'Private Enterprise', 'Dealer_FItness':'Private Enterprise',
                'Dealer_Medical':'Private Enterprise','Enterprise':'Others_Others Corporate', 'Health Functional Food sales':'Private Enterprise',
                'Individual':'Others_Individual', 'University':'Academic', 'Public Medical':'Hospital','Public Health Center':'Fitness'
                ,'Pharmacy':'Private Enterprise', 'National and Public Institutions':'Public Association','Military base':'Military',
                'Middle budget Fitness' : 'Fitness','Key man':'Private Enterprise','Individual Fitness':'Fitness','Hospitals':'Hospital',
                'High budget Fitness':'Fitness', 'Government Medical' : 'Hospital', 'Amazon/CS' : 'Others_Others Corporate'
                }

keywords2 = {'self':'Others_Individual', 'dietician':'Clinic', 'insurance':'Private Enterprise', 'loss':'Clinic', 'mechanics':'Fitness','association':'Public Association',
             'football':'Public Association', 'fit':'Fitness', 'diet centre' : 'Clinic', 'path lab' :'Clinic', 'safe': 'Clinic',
             'dt ':'Clinic', 'dt.':'Clinic', 'diet':'Clinic', 'ms.':'Others_Individual', 'mr ':'Others_Individual', 'mr.':'Others_Individual',
             'nutri':'Private Enterprise','nutritionist':'Clinic','healthcare':'Hospital', 'wellness':'Others_Aesthetic', 'cosmetics':'Others_Aesthetic', 'force':'Public Association',
             'medical':'Hospital','bodycare':'Others_Aesthetic','vibes':'Others_Aesthetic', 'inorbvict':'Private Enterprise', 'sbm':'Private Enterprise',
             'health club':'Fitness'
}

ids_keywords2 = {'Sports':'Private Enterprise', 'Private Medical':'Private Enterprise', 'Health Center':'Others_Aesthetic','Defense':'Private Enterprise',
                 'Others':'Others_Others Corporate'}

keywords3 = {'club':'Hotel','tech':'Others_Others Corporate', 'health':'Private Enterprise', 'health club':'Fitness',
             'federation':'Public Association','foundation':'Public Association', 'ltd':'Others_Others Corporate', 'body':'Fitness','studio':'Others_Others Corporate' ,
             'sakthivel.a':'Academic', 'enterpri':'Private Enterprise', 'private':'Others_Others Corporate', 'sai ':'Private Enterprise',
             'm.m':'Public Association', 'officer':'Military', 'company':'Others_Others Corporate', 'beast':'Clinic', 'Slimming':'Private Enterprise',
             'centr':'Clinic','Talwalkars':'Fitness', 'franchise':'Fitness', 'develop':'Others_Others Corporate', 'iifw':'Others_Others Corporate', 'square':'Others_Others Corporate',
             'corporation':'Others_Others Corporate', 'limited':'Others_Others Corporate','life':'Clinic','llp':'Others_Others Corporate', 'general':'Public Association','seven':'Others_Others Corporate' ,
             'olympic':'Others_Others Corporate', 'physio':'Clinic', 'equipment':'Private Enterprise','push':'Fitness', 'associate':'Public Association',
             'solution':'Private Enterprise', 'infra':'Others_Others Corporate', 'nuelife':'Private Enterprise', 'squad':'Others_Others Corporate','workout':'Fitness',
             'resort':'Hotel', 'venture':'Others_Others Corporate', 'sprinklr':'Others_Others Corporate', 'cdmdt':'Public Association', 'eat':'Clinic','commander':'Military',
}

# Classification 1
for row in accounts.index :
    title = accounts['Company Name'][row].lower()
    for key in keywords1.keys() :
        if key in title :
            accounts['Industry Fin'][row] = keywords1[key]
            #print(accounts['Company Name'][row], accounts['Industry Fin'][row])
    if (accounts['Industry Fin'][row] == 'Hospital' and 'hospitality' in title) :
        accounts['Industry Fin'][row] = 'Private Enterprise'

for row in accounts.index:
    ids = accounts['Industry'][row]
    if (accounts['Industry Fin'][row] == 'No' and ids in ids_keywords.keys()) :
        accounts['Industry Fin'][row] = ids_keywords[ids]

# Classification 2
for row in accounts.index :
    if (accounts['Industry Fin'][row] == 'No'):
        title = accounts['Company Name'][row].lower()
        for key in keywords2.keys() :
            if key in title :
                accounts['Industry Fin'][row] = keywords2[key]
                #print(accounts['Company Name'][row], accounts['Industry Fin'][row])

        # Arth == 'Clinic"
        if (title == 'arth') :
            accounts['Industry Fin'][row] = 'Clinic'

        if (accounts['Sales Person'][row] == 'CS/Amazon/Other'):
            accounts['Industry Fin'][row] = 'Others_etc'


for row in accounts.index:
    ids = accounts['Industry'][row]
    if (accounts['Industry Fin'][row] == 'No' and ids in ids_keywords2.keys()) :
        accounts['Industry Fin'][row] = ids_keywords2[ids]

# Classification 3
for row in accounts.index :
    if (accounts['Industry Fin'][row] == 'No'):
        title = accounts['Company Name'][row].lower()
        for key in keywords3.keys() :
            if key in title :
                accounts['Industry Fin'][row] = keywords3[key]
                #print(accounts['Company Name'][row], accounts['Industry Fin'][row])


# Classification 4
upper = list()
for row in accounts.index :
    if (accounts['Industry Fin'][row] == 'No'):
        title = accounts['Company Name'][row]
        if(str(title).isupper()):
            upper.append(title)

cnt = 0
for row in accounts.index:
    if (accounts['Industry Fin'][row] == 'No'):
        title = accounts['Company Name'][row]
        if(title in upper and title not in peoples):
            if (title == 'T VENUGOPAL' or title == 'NIKHIL PRABHAKAR BURUTE'):
                accounts['Industry Fin'][row] = 'Clinic'
            else : accounts['Industry Fin'][row] = 'Others_Others Corporate'

        elif(title in upper and title in peoples):
            accounts['Industry Fin'][row] = 'Others_Individual'
        else: accounts['Industry Fin'][row] = 'Others_etc'

    # 이상치 제거
    if ('inbody' in accounts['Company Name'][row].lower() or accounts['Company Name'][row].lower() == 'unknown'):
        accounts = accounts.drop(index=row, axis=0)
        cnt += 1

print(cnt)
#upper = pd.DataFrame(upper)
#upper.to_csv('upper_names.txt',index=False)

print('Cleansed:',len(accounts[accounts['Industry Fin']!='No']))


is_not_changed = accounts['Industry Fin'] == 'No'
parse = accounts[is_not_changed]
print('Not Cleansed:',len(parse))

#14개
#print(accounts['Industry Fin'].nunique(), accounts['Industry Fin'].unique())

accounts = accounts.drop(['Industry','Sub industry'],axis=1)
accounts.to_csv('../../resource/CleansedData/ZohoCRM/Accounts_001_IndustryCleansed.csv',index=False)