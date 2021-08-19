import pandas as pd
import os

data_dir = '../../resource/GoogleTrends/Parsing/'
details = ['2016/', '2017/', '2018/', '2019/', '2020/', '2021/']

monthly_mean = pd.DataFrame(columns=['Date', 'Interest Level'])
for detail in details:
    for csv_data in os.listdir(data_dir+detail):
        data_dict = dict.fromkeys(['Date', 'Interest Level'])  # date, mean의 곱 저장할 dict
        # 칼럼명 변경
        data = pd.read_csv(data_dir + detail + csv_data, encoding='cp949')
        data.columns = ['Date', 'BMI', 'Muscle', 'Weight Loss', 'Gym', 'Body Mass']

        # 리스트에 date 추가
        data['Date'] = pd.to_datetime(data['Date'])
        year, month = data['Date'].dt.year, data['Date'].dt.month
        data_dict['Date'] = str(year[0])+'-'+str(month[0])
        
        # 리스트에 mean의 곱 추가
        mean_multi = 1
        for col in data.columns:
            if col == 'Date':
                continue
            idx_list = data[data[col].astype('str').str.contains('<')].index.tolist()
            data.at[idx_list, col] = 0
            data = data.astype({col: 'int'})

            m = data[col].mean()
            mean_multi *= m
        # mean_multi *= 100
        data_dict['Interest Level'] = mean_multi
        print(data_dict)
        # 최종 데이터프레임에 리스트 추가
        monthly_mean = monthly_mean.append(data_dict, ignore_index=True)

monthly_mean.to_csv('../../resource/GoogleTrends/google_trends_monthly_mean.csv', index=False)