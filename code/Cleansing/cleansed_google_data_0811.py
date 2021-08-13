
import os.path
import pandas as pd
import re

path = '../../resource/CrawlingData/'
detail_dir = ['clinic','fitness','hospital']
lenList=[]
total_csv =[]
for i in detail_dir:    #  파일 내에 있는 모든 csv파일명 가져옴
    file_list = os.listdir(path+i)
    file_list_py = [re.sub(".csv","",file) for file in file_list if file.endswith('.csv')] ## 파일명 끝이 .csv인 경우
    # print(file_list_py)
    a=len(file_list_py)
    lenList.append(a)
    total_csv.append(file_list_py)
# print(lenList)


# 1. 각 csv 파일 내 중복 , 더미데이터 제거
#clinic
new_clinic = list()
print(total_csv[0])
for i in total_csv[0]:
    data_csv = pd.read_csv("../../resource/CrawlingData/clinic/" + i+'.csv')
    print(i,"\tlength of raw data: ", len(data_csv), end='')
    data_csv = data_csv.drop_duplicates(['Url'])  # 중복 제거
    data_csv = data_csv.dropna(axis=0)

    print("\tlength of new data : ", len(data_csv))
    data_csv = data_csv.reset_index(drop=True)
    new_clinic.append(data_csv)


# Fitness
new_fitness = list()
print(total_csv[1])
for j in total_csv[1]:
    data_csv = pd.read_csv("../../resource/CrawlingData/fitness/" + j+'.csv')
    print(j, "\tlength of raw data: ", len(data_csv), end='')
    data_csv = data_csv.drop_duplicates(['Url'])  # 중복 제거
    data_csv = data_csv.dropna(axis=0)
    print("\tlength of new data : ", len(data_csv))
    data_csv = data_csv.reset_index(drop=True)
    new_fitness.append(data_csv)

# Hospital
new_hospital = list()
print(total_csv[2])
for j in total_csv[2]:
    data_csv = pd.read_csv("../../resource/CrawlingData/hospital/" + j+'.csv')
    print(j, "\tlength of raw data: ", len(data_csv), end='')
    data_csv = data_csv.drop_duplicates(['Url'])  # 중복 제거

    data_csv = data_csv.dropna(axis = 0)
    print("\tlength of new data : ", len(data_csv))
    data_csv = data_csv.reset_index(drop=True)
    new_hospital.append(data_csv)

#2 카테고리 키워드 제거
drop_list_hos = ['eye', 'dental', 'animal', 'psychiatric', 'family', 'skin', 'hair', 'psychiatrist', 'ophthalmology', "road cycling", 'dentist'
              , 'dental','psychiatrist','parking','electronics','chiropractor','skin','hair','visa', 'derma','mental','freight','taxi','bus','watch',
              'industrial','phone','college','pharmacy','guest','car','insurance','solar','alternative','auto','labor', 'dental','community','box',
              'architecture','coffee','school','manufacturer','homeopath','printing','dairy','dry','grocery','photo','education center','phone','bank',
              'linen','corporate office','motor','baby store','criminal','statue','herbal medicine','furniture','marrage','appliance store','costume',
              'publisher','telecommunicatons','garden','familypractice','railway','video arcade','panipury', 'tourist attraction', 'secondary','seal shop',
              'store','government office','veterinarian', 'contractor','apartment building','charity','biotechnology company','maarage','clothing',
              'telecommunication','employment agency','ophthalmologist','university','back office','anesthesiologist','advertising','sports association',
              'transit deposit', 'housing', 'mosque', 'lodging', 'educational institution', 'milk delivery service','worship', 'playground', 'villa',
              'free clinic','accountant', 'drinking water','hostel','human resource','home builder','interchange','stationery','atm'
              'florist','fashion',  'function','post office','social services','ATM','district office','agriculture','state','historical',
              'non-profit','tractor','association','army','computer', 'sculptor','sexologist','sports medicine','occupational','auditorium','foundation',
              'dormitory','subway','optician','food court','air filter',  'internal medicine','consultant','florist','shopping','library','research',
              'indian restaurant','gas station','interior','recruiter','passport','ice cream','restaurant','media','bed','copper supplier','stock',
              'winery','beauty salon','fast food','radio broadcaster','hotel','bazar','closed','services', 'ambulance service','religious','ground self','train',
              'clubhouse','temple','organic shop','general practitioner','website designer','marketing agency','gas station', 'ethnic restaurant','church','market',
              'police station','fire','bakery','park', 'hiv testing','food','gas shop','milwork','convention','marriage','fitness equipment', 'transit station','park',
              'software', 'astrologer','night club','e-commerce','plastic surgeon','homestay','bar','tattoo shop','architect','tourist information','bathroom','tire shop','travel','court',
              'cafeteria', 'water treatment', 'water damage', 'gps', 'condominium complex', 'news','safety',"sheriff",'mining','coaching','wellness','transit','emergency','dried flower',
              'board of education','zoo', 'gaon','equipment','internet cafe','wedding','cleaning','500 error','racecourse','goods','online','atm',
               'company','thera','service','agency','printer','shop','department','referral','tour','caterer','fabricator','tattoo']

drop_list_clinic = ['skin care' ,'dermatology','hair transplantation','dental','eye','beauty salon','veterinarian','animal','veterinary','alternative',
              'pet','dentist','school','state government office','computer service','community health','psychologist','homeopath','shopping mall',
              'environmental health service','lawyer','car leasing','lasik','park','dermatologist','parking garage','church','bank','hotel',
              'water purification','dairy store','gas comapny','news','restaurant','plastic surgeon', 'non-profit organization','orthodontist',
              'optician','sexologist','drug store','speech','oral','car repair','day care center','tour','radiologist','pharmacy',
              'hair removal','caterer','corporate','library','general store','lodging','atm', 'psychiatrist','infectious','chiropractor',
              'drug testing','nutritionist','testing service','hair replacement','hair salon','abortion clinic','hearing aid',
              'camera store','computer store','chauffeur service','industrial area','abhilasha business','family planning','software',
              'courier service','oil change','ambulance','bathroom','post office','jewelry','life insurance','baby store','interior',
              'mental health','holiday','emergency room','laboratory','dormitory','college','transit','association','insurance','walk',
              'native american','consultant','laboratory','university','call center','equipment','bus','gift','repair','bar','gas', 'winery',
              'fabric','broadcaster','clothing','dar dealer','family','educational','psychiatric','travel','marriage','lounge','heritage',
              'database','home health','research','sweet','acupuncture','back office','employment','appliance','electronics', 'herbalist','legal',
              'agricultural','hiv','housing','apartment','student','historical','market','police','city or town','lodge', 'ear piercing','hiv',
              'assistant','health food','cosmetics','playground','garden','shoe', 'watch store','optical','seed', 'referral','farm', 'internet marketing',
              'dharamashala','manufacturer','grocery',  'night club','spa','e-commerce','homestay','government office','pharmaceutical company',
              'plastic surgery','products','manu_dhumachharra','spa','condominium','mosque','medicine clinic','agricultural','foundation','temple',
              '500 error', 'neonatal', 'american football', 'construction','atm','car dealer','cafeteria','agriculture cooperative','club',
                'attorney','counselor','community center','council','district office','event', 'e park','gym','forwarding','shop','loan','media',
                'yoga','estate','station','tattoo','stock','store','investment','make-up']

drop_list_fit = ['martial arts','exercise equipment store','business center','fitness equipment','supplements','trainer','make-up','dance',
              'grocery store','recruiting','repair service','instructor','butcher shop','meditation center','sports nutrition','university',
              'health and beauty','design','wellness center','store','oxygen cocktail','manufacturer','park', 'fencing', 'consultant',
              'energy equipment','educational institution','playground','tempororily','religious institution', 'addiction','nutritionist','beauty',
              'equipment rental agency', 'corporate', 'charter', 'gift', 'sports accessories', 'physical therapist','hotel', 'art school','software',
              'water softening','therapy','spa','news','federal','government office','sports association','basketball court','unemployment school',
              'vocational school','information','tai chi','back office','wellness','warehouse','construciton','wing','temple','supplier','distribution service'
              ,'homestay','home','association','indoor swimming','non-governmental', 'lodging','exporter','wholesaler', 'school','vehicle','garden',
              'recreation center','court','self defense','location','stadium','biotechnology','shopping','motorcycle', 'radhanagar','pharmacy',
              'education','e-commerce','hospital',  'temporarily', 'studying center','atm','doctor','importer','club','company','room','authority',
              'restaurant','foundation']


# Clinic
print('-----------CLINIC------------')
cnt = 0
for data in new_clinic:
    row_list = []
    print('Before: ',len(data), end='\t')
    for row in data.index:
        category = str(data['Category'][row]).lower()
        company_name = str(data['Company_Name'][row]).lower()
        for l in drop_list_clinic:
            if l in category or l in company_name:
                row_list.append(row)
    data = data.drop(index=row_list, axis=0)
    print('After:', len(data))
    data.to_csv('../../resource/CleansedData/GoogleMap/Clinic/'+total_csv[0][cnt]+'_cleansed.csv',index=False)
    cnt += 1


# Fitness
print('-----------FITNESS------------')
cnt = 0
for data in new_fitness:
    row_list = []
    print('Before: ',len(data), end='\t')
    for row in data.index:
        category = str(data['Category'][row]).lower()
        company_name = str(data['Company_Name'][row]).lower()
        for l in drop_list_fit:
            if l in category or l in company_name:
                row_list.append(row)
    data = data.drop(index=row_list, axis=0)
    print('After:', len(data))
    data.to_csv('../../resource/CleansedData/GoogleMap/Fitness/' + total_csv[1][cnt]+'_cleansed.csv', index=False)
    cnt += 1


# Hospital
print('-----------HOSPITAL------------')
cnt = 0
for data in new_hospital:
    row_list = []
    print('Before: ',len(data), end='\t')
    for row in data.index:
        category = str(data['Category'][row]).lower()
        company_name = str(data['Company_Name'][row]).lower()
        for l in drop_list_hos:
            if l in category or l in company_name:
                row_list.append(row)
    data = data.drop(index=row_list, axis=0)
    print('After:', len(data))
    data.to_csv('../../resource/CleansedData/GoogleMap/Hospital/' + total_csv[2][cnt]+'_cleansed.csv', index=False)
    cnt += 1
