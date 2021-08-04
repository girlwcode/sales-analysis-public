import pandas as pd

# Industry Cleansing
accounts = pd.read_csv('../resource/CleansedData/Accounts_001_fillTerritories_final.csv')
deal = pd.read_csv('../resource/CleansedData/ParsedData/Potentials_001_droppedCol.csv')

accounts['Industry Fin'] = 'No'

print(deal.columns)
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

keywords = {'hospital':'Hospital','hotel':'Hotel','clinic':'Clinic','fitness':'Fitness', 'gym':'Fitness','academy':'Academic',
            'college':'Academic','university' :'Academic', 'army':'Millitary', 'team':'Public Association', 'institution':'Public Association'
               , 'principal':'Public Association', 'diagno':'Clinic', 'obesit':'Clinic', 'diabe':'Clinic','school':'Academic', 'dr ':'Clinic',
            'dr.':'Clinic', 'patho':'clinic', 'personal':'Others'}

ids_keywords = {'Fitness':'Fitness', 'Hotel':'Hotel', 'Hospitality':'Private Enterprise', 'Corporate wellness':'Others'
                ,'Corporates':'Others','Academic':'Academic','Dealer':'Private Enterprise', 'Dealer_FItness':'Private Enterprise',
                'Dealer_Medical':'Private Enterprise','Enterprise':'Others', 'Health Functional Food sales':'Private Enterprise',
                'Individual':'Others', 'University':'Academic'}

cnt = 0
for row in accounts.index :
    title = accounts['Company Name'][row].lower()
    for key in keywords.keys() :
        if key in title :
            accounts['Industry Fin'][row] = keywords[key]
            #print(accounts['Company Name'][row], accounts['Industry Fin'][row])
            cnt+=1
    if (accounts['Industry Fin'][row] == 'Hospital' and 'hospitality' in title) :
        accounts['Industry Fin'][row] = 'Private Enterprise'

for row in accounts.index:
    ids = accounts['Industry'][row]
    if (accounts['Industry Fin'][row] == 'No' and ids in ids_keywords.keys()) :
        accounts['Industry Fin'][row] = ids_keywords[ids]
        cnt += 1



#1953
#2000
#2010
#2024
#2040
#2107
print('Cleansed:',cnt)


is_not_changed = accounts['Industry Fin'] == 'No'
parse = accounts[is_not_changed]
print('Not Cleansed:',len(parse))
# 2066
# 2050
# 1984
# 1781
# 1778
# 1744
parse.to_csv('No change.csv',index=False)

accounts.to_csv('Changed.csv',index=False)