import pandas as pd
import os

data_dir = '../../resource/GeocodingData/Territory_category(uninstalled)/'

terri_dict = {
    'east': ['West Bengal', 'Assam', 'Tripura', 'Sikkim', 'Manipur', 'Nagaland', 'Arunachal Pradesh', 'Mizoram'],
    'west1': ['Maharashtra', 'Goa'],
    'west2': ['Gujarat', 'Rajasthan', 'Madhya Pradesh'],
    'north': ['Uttar Pradesh', 'Delhi', 'Haryana', 'Punjab', 'Uttarakhand', 'Himachal Pradesh', 'Jammu and Kashmir',
              'Chandigarh', 'Meghalaya'],
    'south': ['Tamil Nadu', 'Karnataka', 'Andhra Pradesh', 'Telangana', 'Kerala', 'Puducherry']}

clinic_north = pd.read_csv(data_dir+'north_clinic_uninstalled.csv')
fitness_north = pd.read_csv(data_dir+'north_fitness_uninstalled.csv')
hospital_north = pd.read_csv(data_dir+'north_hospital_uninstalled.csv')

clinic_west2 = pd.read_csv(data_dir+'west2_clinic_uninstalled.csv')
fitness_west2 = pd.read_csv(data_dir+'west2_fitness_uninstalled.csv')
hospital_west2 = pd.read_csv(data_dir+'west2_hospital_uninstalled.csv')

clinic_east = pd.read_csv(data_dir+'east_clinic_uninstalled.csv')
fitness_east = pd.read_csv(data_dir+'east_fitness_uninstalled.csv')
hospital_east = pd.read_csv(data_dir+'east_hospital_uninstalled.csv')

clinic_south = pd.read_csv(data_dir+'south_clinic_uninstalled.csv')
fitness_south = pd.read_csv(data_dir+'south_fitness_uninstalled.csv')
hospital_south = pd.read_csv(data_dir+'south_hospital_uninstalled.csv')

clinic_west1 = pd.read_csv(data_dir+'west1_clinic_uninstalled.csv')
fitness_west1 = pd.read_csv(data_dir+'west1_fitness_uninstalled.csv')
hospital_west1 = pd.read_csv(data_dir+'west1_hospital_uninstalled.csv')


## east: 방글라데시/차이나 삭제
'''
idx_list = clinic_east[clinic_east['Address'].str.contains('Bangladesh|China')].index.tolist()
clinic_east = clinic_east.drop(idx_list, axis=0)

idx_list = fitness_east[fitness_east['Address'].str.contains('Bangladesh|China')].index.tolist()
fitness_east = fitness_east.drop(idx_list, axis=0)

idx_list = hospital_east[hospital_east['Address'].str.contains('Bangladesh|China')].index.tolist()
hospital_east = hospital_east.drop(idx_list, axis=0)

clinic_east.to_csv(data_dir+'east_clinic_uninstalled.csv', index=False)
fitness_east.to_csv(data_dir+'east_fitness_uninstalled.csv', index=False)
hospital_east.to_csv(data_dir+'east_hospital_uninstalled.csv', index=False)
'''

## south: Maharashtra west1로 이동
'''
idx_list = clinic_south[clinic_south['Address'].str.contains('Maharashtra')].index.tolist()
clinic_south.at[idx_list, 'State'] = 'Maharashtra'
clinic_west1 = clinic_west1.append(clinic_south.iloc[idx_list])
clinic_south = clinic_south.drop(idx_list, axis=0)

idx_list = fitness_south[fitness_south['Address'].str.contains('Maharashtra')].index.tolist()
fitness_south.at[idx_list, 'State'] = 'Maharashtra'
fitness_west1 = fitness_west1.append(fitness_south.iloc[idx_list])
fitness_south = fitness_south.drop(idx_list, axis=0)
'
idx_list = hospital_south[hospital_south['Address'].str.contains('Maharashtra')].index.tolist()
hospital_south.at[idx_list, 'State'] = 'Maharashtra'
hospital_west1 = hospital_west1.append(hospital_south.iloc[idx_list])
hospital_south = hospital_south.drop(idx_list, axis=0)

clinic_south.to_csv(data_dir+'south_clinic_uninstalled.csv', index=False)
fitness_south.to_csv(data_dir+'south_fitness_uninstalled.csv', index=False)
hospital_south.to_csv(data_dir+'south_hospital_uninstalled.csv', index=False)
clinic_west1.to_csv(data_dir+'west1_clinic_uninstalled.csv', index=False)
fitness_west1.to_csv(data_dir+'west1_fitness_uninstalled.csv', index=False)
hospital_west1.to_csv(data_dir+'west1_hospital_uninstalled.csv', index=False)
'''

## north: 방글라데시 삭제 + Rajasthan west2로 이동
'''
idx_list = clinic_north[clinic_north['Address'].str.contains('Bangladesh')].index.tolist()
clinic_north = clinic_north.drop(idx_list, axis=0)
idx_list = fitness_north[fitness_north['Address'].str.contains('Bangladesh')].index.tolist()
fitness_north = fitness_north.drop(idx_list, axis=0)
idx_list = hospital_north[hospital_north['Address'].str.contains('Bangladesh')].index.tolist()
hospital_north = hospital_north.drop(idx_list, axis=0)

idx_list = clinic_north[clinic_north['Address'].str.contains('Rajasthan')].index.tolist()
clinic_north.at[idx_list, 'State'] = 'Rajasthan'
clinic_west2 = clinic_west2.append(clinic_north.iloc[idx_list])
clinic_north = clinic_north.drop(idx_list, axis=0)

idx_list = hospital_north[hospital_north['Address'].str.contains('Rajasthan')].index.tolist()
hospital_north.at[idx_list, 'State'] = 'Rajasthan'
hospital_west2 = hospital_west2.append(hospital_north.iloc[idx_list])
hospital_north = hospital_north.drop(idx_list, axis=0)

idx_list = fitness_north[fitness_north['Address'].str.contains('Rajasthan')].index.tolist()
fitness_north.at[idx_list, 'State'] = 'Rajasthan'
fitness_west2 = fitness_west2.append(fitness_north.iloc[idx_list])
fitness_north = fitness_north.drop(idx_list, axis=0)

clinic_north.to_csv(data_dir+'north_clinic_uninstalled.csv', index=False)
fitness_north.to_csv(data_dir+'north_fitness_uninstalled.csv', index=False)
hospital_north.to_csv(data_dir+'north_hospital_uninstalled.csv', index=False)
clinic_west2.to_csv(data_dir+'west2_clinic_uninstalled.csv', index=False)
fitness_west2.to_csv(data_dir+'west2_fitness_uninstalled.csv', index=False)
hospital_west2.to_csv(data_dir+'west2_hospital_uninstalled.csv', index=False)
'''

# west1: Karnataka, Telangana south로 이동
'''
idx_list = clinic_west1[clinic_west1['Address'].str.contains('Karnataka')].index.tolist()
clinic_west1.at[idx_list, 'State'] = 'Karnataka'
clinic_south = clinic_south.append(clinic_west1.iloc[idx_list])
clinic_west1 = clinic_west1.drop(idx_list, axis=0)

idx_list = fitness_west1[fitness_west1['Address'].str.contains('Karnataka')].index.tolist()
fitness_west1.at[idx_list, 'State'] = 'Karnataka'
fitness_south = fitness_south.append(fitness_west1.iloc[idx_list])
fitness_west1 = fitness_west1.drop(idx_list, axis=0)

idx_list = hospital_west1[hospital_west1['Address'].str.contains('Karnataka')].index.tolist()
hospital_west1.at[idx_list, 'State'] = 'Karnataka'
hospital_south = hospital_south.append(hospital_west1.iloc[idx_list])
hospital_west1 = hospital_west1.drop(idx_list, axis=0)

idx_list = clinic_west1[clinic_west1['Address'].str.contains('Telangana')].index.tolist()
clinic_west1.at[idx_list, 'State'] = 'Telangana'
clinic_south = clinic_south.append(clinic_west1.iloc[idx_list])
clinic_west1 = clinic_west1.drop(idx_list, axis=0)

idx_list = fitness_west1[fitness_west1['Address'].str.contains('Telangana')].index.tolist()
fitness_west1.at[idx_list, 'State'] = 'Telangana'
fitness_south = fitness_south.append(fitness_west1.iloc[idx_list])
fitness_west1 = fitness_west1.drop(idx_list, axis=0)

idx_list = hospital_west1[hospital_west1['Address'].str.contains('Telangana')].index.tolist()
hospital_west1.at[idx_list, 'State'] = 'Telangana'
hospital_south = hospital_south.append(hospital_west1.iloc[idx_list])
hospital_west1 = hospital_west1.drop(idx_list, axis=0)

clinic_south.to_csv(data_dir+'south_clinic_uninstalled.csv', index=False)
fitness_south.to_csv(data_dir+'south_fitness_uninstalled.csv', index=False)
hospital_south.to_csv(data_dir+'south_hospital_uninstalled.csv', index=False)
clinic_west1.to_csv(data_dir+'west1_clinic_uninstalled.csv', index=False)
fitness_west1.to_csv(data_dir+'west1_fitness_uninstalled.csv', index=False)
hospital_west1.to_csv(data_dir+'west1_hospital_uninstalled.csv', index=False)
'''

## west2: Uttar Pradesh north로 이동 + Maharashtra west1으로 이동
'''
idx_list = clinic_west2[clinic_west2['Address'].str.contains('Uttar Pradesh')].index.tolist()
clinic_west2.at[idx_list, 'State'] = 'Uttar Pradesh'
clinic_north = clinic_north.append(clinic_west2.iloc[idx_list])
clinic_west2 = clinic_west2.drop(idx_list, axis=0)

idx_list = fitness_west2[fitness_west2['Address'].str.contains('Uttar Pradesh')].index.tolist()
fitness_west2.at[idx_list, 'State'] = 'Uttar Pradesh'
fitness_north = fitness_north.append(fitness_west2.iloc[idx_list])
fitness_west2 = fitness_west2.drop(idx_list, axis=0)

idx_list = hospital_west2[hospital_west2['Address'].str.contains('Uttar Pradesh')].index.tolist()
hospital_west2.at[idx_list, 'State'] = 'Uttar Pradesh'
hospital_north = hospital_north.append(hospital_west2.iloc[idx_list])
hospital_west2 = hospital_west2.drop(idx_list, axis=0)

idx_list = clinic_west2[clinic_west2['Address'].str.contains('Uttar Pradesh')].index.tolist()
clinic_west2.at[idx_list, 'State'] = 'Uttar Pradesh'
clinic_west1 = clinic_west1.append(clinic_west2.iloc[idx_list])
clinic_west2 = clinic_west2.drop(idx_list, axis=0)

idx_list = fitness_west2[fitness_west2['Address'].str.contains('Maharashtra')].index.tolist()
fitness_west2.at[idx_list, 'State'] = 'Maharashtra'
fitness_west1 = fitness_west1.append(fitness_west2.iloc[idx_list])
fitness_west2 = fitness_west2.drop(idx_list, axis=0)

idx_list = hospital_west2[hospital_west2['Address'].str.contains('Maharashtra')].index.tolist()
hospital_west2.at[idx_list, 'State'] = 'Maharashtra'
hospital_west1 = hospital_west1.append(hospital_west2.iloc[idx_list])
hospital_west2 = hospital_west2.drop(idx_list, axis=0)

clinic_north.to_csv(data_dir+'north_clinic_uninstalled.csv', index=False)
fitness_north.to_csv(data_dir+'north_fitness_uninstalled.csv', index=False)
hospital_north.to_csv(data_dir+'north_hospital_uninstalled.csv', index=False)
clinic_west1.to_csv(data_dir+'west1_clinic_uninstalled.csv', index=False)
fitness_west1.to_csv(data_dir+'west1_fitness_uninstalled.csv', index=False)
hospital_west1.to_csv(data_dir+'west1_hospital_uninstalled.csv', index=False)
clinic_west2.to_csv(data_dir+'west2_clinic_uninstalled.csv', index=False)
fitness_west2.to_csv(data_dir+'west2_fitness_uninstalled.csv', index=False)
hospital_west2.to_csv(data_dir+'west2_hospital_uninstalled.csv', index=False)
'''

# csv에 territory column 추가
# concat Final
# 카테고리 별로 데이터 concat
'''
for csv_data in os.listdir(data_dir):
    data = pd.read_csv(data_dir + csv_data)
    if 'east' in csv_data:
        data['Territory'] = 'East'
    elif 'north' in csv_data:
        data['Territory'] = 'North'
    elif 'south' in csv_data:
        data['Territory'] = 'South'
    elif 'west1' in csv_data:
        data['Territory'] = 'West 1'
    elif 'west2' in csv_data:
        data['Territory'] = 'West 2'
    data.to_csv(data_dir+csv_data, index=False)


clinic_list = []
fitness_list = []
hospital_list = []
for csv_data in os.listdir(data_dir):
    if 'clinic' in csv_data:
        clinic_list.append(pd.read_csv(data_dir+csv_data))
    elif 'fitness' in csv_data:
        fitness_list.append(pd.read_csv(data_dir+csv_data))
    elif 'hospital' in csv_data:
        hospital_list.append(pd.read_csv(data_dir+csv_data))

full_clinic = pd.concat(clinic_list, ignore_index=True)
full_fitness = pd.concat(fitness_list, ignore_index=True)
full_hospital = pd.concat(hospital_list, ignore_index=True)

full_clinic = full_clinic.dropna(axis=0)
idx_list = full_clinic[full_clinic['State'].str.contains('http')].index.to_list()
full_clinic = full_clinic.drop(idx_list, axis=0)

full_hospital = full_hospital.dropna(axis=0)

# 데이터 저장
google_dir = '../../resource/GeocodingData/merge/'
# full_clinic.to_csv(google_dir+'Clinic_final2.csv', index=False)
# full_fitness.to_csv(google_dir+'Fitness_final2.csv', index=False)
full_hospital.to_csv(google_dir+'Hospital_final2.csv', index=False)
'''

full_hospital = pd.read_csv('../../resource/GeocodingData/merge/Hospital_final2.csv')
# idx_list = full_hospital[full_hospital['State'].str.contains('Thaltej')].index.to_list()
# full_hospital = full_hospital.drop(idx_list, axis=0)
# full_hospital.to_csv('../../resource/GeocodingData/merge/Hospital_final2.csv', index=False)
print(len(full_hospital['State'].unique()))