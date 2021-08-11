import os
import pandas as pd

path = '../../resource/CrawlingData/'
parsing_path = path + 'Parsing/'
details = ['hospital/', 'clinic/', 'fitness/']

drop_list1 = ['eye', 'dental', 'animal', 'psychiatric', 'family', 'skin', 'hair', 'psychiatrist', 'ophthalmology', "road cycling", 'dentist'
              , 'dental','psychiatrist','parking','electronics','chiropractor','skin','hair','visa', 'derma','mental','freight','taxi','bus','watch',
              'industrial','phone','college','pharmacy','guest','car','insurance','solar','alternative','auto','labor', 'dental','community','box',
              'architecture','coffee','school','manufacturer','homeopath','printing','dairy','dry','grocery','photo','education center','phone','bank',
              'linen','corporate office','motor','baby store','criminal','statue','herbal medicine','furniture','marrage','appliance store','costume',
              'publisher','telecommunicatons','garden','familypractice','railway','video arcade','panipury','tourist attraction','secondary','seal shop',
              'store','government office','veterinarian']

drop_list2 = ['skin care' ,'dermatology','hair transplantation','dental','eye','beauty salon','veterinarian','animal','veterinary','alternative',
              'pet','dentist','school','state government office','computer service','community health','psychologist','homeopath','shopping mall',
              'environmental health service','lawyer','car leasing','lasik','park','dermatologist','parking garage','church','bank','hotel',
              'water purification','dairy store','gas comapny','news','restaurant','plastic surgeon', 'non-profit organization','orthodontist',
              'optician','sexologist','drug store','speech','oral','car repair','therapy clinic','day care center','tour','radiologist','pharmacy',
              'hair removal','caterer','corporate','library','general store','lodging']

drop_list3 = ['martial arts school','exercise equipment store','business center','fitness equipment','supplements','trainer','make-up','dance',
              'grocery store','recruiting','repair service','instructor','butcher shop','meditation center','sports nutrition','university',
              'health and beauty','design','wellness center','store','oxygen cocktail','manufacturer','park', 'fencing', 'consultant',
              'energy equipment','educational institution','playground','tempororily','religious institution'    ]

# 1. 각 csv 파일 내 중복 제거 + 더미데이터(주소+카테고리:null) 제거
for detail in details:
    full_path = path + detail
    csv_list = os.listdir(full_path)
    for data in csv_list:
        print(data)
        # filename = os.path.basename(data)
        raw_data = pd.read_csv(data)
        print(data, 'raw데이터 수:', len(raw_data))
        new_data = raw_data.drop_duplicates(['Url'])
        new_data = raw_data.dropna(subset=['Category', 'Address'], how="all")
        print('\t수정데이터 수:', len(new_data))
        # new_data.to_csv(parsing_path+filename, index=False)

# 2. 안맞는 카테고리 제거
# hospital
# save_dir = '../resource/poppedData'
# hospital_list = os.listdir(parsing_path + details[0])
# for data in hospital_list:
#     hospital = pd.read_csv(data)
#     for i in hospital.index:
#         category = hospital['Category'][i].lower()
#         for drop in drop_list1:
#             if drop in category:
#                 hospital = hospital.drop(i, axis=0)
#                 save_hospt = hospital.to_csv(save_dir, index=False)
#
#

# # clinic
# clinic_list = os.listdir(parsing_path + details[1])
# for data in clinic_list:
#     clinic = pd.read_csv(data)
#     for i in clinic.index:
#         category = clinic['Category'][i].lower()
#         for drop in drop_list2:
#             if drop in category:
#                 hospital = hospital.drop(i, axis=0)
#
# # fitness
# fitness_list = os.listdir(parsing_path + details[2])
# for data in fitness_list:
#     fitness = pd.read_csv(data)
#     for i in fitness.index:
#         category = fitness['Category'][i].lower()
#         for drop in drop_list3:
#             if drop in category:
#                 fitness = fitness.drop(i, axis=0)