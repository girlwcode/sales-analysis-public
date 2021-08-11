
import os
import os.path
import pandas as pd

path = '../../resource/CrawlingData/'
detail_dir = ['clinic','fitness','hospital']
lenList=[]
total_csv =[]
for i in detail_dir:    #  파일 내에 있는 모든 csv파일명 가져옴
    file_list = os.listdir(path+i)
    file_list_py = [file for file in file_list if file.endswith('.csv')] ## 파일명 끝이 .csv인 경우
    # print(file_list_py)
    a=len(file_list_py)
    lenList.append(a)
    total_csv.append(file_list_py)
# print(total_csv)
# print(len(total_csv[2]))


# 1. 각 csv 파일 내 중복 , 더미데이터 제거
#clinic

print(total_csv[0])
for i in total_csv[0]:
    data_csv = pd.read_csv("../../resource/CrawlingData/clinic/" + i)
    new_data = data_csv.drop_duplicates(['Url'])  # 중복 제거
    # new_data = data_csv.dropna(subset=['Category', 'Address'], how='all')  # 더미데이터 제거
    print(i,"\tlength of raw data: ", len(data_csv), end='')
    print("\tlength of new data : ", len(new_data))


print(total_csv[1])
for j in total_csv[1]:
    data_csv = pd.read_csv("../../resource/CrawlingData/fitness/" + j)
    new_data = data_csv.drop_duplicates(['Url'])  # 중복 제거
    # new_data = data_csv.dropna(subset=['Category', 'Address'], how='all')  # 더미데이터 제거
    print(j,"\tlength of raw data: ", len(data_csv), end='')
    print("\tlength of new data : ", len(new_data))

print(total_csv[2])
for j in total_csv[2]:
    data_csv = pd.read_csv("../../resource/CrawlingData/hospital/" + j)
    new_data = data_csv.drop_duplicates(['Url'])  # 중복 제거
    # new_data = data_csv.dropna(subset=['Category', 'Address'], how='all')  # 더미데이터 제거
    print(j,"\tlength of raw data: ", len(data_csv), end='')
    print("\tlength of new data : ", len(new_data))

#2 카테고리 키워드 제거
drop_list_hos = ['eye', 'dental', 'animal', 'psychiatric', 'family', 'skin', 'hair', 'psychiatrist', 'ophthalmology', "road cycling", 'dentist'
              , 'dental','psychiatrist','parking','electronics','chiropractor','skin','hair','visa', 'derma','mental','freight','taxi','bus','watch',
              'industrial','phone','college','pharmacy','guest','car','insurance','solar','alternative','auto','labor', 'dental','community','box',
              'architecture','coffee','school','manufacturer','homeopath','printing','dairy','dry','grocery','photo','education center','phone','bank',
              'linen','corporate office','motor','baby store','criminal','statue','herbal medicine','furniture','marrage','appliance store','costume',
              'publisher','telecommunicatons','garden','familypractice','railway','video arcade','panipury', 'tourist attraction', 'secondary','seal shop',
              'store','government office','veterinarian']

drop_list_clinic = ['skin care' ,'dermatology','hair transplantation','dental','eye','beauty salon','veterinarian','animal','veterinary','alternative',
              'pet','dentist','school','state government office','computer service','community health','psychologist','homeopath','shopping mall',
              'environmental health service','lawyer','car leasing','lasik','park','dermatologist','parking garage','church','bank','hotel',
              'water purification','dairy store','gas comapny','news','restaurant','plastic surgeon', 'non-profit organization','orthodontist',
              'optician','sexologist','drug store','speech','oral','car repair','therapy clinic','day care center','tour','radiologist','pharmacy',
              'hair removal','caterer','corporate','library','general store','lodging']

drop_list_fit = ['martial arts school','exercise equipment store','business center','fitness equipment','supplements','trainer','make-up','dance',
              'grocery store','recruiting','repair service','instructor','butcher shop','meditation center','sports nutrition','university',
              'health and beauty','design','wellness center','store','oxygen cocktail','manufacturer','park', 'fencing', 'consultant',
              'energy equipment','educational institution','playground','tempororily','religious institution' ]

for j in total_csv[0]:
    data_csv = pd.read_csv("../../resource/CrawlingData/clinic/" + j)
    df = pd.DataFrame(data_csv, columns=['Category'])
    df['Category'] = df['Category'].str.lower()
    idx = data_csv[data_csv['Category'] == item].index
    data_csv = data_csv.drop(idx)
    print(len(new_data), end='    ')
