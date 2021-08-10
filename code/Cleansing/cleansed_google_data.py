import os
import pandas as pd

path = '../../resource/CrawlingData/'
details = ['hospital/', 'clinic/', 'fitness/']

# 1. 각 csv 파일 내 중복 제거
for detail in details:
    full_path = path+detail
    csv_list = os.listdir(full_path)
    for data in csv_list:
        raw_data = pd.read_csv(data)
        print(data, 'raw데이터 수:', len(raw_data))
        new_data = raw_data.drop_duplicates(['Url'])
        print('\t수정 데이터 수:', len(new_data))


# 2. 안맞는 카테고리 제거 + 더미데이터(주소/카테고리:null) 제거
# hospital(animal, eye)
hospital_list = os.listdir(path+details[0])
for data in hospital_list:
    hospital = pd.read_csv(data)

# clinic()
clinic_list = os.listdir(path+details[1])
for data in clinic_list:
    clinic = pd.read_csv(data)

# fitness(equipment? store? )
fitness_list = os.listdir(path+details[2])
for data in fitness_list:
    fitness = pd.read_csv(data)
