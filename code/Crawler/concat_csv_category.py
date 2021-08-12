import pandas as pd
import os


origin_dir = '../../resource/GeocodingData/'
details = ['Clinic', 'Fitness', 'Hospital']

# 카테고리 별로 데이터 concat
for detail in details:
    df_list = []
    for csv_data in os.listdir(origin_dir+detail):
        data = pd.read_csv(origin_dir + detail + '/' + csv_data)
        df_list.append(data)
    full_data = pd.concat(df_list, ignore_index=True)
    print(detail, ': before', len(full_data), sep="", end='\t')
    full_data = full_data.drop_duplicates(['Url'])
    print('after', len(full_data), sep="")
    # 데이터 저장
    full_data.to_csv(origin_dir+'/merge/'+detail+'_final.csv', index=False)

# before 2243	after 2228
# before 5579	after 5172
# before 2762	after 2729


# already_installed 삭제
installed = pd.read_csv('')

for csv_data in os.listdir(origin_dir+'merge/'):
    data = pd.read_csv(origin_dir+'merge/'+csv_data)





'''
# Clinic + Hospital
url_list = []
for detail in details:
    if detail == 'Clinic' or detail == 'Hospital':
        for csv_data in os.listdir(origin_dir + detail):
            data = pd.read_csv(origin_dir + detail + '/' + csv_data)
            url_list.extend(data['Url'].to_list())

print('before', len(url_list), end='\t')
url_list = list(set(url_list))
print('after', len(url_list))

# before 6059	after 5162
'''