import pandas as pd
import os

data_dir = '../../resource/GoogleTrends/Parsing/'
details = ['2016/', '2017/', '2018/', '2019/', '2020/', '2021/']

monthly_mean = pd.DataFrame(columns=['Date', 'BMI', 'Muscle', 'Weight Loss', 'Gym', 'Body Mass'])
for detail in details:
    for csv_data in os.listdir(data_dir+detail):
        data_list = []  # date, mean 저장할 리스트
        # 칼럼명 변경
        data = pd.read_csv(data_dir + detail + csv_data)
        data.columns = ['Date', 'BMI', 'Muscle', 'Weight Loss', 'Gym', 'Body Mass']

        # 리스트에 date 추가
        data['Date'] = pd.to_datetime(data['Date'])
        year, month = data['Date'].dt.year, data['Date'].dt.month
        data_list.append(str(year)+'-'+str(month))
        
        # 리스트에 mean 추가

        for col in data.columns:
            if col == 'Date':
                continue
            idx_list = data[data[col].astype(str).str.contains('<')].index.tolist()
            data.at[idx_list, col] = 0
            data[col].astype('float')
            print(data[col].dtype)
            data_list.append(data[col].mean())

        # 최종 데이터프레임에 리스트 추가
        monthly_mean.append(pd.Series(data_list), ignore_index=True)

monthly_mean.to_csv('../../resource/GoogleTrends/google_trends_monthly_mean.csv', index=False)