import pandas as pd

#143개 채움
path='../resource/CleansedData/ModifiedData/'
file_name='Accounts_001_droppedCol_deleted_korean'
accounts =pd.read_csv(path+file_name+'.csv')
save_as='../resource/CleansedData/ModifiedData/Accounts_001_unique_id.csv'


# territories Unique 값 - 'South' 'South, West 2' 'East' 'West 1' 'West 2' 'North'
#  'South, North' 'North, West 1' 'North, East' 'South, East' 'East, West 1'
#  'North, West 2' 'South, West 1' 'West 1, West 2'
print(accounts['Territories'].unique())

# territories 결측치 - 3134개
print(accounts['Territories'].isna().sum())

# Sales Person Unique 값 - 23개 'Arun Sharma' 'Mahesh Gulwani' 'Taukheer Ahmed' 'Karn Sharma'
#  'Ashwini Dixit' 'Anees Mukhtar' 'Shubham Tonk' 'Ayan' 'CS/Amazon/Other'
#  'Nasir' 'Nihal Pawar' 'Dixiata Sharma' 'Aaruni Sinha' 'Chris Shin'
#  'Mrunal Sardar' 'Mohammad Afnan' 'Gurraj Singh' 'Kenneth Cha'
#  'Prasad Gosavi' 'Ankita' 'Abhinanda Ghosh' 'Puneet Shukla'
#  'Neelabh Kashyap'
print(accounts['Sales Person'].nunique(),accounts['Sales Person'].unique())

# dict
territories = {}
owner_id = {}

# 직원별 territory dict 저장
for i in accounts.index:
    if pd.notnull(accounts.loc[i, 'Sales Person']) and pd.notnull(accounts.loc[i, 'Territories']):
        name = accounts.loc[i, 'Sales Person']
        territory = accounts.loc[i, 'Territories']
        if name not in territories:
            territories[name] = []
        territories[name].append(territory)

# territory dict 출력 - 8개
name_list = []
for name in territories:
    if len(set(territories[name])) == 1:
        print(name, ':', set(territories[name]))
        name_list.append(name)
