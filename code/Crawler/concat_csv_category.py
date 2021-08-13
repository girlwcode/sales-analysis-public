import pandas as pd
import os

google_dir = '../../resource/GeocodingData/'
details = ['Clinic', 'Fitness', 'Hospital']
sales_dir = '../../resource/SalesData/'


clinic_assam = pd.read_csv('../../resource/GeocodingData/Clinic/clinic in Assam, India_cleansed_final.csv')
fitness_assam = pd.read_csv('../../resource/GeocodingData/Fitness/fitness in Assam, India_cleansed_final.csv')
hospital_assam = pd.read_csv('../../resource/GeocodingData/Hospital/hospital in Assam, India_cleansed_final.csv')

clinic_meg = pd.read_csv('../../resource/GeocodingData/Clinic/clinic in Meghalaya, India_cleansed_final.csv')
fitness_meg = pd.read_csv('../../resource/GeocodingData/Fitness/fitness in Meghalaya, India_cleansed_final.csv')
hospital_meg = pd.read_csv('../../resource/GeocodingData/Hospital/hospital in Meghalaya, India_cleansed_final.csv')

# assam, meg 후처리 - clinic
idx_list = clinic_meg[clinic_meg['Address'].str.contains('Assam')].index.tolist()
clinic_assam = clinic_assam.append(clinic_meg.iloc[idx_list])
clinic_meg = clinic_meg.drop(idx_list, axis=0)
clinic_meg['State'] = 'Meghalaya'
clinic_assam['State'] = 'Assam'

clinic_assam.to_csv('../../resource/GeocodingData/Clinic/clinic in Assam, India_cleansed_final.csv',index=False)
clinic_meg.to_csv('../../resource/GeocodingData/Clinic/clinic in Meghalaya, India_cleansed_final.csv',index=False)

# assam, meg 후처리 - Fitness
idx_list = fitness_meg[fitness_meg['Address'].str.contains('Assam')].index.tolist()
fitness_assam = fitness_assam.append(fitness_meg.iloc[idx_list])
fitness_meg = fitness_meg.drop(idx_list, axis=0)
fitness_meg['State'] = 'Meghalaya'
fitness_assam['State'] = 'Assam'

fitness_assam.to_csv('../../resource/GeocodingData/Fitness/fitness in Assam, India_cleansed_final.csv',index=False)
fitness_meg.to_csv('../../resource/GeocodingData/Fitness/fitness in Meghalaya, India_cleansed_final.csv',index=False)

# assam, meg 후처리 - Hospital
idx_list = hospital_meg[hospital_meg['Address'].str.contains('Assam')].index.tolist()
hospital_assam = hospital_assam.append(hospital_meg.iloc[idx_list])
hospital_meg = hospital_meg.drop(idx_list, axis=0)
hospital_meg['State'] = 'Meghalaya'
hospital_assam['State'] = 'Assam'

hospital_assam.to_csv('../../resource/GeocodingData/Hospital/hospital in Assam, India_cleansed_final.csv',index=False)
hospital_meg.to_csv('../../resource/GeocodingData/Hospital/hospital in Meghalaya, India_cleansed_final.csv',index=False)

# 카테고리 별로 데이터 concat
for detail in details:
    df_list = []
    for csv_data in os.listdir(google_dir + detail):
        data = pd.read_csv(google_dir + detail + '/' + csv_data)
        df_list.append(data)
    full_data = pd.concat(df_list, ignore_index=True)
    print(detail, ':\tbefore ', len(full_data), sep="", end='\t\t')
    full_data = full_data.drop_duplicates(['Url'])
    print('after ', len(full_data), sep="")
    # 데이터 저장
    full_data.to_csv(google_dir + '/merge/' + detail + '.csv', index=False)

# Clinic:	before 5748		after 5628
# Fitness:	before 5745		after 5360
# Hospital:	before 5815		after 5710


# Clinic + Hospital
url_list = []
for detail in details:
    if detail == 'Clinic' or detail == 'Hospital':
        for csv_data in os.listdir(google_dir + detail):
            data = pd.read_csv(google_dir + detail + '/' + csv_data)
            url_list.extend(data['Url'].to_list())

print('before', len(url_list), end='\t')
url_list = list(set(url_list))
print('after', len(url_list))

# before 11563	after 9337 (Clinic-Hospital 사이에 중복 존재)


''' ## 완료
# installed concat
df_list = []
for csv_data in os.listdir(sales_dir):
    if csv_data.startswith('Installation') and csv_data.endswith('.csv'):
        data = pd.read_csv(sales_dir+csv_data)
        new_data = data[['Client', 'City', 'State']]
        df_list.append(new_data)
installed = pd.concat(df_list, ignore_index=True)
installed = installed.drop_duplicates(['Client', 'City'])
installed.to_csv(sales_dir+'Installation_full.csv', index=False)
'''
