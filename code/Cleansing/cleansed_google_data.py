import os
import os.path
import pandas as pd

path = r'../../CrawlingData/'
details = ['hospital/', 'clinic/', 'fitness/']

# 1. 각 csv 파일 내 중복 제거
for detail in details:
    full_path = path+detail
    csv_list = os.listdir(full_path)
    for data in csv_list:
        raw_data = pd.read_csv(data)
        print('raw데이터 수:', len(raw_data))
        new_data = raw_data.drop_duplicates(['Url'])   #url이 중복 발견의 기준
        print('수정 데이터 수:', len(new_data))


# 2. 안맞는 카테고리 제거 + 더미데이터(url&카테고리:null) 제거;
# hospital(animal, eye)
hospital_list = os.listdir(path+details[0])



# clinic()
clinic_list = os.listdir(path+details[1])
for csv_data in clinic_list:
    clinic = pd.read_csv(csv_data)
    for idx in clinic['Category']:
        idx = clinic[clinic['Category'] == 'Hair' or 'Eye' or 'Dental','Beauty' or 'Counselor' or 'Animal' or
        'pet' or 'Dentist' or 'mall' or 'Hotel'].index
        clinic.drop(idx, inplace=True)
        idx = clinic[clinic['Category'] == 'Family' or 'Dermatolo' or 'pediatrician' or 'Hair' or ''
        rowth2 = rowth2.extend(idx)

# fitness(equipment? store? )
fitness_list = os.listdir(path+details[2])
for csv_data in fitness_list:
    fitness = pd.read_csv(csv_data)
